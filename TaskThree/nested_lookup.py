def get_value_by_path(obj: dict, path: str, delimiter: str = "/") -> str:
   
    if not isinstance(obj, dict):
        raise TypeError("Provided object is not a dictionary")

    keys = path.split(delimiter)
    current = obj

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            raise KeyError(f"Key path '{path}' not found at '{key}'")

    return current
