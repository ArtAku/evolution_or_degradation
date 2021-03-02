import matplotlib.pyplot as plt
from entities import Map
from matplotlib.pyplot import cm


def paint_all(map_input: Map) -> None:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    ax1.imshow(map_input.temperature(), cmap=cm.YlOrRd)
    ax2.imshow(map_input.hardness(), cmap=cm.Blues)

    ax3.imshow(map_input.current_energy(), cmap=cm.YlGn)
    ax4.imshow(map_input.energy_income(), cmap=cm.summer)

    fig.tight_layout()
    # plt.savefig('solid.png')
    plt.show()
