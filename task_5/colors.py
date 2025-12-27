import matplotlib.cm as cm
import matplotlib.colors as mcolors


def generate_colors(
    order: list[str],
    cmap_name: str = "Blues_r",
) -> dict[str, str]:

    n = len(order)
    if n == 0:
        return {}

    cmap = cm.get_cmap(cmap_name)

    colors: dict[str, str] = {}

    for i, node_id in enumerate(order):
        t = i / (n - 1) if n > 1 else 0.0
        rgba = cmap(t)
        colors[node_id] = mcolors.to_hex(rgba)

    return colors
