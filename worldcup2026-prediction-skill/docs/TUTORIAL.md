# 🚀 绿茵神算 Skill · 零基础部署教程

> 这份教程是给**完全没接触过命令行、没注册过 AI API、连 GitHub 是啥都不太清楚**的朋友写的。
> 全程**无需翻墙**、**全程国内服务**、**全程免费起步**。
> 如果你只想"花 3 分钟把它跑起来",直接看 **路径 A**。
> 如果你想"用得舒服点、能反复调",看 **路径 B**。
> 如果你是开发者想批量调用 / 接到自己的程序里,看 **路径 C**。

---

## 📋 你将得到什么

跟完这份教程,你会拥有一个**自己电脑上的世界杯预测 AI 助手**,可以这样问它:

> 你:**"请预测这场 2026 世界杯比赛:【小组赛】墨西哥 vs 南非"**
> AI:返回一份漂亮的 JSON 预测结果——胜平负概率、预测比分、关键先生、专业解说。

---

## 🛒 全程要准备的东西(共 3 件)

| # | 物料 | 哪里拿 | 花钱吗 |
|:---:|:---|:---|:---:|
| 1 | **`skill.md` 文件** | 从 GitHub 仓库下载 | 免费 |
| 2 | **DeepSeek API Key** | deepseek.com 注册并领取 | 注册送 5 元 · 跑 1000 场预测花不完 |
| 3 | **Agent 工具(三选一)** | 网页版 / Trae / Codex CLI | 全部免费 |

> 💡 为什么用 DeepSeek?**国内可访问、无需翻墙、JSON 输出稳定、中文表达自然、最便宜。** 同款步骤换成通义千问也能跑,只需要改一个网址。

---

# 📥 第 0 步:下载 skill.md(所有路径共用)

无论你走哪条路径,都需要先拿到 `skill.md` 这个文件。

### 方法 ① 网页直接下载(推荐 · 不需要装 Git)

1. 浏览器打开:**https://github.com/TradingAi666/worldcup2026-prediction-skill**
2. 看到文件列表里有一行 `skill.md`,**点它**
3. 进入文件页面,右上角找到 **"Raw"** 或下载按钮(⬇️ icon)
4. **右键 → 另存为 → skill.md**,保存到电脑桌面

> 💡 文件大小只有 **10KB**,本质就是一段中文文本,你可以用记事本/TextEdit 直接打开看。

### 方法 ② 命令行 clone(给会用 Git 的朋友)

```bash
git clone https://github.com/TradingAi666/worldcup2026-prediction-skill.git
cd worldcup2026-prediction-skill
```

---

# 🔑 第 0.5 步:领一个 DeepSeek API Key(所有路径共用)

> **不要被"API Key"这四个字吓退,这就是 AI 给你的一串密码,凭这串密码你才能用它的服务。**

### 详细步骤(共 6 步)

1. **打开**:https://platform.deepseek.com
2. 右上角 **"登录 / 注册"** → 用**微信扫码**就能登录(无需手机号验证)
3. 登录后,网页左侧菜单找到 **"API Keys"**(中文界面叫"API 密钥")
4. 点 **"创建新的 API Key"** 按钮
5. 取个名字随便起,比如 `worldcup`,点确认
6. ⚠️ **会弹出一串以 `sk-` 开头的字符串,这就是你的 API Key**
   - 比如:`sk-1234567890abcdef1234567890abcdef`
   - **立刻复制并存到一个安全的地方**(比如微信发给自己),它只显示一次

### 关于充值

- 注册账号默认会赠送 **5 元免费额度**,够你跑 ~500 场比赛预测
- 想充更多:左侧 **"充值"** 菜单,支持微信/支付宝,最低 ¥1 起充
- DeepSeek-V4-Pro 的价格:每 100 万 tokens 约 1 元,1 场预测 ≈ 0.005 元

---

# 🟢 路径 A · 最小白 — 网页直接用(0 安装 · 3 分钟)

**适合人群**:第一次接触 AI,只想"快速体验一下能不能用",不想装任何软件。
**所需时间**:3 分钟
**所需技能**:会用浏览器 ✅

---

## 步骤 A1 · 打开 DeepSeek 网页 Chat

1. 浏览器打开:**https://chat.deepseek.com**
2. 用同一个微信登录(和申请 API Key 那个账号是一回事)
3. 你会看到一个像 ChatGPT 一样的聊天界面

