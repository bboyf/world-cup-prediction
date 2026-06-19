# 2026世界杯AI预测引擎 - Docker部署文件
# 基于Python 3.11 slim镜像

# 使用官方Python 3.11镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置时区
ENV TZ=Asia/Shanghai

# 防止Python缓冲输出
ENV PYTHONUNBUFFERED=1

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY backend/ ./backend/
COPY scripts/ ./scripts/
COPY templates/ ./templates/
COPY static/ ./static/
COPY worldcup2026-prediction-skill/ ./worldcup2026-prediction-skill/
COPY worldcup_predict.py ./
COPY start_web.bat ./
COPY .gitignore ./

# 创建数据目录
RUN mkdir -p /app/data

# 暴露端口
EXPOSE 8000

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/health')" || exit 1

# 启动命令
CMD ["python", "backend/main.py"]