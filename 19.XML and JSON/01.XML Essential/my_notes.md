-----------------
# 5) XML and XPath

![X_Path.png](X_Path.png)
![X_Path_Example.png](X_Path_Example.png)

## businesscard.xml

### to select name

/BusinessCard/Name

### text of name, using text() function

/BusinessCard/Name/text()

### to select all phones

/BusinessCard/phone

### to select specific phone number 1, using predicate

/Businesscard/phone[1]

### last phone number, using last() function

/BusinessCard/phone[last()]

### check specific words in text using contains() function

/BusinessCard/Name[contains(text(), 'Joe')]

### get all phone numbers with the attributes "type"

/BusinessCard/phone[@type]

### get all phone numbers with the attributes "type" of "work"

/BusinessCard/phone[@type='work']

---

## items.xml

### we want to select photo of Coffee type

/items/item[type='Coffee']/photo
