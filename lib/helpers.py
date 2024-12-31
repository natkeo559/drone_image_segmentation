from pathlib import Path
import tomllib


def parse_colormap(data_dir: str | Path, colormap_index: int) -> dict:
    """
    Parses colormap data from a TOML file and returns a dictionary of class information.

    Args:
        data_dir (str | Path): The directory containing the 'colormaps.toml' file.
        colormap_index (int): The index of the colormap to parse (e.g., class_0, class_1, etc.).

    Returns:
        dict: A dictionary where keys are class names (str) and values are tuples:
              ((R, G, B), class_id).

    Raises:
        FileNotFoundError: If the 'colormaps.toml' file does not exist in the given directory.
        KeyError: If 'class_{colormap_index}' key or expected keys in the TOML data are missing.
        ValueError: If any data type is invalid or the parsed TOML data is malformed.
    """
    data_dir = Path(data_dir)

    colormap_file = data_dir / "colormaps.toml"
    if not colormap_file.exists():
        raise FileNotFoundError(f"File not found: {colormap_file}")

    try:
        with colormap_file.open("rb") as f:
            data = tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
        raise ValueError(f"Error decoding TOML file at {colormap_file}: {e}") from e

    colormap_key = f"class_{colormap_index}"
    if colormap_key not in data:
        raise KeyError(
            f"The TOML data does not contain the expected key '{colormap_key}'. "
            f"Available keys: {list(data.keys())}"
        )

    class_dict = {}
    for entry in data[colormap_key]:
        # Validate required fields
        for required_key in ("Classes", "R", "G", "B", "Id"):
            if required_key not in entry:
                raise KeyError(
                    f"Missing '{required_key}' in entry: {entry}. "
                    f"Ensure the TOML file is structured correctly."
                )

        class_name = entry["Classes"]
        if not isinstance(class_name, str):
            raise ValueError(
                f"Expected 'Classes' to be a string, got {type(class_name).__name__}."
            )

        try:
            rgb_tuple = (int(entry["R"]), int(entry["G"]), int(entry["B"]))
        except ValueError as e:
            raise ValueError(
                f"RGB values must be integers. Error in entry: {entry}"
            ) from e

        class_id = entry["Id"]
        if not isinstance(class_id, int):
            raise ValueError(
                f"Expected 'Id' to be an integer, got {type(class_id).__name__}."
            )

        class_dict[class_name] = (rgb_tuple, class_id)

    return class_dict
