# Day 11 : Fonctions - Exercices Level 1

import math


countries_data = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": [
            "Arabic"
        ],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar"
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    },
    {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "languages": [
            "Catalan"
        ],
        "population": 78014,
        "flag": "https://restcountries.eu/data/and.svg",
        "currency": "Euro"
    },
    {
        "name": "Angola",
        "capital": "Luanda",
        "languages": [
            "Portuguese"
        ],
        "population": 25868000,
        "flag": "https://restcountries.eu/data/ago.svg",
        "currency": "Angolan kwanza"
    },
    {
        "name": "Anguilla",
        "capital": "The Valley",
        "languages": [
            "English"
        ],
        "population": 13452,
        "flag": "https://restcountries.eu/data/aia.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Antarctica",
        "capital": "",
        "languages": [
            "English",
            "Russian"
        ],
        "population": 1000,
        "flag": "https://restcountries.eu/data/ata.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Antigua and Barbuda",
        "capital": "Saint John's",
        "languages": [
            "English"
        ],
        "population": 86295,
        "flag": "https://restcountries.eu/data/atg.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Argentina",
        "capital": "Buenos Aires",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 43590400,
        "flag": "https://restcountries.eu/data/arg.svg",
        "currency": "Argentine peso"
    },
    {
        "name": "Armenia",
        "capital": "Yerevan",
        "languages": [
            "Armenian",
            "Russian"
        ],
        "population": 2994400,
        "flag": "https://restcountries.eu/data/arm.svg",
        "currency": "Armenian dram"
    },
    {
        "name": "Aruba",
        "capital": "Oranjestad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi"
        ],
        "population": 107394,
        "flag": "https://restcountries.eu/data/abw.svg",
        "currency": "Aruban florin"
    },
    {
        "name": "Australia",
        "capital": "Canberra",
        "languages": [
            "English"
        ],
        "population": 24117360,
        "flag": "https://restcountries.eu/data/aus.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Austria",
        "capital": "Vienna",
        "languages": [
            "German"
        ],
        "population": 8725931,
        "flag": "https://restcountries.eu/data/aut.svg",
        "currency": "Euro"
    },
    {
        "name": "Azerbaijan",
        "capital": "Baku",
        "languages": [
            "Azerbaijani"
        ],
        "population": 9730500,
        "flag": "https://restcountries.eu/data/aze.svg",
        "currency": "Azerbaijani manat"
    },
    {
        "name": "Bahamas",
        "capital": "Nassau",
        "languages": [
            "English"
        ],
        "population": 378040,
        "flag": "https://restcountries.eu/data/bhs.svg",
        "currency": "Bahamian dollar"
    },
    {
        "name": "Bahrain",
        "capital": "Manama",
        "languages": [
            "Arabic"
        ],
        "population": 1404900,
        "flag": "https://restcountries.eu/data/bhr.svg",
        "currency": "Bahraini dinar"
    },
    {
        "name": "Bangladesh",
        "capital": "Dhaka",
        "languages": [
            "Bengali"
        ],
        "population": 161006790,
        "flag": "https://restcountries.eu/data/bgd.svg",
        "currency": "Bangladeshi taka"
    },
    {
        "name": "Barbados",
        "capital": "Bridgetown",
        "languages": [
            "English"
        ],
        "population": 285000,
        "flag": "https://restcountries.eu/data/brb.svg",
        "currency": "Barbadian dollar"
    },
    {
        "name": "Belarus",
        "capital": "Minsk",
        "languages": [
            "Belarusian",
            "Russian"
        ],
        "population": 9498700,
        "flag": "https://restcountries.eu/data/blr.svg",
        "currency": "New Belarusian ruble"
    },
    {
        "name": "Belgium",
        "capital": "Brussels",
        "languages": [
            "Dutch",
            "French",
            "German"
        ],
        "population": 11319511,
        "flag": "https://restcountries.eu/data/bel.svg",
        "currency": "Euro"
    },
    {
        "name": "Belize",
        "capital": "Belmopan",
        "languages": [
            "English",
            "Spanish"
        ],
        "population": 370300,
        "flag": "https://restcountries.eu/data/blz.svg",
        "currency": "Belize dollar"
    },
    {
        "name": "Benin",
        "capital": "Porto-Novo",
        "languages": [
            "French"
        ],
        "population": 10653654,
        "flag": "https://restcountries.eu/data/ben.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Bermuda",
        "capital": "Hamilton",
        "languages": [
            "English"
        ],
        "population": 61954,
        "flag": "https://restcountries.eu/data/bmu.svg",
        "currency": "Bermudian dollar"
    },
    {
        "name": "Bhutan",
        "capital": "Thimphu",
        "languages": [
            "Dzongkha"
        ],
        "population": 775620,
        "flag": "https://restcountries.eu/data/btn.svg",
        "currency": "Bhutanese ngultrum"
    },
    {
        "name": "Bolivia (Plurinational State of)",
        "capital": "Sucre",
        "languages": [
            "Spanish",
            "Aymara",
            "Quechua"
        ],
        "population": 10985059,
        "flag": "https://restcountries.eu/data/bol.svg",
        "currency": "Bolivian boliviano"
    },
    {
        "name": "Bonaire, Sint Eustatius and Saba",
        "capital": "Kralendijk",
        "languages": [
            "Dutch"
        ],
        "population": 17408,
        "flag": "https://restcountries.eu/data/bes.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Bosnia and Herzegovina",
        "capital": "Sarajevo",
        "languages": [
            "Bosnian",
            "Croatian",
            "Serbian"
        ],
        "population": 3531159,
        "flag": "https://restcountries.eu/data/bih.svg",
        "currency": "Bosnia and Herzegovina convertible mark"
    },
    {
        "name": "Botswana",
        "capital": "Gaborone",
        "languages": [
            "English",
            "Tswana"
        ],
        "population": 2141206,
        "flag": "https://restcountries.eu/data/bwa.svg",
        "currency": "Botswana pula"
    },
    {
        "name": "Bouvet Island",
        "capital": "",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/bvt.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Brazil",
        "capital": "Brasília",
        "languages": [
            "Portuguese"
        ],
        "population": 206135893,
        "flag": "https://restcountries.eu/data/bra.svg",
        "currency": "Brazilian real"
    },
    {
        "name": "British Indian Ocean Territory",
        "capital": "Diego Garcia",
        "languages": [
            "English"
        ],
        "population": 3000,
        "flag": "https://restcountries.eu/data/iot.svg",
        "currency": "United States dollar"
    },
    {
        "name": "United States Minor Outlying Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 300,
        "flag": "https://restcountries.eu/data/umi.svg",
        "currency": "United States Dollar"
    },
    {
        "name": "Virgin Islands (British)",
        "capital": "Road Town",
        "languages": [
            "English"
        ],
        "population": 28514,
        "flag": "https://restcountries.eu/data/vgb.svg",
        "currency": "[D]"
    },
    {
        "name": "Virgin Islands (U.S.)",
        "capital": "Charlotte Amalie",
        "languages": [
            "English"
        ],
        "population": 114743,
        "flag": "https://restcountries.eu/data/vir.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Brunei Darussalam",
        "capital": "Bandar Seri Begawan",
        "languages": [
            "Malay"
        ],
        "population": 411900,
        "flag": "https://restcountries.eu/data/brn.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Bulgaria",
        "capital": "Sofia",
        "languages": [
            "Bulgarian"
        ],
        "population": 7153784,
        "flag": "https://restcountries.eu/data/bgr.svg",
        "currency": "Bulgarian lev"
    },
    {
        "name": "Burkina Faso",
        "capital": "Ouagadougou",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 19034397,
        "flag": "https://restcountries.eu/data/bfa.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Burundi",
        "capital": "Bujumbura",
        "languages": [
            "French",
            "Kirundi"
        ],
        "population": 10114505,
        "flag": "https://restcountries.eu/data/bdi.svg",
        "currency": "Burundian franc"
    },
    {
        "name": "Cambodia",
        "capital": "Phnom Penh",
        "languages": [
            "Khmer"
        ],
        "population": 15626444,
        "flag": "https://restcountries.eu/data/khm.svg",
        "currency": "Cambodian riel"
    },
    {
        "name": "Cameroon",
        "capital": "Yaoundé",
        "languages": [
            "English",
            "French"
        ],
        "population": 22709892,
        "flag": "https://restcountries.eu/data/cmr.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Canada",
        "capital": "Ottawa",
        "languages": [
            "English",
            "French"
        ],
        "population": 36155487,
        "flag": "https://restcountries.eu/data/can.svg",
        "currency": "Canadian dollar"
    },
    {
        "name": "Cabo Verde",
        "capital": "Praia",
        "languages": [
            "Portuguese"
        ],
        "population": 531239,
        "flag": "https://restcountries.eu/data/cpv.svg",
        "currency": "Cape Verdean escudo"
    },
    {
        "name": "Cayman Islands",
        "capital": "George Town",
        "languages": [
            "English"
        ],
        "population": 58238,
        "flag": "https://restcountries.eu/data/cym.svg",
        "currency": "Cayman Islands dollar"
    },
    {
        "name": "Central African Republic",
        "capital": "Bangui",
        "languages": [
            "French",
            "Sango"
        ],
        "population": 4998000,
        "flag": "https://restcountries.eu/data/caf.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chad",
        "capital": "N'Djamena",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 14497000,
        "flag": "https://restcountries.eu/data/tcd.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Chile",
        "capital": "Santiago",
        "languages": [
            "Spanish"
        ],
        "population": 18191900,
        "flag": "https://restcountries.eu/data/chl.svg",
        "currency": "Chilean peso"
    },
    {
        "name": "China",
        "capital": "Beijing",
        "languages": [
            "Chinese"
        ],
        "population": 1377422166,
        "flag": "https://restcountries.eu/data/chn.svg",
        "currency": "Chinese yuan"
    },
    {
        "name": "Christmas Island",
        "capital": "Flying Fish Cove",
        "languages": [
            "English"
        ],
        "population": 2072,
        "flag": "https://restcountries.eu/data/cxr.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Cocos (Keeling) Islands",
        "capital": "West Island",
        "languages": [
            "English"
        ],
        "population": 550,
        "flag": "https://restcountries.eu/data/cck.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Colombia",
        "capital": "Bogotá",
        "languages": [
            "Spanish"
        ],
        "population": 48759958,
        "flag": "https://restcountries.eu/data/col.svg",
        "currency": "Colombian peso"
    },
    {
        "name": "Comoros",
        "capital": "Moroni",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 806153,
        "flag": "https://restcountries.eu/data/com.svg",
        "currency": "Comorian franc"
    },
    {
        "name": "Congo",
        "capital": "Brazzaville",
        "languages": [
            "French",
            "Lingala"
        ],
        "population": 4741000,
        "flag": "https://restcountries.eu/data/cog.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Congo (Democratic Republic of the)",
        "capital": "Kinshasa",
        "languages": [
            "French",
            "Lingala",
            "Kongo",
            "Swahili",
            "Luba-Katanga"
        ],
        "population": 85026000,
        "flag": "https://restcountries.eu/data/cod.svg",
        "currency": "Congolese franc"
    },
    {
        "name": "Cook Islands",
        "capital": "Avarua",
        "languages": [
            "English"
        ],
        "population": 18100,
        "flag": "https://restcountries.eu/data/cok.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Costa Rica",
        "capital": "San José",
        "languages": [
            "Spanish"
        ],
        "population": 4890379,
        "flag": "https://restcountries.eu/data/cri.svg",
        "currency": "Costa Rican colón"
    },
    {
        "name": "Croatia",
        "capital": "Zagreb",
        "languages": [
            "Croatian"
        ],
        "population": 4190669,
        "flag": "https://restcountries.eu/data/hrv.svg",
        "currency": "Croatian kuna"
    },
    {
        "name": "Cuba",
        "capital": "Havana",
        "languages": [
            "Spanish"
        ],
        "population": 11239004,
        "flag": "https://restcountries.eu/data/cub.svg",
        "currency": "Cuban convertible peso"
    },
    {
        "name": "Curaçao",
        "capital": "Willemstad",
        "languages": [
            "Dutch",
            "(Eastern) Punjabi",
            "English"
        ],
        "population": 154843,
        "flag": "https://restcountries.eu/data/cuw.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Cyprus",
        "capital": "Nicosia",
        "languages": [
            "Greek (modern)",
            "Turkish",
            "Armenian"
        ],
        "population": 847000,
        "flag": "https://restcountries.eu/data/cyp.svg",
        "currency": "Euro"
    },
    {
        "name": "Czech Republic",
        "capital": "Prague",
        "languages": [
            "Czech",
            "Slovak"
        ],
        "population": 10558524,
        "flag": "https://restcountries.eu/data/cze.svg",
        "currency": "Czech koruna"
    },
    {
        "name": "Denmark",
        "capital": "Copenhagen",
        "languages": [
            "Danish"
        ],
        "population": 5717014,
        "flag": "https://restcountries.eu/data/dnk.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Djibouti",
        "capital": "Djibouti",
        "languages": [
            "French",
            "Arabic"
        ],
        "population": 900000,
        "flag": "https://restcountries.eu/data/dji.svg",
        "currency": "Djiboutian franc"
    },
    {
        "name": "Dominica",
        "capital": "Roseau",
        "languages": [
            "English"
        ],
        "population": 71293,
        "flag": "https://restcountries.eu/data/dma.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Dominican Republic",
        "capital": "Santo Domingo",
        "languages": [
            "Spanish"
        ],
        "population": 10075045,
        "flag": "https://restcountries.eu/data/dom.svg",
        "currency": "Dominican peso"
    },
    {
        "name": "Ecuador",
        "capital": "Quito",
        "languages": [
            "Spanish"
        ],
        "population": 16545799,
        "flag": "https://restcountries.eu/data/ecu.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Egypt",
        "capital": "Cairo",
        "languages": [
            "Arabic"
        ],
        "population": 91290000,
        "flag": "https://restcountries.eu/data/egy.svg",
        "currency": "Egyptian pound"
    },
    {
        "name": "El Salvador",
        "capital": "San Salvador",
        "languages": [
            "Spanish"
        ],
        "population": 6520675,
        "flag": "https://restcountries.eu/data/slv.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Equatorial Guinea",
        "capital": "Malabo",
        "languages": [
            "Spanish",
            "French"
        ],
        "population": 1222442,
        "flag": "https://restcountries.eu/data/gnq.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Eritrea",
        "capital": "Asmara",
        "languages": [
            "Tigrinya",
            "Arabic",
            "English"
        ],
        "population": 5352000,
        "flag": "https://restcountries.eu/data/eri.svg",
        "currency": "Eritrean nakfa"
    },
    {
        "name": "Estonia",
        "capital": "Tallinn",
        "languages": [
            "Estonian"
        ],
        "population": 1315944,
        "flag": "https://restcountries.eu/data/est.svg",
        "currency": "Euro"
    },
    {
        "name": "Ethiopia",
        "capital": "Addis Ababa",
        "languages": [
            "Amharic"
        ],
        "population": 92206005,
        "flag": "https://restcountries.eu/data/eth.svg",
        "currency": "Ethiopian birr"
    },
    {
        "name": "Falkland Islands (Malvinas)",
        "capital": "Stanley",
        "languages": [
            "English"
        ],
        "population": 2563,
        "flag": "https://restcountries.eu/data/flk.svg",
        "currency": "Falkland Islands pound"
    },
    {
        "name": "Faroe Islands",
        "capital": "Tórshavn",
        "languages": [
            "Faroese"
        ],
        "population": 49376,
        "flag": "https://restcountries.eu/data/fro.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Fiji",
        "capital": "Suva",
        "languages": [
            "English",
            "Fijian",
            "Hindi",
            "Urdu"
        ],
        "population": 867000,
        "flag": "https://restcountries.eu/data/fji.svg",
        "currency": "Fijian dollar"
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": [
            "Finnish",
            "Swedish"
        ],
        "population": 5491817,
        "flag": "https://restcountries.eu/data/fin.svg",
        "currency": "Euro"
    },
    {
        "name": "France",
        "capital": "Paris",
        "languages": [
            "French"
        ],
        "population": 66710000,
        "flag": "https://restcountries.eu/data/fra.svg",
        "currency": "Euro"
    },
    {
        "name": "French Guiana",
        "capital": "Cayenne",
        "languages": [
            "French"
        ],
        "population": 254541,
        "flag": "https://restcountries.eu/data/guf.svg",
        "currency": "Euro"
    },
    {
        "name": "French Polynesia",
        "capital": "Papeetē",
        "languages": [
            "French"
        ],
        "population": 271800,
        "flag": "https://restcountries.eu/data/pyf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "French Southern Territories",
        "capital": "Port-aux-Français",
        "languages": [
            "French"
        ],
        "population": 140,
        "flag": "https://restcountries.eu/data/atf.svg",
        "currency": "Euro"
    },
    {
        "name": "Gabon",
        "capital": "Libreville",
        "languages": [
            "French"
        ],
        "population": 1802278,
        "flag": "https://restcountries.eu/data/gab.svg",
        "currency": "Central African CFA franc"
    },
    {
        "name": "Gambia",
        "capital": "Banjul",
        "languages": [
            "English"
        ],
        "population": 1882450,
        "flag": "https://restcountries.eu/data/gmb.svg",
        "currency": "Gambian dalasi"
    },
    {
        "name": "Georgia",
        "capital": "Tbilisi",
        "languages": [
            "Georgian"
        ],
        "population": 3720400,
        "flag": "https://restcountries.eu/data/geo.svg",
        "currency": "Georgian Lari"
    },
    {
        "name": "Germany",
        "capital": "Berlin",
        "languages": [
            "German"
        ],
        "population": 81770900,
        "flag": "https://restcountries.eu/data/deu.svg",
        "currency": "Euro"
    },
    {
        "name": "Ghana",
        "capital": "Accra",
        "languages": [
            "English"
        ],
        "population": 27670174,
        "flag": "https://restcountries.eu/data/gha.svg",
        "currency": "Ghanaian cedi"
    },
    {
        "name": "Gibraltar",
        "capital": "Gibraltar",
        "languages": [
            "English"
        ],
        "population": 33140,
        "flag": "https://restcountries.eu/data/gib.svg",
        "currency": "Gibraltar pound"
    },
    {
        "name": "Greece",
        "capital": "Athens",
        "languages": [
            "Greek (modern)"
        ],
        "population": 10858018,
        "flag": "https://restcountries.eu/data/grc.svg",
        "currency": "Euro"
    },
    {
        "name": "Greenland",
        "capital": "Nuuk",
        "languages": [
            "Kalaallisut"
        ],
        "population": 55847,
        "flag": "https://restcountries.eu/data/grl.svg",
        "currency": "Danish krone"
    },
    {
        "name": "Grenada",
        "capital": "St. George's",
        "languages": [
            "English"
        ],
        "population": 103328,
        "flag": "https://restcountries.eu/data/grd.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Guadeloupe",
        "capital": "Basse-Terre",
        "languages": [
            "French"
        ],
        "population": 400132,
        "flag": "https://restcountries.eu/data/glp.svg",
        "currency": "Euro"
    },
    {
        "name": "Guam",
        "capital": "Hagåtña",
        "languages": [
            "English",
            "Chamorro",
            "Spanish"
        ],
        "population": 184200,
        "flag": "https://restcountries.eu/data/gum.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Guatemala",
        "capital": "Guatemala City",
        "languages": [
            "Spanish"
        ],
        "population": 16176133,
        "flag": "https://restcountries.eu/data/gtm.svg",
        "currency": "Guatemalan quetzal"
    },
    {
        "name": "Guernsey",
        "capital": "St. Peter Port",
        "languages": [
            "English",
            "French"
        ],
        "population": 62999,
        "flag": "https://restcountries.eu/data/ggy.svg",
        "currency": "British pound"
    },
    {
        "name": "Guinea",
        "capital": "Conakry",
        "languages": [
            "French",
            "Fula"
        ],
        "population": 12947000,
        "flag": "https://restcountries.eu/data/gin.svg",
        "currency": "Guinean franc"
    },
    {
        "name": "Guinea-Bissau",
        "capital": "Bissau",
        "languages": [
            "Portuguese"
        ],
        "population": 1547777,
        "flag": "https://restcountries.eu/data/gnb.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Guyana",
        "capital": "Georgetown",
        "languages": [
            "English"
        ],
        "population": 746900,
        "flag": "https://restcountries.eu/data/guy.svg",
        "currency": "Guyanese dollar"
    },
    {
        "name": "Haiti",
        "capital": "Port-au-Prince",
        "languages": [
            "French",
            "Haitian"
        ],
        "population": 11078033,
        "flag": "https://restcountries.eu/data/hti.svg",
        "currency": "Haitian gourde"
    },
    {
        "name": "Heard Island and McDonald Islands",
        "capital": "",
        "languages": [
            "English"
        ],
        "population": 0,
        "flag": "https://restcountries.eu/data/hmd.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Holy See",
        "capital": "Rome",
        "languages": [
            "Latin",
            "Italian",
            "French",
            "German"
        ],
        "population": 451,
        "flag": "https://restcountries.eu/data/vat.svg",
        "currency": "Euro"
    },
    {
        "name": "Honduras",
        "capital": "Tegucigalpa",
        "languages": [
            "Spanish"
        ],
        "population": 8576532,
        "flag": "https://restcountries.eu/data/hnd.svg",
        "currency": "Honduran lempira"
    },
    {
        "name": "Hong Kong",
        "capital": "City of Victoria",
        "languages": [
            "English",
            "Chinese"
        ],
        "population": 7324300,
        "flag": "https://restcountries.eu/data/hkg.svg",
        "currency": "Hong Kong dollar"
    },
    {
        "name": "Hungary",
        "capital": "Budapest",
        "languages": [
            "Hungarian"
        ],
        "population": 9823000,
        "flag": "https://restcountries.eu/data/hun.svg",
        "currency": "Hungarian forint"
    },
    {
        "name": "Iceland",
        "capital": "Reykjavík",
        "languages": [
            "Icelandic"
        ],
        "population": 334300,
        "flag": "https://restcountries.eu/data/isl.svg",
        "currency": "Icelandic króna"
    },
    {
        "name": "India",
        "capital": "New Delhi",
        "languages": [
            "Hindi",
            "English"
        ],
        "population": 1295210000,
        "flag": "https://restcountries.eu/data/ind.svg",
        "currency": "Indian rupee"
    },
    {
        "name": "Indonesia",
        "capital": "Jakarta",
        "languages": [
            "Indonesian"
        ],
        "population": 258705000,
        "flag": "https://restcountries.eu/data/idn.svg",
        "currency": "Indonesian rupiah"
    },
    {
        "name": "Côte d'Ivoire",
        "capital": "Yamoussoukro",
        "languages": [
            "French"
        ],
        "population": 22671331,
        "flag": "https://restcountries.eu/data/civ.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Iran (Islamic Republic of)",
        "capital": "Tehran",
        "languages": [
            "Persian (Farsi)"
        ],
        "population": 79369900,
        "flag": "https://restcountries.eu/data/irn.svg",
        "currency": "Iranian rial"
    },
    {
        "name": "Iraq",
        "capital": "Baghdad",
        "languages": [
            "Arabic",
            "Kurdish"
        ],
        "population": 37883543,
        "flag": "https://restcountries.eu/data/irq.svg",
        "currency": "Iraqi dinar"
    },
    {
        "name": "Ireland",
        "capital": "Dublin",
        "languages": [
            "Irish",
            "English"
        ],
        "population": 6378000,
        "flag": "https://restcountries.eu/data/irl.svg",
        "currency": "Euro"
    },
    {
        "name": "Isle of Man",
        "capital": "Douglas",
        "languages": [
            "English",
            "Manx"
        ],
        "population": 84497,
        "flag": "https://restcountries.eu/data/imn.svg",
        "currency": "British pound"
    },
    {
        "name": "Israel",
        "capital": "Jerusalem",
        "languages": [
            "Hebrew (modern)",
            "Arabic"
        ],
        "population": 8527400,
        "flag": "https://restcountries.eu/data/isr.svg",
        "currency": "Israeli new shekel"
    },
    {
        "name": "Italy",
        "capital": "Rome",
        "languages": [
            "Italian"
        ],
        "population": 60665551,
        "flag": "https://restcountries.eu/data/ita.svg",
        "currency": "Euro"
    },
    {
        "name": "Jamaica",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2723246,
        "flag": "https://restcountries.eu/data/jam.svg",
        "currency": "Jamaican dollar"
    },
    {
        "name": "Japan",
        "capital": "Tokyo",
        "languages": [
            "Japanese"
        ],
        "population": 126960000,
        "flag": "https://restcountries.eu/data/jpn.svg",
        "currency": "Japanese yen"
    },
    {
        "name": "Jersey",
        "capital": "Saint Helier",
        "languages": [
            "English",
            "French"
        ],
        "population": 100800,
        "flag": "https://restcountries.eu/data/jey.svg",
        "currency": "British pound"
    },
    {
        "name": "Jordan",
        "capital": "Amman",
        "languages": [
            "Arabic"
        ],
        "population": 9531712,
        "flag": "https://restcountries.eu/data/jor.svg",
        "currency": "Jordanian dinar"
    },
    {
        "name": "Kazakhstan",
        "capital": "Astana",
        "languages": [
            "Kazakh",
            "Russian"
        ],
        "population": 17753200,
        "flag": "https://restcountries.eu/data/kaz.svg",
        "currency": "Kazakhstani tenge"
    },
    {
        "name": "Kenya",
        "capital": "Nairobi",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 47251000,
        "flag": "https://restcountries.eu/data/ken.svg",
        "currency": "Kenyan shilling"
    },
    {
        "name": "Kiribati",
        "capital": "South Tarawa",
        "languages": [
            "English"
        ],
        "population": 113400,
        "flag": "https://restcountries.eu/data/kir.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Kuwait",
        "capital": "Kuwait City",
        "languages": [
            "Arabic"
        ],
        "population": 4183658,
        "flag": "https://restcountries.eu/data/kwt.svg",
        "currency": "Kuwaiti dinar"
    },
    {
        "name": "Kyrgyzstan",
        "capital": "Bishkek",
        "languages": [
            "Kyrgyz",
            "Russian"
        ],
        "population": 6047800,
        "flag": "https://restcountries.eu/data/kgz.svg",
        "currency": "Kyrgyzstani som"
    },
    {
        "name": "Lao People's Democratic Republic",
        "capital": "Vientiane",
        "languages": [
            "Lao"
        ],
        "population": 6492400,
        "flag": "https://restcountries.eu/data/lao.svg",
        "currency": "Lao kip"
    },
    {
        "name": "Latvia",
        "capital": "Riga",
        "languages": [
            "Latvian"
        ],
        "population": 1961600,
        "flag": "https://restcountries.eu/data/lva.svg",
        "currency": "Euro"
    },
    {
        "name": "Lebanon",
        "capital": "Beirut",
        "languages": [
            "Arabic",
            "French"
        ],
        "population": 5988000,
        "flag": "https://restcountries.eu/data/lbn.svg",
        "currency": "Lebanese pound"
    },
    {
        "name": "Lesotho",
        "capital": "Maseru",
        "languages": [
            "English",
            "Southern Sotho"
        ],
        "population": 1894194,
        "flag": "https://restcountries.eu/data/lso.svg",
        "currency": "Lesotho loti"
    },
    {
        "name": "Liberia",
        "capital": "Monrovia",
        "languages": [
            "English"
        ],
        "population": 4615000,
        "flag": "https://restcountries.eu/data/lbr.svg",
        "currency": "Liberian dollar"
    },
    {
        "name": "Libya",
        "capital": "Tripoli",
        "languages": [
            "Arabic"
        ],
        "population": 6385000,
        "flag": "https://restcountries.eu/data/lby.svg",
        "currency": "Libyan dinar"
    },
    {
        "name": "Liechtenstein",
        "capital": "Vaduz",
        "languages": [
            "German"
        ],
        "population": 37623,
        "flag": "https://restcountries.eu/data/lie.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Lithuania",
        "capital": "Vilnius",
        "languages": [
            "Lithuanian"
        ],
        "population": 2872294,
        "flag": "https://restcountries.eu/data/ltu.svg",
        "currency": "Euro"
    },
    {
        "name": "Luxembourg",
        "capital": "Luxembourg",
        "languages": [
            "French",
            "German",
            "Luxembourgish"
        ],
        "population": 576200,
        "flag": "https://restcountries.eu/data/lux.svg",
        "currency": "Euro"
    },
    {
        "name": "Macao",
        "capital": "",
        "languages": [
            "Chinese",
            "Portuguese"
        ],
        "population": 649100,
        "flag": "https://restcountries.eu/data/mac.svg",
        "currency": "Macanese pataca"
    },
    {
        "name": "Macedonia (the former Yugoslav Republic of)",
        "capital": "Skopje",
        "languages": [
            "Macedonian"
        ],
        "population": 2058539,
        "flag": "https://restcountries.eu/data/mkd.svg",
        "currency": "Macedonian denar"
    },
    {
        "name": "Madagascar",
        "capital": "Antananarivo",
        "languages": [
            "French",
            "Malagasy"
        ],
        "population": 22434363,
        "flag": "https://restcountries.eu/data/mdg.svg",
        "currency": "Malagasy ariary"
    },
    {
        "name": "Malawi",
        "capital": "Lilongwe",
        "languages": [
            "English",
            "Chichewa"
        ],
        "population": 16832910,
        "flag": "https://restcountries.eu/data/mwi.svg",
        "currency": "Malawian kwacha"
    },
    {
        "name": "Malaysia",
        "capital": "Kuala Lumpur",
        "languages": [
            "Malaysian"
        ],
        "population": 31405416,
        "flag": "https://restcountries.eu/data/mys.svg",
        "currency": "Malaysian ringgit"
    },
    {
        "name": "Maldives",
        "capital": "Malé",
        "languages": [
            "Divehi"
        ],
        "population": 344023,
        "flag": "https://restcountries.eu/data/mdv.svg",
        "currency": "Maldivian rufiyaa"
    },
    {
        "name": "Mali",
        "capital": "Bamako",
        "languages": [
            "French"
        ],
        "population": 18135000,
        "flag": "https://restcountries.eu/data/mli.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Malta",
        "capital": "Valletta",
        "languages": [
            "Maltese",
            "English"
        ],
        "population": 425384,
        "flag": "https://restcountries.eu/data/mlt.svg",
        "currency": "Euro"
    },
    {
        "name": "Marshall Islands",
        "capital": "Majuro",
        "languages": [
            "English",
            "Marshallese"
        ],
        "population": 54880,
        "flag": "https://restcountries.eu/data/mhl.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Martinique",
        "capital": "Fort-de-France",
        "languages": [
            "French"
        ],
        "population": 378243,
        "flag": "https://restcountries.eu/data/mtq.svg",
        "currency": "Euro"
    },
    {
        "name": "Mauritania",
        "capital": "Nouakchott",
        "languages": [
            "Arabic"
        ],
        "population": 3718678,
        "flag": "https://restcountries.eu/data/mrt.svg",
        "currency": "Mauritanian ouguiya"
    },
    {
        "name": "Mauritius",
        "capital": "Port Louis",
        "languages": [
            "English"
        ],
        "population": 1262879,
        "flag": "https://restcountries.eu/data/mus.svg",
        "currency": "Mauritian rupee"
    },
    {
        "name": "Mayotte",
        "capital": "Mamoudzou",
        "languages": [
            "French"
        ],
        "population": 226915,
        "flag": "https://restcountries.eu/data/myt.svg",
        "currency": "Euro"
    },
    {
        "name": "Mexico",
        "capital": "Mexico City",
        "languages": [
            "Spanish"
        ],
        "population": 122273473,
        "flag": "https://restcountries.eu/data/mex.svg",
        "currency": "Mexican peso"
    },
    {
        "name": "Micronesia (Federated States of)",
        "capital": "Palikir",
        "languages": [
            "English"
        ],
        "population": 102800,
        "flag": "https://restcountries.eu/data/fsm.svg",
        "currency": "[D]"
    },
    {
        "name": "Moldova (Republic of)",
        "capital": "Chișinău",
        "languages": [
            "Romanian"
        ],
        "population": 3553100,
        "flag": "https://restcountries.eu/data/mda.svg",
        "currency": "Moldovan leu"
    },
    {
        "name": "Monaco",
        "capital": "Monaco",
        "languages": [
            "French"
        ],
        "population": 38400,
        "flag": "https://restcountries.eu/data/mco.svg",
        "currency": "Euro"
    },
    {
        "name": "Mongolia",
        "capital": "Ulan Bator",
        "languages": [
            "Mongolian"
        ],
        "population": 3093100,
        "flag": "https://restcountries.eu/data/mng.svg",
        "currency": "Mongolian tögrög"
    },
    {
        "name": "Montenegro",
        "capital": "Podgorica",
        "languages": [
            "Serbian",
            "Bosnian",
            "Albanian",
            "Croatian"
        ],
        "population": 621810,
        "flag": "https://restcountries.eu/data/mne.svg",
        "currency": "Euro"
    },
    {
        "name": "Montserrat",
        "capital": "Plymouth",
        "languages": [
            "English"
        ],
        "population": 4922,
        "flag": "https://restcountries.eu/data/msr.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Morocco",
        "capital": "Rabat",
        "languages": [
            "Arabic"
        ],
        "population": 33337529,
        "flag": "https://restcountries.eu/data/mar.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Mozambique",
        "capital": "Maputo",
        "languages": [
            "Portuguese"
        ],
        "population": 26423700,
        "flag": "https://restcountries.eu/data/moz.svg",
        "currency": "Mozambican metical"
    },
    {
        "name": "Myanmar",
        "capital": "Naypyidaw",
        "languages": [
            "Burmese"
        ],
        "population": 51419420,
        "flag": "https://restcountries.eu/data/mmr.svg",
        "currency": "Burmese kyat"
    },
    {
        "name": "Namibia",
        "capital": "Windhoek",
        "languages": [
            "English",
            "Afrikaans"
        ],
        "population": 2324388,
        "flag": "https://restcountries.eu/data/nam.svg",
        "currency": "Namibian dollar"
    },
    {
        "name": "Nauru",
        "capital": "Yaren",
        "languages": [
            "English",
            "Nauruan"
        ],
        "population": 10084,
        "flag": "https://restcountries.eu/data/nru.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Nepal",
        "capital": "Kathmandu",
        "languages": [
            "Nepali"
        ],
        "population": 28431500,
        "flag": "https://restcountries.eu/data/npl.svg",
        "currency": "Nepalese rupee"
    },
    {
        "name": "Netherlands",
        "capital": "Amsterdam",
        "languages": [
            "Dutch"
        ],
        "population": 17019800,
        "flag": "https://restcountries.eu/data/nld.svg",
        "currency": "Euro"
    },
    {
        "name": "New Caledonia",
        "capital": "Nouméa",
        "languages": [
            "French"
        ],
        "population": 268767,
        "flag": "https://restcountries.eu/data/ncl.svg",
        "currency": "CFP franc"
    },
    {
        "name": "New Zealand",
        "capital": "Wellington",
        "languages": [
            "English",
            "Māori"
        ],
        "population": 4697854,
        "flag": "https://restcountries.eu/data/nzl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Nicaragua",
        "capital": "Managua",
        "languages": [
            "Spanish"
        ],
        "population": 6262703,
        "flag": "https://restcountries.eu/data/nic.svg",
        "currency": "Nicaraguan córdoba"
    },
    {
        "name": "Niger",
        "capital": "Niamey",
        "languages": [
            "French"
        ],
        "population": 20715000,
        "flag": "https://restcountries.eu/data/ner.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Nigeria",
        "capital": "Abuja",
        "languages": [
            "English"
        ],
        "population": 186988000,
        "flag": "https://restcountries.eu/data/nga.svg",
        "currency": "Nigerian naira"
    },
    {
        "name": "Niue",
        "capital": "Alofi",
        "languages": [
            "English"
        ],
        "population": 1470,
        "flag": "https://restcountries.eu/data/niu.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Norfolk Island",
        "capital": "Kingston",
        "languages": [
            "English"
        ],
        "population": 2302,
        "flag": "https://restcountries.eu/data/nfk.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Korea (Democratic People's Republic of)",
        "capital": "Pyongyang",
        "languages": [
            "Korean"
        ],
        "population": 25281000,
        "flag": "https://restcountries.eu/data/prk.svg",
        "currency": "North Korean won"
    },
    {
        "name": "Northern Mariana Islands",
        "capital": "Saipan",
        "languages": [
            "English",
            "Chamorro"
        ],
        "population": 56940,
        "flag": "https://restcountries.eu/data/mnp.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Norway",
        "capital": "Oslo",
        "languages": [
            "Norwegian",
            "Norwegian Bokmål",
            "Norwegian Nynorsk"
        ],
        "population": 5223256,
        "flag": "https://restcountries.eu/data/nor.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Oman",
        "capital": "Muscat",
        "languages": [
            "Arabic"
        ],
        "population": 4420133,
        "flag": "https://restcountries.eu/data/omn.svg",
        "currency": "Omani rial"
    },
    {
        "name": "Pakistan",
        "capital": "Islamabad",
        "languages": [
            "English",
            "Urdu"
        ],
        "population": 194125062,
        "flag": "https://restcountries.eu/data/pak.svg",
        "currency": "Pakistani rupee"
    },
    {
        "name": "Palau",
        "capital": "Ngerulmud",
        "languages": [
            "English"
        ],
        "population": 17950,
        "flag": "https://restcountries.eu/data/plw.svg",
        "currency": "[E]"
    },
    {
        "name": "Palestine, State of",
        "capital": "Ramallah",
        "languages": [
            "Arabic"
        ],
        "population": 4682467,
        "flag": "https://restcountries.eu/data/pse.svg",
        "currency": "Israeli new sheqel"
    },
    {
        "name": "Panama",
        "capital": "Panama City",
        "languages": [
            "Spanish"
        ],
        "population": 3814672,
        "flag": "https://restcountries.eu/data/pan.svg",
        "currency": "Panamanian balboa"
    },
    {
        "name": "Papua New Guinea",
        "capital": "Port Moresby",
        "languages": [
            "English"
        ],
        "population": 8083700,
        "flag": "https://restcountries.eu/data/png.svg",
        "currency": "Papua New Guinean kina"
    },
    {
        "name": "Paraguay",
        "capital": "Asunción",
        "languages": [
            "Spanish",
            "Guaraní"
        ],
        "population": 6854536,
        "flag": "https://restcountries.eu/data/pry.svg",
        "currency": "Paraguayan guaraní"
    },
    {
        "name": "Peru",
        "capital": "Lima",
        "languages": [
            "Spanish"
        ],
        "population": 31488700,
        "flag": "https://restcountries.eu/data/per.svg",
        "currency": "Peruvian sol"
    },
    {
        "name": "Philippines",
        "capital": "Manila",
        "languages": [
            "English"
        ],
        "population": 103279800,
        "flag": "https://restcountries.eu/data/phl.svg",
        "currency": "Philippine peso"
    },
    {
        "name": "Pitcairn",
        "capital": "Adamstown",
        "languages": [
            "English"
        ],
        "population": 56,
        "flag": "https://restcountries.eu/data/pcn.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Poland",
        "capital": "Warsaw",
        "languages": [
            "Polish"
        ],
        "population": 38437239,
        "flag": "https://restcountries.eu/data/pol.svg",
        "currency": "Polish złoty"
    },
    {
        "name": "Portugal",
        "capital": "Lisbon",
        "languages": [
            "Portuguese"
        ],
        "population": 10374822,
        "flag": "https://restcountries.eu/data/prt.svg",
        "currency": "Euro"
    },
    {
        "name": "Puerto Rico",
        "capital": "San Juan",
        "languages": [
            "Spanish",
            "English"
        ],
        "population": 3474182,
        "flag": "https://restcountries.eu/data/pri.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Qatar",
        "capital": "Doha",
        "languages": [
            "Arabic"
        ],
        "population": 2587564,
        "flag": "https://restcountries.eu/data/qat.svg",
        "currency": "Qatari riyal"
    },
    {
        "name": "Republic of Kosovo",
        "capital": "Pristina",
        "languages": [
            "Albanian",
            "Serbian"
        ],
        "population": 1733842,
        "flag": "https://restcountries.eu/data/kos.svg",
        "currency": "Euro"
    },
    {
        "name": "Réunion",
        "capital": "Saint-Denis",
        "languages": [
            "French"
        ],
        "population": 840974,
        "flag": "https://restcountries.eu/data/reu.svg",
        "currency": "Euro"
    },
    {
        "name": "Romania",
        "capital": "Bucharest",
        "languages": [
            "Romanian"
        ],
        "population": 19861408,
        "flag": "https://restcountries.eu/data/rou.svg",
        "currency": "Romanian leu"
    },
    {
        "name": "Russian Federation",
        "capital": "Moscow",
        "languages": [
            "Russian"
        ],
        "population": 146599183,
        "flag": "https://restcountries.eu/data/rus.svg",
        "currency": "Russian ruble"
    },
    {
        "name": "Rwanda",
        "capital": "Kigali",
        "languages": [
            "Kinyarwanda",
            "English",
            "French"
        ],
        "population": 11553188,
        "flag": "https://restcountries.eu/data/rwa.svg",
        "currency": "Rwandan franc"
    },
    {
        "name": "Saint Barthélemy",
        "capital": "Gustavia",
        "languages": [
            "French"
        ],
        "population": 9417,
        "flag": "https://restcountries.eu/data/blm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Helena, Ascension and Tristan da Cunha",
        "capital": "Jamestown",
        "languages": [
            "English"
        ],
        "population": 4255,
        "flag": "https://restcountries.eu/data/shn.svg",
        "currency": "Saint Helena pound"
    },
    {
        "name": "Saint Kitts and Nevis",
        "capital": "Basseterre",
        "languages": [
            "English"
        ],
        "population": 46204,
        "flag": "https://restcountries.eu/data/kna.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Lucia",
        "capital": "Castries",
        "languages": [
            "English"
        ],
        "population": 186000,
        "flag": "https://restcountries.eu/data/lca.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Saint Martin (French part)",
        "capital": "Marigot",
        "languages": [
            "English",
            "French",
            "Dutch"
        ],
        "population": 36979,
        "flag": "https://restcountries.eu/data/maf.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Pierre and Miquelon",
        "capital": "Saint-Pierre",
        "languages": [
            "French"
        ],
        "population": 6069,
        "flag": "https://restcountries.eu/data/spm.svg",
        "currency": "Euro"
    },
    {
        "name": "Saint Vincent and the Grenadines",
        "capital": "Kingstown",
        "languages": [
            "English"
        ],
        "population": 109991,
        "flag": "https://restcountries.eu/data/vct.svg",
        "currency": "East Caribbean dollar"
    },
    {
        "name": "Samoa",
        "capital": "Apia",
        "languages": [
            "Samoan",
            "English"
        ],
        "population": 194899,
        "flag": "https://restcountries.eu/data/wsm.svg",
        "currency": "Samoan tālā"
    },
    {
        "name": "San Marino",
        "capital": "City of San Marino",
        "languages": [
            "Italian"
        ],
        "population": 33005,
        "flag": "https://restcountries.eu/data/smr.svg",
        "currency": "Euro"
    },
    {
        "name": "Sao Tome and Principe",
        "capital": "São Tomé",
        "languages": [
            "Portuguese"
        ],
        "population": 187356,
        "flag": "https://restcountries.eu/data/stp.svg",
        "currency": "São Tomé and Príncipe dobra"
    },
    {
        "name": "Saudi Arabia",
        "capital": "Riyadh",
        "languages": [
            "Arabic"
        ],
        "population": 32248200,
        "flag": "https://restcountries.eu/data/sau.svg",
        "currency": "Saudi riyal"
    },
    {
        "name": "Senegal",
        "capital": "Dakar",
        "languages": [
            "French"
        ],
        "population": 14799859,
        "flag": "https://restcountries.eu/data/sen.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Serbia",
        "capital": "Belgrade",
        "languages": [
            "Serbian"
        ],
        "population": 7076372,
        "flag": "https://restcountries.eu/data/srb.svg",
        "currency": "Serbian dinar"
    },
    {
        "name": "Seychelles",
        "capital": "Victoria",
        "languages": [
            "French",
            "English"
        ],
        "population": 91400,
        "flag": "https://restcountries.eu/data/syc.svg",
        "currency": "Seychellois rupee"
    },
    {
        "name": "Sierra Leone",
        "capital": "Freetown",
        "languages": [
            "English"
        ],
        "population": 7075641,
        "flag": "https://restcountries.eu/data/sle.svg",
        "currency": "Sierra Leonean leone"
    },
    {
        "name": "Singapore",
        "capital": "Singapore",
        "languages": [
            "English",
            "Malay",
            "Tamil",
            "Chinese"
        ],
        "population": 5535000,
        "flag": "https://restcountries.eu/data/sgp.svg",
        "currency": "Brunei dollar"
    },
    {
        "name": "Sint Maarten (Dutch part)",
        "capital": "Philipsburg",
        "languages": [
            "Dutch",
            "English"
        ],
        "population": 38247,
        "flag": "https://restcountries.eu/data/sxm.svg",
        "currency": "Netherlands Antillean guilder"
    },
    {
        "name": "Slovakia",
        "capital": "Bratislava",
        "languages": [
            "Slovak"
        ],
        "population": 5426252,
        "flag": "https://restcountries.eu/data/svk.svg",
        "currency": "Euro"
    },
    {
        "name": "Slovenia",
        "capital": "Ljubljana",
        "languages": [
            "Slovene"
        ],
        "population": 2064188,
        "flag": "https://restcountries.eu/data/svn.svg",
        "currency": "Euro"
    },
    {
        "name": "Solomon Islands",
        "capital": "Honiara",
        "languages": [
            "English"
        ],
        "population": 642000,
        "flag": "https://restcountries.eu/data/slb.svg",
        "currency": "Solomon Islands dollar"
    },
    {
        "name": "Somalia",
        "capital": "Mogadishu",
        "languages": [
            "Somali",
            "Arabic"
        ],
        "population": 11079000,
        "flag": "https://restcountries.eu/data/som.svg",
        "currency": "Somali shilling"
    },
    {
        "name": "South Africa",
        "capital": "Pretoria",
        "languages": [
            "Afrikaans",
            "English",
            "Southern Ndebele",
            "Southern Sotho",
            "Swati",
            "Tswana",
            "Tsonga",
            "Venda",
            "Xhosa",
            "Zulu"
        ],
        "population": 55653654,
        "flag": "https://restcountries.eu/data/zaf.svg",
        "currency": "South African rand"
    },
    {
        "name": "South Georgia and the South Sandwich Islands",
        "capital": "King Edward Point",
        "languages": [
            "English"
        ],
        "population": 30,
        "flag": "https://restcountries.eu/data/sgs.svg",
        "currency": "British pound"
    },
    {
        "name": "Korea (Republic of)",
        "capital": "Seoul",
        "languages": [
            "Korean"
        ],
        "population": 50801405,
        "flag": "https://restcountries.eu/data/kor.svg",
        "currency": "South Korean won"
    },
    {
        "name": "South Sudan",
        "capital": "Juba",
        "languages": [
            "English"
        ],
        "population": 12131000,
        "flag": "https://restcountries.eu/data/ssd.svg",
        "currency": "South Sudanese pound"
    },
    {
        "name": "Spain",
        "capital": "Madrid",
        "languages": [
            "Spanish"
        ],
        "population": 46438422,
        "flag": "https://restcountries.eu/data/esp.svg",
        "currency": "Euro"
    },
    {
        "name": "Sri Lanka",
        "capital": "Colombo",
        "languages": [
            "Sinhalese",
            "Tamil"
        ],
        "population": 20966000,
        "flag": "https://restcountries.eu/data/lka.svg",
        "currency": "Sri Lankan rupee"
    },
    {
        "name": "Sudan",
        "capital": "Khartoum",
        "languages": [
            "Arabic",
            "English"
        ],
        "population": 39598700,
        "flag": "https://restcountries.eu/data/sdn.svg",
        "currency": "Sudanese pound"
    },
    {
        "name": "Suriname",
        "capital": "Paramaribo",
        "languages": [
            "Dutch"
        ],
        "population": 541638,
        "flag": "https://restcountries.eu/data/sur.svg",
        "currency": "Surinamese dollar"
    },
    {
        "name": "Svalbard and Jan Mayen",
        "capital": "Longyearbyen",
        "languages": [
            "Norwegian"
        ],
        "population": 2562,
        "flag": "https://restcountries.eu/data/sjm.svg",
        "currency": "Norwegian krone"
    },
    {
        "name": "Swaziland",
        "capital": "Lobamba",
        "languages": [
            "English",
            "Swati"
        ],
        "population": 1132657,
        "flag": "https://restcountries.eu/data/swz.svg",
        "currency": "Swazi lilangeni"
    },
    {
        "name": "Sweden",
        "capital": "Stockholm",
        "languages": [
            "Swedish"
        ],
        "population": 9894888,
        "flag": "https://restcountries.eu/data/swe.svg",
        "currency": "Swedish krona"
    },
    {
        "name": "Switzerland",
        "capital": "Bern",
        "languages": [
            "German",
            "French",
            "Italian"
        ],
        "population": 8341600,
        "flag": "https://restcountries.eu/data/che.svg",
        "currency": "Swiss franc"
    },
    {
        "name": "Syrian Arab Republic",
        "capital": "Damascus",
        "languages": [
            "Arabic"
        ],
        "population": 18564000,
        "flag": "https://restcountries.eu/data/syr.svg",
        "currency": "Syrian pound"
    },
    {
        "name": "Taiwan",
        "capital": "Taipei",
        "languages": [
            "Chinese"
        ],
        "population": 23503349,
        "flag": "https://restcountries.eu/data/twn.svg",
        "currency": "New Taiwan dollar"
    },
    {
        "name": "Tajikistan",
        "capital": "Dushanbe",
        "languages": [
            "Tajik",
            "Russian"
        ],
        "population": 8593600,
        "flag": "https://restcountries.eu/data/tjk.svg",
        "currency": "Tajikistani somoni"
    },
    {
        "name": "Tanzania, United Republic of",
        "capital": "Dodoma",
        "languages": [
            "Swahili",
            "English"
        ],
        "population": 55155000,
        "flag": "https://restcountries.eu/data/tza.svg",
        "currency": "Tanzanian shilling"
    },
    {
        "name": "Thailand",
        "capital": "Bangkok",
        "languages": [
            "Thai"
        ],
        "population": 65327652,
        "flag": "https://restcountries.eu/data/tha.svg",
        "currency": "Thai baht"
    },
    {
        "name": "Timor-Leste",
        "capital": "Dili",
        "languages": [
            "Portuguese"
        ],
        "population": 1167242,
        "flag": "https://restcountries.eu/data/tls.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Togo",
        "capital": "Lomé",
        "languages": [
            "French"
        ],
        "population": 7143000,
        "flag": "https://restcountries.eu/data/tgo.svg",
        "currency": "West African CFA franc"
    },
    {
        "name": "Tokelau",
        "capital": "Fakaofo",
        "languages": [
            "English"
        ],
        "population": 1411,
        "flag": "https://restcountries.eu/data/tkl.svg",
        "currency": "New Zealand dollar"
    },
    {
        "name": "Tonga",
        "capital": "Nuku'alofa",
        "languages": [
            "English",
            "Tonga (Tonga Islands)"
        ],
        "population": 103252,
        "flag": "https://restcountries.eu/data/ton.svg",
        "currency": "Tongan paʻanga"
    },
    {
        "name": "Trinidad and Tobago",
        "capital": "Port of Spain",
        "languages": [
            "English"
        ],
        "population": 1349667,
        "flag": "https://restcountries.eu/data/tto.svg",
        "currency": "Trinidad and Tobago dollar"
    },
    {
        "name": "Tunisia",
        "capital": "Tunis",
        "languages": [
            "Arabic"
        ],
        "population": 11154400,
        "flag": "https://restcountries.eu/data/tun.svg",
        "currency": "Tunisian dinar"
    },
    {
        "name": "Turkey",
        "capital": "Ankara",
        "languages": [
            "Turkish"
        ],
        "population": 78741053,
        "flag": "https://restcountries.eu/data/tur.svg",
        "currency": "Turkish lira"
    },
    {
        "name": "Turkmenistan",
        "capital": "Ashgabat",
        "languages": [
            "Turkmen",
            "Russian"
        ],
        "population": 4751120,
        "flag": "https://restcountries.eu/data/tkm.svg",
        "currency": "Turkmenistan manat"
    },
    {
        "name": "Turks and Caicos Islands",
        "capital": "Cockburn Town",
        "languages": [
            "English"
        ],
        "population": 31458,
        "flag": "https://restcountries.eu/data/tca.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Tuvalu",
        "capital": "Funafuti",
        "languages": [
            "English"
        ],
        "population": 10640,
        "flag": "https://restcountries.eu/data/tuv.svg",
        "currency": "Australian dollar"
    },
    {
        "name": "Uganda",
        "capital": "Kampala",
        "languages": [
            "English",
            "Swahili"
        ],
        "population": 33860700,
        "flag": "https://restcountries.eu/data/uga.svg",
        "currency": "Ugandan shilling"
    },
    {
        "name": "Ukraine",
        "capital": "Kiev",
        "languages": [
            "Ukrainian"
        ],
        "population": 42692393,
        "flag": "https://restcountries.eu/data/ukr.svg",
        "currency": "Ukrainian hryvnia"
    },
    {
        "name": "United Arab Emirates",
        "capital": "Abu Dhabi",
        "languages": [
            "Arabic"
        ],
        "population": 9856000,
        "flag": "https://restcountries.eu/data/are.svg",
        "currency": "United Arab Emirates dirham"
    },
    {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "capital": "London",
        "languages": [
            "English"
        ],
        "population": 65110000,
        "flag": "https://restcountries.eu/data/gbr.svg",
        "currency": "British pound"
    },
    {
        "name": "United States of America",
        "capital": "Washington, D.C.",
        "languages": [
            "English"
        ],
        "population": 323947000,
        "flag": "https://restcountries.eu/data/usa.svg",
        "currency": "United States dollar"
    },
    {
        "name": "Uruguay",
        "capital": "Montevideo",
        "languages": [
            "Spanish"
        ],
        "population": 3480222,
        "flag": "https://restcountries.eu/data/ury.svg",
        "currency": "Uruguayan peso"
    },
    {
        "name": "Uzbekistan",
        "capital": "Tashkent",
        "languages": [
            "Uzbek",
            "Russian"
        ],
        "population": 31576400,
        "flag": "https://restcountries.eu/data/uzb.svg",
        "currency": "Uzbekistani so'm"
    },
    {
        "name": "Vanuatu",
        "capital": "Port Vila",
        "languages": [
            "Bislama",
            "English",
            "French"
        ],
        "population": 277500,
        "flag": "https://restcountries.eu/data/vut.svg",
        "currency": "Vanuatu vatu"
    },
    {
        "name": "Venezuela (Bolivarian Republic of)",
        "capital": "Caracas",
        "languages": [
            "Spanish"
        ],
        "population": 31028700,
        "flag": "https://restcountries.eu/data/ven.svg",
        "currency": "Venezuelan bolívar"
    },
    {
        "name": "Viet Nam",
        "capital": "Hanoi",
        "languages": [
            "Vietnamese"
        ],
        "population": 92700000,
        "flag": "https://restcountries.eu/data/vnm.svg",
        "currency": "Vietnamese đồng"
    },
    {
        "name": "Wallis and Futuna",
        "capital": "Mata-Utu",
        "languages": [
            "French"
        ],
        "population": 11750,
        "flag": "https://restcountries.eu/data/wlf.svg",
        "currency": "CFP franc"
    },
    {
        "name": "Western Sahara",
        "capital": "El Aaiún",
        "languages": [
            "Spanish"
        ],
        "population": 510713,
        "flag": "https://restcountries.eu/data/esh.svg",
        "currency": "Moroccan dirham"
    },
    {
        "name": "Yemen",
        "capital": "Sana'a",
        "languages": [
            "Arabic"
        ],
        "population": 27478000,
        "flag": "https://restcountries.eu/data/yem.svg",
        "currency": "Yemeni rial"
    },
    {
        "name": "Zambia",
        "capital": "Lusaka",
        "languages": [
            "English"
        ],
        "population": 15933883,
        "flag": "https://restcountries.eu/data/zmb.svg",
        "currency": "Zambian kwacha"
    },
    {
        "name": "Zimbabwe",
        "capital": "Harare",
        "languages": [
            "English",
            "Shona",
            "Northern Ndebele"
        ],
        "population": 14240168,
        "flag": "https://restcountries.eu/data/zwe.svg",
        "currency": "Botswana pula"
    }
]

