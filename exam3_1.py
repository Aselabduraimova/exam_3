list_ = [True, 2.3, None, "brook", 5]

type_dict = {}

for i in list_:
    if type(i) in [int]:
        type_dict["int"] = i

    elif type(i) == float:
        type_dict["float"] = i

    elif type(i) == str:
        type_dict["str"] = i

    elif type(i) == bool:
        type_dict["bool"] = i

    elif type(i) is not None:
        type_dict["none"] = i

print(type_dict)