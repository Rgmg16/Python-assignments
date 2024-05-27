# Exercise 1: Write a program that takes a sentence and then prints the number of words in that sentence.

def count_words(sentence):
    
    words = sentence.split()
    
    return len(words)


sentence = input("Enter a sentence: ")

num_words = count_words(sentence)

print(f"The number of words in the sentence is: {num_words}")

# Exercise 2: Write a program that opens an existing text file, reads its contents, and creates a new file with a different name, writing the copied content to the new file.

def copy_file(source_file, destination_file):
    try:
        
        with open(source_file, 'r') as src:
            
            content = src.read()
                
        with open(destination_file, 'w') as dest:
            
            dest.write(content)
        
        print(f"Content copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except IOError as e:
        print(f"An error occurred while copying the file: {e}")


source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")


copy_file(source_file, destination_file)

# Exercise 3: Write a program that opens a text file and iterates through each line using a for loop, printing each line separately.

with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
