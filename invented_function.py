# this function is to count the number of people who work in certain occupation in a pie chart
def number_of_people(degree, totalAmount, occupation):
    # totalAmount is the total of people who works in the company
    # one full rotation is 360 degrees
    if degree <= 360: 
        numberOfPeople = (degree/360)*totalAmount
        total = round(numberOfPeople) # round the number so it won't show a decimal
        print("The number of people who work as {}s in the company are {} people.".format(occupation, total))
    else: 
        print("the degree is greater than 360 degrees") # the degree can't exceed 360 degrees in a pie chart

number_of_people(20, 200, "Clerk")
number_of_people(45, 350, "Manager")
number_of_people(90, 124, "Developer")
