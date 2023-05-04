Name=input('What is your name? ')
Weight=input('What is your weight? ')
Gender=input('What is your gender? ')
Day=input('What day were you born? ')
Month=input('What month were you born? ')
Year=int(input('What year were you born? '))
Age=2022-Year
#print(Name', your weight is',Weight,', your gender is',Gender,', and you were born on',Month, Day,',', Year,'. Your age is',Age,', right? ')
print(
    '{}, your weight is {}, your gender is {}, and you were born on {} {}, {}. Your age is {}, right? '
    .format(Name,Weight,Gender,Day,Month,Year,Age)
    )

