# Вы разрабатываете систему управления звуковым оборудованием в театре.
# У вас есть базовый класс SoundEquipment с методом switch_on(), который включает оборудование,
# и методом switch_off(), который выключает оборудование.
# Создайте два дочерних класса: Microphone и Speaker. Оба должны наследоваться от SoundEquipment.
# В классе Microphone должен быть инициализатор, который задает уровень громкости — volume (от 0 до 10) и
# состояние — state (включен/выключен).
# Также этот класс должен содержать метод adjust_volume(), который позволяет изменять уровень громкости на
# переданную в качестве аргумента величину. После изменения уровня громкости метод должен выводить на
# экран фразу в формате "Volume is now <volume>".
# В классе Speaker должен быть инициализатор, который задаёт уровень басов — bass (от 0 до 10) и состояние —
# state (включен/выключен).
# Этот класс должен содержать метод adjust_bass(), который позволяет изменять уровень басов на переданную в
# качестве аргумента величину. После изменения уровня громкости метод должен выводить на экран фразу в
# формате "Bass level is now <bass>".

class SoundEquipment:
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False


class Microphone(SoundEquipment):
    def __init__(self, volume, state):
        self.volume = volume
        self.state = state

    def adjust_volume(self, new_volume):
        self.volume = new_volume
        print(f"Volume is now {self.volume}")

class Speaker(SoundEquipment):
    def __init__(self, bass, state):
        self.bass = bass
        self.state = state

    def adjust_bass(self, new_bass):
        self.bass = new_bass
        print(f"Bass level is now {self.bass}")
