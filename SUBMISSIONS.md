# 伐木累分析大师 - 平台发布模板

> 快速复制粘贴到各平台

---

## 📦 Product Hunt

**Name**: 伐木累分析大师 (Family Analyzer)

**Tagline**: 从微信群聊记录提炼群体人格画像

**Description**:
```
你家群是不是也叫「相亲相爱一家人」？

这个工具能自动分析微信群聊，发现：
• 谁才是真正的"话事人"
• 「收到」背后的真实情绪
• 你们家的专属黑话和暗号
• 每个成员的隐藏角色（早安打卡机/转发轰炸机/已读不回/养生专家）

上传聊天记录 JSON 文件，AI 自动分析并生成人格档案。

支持导出 Markdown 格式的：
- 群体人格档案 (soul.md)
- 成员个人画像 (persona_*.md)

开源免费，支持 OpenClaw / MCP / CLI 多种使用方式。
```

**Topics**: AI, Chat Analysis, WeChat, Family, Open Source, Python

**Maker**: @zengury

---

## 📦 Coze (扣子)

**名称**: 伐木累分析大师

**描述**: 
上传微信群聊记录，AI自动分析群体行为和成员画像。识别每个家庭的"早安打卡机"、"转发轰炸机"、"已读不回"等隐藏角色。

**图标**: poster_fun.png

**提示词**: (见 prompts/coze_prompt.txt)

**工具**:
- 文件解析
- 数据分析
- 报告生成

---

## 📦 Dify

**应用名称**: 伐木累分析大师

**应用类型**: Chatflow / Agent

**描述**: 微信群聊行为分析工具

**系统提示词**:
```
你是「伐木累分析大师」，专门分析微信群聊记录的 AI 助手。

你的任务是：
1. 解析用户上传的群聊 JSON 文件
2. 提取每个成员的发言特征和行为模式
3. 识别群体互动模式
4. 用幽默风趣的语言生成成员画像

风格要求：
- 用「相亲相爱一家人」等梗
- 识别角色：早安打卡机、转发轰炸机、已读不回、养生专家
- 既要有洞察，又要有温度
```

**知识库**: 上传 prompts/ 下的所有文件

---

## 📦 V2EX

**标题**: [分享] 做了一个分析微信群聊的工具，发现我妈是「早安打卡机」

**内容**:
```
最近做了一个小工具，叫「伐木累分析大师」。

背景：
家里有个群叫「相亲相爱一家人」，天天各种早安图、养生文、震惊体。突发奇想，能不能用 AI 分析一下这个群到底什么画风？

功能：
1. 上传微信聊天记录导出文件（JSON格式）
2. AI 自动分析每个成员的角色
3. 生成群体人格档案

结果还挺有意思的：
- 我妈 → 早安打卡机（每天6点准时发🌞）
- 我爸 → 转发轰炸机（震惊！快看！）
- 我 → 已读不回（偶尔回个👍）
- 三姨 → 养生专家（这个致癌那个长寿）

技术栈：
- Python + Kimi API
- 支持 OpenClaw / MCP / CLI
- 开源：https://github.com/zengury/family-analyzer

欢迎试用，看看你家群是什么画风😂
```

---

## 📦 即刻

**标题**: 用 AI 分析了一下我家「相亲相爱一家人」群聊

**内容**:
```
发现了一些有趣的真相：

我妈 = 早安打卡机 ⏰
每天早上6点准时发送🌞+鸡汤文案

我爸 = 转发轰炸机 📰
震惊体专业户，"不转不是中国人"

我 = 已读不回 🙈
常年潜水，偶尔回个👍维持亲情

三姨 = 养生专家 🏥
吃什么致癌、吃什么长寿，了如指掌

工具开源了，欢迎大家分析自家的群聊👇
GitHub: zengury/family-analyzer

#AI工具 #微信 #家庭群 #相亲相爱一家人
```

---

## 📦 Awesome 清单 PR 模板

### Awesome OpenClaw
```markdown
## [伐木累分析大师](https://github.com/zengury/family-analyzer)

从微信群聊记录提炼群体人格画像的 OpenClaw Skill。

- 自动识别成员角色（早安打卡机/转发轰炸机/已读不回/养生专家）
- 生成群体人格档案和成员画像
- 支持多平台：OpenClaw / MCP / CLI
```

### Awesome Python
```markdown
## [family-analyzer](https://github.com/zengury/family-analyzer)

微信群聊行为分析工具。

Features:
- Parse WeChat exported JSON
- Extract behavioral patterns using AI
- Generate persona files
- MCP server support
```

### Awesome MCP Servers
```markdown
### Family Analyzer

[伐木累分析大师](https://github.com/zengury/family-analyzer) - 微信群聊行为分析

`mcp.json`:
```json
{
  "name": "family-analyzer",
  "command": "python3",
  "args": ["mcp_server.py"]
}
```
```

---

## 📦 小红书

**标题**: 用AI分析我家群聊，发现了惊天大秘密🤯

**内容**:
```
家人们谁懂啊！

用AI分析了一下「相亲相爱一家人」群聊
结果发现了每个人的隐藏角色😂

我妈：早安打卡机 ⏰
（每天6点准时发太阳表情）

我爸：转发轰炸机 📰
（"震惊！再不看就删了！"）

我：已读不回 🙈
（潜水王者，偶尔👍）

三姨：养生专家 🏥
（这个致癌那个长寿）

工具是开源的，在GitHub搜 family-analyzer
评论区说说你家群是什么画风？

#AI工具 #微信群聊 #相亲相爱一家人 #家庭日常 #科技改变生活
```

---

## 📦 Twitter / X

```
Built a tool to analyze WeChat group chats.

Turns out my mom is the "Morning Greeting Bot" 
(6AM daily ☀️)

Dad = "News Forwarding Bomber" 
("SHOCKING! Read before deleted!")

Me = "Seen but no reply"
(Professional lurker 👍)

Open source: github.com/zengury/family-analyzer

#AI #WeChat #FamilyGroup #OpenSource
```
