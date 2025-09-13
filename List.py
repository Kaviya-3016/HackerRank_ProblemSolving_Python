if __name__ == '__main__':
    N = int(input())   # Take integer input from the user
    
    list = []   # Create an empty list (⚠️ better to avoid using 'list' as a variable name
                # since it overwrites Python's built-in 'list' type)
    
    # Case 1: If N is less than 15
    if N < 15:
        # Insert values into the list
        list.insert(0, 5)   # list = [5]
        list.insert(1, 10)  # list = [5, 10]
        list.insert(0, 6)   # list = [6, 5, 10]
        print(list)         # prints: [6, 5, 10]
        
        list.remove(6)      # remove first occurrence of 6 → list = [5, 10]
        list.append(9)      # add 9 at the end → list = [5, 10, 9]
        list.append(1)      # add 1 at the end → list = [5, 10, 9, 1]
        list.sort()         # sort in ascending → list = [1, 5, 9, 10]
        print(list)         # prints: [1, 5, 9, 10]
        
        list.pop()          # remove last element (10) → list = [1, 5, 9]
        list.reverse()      # reverse → list = [9, 5, 1]
        print(list)         # prints: [9, 5, 1]
    
    # Case 2: If N is 15 or more
    else:
        # Append values to the list
        list.append(1)
        list.append(6)
        list.append(10)
        list.append(8)
        list.append(9)
        list.append(2)
        list.append(12)
        list.append(7)
        list.append(3)
        list.append(5)
        
        # Now list = [1, 6, 10, 8, 9, 2, 12, 7, 3, 5]
        
        # Insert values at specific positions
        list.insert(8, 66)   # insert 66 at index 8
        list.insert(1, 30)   # insert 30 at index 1
        list.insert(6, 75)   # insert 75 at index 6
        list.insert(4, 44)   # insert 44 at index 4
        list.insert(9, 67)   # insert 67 at index 9
        list.insert(2, 44)   # insert 44 at index 2
        list.insert(9, 21)   # insert 21 at index 9
        list.insert(8, 87)   # insert 87 at index 8
        list.insert(1, 75)   # insert 75 at index 1
        list.insert(1, 48)   # insert 48 at index 1
        
        print(list)          # print list after all insertions
        
        list.reverse()       # reverse the entire list
        print(list)
        
        list.sort()          # sort the list in ascending order
        print(list)
        
        list.append(2)       # add 2 at the end
        list.append(5)       # add 5 at the end
        list.remove(2)       # remove the FIRST 2 found in the list
        print(list)          # print the final list
