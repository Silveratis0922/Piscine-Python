def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float):
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    elif (isinstance(object, str)) and (len(object) == 0):
        print(f"Empty: {object}{type(object)}")
    elif isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    else:
        print("Type not found")
    return (1)
