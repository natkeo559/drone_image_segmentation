from lib.helpers import parse_colormap

DATA_DIR = "data/"


def test_parse_colormaps() -> None:
    colormap_dict = {
        "unlabeled": ((0, 0, 0), 0),
        "paved-area": ((128, 64, 128), 1),
        "dirt": ((130, 76, 0), 2),
        "grass": ((0, 102, 0), 3),
        "gravel": ((112, 103, 87), 4),
        "water": ((28, 42, 168), 5),
        "rocks": ((48, 41, 30), 6),
        "pool": ((0, 50, 89), 7),
        "vegetation": ((107, 142, 35), 8),
        "roof": ((70, 70, 70), 9),
        "wall": ((102, 102, 156), 10),
        "window": ((254, 228, 12), 11),
        "door": ((254, 148, 12), 12),
        "fence": ((190, 153, 153), 13),
        "fence-pole": ((153, 153, 153), 14),
        "person": ((255, 22, 96), 15),
        "dog": ((102, 51, 0), 16),
        "car": ((9, 143, 150), 17),
        "bicycle": ((119, 11, 32), 18),
        "tree": ((51, 51, 0), 19),
        "bald-tree": ((190, 250, 190), 20),
        "ar-marker": ((112, 150, 146), 21),
        "obstacle": ((2, 135, 115), 22),
        "conflicting": ((255, 0, 0), 23),
    }

    class_dict = parse_colormap(data_dir=DATA_DIR, colormap_index=0)

    assert class_dict == colormap_dict
