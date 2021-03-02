from entities import BiomCenter, Map, Cell, temperature_range, hardness_range
from scipy.interpolate import interp2d
from random import randint


def default_energy_income(t: float, h: float) -> tuple:
    k_t = 5.0
    m_t = (temperature_range[1] + temperature_range[0]
           ) / 4.0 * 3.0  # best temperature
    r_t = (temperature_range[1] - temperature_range[0])  # temperature range
    _t = r_t - abs(t - m_t)
    _t = _t / r_t * k_t
    k_h = 5.0
    m_h = (hardness_range[1] + hardness_range[0]) / 2.0  # best hardness
    r_h = (hardness_range[1] - hardness_range[0])  # hardness range
    _h = r_h - abs(h - m_h)
    _h = _h / r_h * k_h
    return _t + _h


def default_start_energy(t: float, h: float) -> tuple:
    k_t = 5.0
    m_t = (temperature_range[1] + temperature_range[0]
           ) / 4.0  # best temperature
    r_t = (temperature_range[1] - temperature_range[0])  # temperature range
    _t = r_t - abs(t - m_t)
    _t = _t / r_t * k_t
    k_h = 5.0
    m_h = (hardness_range[1] + hardness_range[0]) / 4.0 * 3.0  # best hardness
    r_h = (hardness_range[1] - hardness_range[0])  # hardness range
    _h = r_h - abs(h - m_h)
    _h = _h / r_h * k_h
    return _t + _h


default_width: int = 20
default_height: int = 10

default_biom_centers: list = [
    BiomCenter(x=0, y=0, temperature=50, hardness=10),
    BiomCenter(x=0, y=default_height - 1, temperature=99, hardness=80),
    BiomCenter(x=default_width - 1, y=0, temperature=10, hardness=80),
    BiomCenter(
        x=default_width - 1,
        y=default_height - 1,
        temperature=99,
        hardness=10),
]


def create_simple() -> Map:
    bioms = default_biom_centers
    x = [b.center_x for b in bioms]
    y = [b.center_y for b in bioms]
    temperature = [b.temperature for b in bioms]
    hardness = [b.hardness for b in bioms]
    interp_t = interp2d(x, y, temperature)
    interp_h = interp2d(x, y, hardness)
    cells = []
    for i in range(default_height):
        cells.append([])
        for j in range(default_width):
            t, h = interp_t(j, i), interp_h(j, i)
            cells[i].append(Cell(j, i, temperature=t, hardness=h,
                                 current_energy=10, energy_income=1))

    return Map(cells=cells)


def create_complex(**params) -> Map:
    bioms = params.get('bioms') or default_biom_centers
    width = params.get('width') or default_width
    height = params.get('height') or default_height

    start_energy = params.get('start_energy') or default_start_energy
    energy_income = params.get('energy_income') or default_energy_income
    x = [b.center_x for b in bioms]
    y = [b.center_y for b in bioms]
    temperature = [b.temperature for b in bioms]
    hardness = [b.hardness for b in bioms]
    interp_t = interp2d(x, y, temperature)
    interp_h = interp2d(x, y, hardness)
    cells = []
    for i in range(height):
        cells.append([])
        for j in range(width):
            t, h = interp_t(j, i), interp_h(j, i)
            cells[i].append(Cell(j, i, temperature=t, hardness=h,
                                 current_energy=start_energy(t, h), energy_income=energy_income(t, h)))
    # cells = cut_bounds(cells)
    return Map(cells=cells)


def create_random(**params) -> Map:
    width = params.get('width') or default_width
    height = params.get('height') or default_height

    start_energy = params.get('start_energy') or default_start_energy
    energy_income = params.get('energy_income') or default_energy_income
    num_bioms = range(params.get('num_bioms') or 4)
    bioms = [
        BiomCenter(
            x=randint(
                0, width), y=randint(
                0, height), temperature=randint(
                temperature_range[0], temperature_range[1]), hardness=randint(
                    hardness_range[0], hardness_range[1])) for n in num_bioms]

    for b in bioms:
        print(b)

    x = [b.center_x for b in bioms]
    y = [b.center_y for b in bioms]
    temperature = [b.temperature for b in bioms]
    hardness = [b.hardness for b in bioms]
    interp_t = interp2d(x, y, temperature)
    interp_h = interp2d(x, y, hardness)
    cells = []
    for i in range(height):
        cells.append([])
        for j in range(width):
            t, h = interp_t(j, i)[0], interp_h(j, i)[0]
            cells[i].append(Cell(j, i, temperature=t, hardness=h,
                                 current_energy=start_energy(t, h), energy_income=energy_income(t, h)))
    cells = cut_bounds(cells)
    return Map(cells=cells)


def cut_bounds(cells: list) -> Map:
    for i in range(len(cells)):
        row_cells: list = cells[i]
        for j in range(len(row_cells)):
            cell: Cell = row_cells[j]
            t, h = cell.temperature, cell.hardness
            if t < temperature_range[0]:
                cell.temperature = temperature_range[0]
            if t > temperature_range[1]:
                cell.temperature = temperature_range[1]
            if h < hardness_range[0]:
                cell.hardness = hardness_range[0]
            if h > hardness_range[1]:
                cell.hardness = hardness_range[1]
            if cell.current_energy < 0:
                cell.current_energy = 0
            if cell.energy_income < 0:
                cell.energy_income = 0
    return cells
