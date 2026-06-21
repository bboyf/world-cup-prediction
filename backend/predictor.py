# -*- coding: utf-8 -*-
"""
预测引擎核心模块
调用DeepSeek API进行比赛预测
"""

import json
import os
import openai
from pathlib import Path
from typing import Dict

# DeepSeek API配置（从环境变量读取，不要硬编码 Key）
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
API_BASE = "https://api.deepseek.com/v1"
MODEL = "deepseek-v4-pro"

# skill.md文件路径
SKILL_FILE = Path(__file__).parent.parent / "worldcup2026-prediction-skill" / "skill.md"

def load_skill() -> str:
    """加载skill.md文件作为系统提示词"""
    if not SKILL_FILE.exists():
        raise FileNotFoundError(f"找不到skill.md文件！请确保 {SKILL_FILE} 存在")
    
    with open(SKILL_FILE, "r", encoding="utf-8") as f:
        return f.read()

def predict_match(team_a: str, team_b: str, stage: str = "小组赛") -> Dict:
    """
    预测世界杯比赛结果
    
    参数:
        team_a: 主队名称（中文）
        team_b: 客队名称（中文）
        stage: 比赛阶段（小组赛/16强/8强/半决赛/决赛等）
    
    返回:
        预测结果字典（JSON格式）
    """
    if not API_KEY:
        raise ValueError("请设置DeepSeek API Key")
    
    # 初始化客户端
    client = openai.OpenAI(
        api_key=API_KEY,
        base_url=API_BASE
    )
    
    # 加载skill.md
    skill_content = load_skill()
    
    # 构建用户提问
    user_message = f"请预测这场2026世界杯比赛：【{stage}】{team_a} vs {team_b}。严格按约束文档的JSON格式输出。"
    
    # 调用API
    response = client.chat.completions.create(
        model=MODEL,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": skill_content},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    
    # 解析返回结果
    result = json.loads(response.choices[0].message.content)
    return result