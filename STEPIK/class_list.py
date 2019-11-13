import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, num):
        super(LoggableList, self).append(num)
        return self.log(num)

x = LoggableList([1, 2])
print(x)
x.append(1)
print(x)