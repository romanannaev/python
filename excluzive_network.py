#эксклюзивная сеть
#демонстрирует работу составных условий и логических операторов

print("\t Эксклюзивная компьютерная сеть")
print("\t Только для зарегистрированных пользователей! \n")

security = 0
username = ""

while not username :
    username = input ("Введите логин:") 

password = ""
while not password :
    password = input("Введите пароль:")

if username == "M.Dowson" and password == "secret":
    print("Привет, майк!")
    security = 5

elif username == "roman" and password == "annaev":
    print("hi,roma!")
    security = 3

elif username == "Mr.name" and password == "name":
    print("прив мистер найм. как дела?")
    security = 3

elif username == "con'" and password == "con'":
    print("здоров мистер конь,и пока")
    security = 3

elif username == "quest" or password == "quest":
    print("Добро пожаловать в компьютерные системы,вы в гостях")
    security = 1

else :
    print("\n\t Войти в систему не удалось,дожно быть вы и не очень то важный"
          , "парень для нас. \n ")
input ("\n\t press key enter to exit")
