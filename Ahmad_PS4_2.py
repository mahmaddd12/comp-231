import csv

def quicksort(y):
    if len(y) <= 1: ##cannot work if len(y) is less than 1
        return y
    else:
        pivot = y[0] ##Set the first index equal to pivot(all numbers larger than it will go to right, all less than will go to left )
        l = [x for x in y[1:] if x < pivot] ## making list for values that will go left of pivot (less than), from the second index to end of the list
        r = [x for x in y[1:] if x >= pivot] ## Making list for values that will right of pivot (greater than), from second index to end of list
        return quicksort(l) + [pivot] + quicksort(r) ##concatenating the lists to get the ascending order

file = open('PS4_test_dataset_Q1and2[85].txt', "r") ##Read in the file
data = file.read()
insert_list = data.replace('\n', ' ').split(".") ##Make the data into a list
insert_list = data.split(",") ##split up into separate elements
int_list = [] ##initialize new list for integers
for i in insert_list:
    integer = int(i)  ##converts data type of elements in insert_list to integers
    int_list.append(integer) ##append integers them to the new list

sorted_list = quicksort(int_list)
with open('Ahmad_PS4_2.csv', 'w', newline='') as file: ##writing csv file
    # Using csv.writer to write the list to the CSV file
    writer = csv.writer(file)
    writer.writerow(sorted_list)