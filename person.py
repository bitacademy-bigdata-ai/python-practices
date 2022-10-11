


class Person():
    count = 1 # 비공개 속성 
    # 1
    def __init__(self) -> None:
        Person.count += 1 # Person.count 1
        self.count = self.count + 1 
        # c.count =self.count = self.count 1 + 1 = 2
        
    @classmethod
    def printCount(cls): #cls = Person
        print(cls.count) # 1

    def printCount2(self):# self =c
        print(self.count)  # c.count = 2 
    