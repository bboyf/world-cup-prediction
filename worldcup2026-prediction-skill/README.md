<div align="center">

# ⚽ WorldCup-2026-Prediction-Skill

### 绿茵神算 · 2026 FIFA World Cup AI Prediction Engine

**一份 system prompt,把任意大模型驯成专业世界杯预测引擎**
*Turn any LLM into a deterministic World Cup prediction engine with one prompt.*

[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
[![Skill Version](https://img.shields.io/badge/skill-v1.0-blue.svg?style=flat-square)](skill.md)
[![Stars](https://img.shields.io/github/stars/TradingAi666/worldcup2026-prediction-skill?style=flat-square&color=yellow)](https://github.com/TradingAi666/worldcup2026-prediction-skill/stargazers)
[![Forks](https://img.shields.io/github/forks/TradingAi666/worldcup2026-prediction-skill?style=flat-square&color=orange)](https://github.com/TradingAi666/worldcup2026-prediction-skill/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/TradingAi666/worldcup2026-prediction-skill?style=flat-square)](https://github.com/TradingAi666/worldcup2026-prediction-skill/commits/main)
[![Issues](https://img.shields.io/github/issues/TradingAi666/worldcup2026-prediction-skill?style=flat-square)](https://github.com/TradingAi666/worldcup2026-prediction-skill/issues)

[![Language](https://img.shields.io/badge/lang-中文%20%7C%20English-red.svg?style=flat-square)](#)
[![Compatible](https://img.shields.io/badge/LLM-DeepSeek%20%7C%20Qwen%20%7C%20GPT%20%7C%20Claude-purple.svg?style=flat-square)](#兼容模型)
[![Format](https://img.shields.io/badge/output-strict%20JSON-success.svg?style=flat-square)](#输出契约)
[![Teams](https://img.shields.io/badge/teams-48-9cf.svg?style=flat-square)](skill.md#四球队资料库核心依据)
[![Matches](https://img.shields.io/badge/matches-64-9cf.svg?style=flat-square)](#)
[![Updated](https://img.shields.io/badge/data-2026--06--11-informational.svg?style=flat-square)](#)

🔗 **Live Demo** · [worldcup.youliaoyun.com](http://worldcup.youliaoyun.com)
&nbsp;&nbsp;|&nbsp;&nbsp;
🇨🇳 **中文** · [skill.md](skill.md)
&nbsp;&nbsp;|&nbsp;&nbsp;
📺 **Video Walkthrough** · *Coming soon*

---

</div>

> *"GUI 是给人手设计的,CLI 是给 AI 设计的。Skill 是给 LLM 用的提示词。"*
> — 项目作者 · 柱子哥

## 📚 目录 · Table of Contents

- [✨ 核心特性](#-核心特性)
- [🎯 它解决什么问题](#-它解决什么问题)
- [🧠 架构 · 四层约束](#-架构--四层约束)
- [🚀 快速开始](#-快速开始)
- [🌐 兼容模型](#-兼容模型)
- [📦 输出契约](#-输出契约)
- [🇲🇽 分组与赛程](#-分组与赛程)
- [🔄 每日情报更新流程](#-每日情报更新流程)
- [💡 适用场景](#-适用场景)
- [🛣️ Roadmap](#️-roadmap)
- [❓ FAQ](#-faq)
- [🤝 Contributing](#-contributing)
- [⚠️ 声明](#️-声明)
- [📜 License](#-license)
- [🙏 致谢](#-致谢)

---

## ✨ 核心特性

| 特性 | 说明 |
|:---|:---|
| 🎯 **零依赖** | 单文件 `skill.md`,无需训练、无需向量库、无需 API server |
| 🧱 **资料锁死** | 48 队完整资料库写在 prompt 内,模型只许引用 / 不许编造 |
| 📐 **方法论固化** | 4 维评估权重 + 胜率上限 85% 铁律,杜绝"凭感觉胡说" |
| 📦 **严格 JSON** | 输出格式锁死,前端可直接渲染,零后处理 |
| 🔄 **可热更新** | 末尾"每日情报区"为动态注入位,30 行更新 → 全 Skill 即时跟进 |
| 🌍 **多模型通用** | 任意 OpenAI 兼容接口即贴即用(DeepSeek / Qwen / GPT / Claude) |
| 🛡️ **内置红线** | 拒绝任何投注 / 赔率 / 下注建议,娱乐讨论场景安全 |
| 📊 **可视化友好** | JSON 字段映射设计已对前端卡片组件优化 |

---

## 🎯 它解决什么问题

直接问大模型 *"墨西哥对南非谁会赢?"*,你会得到:

❌ **编造历史交锋** — 两队从未交手,它能列出"上次 2-1"
❌ **编造伤病信息** — 编造"梅西腿伤上半场退场"
❌ **格式飘忽不定** — 一会儿大段文字,一会儿 markdown,一会儿表格
❌ **信息严重过时** — 训练数据截止到 2024,2026 预选赛它不知道
❌ **无法接前端** — 自然语言输出根本没法解析

本 Skill 用 **4 层约束** 一次治住所有问题:

```
┌─────────────────────────────────────────────────────────┐
│            一份 system prompt = 一个垂类小模型            │
└─────────────────────────────────────────────────────────┘
                            ↓
┌────────────────┬─────────────────┬─────────────────────┐
│  Layer 1       │  Layer 2        │  Layer 3            │
│  📚 资料库     │  📐 方法论      │  📦 输出契约         │
│  48 队锁死     │  4 维权重       │  严格 JSON Schema   │
└────────────────┴─────────────────┴─────────────────────┘
                            +
┌─────────────────────────────────────────────────────────┐
│  Layer 4 · 🔄 每日情报区(动态覆盖位 · 实时跟进伤停)      │
└─────────────────────────────────────────────────────────┘
```

---

## 🧠 架构 · 四层约束

```
                    用户提问
                       │
                       ▼
        ┌──────────────────────────────┐
        │  LLM (DeepSeek / GPT / ...)  │
        └──────────────┬───────────────┘
                       │
       ┌───────────────┴────────────────┐
       │     skill.md (system prompt)    │
       ├────────────────────────────────┤
       │                                 │
       │  ① 资料库 ─ Knowledge Base      │
       │     ├─ 48 队分档(4 档)         │
       │     ├─ 核心球员 + 状态          │
       │     ├─ 教练 + 体系              │
       │     └─ 隐忧 + 历史底蕴          │
       │                                 │
       │  ② 方法论 ─ Methodology         │
       │     ├─ 近期状态  ████████  40%  │
       │     ├─ 硬实力    ██████    30%  │
       │     ├─ 历史交锋  ███       15%  │
       │     ├─ 情境因素  ███       15%  │
       │     └─ 🚫 胜率硬上限 ≤ 85%      │
       │                                 │
       │  ③ 输出契约 ─ Output Schema     │
       │     └─ JSON · 字段固定 · 总和=100│
       │                                 │
       │  ④ 每日情报区 ─ Daily Brief     │
       │     └─ 动态覆盖位 · 优先级最高   │
       │                                 │
       └─────────────┬──────────────────┘
                     │
                     ▼
        ┌──────────────────────────────┐
        │   严格 JSON 预测结果(前端可渲染)│
        └──────────────────────────────┘
```

### 各层职责拆解

#### Layer 1 · 资料库

| 档位 | 球队示例 |
|:---|:---|
| 🥇 夺冠热门档 | 阿根廷 · 西班牙 · 法国 · 英格兰 · 巴西 |
| 🥈 一线强队档 | 德国 · 葡萄牙 · 荷兰 · 乌拉圭 · 克罗地亚 · 摩洛哥 · 哥伦比亚 · 日本 · 挪威 |
| 🏠 二线 / 东道主档 | 美国 · 墨西哥 · 加拿大 · 瑞士 · 韩国 · 比利时 · 塞内加尔 · ... |
| 🌱 中游 / 新军档 | 库拉索 · 佛得角 · 乌兹别克斯坦 · 约旦 · 海地 · ... |

**全部 48 队的核心球员、近况、隐忧均写死在 [`skill.md`](skill.md#四球队资料库核心依据) 内,模型只许引用,严禁编造。**

#### Layer 2 · 方法论

| 维度 | 权重 | 涵盖内容 |
|:---|:---:|:---|
| 近期状态 | **40%** | 预选赛表现 · 大赛成绩 · 核心球员状态与伤病 |
| 球队硬实力 | **30%** | 阵容厚度 · 世界排名档位 · 历史大赛底蕴 |
| 历史交锋 | **15%** | 两队过往交手记录(允许常识补充 / 必须标注不确定) |
| 情境因素 | **15%** | 东道主主场 · 气候 · 抗压经验 · 阵容年龄 |

> ⚠️ **铁律:实力悬殊也不得给出超过 85% 的胜率(足球有偶然性 — 2022 沙特 vs 阿根廷)**

#### Layer 3 · 输出契约

详见下方 [输出契约](#-输出契约) 章节。

#### Layer 4 · 每日情报区

详见下方 [每日情报更新流程](#-每日情报更新流程) 章节。

---

## 🚀 快速开始

### Method 1 — cURL · 一行直接跑

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{
    "model": "deepseek-v4-pro",
    "response_format": {"type": "json_object"},
    "messages": [
      {"role": "system", "content": "<skill.md 全文粘贴到这里>"},
      {"role": "user", "content": "请预测这场 2026 世界杯比赛:【小组赛】墨西哥 vs 南非。严格按约束文档的 JSON 格式输出。"}
    ]
  }'
```

### Method 2 — Python · 接进你的应用

```python
import openai, pathlib, json

SKILL = pathlib.Path("skill.md").read_text(encoding="utf-8")
client = openai.OpenAI(base_url="https://api.deepseek.com", api_key="...")

def predict(team_a: str, team_b: str, stage: str = "小组赛") -> dict:
    resp = client.chat.completions.create(
        model="deepseek-v4-pro",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SKILL},
            {"role": "user",   "content": f"请预测这场 2026 世界杯比赛:【{stage}】{team_a} vs {team_b}。严格按约束文档的 JSON 格式输出。"},
        ],
    )
    return json.loads(resp.choices[0].message.content)

print(predict("墨西哥", "南非"))
```

### Method 3 — Node.js · TypeScript

```ts
import OpenAI from "openai"
import { readFileSync } from "node:fs"

const SKILL = readFileSync("skill.md", "utf-8")
const client = new OpenAI({ baseURL: "https://api.deepseek.com", apiKey: process.env.DEEPSEEK_API_KEY })

export async function predict(teamA: string, teamB: string, stage = "小组赛") {
  const r = await client.chat.completions.create({
    model: "deepseek-v4-pro",
    response_format: { type: "json_object" },
    messages: [
      { role: "system", content: SKILL },
      { role: "user",   content: `请预测这场 2026 世界杯比赛:【${stage}】${teamA} vs ${teamB}。严格按约束文档的 JSON 格式输出。` },
    ],
  })
  return JSON.parse(r.choices[0].message.content!)
}
```

---

## 🌐 兼容模型

| Provider | Model | response_format | 实测稳定性 |
|:---|:---|:---:|:---:|
| **DeepSeek** | `deepseek-v4-pro` | ✅ `json_object` | ⭐⭐⭐⭐⭐ |
| **Alibaba Qwen** | `qwen-max-latest` | ✅ `json_object` | ⭐⭐⭐⭐⭐ |
| **OpenAI** | `gpt-4o` / `gpt-5` | ✅ `json_schema` | ⭐⭐⭐⭐⭐ |
| **Anthropic** | `claude-opus-4-8` | ⚠️ 需 `tool_use` 强制 | ⭐⭐⭐⭐ |
| **Doubao** | `doubao-pro-256k` | ✅ `json_object` | ⭐⭐⭐⭐ |
| **Moonshot Kimi** | `kimi-k2` | ✅ `json_object` | ⭐⭐⭐⭐ |
| **ZhiPu GLM** | `glm-5-plus` | ✅ `json_object` | ⭐⭐⭐ |

> 推荐 DeepSeek-V4-Pro:成本最低、JSON 稳定、中文表达自然。

---

## 📦 输出契约

每次调用返回一份**严格 JSON**,字段、类型、长度全部锁死:

```json
{
  "teamA":           { "name": "墨西哥", "winProb": 70 },
  "draw":            20,
  "teamB":           { "name": "南非",   "winProb": 10 },
  "predictedScore":  "2-0",
  "confidence":      "高",
  "keyFactors":      [
    "阿兹特克主场揭幕战气势如虹",
    "墨西哥金杯冠军班底实力碾压",
    "南非时隔16年重返经验不足"
  ],
  "analysis":        "东道主墨西哥在阿兹特克球场迎战南非,实力与主场优势明显……",
  "playersToWatch":  [
    { "team": "墨西哥", "player": "圣地亚哥·希门尼斯", "reason": "米兰前锋状态火热" },
    { "team": "南非",   "player": "佩西·塔乌",         "reason": "南非进攻核心,肩负爆冷希望" }
  ]
}
```

### 字段约束表

| 字段 | 类型 | 约束 | 备注 |
|:---|:---:|:---|:---|
| `teamA.name` / `teamB.name` | `string` | 中文队名 | 必须与资料库一致 |
| `teamA.winProb` / `teamB.winProb` / `draw` | `int` | `0 ≤ x ≤ 85` | **三者总和 == 100** |
| `predictedScore` | `string` | `^\d{1,2}-\d{1,2}$` | e.g. `"2-0"` |
| `confidence` | `enum` | `高 / 中 / 低` | 三选一 |
| `keyFactors` | `string[]` | **3 ≤ len ≤ 5** · 每条 ≤ 15 字 | 关键判断依据 |
| `analysis` | `string` | ≤ 150 字 | 专业解说式分析 |
| `playersToWatch` | `object[]` | **len == 2** · 每队 1 人 | 关键先生推荐 |

### 阶段(stage)取值

```
小组赛 → 32 强 → 16 强 → 8 强 → 半决赛 → 决赛
```

> 淘汰赛的 `draw` 概率代表 **90 分钟战平进加时/点球**(对应 `analysis` 须说明谁更可能笑到最后)。

---

## 🇲🇽 分组与赛程

赛事:**2026 FIFA World Cup**(美国 · 加拿大 · 墨西哥三国联办)
日期:**2026 年 6 月 11 日 — 7 月 19 日**
揭幕战:**6 月 11 日 · 墨西哥 vs 南非 · 阿兹特克球场**

<details>
<summary><b>👉 点击展开 12 个小组完整分组表</b></summary>

| 组 | 球队 |
|:---:|:---|
| A | 🇲🇽 墨西哥 · 🇿🇦 南非 · 🇰🇷 韩国 · 🇨🇿 捷克 |
| B | 🇨🇦 加拿大 · 🇧🇦 波黑 · 🇶🇦 卡塔尔 · 🇨🇭 瑞士 |
| C | 🇧🇷 巴西 · 🇲🇦 摩洛哥 · 🇭🇹 海地 · 🏴󠁧󠁢󠁳󠁣󠁴󠁿 苏格兰 |
| D | 🇺🇸 美国 · 🇵🇾 巴拉圭 · 🇦🇺 澳大利亚 · 🇹🇷 土耳其 |
| E | 🇩🇪 德国 · 🇨🇼 库拉索 · 🇨🇮 科特迪瓦 · 🇪🇨 厄瓜多尔 |
| F | 🇳🇱 荷兰 · 🇯🇵 日本 · 🇸🇪 瑞典 · 🇹🇳 突尼斯 |
| G | 🇧🇪 比利时 · 🇪🇬 埃及 · 🇮🇷 伊朗 · 🇳🇿 新西兰 |
| H | 🇪🇸 西班牙 · 🇨🇻 佛得角 · 🇸🇦 沙特 · 🇺🇾 乌拉圭 |
| I | 🇫🇷 法国 · 🇸🇳 塞内加尔 · 🇮🇶 伊拉克 · 🇳🇴 挪威 |
| J | 🇦🇷 阿根廷 · 🇩🇿 阿尔及利亚 · 🇦🇹 奥地利 · 🇯🇴 约旦 |
| K | 🇵🇹 葡萄牙 · 🇨🇩 刚果金 · 🇺🇿 乌兹别克斯坦 · 🇨🇴 哥伦比亚 |
| L | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 英格兰 · 🇭🇷 克罗地亚 · 🇬🇭 加纳 · 🇵🇦 巴拿马 |

每组前两名 + 8 个成绩最好的第三名 → 晋级 32 强淘汰赛。

</details>

---

## 🔄 每日情报更新流程

**核心设计:写死的资料库 + 每天可覆盖的情报位 = 动静结合。**

```
┌─────────────────────────────────────────┐
│  skill.md  (~10 KB · 一二三四五节 锁死)  │
│  ────────────────────────────────────   │
│  一、赛事基本盘                          │
│  二、预测方法论                          │
│  三、输出格式契约                        │
│  四、48 队球队资料库                     │
│  五、红线                                │
│                                         │
│  ↓↓↓ 永远只动这一节 ↓↓↓                   │
│                                         │
│  六、最新情报(每日更新区)               │
│   - 情报日期:YYYY-MM-DD                 │
│   - 未来 48h 参赛队伤停 / 状态要点       │
│   - 与第四节冲突时,以本节为准            │
└─────────────────────────────────────────┘
```

### 推荐自动化方式

| 方式 | 适用场景 |
|:---|:---|
| 🤖 **AI Agent 每日定时跑** | 拉新闻 → LLM 提取要点 → 写入第六节 → push |
| 🕸️ **爬虫 + 模板** | 抓 BBC / ESPN / 体坛周报 → 模板填充 → push |
| ✍️ **人工值守** | 大赛期间编辑 1 名 · 每日 5 分钟手动整理 |

> ⚠️ **永远不要动一至五节**——这是资料库稳定性的保证。

---

## 💡 适用场景

- 📱 **球迷应用 / 小程序** — 直接喂给前端渲染预测卡片
- 🤖 **微信群 / Discord 机器人** — 群友提问即出预测
- 📊 **数据可视化看板** — 64 场比赛批量预测 · 跑出冠军树
- 🎙️ **内容创作辅助** — 解说稿 / 短视频脚本基础数据
- 🎮 **预测游戏 / 竞猜社区** — 作为 AI 对手 / 参考意见(*非投注*)
- 🧪 **Prompt Engineering 教学样本** — 极简结构 · 教科书级约束设计

---

## 🛣️ Roadmap

- [x] **v1.0** — 48 队完整资料库 + 4 层约束 + 严格 JSON
- [x] **v1.0** — DeepSeek / Qwen / GPT / Claude 全模型适配
- [x] **v1.0** — 在线 Demo 站(worldcup.youliaoyun.com)
- [ ] **v1.1** — 每日情报区自动化更新 GitHub Action
- [ ] **v1.1** — 英文版 `skill.en.md`
- [ ] **v1.2** — 球员级别预测(进球者 / MVP / 黄牌)
- [ ] **v1.2** — 赛后回测脚本(对照实际结果统计命中率)
- [ ] **v2.0** — 升级为 Skill Pack:把方法论抽象为可复用的"赛事预测 Skill 模板",支持欧洲杯 / 奥运 / NBA

---

## ❓ FAQ

<details>
<summary><b>Q1: 这是机器学习模型吗?需要训练吗?</b></summary>

**不是,不需要。** 本项目本质是**一份 system prompt(文本文件)**。
你拿任何一个开箱即用的 LLM(GPT / Claude / DeepSeek 等),把 `skill.md` 全文塞进它的 system 消息,它就具备了"世界杯专家"的能力。

零训练、零向量库、零依赖。
</details>

<details>
<summary><b>Q2: 预测准确率有多高?会不会瞎说?</b></summary>

本 Skill 通过四层约束**大幅降低**瞎说概率,但**不保证**比赛结果——足球本身的偶然性谁都消不掉。
我们刻意把胜率上限锁在 85%,就是为了承认"再悬殊也可能爆冷"(沙特 vs 阿根廷)。

**这是娱乐和讨论工具,不是先知。**
</details>

<details>
<summary><b>Q3: 我能拿这个去做付费应用吗?</b></summary>

MIT 协议,**可以**。但请注意:
- 仅限娱乐与球迷讨论场景
- **严禁**用于任何投注、博彩、赔率、下注业务(Skill 自身已内置红线拒绝)
- 如果做了酷的东西,欢迎在 Issues / PR 里分享一下
</details>

<details>
<summary><b>Q4: 资料库里我喜欢的球队漏写了/写错了,怎么办?</b></summary>

欢迎提 PR 修订 `skill.md` 第四节。
请在 PR 描述里贴上信息来源(官方/权威媒体),不接受小道消息。
</details>

<details>
<summary><b>Q5: 每天的伤停情报怎么自动更新?</b></summary>

短期(v1.0):手动在第六节顶部覆盖一次,即可生效。
中期(v1.1 规划):GitHub Action + LLM 每日自动抓取新闻 → 提取要点 → PR 第六节。
长期(v2.0 规划):抽象成"赛事 Skill 模板",任意赛事可复用本模式。
</details>

<details>
<summary><b>Q6: 为什么淘汰赛的"平局"概率也要给?</b></summary>

淘汰赛不存在平局,`draw` 字段表示 **90 分钟战平进入加时/点球**的概率。
`analysis` 字段中会进一步说明加时/点球阶段谁更有可能笑到最后。
</details>

---

## 🤝 Contributing

欢迎以任何形式贡献:

- ⭐ **Star 本项目** — 最简单的支持方式
- 🐛 **报告 Bug / 提 Issue** — 发现预测离谱、字段约束失效、文档错漏
- 📝 **修订资料库** — 球员转会 / 教练变更 / 大赛阵容(请附信息来源)
- 🌍 **翻译** — 帮助本 Skill 走向更多语言
- 💡 **二次创作** — 做了自己的预测站 / 小程序?来 Issues 里炫一下

### 提交流程

```bash
git clone https://github.com/TradingAi666/worldcup2026-prediction-skill.git
cd worldcup2026-prediction-skill
git checkout -b feature/your-update
# 修改 skill.md 或 README.md
git commit -m "docs: update XX team roster"
git push origin feature/your-update
# 然后到 GitHub 开 PR
```

---

## ⚠️ 声明

- 🎯 本项目**仅供娱乐与球迷讨论**
- 🚫 Skill 内置红线 — 拒绝输出任何**投注、赔率、下注建议**
- 🧠 预测结果**不构成任何参考依据**,请理性看球
- ⚖️ 所有球队、球员、教练信息均为公开资料,不涉及隐私
- 🌍 仅供 **2026 FIFA World Cup** 一届使用,赛后将归档

---

## 📜 License

[MIT License](LICENSE) © 2026 [TradingAi666](https://github.com/TradingAi666)

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, ...
```

---

## 🙏 致谢

- **FIFA** — 提供本届赛事赛程与分组信息
- **DeepSeek / Qwen / OpenAI / Anthropic** — 提供本 Skill 赖以运行的 LLM 能力
- **柱子哥(TzFilm)社区** — 持续的反馈与共创
- 所有 ⭐ **本项目的朋友** — 是你们让"提示词也可以开源"这件事被看见

---

<div align="center">

**⚽ 让我们拭目以待 · See You at the Pitch ⚽**

[![Star History Chart](https://api.star-history.com/svg?repos=TradingAi666/worldcup2026-prediction-skill&type=Date)](https://star-history.com/#TradingAi666/worldcup2026-prediction-skill&Date)

Made with ⚽ by [@TradingAi666](https://github.com/TradingAi666) · *Open-sourced on the opening day, June 11, 2026.*

</div>
