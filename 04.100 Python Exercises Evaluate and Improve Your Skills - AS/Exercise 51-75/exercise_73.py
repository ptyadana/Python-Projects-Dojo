#Multiply the values of the text file in the URL by two and export the result to a new file
# Hint: The easiest way to do this is with pandas.

# Exercise for reference: http://www.pythonhow.com/data/sampledata.txt
# Create a script that reads this file, multiplies its values by two and saves the output in a new text file.

import pandas as pd

df = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
df2= df*2

df2.to_csv('./output/output_73.csv', index=None)

print(df)
print(df2)


# Explanation:
# As you can see this can be done with pandas  in four lines of code. We use read_csv  to create a pandas dataframe object which is like a table with data. Then we multiply this table by two and then export the calculated data to a text file in our local directory.