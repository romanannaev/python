'''
Инкапсуляция

Python 3 предоставляет 3 уровня доступа к данным:
публичный (public, нет особого синтаксиса, publicBanana);
защищенный (protected, одно нижнее подчеркивание в начале названия, _protectedBanana);
приватный (private, два нижних подчеркивания в начала названия, __privateBanana).
Для краткости и простоты, только два базовых уровня (приватный и публичный) освещены в примере.'''

class Phone:
    username = "Kate"                # public variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print( "Ring-ring!" )

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

#my_phone.call()
#print( "The username is ", my_phone.username )
#my_phone.turn_on()
#my_phone.__turn_on()
#print( 'Turned on: ', my_phone.__how_many_times_turned_on)
#
print( 'Turned on: ', my_phone.how_many_times_turned_on)
# will produce an error
input( "Press Enter to exit" )


#---Нарушим инкапсуляцию----

'''class Phone:
    username = "Kate"                # public variable
    __serial_number = "11.22.33"     # private variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        print( "Ring-ring!" )

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1 
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

my_phone._Phone__turn_on()
my_phone._Phone__serial_number = "44.55.66"
print( "New serial number is ", my_phone._Phone__serial_number )

input( "Press Enter to exit" )'''














'''Несколько слов о Магии

Существуют методы, так называемые «магические методы» («magic methods») или «специальные методы» («special methods»), которые позволяют классам определять свое поведение в отношении стандартных языковых операторов. Примером таких языковых операторов могут служить следующие выражения:


x > y
x[ i ]

Python 3 поддерживает множество таких методов, полный список можно найти на странице официальной документации языка. __init__ (инициализатор) является наиболее часто используемым из них и запускается при создании нового объекта класса. Другой, __lt__ (расширенное сравнение), определяет правила для сравнения двух объектов пользовательского класса. Такие методы не попадают в категорию «приватных» или «публичных», поскольку служат другим целям и корнями глубоко уходят во внутреннюю структуру языка.


#!/usr/bin/python3

class Phone:
    def __init__(self, number):      # magic method / inititalizer
        print( "The Phone object was created" )
        self.number = number

    def __lt__(self, other):         # magic method / rich comparison
        return self.number < other.number

my_phone = Phone(20)
other_phone = Phone(30)

if my_phone < other_phone:
    print( "Two instances of custom class were compared" )
    print( "'__lt__' was called implicitly" )

if my_phone.__lt__(other_phone):
    print( "Now, '__lt__' was used explicitly" )

input( "Press Enter to exit" )

Магические методы могут быть вызваны любым пользователем таким же образом как и любой публичный метод в Питоне, однако они предназначены для неявного использования в своих особых случаях. Специальный случай для метода __init__ — инициализация нового объекта класса. __lt__ служит для сравнения двух объектов.


Заключение

Python3 не обеспечивает ограниченный доступ к каким-либо переменным или методам класса. Данные, которые должны быть скрыты, на самом деле могут быть прочитаны и изменены. В Python3 инкапсуляция является скорее условностью, и программист должен самостоятельно заботиться о ее сохранении.

'''