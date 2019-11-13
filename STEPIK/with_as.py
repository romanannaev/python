# with open('dataset_24465_4.txt') as f, open('dataset.txt', 'w') as dat:
#     f = f.readlines()
#     for f in f[::-1]:
#         dat.write(f)
# with open('new.txt') as f, open("new1.txt", mode='w') as n:
#     f = f.readlines()[::-1]
#     n.write(''.join(f))
#     print(f)
with open('new.txt') as f, open("new1.txt", mode='w') as n:
   print(f.readable())
   
