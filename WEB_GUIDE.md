# 2026世界杯AI预测引擎 - Web版本使用指南

## 📦 项目结构

```
world-cup-prediction/
├── backend/
│   ├── main.py              # FastAPI主程序
│   ├── api.py               # API路由
│   ├── models.py            # 数据模型
│   └── predictor.py         # 预测引擎核心
├── templates/
│   └── index.html           # 前端主页面
├── static/
│   ├── css/
│   │   └── style.css        # 样式文件
│   └── js/
│       └── app.js           # 前端逻辑
├── worldcup_predict.py      # 命令行版本
├── requirements.txt         # 命令行版本依赖
├── requirements-web.txt     # Web版本依赖
└── start_web.bat            # Windows启动脚本
```

---

## 🚀 快速启动

### 方式1：使用启动脚本（推荐 Windows 用户）

双击运行 `start_web.bat`

### 方式2：手动启动

```bash
# 1. 激活conda环境
conda activate Langchain_env

# 2. 安装依赖（如果还没安装）
pip install -r requirements-web.txt

# 3. 启动服务
python backend/main.py
```

---

## 🌐 访问服务

启动成功后，打开浏览器访问：

- **主页：** http://localhost:8000
- **API文档：** http://localhost:8000/docs
- **健康检查：** http://localhost:8000/api/health

---

## 🎯 使用方法

### 1. 打开主页

在浏览器中打开 http://localhost:8000

### 2. 输入预测信息

- **主队**：输入第一支球队名称（如：墨西哥）
- **客队**：输入第二支球队名称（如：南非）
- **比赛阶段**：选择比赛阶段（小组赛/16强/8强/半决赛/决赛）

### 3. 点击预测

点击"开始预测"按钮，系统会调用AI进行预测并展示结果

### 4. 查看结果

结果包含：
- 预测比分
- 胜平负概率（可视化条形图）
- 置信度
- 关键球员
- 详细分析（关键因素 + 综合分析）

---

## 📡 API接口

### POST /api/predict

预测比赛结果

**请求体：**
```json
{
  "team_a": "墨西哥",
  "team_b": "南非",
  "stage": "小组赛"
}
```

**响应示例：**
```json
{
  "success": true,
  "message": "预测成功",
  "data": {
    "teamA": {"name": "墨西哥", "winProb": 68},
    "draw": 20,
    "teamB": {"name": "南非", "winProb": 12},
    "predictedScore": "2-0",
    "confidence": "高",
    "keyFactors": ["东道主揭幕战气势如虹", ...],
    "analysis": "墨西哥城阿兹特克球场...",
    "playersToWatch": [
      {"team": "墨西哥", "player": "劳尔·希门尼斯", "reason": "..."},
      {"team": "南非", "player": "珀西·陶", "reason": "..."}
    ]
  }
}
```

### GET /api/teams

获取所有支持的球队列表

### GET /api/health

健康检查接口

---

## 🎨 界面特色

### 现代化设计
- 深色主题，护眼舒适
- 渐变色彩，专业美观
- 响应式布局，适配各种设备

### 交互体验
- 输入验证，实时反馈
- 加载动画，过程可见
- 平滑滚动，用户友好

### 数据可视化
- 概率条形图，一目了然
- 置信度标签，清晰直观
- 关键球员突出显示

---

## 🔧 配置说明

### 修改API Key

编辑 `backend/predictor.py` 第8行：

```python
API_KEY = "你的新API密钥"
```

### 修改端口

编辑 `backend/main.py` 第43行：

```python
uvicorn.run(..., port=8001)  # 改为你想要的端口
```

### 启用调试模式

编辑 `backend/main.py` 第43行：

```python
uvicorn.run(..., reload=True, log_level="debug")
```

---

## 📝 开发说明

### 技术栈
- **后端：** FastAPI + Python
- **前端：** HTML5 + CSS3 + JavaScript (原生)
- **AI服务：** DeepSeek API

### 扩展功能

如果你想添加新功能，可以：

1. **添加新的API接口：** 在 `backend/api.py` 中添加
2. **修改前端页面：** 编辑 `templates/index.html` 和相关静态文件
3. **添加数据验证：** 在 `backend/models.py` 中定义新的Pydantic模型

---

## 🐛 常见问题

### 问题1：服务启动失败

**原因：** 端口被占用  
**解决：** 关闭占用端口的程序，或修改 `backend/main.py` 中的端口号

### 问题2：预测请求失败

**原因：** API Key无效或余额不足  
**解决：** 检查 `backend/predictor.py` 中的API Key，或到DeepSeek平台充值

### 问题3：前端页面显示异常

**原因：** 静态文件路径错误  
**解决：** 确保 `backend/main.py` 中正确挂载了静态文件目录

---

## ⚠️ 声明

本工具仅供娱乐和球迷讨论使用，**严禁用于任何投注、博彩活动**。

足球比赛结果具有偶然性，AI预测仅供参考，不代表真实比赛结果。

---

**创建时间：** 2026-06-19  
**版本：** 1.0.0  
**技术栈：** FastAPI + HTML5 + DeepSeek API