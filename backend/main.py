# -*- coding: utf-8 -*-
"""
FastAPI 主程序
2026世界杯AI预测引擎 - Web服务
"""

import sys
from pathlib import Path

# 将项目根目录添加到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from backend.api import router
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 创建FastAPI应用
app = FastAPI(
    title="2026世界杯AI预测引擎",
    description="基于DeepSeek AI的世界杯比赛预测服务",
    version="1.0.0"
)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 注册路由
app.include_router(router, prefix="/api", tags=["预测"])

# 首页路由
@app.get("/", response_class=HTMLResponse)
async def read_root():
    """返回前端页面"""
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/index.html", response_class=HTMLResponse)
async def read_index():
    """返回前端页面"""
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    print("=" * 60)
    print("[2026世界杯AI预测引擎] - Web服务启动中")
    print("=" * 60)
    print("服务地址：http://localhost:8000")
    print("API文档：http://localhost:8000/docs")
    print("=" * 60)
    
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )