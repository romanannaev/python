def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    lst = []
    for s in phrases:
        if s.find('right') != -1:
            new_s = s.replace('right', 'left' )
            lst.append(new_s)
        else:
            lst.append(s)
    return ','.join(lst)
    

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# import re
# string = ','.join(phrases)
#     string = re.sub(r'right', 'left', string)
#     return string

# return (",".join(phrases)).replace("right","left")