@echo off
chcp 65001 > nul
title 2026世界杯AI预测引擎 - Web服务

echo.
echo ==============================================================
echo.
echo          2026世界杯AI预测引擎 - Web服务启动中...
echo.
echo ==============================================================
echo.

REM 激活conda环境
call conda activate Langchain_env

REM 检查并安装依赖
echo [1/3] 检查依赖...
pip show fastapi > nul 2>&1
if %errorlevel% neq 0 (
    echo [2/3] 安装依赖包...
    pip install -r requirements-web.txt
) else (
    echo [2/3] 依赖已安装，跳过
)

REM 启动服务
echo [3/3] 启动Web服务...
echo.
echo 服务地址：http://localhost:8000
echo API文档：http://localhost:8000/docs
echo.
echo 按 Ctrl+C 停止服务
echo.

python backend/main.py

pause