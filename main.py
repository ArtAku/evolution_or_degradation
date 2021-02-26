from builder import MapBuilder
from paint import paint_all

my_map = MapBuilder.create_random(width=20, height=8)
paint_all(my_map)
