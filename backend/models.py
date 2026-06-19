# -*- coding: utf-8 -*-
"""
数据模型定义
定义API请求和响应的数据结构
"""

from pydantic import BaseModel, Field
from typing import List, Optional

class PredictionRequest(BaseModel):
    """预测请求模型"""
    team_a: str = Field(..., description="主队名称（中文）")
    team_b: str = Field(..., description="客队名称（中文）")
    stage: str = Field(default="小组赛", description="比赛阶段")

class TeamPrediction(BaseModel):
    """球队预测模型"""
    name: str
    winProb: int

class Player(BaseModel):
    """关键球员模型"""
    team: str
    player: str
    reason: str

class PredictionResponse(BaseModel):
    """预测响应模型"""
    teamA: TeamPrediction
    draw: int
    teamB: TeamPrediction
    predictedScore: str
    confidence: str
    keyFactors: List[str]
    analysis: str
    playersToWatch: List[Player]

class APIResponse(BaseModel):
    """统一API响应格式"""
    success: bool
    message: str
    data: Optional[PredictionResponse] = None