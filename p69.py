dict1 = {'-----':0,'.----':1,'..---':2,'...--':3,'....-':4,'.....':5,'-....':6,'--...':7,'---..':8,'----.':9}
s = input("")
list1 = s.split(" ")

#print(type(list1))

total = ""
for i in list1:
    total = total + str(dict1[i])
print(total)