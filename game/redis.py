import redis
from .entities import Map

r = redis.Redis(host='localhost', port=6379, db=0)

class MapExporter():

  def __init__(self, monitoring_map:Map) -> None:
      pass