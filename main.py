import random
# importuojam randoma


class Tank:
    # init'as inicijuoja atributus - krypti, suviu skaiciu, suvius, taskus, kiek kartu pataike
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "North"
        self.shots_total = 0
        self.shots = {"North": 0, "East": 0, "South": 0, "West": 0}
        self.points = 100
        self.targets_hit = 0
        self.target_x = 0
        self.target_y = 0

    # cia metodai judina tanka aprasyta kryptimi. kiekvienas judesys kainuoja 5 taskus
    def move_forward(self):
        if self.direction == "North":
            self.y += 1
        elif self.direction == "East":
            self.x += 1
        elif self.direction == "South":
            self.y -= 1
        elif self.direction == "West":
            self.x -= 1
        self.points -= 5

    def move_backward(self):
        if self.direction == "North":
            self.y -= 1
        elif self.direction == "East":
            self.x -= 1
        elif self.direction == "South":
            self.y += 1
        elif self.direction == "West":
            self.x += 1
        self.points -= 5

    # pasuka tanka i kaire ar desine 90 laipsniu ir atima 5 taskus
    def turn_left(self):
        directions = ["North", "West", "South", "East"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        self.points -= 5

    def turn_right(self):
        directions = ["North", "East", "South", "West"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]
        self.points -= 5

    # cia turim fire metoda kuris imituoja suvi, padidina bendra suviu skaiciu ir atnaujina suviu
    # zodyna pagal suvio kripti, jei suvis pataiko, tasku skaicius padideja 50 tasku, ir prideda
    # viena prie pataikytu taikiniu skaiciaus, kitu atveju atima 10 balu is tasku.
    def fire(self):
        self.shots_total += 1
        self.shots[self.direction] += 1
        if self.direction == "North" and self.y < self.target_y and self.x == self.target_x:
            print("Hit!")
            self.points += 50
            self.targets_hit += 1
            self.generate_target()
        elif self.direction == "East" and self.x < self.target_x and self.y == self.target_y:
            print("Hit!")
            self.points += 50
            self.targets_hit += 1
            self.generate_target()
        elif self.direction == "South" and self.y > self.target_y and self.x == self.target_x:
            print("Hit!")
            self.points += 50
            self.targets_hit += 1
            self.generate_target()
        elif self.direction == "West" and self.x > self.target_x and self.y == self.target_y:
            print("Hit!")
            self.points += 50
            self.targets_hit += 1
            self.generate_target()
        else:
            print("Miss!")
            self.points -= 10

    # sis metodas atprintina informacija apie tanka, i kuria puse jis atsisukes, koordinates,
    # kiek suviu padaryta is viso, kiek suviu padaryta i atskiras puses ir turimu tasku skaicius.
    def show_info(self):
        print(f"Facing: {self.direction}")
        print(f"Coordinates: ({self.x}, {self.y})")
        print(f"Total Shots: {self.shots_total}")
        print("Shots Fired:")
        for direction, count in self.shots.items():
            print(f"{direction}: {count}")
        print(f"Points: {self.points}")
# sis metodas sugeneruoja taikini zemelapyje

    def generate_target(self):
        self.target_x = random.randint(-4, 4)
        self.target_y = random.randint(-4, 4)
# cia metodas atprintina fizini zemelapi, kad butu galima matyti taikini ir tanka kaip grida
# atprintina simbolius kuriuos naudojau:
# tuscioms vietoms *, tankui <>^⌄ priklausomai nuo to i kuria puse atsisukes, taikiniui 0

    def print_map(self):
        print("\nMovement Map:")
        for j in range(4, -5, -1):
            for i in range(-4, 5):
                if (i, j) == (self.x, self.y):
                    if self.direction == "North":
                        print(" ^ ", end="")
                    elif self.direction == "East":
                        print(" > ", end="")
                    elif self.direction == "South":
                        print(" ⌄ ", end="")
                    elif self.direction == "West":
                        print(" < ", end="")
                elif (i, j) == (self.target_x, self.target_y):
                    print(" 0 ", end="")
                else:
                    print(" * ", end="")
            print()

# sukuriam funkcija kuri inicijuoja tanka ir sugeneruoja taikinio pozicija
def main():
    tank = Tank()
    tank.generate_target()
# pradedam cikla kuris gali testis iki kol turimi taskai yra daugiau nei 0
    while tank.points > 0:
        # printinam mapa su tanku, taikiniu, tusciom vietom
        tank.print_map()
        # printinam meniu su pasirinkimais
        print("\nMENU:")
        print("1. Move Forward")
        print("2. Move Backward")
        print("3. Turn Left")
        print("4. Turn Right")
        print("5. Fire")
        print("6. Show Info")
        print("7. Quit")
        # inputas pasirinkimo irasimui
        choice = input("Your choice: ")
# cia pagal pasirinkima iskvieciam tinkamus auksciau aprasytus metodus, arba baigiam zaidima
        if choice == "1":
            tank.move_forward()
        elif choice == "2":
            tank.move_backward()
        elif choice == "3":
            tank.turn_left()
        elif choice == "4":
            tank.turn_right()
        elif choice == "5":
            tank.fire()
        elif choice == "6":
            tank.show_info()
        elif choice == "7":
            print("\nGame Over!")
            if tank.targets_hit > 0:
                name = input("Enter your name: ")
                high_scores.append((name, tank.targets_hit))
                high_scores.sort(key=lambda x: x[1], reverse=True)
                print("\nHigh Scores:")
                for i, (name, score) in enumerate(high_scores[:5], start=1):
                    print(f"{i}. {name}: {score} targets")
            return
        else:
            print("Invalid choice. Try again.")


# sitas inicijuoja sarasa high scores kad isaugoti rezultatus, ir iskviecia main funkcija pradeti zaidimui
if __name__ == "__main__":
    high_scores = []
    main()
