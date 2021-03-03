from random import randint
from builder import create_random
from paint import paint_all
from entities import Map

# my_map = create_random(width=20, height=8)
# paint_all(my_map)


def one_day(cur_day: Map) -> Map:
    # Цикл насыщения

    # Цикл кормежки

    # Цикл трат

    # Цикл размножения

    # Цикл вымирания
    pass

if __name__ == '__main__':
    start_map = create_random(width=20, height=8)
    start_plant_count = 8
    plant_positions = []
    for i in range(start_plant_count):
        plant_positions.append((randint(0, 20),
                               randint(0, 8)))


    print('hello')