import random

class Game:
    def __init__(self):
        self.choices = ['к', 'н', 'б']

    def get_user_choice(self):
        user_choice = input("Выберите камень (к), ножницы (н) или бумагу (б): ")
        return user_choice.lower()

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Ничья!"
        elif (user_choice == 'к' and computer_choice == 'н') or \
             (user_choice == 'н' and computer_choice == 'б') or \
             (user_choice == 'б' and computer_choice == 'к'):
            return "Вы выиграли!"
        else:
            return "Вы проиграли."

    def play_game(self):
        print("Добро пожаловать в игру камень, ножницы, бумага!")
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        print(self.determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    game = Game()
    game.play_game()