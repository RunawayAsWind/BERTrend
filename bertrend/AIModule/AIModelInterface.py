class AIModelInterface:
    def __init__(self, modelname: str, temperature: float):
        self.modelname = modelname
        self.temperature = temperature

    def Chat(self, userinput: str, conversation_history: list):
        print("[AIModelInterface::Chat]")
        return False, ""

    def DebugInfo(self, stackdepth: int):
        stackstr = ""
        for i in range(stackdepth):
            stackstr += "   "
        return f"{stackstr}modelname: {self.modelname} temperature: {self.temperature}"

if __name__ == "__main__":
    model = AIModelInterface("AIModel", 1.0)
    conversation_history = []
    bsuccess, reply = model.Chat("你好", conversation_history)
    if bsuccess:
        print(reply)
    print(model.DebugInfo(0))
