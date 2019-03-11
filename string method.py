#манипуляция с цитатой
#демонстрирует строковые методы
#цитата дирика ibm в 1943
quote = "Думаю на мировом рынке можно будет продать штук пять компьютеров."
print("Исходная цитата:")
print(quote)
print("\n Она же в верхнем регистре:")
print(quote.upper())
print("\n В нижнем регистре:")
print(quote.lower())
print("\n Как заголовок:")
print(quote.title())
print("\n С ма-а-аленькой заменой:")
print(quote.replace("штук пять","несколько миллиардов"))
print("\n а вот опять исходная цитата:")
print(quote*2)
input("\n\n press enter men")
