import matplotlib.pyplot as plt
from entities import Map


def paint_all(map_input: Map) -> None:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    ax1.imshow(map_input.temperature())
    ax2.imshow(map_input.hardness())

    ax3.imshow(map_input.current_energy())
    ax4.imshow(map_input.energy_income())

    fig.tight_layout()
    # plt.savefig('solid.png')
    plt.show()
