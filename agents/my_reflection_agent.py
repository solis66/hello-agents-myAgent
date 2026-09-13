DEFAULT_PROMPTS = {
    "initial": """
请根据以下要求完成任务:

任务: {task}

请提供一个完整、准确的回答。
""",
    "reflect": """
请仔细审查以下回答，并找出可能的问题或改进空间:

# 原始任务:
{task}

# 当前回答:
{content}

请分析这个回答的质量，指出不足之处，并提出具体的改进建议。
如果回答已经很好，请回答"无需改进"。
""",
    "refine": """
请根据反馈意见改进你的回答:

# 原始任务:
{task}

# 上一轮回答:
{last_attempt}

# 反馈意见:
{feedback}

请提供一个改进后的回答。
"""
}
import re
from typing import Optional, List, Tuple
from hello_agents import ReflectionAgent, HelloAgentsLLM, Config, Message

class MyReflectionAgent(ReflectionAgent):
    """
    重写的Reflection Agent - 反思与改进结合的智能体
    """

    def __init__(
        self,
        name: str,
        llm: HelloAgentsLLM,
        system_prompt: Optional[str] = None,
        config: Optional[Config] = None,
        custom_prompts: Optional[dict] = None
    ):
        super().__init__(name, llm, system_prompt, config)
        self.prompts = custom_prompts if custom_prompts else DEFAULT_PROMPTS
        print(f"✅ {name} 初始化完成，使用自定义提示词: {bool(custom_prompts)}")

    def run(self, task: str, **kwargs) -> str:
        """运行Reflection Agent"""
        print(f"\n🤖 {self.name} 开始处理任务: {task}")

        # 1. 初始回答
        initial_prompt = self.prompts["initial"].format(task=task)
        messages = [{"role": "user", "content": initial_prompt}]
        initial_response = self.llm.invoke(messages, **kwargs)
        print(f"\n初始回答:\n{initial_response}")

        # 2. 反思阶段
        reflect_prompt = self.prompts["reflect"].format(task=task, content=initial_response)
        messages = [{"role": "user", "content": reflect_prompt}]
        feedback = self.llm.invoke(messages, **kwargs)
        print(f"\n反馈意见:\n{feedback}")

        # 3. 改进阶段
        refine_prompt = self.prompts["refine"].format(task=task, last_attempt=initial_response, feedback=feedback)
        messages = [{"role": "user", "content": refine_prompt}]
        refined_response = self.llm.invoke(messages, **kwargs)
        print(f"\n改进后的回答:\n{refined_response}")

        return refined_response