📷 *[截图位:DeepSeek 主界面 · 中间一个对话框]*

---

## 步骤 A2 · 注入 Skill(关键一步)

1. **打开你下载好的 `skill.md`** 文件(双击,用记事本/文本编辑器打开)
2. **`Ctrl+A` 全选 → `Ctrl+C` 复制全文**
3. 回到 DeepSeek 聊天框,**粘贴进去**(`Ctrl+V`)
4. 在粘贴内容的**最后一行**,加一句:

   ```
   ---
   以上是你的系统约束文档,请严格遵守。
   现在我要预测一场比赛:【小组赛】墨西哥 vs 南非。
   请按文档定义的 JSON 格式输出。
   ```

5. 点 **发送** 按钮(或按回车)

📷 *[截图位:粘贴完整段内容 + 提问,准备发送]*

---

## 步骤 A3 · 看到第一个预测结果

模型思考 3-5 秒后,会返回一段 JSON,类似:

```json
{
  "teamA":          { "name": "墨西哥", "winProb": 70 },
  "draw":           20,
  "teamB":          { "name": "南非",   "winProb": 10 },
  "predictedScore": "2-0",
  "confidence":     "高",
  "keyFactors":     ["..."],
  "analysis":       "...",
  "playersToWatch": [...]
}
```

🎉 **跑通了!**

---

## 路径 A · 后续怎么继续提问?

每次想换一场比赛,**不需要重新粘 skill.md**,只要在同一个对话里继续发:

> "再预测一场:【小组赛】巴西 vs 摩洛哥"

模型会延续之前的约束,直接给新的 JSON。

> ⚠️ 注意:如果你**新建对话**,就要重新粘 skill.md 全文。一对话一注入。

---

# 🟡 路径 B · 工程化 — Trae IDE(免费 · 字节出品 · 无需翻墙)

**适合人群**:想稳定保存这套配置、想反复调、想批量操作的朋友。
**所需时间**:15 分钟
**所需技能**:能装一个软件 ✅

---

## 关于 Trae

**Trae** 是字节跳动出的 AI 编程 IDE,**国内可下载、免费、内置中文界面**,内置的 AI Chat 可以直接接你的 API Key。
官网:**https://www.trae.ai/** (中国地区版:**https://www.trae.cn/**)

---

## 步骤 B1 · 下载安装 Trae

1. 打开 **https://www.trae.cn/**
2. 点首页 **"下载 Trae"** 按钮
3. 根据你的系统选:
   - 🪟 Windows:`.exe` 安装包,**双击运行 → 一路下一步**
   - 🍎 macOS:`.dmg` 安装包,**双击打开 → 拖进 Applications**
4. 装完后启动,**首次进入会引导你登录**,用手机号/微信任意一个登录即可

📷 *[截图位:Trae 主界面 · 左侧文件树 + 右侧 AI Chat 面板]*

---

## 步骤 B2 · 新建项目并放入 skill.md

1. Trae 启动后,左上角 **"打开文件夹"** 或 **"新建项目"**
2. 在电脑桌面新建一个空文件夹,叫 `worldcup`(随便起)
3. 用 Trae 打开这个文件夹
4. **把你下载好的 `skill.md` 拖进 Trae 左侧的文件树里**
5. 现在 `skill.md` 就在你的项目里了

---

## 步骤 B3 · 在 Trae 里把 skill.md 设成 AI 的"角色"

1. Trae 右侧有个 **AI 对话面板**(看不到的话,顶部菜单 View → AI Chat)
2. AI 面板里有一个 **"# 引用上下文"** 按钮(或 `@` 输入)
3. **打 `@` 选择 `skill.md`**,Trae 就会把整份 Skill 自动塞进 system prompt
4. 然后输入你的问题:

   ```
   请基于 @skill.md 的全部约束,预测这场比赛:
   【小组赛】墨西哥 vs 南非
   严格输出 JSON。
   ```

5. 回车发送,等待 AI 输出

📷 *[截图位:AI Chat 面板里 @skill.md 后提问 → 返回 JSON]*

---

## 步骤 B4 · 切换到你充值过 API 的模型(推荐 DeepSeek)

Trae 默认用字节自家模型(也好用),但如果你想保持成本最低 + 用上 DeepSeek 的 JSON 强约束:

1. AI 面板顶部有个**模型选择下拉框**
2. 选 **DeepSeek-V4-Pro**(如果列表里没有,点 **"添加自定义模型"**)
3. 在弹窗里填:
   - **API Base**: `https://api.deepseek.com/v1`
   - **API Key**: 你在第 0.5 步领到的 `sk-...`
   - **Model Name**: `deepseek-v4-pro`
4. 保存,在模型下拉里选中它,**之后所有提问都走 DeepSeek**

> 💡 这一步让"Trae 这个软件"变成了"你的私人世界杯助手 + 老板还是 DeepSeek"。

---

## 路径 B · 进阶玩法:一次批量预测多场

在 AI 面板里直接问:

> 请基于 @skill.md,把今天和明天 A 组的 4 场比赛全部预测一遍,逐场输出 JSON。

Trae 会逐个返回,你可以**直接 Ctrl+S 把对话保存为 markdown**,留作复盘。

---

# 🔴 路径 C · 程序员级 — Codex CLI(终端命令行)

**适合人群**:开发者、自动化爱好者、想接进自己脚本/网站的朋友。
**所需时间**:30 分钟
**所需技能**:会用终端 ✅

---

## 关于 Codex CLI

**Codex CLI** 是 OpenAI 官方开源的命令行 Agent(npm 包),开源在 GitHub,**可以通过设置环境变量改 API 端点,直接接 DeepSeek**——既享受 Codex 的好用 UX,又用国内可访问的模型。

---

## 步骤 C1 · 装 Node.js(如果还没装)

1. 打开 **https://nodejs.org/zh-cn**
2. 下载 **LTS** 版(长期支持版本)
3. Windows 直接双击 `.msi` 一路下一步;macOS 双击 `.pkg`
4. 装完后,**打开终端**(Windows 是 PowerShell,macOS 是 Terminal),输入:

   ```bash
   node --version
   ```

   能看到 `v20.x.x` 之类的版本号,就说明装好了 ✅

---

## 步骤 C2 · 装 Codex CLI

在终端里运行:

```bash
npm install -g @openai/codex
```

> 装完后输入 `codex --version` 验证。

> 💡 **国内 npm 装得慢?** 换个源再装:
> ```bash
> npm config set registry https://registry.npmmirror.com
> npm install -g @openai/codex
> ```

---

## 步骤 C3 · 把 Codex 指向 DeepSeek

Codex 默认走 OpenAI 接口,**改两个环境变量就能让它走 DeepSeek**——key 和 base URL。

### 🪟 Windows(PowerShell)

```powershell
$env:OPENAI_API_KEY = "sk-你的DeepSeekKey"
$env:OPENAI_BASE_URL = "https://api.deepseek.com/v1"
```

> 想永久生效:在「系统属性 → 环境变量」里把这两个加进去。

### 🍎 macOS / Linux(zsh / bash)

```bash
export OPENAI_API_KEY="sk-你的DeepSeekKey"
export OPENAI_BASE_URL="https://api.deepseek.com/v1"
```

> 永久生效:把这两行加到 `~/.zshrc` 或 `~/.bashrc` 末尾。

---

## 步骤 C4 · 把 skill.md 放进 Codex 的工作目录

```bash
cd ~/Desktop                              # 进到你存 skill.md 的目录
codex --model deepseek-v4-pro             # 启动 codex,指定模型
```

Codex 启动后是一个交互式终端,**像和 AI 聊天一样**。
在 Codex 里直接说:

```
请读取当前目录下的 skill.md,把它的内容作为系统提示词的全部约束。
然后预测这场:【小组赛】墨西哥 vs 南非,严格按文档 JSON 输出。
```

它会:
1. 自动读 `skill.md`
2. 把全文作为 system prompt 注入
3. 调用 DeepSeek 返回 JSON

📷 *[截图位:终端里 Codex 返回 JSON 的画面]*

---

## 步骤 C5 · 一行命令出预测(脚本化)

如果你想做自动化(比如做个网站、做个机器人),直接用 `curl`:

```bash
curl https://api.deepseek.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d @- <<EOF
{
  "model": "deepseek-v4-pro",
  "response_format": {"type": "json_object"},
  "messages": [
    {"role": "system", "content": $(jq -Rs . < skill.md)},
    {"role": "user",   "content": "请预测这场 2026 世界杯比赛:【小组赛】墨西哥 vs 南非。严格按约束文档 JSON 输出。"}
  ]
}
EOF
```

返回的就是干净 JSON,**可以直接喂给你的前端 / Excel / 飞书多维表格**。

