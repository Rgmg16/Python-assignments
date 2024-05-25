def chop(lst):
    
    if len(lst) > 1:
        del lst[0]  # Remove the first element
        del lst[-1]  # Remove the last element
    elif len(lst) == 1:
        del lst[0]  # If there's only one element, remove it
    # If the list is empty, do nothing
    return None

def middle(lst):
  
    return lst[1:-1] if len(lst) > 1 else []

# Test the functions
original_list = [1, 2, 3, 4, 5]

# Testing the chop function
chop_list = original_list.copy()
print(f"Original list before chop: {chop_list}")
chop(chop_list)
print(f"List after chop: {chop_list}")

# Testing the middle function
middle_list = original_list.copy()
print(f"Original list: {middle_list}")
new_list = middle(middle_list)
print(f"New list after middle: {new_list}")
