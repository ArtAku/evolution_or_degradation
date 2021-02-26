import matplotlib.pyplot as plt
from entities import Map

def paint_all(map: Map) -> None:
  fig, ((ax),(ax2)) = plt.subplots(1, 2)

  ax.imshow(map.Temperature())
  ax2.imshow(map.Hardness())

  fig.tight_layout()
  # plt.savefig('solid.png')
  plt.show()