##### Exercice 1: level 1
# 1. Fonction qui additionne deux nombres
def add_two_numbers(a, b):
    """Prend deux paramètres et retourne leur somme"""
    return a + b

# 2. Fonction qui calcule l'aire d'un cercle
def area_of_circle(r):
    """Calcule l'aire d'un cercle avec le rayon r"""
    return 3.14 * r * r

# 3. Fonction qui additionne un nombre arbitraire d'arguments
def add_nums(*args):
    """Additionne tous les arguments. Vérifie que tous sont des nombres."""
    # Vérifier que tous les arguments sont des nombres
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Erreur: Tous les arguments doivent être des nombres"
    # Retourner la somme des arguments
    return sum(args)

# 4. Fonction de conversion Celsius vers Fahrenheit
def conversion_celsius_to_fahrenheit(celsius):
    """Convertit une température de Celsius vers Fahrenheit"""
    return (celsius * 9/5) + 32

# 5. Fonction qui détermine la saison selon le mois
def find_season(month):
    """Retourne la saison selon le mois donné selon les mois français et anglais"""
    month = month.lower()
    
    if month in ['décembre', 'janvier', 'février', 'december', 'january', 'february', 'decembre', 'fevrier']:
        return 'Hiver'
    elif month in ['mars', 'avril', 'mai', 'march', 'april', 'may']:
        return 'Printemps'
    elif month in ['juin', 'juillet', 'août', 'june', 'july', 'august', 'aout']:
        return 'Été'
    elif month in ['septembre', 'octobre', 'novembre', 'september', 'october', 'november']:
        return 'Automne'
    ### Cas de Certains pays ou régions
    # elif month in ['novembre', 'décembre', 'janvier', 'fevrier', 'november', 'december', 'january', 'february', 'decembre', 'février']:
    #     return 'Harmattan'
    # elif month in ['juin', 'juillet', 'août', 'september', 'october', 'june', 'july', 'august', 'aout', 'septembre', 'octobre']:
    #     return 'Mousson'
    else:
        return 'Mois invalide'

