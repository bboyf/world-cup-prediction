# 2026世界杯AI预测引擎

基于 DeepSeek AI 的智能世界杯比赛预测系统，支持每日自动情报更新与 Web 可视化展示。

## 功能特性

- **智能预测**：基于 AI 分析球队资料库，输出比分、胜率、关键因素等结构化预测结果
- **四层约束架构**：资料库锁死 + 方法论固化 + 输出契约 + 动态更新，保证预测可复现
- **每日自动更新**：GitHub Actions 定时拉取比赛数据，AI 自动生成最新情报
- **Web 可视化界面**：FastAPI 后端 + 响应式前端，选择球队即可预测
- **命令行 + API**：支持命令行快速预测和 RESTful API 集成

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/bboyf/world-cup-prediction.git
cd world-cup-prediction
```

### 2. 创建虚拟环境并安装依赖

**推荐使用 Conda（已有 Langchain_env 环境可跳过创建）：**

```bash
# 创建环境（首次）
conda create -n Langchain_env python=3.10 -y
conda activate Langchain_env

# 安装依赖
pip install -r requirements.txt
```

**或使用 venv：**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. 配置 API Key

本项目的 DeepSeek API Key **通过环境变量读取**，不在代码中硬编码。

**Windows PowerShell：**

```powershell
$env:DEEPSEEK_API_KEY='sk-你的DeepSeek密钥'
```

**macOS / Linux：**

```bash
export DEEPSEEK_API_KEY='sk-你的DeepSeek密钥'
```

获取 Key：[DeepSeek 开放平台](https://platform.deepseek.com) → API Keys

### 4. 启动服务

**Web 服务模式（推荐）：**

```bash
# 先设置环境变量，再启动（必须在同一个终端）
$env:DEEPSEEK_API_KEY='sk-你的密钥'
python backend/main.py
```

浏览器访问 `http://127.0.0.1:8000`，选择两支球队即可预测。

**命令行模式：**

```bash
$env:DEEPSEEK_API_KEY='sk-你的密钥'
python worldcup_predict.py
```

按交互提示输入球队名称和比赛阶段。

**快捷启动（Windows）：**

双击 `start_web.bat`，将按提示输入 API Key 后启动 Web 服务。

## 项目结构

```
world-cup-prediction/
├── backend/                     # FastAPI 后端
│   ├── main.py                  # 服务入口
│   ├── api.py                   # API 路由
│   ├── predictor.py             # 预测引擎（调用 DeepSeek）
│   └── models.py                # 数据模型
├── templates/                   # 前端 HTML 模板
│   └── index.html
├── static/                      # 前端静态资源
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── scripts/                     # 自动化脚本（供 GitHub Actions 调用）
│   ├── fetch_football_data.py   # 抓取比赛数据
│   ├── generate_intelligence.py # AI 生成每日情报
│   └── update_skill_md.py       # 将情报写入 skill.md
├── worldcup2026-prediction-skill/ # AI 约束文档（预测逻辑核心）
│   └── skill.md                 # 球队资料库 + 预测方法论 + 情报区
├── .github/workflows/           # GitHub Actions 工作流
│   └── daily-update.yml         # 每日自动更新情报
├── worldcup_predict.py          # 命令行预测脚本
├── start_web.bat                # Windows 一键启动
├── requirements.txt             # Python 依赖
├── Dockerfile                   # Docker 镜像
└── docker-compose.yml           # Docker Compose 编排
```

## API 接口

### POST /api/predict

请求：

```json
{
  "team_a": "巴西",
  "team_b": "德国",
  "stage": "小组赛"
}
```

响应：

```json
{
  "success": true,
  "data": {
    "teamA": { "name": "巴西", "winProb": 45 },
    "draw": 25,
    "teamB": { "name": "德国", "winProb": 30 },
    "predictedScore": "2-1",
    "confidence": "高",
    "keyFactors": ["巴西锋线状态火热", "德国中场组织出色"],
    "analysis": "详细分析文字...",
    "playersToWatch": ["维尼修斯", "穆西亚拉"]
  }
}
```

### GET /api/health

```json
{ "status": "ok", "service": "worldcup-prediction-api" }
```

## 每日自动更新

项目使用 GitHub Actions 实现每日情报自动更新：

- **执行时间**：每天约 08:00（北京时间）
- **手动触发**：仓库 Actions 页面 → `Daily Update` → `Run workflow`
- **流程**：抓取比赛数据 → AI 生成情报 → 更新 skill.md → 推送回仓库

### 配置 GitHub Secrets

在仓库 `Settings → Secrets and variables → Actions` 中添加：

| Secret 名称 | 说明 | 必需 |
|:---|:---|---:|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 | 是 |

## 预测逻辑

### 四层约束架构

1. **资料库锁死**：48 支球队完整资料（实力、阵容、历史等），防止 AI 编造
2. **方法论固化**：四维评估体系 —— 40% 近期状态 + 30% 硬实力 + 15% 历史交锋 + 15% 情境因素
3. **输出契约**：严格 JSON 格式，机器可解析
4. **动态更新**：第六节情报区由每日工作流覆盖，确保信息时效

### 工作流程

```
用户请求 → skill.md 约束 → DeepSeek API → JSON 预测结果
                ↓
        第六节情报（GitHub Actions 每日更新）
```

## Docker 部署

```bash
# 构建并启动
docker-compose up -d

# 查看日志
docker-compose logs -f web

# 停止
docker-compose down
```

详细说明见 [DEPLOY_DOCKER.md](DEPLOY_DOCKER.md)。

## 故障排查

| 问题 | 原因 | 解决 |
|:---|:---|:---|
| 预测返回 500 | 未设置或 Key 无效 | 执行 `$env:DEEPSEEK_API_KEY='sk-...'` 后重启服务 |
| 端口被占用 | 已有进程在 8000 端口 | `netstat -ano \| findstr :8000` 查看并停掉 |
| 情报都是"暂无更新" | 远程数据文件未传递 | 检查 Actions 日志中 artifact 上传/下载是否成功 |
| 依赖安装失败 | 网络或版本问题 | 尝试 `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple` |

## 环境变量参考

| 变量名 | 说明 | 默认值 |
|:---|:---|---:|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 | 空 |
| `MODEL` | 使用的模型 | `deepseek-v4-pro` |
| `API_BASE` | API 地址 | `https://api.deepseek.com/v1` |

## 注意事项

- 本工具仅供娱乐和球迷讨论使用，**禁止用于任何投注或博彩活动**
- 足球比赛具有高度偶然性，AI 预测不构成任何结果保证
- API Key 通过环境变量传递，**请勿将 Key 硬编码在代码中或提交到 Git 仓库**
- `intelligence.md` 是中间产物，不会出现在仓库文件列表中，最终更新保存在 `skill.md`

## License

MIT License

## 致谢

- [DeepSeek](https://platform.deepseek.com) — AI 模型支持
- [TradingAi666/worldcup2026-prediction-skill](https://github.com/TradingAi666/worldcup2026-prediction-skill) — 原始项目
