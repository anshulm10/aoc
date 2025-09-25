def dist_problem():
    with open("input.txt", "r") as f:
        data = f.read().strip().split('\n')
        
    l_list = [] # list to store lengths of each string
    r_list = []
    for line in data:
        numbers = line.split() # split each line into numbers
        l_list.append(int(numbers[0])) # append the first number to l_list
        r_list.append(int(numbers[1])) # append the second number to r_list
        
    l_list.sort() # sort the lengths
    r_list.sort() 
    
    total_distance = 0 # variable to store final answer(total distance)
    
    for i in range(len(l_list)): # iterate through the lengths (one list taken as they are of same length)
        #getting the number at i from both lists
        
        l_num = l_list[i]
        r_num = r_list[i]
        
        distance = abs(l_num - r_num) # calculate the distance
        total_distance += distance # add the distance to total_distance
        
        print(f"Pair {i+1}: ({l_num}, {r_num}) -> Distance: {distance}")  # Print each pair and their distance
        
    return total_distance  # Return the sum of all distances

if __name__ == "__main__":
        result = dist_problem()  # Call the function and store the result
        print(f"Total Distance: {result}")  # Print the total distance