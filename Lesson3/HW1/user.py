class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_last_first_name(self):
        print(f"Вас зовут: {self.last_name} {self.first_name}")

    def say_last_name(self):
        print(f"Ваша фамилия: {self.last_name}")

    def say_first_name(self):
        print(f"Ваше имя: {self.first_name}")

