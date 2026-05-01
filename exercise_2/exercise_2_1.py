#exercise_2_1.py
#Author: Karoline Trindade Dutra
#Date: 2026-04-28
#Description: Exercise 2.1 - Three basic Python functions 
#             for the Python in Qgis and ArcGis Course

#1st function:
#Function to count the number of donuts if they are less than 10.
#If they are more than 10 it should return "many". 
# If by mistake a word is used in the function, it will return an error explaining the reason.
def donuts(count):
    if type(count) != int:
        message = "Error: Count must be an integer."
    elif count < 10:
        message = "Number of donuts: " + str(count)
    else:
        message = "Number of donuts: many"
    return message

#to test the result
print(donuts(5))
print(donuts(25))
print(donuts("ten"))

#2nd function:
#Function to add specific ending in words.
#If the word has 3 or more characteres, the function will add "ing".
#If the word already finishes with "ing", thus the function will add "ly".
#If the word is small, less than 3 characteres, no changes will be performed.
#If by mistake a number is used in the function, it will present an error explaing to use string.
def verbing(s):
    if type(s) != str:
        message = "Error: Input must be a string."
    elif len(s) >= 3:
        if s.endswith("ing"):
            message = s + "ly"
        else:
            message = s + "ing"
    else:
        message = s
    return message

#to test the result:
print(verbing("test"))
print(verbing("testing"))
print(verbing("go"))
print(verbing(14))


#3rd function:
#Function to remove the adjacent repeated number in a list.
#It should be used in the function only list, and non-empty list.
#It is not allowed to use words.
#The function shows an error message if these 3 last cases occur.
def remove_adjacent(nums):
    if not isinstance(nums, list):
       return "Error: Nums should be a list of numbers."

    if len(nums) == 0:
        return "Error: Nums is empty. It should contains a list of numbers." 
        
    for item in nums:
        if not isinstance(item, (int, float)):
            return "Error: Nums must contain only numbers."
        
        return list(dict.fromkeys(nums))

#To test the result
list1 = [1, 2, 2, 3]
list2 = [100, 104.5, 104.5, 220, 230, 230]
list3 = ["a", 100, 1, "b"]
list4 = ["abc", "def", "ghi"]

print(remove_adjacent(list1))
print(remove_adjacent(list2))
print(remove_adjacent(list3))
print(remove_adjacent(list4))



#function to test the whole excercise:

def main():
    print('donuts')
    print(donuts(4))
    print(donuts(9))
    print(donuts(10))
    print(donuts('twentyone'))
    print('verbing')
    print(verbing('hail'))
    print(verbing('swiming'))
    print(verbing('do'))
    print('remove_adjacent')
    print(remove_adjacent([1, 2, 2, 3]))
    print(remove_adjacent([2, 2, 3, 3, 3]))
    print(remove_adjacent([]))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()