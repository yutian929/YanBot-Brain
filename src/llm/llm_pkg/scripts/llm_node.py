import os
from openai import OpenAI

# 从环境变量获取API密钥
api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("请设置DEEPSEEK_API_KEY环境变量")

# 创建客户端（只需要创建一次）
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# 初始对话
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
)
print(response.choices[0].message.content)

# Round 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(model="deepseek-reasoner", messages=messages)

reasoning_content = response.choices[0].message.reasoning_content
content = response.choices[0].message.content
print(reasoning_content)
print(content)

# Round 2
messages.append({"role": "assistant", "content": content})
messages.append(
    {"role": "user", "content": "How many Rs are there in the word 'strawberry'?"}
)
response = client.chat.completions.create(model="deepseek-reasoner", messages=messages)
# ...后续处理...
