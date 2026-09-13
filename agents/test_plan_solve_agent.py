# test_plan_solve_agent.py
from dotenv import load_dotenv
from hello_agents.core.llm import HelloAgentsLLM
from my_plan_solve_agent import MyPlanAndSolveAgent
from pathlib import Path
import os

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

# 创建自定义PlanAndSolveAgent
agent = MyPlanAndSolveAgent(
    name="我的规划执行助手",
    llm=llm
)

# 测试复杂问题
question = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"

result = agent.run(question)
print(f"\n最终结果: {result}")

# 查看对话历史
print(f"对话历史: {len(agent.get_history())} 条消息")