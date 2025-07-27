###### 1.
print("****************************************************")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Trier la liste
ages.sort()
print("Ages triés :", ages)

# Afficher l'age le plus bas et le plus haut
print("****************************************************")
min_age = min(ages)
max_age = max(ages)
print("Age le plus bas :", min_age)
print("Age le plus haut :", max_age)

# Ajouter l'age le plus bas et le plus haut à la liste
print("****************************************************")
ages.append(min_age)
ages.append(max_age)
print("Liste après ajout :", ages)

# Calculer la Médiane
print("****************************************************")
ages_sorted = sorted(ages)
n = len(ages_sorted)
print("Liste triée pour la médiane :", ages_sorted)
var1 = ages_sorted[n // 2 - 1 : n // 2 + 1]
var2 = ages_sorted[n // 2]

if n % 2 == 1:
    median = var2
else:
    median = (var1[0] + var1[1]) / 2
print("Médiane :", median)


# Calculer la Moyenne
print("****************************************************")
average = sum(ages_sorted) / n
print("Moyenne :", average)

# Afficher l'interval (range)
print("****************************************************")
range_ages = max_age - min_age
print("Range :", range_ages)

# Comparaison des valeurs
print("****************************************************")
print("Comparaison des valeurs :")
min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print("abs(min - moyenne) :", min_diff)
print("abs(max - moyenne) :", max_diff)

# 2. Liste des pays
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print("****************************************************")
n = len(countries)

if n % 2 == 1:
    print("Pays du milieu :", countries[n // 2])
else:
    print("Pays du milieu :", countries[n // 2 - 1 : n // 2 + 1])

# 2. Diviser la liste en deux parties égales (la première moitié sera plus grande si elle est impair)
print("****************************************************")
milieu = (n + 1) // 2
premiere_partie = countries[:milieu]
deuxieme_partie = countries[milieu:]
print("Première moitié :", premiere_partie)
print("Deuxième moitié :", deuxieme_partie)

# 3. Déballer les trois premiers pays et le reste comme pays scandinaves

print("****************************************************")
liste_exemple = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandinaves = liste_exemple
print("China :", china)
print("Russia :", russia)
print("USA :", usa)
print("Pays scandinaves :", scandinaves)