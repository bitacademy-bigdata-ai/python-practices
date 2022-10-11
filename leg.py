from human import Human


class Leg(Human):
    def __init__(self,side,name) -> None:
        self.side = side
        super().setName(name)
        pass