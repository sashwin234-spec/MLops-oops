class employe:
    def __init__(self):
        self.id = 123
        self.salary = 10000
        self.designation = "SDE"
        print("hii this")
    def travel(self,destination):
        print(f"employe is travelling in{destination}")
sam = employe()
print(sam.id)
sam.travel("bhopal")