import numpy as np
import random
data = []
for x in range(50):
    num = random.randint(250,300)
    data.append(num)

for x in range(100):
    num = random.randint(200,250)
    data.append(num)

for x in range(1000):
    num = random.randint(100,200)
    data.append(num)

for x in range(5000):
    num = random.randint(100,200)
    data.append(num)
# data = [1,3,8,12,15,16,25,33,34,39,44,51,56,60,64,70,82,84,86,90,93,96,97,100]
percentile = np.arange(0, 100, 5)
percentile = percentile[1:]
print(percentile)
n = len(data)
print(n)
result = {}
for k in percentile:
    i = (k/100)*(n + 1)
    if(not i.is_integer()):
        down = int(i)
        up = down + 1
        down_n = data[down-1]
        up_n = data[up-1]
        p = (down_n+up_n)/2
    else:
        p = data[int(i)-1]
   
    result[k] = p


for key, value in result.items():
    if(key-5 == 0):
        print("{0}% of data value are less than or equal to {1}".format(key, value))
    else:
        before_value = result[key-5]
        students = 0
        studentscore = []
        for datum in data:            
            if datum > before_value and datum <= value:
                studentscore.append(datum)
                students = students + 1
        # print(studentscore)    
        print("{0}% of data value are less than or equal to {1} and {2} students are between {3}% and {0}%".format(key, value, students, key-5))


    
    

