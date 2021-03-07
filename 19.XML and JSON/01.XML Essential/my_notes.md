-----------------
# 3) Working with XML

## Associat css style with XML
- We can associate css style for the XML elements like below.

`<?xml-stylesheet type="text/css" href="businesscard.css" ?>`

- Nodes can be applied with custom css styling using the XML tag name directly like below.
`Name {`
`  color: blueviolet;`
`}`

## Advanced Styling with CSS

- we can use custom attribute type and associate it with css to display custom styling.
`<phone type="mobile" primary="super-important">(415) 555-4567</phone>` can be associated with css styling of 
`phone[primary]::after {`
`  content: " (" attr(primary) ")";`
`}` 
this will result to displayed in
`(65)123 - 456 (super important)`


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
