# -*- coding: utf-8 -*-
"""
从免费API获取世界杯足球数据
使用 wheniskickoff.com 的免费公共API
无需API Key，完全免费！
"""

import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

class FootballDataFetcher:
    """足球数据获取器 - 使用免费API"""
    
    def __init__(self, api_key: Optional[str] = None):
        # wheniskickoff.com API - 完全免费，无需API Key
        self.base_url = "https://wheniskickoff.com/data/v1"
        self.api_key = api_key  # 保留参数以保持兼容性，但实际不需要
    
    def get_all_matches(self) -> List[Dict]:
        """获取所有比赛"""
        try:
            url = f"{self.base_url}/matches.json"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            # 解析数据
            matches = []
            for match in data.get("data", []):
                matches.append({
                    "date": match.get("date", ""),
                    "time": match.get("time_utc", ""),
                    "home_team": self._translate_team_name(match.get("home_name", "")),
                    "away_team": self._translate_team_name(match.get("away_name", "")),
                    "stage": self._convert_phase(match.get("phase", "")),
                    "group": match.get("group", ""),
                    "venue": match.get("venue_name", ""),
                    "city": match.get("venue_city", ""),
                    "slug": match.get("slug", "")
                })
            
            return matches
        except Exception as e:
            print(f"❌ 获取比赛数据失败: {e}")
            # 如果API失败，返回空列表
            return []
    
    def get_upcoming_matches(self, days_ahead: int = 7) -> List[Dict]:
        """获取未来N天的比赛"""
        all_matches = self.get_all_matches()
        
        today = datetime.now()
        end_date = today + timedelta(days=days_ahead)
        
        upcoming = []
        for match in all_matches:
            try:
                match_date = datetime.strptime(match["date"], "%Y-%m-%d")
                if today <= match_date <= end_date:
                    upcoming.append(match)
            except:
                continue
        
        return upcoming
    
    def get_today_matches(self) -> List[Dict]:
        """获取今天的比赛"""
        all_matches = self.get_all_matches()
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        today_matches = []
        for match in all_matches:
            if match["date"] == today:
                today_matches.append(match)
        
        return today_matches
    
    def get_team_status(self) -> List[Dict]:
        """获取球队状态信息（简化版）"""
        # 这里返回预设的球队状态
        # 实际应用中可以从其他数据源获取实时状态
        return [
            {"team": "墨西哥", "status": "正常", "notes": "东道主，揭幕战主队"},
            {"team": "南非", "status": "正常", "notes": "2010年后首次晋级"},
            {"team": "阿根廷", "status": "正常", "notes": "卫冕冠军"},
            {"team": "巴西", "status": "正常", "notes": "5星巴西"},
            {"team": "法国", "status": "正常", "notes": "2018冠军、2022亚军"},
            {"team": "德国", "status": "正常", "notes": "4次夺冠"},
            {"team": "西班牙", "status": "正常", "notes": "2024欧洲杯冠军"},
            {"team": "英格兰", "status": "正常", "notes": "2024欧洲杯亚军"},
        ]
    
    def _translate_team_name(self, name: str) -> str:
        """球队名称英中对照"""
        translations = {
            "Mexico": "墨西哥",
            "South Korea": "韩国",
            "South Africa": "南非",
            "Argentina": "阿根廷",
            "Brazil": "巴西",
            "France": "法国",
            "Germany": "德国",
            "Spain": "西班牙",
            "England": "英格兰",
            "Portugal": "葡萄牙",
            "Netherlands": "荷兰",
            "Uruguay": "乌拉圭",
            "Croatia": "克罗地亚",
            "Japan": "日本",
            "Morocco": "摩洛哥",
            "United States": "美国",
            "Canada": "加拿大",
            "Switzerland": "瑞士",
            "Belgium": "比利时",
            "Poland": "波兰",
            "Senegal": "塞内加尔",
            "Serbia": "塞尔维亚",
            "Australia": "澳大利亚",
            "Costa Rica": "哥斯达黎加",
            "Saudi Arabia": "沙特",
            "Iran": "伊朗",
            "Denmark": "丹麦",
            "Peru": "秘鲁",
            "Tunisia": "突尼斯",
            "Cameroon": "喀麦隆",
            "Ghana": "加纳",
            "Algeria": "阿尔及利亚",
            "Egypt": "埃及",
            "Nigeria": "尼日利亚",
            "Iceland": "冰岛",
            "Sweden": "瑞典",
            "Colombia": "哥伦比亚",
            "Chile": "智利",
            "Ecuador": "厄瓜多尔",
            "Paraguay": "巴拉圭",
            "Bolivia": "玻利维亚",
            "Venezuela": "委内瑞拉",
            "Panama": "巴拿马",
            "Honduras": "洪都拉斯",
            "Jamaica": "牙买加",
            "New Zealand": "新西兰",
            "Qatar": "卡塔尔",
            "UAE": "阿联酋",
            "Iraq": "伊拉克",
            "China": "中国",
            "Korea DPR": "朝鲜",
            "Oman": "阿曼",
            "Jordan": "约旦",
            "Uzbekistan": "乌兹别克斯坦",
            "Kazakhstan": "哈萨克斯坦",
            "Turkey": "土耳其",
            "Austria": "奥地利",
            "Scotland": "苏格兰",
            "Wales": "威尔士",
            "Ukraine": "乌克兰",
            "Czech Republic": "捷克",
            "Norway": "挪威",
            "Romania": "罗马尼亚",
            "Hungary": "匈牙利",
            "Slovakia": "斯洛伐克",
            "Bosnia and Herzegovina": "波黑",
            "Slovenia": "斯洛文尼亚",
            "Albania": "阿尔巴尼亚",
            "Montenegro": "黑山",
            "North Macedonia": "北马其顿",
            "Ivory Coast": "科特迪瓦",
            "DR Congo": "刚果金",
            "Gabon": "加蓬",
            "Mali": "马里",
            "Guinea": "几内亚",
            "Burkina Faso": "布基纳法索",
            "Zambia": "赞比亚",
            "South Sudan": "南苏丹",
            "El Salvador": "萨尔瓦多",
            "Trinidad and Tobago": "特立尼达和多巴哥",
            "Haiti": "海地",
            "Cuba": "古巴",
            "Canada": "加拿大",
            "Curacao": "库拉索",
            "Cape Verde": "佛得角",
            "Gambia": "冈比亚",
            "Togo": "多哥",
            "Benin": "贝宁",
            "Mauritania": "毛里塔尼亚",
            "Madagascar": "马达加斯加",
            "Mauritius": "毛里求斯",
            "Mozambique": "莫桑比克",
            "Angola": "安哥拉",
            "Namibia": "纳米比亚",
            "Botswana": "博茨瓦纳",
            "Sierra Leone": "塞拉利昂",
            "Liberia": "利比里亚",
            "Ethiopia": "埃塞俄比亚",
            "Kenya": "肯尼亚",
            "Tanzania": "坦桑尼亚",
            "Uganda": "乌干达",
        }
        return translations.get(name, name)
    
    def _convert_phase(self, phase: str) -> str:
        """转换比赛阶段"""
        phase_map = {
            "group": "小组赛",
            "round of 16": "16强",
            "round16": "16强",
            "quarter-final": "8强",
            "quarterfinal": "8强",
            "quarter": "8强",
            "semi-final": "半决赛",
            "semifinal": "半决赛",
            "semi": "半决赛",
            "third place": "三四名决赛",
            "third": "三四名决赛",
            "final": "决赛",
        }
        return phase_map.get(phase.lower(), phase)

