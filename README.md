# ⚽ 2026世界杯AI预测引擎

基于 DeepSeek AI 的智能世界杯比赛预测系统，支持每日自动情报更新。

## 🌟 功能特性

- ✅ **智能预测**：基于AI的世界杯比赛预测
- ✅ **四层约束架构**：资料库锁死 + 方法论固化 + 输出契约 + 动态更新
- ✅ **每日自动更新**：GitHub Actions + AI Agent 自动更新情报
- ✅ **多模式使用**：支持命令行、Web界面、API调用
- ✅ **现代化Web界面**：响应式设计，数据可视化展示

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/bboyf/world-cup-prediction.git
cd world-cup-prediction
```

### 2. 安装依赖

```bash
conda activate Langchain_env
pip install -r requirements.txt
```

### 3. 配置API Key

创建 `config.ini` 文件（参考 `config.example.ini`）：

```ini
[api]
deepseek_api_key = sk-your-api-key
```

### 4. 运行预测

**命令行模式：**
```bash
python worldcup_predict.py 墨西哥 南非 小组赛
```

**Web服务模式：**
```bash
python backend/main.py
# 访问 http://localhost:8000
```

## 📁 项目结构

```
world-cup-prediction/
├── backend/                    # FastAPI后端
│   ├── main.py               # 主程序
│   ├── api.py                # API路由
│   └── predictor.py          # 预测引擎
├── templates/                 # 前端模板
│   └── index.html
├── static/                   # 静态资源
│   ├── css/
│   └── js/
├── scripts/                  # 自动化脚本
│   ├── fetch_football_data.py    # 数据获取
│   ├── generate_intelligence.py  # AI情报生成
│   └── update_skill_md.py        # 文件更新
├── worldcup2026-prediction-skill/ # 原始项目
│   └── skill.md              # AI约束文档
├── .github/                  # GitHub配置
│   └── workflows/            # Actions工作流
│       └── daily-update.yml  # 每日更新
└── requirements.txt          # Python依赖
```

## 🔄 自动更新功能

项目配置了 GitHub Actions 每日自动更新功能：

- **执行时间**：每天 08:00 (北京时间)
- **更新内容**：自动更新 `skill.md` 第六节（最新情报）
- **数据源**：Football-Data API + DeepSeek AI

### 配置Secrets

在 GitHub 仓库的 `Settings → Secrets and variables → Actions` 中添加：

| Secret 名称 | 说明 |
|:---|:---|
| `DEEPSEEK_API_KEY` | DeepSeek API密钥 |
| `FOOTBALL_API_KEY` | Football-Data API密钥（可选） |

## 📊 技术架构

### 四层约束设计

1. **资料库锁死**：48支球队完整资料，防止编造
2. **方法论固化**：四维评估体系（40%近期状态 + 30%硬实力 + 15%历史交锋 + 15%情境因素）
3. **输出契约**：严格JSON格式，机器可解析
4. **动态更新**：每日情报区自动更新

### 工作流程

```
用户请求 → skill.md约束 → DeepSeek API → JSON预测结果
                ↓
         第六节情报（每日自动更新）
```

## 🎯 使用示例

### 预测揭幕战

```bash
$ python worldcup_predict.py 墨西哥 南非 小组赛

============================================================
[预测结果] 墨西哥 vs 南非
============================================================

  预测比分：2-0
  胜率：墨西哥 68% / 平局 20% / 南非 12%
  置信度：高
  关键球员：希门尼斯（墨西哥）、珀西·陶（南非）

------------------------------------------------------------
详细分析
------------------------------------------------------------

  关键因素：
    1. 东道主揭幕战主场优势
    2. 墨西哥大赛经验丰富
    3. 南非实力差距明显
    4. 阿兹特克高原主场

  综合分析：
    墨西哥在阿兹特克球场迎来揭幕战...
============================================================
```

### Web界面

访问 http://localhost:8000 使用可视化界面进行预测。

## 📝 API接口

### POST /api/predict

```json
POST /api/predict
{
  "team_a": "墨西哥",
  "team_b": "南非",
  "stage": "小组赛"
}
```

响应：
```json
{
  "success": true,
  "data": {
    "teamA": {"name": "墨西哥", "winProb": 68},
    "draw": 20,
    "teamB": {"name": "南非", "winProb": 12},
    "predictedScore": "2-0",
    "confidence": "高",
    "keyFactors": [...],
    "analysis": "...",
    "playersToWatch": [...]
  }
}
```

## ⚙️ 配置说明

### 环境变量

| 变量名 | 说明 | 必需 |
|:---|:---|:---:|
| `DEEPSEEK_API_KEY` | DeepSeek API密钥 | ✅ |
| `FOOTBALL_API_KEY` | Football-Data API密钥 | ❌ |

### 配置文件

参考 `config.example.ini` 创建 `config.ini`：

```ini
[api]
deepseek_api_key = sk-your-api-key
model = deepseek-v4-pro

[prediction]
temperature = 0.7
max_tokens = 2000
```

## 🐛 故障排查

### 常见问题

1. **API Key无效**：检查 `config.ini` 或环境变量
2. **预测失败**：检查网络连接和API余额
3. **Web服务无法启动**：检查端口占用情况

### 日志查看

GitHub Actions 工作流日志：`仓库 → Actions → Daily Update Intelligence`

## 📚 文档

- [GitHub 部署指南](SETUP_GITHUB.md)
- [Web版使用指南](WEB_GUIDE.md)
- [skill.md 预测逻辑解析](worldcup2026-prediction-skill/)

## ⚠️ 声明

本工具仅供娱乐和球迷讨论使用，**严禁用于任何投注、博彩活动**。

足球比赛结果具有偶然性，AI预测仅供参考，不代表真实比赛结果。

## 📜 License

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [DeepSeek](https://platform.deepseek.com) - AI模型支持
- [Football-Data](https://www.football-data.org) - 足球数据支持
- [TradingAi666/worldcup2026-prediction-skill](https://github.com/TradingAi666/worldcup2026-prediction-skill) - 原始项目

---

**享受世界杯预测的乐趣！** ⚽🏆