# только гласные
#демонстрирует как создавать новые строки из исходных данных с помощью цикла for

message = input("\nВведите ваш текст : ")
new_message = ""
VOWELS = "aiuoeаеёиуоыэюя"
print()

for letter in message:
    if letter.lower() not in VOWELS :
        new_message += letter
        
        print("Создана новая строка: ", new_message)

print ("\nВот новый текст с изъятыми гласными буквами : ", new_message)
input("\nНажмите enter, чтобы выйти.")
