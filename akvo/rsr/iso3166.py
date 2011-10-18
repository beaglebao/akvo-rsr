#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ISO 3166 country names and their corresponding 3166-1-alpha-2 codes
"""
from django.utils.translation import ugettext as _

ISO_3166_COUNTRIES = (
    (u"af", _(u"Afghanistan")),
    (u"ax", _(u"Åland Islands")),
    (u"al", _(u"Albania")),
    (u"dz", _(u"Algeria")),
    (u"as", _(u"American Samoa")),
    (u"ad", _(u"Andorra")),
    (u"ao", _(u"Angola")),
    (u"ai", _(u"Anguilla")),
    (u"aq", _(u"Antarctica")),
    (u"ag", _(u"Antigua and Barbuda")),
    (u"ar", _(u"Argentina")),
    (u"am", _(u"Armenia")),
    (u"aw", _(u"Aruba")),
    (u"au", _(u"Australia")),
    (u"at", _(u"Austria")),
    (u"az", _(u"Azerbaijan")),
    (u"bs", _(u"Bahamas")),
    (u"bh", _(u"Bahrain")),
    (u"bd", _(u"Bangladesh")),
    (u"bb", _(u"Barbados")),
    (u"by", _(u"Belarus")),
    (u"be", _(u"Belgium")),
    (u"bz", _(u"Belize")),
    (u"bj", _(u"Benin")),
    (u"bm", _(u"Bermuda")),
    (u"bt", _(u"Bhutan")),
    (u"bo", _(u"Bolivia, Plurinational State of")),
    (u"bq", _(u"Bonaire, Sint Eustatius and Saba")),
    (u"ba", _(u"Bosnia and Herzegovina")),
    (u"bw", _(u"Botswana")),
    (u"bv", _(u"Bouvet Island")),
    (u"br", _(u"Brazil")),
    (u"io", _(u"British Indian Ocean Territory")),
    (u"bn", _(u"Brunei Darussalam")),
    (u"bg", _(u"Bulgaria")),
    (u"bf", _(u"Burkina Faso")),
    (u"bi", _(u"Burundi")),
    (u"kh", _(u"Cambodia")),
    (u"cm", _(u"Cameroon")),
    (u"ca", _(u"Canada")),
    (u"cv", _(u"Cape Verde")),
    (u"ky", _(u"Cayman Islands")),
    (u"cf", _(u"Central African Republic")),
    (u"td", _(u"Chad")),
    (u"cl", _(u"Chile")),
    (u"cn", _(u"China")),
    (u"cx", _(u"Christmas Island")),
    (u"cc", _(u"Cocos (keeling) Islands")),
    (u"co", _(u"Colombia")),
    (u"km", _(u"Comoros")),
    (u"cg", _(u"Congo")),
    (u"cd", _(u"Congo, The Democratic Republic of the")),
    (u"ck", _(u"Cook Islands")),
    (u"cr", _(u"Costa Rica")),
    (u"ci", _(u"Côte D'ivoire")),
    (u"hr", _(u"Croatia")),
    (u"cu", _(u"Cuba")),
    (u"cw", _(u"Curaçao")),
    (u"cy", _(u"Cyprus")),
    (u"cz", _(u"Czech Republic")),
    (u"dk", _(u"Denmark")),
    (u"dj", _(u"Djibouti")),
    (u"dm", _(u"Dominica")),
    (u"do", _(u"Dominican Republic")),
    (u"ec", _(u"Ecuador")),
    (u"eg", _(u"Egypt")),
    (u"sv", _(u"El Salvador")),
    (u"gq", _(u"Equatorial Guinea")),
    (u"er", _(u"Eritrea")),
    (u"ee", _(u"Estonia")),
    (u"et", _(u"Ethiopia")),
    (u"fk", _(u"Falkland Islands (Malvinas)")),
    (u"fo", _(u"Faroe Islands")),
    (u"fj", _(u"Fiji")),
    (u"fi", _(u"Finland")),
    (u"fr", _(u"France")),
    (u"gf", _(u"French Guiana")),
    (u"pf", _(u"French Polynesia")),
    (u"tf", _(u"French Southern Territories")),
    (u"ga", _(u"Gabon")),
    (u"gm", _(u"Gambia")),
    (u"ge", _(u"Georgia")),
    (u"de", _(u"Germany")),
    (u"gh", _(u"Ghana")),
    (u"gi", _(u"Gibraltar")),
    (u"gr", _(u"Greece")),
    (u"gl", _(u"Greenland")),
    (u"gd", _(u"Grenada")),
    (u"gp", _(u"Guadeloupe")),
    (u"gu", _(u"Guam")),
    (u"gt", _(u"Guatemala")),
    (u"gg", _(u"Guernsey")),
    (u"gn", _(u"Guinea")),
    (u"gw", _(u"Guinea-bissau")),
    (u"gy", _(u"Guyana")),
    (u"ht", _(u"Haiti")),
    (u"hm", _(u"Heard Island and Mcdonald Islands")),
    (u"va", _(u"Holy See (Vatican City State)")),
    (u"hn", _(u"Honduras")),
    (u"hk", _(u"Hong Kong")),
    (u"hu", _(u"Hungary")),
    (u"is", _(u"Iceland")),
    (u"in", _(u"India")),
    (u"id", _(u"Indonesia")),
    (u"ir", _(u"Iran, Islamic Republic of")),
    (u"iq", _(u"Iraq")),
    (u"ie", _(u"Ireland")),
    (u"im", _(u"Isle of Man")),
    (u"il", _(u"Israel")),
    (u"it", _(u"Italy")),
    (u"jm", _(u"Jamaica")),
    (u"jp", _(u"Japan")),
    (u"je", _(u"Jersey")),
    (u"jo", _(u"Jordan")),
    (u"kz", _(u"Kazakhstan")),
    (u"ke", _(u"Kenya")),
    (u"ki", _(u"Kiribati")),
    (u"kp", _(u"Korea, Democratic People's Republic of")),
    (u"kr", _(u"Korea, Republic of")),
    (u"kw", _(u"Kuwait")),
    (u"kg", _(u"Kyrgyzstan")),
    (u"la", _(u"Lao People's Democratic Republic")),
    (u"lv", _(u"Latvia")),
    (u"lb", _(u"Lebanon")),
    (u"ls", _(u"Lesotho")),
    (u"lr", _(u"Liberia")),
    (u"ly", _(u"Libyan Arab Jamahiriya")),
    (u"li", _(u"Liechtenstein")),
    (u"lt", _(u"Lithuania")),
    (u"lu", _(u"Luxembourg")),
    (u"mo", _(u"Macao")),
    (u"mk", _(u"Macedonia, The Former Yugoslav Republic of")),
    (u"mg", _(u"Madagascar")),
    (u"mw", _(u"Malawi")),
    (u"my", _(u"Malaysia")),
    (u"mv", _(u"Maldives")),
    (u"ml", _(u"Mali")),
    (u"mt", _(u"Malta")),
    (u"mh", _(u"Marshall Islands")),
    (u"mq", _(u"Martinique")),
    (u"mr", _(u"Mauritania")),
    (u"mu", _(u"Mauritius")),
    (u"yt", _(u"Mayotte")),
    (u"mx", _(u"Mexico")),
    (u"fm", _(u"Micronesia, Federated States of")),
    (u"md", _(u"Moldova, Republic of")),
    (u"mc", _(u"Monaco")),
    (u"mn", _(u"Mongolia")),
    (u"me", _(u"Montenegro")),
    (u"ms", _(u"Montserrat")),
    (u"ma", _(u"Morocco")),
    (u"mz", _(u"Mozambique")),
    (u"mm", _(u"Myanmar")),
    (u"na", _(u"Namibia")),
    (u"nr", _(u"Nauru")),
    (u"np", _(u"Nepal")),
    (u"nl", _(u"Netherlands")),
    (u"nc", _(u"New Caledonia")),
    (u"nz", _(u"New Zealand")),
    (u"ni", _(u"Nicaragua")),
    (u"ne", _(u"Niger")),
    (u"ng", _(u"Nigeria")),
    (u"nu", _(u"Niue")),
    (u"nf", _(u"Norfolk Island")),
    (u"mp", _(u"Northern Mariana Islands")),
    (u"no", _(u"Norway")),
    (u"om", _(u"Oman")),
    (u"pk", _(u"Pakistan")),
    (u"pw", _(u"Palau")),
    (u"ps", _(u"Palestinian Territory, Occupied")),
    (u"pa", _(u"Panama")),
    (u"pg", _(u"Papua New Guinea")),
    (u"py", _(u"Paraguay")),
    (u"pe", _(u"Peru")),
    (u"ph", _(u"Philippines")),
    (u"pn", _(u"Pitcairn")),
    (u"pl", _(u"Poland")),
    (u"pt", _(u"Portugal")),
    (u"pr", _(u"Puerto Rico")),
    (u"qa", _(u"Qatar")),
    (u"re", _(u"Réunion")),
    (u"ro", _(u"Romania")),
    (u"ru", _(u"Russian Federation")),
    (u"rw", _(u"Rwanda")),
    (u"bl", _(u"Saint Barthélemy")),
    (u"sh", _(u"Saint Helena, Ascension and Tristan Da Cunha")),
    (u"kn", _(u"Saint Kitts and Nevis")),
    (u"lc", _(u"Saint Lucia")),
    (u"mf", _(u"Saint Martin (French part)")),
    (u"pm", _(u"Saint Pierre and Miquelon")),
    (u"vc", _(u"Saint Vincent and the Grenadines")),
    (u"ws", _(u"Samoa")),
    (u"sm", _(u"San Marino")),
    (u"st", _(u"Sao Tome and Principe")),
    (u"sa", _(u"Saudi Arabia")),
    (u"sn", _(u"Senegal")),
    (u"rs", _(u"Serbia")),
    (u"sc", _(u"Seychelles")),
    (u"sl", _(u"Sierra Leone")),
    (u"sg", _(u"Singapore")),
    (u"sx", _(u"Sint Maarten (Dutch part)")),
    (u"sk", _(u"Slovakia")),
    (u"si", _(u"Slovenia")),
    (u"sb", _(u"Solomon Islands")),
    (u"so", _(u"Somalia")),
    (u"za", _(u"South Africa")),
    (u"gs", _(u"South Georgia and the South Sandwich Islands")),
    (u"ss", _(u"South Sudan")),
    (u"es", _(u"Spain")),
    (u"lk", _(u"Sri Lanka")),
    (u"sd", _(u"Sudan")),
    (u"sr", _(u"Suriname")),
    (u"sj", _(u"Svalbard and Jan Mayen")),
    (u"sz", _(u"Swaziland")),
    (u"se", _(u"Sweden")),
    (u"ch", _(u"Switzerland")),
    (u"sy", _(u"Syrian Arab Republic")),
    (u"tw", _(u"Taiwan, Province of China")),
    (u"tj", _(u"Tajikistan")),
    (u"tz", _(u"Tanzania, United Republic of")),
    (u"th", _(u"Thailand")),
    (u"tl", _(u"Timor-leste")),
    (u"tg", _(u"Togo")),
    (u"tk", _(u"Tokelau")),
    (u"to", _(u"Tonga")),
    (u"tt", _(u"Trinidad and Tobago")),
    (u"tn", _(u"Tunisia")),
    (u"tr", _(u"Turkey")),
    (u"tm", _(u"Turkmenistan")),
    (u"tc", _(u"Turks and Caicos Islands")),
    (u"tv", _(u"Tuvalu")),
    (u"ug", _(u"Uganda")),
    (u"ua", _(u"Ukraine")),
    (u"ae", _(u"United Arab Emirates")),
    (u"gb", _(u"United Kingdom")),
    (u"us", _(u"United States")),
    (u"um", _(u"United States Minor Outlying Islands")),
    (u"uy", _(u"Uruguay")),
    (u"uz", _(u"Uzbekistan")),
    (u"vu", _(u"Vanuatu")),
    (u"ve", _(u"Venezuela, Bolivarian Republic of")),
    (u"vn", _(u"Viet Nam")),
    (u"vg", _(u"Virgin Islands, British")),
    (u"vi", _(u"Virgin Islands, U.S.")),
    (u"wf", _(u"Wallis and Futuna")),
    (u"eh", _(u"Western Sahara")),
    (u"ye", _(u"Yemen")),
    (u"zm", _(u"Zambia")),
    (u"zw", _(u"Zimbabwe")),
)

COUNTRY_CONTINENTS = {
    u'ad': u'eu',
    u'ae': u'as',
    u'af': u'as',
    u'ag': u'na',
    u'ai': u'na',
    u'al': u'eu',
    u'am': u'as',
    u'an': u'na',
    u'ao': u'af',
    u'ap': u'as',
    u'aq': u'an',
    u'ar': u'sa',
    u'as': u'oc',
    u'at': u'eu',
    u'au': u'oc',
    u'aw': u'na',
    u'ax': u'eu',
    u'az': u'as',
    u'ba': u'eu',
    u'bb': u'na',
    u'bd': u'as',
    u'be': u'eu',
    u'bf': u'af',
    u'bg': u'eu',
    u'bh': u'as',
    u'bi': u'af',
    u'bj': u'af',
    u'bl': u'na',
    u'bm': u'na',
    u'bn': u'as',
    u'bo': u'sa',
    u'br': u'sa',
    u'bs': u'na',
    u'bt': u'as',
    u'bv': u'an',
    u'bw': u'af',
    u'by': u'eu',
    u'bz': u'na',
    u'ca': u'na',
    u'cc': u'as',
    u'cd': u'af',
    u'cf': u'af',
    u'cg': u'af',
    u'ch': u'eu',
    u'ci': u'af',
    u'ck': u'oc',
    u'cl': u'sa',
    u'cm': u'af',
    u'cn': u'as',
    u'co': u'sa',
    u'cr': u'na',
    u'cu': u'na',
    u'cv': u'af',
    u'cx': u'as',
    u'cy': u'as',
    u'cz': u'eu',
    u'de': u'eu',
    u'dj': u'af',
    u'dk': u'eu',
    u'dm': u'na',
    u'do': u'na',
    u'dz': u'af',
    u'ec': u'sa',
    u'ee': u'eu',
    u'eg': u'af',
    u'eh': u'af',
    u'er': u'af',
    u'es': u'eu',
    u'et': u'af',
    u'eu': u'eu',
    u'fi': u'eu',
    u'fj': u'oc',
    u'fk': u'sa',
    u'fm': u'oc',
    u'fo': u'eu',
    u'fr': u'eu',
    u'fx': u'eu',
    u'ga': u'af',
    u'gb': u'eu',
    u'gd': u'na',
    u'ge': u'as',
    u'gf': u'sa',
    u'gg': u'eu',
    u'gh': u'af',
    u'gi': u'eu',
    u'gl': u'na',
    u'gm': u'af',
    u'gn': u'af',
    u'gp': u'na',
    u'gq': u'af',
    u'gr': u'eu',
    u'gs': u'an',
    u'gt': u'na',
    u'gu': u'oc',
    u'gw': u'af',
    u'gy': u'sa',
    u'hk': u'as',
    u'hm': u'an',
    u'hn': u'na',
    u'hr': u'eu',
    u'ht': u'na',
    u'hu': u'eu',
    u'id': u'as',
    u'ie': u'eu',
    u'il': u'as',
    u'im': u'eu',
    u'in': u'as',
    u'io': u'as',
    u'iq': u'as',
    u'ir': u'as',
    u'is': u'eu',
    u'it': u'eu',
    u'je': u'eu',
    u'jm': u'na',
    u'jo': u'as',
    u'jp': u'as',
    u'ke': u'af',
    u'kg': u'as',
    u'kh': u'as',
    u'ki': u'oc',
    u'km': u'af',
    u'kn': u'na',
    u'kp': u'as',
    u'kr': u'as',
    u'kw': u'as',
    u'ky': u'na',
    u'kz': u'as',
    u'la': u'as',
    u'lb': u'as',
    u'lc': u'na',
    u'li': u'eu',
    u'lk': u'as',
    u'lr': u'af',
    u'ls': u'af',
    u'lt': u'eu',
    u'lu': u'eu',
    u'lv': u'eu',
    u'ly': u'af',
    u'ma': u'af',
    u'mc': u'eu',
    u'md': u'eu',
    u'me': u'eu',
    u'mf': u'na',
    u'mg': u'af',
    u'mh': u'oc',
    u'mk': u'eu',
    u'ml': u'af',
    u'mm': u'as',
    u'mn': u'as',
    u'mo': u'as',
    u'mp': u'oc',
    u'mq': u'na',
    u'mr': u'af',
    u'ms': u'na',
    u'mt': u'eu',
    u'mu': u'af',
    u'mv': u'as',
    u'mw': u'af',
    u'mx': u'na',
    u'my': u'as',
    u'mz': u'af',
    u'na': u'af',
    u'nc': u'oc',
    u'ne': u'af',
    u'nf': u'oc',
    u'ng': u'af',
    u'ni': u'na',
    u'nl': u'eu',
    u'no': u'eu',
    u'np': u'as',
    u'nr': u'oc',
    u'nu': u'oc',
    u'nz': u'oc',
    u'o1': u'--',
    u'om': u'as',
    u'pa': u'na',
    u'pe': u'sa',
    u'pf': u'oc',
    u'pg': u'oc',
    u'ph': u'as',
    u'pk': u'as',
    u'pl': u'eu',
    u'pm': u'na',
    u'pn': u'oc',
    u'pr': u'na',
    u'ps': u'as',
    u'pt': u'eu',
    u'pw': u'oc',
    u'py': u'sa',
    u'qa': u'as',
    u're': u'af',
    u'ro': u'eu',
    u'rs': u'eu',
    u'ru': u'eu',
    u'rw': u'af',
    u'sa': u'as',
    u'sb': u'oc',
    u'sc': u'af',
    u'sd': u'af',
    u'se': u'eu',
    u'sg': u'as',
    u'sh': u'af',
    u'si': u'eu',
    u'sj': u'eu',
    u'sk': u'eu',
    u'sl': u'af',
    u'sm': u'eu',
    u'sn': u'af',
    u'so': u'af',
    u'sr': u'sa',
    u'ss': u'af',
    u'st': u'af',
    u'sv': u'na',
    u'sy': u'as',
    u'sz': u'af',
    u'tc': u'na',
    u'td': u'af',
    u'tf': u'an',
    u'tg': u'af',
    u'th': u'as',
    u'tj': u'as',
    u'tk': u'oc',
    u'tl': u'as',
    u'tm': u'as',
    u'tn': u'af',
    u'to': u'oc',
    u'tr': u'eu',
    u'tt': u'na',
    u'tv': u'oc',
    u'tw': u'as',
    u'tz': u'af',
    u'ua': u'eu',
    u'ug': u'af',
    u'um': u'oc',
    u'us': u'na',
    u'uy': u'sa',
    u'uz': u'as',
    u'va': u'eu',
    u'vc': u'na',
    u've': u'sa',
    u'vg': u'na',
    u'vi': u'na',
    u'vn': u'as',
    u'vu': u'oc',
    u'wf': u'oc',
    u'ws': u'oc',
    u'ye': u'as',
    u'yt': u'af',
    u'za': u'af',
    u'zm': u'af',
    u'zw': u'af',
}

CONTINENTS = (
    (u"af", _(u"Africa")),
    (u"as", _(u"Asia")),
    (u"eu", _(u"Europe")),
    (u"na", _(u"North America")),
    (u"sa", _(u"South America")),
    (u"oc", _(u"Oceania")),
    (u"an", _(u"Antarctica")),
)