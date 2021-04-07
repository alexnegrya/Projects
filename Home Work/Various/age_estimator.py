birth = int(input('Enter the year of your birth: '))

year = 2021
age = year - birth

if birth < 1900:
    print('Error: the minimum allowable year of birth is 1900!'),
elif age <= 3:
    print('Your age is',age,'year(s), you are baby.'),
elif age >= 4 and age <= 9:
    print('Your age is',age,'year(s), you are kid.'),
elif age >= 10 and age <= 15:
    print('Your age is',age,'year(s), you are teen.'),
elif age >= 16 and age <= 18:
    print('Your age is',age,'year(s), you are young.'),
elif age >= 19 and age <= 50:
    print('Your age is',age,'year(s), you are adult.'),
elif age >= 51:
    print('Your age is',age,'year(s), you are old.'),
elif birth > year:
    print('Error: the maximum allowed year is',year,'!'),
else:
    print('An unexpected error occurred!')