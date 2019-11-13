# def find_message(text: str) -> str:
#     """Find a secret message"""
    

#     return "".join(s for s in text if s.islower()== True)
    

# print(find_message('Hello DANhjkjh you know World!'))
# def checkio(number: int) -> str:
    

#     if number % 3 == 0 and number % 5 == 0 :

#         return 'Fizz Buzz'

#     elif number % 3 == 0 :

#         return 'Fizz'

#     elif number % 5 == 0 :

#         return 'Buzz'
#     else :
#         return str(number)


# print(checkio(8))
# def checkio(array):
#     """
#         sums even-indexes elements and multiply at the last
#     """
#     total = []
#     if array:
#         for i in range(len(array)):
#             if i % 2 == 0:
#                 total.append(array[i])
                
#         x = sum(total) * array[-1]
#         return x
#     else:
#         return 0

# print(checkio([0, 1, 2, 3, 4, 5]))
# eturn sum(array[i] for i in range(len(array)) if not i % 2) * array[-1] if array else 0

