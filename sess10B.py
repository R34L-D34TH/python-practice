#1D list
my_data=[10, 20, 30]

#2D List
numbers =  [
    [10,20,30],
    [40,50,60,70,80],
    [90,99]
]
largeData = [
    [
    [10,20,30],
    [40,50,60,70,80],
    [90,99]
],
[
    [10,20,30],
    [40,50,60,70,80],
    [90,99]
]
]

print(len(numbers)) # output --> 3
print(numbers[1])
print(my_data[-1])
print (largeData [-2][-2][-4])

#Slicing 

data = list(range(10, 101, 10))
print("Data: ", data)
print("5:- ",data[:5]) # index will run till index 4 (less than 5)
print(data[6:]) #start from 6th index till end
print(data[5:9]) #start from 5th index till 8th (less than 9)
 
 # IQ
print("-5:- ", data[:-5]) #start from 5th index till 8th (less than 9)
print(data[-5:-2]) #start from 5th index till 8th (less than 9)

#concatenation
data1 = [10,20,30]
data2 = [40,50,60]

data3 = data1 + data2
print("data3:- ", data3)

#mutiplicity
data4 = data1 * 2 #repeat same data 2 times
print(data4)

#membership testing
print(10 in data1)
print(100 in data1)
print(100 not in data1)