def grade(marks):
    if 90<=marks<=100:
        print("Congratulations! You've scored an A grade!")
    elif 80<=marks<=89:
        print("Good job!You've scored a B grade!")
    elif 60<=marks<=79:
        print("Fair attempt, you've scored a C grade")        
    elif 40<=marks<=59:
        print("Do better, you've scored a D.")
    else:
        print("Work harder, you've scored an E")    

grade(75)          