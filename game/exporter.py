import redis
from entities import Map, temperature_range, hardness_range, energy_range
from configurator import redis_config
from logger import get_logger


class MapMonitor():
    # redis_client: Redis_client =
    # monitoring_map
    logger = get_logger(__name__)

    def __init__(self, monitoring_map: Map) -> None:
        self.monitoring_map = monitoring_map

    def export_map(self) -> None:
        raise Exception("Not implemented!")


class RedisMapMonitor(MapMonitor):

    def __init__(self, monitoring_map: Map) -> None:
        super().__init__(monitoring_map)
        self.redis_client = redis.Redis(
            host=redis_config['REDIS_HOST'],
            port=redis_config['REDIS_PORT'],
            db=0)
        self.logger.info("Redis client establish connection")
        self.redis_client.set("a", "b")
        self.logger.info("Redis client establish connection")

    def export_map(self) -> None:
        cells: list = self.monitoring_map.cells
        width = self.monitoring_map.width
        height = self.monitoring_map.height
        mx = 0

        for raw in cells:
            for c in raw:
                if c.energy_income > mx:
                    mx = c.energy_income

        self.redis_client.set(f"height", height)
        self.logger.debug(f"Redis export height: {height}")
        self.redis_client.set(f"width", width)
        self.logger.debug(f"Redis export width: {width}")
        for i, cells_raw in enumerate(cells):
            self.redis_client.set(f"{i}_t", str(
                [c.temperature / temperature_range[1] for c in cells_raw]))
            self.redis_client.set(f"{i}_h", str(
                [c.hardness / hardness_range[1] for c in cells_raw]))
            self.redis_client.set(f"{i}_e", str(
                [c.current_energy / energy_range[1] for c in cells_raw]))
            self.redis_client.set(f"{i}_i", str(
                [c.energy_income / mx for c in cells_raw]))
        self.logger.info("Redis export map")

    # def import_map(self) -> None:
    #     height, width = self.monitoring_map.height, self.monitoring_map.width

    #     cells = []
    #     for i in range(height):
    #         cells.append([])
    #         for j in range(width):
    #             temperature = float(self.redis_client.get(f"{i}_{j}_t").decode("utf-8"))
    #             hardness = float(self.redis_client.get(f"{i}_{j}_h").decode("utf-8"))
    #             current_energy = float(self.redis_client.get(f"{i}_{j}_e").decode("utf-8"))
    #             energy_income = float(self.redis_client.get(f"{i}_{j}_i").decode("utf-8"))
    #             cells[i].append({
    #                 "temperature": temperature,
    #                 "hardness": hardness,
    #                 "current_energy": current_energy,
    #                 "energy_income": energy_income,
    #             })
    #     self.logger.info("Redis import map")
    #     return cells