def main():
    """主函数 - 获取所有足球数据"""
    
    print("=" * 60)
    print("🏈 足球数据获取工具 (免费API版)")
    print("=" * 60)
    print(f"数据源: {FootballDataFetcher().base_url}")
    
    # 创建数据目录
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # 创建获取器
    fetcher = FootballDataFetcher()
    
    # 获取数据
    data = {
        "fetch_time": datetime.now().isoformat(),
        "api_status": "wheniskickoff.com (免费API)",
        "all_matches": fetcher.get_all_matches(),
        "today_matches": fetcher.get_today_matches(),
        "upcoming_matches": fetcher.get_upcoming_matches(days_ahead=7),
        "team_status": fetcher.get_team_status(),
        "injuries": [],
        "recent_results": []
    }
    
    # 保存数据
    output_file = data_dir / "football_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 数据已保存到: {output_file}")
    print(f"\n📊 数据统计:")
    print(f"  - 总比赛数: {len(data['all_matches'])} 场")
    print(f"  - 今日比赛: {len(data['today_matches'])} 场")
    print(f"  - 近期比赛: {len(data['upcoming_matches'])} 场")
    print(f"  - 球队状态: {len(data['team_status'])} 条")
    
    # 打印今日比赛
    if data["today_matches"]:
        print(f"\n📅 今日比赛:")
        for match in data["today_matches"]:
            print(f"  {match['date']} {match['time']} | {match['home_team']} vs {match['away_team']} [{match['stage']}] @ {match['venue']}")
    
    # 打印近期比赛
    if data["upcoming_matches"]:
        print(f"\n📅 近期比赛 (未来7天):")
        for match in data["upcoming_matches"][:5]:
            print(f"  {match['date']} {match['time']} | {match['home_team']} vs {match['away_team']} [{match['stage']}]")
    
    print("\n" + "=" * 60)
    return data

if __name__ == "__main__":
    main()