# 6. Fonction qui calcule la pente d'une équation linéaire
def calculate_slope(x1, y1, x2, y2):
    """Calcule la pente d'une ligne entre deux points (x1, y1) et (x2, y2)"""
    if x2 - x1 == 0:
        return "Pente infinie (ligne verticale)"
    return (y2 - y1) / (x2 - x1)

# 7. Fonction qui résout une équation de second degré
def solve_equation_second_degre(a, b, c):
    """Résout une équation de second degré ax² + bx + c = 0"""
    if a == 0:
        return "Ce n'est pas une équation de second degré"

    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return "Pas de solution dans R"

# 8. Fonction qui Affiche chaque élément d'une liste
def affiche_list(lst):
    """Affiche chaque élément de la liste"""
    for item in lst:
        print(item)

# 9. Fonction qui inverse une liste en utilisant des boucles
def reverse_list(arr):
    """Retourne une liste inversée en utilisant des boucles"""
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# 10. Fonction qui met en majuscule les éléments d'une liste
def capitalize_list_items(lst):
    """Retourne une liste avec tous les éléments en majuscules"""
    majuscules = []
    for item in lst:
        if isinstance(item, str):
            majuscules.append(item.upper())
        else:
            majuscules.append(item)
    return majuscules

# 11. Fonction qui ajoute un élément à la fin d'une liste
def add_item(lst, item):
    """Retourne une nouvelle liste avec l'élément ajouté à la fin"""
    new_list = lst.copy()  # Créer une copie pour ne pas modifier l'original
    new_list.append(item)
    return new_list

