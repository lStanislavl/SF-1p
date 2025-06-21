# При работе над проектом облачного сервиса планирования и управления задачами вам
# поручили улучшить класс Team, воспользовавшись инициализатором __init__(), при помощи
# которого устанавливаются локальные атрибуты name, team_size и capital.
# Также добавьте в класс метод show_info(), который выводит информацию по проекту в виде
# Team name: <значение атрибута name>, team size: <значение атрибута team_size>,
# capital: <значение атрибута capital>.

class Team:
    def __init__(self, name, team_size, capital):
        self.name = name
        self.team_size = team_size
        self.capital = capital

    def show_info(self):
        print(f"Team name: {self.name}, team size: {self.team_size}, capital: {self.capital}")
