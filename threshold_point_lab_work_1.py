class_a = list(map(int, input("Enter points of class A : ").split()))
class_b = list(map(int, input("Enter point of class B : ").split()))

min_value = min(class_a+class_b)
max_value = max(class_a+class_b)

accuracy = 0.0
point = 0

def min_error(l,value):
    counter=0
    for i in l:
        if value<=i:
            counter = counter + 1
    return counter

def max_error(l,value):
    counter = 0

    for i in l:
        if value>i:
            counter = counter + 1
    return counter

total_values = len(class_a) + len(class_b)
for i in range(min_value,max_value,1):
    mismatched_value = min_error(class_a,i) + max_error(class_b,i)
    print(mismatched_value,i)
    temp_accuracy = (total_values-mismatched_value)/total_values
    #print(temp_accuracy,total_values-mismatched_value,total_values,sep=" ")
    if temp_accuracy>=accuracy:
        accuracy = temp_accuracy
        point = i

print("Accuracy = "+str(accuracy*100)+"%")
print("Threshold point : "+str(point))
