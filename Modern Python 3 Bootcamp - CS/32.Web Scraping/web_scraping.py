#Web Scraping with BeautifulSoup
#https://beautiful-soup-4.readthedocs.io/en/latest/

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" class="special">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testing of Web Scraping</title>
</head>
<body>
    <div class="main"><p>This is the welcome message</p></div>
    <h1 data-example="yes">HELLLOOOOO</h1>
    <hr>
    <p>love learning new stuffs</p>
    <div>
        <ul>
            <li>Item A</li>
            <li id="seconditem">Item B</li>
            <li class="special super-power">Item C</li>
            <li>Item D</li>
            <li class="special">Item E</li>
        </ul>
    </div>
    <div>peaceful div</div>
    <div class="zone">I am in zone.</div>
</body>
</html>
"""
soup = BeautifulSoup(html_doc,'html.parser')

print(soup.title.string)
print(soup.div)
print(soup.find_all('li'))
print(soup.find(id='secondId'))
print(soup.find(class_='main'))
print(soup.find_all(attrs={'data-example':'yes'}))

print('----------------')
data = soup.select('#seconditem')
print(data)

print('----------------')
data = soup.select('div')[2]
print(data)

print('----------------')
data = soup.select('.main')
print(data)

print('----------------')
data = soup.select('[data-example]')
print(data)

#--------------------------------------------#
print('----------------')
element = soup.select('li')
for item in element:
    print(item.getText())


print('----------------')
element = soup.select('.zone')
print(element[0].getText())

print('----------------')
element = soup.select('.special')
for item in element:
    print(item.name)
    print(item.attrs)


#--------------------------------------------#
print('------------------')
# element = soup.select('body')
data = soup.body.contents[3]
print(data)

#--------------------------------------------#
print('------------------')
data = soup.body.contents[7].next_sibling.next_sibling
print(data)

#--------------------------------------------#
print('------------------')
data = soup.body.contents[1].find_next_sibling()
print(data)


#--------------------------------------------#
print('------------------')
data = soup.select('.zone')[0].find_previous_sibling()
print(data)


#check help page of doc
help(data)