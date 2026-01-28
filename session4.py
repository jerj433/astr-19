class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.num_eyes = int(num_eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)

    def describe(self):
        print("Favorite Animal Description:")
        print("Arm length:", self.arm_length)
        print("Leg length:", self.leg_length)
        print("Number of eyes:", self.num_eyes)
        print("Has a tail?:", self.has_tail)
        print("Is furry?:", self.is_furry)


def main(): #Red Panda
    animal = FavoriteAnimal(arm_length=0.5, leg_length=0.5, num_eyes=2, has_tail=True, is_furry=True)
    animal.describe()


if __name__ == "__main__":
    main()
