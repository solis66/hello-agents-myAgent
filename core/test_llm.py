from dotenv import load_dotenv
from my_llm import MyLLM
from pathlib import Path

# 因为 Windows 终端默认使用 GBK 编码，无法输出父类 think() 中的表情符号
# 强制使用 UTF-8
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# 加载环境变量，让 .env 中的变量覆盖系统已有的环境变量
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path, override=True)

# 准备消息
messages = [{"role": "user", "content": "你好，请介绍一下你自己"}]

# 实例化我们重写的客户端，并指定provider
llm = MyLLM(provider="auto")

# 发起调用，think等方法都已从父类继承，无需重写
response_stream = llm.think(messages)

# 打印响应
print("ModelScope Response")
for chunk in response_stream:
    # chunk在my_llm库中已经打印过一遍，这里只需要pass即可
    # print(chunk, end="", flush=True)
    pass

