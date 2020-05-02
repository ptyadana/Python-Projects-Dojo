#Add missing items into file

checklist = ["Portugal", "Germany", "Spain"]

with open('raw/countries_missing.txt', mode='rt') as file:
    countries = file.readlines()

countries = [c.strip('\n') for c in countries]

sorted_countries = sorted(countries + checklist)

with open('processed/countries_sorted.txt', mode='wt') as file:
    for c in sorted_countries:
        file.writelines(c+'\n')