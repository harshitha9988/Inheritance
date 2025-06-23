class bird:
    def __init__(self):
        print("Bird is ready")
    
    def whoisthis(self):
        print("Bird")

    def swim(self):
        print("swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")

    def whoisthis(self):
        print("penguin")

    def run(self):
        print("run faster")


peggy=penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()