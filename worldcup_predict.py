# -*- coding: utf-8 -*-
"""
2026世界杯AI预测引擎 - 本地部署脚本
=====================================
使用方法：
1. 设置环境变量 DEEPSEEK_API_KEY=你的API密钥
2. 运行命令：python worldcup_predict.py

或者直接在脚本中修改 API_KEY 变量
"""

import os
import json
import openai
from pathlib import Path

# ==================== 配置区域 ====================
# 方式1：直接在这里填入你的API Key（安全性较低，仅测试用）
API_KEY = "sk-3c560b18e0eb4feebea7c50977925669"  # DeepSeek API Key

# 方式2：从环境变量读取（推荐，更加安全）
# API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

# DeepSeek API配置
API_BASE = "https://api.deepseek.com/v1"
MODEL = "deepseek-v4-pro"

# 读取skill.md作为系统提示词
# skill.md在worldcup2026-prediction-skill子目录中
SKILL_FILE = Path(__file__).parent / "worldcup2026-prediction-skill" / "skill.md"

# ==================== 核心函数 ====================

def load_skill():
    """加载skill.md文件作为系统提示词"""
    if not SKILL_FILE.exists():
        raise FileNotFoundError(f"找不到skill.md文件！请确保 {SKILL_FILE} 存在")
    
    with open(SKILL_FILE, "r", encoding="utf-8") as f:
        return f.read()

def predict_match(team_a: str, team_b: str, stage: str = "小组赛") -> dict:
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
        raise ValueError("请设置DeepSeek API Key！\n方式1：设置环境变量 DEEPSEEK_API_KEY\n方式2：在脚本中修改 API_KEY 变量")
    
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
        max_tokens=2000  # 增加token数量以容纳完整JSON
    )
    
    # 解析返回结果
    result = json.loads(response.choices[0].message.content)
    return result

def display_result(result: dict, team_a: str, team_b: str):
    """美化展示预测结果 - 简洁专业格式"""
    
    # 获取数据
    team_a_name = result.get("teamA", {}).get("name", team_a)
    team_a_prob = result.get("teamA", {}).get("winProb", 0)
    team_b_name = result.get("teamB", {}).get("name", team_b)
    team_b_prob = result.get("teamB", {}).get("winProb", 0)
    draw_prob = result.get("draw", 0)
    predicted_score = result.get("predictedScore", "未知")
    confidence = result.get("confidence", "未知")
    analysis = result.get("analysis", "")
    key_factors = result.get("keyFactors", [])
    players = result.get("playersToWatch", [])
    
    # 构建简洁格式的输出（不使用emoji避免编码问题）
    output = []
    output.append("")
    output.append("="*60)
    output.append(f"[预测结果] {team_a_name} vs {team_b_name}")
    output.append("="*60)
    output.append("")
    
    # 预测比分和置信度
    output.append("  预测比分：{0}".format(predicted_score))
    output.append("  胜率：{0} {1}% / 平局 {2}% / {3} {4}%".format(
        team_a_name, team_a_prob, draw_prob, team_b_name, team_b_prob))
    output.append("  置信度：{0}".format(confidence))
    
    # 关键球员
    if players and len(players) >= 2:
        player_a = players[0]
        player_b = players[1]
        output.append("  关键球员：{0}（{1}）、{2}（{3}）".format(
            player_a.get('player', ''), player_a.get('team', ''),
            player_b.get('player', ''), player_b.get('team', '')))
    
    output.append("")
    output.append("-"*60)
    output.append("详细分析")
    output.append("-"*60)
    output.append("")
    
    # 关键因素
    if key_factors:
        output.append("  关键因素：")
        for i, factor in enumerate(key_factors, 1):
            output.append("    {0}. {1}".format(i, factor))
        output.append("")
    
    # 分析文字
    if analysis:
        output.append("  综合分析：")
        output.append("    {0}".format(analysis))
        output.append("")
    
    output.append("="*60)
    
    # 打印所有内容
    print("\n".join(output))

def interactive_mode():
    """交互式预测模式"""
    print("\n" + "🌟"*25)
    print("⚽ 2026世界杯AI预测引擎 - 交互模式")
    print("🌟"*25)
    
    # 检查API Key
    if not API_KEY:
        print("\n❌ 错误：请先设置DeepSeek API Key！")
        print("方式1：设置环境变量")
        print("  Windows PowerShell: $env:DEEPSEEK_API_KEY='你的密钥'")
        print("  macOS/Linux: export DEEPSEEK_API_KEY='你的密钥'")
        print("方式2：在脚本中修改 API_KEY 变量")
        return
    
    print(f"✅ API Key已配置")
    print(f"✅ 模型：{MODEL}")
    print(f"✅ Skill文件：{SKILL_FILE}")
    
    while True:
        print("\n" + "-"*40)
        print("请输入预测信息（直接回车退出）：")
        
        team_a = input("主队（如：墨西哥）：").strip()
        if not team_a:
            break
        
        team_b = input("客队（如：南非）：").strip()
        if not team_b:
            break
        
        stage = input("比赛阶段（直接回车默认=小组赛）：").strip() or "小组赛"
        
        try:
            result = predict_match(team_a, team_b, stage)
            display_result(result, team_a, team_b)
        except Exception as e:
            print(f"\n❌ 错误：{e}")

def batch_predict():
    """批量预测示例"""
    matches = [
        ("墨西哥", "南非", "小组赛"),  # 揭幕战
        ("阿根廷", "巴西", "小组赛"),
        ("法国", "英格兰", "决赛"),
    ]
    
    print("\n🔄 开始批量预测...")
    
    for team_a, team_b, stage in matches:
        try:
            print(f"\n正在预测：{team_a} vs {team_b}（{stage}）")
            result = predict_match(team_a, team_b, stage)
            display_result(result, team_a, team_b)
        except Exception as e:
            print(f"❌ 预测失败：{e}")

# ==================== 主程序 ====================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # 命令行模式：python worldcup_predict.py 主队 客队 [阶段]
        team_a = sys.argv[1]
        team_b = sys.argv[2] if len(sys.argv) > 2 else ""
        stage = sys.argv[3] if len(sys.argv) > 3 else "小组赛"
        
        if not team_b:
            print("用法：python worldcup_predict.py 主队 客队 [阶段]")
            print("示例：python worldcup_predict.py 墨西哥 南非 小组赛")
        else:
            result = predict_match(team_a, team_b, stage)
            # 使用美化格式输出（不显示原始JSON）
            display_result(result, team_a, team_b)
            print("\n提示：原始JSON数据可直接导入前端或数据库使用")
    else:
        # 交互式模式
        interactive_mode()
        # 如果想用批量预测，取消下面这行的注释：
        # batch_predict()