# 12. Fonction qui supprime un élément d'une liste
def remove_item(lst, item):
    """Retourne une nouvelle liste sans l'élément supprimé"""
    new_list = lst.copy()  # Créer une copie pour ne pas modifier l'original
    if item in new_list:
        new_list.remove(item)
    return new_list

# 13. Fonction qui additionne tous les nombres dans une plage
def sum_of_numbers(n):
    """Additionne tous les nombres de 1 à n inclus"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 14. Fonction qui additionne tous les nombres impairs dans une plage
def sum_of_odds(n):
    """Additionne tous les nombres impairs de 1 à n inclus"""
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  # Si le nombre est impair
            total += i
    return total

# 15. Fonction qui additionne tous les nombres pairs dans une plage
def sum_of_even(n):
    """Additionne tous les nombres pairs de 1 à n inclus"""
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:  # Si le nombre est pair
            total += i
    return total

##### Exercice 2: Level 2

# 1. Fonction qui compte les nombres pairs et impairs
def evens_and_odds(number):
    """Compte le nombre de chiffres pairs et impairs dans un entier positif"""
    evens = 0
    odds = 0
    
    # Convertir en chaîne pour parcourir chaque chiffre
    str_number = str(number)
    
    for digit in str_number:
        digit_int = int(digit)
        if digit_int % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

# 2. Fonction factorielle
def factorial(n):
    """Calcule la factorielle d'un nombre entier positif"""
    if n < 0:
        return "La factorielle n'est pas définie pour les nombres négatifs"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# 3. Fonction qui vérifie si un paramètre est vide
