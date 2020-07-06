# Question: Please download the attached urls.txt file. 
# The file contains some broken URLs. Here's what the file contains:

# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com
# Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

# Expected output: 

# http://www.google.com
# http://www.yahoo.com
# http://www.stackoverflow.com
# http://www.pythonhow.com

with open('94_file/94_urls.txt', 'r') as file:
    data = file.read().splitlines();

corrected_url = [];

for url in data:
    url = url.replace('https:/', 'http://');
    print(url);
    corrected_url.append(url);

with open('94_file/corrected_urls.txt', 'w') as file:
    for url in corrected_url:
        file.write(url + '\n');