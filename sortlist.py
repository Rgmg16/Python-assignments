def sort_list():
    # Ask the user to choose between sorting numbers or words
    choice = input("Do you want to sort numbers or words? (Enter 'numbers' or 'words'): ").strip().lower()

    if choice == 'numbers':
        # Create a list of numbers
        input_list = input("Enter numbers separated by spaces: ").split()
        # Convert the input to a list of integers
        input_list = [int(num) for num in input_list]
    elif choice == 'words':
        # Create a list of words
        input_list = input("Enter words separated by spaces: ").split()
    else:
        print("Invalid choice. Please enter 'numbers' or 'words'.")
        return

    # Ask the user for the sorting order
    order = input("Do you want to sort in ascending or descending order? (Enter 'ascending' or 'descending'): ").strip().lower()

    # Sort the list using the sorted function
    if order == 'ascending':
        sorted_list = sorted(input_list)
    elif order == 'descending':
        sorted_list = sorted(input_list, reverse=True)
    else:
        print("Invalid order. Please enter 'ascending' or 'descending'.")
        return

    # Display the sorted list using sorted function
    print("Sorted list using sorted function:", sorted_list)

    # Sort the list in place using the sort method
    if order == 'ascending':
        input_list.sort()
    elif order == 'descending':
        input_list.sort(reverse=True)

    # Display the sorted list using sort method
    print("Sorted list using sort method:", input_list)

# Run the sort_list function
sort_list()
