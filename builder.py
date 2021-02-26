from entities import BiomCenter, Map, Cell

class MapBuilder():

  width: int = 20
  height: int = 10

  biom_centers: list() = [
      BiomCenter(x=0,y=0,r=5,temprature=0,hardness=0.1),
      BiomCenter(x=0,y=height-1,r=5,temprature=80,hardness=0.9),
      BiomCenter(x=width-1,y=0,r=5,temprature=0,hardness=0.9),
      BiomCenter(x=width-1,y=height-1,r=5,temprature=80,hardness=0.1),
    ]
  defaultCell: Cell = Cell(-1, -1)

  def CreateSimple() -> Map:
    bioms = MapBuilder.biom_centers
    cells = []
    for i in range(MapBuilder.width):
      cells.append([])
      for j in range(MapBuilder.height):
        t, h = MapBuilder.interpolate(bioms, i, j)
        cells[i].append(Cell(i, j, temprature=t, hardness=h, current_energy=10, energy_income=1))
    
    return Map(cells=cells)

  def interpolate(bioms: list, i: int, j: int) -> tuple:
    coeffs = [b.Coefficient(i,j) for b in bioms]
    def_t = MapBuilder.defaultCell.temprature
    def_h = MapBuilder.defaultCell.hardness

    # t = 0
    # h = 0
    # index = coeffs.index(max(coeffs))
    # t = bioms[index].temprature * coeffs[index]
    # h = bioms[index].hardness * coeffs[index]

    t = def_t
    h = def_h
    for k, b in enumerate(bioms):
      t += b.temprature * coeffs[k]
      h += b.hardness * coeffs[k]
    t = t / (len(coeffs)+ 1)
    h = h / (len(coeffs)+1)

    return t, h
