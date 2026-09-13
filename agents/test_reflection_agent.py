# test_reflection_agent.py
from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM
from my_reflection_agent import MyReflectionAgent
import os
from pathlib import Path

# 因为Windows 终端默认使用 GBK 编码，无法输出父类 think() 中的表情符号
# 强制使用 UTF-8
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# 加载环境变量
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path, override=True)

# 创建LLM实例
llm = HelloAgentsLLM(
    provider="deepseek",
    model=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

# 使用默认通用提示词
general_agent = MyReflectionAgent(name="我的反思助手", llm=llm)

# 使用自定义代码生成提示词（类似第四章）
code_prompts = {
    "initial": "你是Python专家，请编写函数：{task}",
    "reflect": "请审查代码的算法效率：\n任务：{task}\n代码：{content}",
    "refine": "请根据反馈优化代码：\n任务：{task}\n反馈：{feedback}"
}
code_agent = MyReflectionAgent(
    name="我的代码生成助手",
    llm=llm,
    custom_prompts=code_prompts
)

# 测试使用
result = general_agent.run("写一篇关于人工智能发展历程的简短文章")
print(f"最终结果: {result}")