---

# 🛟 路径 D · 万能托底 — 我的在线 Demo 站

如果上面三条路径你都跑不通,**最最最简单的办法**:

🔗 **打开 http://worldcup.youliaoyun.com**

我已经把 Skill 接上 DeepSeek 部署在这个网站上了,**选场次 → 点预测 → 三秒出卡片**。
免费用,不需要注册。

> 适用场景:朋友想看预测、要做截图当素材、要给老板演示效果。

---

# 🐛 常见报错 / 怎么救场

<details>
<summary><b>问题 1:返回的不是 JSON,而是一段中文解释</b></summary>

**原因**:模型把约束当成了"参考",没严格遵守。
**解决**:在你的提问最后加一句强约束:

> ⚠️ 直接输出 JSON 对象,不要包 markdown 代码块,不要写任何 JSON 之外的文字。

或者在 API 调用里加 `"response_format": {"type": "json_object"}`(DeepSeek/Qwen/GPT 都支持)。
</details>

<details>
<summary><b>问题 2:模型瞎编球员伤病</b></summary>

**原因**:你可能粘漏了 skill.md,或者 skill.md 第六节(每日情报区)被人改坏了。
**解决**:重新下载一份原版 skill.md,完整粘贴。
</details>

<details>
<summary><b>问题 3:三个胜平负概率加起来不等于 100</b></summary>

**原因**:小模型可能违反约束。
**解决**:换更强的模型(DeepSeek-V4-Pro / GPT-4o / Claude Opus)。**不要用 ChatGPT 免费版**(用的是阉割版小模型)。
</details>

<details>
<summary><b>问题 4:DeepSeek 提示余额不足</b></summary>

**解决**:登录 platform.deepseek.com,左侧"充值",微信/支付宝充 1 元就够你再跑 100 场。
</details>

<details>
<summary><b>问题 5:Trae / Codex 连不上 DeepSeek</b></summary>

**排查**:
1. 检查 API Key 是不是粘对了(开头必须是 `sk-`)
2. 检查 base URL 是不是 `https://api.deepseek.com/v1`(注意有 `/v1` 后缀)
3. 检查电脑有没有开 VPN,**开了 VPN 反而可能连不上**(DeepSeek 是国内服务),关掉 VPN 再试
</details>

<details>
<summary><b>问题 6:Codex CLI 装不上</b></summary>

**原因**:npm 源被墙 / 节点没装好。
**解决**:用 npmmirror 镜像源(见步骤 C2 的小提示)。或者直接走路径 B 的 Trae,免装 Codex。
</details>

---

# 🎁 进阶玩法清单

跑通最基础的预测后,可以试试这些:

| 玩法 | 怎么做 |
|:---|:---|
| 🏆 **预测冠军** | 让 AI 把 64 场全部跑一遍,自动生成晋级树 |
| 📊 **导出 Excel** | 让 AI 把每场 JSON 串起来,导成 CSV 给到飞书多维表格 |
| 🤖 **微信群机器人** | 用 Trae 写个简单脚本,接到企业微信 webhook |
| 🌐 **做你自己的预测网站** | 拿 README 里的 Node.js 代码,放到 Vercel 一键部署 |
| 📝 **改造成"NBA 季后赛 Skill"** | 把 skill.md 的资料库换成 NBA 球队,方法论照搬 |
| 🎙️ **做内容创作** | 直接把 JSON 喂给你的稿子/视频脚本,作为 fact-checking 基础数据 |

---

# 🤔 我能拿这个赚钱吗?

可以。MIT 协议,允许商用。但请注意:

✅ **可以**:做付费小程序、付费看板、付费预测群、培训课程素材
❌ **不可以**:用于任何投注、博彩、赔率、下注业务(Skill 自身已内置红线拒绝)
✅ **建议**:做出来 fork 一份到 GitHub,留个 reference 链接互相引流

---

# 📞 还是搞不定?

- 🐛 GitHub Issues:**https://github.com/TradingAi666/worldcup2026-prediction-skill/issues**
- 💬 评论区直接留言我,看到都会回
- 🎥 视频里我也演示了一遍,可以回去对照看

---

<div align="center">

**⚽ 跑通后记得给仓库点个 ⭐ Star,这是对开源最大的支持 ⚽**

*这份教程会随着新工具的出现持续更新——v1.0 · 2026-06-11*

</div>
