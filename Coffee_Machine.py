class Machine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def take_coffee(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        self.main_menu()

    def fill_coffee(self):
        print("Write how many ml of water do you want to add:")
        self.add = int(input())
        self.water += self.add
        print("Write how many ml of milk do you want to add:")
        self.add = int(input())
        self.milk += self.add
        print("Write how many grams of coffee beans do you want to add:")
        self.add = int(input())
        self.beans += self.add
        print("Write how many disposable cups of coffee do you want to add:")
        self.add = int(input())
        self.cups += self.add
        self.main_menu()

    def buy_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.choice = input()
        if self.choice == "1":
            if self.water < 250:
                print("Sorry, not enough water")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans")
            elif self.cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
            self.main_menu()
        elif self.choice == "2":
            if self.water < 350:
                print("Sorry, not enough water")
            elif self.milk < 75:
                print("Sorry, not enough milk")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans")
            elif self.cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
            self.main_menu()
        elif self.choice == "3":
            if self.water < 200:
                print("Sorry, not enough water")
            elif self.milk < 100:
                print("Sorry, not enough milk")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans")
            elif self.cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
            self.main_menu()
        elif self.choice == "back":
            self.main_menu()

    def contents(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def main_menu(self):
        print("Write action(buy, fill, take, remaining, exit):")
        self.action = input()
        if self.action == "buy":
            self.buy_coffee()
        elif self.action == "fill":
            self.fill_coffee()
        elif self.action == "take":
            self.take_coffee()
        elif self.action == "remaining":
            self.contents()
        elif self.action == "exit":
            exit()


cm = Machine()
while True:
    cm.main_menu()