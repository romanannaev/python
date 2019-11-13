#https://tproger.ru/translations/demystifying-decorators-in-python/

'''Декораторы — один из самых полезных инструментов в Python,
однако новичкам они могут показаться непонятными. Возможно,
 вы уже встречались с ними, например, при работе с Flask,
 но не хотели особо вникать в суть их работы. Эта статья поможет вам понять,
 чем являются декораторы и как они работают.

Что такое декоратор?
Новичкам декораторы могут показаться неудобными и непонятными,
потому что они выходят за рамки «обычного» процедурного программирования как в Си,
 где вы объявляете функции, содержащие блоки кода, и вызываете их.
  То же касается и объектно-ориентированного программирования,
  где вы определяете классы и создаёте на их основе объекты.
  Декораторы не принадлежат ни одной из этих парадигм и исходят из области функционального программирования.
  Однако не будем забегать вперёд, разберёмся со всем по порядку.

Декоратор — это функция,
которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.
 Вот почему декораторы можно рассматривать как практику метапрограммирования,
 когда программы могут работать с другими программами как со своими данными.
  Чтобы понять, как это работает, сначала разберёмся в работе функций в Python.

Как работают функции
Все мы знаем, что такое функции, не так ли? Не будьте столь уверены в этом.
 У функций Python есть определённые аспекты, с которыми мы нечасто имеем дело, и,
  как следствие, они забываются. Давайте проясним, что такое функции и как они представлены в Python.

Функции как процедуры
С этим аспектом функций мы знакомы лучше всего. Процедура — это именованная последовательность вычислительных шагов.
 Любую процедуру можно вызвать в любом месте программы, в том числе внутри другой процедуры или даже самой себя.
  По этой части больше нечего сказать, поэтому переходим к следующему аспекту функций в Python.

Функции как объекты первого класса
В Python всё является объектом, а не только объекты, которые вы создаёте из классов.
 В этом смысле он (Python) полностью соответствует идеям объектно-ориентированного программирования.
  Это значит, что в Python всё это — объекты:

числа;
строки;
классы (да, даже классы!);
функции (то, что нас интересует).
Тот факт, что всё является объектами, открывает перед нами множество возможностей.
 Мы можем сохранять функции в переменные, передавать их в качестве аргументов и возвращать из других функций.
  Можно даже определить одну функцию внутри другой. Иными словами, функции — это объекты первого класса.
   Из определения в Википедии:

Объектами первого класса в контексте конкретного языка программирования называются элементы,
 с которыми можно делать всё то же, что и с любым другим объектом: передавать как параметр,
 возвращать из функции и присваивать переменной.

И тут в дело вступает функциональное программирование, а вместе с ним — декораторы.

Функциональное программирование — функции высших порядков
В Python используются некоторые концепции из функциональных языков вроде Haskell и OCaml.
 Пропустим формальное определение функционального языка и перейдём к двум его характеристикам, свойственным Python:

функции являются объектами первого класса;
следовательно, язык поддерживает функции высших порядков.
Функциональному программированию присущи и другие свойства вроде отсутствия побочных эффектов,
 но мы здесь не за этим. Лучше сконцентрируемся на другом — функциях высших порядков.
 Что есть функция высшего порядка? Снова обратимся к Википедии:

Функции высших порядков — это такие функции, которые могут принимать в качестве аргументов и возвращать другие функции.

Если вы знакомы с основами высшей математики,
 то вы уже знаете некоторые математические функции высших порядков порядка вроде дифференциального оператора d/dx.
 Он принимает на входе функцию и возвращает другую функцию, производную от исходной.
  Функции высших порядков в программировании работают точно так же — они либо принимают функцию(и)
   на входе и/или возвращают функцию(и).

Пара примеров
Раз уж мы ознакомились со всеми аспектами функций в Python, давайте продемонстрируем их в коде:

def hello_world():
    print('Hello world!')
Здесь мы определили простую функцию. Из фрагмента кода далее вы увидите, что эта функция, как и классы с числами,
 является объектом в Python:'''

'''> def hello_world():
...     print('Hello world!')
...
>>> type(hello_world)
<class 'function'>
>>> class Hello:
...     pass
...
>>> type(Hello)
<class 'type'>
>>> type(10)
<class 'int'>'''


'''Как работают декораторы
Повторим определение декоратора:

Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её 
функциональности без непосредственного изменения её кода.

Раз мы знаем, как работают функции высших порядков, теперь мы можем понять как работают декораторы. 
Сначала посмотрим на пример декоратора:'''

# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#     return wrapper


# @decorator_function
# def hello_world():
#      print('Hello world!')



# hello_world()

'''Магия, не иначе! Просто добавив @decorator_function перед определением функции hello_world(),
      мы модифицировали её поведение. Однако как вы уже могли догадаться, 
     выражение с @ является всего лишь синтаксическим сахаром для
      hello_world = decorator_function(hello_world).'''


#Полезный пример

# def benchmark(func):
#     import time
#
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
#
#
# fetch_webpage()


'''Используем аргументы и возвращаем значения
В приведённых выше примерах декораторы ничего не принимали и не возвращали. 
Модифицируем наш декоратор для измерения времени выполнения:'''

def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')
print(webpage)

'''Как вы видите, аргументы декорируемой функции передаются функции-обёртке, 
после чего с ними можно делать что угодно. Можно изменять аргументы и затем передавать их декорируемой функции,
а можно оставить их как есть или вовсе забыть про них и передать что-нибудь совсем другое. 
То же касается возвращаемого из декорируемой функции значения, с ним тоже можно делать что угодно.'''