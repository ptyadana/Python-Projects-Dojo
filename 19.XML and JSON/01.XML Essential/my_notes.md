# 2) XML Overview

## XML Types

![XMLtypes.png](img/XMLtypes.png)

## XML Namespaces

We can define custom XML namespace, which needs to be unique name and with customized structure.
![](img/XML_namespace1.png)
![](img/XML_namespace2.png)
![](img/XML_namespace3.png)

---

# 3) Working with XML

## Associat css style with XML

- We can associate css style for the XML elements like below.

  `<?xml-stylesheet type="text/css" href="businesscard.css" ?>`

- Nodes can be applied with custom css styling using the XML tag name directly like below.

  `Name {`
  ` color: blueviolet;`
  `}`

## Advanced Styling with CSS

- we can use custom attribute type and associate it with css to display custom styling.

  `<phone type="mobile" primary="super-important">(415) 555-4567</phone>`

  can be associated with css styling of

  `phone[primary]::after {`
  ` content: " (" attr(primary) ")";`
  `}`

  this will result to displayed in

  **(65)123 - 456 (super important)**

---

# 4) Manipulating XML with DOM

![](img/DOM1.png)
![](img/DOM2.png)
![](img/DOM3.png)
![](img/DOM4.png)
![](img/DOM5.png)

---

# 5) XML and XPath

## XPath important concepts

![X_Path0.png](img/X_Path0.png)

## Using XPath for selecting information

![X_Path.png](img/X_Path.png)
![X_Path_Example.png](img/X_Path_Example.png)

## businesscard.xml

### to select name

`/BusinessCard/Name`

### text of name, using text() function

`/BusinessCard/Name/text()`

### to select all phones

`/BusinessCard/phone`

### to select specific phone number 1, using predicate

Take note that in xpath, referencing list index **start from 1**, not like 0 from other langagues

`/Businesscard/phone[1]`

### last phone number, using last() function

`/BusinessCard/phone[last()]`

### check specific words in text using contains() function

`/BusinessCard/Name[contains(text(), 'Richard')]`

### get all phone numbers with the attributes "type"

`/BusinessCard/phone[@type]`
(or)
`//phone[@type]`

### get all phone numbers with the attributes "type" of "work"

`/BusinessCard/phone[@type='work']`
(or)
`//phone[@type='work']`

## items.xml

### we want to select photo of Coffee type

`/items/item[type='Coffee']/photo`

---

# 6) XML and XSLT

## What is XSLT?

- eXtensible Stylesheet Language Transformations
- Different than CSS - applies templates to XML data
- Written using XML syntax itself
- can transorm XML into almost anything
- can perform operations directly on the data.
- more at https://wwww.w3.org/TR/xslt

![](img/XSLT1.png)
![](img/XSLT2.png)
In below example, we are getting source element(SimpleTag) and replace with whatever we define in this XSLT template (in this case some html).
![](img/XSLT3.png)

---

# 7) XSLT Examples

If there is an issue of Cross-Origin Request Blocked on firefox testing, [temporarily disable the setting](http://testingfreak.com/how-to-fix-cross-origin-request-security-cors-error-in-firefox-chrome-and-ie/) during testing.

---

# 8) Document Type Definition

- Provide way to contstrain XML document content
- Specify what kind of content can appear and where
- Can be included in XML file, or be external to document
- Relatively simple to write, but not powerful

### DTD Syntax and Content

![img/DTD1.png](img/DTD1.png)
![img/DTD2.png](img/DTD2.png)

### DTD Format

![img/DTD3.png](img/DTD3.png)

### 8.1) Declaring Elements in DTD

![img/DTD4.png](img/DTD4.png)

Example :
![img/DTD5.png](img/DTD5.png)
![img/DTD6.png](img/DTD6.png)

### 8.2) Declaring Attributes in DTD

![img/DTD7.png](img/DTD7.png)
![img/DTD8.png](img/DTD8.png)
![img/DTD9.png](img/DTD9.png)

Example: Below basically declare the rules that BusinessCard element needs to follow.

- There should be Name.
- followed by 1 or more phone.
- followed by optional email.

  `<!ELEMENT BusinessCard (Name, phone+, email?)`

  Example2: This means phone number is characters

- Additonally phone has attribute **type** with 4 values which are required.

  `<!ELEMENT phone (#PCDATA)>`

  `<!ATTLIST phone type (mobile | work | fax | home) #REQUIRED>`

## Validation XML definition

- https://www.xmlvalidation.com/

---

# 9) XML Schema

- Alternative way of specifying rules to DTDs
- Provide way to constrain XML document content
- Written in XML syntax
- Similar to DTDs, but more powerful and robust
  - Finar level of control than DTDs allow
  - Schema and XML files are always stored separately

## XML Anatomy

![XML1.png](img/XML1.png)

## 9.1) Declaring Elements in Schema

![XML2.png](img/XML2.png)

## 9.1.1) Simple Schema Type

![XML3.png](img/XML3.png)
![XML4.png](img/XML4.png)
![XML5.png](img/XML5.png)
![XML6.png](img/XML6.png)
![XML7.png](img/XML7.png)

## 9.1.2) Complex Schema Type

![XML8.png](img/XML8.png)
![XML9.png](img/XML9.png)
![XML10.png](img/XML10.png)
![XML11.png](img/XML11.png)
![XML12.png](img/XML12.png)

## 9.2) Declaring Attributes in XML Schema

![XML13.png](img/XML13.png)
![XML14.png](img/XML14.png)
![XML15.png](img/XML15.png)
![XML16.png](img/XML16.png)

## Testing using https://www.xmlvalidation.com/

- go to https://www.xmlvalidation.com/
- upload XML file
- tick `Validate against external XML schema` checkbox and click Validate.
- upload XSD file and validate it.
