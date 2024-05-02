import csv

def insertion(x):
    for i in range(1, len(x)): ##i will be the index for the postion in the list
        current_spot = x[i] ##current spot is the number position of the index being looped through
        position = i ##position is the index
        
        ##because while loop, it will keep shifting to the left until it reaches a left-side value to which it is greater than or until it reaches the very first position. Then it will run back up to the for loop to iterate the next index
        while position > 0 and x[position - 1] > current_spot: ##while not at the very first position and the value of the integer to the left of the current spot is greater than the value at the current spot 
            x[position] = x[position -1] ##switch positions
            position = position - 1 ##now the index will be one less to reflect the change in positions
            x[position] = current_spot ##update the current spot, what value we are currently at
        
    return x



file = open('PS4_test_dataset_Q1and2[85].txt', "r") ##Read in the file
data = file.read()
insert_list = data.replace('\n', ' ').split(".") ##Make the data into a list
insert_list = data.split(",") ##split up into separate elements
int_list = [] ##initialize new list for integers
for i in insert_list:
    integer = int(i)  ##converts data type of elements in insert_list to integers
    int_list.append(integer) ##append integers them to the new list



sorted_list = insertion(int_list) ##call the function
with open('Ahmad_PS4_1.csv', 'w', newline='') as file: ##writing csv file
    # Using csv.writer to write the list to the CSV file
    writer = csv.writer(file)
    writer.writerow(sorted_list)


