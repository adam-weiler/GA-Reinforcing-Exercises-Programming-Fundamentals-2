def add_odds_in_list(num_list): #Takes a list of numbers and returns the sum of the odd numbers.
    our_sum = 0
    
    for num in range(len(num_list)): #Iterates through length of list.
        if (num % 2 != 0): #If current iteration is not even.
            # print(num_list[num])
            our_sum += num_list[num]

    return our_sum


print(add_odds_in_list([1, 0, 1])) #0
print(add_odds_in_list([0, 1, 0])) #1
print(add_odds_in_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) #25
print(add_odds_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #30