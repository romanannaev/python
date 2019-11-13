from datetime import datetime


def get_Time_It(arg):
        print(arg)
        def outer(func):
                def wrapper(*args, **kwargs):
                        start = datetime.now()
                        result = func(*args, **kwargs)
                        print(datetime.now() - start)
                        return result
                return wrapper
        return outer


@get_Time_It('roma')
def get_List_One (n):
        #start = datetime.now()
        l = []
        for i in range(n):
                if i % 2 == 0:
                        l.append(i)
        # print(datetime.now() - start)
        return l
@get_Time_It('name')
def get_List_Two(n):
        #start = datetime.now()
        l1 = [x for x in range(n) if x % 2 == 0]
        #print(datetime.now() - start)
        return l1



l = get_Time_It('roma')(get_List_Two)(10**4)



