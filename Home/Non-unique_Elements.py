def checkio(data: list) -> list:
    newlist = [item for item in data if data.count(item)!=1]
    return newlist