import numpy as np
import random

data = []
for x in range(50):
    num = random.randint(250,300)
    data.append(num)

for x in range(150):
    num = random.randint(200,250)
    data.append(num)

for x in range(5000):
    num = random.randint(100,200)
    data.append(num)

for x in range(100000):
    num = random.randint(0,100)
    data.append(num)

# data = [1,3,8,12,15,16,25,33,34,39,44,51,56,60,64,70,82,84,86,90,93,96,97,100]
step = 5
percentile = np.arange(0, 105, step)
print(percentile)

result = {}
for k in percentile:
    p = np.percentile(data, k)
    print(k,p)
    result[k] = p

for key, value in result.items():
    if(key-step == -5):
        print("{0}% of data value are less than or equal to {1}".format(key, value))
    else:
        before_value = result[key-step]
        students = 0
        studentscore = []
        for datum in data:            
            if datum > before_value and datum <= value:
                studentscore.append(datum)
                students = students + 1
        # print(studentscore)    
        print("{0}% of data value are less than or equal to {1} and {2} students are between {3}% and {0}% percentile".format(key, value, students, key-step))

