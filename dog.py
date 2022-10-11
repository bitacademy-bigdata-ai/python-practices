from animal import Animal
class Dog(Animal):
    def __init__(self) -> None:
        # self.name = "sss"
        # self.sound = ""
        super().setName("강아지")
        super().setSound("멍멍")
        self.master = True
        pass

    def run(self):
        print("뛰다")