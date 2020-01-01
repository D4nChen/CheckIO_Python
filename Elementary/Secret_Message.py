def find_message(text: str) -> str:
    """Find a secret message"""
    result = ""
    for ch in text:
        if ch.isupper() == True:
            result = result + ch 
    return result

if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")