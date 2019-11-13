# программа печатает буквы исходного слова наоборот

#используем списки,срезы и цикл while

print("\nПривет,я буду переворачивать твое любое слово,узнаешь ли ты его?")
word = input("\nВведите исходное слово: ")
rather = ""

while word :
        position = len(word)
        rather += word[(position-1)]
    
        word = word[0:(position - 1)]
    
        
print ("\nВот перевернутое слово: ", rather)
input("\n\t\t\tНажмите Enter, чтобы выйти. ")
    