def is_empty(param):
    """Vérifie si un paramètre est vide ou non"""
    if param is None:
        return True
    elif isinstance(param, (list, tuple, dict, str, set)):
        return len(param) == 0
    elif isinstance(param, (int, float)):
        return param == 0
    else:
        return False

# 4. Fonctions statistiques pour les listes
def calculate_mean(lst):
    """Calcule la moyenne d'une liste de nombres"""
    if not lst:
        return None
    return sum(lst) / len(lst)

def calculate_median(lst):
    """Calcule la médiane d'une liste de nombres"""
    if not lst:
        return None
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 0:  # Nombre pair d'éléments
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:  # Nombre impair d'éléments
        return sorted_lst[n//2]

def calculate_mode(lst):
    """Calcule le mode (valeur la plus fréquente) d'une liste"""
    if not lst:
        return None
    
    # Compter les fréquences
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Trouver la fréquence maximale
    max_frequency = max(frequency.values())
    
    # Trouver toutes les valeurs avec la fréquence maximale
    modes = [key for key, value in frequency.items() if value == max_frequency]
    
    return modes if len(modes) > 1 else modes[0]

def calculate_range(lst):
    """Calcule l'étendue (différence entre max et min) d'une liste"""
    if not lst:
        return None
    return max(lst) - min(lst)

def calculate_variance(lst):
    """Calcule la variance d'une liste de nombres"""
    if not lst:
        return None
    
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance

def calculate_std(lst):
    """Calcule l'écart-type d'une liste de nombres"""
    if not lst:
        return None
    
    variance = calculate_variance(lst)
    return math.sqrt(variance)

##### Exercice 3: Level 3

# 1. Fonction qui vérifie si un nombre est premier
def is_prime(number):
    """Vérifie si un nombre est premier"""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Vérifier les diviseurs impairs jusqu'à la racine carrée
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

# 2. Fonction qui vérifie si tous les éléments d'une liste sont uniques
def all_items_unique(lst):
    """Vérifie si tous les éléments de la liste sont uniques"""
    return len(lst) == len(set(lst))

# 3. Fonction qui vérifie si tous les éléments sont du même type
def all_same_type(lst):
    """Vérifie si tous les éléments de la liste sont du même type de données"""
    if not lst:
        return True
    
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

# 4. Fonction qui vérifie si une variable est un nom de variable Python valide
def is_valid_python_variable(variable_name):
    """Vérifie si le nom de variable fourni est valide en Python"""
    import keyword
    import re
    
    # Vérifier si c'est une chaîne
    if not isinstance(variable_name, str):
        return False
    
    # Vérifier si c'est un mot-clé Python
    if keyword.iskeyword(variable_name):
        return False
    
    # Vérifier le format avec une expression régulière
    # Doit commencer par une lettre ou underscore, suivi de lettres, chiffres ou underscores
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable_name))

