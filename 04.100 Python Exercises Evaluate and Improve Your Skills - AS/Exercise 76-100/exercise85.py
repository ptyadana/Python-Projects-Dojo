# Question: Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 
# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or break lines in it. The new file content should look like in the expected output.

# Expected output: 

# Afghanistan
# Albania
# Algeria
# Andorra
# Angola
# Antigua and Barbuda
# Argentina
# Armenia
# Aruba
# Australia
# Austria
# Azerbaijan
# Bahamas, The
# Bahrain
# Bangladesh
# Barbados
# Belarus
# Belgium
# Belize
# Benin
# Bhutan
# Bolivia
# Bosnia and Herzegovina
# Botswana
# Brazil
# Brunei
# Bulgaria
# Burkina Faso
# Burma
# Burundi
# Cambodia
# Cameroon
# Canada
# Cabo Verde
# Central African Republic
# Chad
# Chile
# China
# Colombia
# Comoros
# Congo, Democratic Republic of the
# Congo, Republic of the
# Costa Rica
# Cote d'Ivoire
# Croatia
# Cuba
# Curacao
# Cyprus
# Czechia
# Denmark
# Djibouti
# Dominica
# Dominican Republic
# East Timor (see Timor-Leste)
# Ecuador
# Egypt
# El Salvador
# Equatorial Guinea
# Eritrea
# Estonia
# Ethiopia
# Fiji
# Finland
# France
# Gabon
# Gambia, The
# Georgia
# Germany
# Ghana
# Greece
# Grenada
# Guatemala
# Guinea
# Guinea-Bissau
# Guyana
# Haiti
# Holy See
# Honduras
# Hong Kong
# Hungary
# Iceland
# India
# Indonesia
# Iran
# Iraq
# Ireland
# Israel
# Italy
# Jamaica
# Japan
# Jordan
# Kazakhstan
# Kenya
# Kiribati
# Korea, North
# Korea, South
# Kosovo
# Kuwait
# Kyrgyzstan
# Laos
# Latvia
# Lebanon
# Lesotho
# Liberia
# Libya
# Liechtenstein
# Lithuania
# Luxembourg
# Macau
# Macedonia
# Madagascar
# Malawi
# Malaysia
# Maldives
# Mali
# Malta
# Marshall Islands
# Mauritania
# Mauritius
# Mexico
# Micronesia
# Moldova
# Monaco
# Mongolia
# Montenegro
# Morocco
# Mozambique
# Namibia
# Nauru
# Nepal
# Netherlands
# New Zealand
# Nicaragua
# Niger
# Nigeria
# North Korea
# Norway
# Oman
# Pakistan
# Palau
# Palestinian Territories
# Panama
# Papua New Guinea
# Paraguay
# Peru
# Philippines
# Poland
# Portugal
# Qatar
# Romania
# Russia
# Rwanda
# Saint Kitts and Nevis
# Saint Lucia
# Saint Vincent and the Grenadines
# Samoa
# San Marino
# Sao Tome and Principe
# Saudi Arabia
# Senegal
# Serbia
# Seychelles
# Sierra Leone
# Singapore
# Sint Maarten
# Slovakia
# Slovenia
# Solomon Islands
# Somalia
# South Africa
# South Korea
# South Sudan
# Spain
# Sri Lanka
# Sudan
# Suriname
# Swaziland
# Sweden
# Switzerland
# Syria
# Taiwan
# Tajikistan
# Tanzania
# Thailand
# Timor-Leste
# Togo
# Tonga
# Trinidad and Tobago
# Tunisia
# Turkey
# Turkmenistan
# Tuvalu
# Uganda
# Ukraine
# United Arab Emirates
# United Kingdom
# Uruguay
# Uzbekistan
# Vanuatu
# Venezuela
# Vietnam
# Yemen
# Zambia
# Zimbabwe

# Answer 1:
with open('raw/countries_raw.txt', mode='rt') as file:
    countries = file.readlines()

cleaned_countries = []
for country in countries:
    country = country.strip('\n')
    if len(country) > 1:
        if country != 'Top of Page':
            cleaned_countries.append(country)

with open('processed/countries_clean.txt', mode='wt') as file:
    for country in cleaned_countries:
        file.write(country+'\n')

# Answer 2: for processing part using List Comprehension
# content = [i.strip('\n') for i in countries if '\n' in i]
# content = [i for i in content if i!='']
# content = [i for i in content if i!='Top of Page']
# content = [i for i in content if len(i) != 1]
