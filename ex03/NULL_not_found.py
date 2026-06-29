def NULL_not_found(object: any) -> int:
    if isinstance(object, str) and object != "":
        print("Type not found")
        return (1)
    elif isinstance(object, type(None)):
        print(f"Nothing : {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty : {object} {type(object)}")
    else:
        print("Other")
    return (0)