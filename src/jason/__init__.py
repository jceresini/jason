def convert_to_jason(o: object):

    first_name_keys = [
        "first_name",
        "firstname",
        "fname",
        "f_name",
    ]

    for k in first_name_keys:
        if hasattr(o, k):
            setattr(o, k, "Jason")

    full_name_keys = [
        "name",
        "full_name",
    ]

    for k in full_name_keys:
        if hasattr(o, k):
            n = getattr(o, k)
            parts = n.split(" ")
            parts[0] = "Jason"
            setattr(o, k, " ".join(parts))

    return o
