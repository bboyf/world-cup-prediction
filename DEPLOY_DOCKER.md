# 2026世界杯AI预测引擎 - Docker部署指南

## 🚀 快速开始

### 前置要求

- Docker 20.10+
- Docker Compose 2.0+
- Git

---

## 📋 部署步骤

### 1. 克隆项目

```bash
git clone https://github.com/bboyf/world-cup-prediction.git
cd world-cup-prediction
```

### 2. 配置环境变量

```bash
# 复制环境变量配置示例
cp .env.example .env

# 编辑 .env 文件，填入你的API密钥
nano .env
```

填入以下内容：
```env
DEEPSEEK_API_KEY=sk-your-deepseek-api-key-here
FOOTBALL_API_KEY=your-football-data-api-key-here
```

### 3. 构建并启动

```bash
# 构建Docker镜像
docker-compose build

# 启动服务
docker-compose up -d

# 查看服务状态
docker-compose ps
```

### 4. 验证部署

```bash
# 检查服务健康状态
curl http://localhost:8000/api/health

# 查看日志
docker-compose logs -f web
```

---

## 🌐 访问应用

- **应用主页**：http://your-server-ip:8000
- **API文档**：http://your-server-ip:8000/docs
- **健康检查**：http://your-server-ip:8000/api/health

---

## 🐳 Docker Compose 命令

### 启动服务
```bash
docker-compose up -d
```

### 停止服务
```bash
docker-compose down
```

### 重启服务
```bash
docker-compose restart
```

### 查看日志
```bash
# 实时查看所有日志
docker-compose logs -f

# 只看Web服务日志
docker-compose logs -f web

# 查看最近100行日志
docker-compose logs --tail 100 web
```

### 进入容器
```bash
docker exec -it worldcup-prediction-web /bin/bash
```

### 重新构建
```bash
docker-compose up -d --build
```

---

## 🏗️ 使用Nginx反向代理（可选）

### 启用Nginx

```bash
# 启动所有服务（包括Nginx）
docker-compose --profile with-nginx up -d
```

### Nginx配置

Nginx会自动：
- 反向代理到FastAPI应用
- 提供静态文件缓存
- 启用Gzip压缩
- 配置SSL（需要手动配置证书）

---

## 🔒 安全配置

### 1. 修改API密钥

确保在 `.env` 文件中设置强密码：
```env
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxx
```

### 2. 配置防火墙

```bash
# 只开放必要端口
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --reload
```

### 3. 使用Nginx SSL（生产环境）

```bash
# 创建SSL证书目录
mkdir -p nginx/ssl

# 使用Let's Encrypt获取免费证书
certbot --nginx -d your-domain.com
```

---

## 📊 监控和维护

### 查看资源使用

```bash
docker stats
```

### 清理旧镜像

```bash
docker image prune -f
```

### 备份数据

```bash
# 备份数据目录
tar -czf backup-$(date +%Y%m%d).tar.gz data/
```

### 更新应用

```bash
# 拉取最新代码
git pull origin main

# 重新构建并启动
docker-compose up -d --build
```

---

## 🐛 故障排查

### 问题1：服务启动失败

**检查日志：**
```bash
docker-compose logs web
```

**常见原因：**
- API密钥未配置
- 端口被占用
- 内存不足

### 问题2：无法访问应用

**检查服务状态：**
```bash
docker-compose ps
```

**检查端口：**
```bash
netstat -tulpn | grep 8000
```

### 问题3：预测功能不工作

**检查API密钥：**
```bash
docker exec worldcup-prediction-web env | grep DEEPSEEK
```

**检查API余额：**
登录 DeepSeek 控制台检查余额

---

## 📝 目录结构

```
world-cup-prediction/
├── backend/              # FastAPI后端代码
├── scripts/              # 自动化脚本
├── templates/            # 前端HTML模板
├── static/               # 静态资源
├── worldcup2026-prediction-skill/  # AI skill文件
├── data/                 # 数据目录（运行时创建）
├── logs/                 # 日志目录（运行时创建）
├── nginx/                # Nginx配置
├── Dockerfile            # Docker镜像配置
├── docker-compose.yml    # Docker Compose配置
├── .env                  # 环境变量（需手动创建）
└── .env.example          # 环境变量示例
```

---

## 🎯 生产环境建议

### 1. 使用Nginx反向代理
- 提高性能和安全性
- 支持SSL终端
- 负载均衡

### 2. 配置SSL证书
```bash
# 使用Let's Encrypt
certbot --nginx -d your-domain.com
```

### 3. 配置日志轮转
在 `docker-compose.yml` 中添加：
```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```

### 4. 定期备份
```bash
# 每天凌晨3点备份
0 3 * * * tar -czf /backup/worldcup-$(date +\%Y\%m\%d).tar.gz /path/to/data
```

### 5. 监控
- 配置 Prometheus + Grafana 监控
- 设置告警通知

---

## 📞 获取帮助

如遇问题，请检查：
1. Docker日志：`docker-compose logs`
2. GitHub Issues：https://github.com/bboyf/world-cup-prediction/issues
3. 文档：项目 README.md

---

**部署成功！享受世界杯预测的乐趣！** ⚽🏆