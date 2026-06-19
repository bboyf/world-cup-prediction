# -*- coding: utf-8 -*-
"""
从足球数据API获取最新比赛和情报信息
用于 GitHub Actions 自动更新
"""

import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

class FootballDataFetcher:
    """足球数据获取器"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("FOOTBALL_API_KEY")
        self.base_url = "https://api.football-data.org/v4"
        self.headers = {
            "X-Auth-Token": self.api_key,
            "Content-Type": "application/json"
        } if self.api_key else {}
    
    def get_matches(self, days_ahead: int = 7) -> List[Dict]:
        """获取未来N天的比赛"""
        if not self.api_key:
            print("⚠️ 未设置Football-Data API Key，使用模拟数据")
            return self._get_mock_matches(days_ahead)
        
        today = datetime.now()
        end_date = today + timedelta(days=days_ahead)
        
        url = f"{self.base_url}/competitions/WC/matches"
        params = {
            "dateFrom": today.strftime("%Y-%m-%d"),
            "dateTo": end_date.strftime("%Y-%m-%d")
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            matches = []
            for match in data.get("matches", []):
                matches.append({
                    "date": match.get("utcDate", "")[:10],
                    "time": match.get("utcDate", "")[11:16],
                    "home_team": self._translate_team_name(match.get("homeTeam", {}).get("name", "")),
                    "away_team": self._translate_team_name(match.get("awayTeam", {}).get("name", "")),
                    "stage": match.get("stage", ""),
                    "status": match.get("status", ""),
                    "venue": match.get("venue", "待定")
                })
            
            return matches
        except Exception as e:
            print(f"❌ 获取比赛数据失败: {e}")
            return self._get_mock_matches(days_ahead)
    
    def get_team_status(self) -> List[Dict]:
        """获取球队状态信息（简化版）"""
        # 实际应用中需要接入更详细的数据源
        # 这里返回预设的球队状态
        return [
            {"team": "墨西哥", "status": "正常", "notes": "东道主，揭幕战主队"},
            {"team": "南非", "status": "正常", "notes": "2010年后首次晋级"},
            {"team": "阿根廷", "status": "正常", "notes": "卫冕冠军"},
            {"team": "巴西", "status": "正常", "notes": "5星巴西"},
        ]
    
    def _translate_team_name(self, name: str) -> str:
        """球队名称中英对照"""
        translations = {
            "Mexico": "墨西哥",
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
            "South Korea": "韩国",
            "Czech Republic": "捷克",
            "Bosnia and Herzegovina": "波黑",
            "Qatar": "卡塔尔",
            "Switzerland": "瑞士",
            "Haiti": "海地",
            "Scotland": "苏格兰",
            "Paraguay": "巴拉圭",
            "Australia": "澳大利亚",
            "Turkey": "土耳其",
            "Curaçao": "库拉索",
            "Ivory Coast": "科特迪瓦",
            "Ecuador": "厄瓜多尔",
            "Netherlands": "荷兰",
            "Sweden": "瑞典",
            "Tunisia": "突尼斯",
            "Belgium": "比利时",
            "Egypt": "埃及",
            "Iran": "伊朗",
            "New Zealand": "新西兰",
            "Cape Verde": "佛得角",
            "Saudi Arabia": "沙特",
            "UAE": "阿联酋",
            "Algeria": "阿尔及利亚",
            "Austria": "奥地利",
            "Jordan": "约旦",
            "Norway": "挪威",
            "Iraq": "伊拉克",
            "Uzbekistan": "乌兹别克斯坦",
            "Ghana": "加纳",
            "Panama": "巴拿马",
            "Senegal": "塞内加尔",
            "DR Congo": "刚果金",
            "Chile": "智利",
            "Colombia": "哥伦比亚",
            "Peru": "秘鲁",
            "Poland": "波兰",
            "Italy": "意大利",
            "Ukraine": "乌克兰",
        }
        return translations.get(name, name)
    
    def _get_mock_matches(self, days: int) -> List[Dict]:
        """获取模拟比赛数据（用于测试或API不可用时）"""
        matches = []
        today = datetime.now()
        
        # 模拟几场比赛
        mock_teams = [
            ("墨西哥", "南非"),
            ("阿根廷", "巴西"),
            ("法国", "英格兰"),
            ("德国", "日本"),
        ]
        
        for i, (home, away) in enumerate(mock_teams[:min(4, days)]):
            match_date = today + timedelta(days=i)
            matches.append({
                "date": match_date.strftime("%Y-%m-%d"),
                "time": f"{18+i:02d}:00",
                "home_team": home,
                "away_team": away,
                "stage": "小组赛" if i < 3 else "淘汰赛",
                "status": "SCHEDULED",
                "venue": "待定"
            })
        
        return matches
    
    def get_injuries(self) -> List[Dict]:
        """获取伤病信息（简化版）"""
        # 实际应用中需要接入专业的伤病数据源
        # 这里返回空列表
        return []
    
    def get_recent_results(self, days_back: int = 7) -> List[Dict]:
        """获取近期比赛结果"""
        # 这个功能需要历史数据支持
        # 这里返回空列表
        return []

def main():
    """主函数 - 获取所有足球数据"""
    
    print("=" * 60)
    print("🏈 足球数据获取工具")
    print("=" * 60)
    
    # 创建数据目录
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # 创建获取器
    fetcher = FootballDataFetcher()
    
    # 获取数据
    data = {
        "fetch_time": datetime.now().isoformat(),
        "api_key_status": "available" if fetcher.api_key else "not_configured",
        "matches": fetcher.get_matches(days_ahead=7),
        "team_status": fetcher.get_team_status(),
        "injuries": fetcher.get_injuries(),
        "recent_results": fetcher.get_recent_results()
    }
    
    # 保存数据
    output_file = data_dir / "football_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 数据已保存到: {output_file}")
    print(f"\n📊 数据统计:")
    print(f"  - 未来比赛: {len(data['matches'])} 场")
    print(f"  - 球队状态: {len(data['team_status'])} 条")
    print(f"  - 伤病信息: {len(data['injuries'])} 条")
    print(f"  - 近期结果: {len(data['recent_results'])} 场")
    
    # 打印比赛列表
    if data["matches"]:
        print(f"\n📅 未来比赛:")
        for match in data["matches"][:5]:  # 只显示前5场
            print(f"  {match['date']} {match['time']} | {match['home_team']} vs {match['away_team']} [{match['stage']}]")
    
    print("\n" + "=" * 60)
    return data

if __name__ == "__main__":
    main()