def checkio(number):
    
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res

if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")