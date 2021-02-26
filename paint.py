import matplotlib.pyplot as plt
from entities import Map


def paint_all(map_input: Map) -> None:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    ax1.imshow(map_input.temperature(),cmap=plt.cm.YlOrRd)
    ax2.imshow(map_input.hardness(),cmap=plt.cm.Blues)

    ax3.imshow(map_input.current_energy(),cmap=plt.cm.YlGn)
    ax4.imshow(map_input.energy_income(),cmap=plt.cm.summer)

    fig.tight_layout()
    # plt.savefig('solid.png')
    plt.show()
