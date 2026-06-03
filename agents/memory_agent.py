class MemoryAgent:
    def __init__(self):
        self.memory=[]

    def save(self,item):
        self.memory.append(item)

    def recall(self):
        return self.memory
