#!/usr/bin/env python3
"""
伐木累分析大师 - 推广文案生成器
自动生成适合不同平台的文案变体
"""

import random

# 标题模板
TITLES = [
    "用AI分析了一下我家「相亲相爱一家人」群聊，发现了惊天大秘密🤯",
    "我妈是「早安打卡机」，我爸是「转发轰炸机」｜群聊分析神器",
    "你家群是不是也叫「相亲相爱一家人」？这个工具扒出了真相",
    "群聊人格分析｜发现谁才是真正的"话事人"",
    "AI 揭秘：微信群聊里的隐藏角色",
    "相亲相爱一家人？我分析了800条消息后发现...",
]

# 开头钩子
HOOKS = [
    "家人们谁懂啊！",
    "笑死我了家人们！",
    "发现了一个宝藏工具！",
    "这玩意儿太绝了！",
    "不得不分享系列：",
]

# 角色描述
ROLES = [
    ("早安打卡机", "⏰", "每天早上6点准时发送🌞+鸡汤文案"),
    ("转发轰炸机", "📰", "震惊体专业户，'不转不是中国人'"),
    ("已读不回", "🙈", "常年潜水，偶尔回个👍维持亲情"),
    ("养生专家", "🏥", "吃什么致癌、吃什么长寿，了如指掌"),
    ("表情包大户", "😂", "一言不合就斗图"),
    ("语音方阵", "🎙️", "60秒语音连发，从不打字"),
    ("红包监察员", "🧧", "专抢红包从不说话"),
]

# 功能点
FEATURES = [
    "自动识别成员角色",
    "发现群体互动模式",
    "提取内部暗号和梗",
    "生成人格档案",
    "支持微信/WhatsApp导出",
]

# CTA (Call to Action)
CTAS = [
    "评论区说说你家群是什么画风？",
    "快去看看你家群聊真相👇",
    "转发给你群里的朋友看看",
    "试试分析你家群，结果可能出乎意料",
    "GitHub 开源免费，欢迎 Star ⭐",
]

# Hashtags
HASHTAGS = [
    "#AI工具",
    "#微信",
    "#群聊分析",
    "#相亲相爱一家人",
    "#家庭日常",
    "#开源",
    "#Python",
    "#人工智能",
]

def generate_xiaohongshu():
    """生成小红书文案"""
    title = random.choice(TITLES)
    hook = random.choice(HOOKS)
    
    roles_sample = random.sample(ROLES, 3)
    roles_text = "\n".join([f"{name} {emoji}\n（{desc}）" for name, emoji, desc in roles_sample])
    
    cta = random.choice(CTAS)
    hashtags = " ".join(random.sample(HASHTAGS, 4))
    
    return f"""{title}

{hook}

用AI分析了一下我家的群聊
结果发现了每个人的隐藏角色😂

{roles_text}

这个工具可以：
{chr(10).join(['• ' + f for f in FEATURES[:3]])}

{cta}

GitHub: zengury/family-analyzer

{hashtags}
"""

def generate_zhihu():
    """生成知乎回答/文章"""
    return f"""# 如何分析微信群聊中的群体行为模式？

最近做了一个小项目，可以自动分析微信群聊记录，提取群体人格画像。

## 背景

家里有个群叫「相亲相爱一家人」，每天各种早安图、养生文、震惊体。突发奇想，能不能用 AI 分析一下这个群到底什么画风？

## 功能

1. **成员角色识别**
   - 早安打卡机：每天准时发送问候
   - 转发轰炸机：震惊体专业户
   - 已读不回：潜水王者
   - 养生专家：健康知识达人

2. **群体互动模式**
   - 谁主导话题
   - 谁负责捧哏
   - 幽默方式分析

3. **内部暗号提取**
   - 家庭专属梗
   - 常用表情包
   - 特殊表达方式

## 技术实现

- Python + Kimi API
- 4阶段流水线：解析 → 去噪 → AI分析 → 合成
- 支持 OpenClaw / MCP / CLI

## 开源地址

https://github.com/zengury/family-analyzer

欢迎试用，看看你家群是什么画风。
"""

def generate_jike():
    """生成即刻动态"""
    hook = random.choice(HOOKS)
    roles = random.sample(ROLES, 2)
    
    return f"""{hook}

分析了800条「相亲相爱一家人」的群聊消息

发现：
• {roles[0][0]} - {roles[0][2]}
• {roles[1][0]} - {roles[1][2]}

笑死，原来每个人在群里都有固定人设😂

工具开源了 👉 github.com/zengury/family-analyzer

#AI #微信 #群聊分析 #开源
"""

def generate_twitter():
    """生成 Twitter 推文"""
    return f"""Built a tool to analyze WeChat group chats.

Turns out my mom is the "Morning Greeting Bot" 
(6AM daily ☀️)

Dad = "News Forwarding Bomber" 
("SHOCKING! Read before deleted!")

Me = "Seen but no reply" (👍)

Open source: github.com/zengury/family-analyzer

#AI #WeChat #OpenSource #FamilyGroup
"""

def generate_hackernews():
    """生成 Hacker News Show HN"""
    return f"""Show HN: Family Analyzer – Extract behavioral patterns from WeChat group chats

I built a tool that analyzes WeChat exported chat history to extract:
- Member personas (who's the leader, lurker, comic relief)
- Group dynamics (interaction patterns, inside jokes)
- Collective personality (shared values, communication style)

Built with Python + Kimi API. 4-stage pipeline: parse → denoise → AI extraction → synthesis.

Outputs markdown persona files that can be used as personality bases for AI agents.

GitHub: https://github.com/zengury/family-analyzer

Would love feedback from anyone interested in digital ethnography or group dynamics analysis!
"""

def main():
    print("📝 伐木累分析大师 - 推广文案生成器\n")
    
    platforms = {
        "1": ("小红书", generate_xiaohongshu),
        "2": ("知乎", generate_zhihu),
        "3": ("即刻", generate_jike),
        "4": ("Twitter", generate_twitter),
        "5": ("Hacker News", generate_hackernews),
    }
    
    print("选择平台:")
    for key, (name, _) in platforms.items():
        print(f"  {key}. {name}")
    print("  0. 全部生成")
    
    choice = input("\n输入数字: ").strip()
    
    if choice == "0":
        for name, func in platforms.values():
            print(f"\n{'='*60}")
            print(f"📱 {name}")
            print("="*60)
            print(func())
    elif choice in platforms:
        name, func = platforms[choice]
        print(f"\n📱 {name}")
        print("="*60)
        print(func())
    else:
        print("无效选择")

if __name__ == "__main__":
    main()
