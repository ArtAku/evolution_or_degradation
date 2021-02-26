from entities import Map
from builder import MapBuilder
from paint import paint_all

map = MapBuilder.CreateSimple()
paint_all(map)
