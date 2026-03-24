# 微信小程序版本

## 架构
- 前端：微信小程序
- 后端：腾讯云开发（CloudBase）
- AI：腾讯云智言/混元大模型

## 功能
1. 用户选择聊天记录文件（从微信聊天中选择）
2. 上传到云开发存储
3. 触发云函数进行分析
4. 在小程序内展示结果

## 项目结构
```
miniprogram/
├── pages/
│   ├── index/          # 首页
│   ├── upload/         # 上传页面
│   └── result/         # 结果展示
├── cloudfunctions/
│   └── analyze/        # 分析云函数
└── utils/
    └── parser.js       # 聊天记录解析
```

## 关键代码

### 云函数：analyze
```javascript
const cloud = require('wx-server-sdk');
const { analyzeChat } = require('./analyzer');

cloud.init();

exports.main = async (event, context) => {
  const { fileID } = event;
  
  // 1. 下载文件
  const res = await cloud.downloadFile({ fileList: [fileID] });
  const buffer = res.fileList[0].buffer;
  
  // 2. 解析聊天记录
  const messages = parseWeChatJSON(buffer);
  
  // 3. 调用混元大模型分析
  const analysis = await analyzeWithHunyuan(messages);
  
  // 4. 返回结果
  return {
    code: 0,
    data: analysis
  };
};
```

### 小程序页面
```json
{
  "pages": [
    "pages/index/index",
    "pages/upload/upload",
    "pages/result/result"
  ],
  "window": {
    "navigationBarTitleText": "伐木累分析大师"
  }
}
```

## 发布
1. 微信开发者工具上传代码
2. 微信公众平台提交审核
3. 审核通过后发布
