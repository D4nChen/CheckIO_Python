from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    result = True
    for i in elements:
        if elements.index(i) != 0:
            if i != elements[elements.index(i) - 1]:
                result = False
            else: 
                return result
    return result