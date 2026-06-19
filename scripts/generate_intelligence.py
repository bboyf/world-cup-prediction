# -*- coding: utf-8 -*-
"""
使用 DeepSeek AI 生成格式化每日情报文本
用于 GitHub Actions 自动更新
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

class IntelligenceGenerator:
    """AI情报生成器"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY")
        
        if not self.api_key:
            raise ValueError("❌ 未设置 DeepSeek API Key")
        
        # 使用兼容的 OpenAI 客户端
        try:
            import openai
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url="https://api.deepseek.com/v1"
            )
        except ImportError:
            # 如果 openai 库不可用，使用 requests
            import requests
            self.client = None
            self.requests = requests
    
    def generate_daily_brief(self, football_data: Optional[Dict] = None) -> str:
        """生成每日情报文本"""
        
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 格式化足球数据
        if football_data is None:
            football_data = {"matches": [], "team_status": [], "injuries": [], "recent_results": []}
        
        matches_text = self._format_matches(football_data.get("matches", []))
        team_status_text = self._format_team_status(football_data.get("team_status", []))
        injuries_text = self._format_injuries(football_data.get("injuries", []))
        results_text = self._format_results(football_data.get("recent_results", []))
        
        # 构建提示词
        prompt = self._build_prompt(
            current_date,
            matches_text,
            team_status_text,
            injuries_text,
            results_text
        )
        
        # 调用 AI 生成
        try:
            if self.client:
                response = self._call_openai_api(prompt)
            else:
                response = self._call_requests_api(prompt)
            
            return response
        except Exception as e:
            print(f"❌ AI生成失败: {e}")
            return self._generate_fallback_intelligence(current_date, football_data)
    
    def _call_openai_api(self, prompt: str) -> str:
        """使用 OpenAI 库调用 API"""
        response = self.client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {
                    "role": "system",
                    "content": """你是一个专业的世界杯情报分析师，擅长整理和分析足球相关数据。
请严格按格式输出情报内容，不要添加任何解释或说明文字。
只输出情报文本本身，不要添加```markdown等标记。"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        result = response.choices[0].message.content.strip()
        return result
    
    def _call_requests_api(self, prompt: str) -> str:
        """使用 requests 直接调用 API"""
        import requests
        
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-v4-pro",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个专业的世界杯情报分析师，只输出情报文本，不要添加任何标记。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "max_tokens": 1000
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()["choices"][0]["message"]["content"].strip()
        return result
    
    def _build_prompt(self, current_date: str, matches: str, 
                      team_status: str, injuries: str, results: str) -> str:
        """构建 AI 提示词"""
        
        return f"""请根据以下足球数据，为2026世界杯生成规范的每日情报更新文本。

当前日期：{current_date}

【今日及近期比赛】
{matches if matches else "暂无比赛信息"}

【球队状态】
{team_status if team_status else "暂无球队状态更新"}

【伤病报告】
{injuries if injuries else "暂无伤病报告"}

【近期结果】
{results if results else "暂无近期比赛结果"}

请生成符合以下格式的情报文本：

---
## 六、最新情报（每日更新区）

> 本节由每日情报流程覆盖更新。**当本节与第四节冲突时，以本节为准**（本节更新）。

**情报日期：{current_date}**

### 今日/近期比赛
- 比赛列表（日期、时间、主队 vs 客队、场地）

### 球队状态更新
- 各队近期状态（如果有更新）

### 伤停信息
- 伤病情况（如果有）

### 重要备注
- 其他需要关注的信息

**优先级说明：** 当本节与第四节冲突时，以本节为准。

要求：
1. 日期使用 YYYY-MM-DD 格式
2. 球队名称使用中文全称
3. 简明扼要，突出关键信息
4. 如果某项没有数据，写"暂无更新"
5. 只输出情报内容，不要其他说明文字
"""

    def _format_matches(self, matches: list) -> str:
        """格式化比赛信息"""
        if not matches:
            return ""
        
        lines = []
        for match in matches[:10]:  # 最多显示10场
            date = match.get("date", "未知")
            time = match.get("time", "未知")
            home = match.get("home_team", "未知")
            away = match.get("away_team", "未知")
            stage = match.get("stage", "待定")
            venue = match.get("venue", "待定")
            
            lines.append(f"{date} {time} | {home} vs {away} [{stage}] @ {venue}")
        
        return "\n".join(lines)
    
    def _format_team_status(self, status: list) -> str:
        """格式化球队状态"""
        if not status:
            return ""
        
        lines = []
        for item in status:
            team = item.get("team", "未知")
            status_text = item.get("status", "未知")
            notes = item.get("notes", "")
            lines.append(f"- {team}: {status_text} {notes}")
        
        return "\n".join(lines)
    
    def _format_injuries(self, injuries: list) -> str:
        """格式化伤病信息"""
        if not injuries:
            return "暂无伤病报告"
        
        lines = []
        for injury in injuries:
            team = injury.get("team", "未知")
            player = injury.get("player", "未知")
            injury_type = injury.get("type", "未知")
            lines.append(f"- {team} {player}: {injury_type}")
        
        return "\n".join(lines)
    
    def _format_results(self, results: list) -> str:
        """格式化近期结果"""
        if not results:
            return ""
        
        lines = []
        for result in results[:5]:  # 最多显示5场
            date = result.get("date", "未知")
            home = result.get("home_team", "未知")
            away = result.get("away_team", "未知")
            score = result.get("score", "待定")
            lines.append(f"{date} | {home} {score} {away}")
        
        return "\n".join(lines)
    
    def _generate_fallback_intelligence(self, current_date: str, 
                                       football_data: Dict) -> str:
        """生成备用情报（当AI不可用时）"""
        
        matches = football_data.get("matches", [])
        team_status = football_data.get("team_status", [])
        
        # 构建简单情报
        intelligence = f"""---

## 六、最新情报（每日更新区）

> 本节由每日情报流程覆盖更新。**当本节与第四节冲突时，以本节为准**（本节更新）。

**情报日期：{current_date}**

### 今日/近期比赛
"""
        
        if matches:
            for match in matches[:5]:
                intelligence += f"- {match.get('date', '未知')} {match.get('time', '')} | {match.get('home_team', '')} vs {match.get('away_team', '')} [{match.get('stage', '')}]\n"
        else:
            intelligence += "- 暂无比赛安排\n"
        
        intelligence += "\n### 球队状态更新\n"
        
        if team_status:
            for status in team_status:
                intelligence += f"- {status.get('team', '')}: {status.get('status', '')} - {status.get('notes', '')}\n"
        else:
            intelligence += "- 暂无状态更新\n"
        
        intelligence += "\n### 伤停信息\n- 暂无伤停报告\n"
        intelligence += "\n### 重要备注\n- 系统自动生成的情报\n"
        intelligence += "\n**优先级说明：** 当本节与第四节冲突时，以本节为准。"
        
        return intelligence

def main():
    """主函数"""
    
    print("=" * 60)
    print("🤖 AI情报生成工具")
    print("=" * 60)
    
    # 检查 API Key
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("❌ 错误：未设置 DEEPSEEK_API_KEY 环境变量")
        print("\n请设置环境变量：")
        print("  Linux/macOS: export DEEPSEEK_API_KEY='你的密钥'")
        print("  Windows: $env:DEEPSEEK_API_KEY='你的密钥'")
        return None
    
    print(f"✅ API Key 已配置")
    
    # 获取足球数据
    # 确保环境变量不是空字符串
    football_data_file = os.environ.get("FOOTBALL_DATA_FILE", "")
    
    # 如果环境变量为空，使用默认路径
    if not football_data_file:
        football_data_file = "data/football_data.json"
    
    football_data = None
    
    # 检查文件是否存在
    data_file_path = Path(football_data_file)
    if data_file_path.exists() and data_file_path.is_file():
        try:
            with open(data_file_path, "r", encoding="utf-8") as f:
                football_data = json.load(f)
            print(f"✅ 足球数据已加载: {football_data_file}")
        except Exception as e:
            print(f"⚠️ 读取足球数据文件失败: {e}")
            print("   将使用空数据进行生成")
    else:
        print(f"⚠️ 未找到足球数据文件: {football_data_file}")
        print("   将使用空数据进行生成")
    
    # 生成情报
    try:
        generator = IntelligenceGenerator(api_key)
        intelligence = generator.generate_daily_brief(football_data)
        
        # 保存情报
        output_file = Path("intelligence.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(intelligence)
        
        print(f"\n✅ 情报已保存到: {output_file}")
        print(f"\n📄 生成的情报内容:")
        print("-" * 60)
        print(intelligence)
        print("-" * 60)
        
        return intelligence
        
    except Exception as e:
        print(f"\n❌ 生成失败: {e}")
        return None

if __name__ == "__main__":
    main()