from bertrend.AIModule.AIModelInterface import AIModelInterface
from openai import OpenAI

class AIModelChatgpt(AIModelInterface):
    def __init__(self, temperature: float):
        super().__init__("gpt-5-chat-latest", temperature)
        # 需要充钱，否则会报错no model: https://openai.com/api/pricing/
        # 虚拟卡充钱：https://bewildcard.com/card
        # 重要的是api_Key: https://platform.openai.com/api-keys
        # self.client = OpenAI(
        #     organization='org-cTbWCvRBJzasvRLegWyRlSe2',
        #     project='proj_cjfFF4QtW13i7QdmKFhZiMbU',
        #     api_key='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'
        # )
        self.client = OpenAI(
            base_url="https://api.gptsapi.net/v1",
            api_key='sk-SMp2087212ab056c2adbff15230bdc4460063fa6f16ShXev'
        )
        print("[AIModelChatgpt::__init__] modelslist:", self.client.models.list())

    def Chat(self, userinput: str, conversation_history: list):
        super().Chat(userinput, conversation_history)
        # 将用户的输入添加到对话历史记录中
        userinput = {"role": "user", "content": userinput}
        conversation_history.append(userinput)
        # for history in conversation_history:
        #    print(history)
        try:
            response = self.client.chat.completions.create(
                model=self.modelname,  # gpt模型
                messages=conversation_history,
                # max_tokens=150,  # 限制返回的最大长度
                n=1,  # 只获取一个回答
                temperature=self.temperature  # 控制生成的随机性
            )
            # print(response.text)
            # 提取返回的文本并去除多余的空格
            replytext = response.choices[0].message.content.strip()
            conversation_history.append({"role": "assistant", "content": replytext})
            return True, replytext
        except Exception as e:
            return False, f"[AIModelChatgpt::Chat] Error: {e}"

if __name__ == "__main__":
    model = AIModelChatgpt(1.0)
    conversation_history = []
    bsuccess, reply = model.Chat("你好", conversation_history)
    if bsuccess:
        print(reply)
    print(model.DebugInfo(0))