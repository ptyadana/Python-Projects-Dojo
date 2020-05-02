# Question: Please take a look at the following list:
# checklist = ["Portugal", "Germany", "Munster", "Spain"]
# One of the items is not a country. Please use Python and the file containing 
# the list of countries (attached) as data source to filter out the checklist  of non-country items. 
# Once you have filtered out checklist , then print it out.

# Expected output: 
# ['Germany', 'Portugal', 'Spain']

# Answer - Country Checker:
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open('processed/countries_clean.txt', mode='rt') as file:
    countries = file.readlines()

countries =[c.strip('\n') for c in countries]
checked_countries = [c for c in countries if c in checklist]

print(checked_countries)

# Explanation:
# We're opening our file data source and loading it in Python as a list in content. Then we clean out that list of break lines in line 6. Then, in line 7 we check if the items of content  are in checklist , and if they are we leave them in the list, otherwise, we remove them. So, we end up with only the three matches.