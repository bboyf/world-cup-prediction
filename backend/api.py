# -*- coding: utf-8 -*-
"""
API路由模块
定义预测相关的API接口
"""

from fastapi import APIRouter, HTTPException
from backend.models import PredictionRequest, PredictionResponse, APIResponse
from backend.predictor import predict_match
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建路由
router = APIRouter()

@router.post("/predict", response_model=APIResponse)
async def predict(request: PredictionRequest):
    """
    预测世界杯比赛结果
    
    请求体:
        team_a: 主队名称
        team_b: 客队名称
        stage: 比赛阶段（可选，默认小组赛）
    
    返回:
        包含预测结果的JSON响应
    """
    try:
        logger.info(f"收到预测请求: {request.team_a} vs {request.team_b} ({request.stage})")
        
        # 调用预测引擎
        result = predict_match(
            team_a=request.team_a,
            team_b=request.team_b,
            stage=request.stage
        )
        
        logger.info(f"预测成功: {result.get('predictedScore', '未知')}")
        
        return APIResponse(
            success=True,
            message="预测成功",
            data=result
        )
    
    except Exception as e:
        logger.error(f"预测失败: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """健康检查接口"""
    return {"status": "ok", "service": "worldcup-prediction-api"}

@router.get("/teams")
async def get_teams():
    """
    获取所有支持的球队列表
    """
    # 48支世界杯参赛球队
    teams = {
        "夺冠热门档": ["阿根廷", "西班牙", "法国", "英格兰", "巴西"],
        "一线强队档": ["德国", "葡萄牙", "荷兰", "乌拉圭", "克罗地亚", "摩洛哥", "哥伦比亚", "日本", "挪威"],
        "二线/东道主档": ["美国", "墨西哥", "加拿大", "瑞士", "韩国", "比利时", "塞内加尔", "厄瓜多尔", "土耳其", "瑞典", "奥地利", "苏格兰"],
        "中游/新军档": ["捷克", "波黑", "卡塔尔", "巴拉圭", "科特迪瓦", "突尼斯", "伊朗", "新西兰", "沙特", "阿尔及利亚", "加纳", "巴拿马", "伊拉克", "乌兹别克斯坦", "约旦", "南非", "海地", "库拉索", "佛得角", "刚果金", "埃及", "澳大利亚"]
    }
    
    return {
        "success": True,
        "data": teams
    }