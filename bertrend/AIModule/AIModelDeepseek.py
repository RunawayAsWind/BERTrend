from bertrend.AIModule.AIModelInterface import AIModelInterface
from openai import OpenAI

class AIModelDeepseek(AIModelInterface):
    def __init__(self, temperature: float):
        super().__init__("deepseek-chat", temperature)
        # 需要充钱，否则会报错no model: https://openai.com/api/pricing/
        # 虚拟卡充钱：https://bewildcard.com/card
        # 重要的是api_Key: https://platform.openai.com/api-keys
        self.client = OpenAI(
            base_url="https://api.deepseek.com",
            api_key='sk-af38170037e8435e9da0bd09cf8602f9'
        )
        print("[AIModelDeepseek::__init__] modelslist:", self.client.models.list())

    def Chat(self, userinput, conversation_history):
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
            return False, f"[AIModelDeepseek::Chat] Error: {e}"

if __name__ == "__main__":
    model = AIModelDeepseek(1.0)
    conversation_history = []
    bsuccess, reply = model.Chat("你好", conversation_history)
    if bsuccess:
        print(reply)
    print(model.DebugInfo(0))
