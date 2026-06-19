/**
 * 2026世界杯AI预测引擎 - 前端逻辑
 */

// 预测按钮点击事件
document.getElementById('predictBtn').addEventListener('click', handlePredict);

// 支持 Enter 键提交
document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && e.target.tagName === 'INPUT') {
        handlePredict();
    }
});

/**
 * 处理预测请求
 */
async function handlePredict() {
    const teamA = document.getElementById('teamA').value.trim();
    const teamB = document.getElementById('teamB').value.trim();
    const stage = document.getElementById('stage').value;

    // 验证输入
    if (!teamA || !teamB) {
        showError('请输入主队和客队名称');
        return;
    }

    if (teamA === teamB) {
        showError('主队和客队不能相同');
        return;
    }

    // 显示加载状态
    showLoading();

    try {
        // 发送预测请求
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                team_a: teamA,
                team_b: teamB,
                stage: stage
            })
        });

        const result = await response.json();

        if (result.success && result.data) {
            // 显示预测结果
            displayResult(result.data, teamA, teamB);
        } else {
            throw new Error(result.message || '预测失败');
        }
    } catch (error) {
        console.error('预测请求失败:', error);
        showError('预测请求失败: ' + error.message);
    } finally {
        hideLoading();
    }
}

/**
 * 显示预测结果
 */
function displayResult(data, teamA, teamB) {
    // 更新标题
    document.getElementById('matchTitle').textContent = 
        `${teamA} vs ${teamB} - 预测结果`;

    // 更新比分
    document.getElementById('predictedScore').textContent = data.predictedScore || '-';

    // 更新置信度
    const confidenceEl = document.getElementById('confidence');
    confidenceEl.textContent = data.confidence || '-';
    confidenceEl.className = 'confidence-badge ' + (data.confidence || '');

    // 更新胜率
    document.getElementById('teamAName').textContent = data.teamA?.name || teamA;
    document.getElementById('teamBName').textContent = data.teamB?.name || teamB;
    
    const teamAProb = data.teamA?.winProb || 0;
    const teamBProb = data.teamB?.winProb || 0;
    const drawProb = data.draw || 0;

    document.getElementById('teamAProb').textContent = teamAProb + '%';
    document.getElementById('teamBProb').textContent = teamBProb + '%';
    document.getElementById('drawProb').textContent = drawProb + '%';

    // 动画显示概率条
    setTimeout(() => {
        document.getElementById('teamAProbBar').style.width = teamAProb + '%';
        document.getElementById('teamBProbBar').style.width = teamBProb + '%';
        document.getElementById('drawProbBar').style.width = drawProb + '%';
    }, 100);

    // 更新关键球员
    const playersList = document.getElementById('playersList');
    playersList.innerHTML = '';
    
    if (data.playersToWatch && data.playersToWatch.length > 0) {
        data.playersToWatch.forEach(player => {
            const playerEl = document.createElement('div');
            playerEl.className = 'player-item';
            playerEl.innerHTML = `
                <div class="player-info">
                    <div class="player-name">${player.player}</div>
                    <div class="player-team">${player.team}</div>
                </div>
                <div class="player-reason">${player.reason}</div>
            `;
            playersList.appendChild(playerEl);
        });
    }

    // 更新关键因素
    const keyFactors = document.getElementById('keyFactors');
    keyFactors.innerHTML = '';
    
    if (data.keyFactors && data.keyFactors.length > 0) {
        data.keyFactors.forEach(factor => {
            const li = document.createElement('li');
            li.textContent = factor;
            keyFactors.appendChild(li);
        });
    }

    // 更新综合分析
    document.getElementById('analysisText').textContent = data.analysis || '-';

    // 显示结果区域
    document.getElementById('resultSection').style.display = 'block';
    
    // 隐藏错误信息
    document.getElementById('errorMessage').style.display = 'none';

    // 滚动到结果区域
    document.getElementById('resultSection').scrollIntoView({ 
        behavior: 'smooth',
        block: 'start'
    });
}

/**
 * 显示加载状态
 */
function showLoading() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('predictBtn').disabled = true;
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('errorMessage').style.display = 'none';
}

/**
 * 隐藏加载状态
 */
function hideLoading() {
    document.getElementById('loading').style.display = 'none';
    document.getElementById('predictBtn').disabled = false;
}

/**
 * 显示错误信息
 */
function showError(message) {
    const errorEl = document.getElementById('errorMessage');
    errorEl.textContent = message;
    errorEl.style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
}

/**
 * 重置概率条（用于重新预测时）
 */
function resetProbBars() {
    document.getElementById('teamAProbBar').style.width = '0%';
    document.getElementById('teamBProbBar').style.width = '0%';
    document.getElementById('drawProbBar').style.width = '0%';
}

// 页面加载完成后重置概率条
document.addEventListener('DOMContentLoaded', function() {
    resetProbBars();
});