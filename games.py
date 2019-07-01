#games
#demonstrates create modul 

class Player(object):
    """ участник игры """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """задает question with answer"""
    response = None
    while response not in ('y', "n"):
        response = input (question).lower()
    return response 

def ask_number(question, low, high):
    """prosit enter guess from zadannii diapazon"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print('you entered this modul napryamu, but don"t import him')
    print('\n\n Press enter for exit')
