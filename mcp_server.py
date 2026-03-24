#!/usr/bin/env python3
"""
MCP Server for Family Analyzer
Model Context Protocol 适配
"""

import asyncio
import json
import sys
from pathlib import Path

# MCP 协议头
print("Content-Type: application/json\n")

# 工具定义
TOOLS = {
    "analyze_chat": {
        "name": "analyze_chat",
        "description": "分析微信群聊记录，提取群体行为模式和成员画像",
        "parameters": {
            "type": "object",
            "properties": {
                "chat_file": {
                    "type": "string",
                    "description": "群聊记录文件路径 (JSON格式)"
                },
                "output_dir": {
                    "type": "string",
                    "description": "输出目录路径"
                }
            },
            "required": ["chat_file"]
        }
    },
    "generate_persona": {
        "name": "generate_persona", 
        "description": "为指定成员生成个人画像",
        "parameters": {
            "type": "object",
            "properties": {
                "member_id": {
                    "type": "string",
                    "description": "成员ID"
                },
                "observations": {
                    "type": "array",
                    "description": "观察数据"
                }
            },
            "required": ["member_id", "observations"]
        }
    }
}

async def handle_request():
    """处理 MCP 请求"""
    try:
        line = input()
        request = json.loads(line)
        
        method = request.get("method")
        params = request.get("params", {})
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "family-analyzer",
                        "version": "0.1.0"
                    }
                }
            }
        
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "tools": list(TOOLS.values())
                }
            }
        
        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            
            # 这里调用实际的分析逻辑
            result = f"Tool {tool_name} called with args: {arguments}"
            
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": result
                        }
                    ]
                }
            }
        
        else:
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }
            
    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": request.get("id", None),
            "error": {
                "code": -32603,
                "message": str(e)
            }
        }

if __name__ == "__main__":
    # MCP 协议初始化
    init_response = {
        "jsonrpc": "2.0",
        "id": 0,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "family-analyzer",
                "version": "0.1.0"
            }
        }
    }
    print(json.dumps(init_response, ensure_ascii=False))
    
    # 进入请求循环
    while True:
        try:
            response = asyncio.run(handle_request())
            print(json.dumps(response, ensure_ascii=False))
        except EOFError:
            break
        except Exception as e:
            print(json.dumps({
                "jsonrpc": "2.0",
                "error": {"code": -32603, "message": str(e)}
            }), file=sys.stderr)
