def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    if symbol in text:
        i = text.index(symbol) + 1
        if symbol in text[i:]:
            return i + text[i:].index(symbol)
        return None
    
    return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

    # pos = -1
    
    # for x in range(2):
    #     pos = text.find(symbol, pos + 1)
        
    # return pos if pos != -1 else None
    try:
        return text.index(symbol, text.index(symbol) + 1)
    except ValueError:
        return None
