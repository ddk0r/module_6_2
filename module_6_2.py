class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']   # Допустимые цвета для окрашивания
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)         # владелец транспорта. (владелец может меняться)
        self.__model = str (__model)    # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = int(__engine_power)   # мощность двигателя. (мы не можем менять самостоятельно)
        self.__color = str(__color)     # название цвета. (мы не можем менять цвет автомобиля своими руками)
#
# Каждый объект Vehicle должен содержать следующий методы:
    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color.upper()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        # new_color = input('Новый цвет: ')
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS] # для проверки без учета регистра
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 3      # (в седан может поместиться только 3 пассажира и 1 водитель)

avto1 = Sedan('Fedos', 'Toyota Mark II', 500,  'blue')


avto1.print_info() # Изначальные свойства

# Меняем свойства (в т.ч. вызывая методы)
avto1.set_color('Pink')
avto1.set_color('BLACK')
avto1.owner = 'Marija'