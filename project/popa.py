c = open("C:/Users/amiGos/Desktop/roma.txt", "r")

correct = c.readline()
if correct:
    correct = correct[45]
    print(correct)