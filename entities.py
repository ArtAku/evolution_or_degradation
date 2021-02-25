import random

temperature_range = (0, 100)
hardness_range = (0, 100)
energy_range = (0, 100)
agressivity_range = (0, 100)

children_range = (1, 8)

class Plant():

    def __init__(self, init_t: float,
                 init_hardness: float, init_max_energy: float,
                 init_devour_per_day: float, init_spend_per_day:float,
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
