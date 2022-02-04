
#This line imports the data and assigns it to the variable log_file
log_file = open("um-server-01.txt")

#This line set up a functions and sets a parameter:
def sales_reports(log_file):
    #This is a for-loop going through all of the data in log_file
    for line in log_file:
        #Adjusts formatting: 
        line = line.rstrip()
        #This returns data for a range of indexes using index 0 - 3
        day = line[0:3]
        #This is a conditional statement executing the code if the day is Tuesday (changed to Monday during assessment)
        if day == "Mon":
            #Show or display the information if condition above is met
            print(line)

#This invokes the function: 
sales_reports(log_file)
