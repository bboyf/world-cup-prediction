# -*- coding: utf-8 -*-
"""
更新 skill.md 文件的第六节
用于 GitHub Actions 自动更新
"""

import re
from pathlib import Path
from datetime import datetime

def update_skill_md(skill_file_path=None):
    """更新 skill.md 的第六节
    
    Args:
        skill_file_path: skill.md 文件的路径，如果为None则自动查找
    """
    
    print("=" * 60)
    print("[文件] Skill.md 更新工具")
    print("=" * 60)
    
    # 读取情报文件
    intelligence_file = Path("intelligence.md")
    
    if not intelligence_file.exists():
        print("[错误] 错误：未找到 intelligence.md 文件")
        print("   请先运行 generate_intelligence.py 生成情报")
        return False
    
    with open(intelligence_file, "r", encoding="utf-8") as f:
        new_section = f.read()
    
    print(f"[OK] 已读取情报文件: {intelligence_file}")
    
    # 读取 skill.md
    if skill_file_path is None:
        skill_file_path = find_skill_md()
    
    if not skill_file_path:
        print("[错误] 错误：未找到 skill.md 文件")
        return False
    
    skill_file = Path(skill_file_path)
    
    if not skill_file.exists():
        print(f"[错误] 错误：skill.md 文件不存在: {skill_file}")
        return False
    
    try:
        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"[OK] 已读取文件: {skill_file}")
    except Exception as e:
        print(f"[错误] 读取文件失败: {e}")
        return False
    
    # 查找第六节的位置
    section_6_start_marker = "## 六、最新情报（每日更新区）"
    
    if section_6_start_marker not in content:
        print("[错误] 错误：在 skill.md 中未找到第六节标记")
        print(f"   期望标记: {section_6_start_marker}")
        return False
    
    print(f"[OK] 找到第六节标记")
    
    # 找到第六节结束位置（下一个 ## 标题）
    # 方法：找到第六节开始，然后找到下一个以 ## 开头的内容
    
    # 分割内容
    parts = content.split(section_6_start_marker)
    
    if len(parts) != 2:
        print("[错误] 错误：找到多个第六节标记")
        return False
    
    part_before_section_6 = parts[0]
    rest_of_content = parts[1]
    
    # 在剩余内容中找到下一个 ## 标题
    # 匹配 ## 标题（## 后面跟着空格和文字）
    next_section_pattern = r'\n## '
    match = re.search(next_section_pattern, rest_of_content)
    
    if match:
        # 找到了下一个章节
        part_after_section_6 = rest_of_content[match.start():]
    else:
        # 没有找到下一个章节，第六节是文件的最后部分
        part_after_section_6 = ""
    
    # 构建新内容
    new_content = part_before_section_6 + section_6_start_marker + new_section + part_after_section_6
    
    # 写回文件
    with open(skill_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[OK] skill.md 已更新")
    print(f"   更新时间: {current_time}")
    print(f"   文件路径: {skill_file.absolute()}")
    
    # 验证更新
    with open(skill_file, "r", encoding="utf-8") as f:
        updated_content = f.read()
    
    if new_section in updated_content:
        print(f"[OK] 验证通过：情报内容已正确插入")
    else:
        print(f"[警告] 警告：可能未正确插入情报内容")
    
    return True

def find_skill_md():
    """查找 skill.md 文件的位置"""
    # 可能的文件位置（按优先级排序）
    possible_paths = [
        Path("skill.md"),                              # 根目录
        Path("worldcup2026-prediction-skill/skill.md"),  # 子目录
        Path("../worldcup2026-prediction-skill/skill.md"),  # 父目录的子目录
    ]
    
    for path in possible_paths:
        if path.exists() and path.is_file():
            print(f"[OK] 找到 skill.md: {path}")
            return path
    
    return None

def validate_skill_md():
    """验证 skill.md 的格式"""
    
    print("\n" + "=" * 60)
    print("[检查] 验证 skill.md")
    print("=" * 60)
    
    # 查找 skill.md 文件
    skill_file = find_skill_md()
    
    if not skill_file:
        print("[错误] 错误：未找到 skill.md 文件")
        print("   查找了以下位置：")
        print("   - skill.md")
        print("   - worldcup2026-prediction-skill/skill.md")
        return False
    
    try:
        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"[错误] 读取文件失败: {e}")
        return False
    
    # 检查必要的章节
    sections = [
        "## 一、赛事基本盘",
        "## 二、预测方法论",
        "## 三、输出格式",
        "## 四、球队资料库",
        "## 五、红线",
        "## 六、最新情报"
    ]
    
    all_found = True
    for section in sections:
        if section in content:
            print(f"[OK] 找到: {section}")
        else:
            print(f"[错误] 缺失: {section}")
            all_found = False
    
    if all_found:
        print("\n[OK] 验证通过：所有章节完整")
    else:
        print("\n[警告] 警告：部分章节缺失")
    
    return all_found, skill_file

def main():
    """主函数"""
    
    # 验证文件（获取文件路径）
    validation_result = validate_skill_md()
    
    # 处理不同的返回情况
    if validation_result is False:
        print("\n[错误] 验证失败，终止更新")
        return False
    elif isinstance(validation_result, tuple):
        is_valid, skill_file = validation_result
        if not is_valid:
            print("\n[错误] 验证失败，终止更新")
            return False
    else:
        # 如果只返回布尔值，使用默认路径
        skill_file = find_skill_md()
        if not skill_file:
            print("\n[错误] 找不到 skill.md 文件，终止更新")
            return False
    
    print(f"\n将更新文件: {skill_file}")
    
    # 更新文件
    print()
    success = update_skill_md(skill_file)
    
    if success:
        print("\n" + "=" * 60)
        print("[完成] 更新完成！")
        print("=" * 60)
        print(f"\n提示：请检查 git diff 确认更改是否正确")
    else:
        print("\n" + "=" * 60)
        print("[错误] 更新失败！")
        print("=" * 60)
    
    return success

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
