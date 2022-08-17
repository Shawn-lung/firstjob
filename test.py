class hi:
    def __init__(self):
        self.wow = '1'
    def update(self):
        for i in range(100):
            print(i)

monkey = hi()
tiger = hi()
monkey.update()
tiger.update()