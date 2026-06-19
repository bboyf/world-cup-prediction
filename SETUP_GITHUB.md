# 2026世界杯AI预测引擎 - GitHub 部署指南

## 🚀 快速开始

本指南将帮助您将项目上传到自己的 GitHub 仓库，并配置每日情报自动更新功能。

---

## 📋 准备工作

在开始之前，请确保您已准备好：

- [ ] GitHub 账号
- [ ] DeepSeek API Key（用于AI情报生成）
- [ ] Football-Data API Key（可选，用于获取比赛数据）
- [ ] Git 客户端已安装

---

## 步骤 1：创建 GitHub 仓库

### 方法A：使用 GitHub 网页（推荐）

1. 登录 GitHub：https://github.com
2. 点击右上角 **"+"** → **"New repository"**
3. 填写仓库信息：
   - **Repository name**: `world-cup-prediction`
   - **Description**: `2026世界杯AI预测引擎 - 基于DeepSeek的智能预测系统`
   - **Visibility**: Private 或 Public（根据需要）
   - **不要勾选** "Add a README file"（我们已经有了）
4. 点击 **"Create repository"**
5. 复制仓库 URL（稍后使用）

### 方法B：使用命令行

```bash
# 创建新仓库（在GitHub网页上操作）
# 然后克隆到本地
git clone https://github.com/你的用户名/world-cup-prediction.git
cd world-cup-prediction
```

---

## 步骤 2：初始化本地 Git 仓库

在项目目录中执行以下命令：

```bash
# 初始化Git仓库
git init

# 添加所有文件（不包括.gitignore中的文件）
git add .

# 提交初始版本
git commit -m "feat: 初始化2026世界杯AI预测引擎项目
- 添加skill.md预测约束文档
- 添加预测脚本worldcup_predict.py
- 添加FastAPI Web服务
- 添加GitHub Actions每日自动更新功能
- 配置文件使用环境变量，不上传敏感信息"

# 添加远程仓库（替换为你的仓库URL）
git remote add origin https://github.com/你的用户名/world-cup-prediction.git

# 验证远程仓库
git remote -v
```

---

## 步骤 3：配置 GitHub Secrets

在 GitHub 仓库中配置敏感信息，这些信息不会上传到代码库：

1. 打开你的 GitHub 仓库
2. 点击 **Settings**（设置）
3. 在左侧菜单中找到 **Secrets and variables** → **Actions**
4. 点击 **"New repository secret"** 添加以下 Secrets：

### 添加必需的 Secrets

| Secret 名称 | 值 | 说明 |
|:---|:---|:---|
| `DEEPSEEK_API_KEY` | `sk-xxxxxxxxxxxxx` | DeepSeek API密钥，用于AI情报生成 |
| `FOOTBALL_API_KEY` | `xxxxxxxxxxxxx` | Football-Data API密钥（可选） |

### 获取 API Keys

#### DeepSeek API Key

1. 访问：https://platform.deepseek.com
2. 注册/登录账号
3. 进入 **API Keys** 页面
4. 点击 **"Create new API Key"**
5. 复制生成的 Key（格式：`sk-xxxxxxxxxxxxx`）

#### Football-Data API Key（可选）

1. 访问：https://www.football-data.org/register
2. 注册账号
3. 登录后获取 API Key
4. 免费版每天 100 次请求，足够日常使用

---

## 步骤 4：推送代码到 GitHub

```bash
# 切换到main分支
git checkout -b main

# 推送到远程仓库
git push -u origin main
```

系统会提示输入 GitHub 用户名和密码（或 Personal Access Token）。

> **注意**：如果启用了 2FA，需要使用 Personal Access Token 代替密码。

---

## 步骤 5：启用 GitHub Actions

推送代码后，GitHub Actions 会自动检测 `.github/workflows/` 目录下的工作流。

### 查看工作流状态

1. 打开 GitHub 仓库
2. 点击 **Actions** 标签页
3. 你会看到 "Daily Update Intelligence" 工作流

### 手动触发测试

1. 点击工作流名称
2. 点击左侧 **"Run workflow"** 按钮
3. 选择 **"Run workflow"** 下拉菜单
4. 点击绿色按钮手动触发

### 验证执行

1. 等待工作流执行完成（约 2-3 分钟）
2. 点击具体的运行记录
3. 查看各个步骤的日志输出

---

## 步骤 6：配置工作流（可选）

编辑 `.github/workflows/daily-update.yml` 自定义工作流行为：

```yaml
# 定时执行时间（修改 cron 表达式）
schedule:
  - cron: '0 16 * * *'  # 每天16:00 UTC = 北京时间每天00:00

# 如果需要更改执行频率：
# 每6小时: '0 */6 * * *'
# 每天3次（8点、12点、18点）: '0 8,12,18 * * *'
# 每周一: '0 16 * * 1'
```

---

## 🔧 本地测试

在将代码推送到 GitHub 之前，建议先在本地测试：

### 1. 测试数据获取

