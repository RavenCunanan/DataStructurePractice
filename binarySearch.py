def binary_search(input_list, target):
  # If the list is empty, return False
  if not input_list:
    return False  
 
  mid = len(input_list) // 2 # Finds the middle index of the list
 
  # Write code to check to see if the middle element equals the target 💖
  if input_list[mid] == target:
    return True
  

  # If the target is less than the middle element, search the left half of the list
  if  target < input_list[mid]:
    return binary_search(input_list[:mid], target)

  # Write code to check to see if the target is greater than the middle element 💖
  if target > input_list[mid]:
    return binary_search(input_list[mid+1 :],target) 
  
  
# ------------- TESTING YOUR ALGORITHM -----------------
email_list = [
  'dwight.schrute@dundermifflin.com', 
  'michael.scott@dundermifflin.com',
  'mochi@codedex.io',
  'mgoodyear@lumonindustries.com',
  'walter.white@jpwynnehigh.edu',
  'hank@dea.gov',
  'kimberly.finkle@essexu.edu',
  'sheldon@caltech.edu',
  'elliot@allsafe.com',
  'mr.robot@fsociety.com',
  'mulder@fbi.gov',
  'carrie@sexandthecity.tvs',
  'pleasecallmebarney@yahoo.com',
  'buffy@sunnydale.edu'
]

print(binary_search(email_list, 'mgoodyear@lumonindustries.com'))   # Output: True
print(binary_search(email_list, 'mark.scout@lumonindustries.com'))  # Output: False

# Checking an edge case - what if our input list is empty?

empty_list = []
print(binary_search(empty_list, 'dwight@dundermifflin.com'))        # Output: False
