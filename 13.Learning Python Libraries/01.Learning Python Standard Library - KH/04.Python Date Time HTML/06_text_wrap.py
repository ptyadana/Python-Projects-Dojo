# Text Wrap Module
import textwrap

websiteText = """   Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print(websiteText)

print("\n---------- No Dedent ----------")
print(textwrap.fill(websiteText)) # the output do not maintain the line break of original text


print("\n---------- Dedent ----------")
dedent_text = textwrap.dedent(websiteText).strip() # still maintain the indentation of original text
print(dedent_text)                                 # so that we can do other manipulation like stripping


print("\n---------- Fill ----------")
print(textwrap.fill(dedent_text, width=50)) # column width 50 
print("")
print(textwrap.fill(dedent_text, width=20))


print("\n---------- Controlling Indent ----------")
print(textwrap.fill(dedent_text, initial_indent="    ", subsequent_indent = "        "))


print("\n---------- Shortening Text ----------")
print(textwrap.shorten("Black coffee is all I need.", width=25, placeholder="...")) #shorten the text to 25 chars and followed by ...