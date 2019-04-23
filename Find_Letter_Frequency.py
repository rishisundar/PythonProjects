import re
fileName = raw_input("Enter the file name : ")
input_file = open(fileName,"r")
pattern = re.compile('[^a-zA-Z]+')
dict = {}
count = 0
input = input_file.read()
input_file.close()
input = re.sub(pattern,'', input)
for n in input:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
        count += 1
    else:
        dict[n] = 1
        count += 1
print ('Total Letters {}').format(count)
for i in sorted(dict.keys()):
    print("letter {} : Count : {:<4} Percentage : {:.2f}%".format(i,dict[i],float((dict[i]*100.0)/count)))
