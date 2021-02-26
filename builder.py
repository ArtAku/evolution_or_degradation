from entities import BiomCenter, Map, Cell, temperature_range, hardness_range
from scipy.interpolate import interp2d

def default_energy_income(t:float, h:float) -> tuple:
    k_t = 5.0
    m_t = (temperature_range[1] + temperature_range[0]) / 4.0 * 3.0 # best temperature
    r_t = (temperature_range[1] - temperature_range[0]) # temperature range
    _t = r_t - abs(t - m_t) 
    _t = _t / r_t * k_t
    k_h = 5.0
    m_h = (hardness_range[1] + hardness_range[0]) / 2.0 # best hardness
    r_h = (hardness_range[1] - hardness_range[0]) # hardness range
    _h = r_h - abs(h - m_h)
    _h = _h / r_h * k_h
    return _t + _h

def default_start_energy(t:float, h:float) -> tuple:
    k_t = 5.0
    m_t = (temperature_range[1] + temperature_range[0]) / 4.0 # best temperature
    r_t = (temperature_range[1] - temperature_range[0]) # temperature range
    _t = r_t - abs(t - m_t) 
    _t = _t / r_t * k_t
    k_h = 5.0
    m_h = (hardness_range[1] + hardness_range[0]) / 4.0 * 3.0 # best hardness
    r_h = (hardness_range[1] - hardness_range[0]) # hardness range
    _h = r_h - abs(h - m_h)
    _h = _h / r_h * k_h
    return _t + _h

class MapBuilder():

    width: int = 20
    height: int = 10

    biom_centers: list = [
        BiomCenter(x=0, y=0, temprature=50, hardness=10),
        BiomCenter(x=0, y=height - 1, temprature=10, hardness=80),
        BiomCenter(x=width - 1, y=0, temprature=10, hardness=80),
        BiomCenter(x=width - 1, y=height - 1, temprature=50, hardness=10),
    ]

    def create_simple() -> Map:
        bioms = MapBuilder.biom_centers
        x = [b.x for b in bioms]
        y = [b.y for b in bioms]
        temprature = [b.temprature for b in bioms]
        hardness = [b.hardness for b in bioms]
        interp_t = interp2d(x, y, temprature)
        interp_h = interp2d(x, y, hardness)
        cells = []
        for i in range(MapBuilder.height):
            cells.append([])
            for j in range(MapBuilder.width):
                t, h = interp_t(j, i), interp_h(j, i)
                cells[i].append(Cell(j, i, temprature=t, hardness=h,
                                     current_energy=10, energy_income=1))

        return Map(cells=cells)

    def create_complex(**params) -> Map:
        bioms = params.get('bioms') or MapBuilder.biom_centers
        width = params.get('width') or MapBuilder.width
        height = params.get('height') or MapBuilder.height

        start_energy = params.get('start_energy') or default_start_energy
        energy_income = params.get('energy_income') or default_energy_income
        x = [b.x for b in bioms]
        y = [b.y for b in bioms]
        temprature = [b.temprature for b in bioms]
        hardness = [b.hardness for b in bioms]
        interp_t = interp2d(x, y, temprature)
        interp_h = interp2d(x, y, hardness)
        cells = []
        for i in range(height):
            cells.append([])
            for j in range(width):
                t, h = interp_t(j, i), interp_h(j, i)
                cells[i].append(Cell(j, i, temprature=t, hardness=h,
                                     current_energy=start_energy(t, h), energy_income=energy_income(t, h)))

        return Map(cells=cells)
