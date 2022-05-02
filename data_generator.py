from random import randint

# A script that generates in a format that is accepted by algorithm
# f = open(input("Enter file name: "), 'w')
f = open("test", "w")
data_quantity = int(input("Enter data quantity: "))
f.write(str(data_quantity))
f.write('\n')
for i in range(0, data_quantity):
    f.write(str(randint(1, data_quantity)))
    f.write(' ')
    f.write(str(randint(1, data_quantity)))
    f.write(' ')
    f.write(str(randint(1, data_quantity)))
    f.write('\n')
f.close()
