import redis
from entities import Map
from configurator import redis_config
from logger import get_logger


class MapMonitor():
    # redis_client: Redis_client = 
    # monitoring_map
    logger = get_logger(__name__)

    def __init__(self, monitoring_map:Map) -> None:
        self.monitoring_map = monitoring_map

    def export_map(self) -> None:
        raise Exception("Not implemented!")

class RedisMapMonitor(MapMonitor):

    def __init__(self, monitoring_map: Map) -> None:
        super().__init__(monitoring_map)
        self.redis_client = redis.Redis(host=redis_config['REDIS_HOST'], port=redis_config['REDIS_PORT'], db=0)
        self.logger.info("Redis client establish connection")
        self.redis_client.set("a","b")
        self.logger.info("Redis client establish connection")

    def export_map(self) -> None:
        cells:list = self.monitoring_map.cells
        self.redis_client.set(f"height", len(cells))
        self.redis_client.set(f"width", len(cells[0]))
        for i, cells_raw in enumerate(cells):
            for j, cell in enumerate(cells_raw):
                self.redis_client.set(f"{i}_{j}_t", str(cell.temprature))
                self.redis_client.set(f"{i}_{j}_h", str(cell.hardness))
                self.redis_client.set(f"{i}_{j}_e", str(cell.current_energy))
                self.redis_client.set(f"{i}_{j}_i", str(cell.energy_income))
        self.logger.info("Redis export map")
    
    def import_map(self) -> None:
        height, width = len(self.monitoring_map.cells), len(self.monitoring_map.cells[0])

        cells = []
        for i in range(height):
            cells.append([])
            for j in range(width):
                temprature = float(self.redis_client.get(f"{i}_{j}_t").decode("utf-8"))
                hardness = float(self.redis_client.get(f"{i}_{j}_h").decode("utf-8"))
                current_energy = float(self.redis_client.get(f"{i}_{j}_e").decode("utf-8"))
                energy_income = float(self.redis_client.get(f"{i}_{j}_i").decode("utf-8"))
                cells[i].append({
                    "temprature": temprature,
                    "hardness": hardness,
                    "current_energy": current_energy,
                    "energy_income": energy_income,
                })
        self.logger.info("Redis import map")
        return cells