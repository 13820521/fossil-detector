name=input("What'S your name?")
age=input("How old are you?")
age=int(age)
years_left=(100-age)
if years_left>20:
    years_left=str(years_left)
    print(name+", if you survive th next "+years_left+" years, you'll hit 100!")
elif (80<age<99):
    print(name+", you're on the edge of fossilhood... be careful!")
else:    
    print(name+", you're officially fossil!")

