from math import sqrt
import random

temperature_range = (0, 100)
hardness_range = (0, 100)
energy_range = (0, 100)
agressivity_range = (0, 100)

children_range = (1, 8)


class Plant():

    def __init__(self, init_t: float,
                 init_hardness: float, init_max_energy: float,
                 init_devour_per_day: float, init_spend_per_day: float,
                 init_max_children: int, init_feed_to_sepparate: float,
                 init_energy: float, init_agressivity: float) -> None:
        #  Изменяемые мутациями параметры
        self.preferred_temperature: float = init_t
        self.prefered_hardness: float = init_hardness

        self.max_energy: float = init_max_energy
        self.energy_max_devour_per_day: float = init_devour_per_day
        self.energy_min_spending_per_day: float = init_spend_per_day
        self.max_children: int = init_max_children
        self.feed_to_sepparate: float = init_feed_to_sepparate
        self.agressivity: float = init_agressivity

        #  Неизменяемые мутациями параметры
        self.energy_mutation_score = 200
        self.current_energy = init_energy

    def mutation(self, mutation_probability) -> None:
        if random.random() <= mutation_probability:
            self.preferred_temperature = random.uniform(temperature_range[0],
                                                        temperature_range[1])

        if random.random() <= mutation_probability:
            self.prefered_hardness = random.uniform(hardness_range[0],
                                                    hardness_range[1])

        if random.random() <= mutation_probability:
            self.agressivity = random.uniform(agressivity_range[0],
                                              agressivity_range[1])

        #  Параметры энергии будем изменять впоследствии, пока забили хер


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
