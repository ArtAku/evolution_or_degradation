from math import sqrt
import random

temperature_range = (0, 100)
hardness_range = (0, 100)
max_energy_range = (100, 1000)
energy_range = (0, 100)
agressivity_range = (0, 100)

children_range = (1, 8)

temperature_max_delta = 10
hardness_max_delta = 10
energy_max_delta = 10
agressivity_max_delta = 10

children_max_delta = 1

class Plant():

    def __init__(self, init_t: float,
                 init_hardness: float, init_max_energy: float,
                 init_devour_per_day: float, init_spend_per_day: float,
                 init_max_children: int, init_feed_to_sepparate: float,
                 init_sepparate_threshold: float,
                 init_energy: float, init_agressivity: float) -> None:
        #  Изменяемые мутациями параметры
        self.preferred_temperature: float = init_t
        self.preferred_hardness: float = init_hardness

        self.max_energy: float = init_max_energy
        self.energy_max_devour_per_day: float = init_devour_per_day
        self.energy_min_spending_per_day: float = init_spend_per_day
        self.max_children: int = init_max_children
        self.sepparate_threshoud: float = init_sepparate_threshold
        self.feed_to_sepparate: float = init_feed_to_sepparate
        self.agressivity: float = init_agressivity

        #  Неизменяемые мутациями параметры
        self.energy_mutation_score = 200
        self.current_energy = init_energy

    def mutation(self, mutation_probability) -> Plant:
        # Начальная энергия равна энергии на размножение данного вида
        new_plant = Plant(self.preferred_temperature, self.preferred_hardness,
                          self.max_energy, self.energy_max_devour_per_day,
                          self.energy_min_spending_per_day, self.max_children,
                          self.feed_to_sepparate, self.sepparate_threshoud,
                          self.feed_to_sepparate, self.agressivity)

        if random.random() <= mutation_probability:
            pref_temp = self.preferred_temperature + random.uniform(self.preferred_temperature - temperature_max_delta,
                                                                    self.preferred_temperature + temperature_max_delta)
            pref_temp = temperature_range[0] if pref_temp < temperature_range[0] else pref_temp
            pref_temp = temperature_range[1] if pref_temp > temperature_range[1] else pref_temp

            new_plant.preferred_temperature = pref_temp

        if random.random() <= mutation_probability:
            pref_hardness = self.preferred_hardness + random.uniform(self.preferred_hardness - hardness_max_delta,
                                                                    self.preferred_hardness + hardness_max_delta)
            pref_hardness = hardness_range[0] if pref_hardness < hardness_range[0] else pref_hardness
            pref_hardness = hardness_range[1] if pref_hardness > hardness_range[1] else pref_hardness

            new_plant.preferred_hardness = pref_hardness


        if random.random() <= mutation_probability:
            agr = self.preferred_hardness + random.uniform(self.agressivity - agressivity_max_delta,
                                                                     self.agressivity + agressivity_max_delta)
            agr = agressivity_range[0] if agr < agressivity_range[0] else agr
            agr = agressivity_range[1] if agr > agressivity_range[1] else agr

            new_plant.agressivity = agr

        #  Параметры энергии будем изменять впоследствии, пока забили хер
        return new_plant


class BiomCenter():
    temperature: float
    hardness: float
    center_r: float
    center_x: int
    center_y: int

    def __init__(self, **params) -> None:
        self.center_x = params.get('x') or 0
        self.center_y = params.get('y') or 0
        self.center_r = params.get('r') or 1

        self.temperature = params.get('temperature') or 20
        self.hardness = params.get('hardness') or 20
        if self.temperature <= temperature_range[0] or self.temperature > temperature_range[1]:
            raise Exception(
                f'self.temperature {self.temperature} out of range')
        if self.hardness <= hardness_range[0] or self.hardness > hardness_range[1]:
            raise Exception(f'self.hardness {self.hardness} out of range')

    def coefficient(self, _x: float, _y: float) -> float:
        coefficient = (self.center_r - sqrt((_x - self.center_x)
                                            ** 2 + (_y - self.center_y)**2)) / self.center_r
        return coefficient if coefficient > 0 else 0

    def __str__(self) -> str:
        return f'center: ({self.center_x},{self.center_y})\nt,h: ({self.temperature},{self.hardness})\n'


class Cell():
    temperature: float
    hardness: float
    current_energy: float
    energy_income: float
    center_x: int
    center_y: int

    def __init__(self, x, y, **params) -> None:
        self.center_x = x
        self.center_y = y

        self.temperature = params.get('temperature') or 20
        self.hardness = params.get('hardness') or 0.5
        self.current_energy = params.get('current_energy') or 10
        self.energy_income = params.get('energy_income') or 1


class Map():
    cells: list
    width: int
    height: int

    def __init__(self, **params) -> None:
        self.cells = params["cells"]
        self.height = len(self.cells)
        self.width = len(self.cells[0])

    def temperature(self) -> list:
        return [[c.temperature for c in row] for row in self.cells]

    def hardness(self) -> list:
        return [[c.hardness for c in row] for row in self.cells]

    def current_energy(self) -> list:
        return [[c.current_energy for c in row] for row in self.cells]

    def energy_income(self) -> list:
        return [[c.energy_income for c in row] for row in self.cells]

    def __str__(self) -> str:
        return f'{len(self.cells)}x{len(self.cells[0])}'
