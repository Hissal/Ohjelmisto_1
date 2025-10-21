class Elevator:
    def __init__(self, min_floor, max_floor):
        self.current_floor = 0
        self.min_floor = min_floor
        self.max_floor = max_floor

    def move_to_floor(self, target_floor):
        if target_floor < self.min_floor or target_floor > self.max_floor:
            raise ValueError("Target floor is out of range.")

        move_amount = target_floor - self.current_floor
        for i in range(abs(move_amount)):
            if move_amount > 0:
                self.move_up()
            else:
                self.move_down()

    def move_up(self):
        if self.current_floor >= self.max_floor:
            print("Already at the top floor.")
            return
        self.current_floor += 1
        print("Moving up to floor", self.current_floor)

    def move_down(self):
        if self.current_floor <= self.min_floor:
            print("Already at the bottom floor.")
            return
        self.current_floor -= 1
        print("Moving down to floor", self.current_floor)