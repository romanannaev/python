#проигранное сражение
#демонстирует работу бесконечного цикла

print("вашего героя окружила многочисленная толпа троллей.")
print("Смрадными зелеными трупами устлана земля.")
print("Одинокий герой достает меч из ножен дабы сразиться в последней битве "\
      ,"ненавистым врагом.\n")

health = 10
trolls = 0
damage = 2

while health != 0:
    trolls += 1
    health -= damage
    print("Взмахнув мечом ,ваш герой убывает тролля ,"\
        " но сам при этом получает повреждений на ", damage, "очков.\n")

print("Ваш герой доблестно сражался и убил ", trolls , "троллей.")
print("Но увы!Он пал на поле боя сам((.")

input("\n\n Press enter key to exit")
    
    