```bash
# 激活conda环境
conda activate Langchain_env

# 设置环境变量（可选）
export DEEPSEEK_API_KEY="你的DeepSeek密钥"
export FOOTBALL_API_KEY="你的Football-Data密钥"

# 运行测试
cd scripts
python fetch_football_data.py
```

### 2. 测试AI情报生成

```bash
# 确保环境变量已设置
python generate_intelligence.py
```

### 3. 测试skill.md更新

```bash
python update_skill_md.py
```

### 4. 验证GitHub Actions工作流

在本地测试完整流程：

```bash
# 安装依赖
pip install -r requirements.txt

# 运行完整流程
python scripts/fetch_football_data.py
python scripts/generate_intelligence.py
python scripts/update_skill_md.py

# 检查更改
git diff skill.md

# 如果满意，提交并推送
git add .
git commit -m "test: 测试每日情报更新流程"
git push
```

---

## 📊 监控和日志

### 查看工作流运行历史

1. 打开 GitHub 仓库
2. 点击 **Actions** 标签页
3. 查看所有运行记录

### 查看特定运行的日志

1. 点击运行记录
2. 点击具体的 job
3. 查看每个 step 的日志输出

### 设置通知（可选）

1. 进入 **Settings** → **Notifications**
2. 配置 Actions 通知规则

---

## ⚙️ 自定义配置

### 修改配置文件

创建 `config.ini` 或 `config.yaml`：

```ini
# config.ini
[api]
deepseek_api_key = sk-your-key-here
football_api_key = your-key-here

[update]
schedule_time = 08:00
enabled = true
```

### 修改预测参数

编辑 `worldcup_predict.py` 或 `backend/predictor.py`：

```python
# 预测参数
TEMPERATURE = 0.7  # 创造性（0-1，越低越确定性）
MAX_TOKENS = 2000  # 最大输出长度
MODEL = "deepseek-v4-pro"  # 使用的模型
```

### 修改更新频率

编辑 `.github/workflows/daily-update.yml`：

```yaml
on:
  schedule:
    - cron: '0 16 * * *'  # 修改为你的时间
```

---

## 🐛 故障排查

### 问题1：工作流失败

**症状**：Actions 显示红色 X

**解决方法**：
1. 点击失败的运行记录
2. 查看失败步骤的日志
3. 常见问题：
   - API Key 无效 → 检查 Secrets 配置
   - API 配额用完 → 检查账户余额
   - 网络问题 → 重试

### 问题2：没有自动触发

**症状**：定时任务没有执行

**解决方法**：
1. 确认 `.github/workflows/daily-update.yml` 存在
2. 检查 cron 表达式是否正确
3. 手动触发一次测试

### 问题3：情报没有更新

**症状**：skill.md 第六节没有变化

**解决方法**：
1. 检查 GitHub Actions 日志
2. 确认情报生成步骤成功
3. 确认提交推送步骤成功

### 问题4：API 错误

**症状**：`AuthenticationError` 或 `RateLimitError`

**解决方法**：
1. 检查 API Key 是否正确
2. 检查账户余额
3. 等待配额重置（通常1小时后）

---

## 🔒 安全建议

### 保护敏感信息

1. **不要将真实 API Key 上传**到代码库
2. **使用 GitHub Secrets** 存储敏感配置
3. **定期轮换** API Key
4. **监控使用量**，防止异常消耗

### 访问控制

- **Public 仓库**：任何人都能看到代码
- **Private 仓库**：只有你和指定协作者能看到
- **Secrets**：即使 Public 仓库，Secrets 也不会暴露

---

## 📈 优化建议

### 降低 API 成本

1. **减少更新频率**：从每天多次改为每天1次
2. **缓存数据**：使用本地文件缓存比赛数据
3. **使用免费 API**：Football-Data 免费版足够日常使用

### 提高可靠性

1. **添加错误重试**：使用 try-except 和 retry 机制
2. **添加超时设置**：防止 API 调用挂起
3. **日志记录**：详细的日志便于问题排查

### 扩展功能

1. **添加邮件通知**：工作流完成后发送邮件
2. **添加 Slack 集成**：在 Slack 中接收通知
3. **添加数据可视化**：生成比赛图表

---

## 📞 获取帮助

如果遇到问题：

1. 查看 **GitHub Actions 日志**
2. 查看本项目的 **Issues** 页面
3. 搜索 **Stack Overflow**
4. 在 **GitHub Discussions** 中提问

---

## 🎉 部署完成检查清单

完成所有步骤后，确认以下项目：

- [ ] GitHub 仓库已创建
- [ ] 代码已推送到仓库
- [ ] GitHub Secrets 已配置
- [ ] GitHub Actions 已启用
- [ ] 手动触发测试成功
- [ ] 自动定时任务配置正确

---

## 📚 相关资源

- GitHub Actions 文档：https://docs.github.com/en/actions
- DeepSeek API 文档：https://platform.deepseek.com/docs
- Football-Data API：https://www.football-data.org/documentation/api

---

**恭喜！您的项目已成功部署到 GitHub 并配置了每日自动更新功能！** 🎊

有任何问题，请随时提问！⚽