# 5. Fonctions pour analyser les données des pays
def most_spoken_languages(countries_data, n=10):
    """Retourne les n langues les plus parlées dans le monde"""
    language_count = {}
    
    for country in countries_data:
        if 'languages' in country:
            for language in country['languages']:
                language_count[language] = language_count.get(language, 0) + 1
    
    # Trier par nombre de pays où la langue est parlée (ordre décroissant)
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_languages[:n]

def most_populated_countries(countries_data, n=10):
    """Retourne les n pays les plus peuplés dans le monde"""
    # Trier les pays par population (ordre décroissant)
    sorted_countries = sorted(countries_data, key=lambda x: x.get('population', 0), reverse=True)
    
    # Retourner seulement les noms et populations des n premiers pays
    result = []
    for i in range(min(n, len(sorted_countries))):
        country = sorted_countries[i]
        result.append({
            'name': country.get('name', 'Unknown'),
            'population': country.get('population', 0)
        })
    
    return result

# Tests des fonctions
if __name__ == "__main__":
    print("=== Tests des fonctions ===")
    print("=== Exercice 1: Level 1 ===")
    print('****************************************************************************')
    print(f"1. addition des nombres 3, 5 = {add_two_numbers(5, 3)}")
    print('****************************************************************************')
    print(f"2. L'aire du cercle de rayon 3 = {area_of_circle(3)}")
    print('****************************************************************************')
    print(f"3. ajout de la liste (1, 2, 3, 4, 5) = {add_nums(1, 2, 3, 4, 5)}")
    print(f"   ajout de la liste (1, 2, 'hello', 4) = {add_nums(1, 2, 'hello', 4)}")
    print('****************************************************************************')
    print(f"4. conversion de celsius en fahrenheit: temperature ( 0) = {conversion_celsius_to_fahrenheit(0)}")
    print(f" conversion de celsius en fahrenheit: temperature (100) = {conversion_celsius_to_fahrenheit(100)}")
    print('****************************************************************************')
    print(f"5. Trouver la saison qu'il fait en Janvier = {find_season('janvier')}")
    print(f"   trouver la saison qu'il fait en Juillet = {find_season('juillet')}")
    print('****************************************************************************')
    print(f"6.  Calculer la pente entre (1, 1) et (4, 4) = {calculate_slope(1, 1, 4, 4)}")
    print(f"   calculer la pente entre (1, 1) et (1, 4) = {calculate_slope(1, 1, 1, 4)}")
    print('****************************************************************************')
    print(f"7. Résoudre l'équation du second degré avec a=1, b=-3, c=2 : {solve_equation_second_degre(1, -3, 2)}")
    print('****************************************************************************')
    print("8. afficher la liste (['a', 'b', 'c']):")
    affiche_list(['a', 'b', 'c'])
    print('****************************************************************************')
    print(f"9. Reverse de la liste [1, 2, 3, 4, 5] = {reverse_list([1, 2, 3, 4, 5])}")
    print(f"   Reverse de la liste ['A', 'B', 'C'] = {reverse_list(['A', 'B', 'C'])}")
    print('****************************************************************************')
    print(f"10. Rendre Majuscule les elements de la liste (['banana', 'orange', 'mango']): {capitalize_list_items(['banana', 'orange', 'mango'])}")
    print('****************************************************************************')
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    print(f"11. Ajouter un item à la liste food_staff ('Meat') = {add_item(food_staff, 'Meat')}")
    nombres = [2, 3, 7, 9]
    print(f"    Ajouter un item à la liste nombres (5) = {add_item(nombres, 5)}")
    print('****************************************************************************')
    print(f"12. Supprimer un item de la liste food_staff ('Mango') = {remove_item(food_staff, 'Mango')}")
    print(f"    Supprimer un item de la liste nombres (3) = {remove_item(nombres, 3)}")
    print('****************************************************************************')
    print(f"13. Somme des nombres de 1 à 5 = {sum_of_numbers(5)}")
    print(f"    Somme des nombres de 1 à 10 = {sum_of_numbers(10)}")
    print(f"    Somme des nombres de 1 à 100 = {sum_of_numbers(100)}")
    print('****************************************************************************')
    print(f"14. Somme des nombres impairs de 1 à 5 = {sum_of_odds(5)}")
    print(f"    Somme des nombres impairs de 1 à 10 = {sum_of_odds(10)}")
    print('****************************************************************************')
    print(f"15. Somme des nombres pairs de 1 à 5 = {sum_of_even(5)}")
    print(f"    Somme des nombres pairs de 1 à 10 = {sum_of_even(10)}")
    
    print("\n=== Exercice 2: Level 2 ===")
    print('****************************************************************************')
    print("1. Compter les chiffres pairs et impairs dans 100:")
    evens_and_odds(100)
    print("   Compter les chiffres pairs et impairs dans 123456:")
    evens_and_odds(123456)
    print('****************************************************************************')
    print(f"2. Factorielle de 5 = {factorial(5)}")
    print(f"   Factorielle de 0 = {factorial(0)}")
    print(f"   Factorielle de 10 = {factorial(10)}")
    print('****************************************************************************')
    print(f"3. is_empty([]) = {is_empty([])}")
    print(f"   is_empty([1, 2, 3]) = {is_empty([1, 2, 3])}")
    print(f"   is_empty('') = {is_empty('')}")
    print(f"   is_empty('hello') = {is_empty('hello')}")
    print(f"   is_empty(0) = {is_empty(0)}")
    print(f"   is_empty(None) = {is_empty(None)}")
    print('****************************************************************************')
    
    # Tests des fonctions statistiques
    test_numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    print("***************************************************************************")
    print("Fonctions statistiques de l'exercice 2 pour la liste [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]:")
    print(f"   Moyenne = {calculate_mean(test_numbers)}")
    print(f"   Médiane = {calculate_median(test_numbers)}")
    print(f"   Mode = {calculate_mode(test_numbers)}")
    print(f"   Étendue = {calculate_range(test_numbers)}")
    print(f"   Variance = {calculate_variance(test_numbers):.2f}")
    print(f"   Écart-type = {calculate_std(test_numbers):.2f}")
    print('****************************************************************************')
    print("\nExercice 3: Level 3")
    print('****************************************************************************')
    print(f"1. is_prime(2) = {is_prime(2)}")
    print(f"   is_prime(9) = {is_prime(9)}")
    print(f"   is_prime(17) = {is_prime(17)}")
    print(f"   is_prime(25) = {is_prime(25)}")
    print('****************************************************************************')
    print(f"2. all_items_unique([1, 2, 3, 4]) = {all_items_unique([1, 2, 3, 4])}")
    print(f"   all_items_unique([1, 2, 3, 2]) = {all_items_unique([1, 2, 3, 2])}")
    print('****************************************************************************')
    print(f"3. all_same_type([1, 2, 3]) = {all_same_type([1, 2, 3])}")
    print(f"   all_same_type([1, '2', 3]) = {all_same_type([1, '2', 3])}")
    print(f"   all_same_type(['a', 'b', 'c']) = {all_same_type(['a', 'b', 'c'])}")
    print('****************************************************************************')
    print(f"4. is_valid_python_variable('first_name') = {is_valid_python_variable('first_name')}")
    print(f"   is_valid_python_variable('first-name') = {is_valid_python_variable('first-name')}")
    print(f"   is_valid_python_variable('1first_name') = {is_valid_python_variable('1first_name')}")
    print(f"   is_valid_python_variable('def') = {is_valid_python_variable('def')}")
    print('****************************************************************************')
    print("5. Analyse des données des pays:")
    print("   Top 10 des langues les plus parlées:")
    languages = most_spoken_languages(countries_data, 10)
    for i, (language, count) in enumerate(languages, 1):
        print(f"      {i}. {language}: {count} pays")
        
    print("\n   Top 10 des pays les plus peuplés:")
    countries = most_populated_countries(countries_data, 10)
    for i, country in enumerate(countries, 1):
        print(f"      {i}. {country['name']}: {country['population']:,} habitants")
    print('****************************************************************************')
