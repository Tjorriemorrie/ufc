from fighters import *

DATA = [
    {
        'date': '2018-07-14',
        'name': 'UFC Fight Night',
        'location': 'Boise, Idaho',
        'venue': 'CenturyLink Arena',
        'fights': [
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JODIE_ESQUIBEL,
                        'stats': '6-4-0',
                    },
                    {
                        'name': JESSICA_AGUILAR,
                        'stats': '20-8-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_AGUILAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:40',
                'odds': {
                    JESSICA_AGUILAR: 146,
                    JODIE_ESQUIBEL: -165,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ELIAS_GARCIA,
                        'stats': '6-2-0',
                    },
                    {
                        'name': MARK_DE_LA_ROSA,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': MARK_DE_LA_ROSA,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:00',
                },
                'time': '17:00',
                'odds': {
                    MARK_DE_LA_ROSA: 117,
                    ELIAS_GARCIA: -132,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JENNIFER_MAIA,
                        'stats': '16-5-1',
                    },
                    {
                        'name': LIZ_CARMOUCHE,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': LIZ_CARMOUCHE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:10',
                'odds': {
                    LIZ_CARMOUCHE: -113,
                    JENNIFER_MAIA: 101,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RAONI_BARCELOS,
                        'stats': '13-1-0',
                    },
                    {
                        'name': KURT_HOLOBAUGH,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': RAONI_BARCELOS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:29',
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SAID_NURMAGOMEDOV,
                        'stats': '13-1-0',
                    },
                    {
                        'name': JUSTIN_SCOGGINS,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': SAID_NURMAGOMEDOV,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    SAID_NURMAGOMEDOV: -120,
                    JUSTIN_SCOGGINS: 107,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': DARREN_ELKINS,
                        'stats': '25-7-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    ALEXANDER_VOLKANOVSKI: -219,
                    DARREN_ELKINS: 192,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ALEJANDRO_PEREZ,
                        'stats': '22-7-1',
                    },
                    {
                        'name': EDDIE_WINELAND,
                        'stats': '23-13-1',
                    },
                ],
                'winner': {
                    'fighter': ALEJANDRO_PEREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    ALEJANDRO_PEREZ: -172,
                    EDDIE_WINELAND: 152,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARION_RENEAU,
                        'stats': '9-5-1',
                    },
                    {
                        'name': CAT_ZINGANO,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': CAT_ZINGANO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    CAT_ZINGANO: 101,
                    MARION_RENEAU: -114,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CHAD_MENDES,
                        'stats': '18-5-0',
                    },
                    {
                        'name': MYLES_JURY,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': CHAD_MENDES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:52',
                },
                'time': '23:00',
                'odds': {
                    CHAD_MENDES: -123,
                    MYLES_JURY: 109,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NIKO_PRICE,
                        'stats': '13-2-0',
                    },
                    {
                        'name': RANDY_BROWN,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': NIKO_PRICE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:09',
                },
                'time': '20:35',
                'odds': {
                    NIKO_PRICE: 112,
                    RANDY_BROWN: -126,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RICK_GLENN,
                        'stats': '21-6-1',
                    },
                    {
                        'name': DENNIS_BERMUDEZ,
                        'stats': '18-9-0',
                    },
                ],
                'winner': {
                    'fighter': RICK_GLENN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:00',
                'odds': {
                    RICK_GLENN: 158,
                    DENNIS_BERMUDEZ: -179,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ZAK_OTTOW,
                        'stats': '17-7-0',
                    },
                    {
                        'name': SAGE_NORTHCUTT,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': SAGE_NORTHCUTT,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:13',
                },
                'time': '23:30',
                'odds': {
                    SAGE_NORTHCUTT: -131,
                    ZAK_OTTOW: 116,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': BLAGOY_IVANOV,
                        'stats': '17-2-0',
                    },
                    {
                        'name': JUNIOR_DOS_SANTOS,
                        'stats': '21-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUNIOR_DOS_SANTOS,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '12:30',
                'odds': {
                    JUNIOR_DOS_SANTOS: -182,
                    BLAGOY_IVANOV: 161,
                },
            },
        ]
    },

    {
        'date': '2018-07-22',
        'name': 'UFC Fight Night',
        'location': 'Hamburg, Germany',
        'venue': 'Barclaycard Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LIU_PINGYUAN,
                        'stats': '13-5-0',
                    },
                    {
                        'name': DAMIAN_STASIAK,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': LIU_PINGYUAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '10:30',
                'odds': {
                    LIU_PINGYUAN: 119,
                    DAMIAN_STASIAK: -134,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DARKO_STOSIC,
                        'stats': '13-1-0',
                    },
                    {
                        'name': JEREMY_KIMBALL,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': DARKO_STOSIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:13',
                },
                'time': '11:00',
                'odds': {
                    DARKO_STOSIC: -249,
                    JEREMY_KIMBALL: 217,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MANNY_BERMUDEZ,
                        'stats': '14-0-0',
                    },
                    {
                        'name': DAVEY_GRANT,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': MANNY_BERMUDEZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '0:59',
                },
                'time': '11:30',
                'odds': {
                    MANNY_BERMUDEZ: -325,
                    DAVEY_GRANT: 278,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSANDAR_RAKIC,
                        'stats': '1-1-0',
                    },
                    {
                        'name': JUSTIN_LEDET,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSANDAR_RAKIC,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:00',
                'odds': {
                    ALEKSANDAR_RAKIC: -110,
                    JUSTIN_LEDET: -102,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': KHALID_TAHA,
                        'stats': '12-2-0',
                    },
                    {
                        'name': NAD_NARIMANI,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': NAD_NARIMANI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:30',
                'odds': {
                    NAD_NARIMANI: -203,
                    KHALID_TAHA: 178,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': EMIL_MEEK,
                        'stats': '9-4-1',
                    },
                    {
                        'name': BARTOSZ_FABINSKI,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': BARTOSZ_FABINSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '1:00',
                'odds': {
                    BARTOSZ_FABINSKI: 127,
                    EMIL_MEEK: -143,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAMIR_HADZOVIC,
                        'stats': '13-4-0',
                    },
                    {
                        'name': NICK_HEIN,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIR_HADZOVIC,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '1:30',
                'odds': {
                    DAMIR_HADZOVIC: 131,
                    NICK_HEIN: -148,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': NASRAT_HAQPARAST,
                        'stats': '10-2-0',
                    },
                    {
                        'name': MARC_DIAKIESE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': NASRAT_HAQPARAST,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:00',
                'odds': {
                    NASRAT_HAQPARAST: 152,
                    MARC_DIAKIESE: -172,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_ZAWADA,
                        'stats': '16-5-0',
                    },
                    {
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': DANNY_ROBERTS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:30',
                'odds': {
                    DANNY_ROBERTS: -214,
                    DAVID_ZAWADA: 188,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCIN_TYBURA,
                        'stats': '17-4-0',
                    },
                    {
                        'name': STEFAN_STRUVE,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': MARCIN_TYBURA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:00',
                'odds': {
                    MARCIN_TYBURA: -188,
                    STEFAN_STRUVE: 166,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ABU_AZAITAR,
                        'stats': '14-1-1',
                    },
                    {
                        'name': VITOR_MIRANDA,
                        'stats': '13-7-0',
                    },
                ],
                'winner': {
                    'fighter': ABU_AZAITAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:30',
                'odds': {
                    ABU_AZAITAR: -205,
                    VITOR_MIRANDA: 180,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': COREY_ANDERSON,
                        'stats': '13-4-0',
                    },
                    {
                        'name': GLOVER_TEIXEIRA,
                        'stats': '28-7-0',
                    },
                ],
                'winner': {
                    'fighter': COREY_ANDERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:00',
                'odds': {
                    COREY_ANDERSON: 111,
                    GLOVER_TEIXEIRA: -125,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': MAURICIO_RUA,
                        'stats': '26-11-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_SMITH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:29',
                },
                'time': '16:30',
                'odds': {
                    ANTHONY_SMITH: -158,
                    MAURICIO_RUA: 140,
                },
            },
        ]
    },

    {
        'date': '2018-07-28',
        'name': 'UFC Fight Night',
        'location': 'Calgary, Alberta',
        'venue': 'Scotiabank Saddledome',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DEVIN_POWELL,
                        'stats': '9-4-0',
                    },
                    {
                        'name': ALVARA_HERRERA,
                        'stats': '9-6-0',
                    },
                ],
                'winner': {
                    'fighter': DEVIN_POWELL,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:52',
                },
                'time': '16:00',
                'odds': {
                    DEVIN_POWELL: -101,
                    ALVARA_HERRERA: -111,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': RANDA_MARKOS,
                        'stats': '9-7-1',
                    },
                    {
                        'name': NINA_ANSAROFF,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': NINA_ANSAROFF,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:30',
                'odds': {
                    NINA_ANSAROFF: -141,
                    RANDA_MARKOS: 125,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MATHEUS_NICOLAU,
                        'stats': '13-3-1',
                    },
                    {
                        'name': DUSTIN_ORTIZ,
                        'stats': '19-8-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_ORTIZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:49',
                },
                'time': '17:00',
                'odds': {
                    DUSTIN_ORTIZ: 170,
                    MATHEUS_NICOLAU: -193,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ALEXIS_DAVIS,
                        'stats': '19-9-0',
                    },
                ],
                'winner': {
                    'fighter': KATLYN_CHOOKAGIAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:30',
                'odds': {
                    KATLYN_CHOOKAGIAN: -158,
                    ALEXIS_DAVIS: 140,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ROSS_PEARSON,
                        'stats': '22-16-0',
                    },
                    {
                        'name': JOHN_MAKDESSI,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_MAKDESSI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:30',
                'odds': {
                    JOHN_MAKDESSI: -223,
                    ROSS_PEARSON: 195,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GADZHIMURAD_ANTIGULOV,
                        'stats': '20-5-0',
                    },
                    {
                        'name': ION_CUTELABA,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': ION_CUTELABA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:25',
                },
                'time': '18:00',
                'odds': {
                    ION_CUTELABA: -135,
                    GADZHIMURAD_ANTIGULOV: 120,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ISLAM_MAKHACHEV,
                        'stats': '16-1-0',
                    },
                    {
                        'name': KAJAN_JOHNSON,
                        'stats': '23-14-1',
                    },
                ],
                'winner': {
                    'fighter': ISLAM_MAKHACHEV,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:43',
                },
                'time': '18:30',
                'odds': {
                    ISLAM_MAKHACHEV: -598,
                    KAJAN_JOHNSON: 480,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HAKEEM_DAWODU,
                        'stats': '9-0-1',
                    },
                    {
                        'name': AUSTIN_ARNETT,
                        'stats': '16-6-0',
                    },
                ],
                'winner': {
                    'fighter': HAKEEM_DAWODU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    HAKEEM_DAWODU: -485,
                    AUSTIN_ARNETT: 400,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_MORONO,
                        'stats': '16-5-0',
                    },
                    {
                        'name': JORDAN_MEIN,
                        'stats': '31-12-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_MEIN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    JORDAN_MEIN: -147,
                    ALEX_MORONO: 130,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_HERNANDEZ,
                        'stats': '10-2-0',
                    },
                    {
                        'name': OLIVIER_AUBIN_MERCIER,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_HERNANDEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    ALEXANDER_HERNANDEZ: -101,
                    OLIVIER_AUBIN_MERCIER: -111,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': TECIA_TORRES,
                        'stats': '10-4-0',
                    },
                    {
                        'name': JOANNA_JEDRZEJCZYK,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': JOANNA_JEDRZEJCZYK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    JOANNA_JEDRZEJCZYK: -315,
                    TECIA_TORRES: 270,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JEREMY_STEPHENS,
                        'stats': '28-16-0',
                    },
                    {
                        'name': JOSE_ALDO,
                        'stats': '28-4-0',
                    },
                ],
                'winner': {
                    'fighter': JOSE_ALDO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:19',
                },
                'time': '21:00',
                'odds': {
                    JOSE_ALDO: 105,
                    JEREMY_STEPHENS: -118,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': EDDIE_ALVAREZ,
                        'stats': '29-6-0',
                    },
                    {
                        'name': DUSTIN_POIRIER,
                        'stats': '24-5-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_POIRIER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:05',
                },
                'time': '21:30',
                'odds': {
                    DUSTIN_POIRIER: -150,
                    EDDIE_ALVAREZ: 133,
                },
            },
        ]
    },

    {
        'date': '2018-08-04',
        'name': 'UFC 227',
        'location': 'Los Angeles, California',
        'venue': 'Staples Center',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': WULIJI_BUREN,
                        'stats': '10-7-0',
                    },
                    {
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:53',
                },
                'time': '18:30',
                'odds': {
                    MARLON_VERA: -504,
                    WULIJI_BUREN: 390,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ZHANG_WEILI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': DANIELLE_TAYLOR,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': ZHANG_WEILI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    ZHANG_WEILI: -340,
                    DANIELLE_TAYLOR: 290,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOSE_TORRES,
                        'stats': '8-1-0',
                    },
                    {
                        'name': ALEX_PEREZ,
                        'stats': '22-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_PEREZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:36',
                },
                'time': '19:30',
                'odds': {
                    ALEX_PEREZ: -106,
                    JOSE_TORRES: -106,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MATT_SAYLES,
                        'stats': '6-2-0',
                    },
                    {
                        'name': SHEYMON_DA_SILVA_MORAES,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': SHEYMON_DA_SILVA_MORAES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    SHEYMON_DA_SILVA_MORAES: 117,
                    MATT_SAYLES: -132,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RICARDO_RAMOS,
                        'stats': '12-1-0',
                    },
                    {
                        'name': KYUNG_HO_KANG,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_RAMOS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    RICARDO_RAMOS: -284,
                    KYUNG_HO_KANG: 245,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MONTEL_JACKSON,
                        'stats': '7-1-0',
                    },
                    {
                        'name': RICKY_SIMON,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': RICKY_SIMON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    RICKY_SIMON: 109,
                    MONTEL_JACKSON: -123,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRETT_JOHNS,
                        'stats': 'u.dec',
                    },
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                ],
                'winner': {
                    'fighter': PEDRO_MUNHOZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    PEDRO_MUNHOZ: -211,
                    BRETT_JOHNS: 185,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_HOLLAND,
                        'stats': '15-4-0',
                    },
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    THIAGO_SANTOS: -353,
                    KEVIN_HOLLAND: 300,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': POLYANA_VIANA,
                        'stats': '10-3-0',
                    },
                    {
                        'name': JJ_ALDRICH,
                        'stats': '7-3-0',
                    },
                ],
                'winner': {
                    'fighter': JJ_ALDRICH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    JJ_ALDRICH: 133,
                    POLYANA_VIANA: -150,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RENATO_MOICANO,
                        'stats': '13-2-1',
                    },
                    {
                        'name': CUB_SWANSON,
                        'stats': '25-10-0',
                    },
                ],
                'winner': {
                    'fighter': RENATO_MOICANO,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:15',
                },
                'time': '23:00',
                'odds': {
                    RENATO_MOICANO: -302,
                    CUB_SWANSON: 260,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': HENRY_CEJUDO,
                        'stats': '14-2-0',
                    },
                    {
                        'name': DEMETRIOUS_JOHNSON,
                        'stats': '27-3-1',
                    },
                ],
                'winner': {
                    'fighter': HENRY_CEJUDO,
                    'by': 's.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    HENRY_CEJUDO: 395,
                    DEMETRIOUS_JOHNSON: -479,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CODY_GARBRANDT,
                        'stats': '11-3-0',
                    },
                    {
                        'name': TJ_DILLASHAW,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': TJ_DILLASHAW,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:10',
                },
                'time': '23:59',
                'odds': {
                    TJ_DILLASHAW: -128,
                    CODY_GARBRANDT: 114,
                },
            },
        ]
    },

    {
        'date': '2018-08-25',
        'name': 'UFC Fight Night',
        'location': 'Lincoln, Nebraska',
        'venue': 'Pinnacle Bank Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUKE_SANDERS,
                        'stats': '13-3-0',
                    },
                    {
                        'name': RANI_YAHYA,
                        'stats': '26-10-0',
                    },
                ],
                'winner': {
                    'fighter': RANI_YAHYA,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:31',
                },
                'time': '18:30',
                'odds': {
                    RANI_YAHYA: -106,
                    LUKE_SANDERS: -106,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JON_TUCK,
                        'stats': '10-5-0',
                    },
                    {
                        'name': DREW_DOBER,
                        'stats': '20-9-0',
                    },
                ],
                'winner': {
                    'fighter': DREW_DOBER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    DREW_DOBER: -235,
                    JON_TUCK: 205,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KALINDRA_FARIA,
                        'stats': '18-8-1',
                    },
                    {
                        'name': JOANNE_CALDERWOOD,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter':JOANNE_CALDERWOOD,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:57',
                },
                'time': '19:30',
                'odds': {
                    JOANNE_CALDERWOOD: -166,
                    KALINDRA_FARIA: 147,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICKEY_GALL,
                        'stats': '5-2-0',
                    },
                    {
                        'name': GEORGE_SULLIVAN,
                        'stats': '17-7-0',
                    },
                ],
                'winner': {
                    'fighter': MICKEY_GALL,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:09',
                },
                'time': '20:06',
                'odds': {
                    MICKEY_GALL: -321,
                    GEORGE_SULLIVAN: 275,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': MARKUS_PEREZ,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ANDREW_SANCHEZ,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANDREW_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    ANDREW_SANCHEZ: -140,
                    MARKUS_PEREZ: 124,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CORY_SANDHAGEN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': IURI_ALCANTARA,
                        'stats': '35-10-0',
                    },
                ],
                'winner': {
                    'fighter': CORY_SANDHAGEN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:01',
                },
                'time': '21:00',
                'odds': {
                    CORY_SANDHAGEN: -199,
                    IURI_ALCANTARA: 175,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': WARLLEY_ALVES,
                        'stats': '13-3-0',
                    },
                    {
                        'name': JAMES_KRAUSE,
                        'stats': '25-8-0',
                    },
                ],
                'winner': {
                    'fighter': JAMES_KRAUSE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:28',
                },
                'time': '21:30',
                'odds': {
                    JAMES_KRAUSE: 300,
                    WARLLEY_ALVES: -353,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TIM_WILLIAMS,
                        'stats': '15-5-0',
                    },
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': ERYK_ANDERS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:42',
                },
                'time': '22:00',
                'odds': {
                    ERYK_ANDERS: -1260,
                    TIM_WILLIAMS: 775,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': DEIVESON_FIGUEIREDO,
                        'stats': '15-1-0',
                    },
                    {
                        'name': JOHN_MORAGA,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': DEIVESON_FIGUEIREDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:08',
                },
                'time': '22:30',
                'odds': {
                    DEIVESON_FIGUEIREDO: -170,
                    JOHN_MORAGA: 150,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BRYAN_BARBERENA,
                        'stats': '14-6-0',
                    },
                    {
                        'name': JAKE_ELLENBERGER,
                        'stats': '31-15-0',
                    },
                ],
                'winner': {
                    'fighter': BRYAN_BARBERENA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:26',
                },
                'time': '23:00',
                'odds': {
                    BRYAN_BARBERENA: -485,
                    JAKE_ELLENBERGER: 400,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CORTNEY_CASEY_SANCHEZ,
                        'stats': '8-6-0',
                    },
                    {
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                ],
                'winner': {
                    'fighter': CORTNEY_CASEY_SANCHEZ,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    CORTNEY_CASEY_SANCHEZ: 110,
                    ANGELA_HILL: -124,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_JOHNSON,
                        'stats': '20-14-0',
                    },
                    {
                        'name': ANDRE_FILI,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAEL_JOHNSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    MICHAEL_JOHNSON: 101,
                    ANDRE_FILI: -114,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_GAETHJE,
                        'stats': '20-2-0',
                    },
                    {
                        'name': JAMES_VICK,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_GAETHJE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:27',
                },
                'time': '23:59',
                'odds': {
                    JUSTIN_GAETHJE: 121,
                    JAMES_VICK: -136,
                },
            },
        ]
    },

    {
        'date': '2018-09-08',
        'name': 'UFC 228',
        'location': 'Dallas, Texas',
        'venue': 'American Airlines Center',
        'fights': [
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ROBERTO_SANCHEZ,
                        'stats': '8-2-0',
                    },
                    {
                        'name': JARRED_BROOKS,
                        'stats': '14-2-0',
                    },
                ],
                'winner': {
                    'fighter': JARRED_BROOKS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:10',
                'odds': {
                    JARRED_BROOKS: -270,
                    ROBERTO_SANCHEZ: 234,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUCIE_PUDILOVA,
                        'stats': '8-4-0',
                    },
                    {
                        'name': IRENE_ALDANA,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': IRENE_ALDANA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:40',
                'odds': {
                    IRENE_ALDANA: -102,
                    LUCIE_PUDILOVA: -110,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_WHITE,
                        'stats': '13-5-0',
                    },
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': JIM_MILLER,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:29',
                },
                'time': '19:20',
                'odds': {
                    JIM_MILLER: 151,
                    ALEX_WHITE: -171,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CRAIG_WHITE,
                        'stats': '14-9-0',
                    },
                    {
                        'name': DIEGO_SANCHEZ,
                        'stats': '31-11-0',
                    },
                ],
                'winner': {
                    'fighter': DIEGO_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    DIEGO_SANCHEZ: 180,
                    CRAIG_WHITE: -205,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_BYRD,
                        'stats': '10-6-0',
                    },
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_STEWART,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:17',
                },
                'time': '20:00',
                'odds': {
                    DARREN_STEWART: 163,
                    CHARLES_BYRD: -185,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GEOFF_NEAL,
                        'stats': '11-2-0',
                    },
                    {
                        'name': FRANK_CAMACHO,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': GEOFF_NEAL,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:23',
                },
                'time': '20:30',
                'odds': {
                    GEOFF_NEAL: -217,
                    FRANK_CAMACHO: 190,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CODY_STAMANN,
                        'stats': '18-2-0',
                    },
                    {
                        'name': ALJAMAIN_STERLING,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALJAMAIN_STERLING,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:42',
                },
                'time': '21:00',
                'odds': {
                    ALJAMAIN_STERLING: -176,
                    CODY_STAMANN: 155,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': TATIANA_SUAREZ,
                        'stats': '7-0-0',
                    },
                    {
                        'name': CARLA_ESPARZA,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': TATIANA_SUAREZ,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:33',
                },
                'time': '21:30',
                'odds': {
                    TATIANA_SUAREZ: -415,
                    CARLA_ESPARZA: 330,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NIKO_PRICE,
                        'stats': '13-2-0',
                    },
                    {
                        'name': ABDUL_RAZAK_ALHASSAN,
                        'stats': '10-1-0',
                    },
                ],
                'winner': {
                    'fighter': ABDUL_RAZAK_ALHASSAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:43',
                },
                'time': '22:00',
                'odds': {
                    ABDUL_RAZAK_ALHASSAN: 100,
                    NIKO_PRICE: -112,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JIMMIE_RIVERA,
                        'stats': '22-3-0',
                    },
                    {
                        'name': JOHN_DODSON,
                        'stats': '21-11-0',
                    },
                ],
                'winner': {
                    'fighter': JIMMIE_RIVERA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    JIMMIE_RIVERA: -147,
                    JOHN_DODSON: 130,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ZABIT_MAGOMEDSHARIPOV,
                        'stats': '17-1-0',
                    },
                    {
                        'name': BRANDON_DAVIS,
                        'stats': '9-5-0',
                    },
                ],
                'winner': {
                    'fighter': ZABIT_MAGOMEDSHARIPOV,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:46',
                },
                'time': '23:00',
                'odds': {
                    ZABIT_MAGOMEDSHARIPOV: -1449,
                    BRANDON_DAVIS: 917,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': KAROLINA_KOWALKIEWICZ,
                        'stats': '13-4-0',
                    },
                    {
                        'name': JESSICA_ANDRADE,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ANDRADE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:58',
                },
                'time': '23:30',
                'odds': {
                    JESSICA_ANDRADE: -452,
                    KAROLINA_KOWALKIEWICZ: 355,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_TILL,
                        'stats': '17-2-1',
                    },
                    {
                        'name': TYRON_WOODLEY,
                        'stats': '19-4-1',
                    },
                ],
                'winner': {
                    'fighter': TYRON_WOODLEY,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:19',
                },
                'time': '23:59',
                'odds': {
                    TYRON_WOODLEY: -106,
                    DARREN_TILL: -106,
                },
            },
        ]
    },

    {
        'date': '2018-09-22',
        'name': 'UFC Fight Night',
        'location': 'Sao Paulo, Brazil',
        'venue': 'Ginasio do Ibirapuera',
        'fights': [
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': LIVINHA_SOUZA,
                        'stats': '12-1-0',
                    },
                    {
                        'name': ALEX_CHAMBERS,
                        'stats': '5-4-0',
                    },
                ],
                'winner': {
                    'fighter': LIVINHA_SOUZA,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:21',
                },
                'time': '18:30',
                'odds': {
                    LIVINHA_SOUZA: -1717,
                    ALEX_CHAMBERS: 944,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LUIGI_VENDRAMINI,
                        'stats': '8-0-0',
                    },
                    {
                        'name': ELIZEU_ZALESKI_DOS_SANTOS,
                        'stats': '20-5-0',
                    },
                ],
                'winner': {
                    'fighter': ELIZEU_ZALESKI_DOS_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:20',
                },
                'time': '19:00',
                'odds': {
                    ELIZEU_ZALESKI_DOS_SANTOS: -1200,
                    LUIGI_VENDRAMINI: 843,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': HECTOR_LOMBARD,
                        'stats': '34-9-1',
                    },
                    {
                        'name': THALES_LEITES,
                        'stats': '28-9-0',
                    },
                ],
                'winner': {
                    'fighter': THALES_LEITES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    THALES_LEITES: -158,
                    HECTOR_LOMBARD: 140,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MAYRA_BUENO_SILVA,
                        'stats': '6-0-0',
                    },
                    {
                        'name': GILLIAN_ROBERTSON,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAYRA_BUENO_SILVA,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:55',
                },
                'time': '19:50',
                'odds': {
                    MAYRA_BUENO_SILVA: 120,
                    GILLIAN_ROBERTSON: -135,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                    {
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                ],
                'winner': {
                    'fighter': SERGIO_MORAES,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:42',
                },
                'time': '20:10',
                'odds': {
                    SERGIO_MORAES: -259,
                    BEN_SAUNDERS: 225,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': AUGUSTO_SAKAI,
                        'stats': '12-1-1',
                    },
                    {
                        'name': CHASE_SHERMAN,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': AUGUSTO_SAKAI,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:03',
                },
                'time': '20:30',
                'odds': {
                    AUGUSTO_SAKAI: -235,
                    CHASE_SHERMAN: 205,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_SPANN,
                        'stats': '15-5-0',
                    },
                    {
                        'name': LUIS_HENRIQUE,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_SPANN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    RYAN_SPANN: -110,
                    LUIS_HENRIQUE: -102,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FRANCISCO_TRINALDO,
                        'stats': '23-6-0',
                    },
                    {
                        'name': EVAN_DUNHAM,
                        'stats': '18-7-1',
                    },
                ],
                'winner': {
                    'fighter': FRANCISCO_TRINALDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:10',
                },
                'time': '21:30',
                'odds': {
                    FRANCISCO_TRINALDO: -170,
                    EVAN_DUNHAM: 150,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHRISTOS_GIAGOS,
                        'stats': '16-7-0',
                    },
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:22',
                },
                'time': '22:00',
                'odds': {
                    CHARLES_OLIVEIRA: -504,
                    CHRISTOS_GIAGOS: 390,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MARINA_RODRIGUEZ,
                        'stats': '11-0-1',
                    },
                    {
                        'name': RANDA_MARKOS,
                        'stats': '9-7-1',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    RANDA_MARKOS: 117,
                    MARINA_RODRIGUEZ: -132,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_EWELL,
                        'stats': '13-5-0',
                    },
                    {
                        'name': RENAN_BARAO,
                        'stats': '36-8-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_EWELL,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    ANDRE_EWELL: 175,
                    RENAN_BARAO: -199,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
                    },
                    {
                        'name': ROGERIO_NOGUEIRA,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': ROGERIO_NOGUEIRA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:00',
                },
                'time': '23:30',
                'odds': {
                    ROGERIO_NOGUEIRA: 290,
                    SAM_ALVEY: -340,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CARLO_PEDERSOLI_JR,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ALEX_OLIVEIRA,
                        'stats': '19-6-1',
                    },
                ],
                'winner': {
                    'fighter': ALEX_OLIVEIRA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:39',
                },
                'time': '23:59',
                'odds': {
                    ALEX_OLIVEIRA: -535,
                    CARLO_PEDERSOLI_JR: 410,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    THIAGO_SANTOS: -199,
                    ERYK_ANDERS: 175,
                },
            },
        ]
    },

    {
        'date': '2018-10-06',
        'name': 'UFC 229',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                    {
                        'name': RYAN_LAFLARE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_ROCCO_MARTIN,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:00',
                },
                'time': '18:15',
                'odds': {
                    ANTHONY_ROCCO_MARTIN: 110,
                    RYAN_LAFLARE: -124,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GRAY_MAYNARD,
                        'stats': '14-8-1',
                    },
                    {
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                ],
                'winner': {
                    'fighter': NIK_LENTZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:19',
                },
                'time': '18:45',
                'odds': {
                    NIK_LENTZ: -247,
                    GRAY_MAYNARD: 215,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': YANA_KUNITSKAYA,
                        'stats': '12-4-0',
                    },
                    {
                        'name': LINA_LANSBERG,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': YANA_KUNITSKAYA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    YANA_KUNITSKAYA: -265,
                    LINA_LANSBERG: 230,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SCOTT_HOLTZMAN,
                        'stats': '12-3-0',
                    },
                    {
                        'name': ALAN_PATRICK,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': SCOTT_HOLTZMAN,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:42',
                },
                'time': '19:15',
                'odds': {
                    SCOTT_HOLTZMAN: 270,
                    ALAN_PATRICK: -315,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ASPEN_LADD,
                        'stats': '7-0-0',
                    },
                    {
                        'name': TONYA_EVINGER,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': ASPEN_LADD,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:26',
                },
                'time': '20:00',
                'odds': {
                    ASPEN_LADD: -185,
                    TONYA_EVINGER: 163,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JALIN_TURNER,
                        'stats': '8-4-0',
                    },
                    {
                        'name': VICENTE_LUQUE,
                        'stats': '15-6-1',
                    },
                ],
                'winner': {
                    'fighter': VICENTE_LUQUE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:52',
                },
                'time': '21:00',
                'odds': {
                    VICENTE_LUQUE: -630,
                    JALIN_TURNER: 470,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SERGIO_PETTIS,
                        'stats': '17-5-0',
                    },
                    {
                        'name': JUSSIER_FORMIGA,
                        'stats': '23-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUSSIER_FORMIGA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:40',
                'odds': {
                    JUSSIER_FORMIGA: 170,
                    SERGIO_PETTIS: -193,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': FELICE_HERRIG,
                        'stats': '14-8-0',
                    },
                    {
                        'name': MICHELLE_WATERSON,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': MICHELLE_WATERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:05',
                'odds': {
                    MICHELLE_WATERSON: 116,
                    FELICE_HERRIG: -131,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKOV,
                        'stats': '30-7-0',
                    },
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': DERRICK_LEWIS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:49',
                },
                'time': '22:30',
                'odds': {
                    DERRICK_LEWIS: 131,
                    ALEXANDER_VOLKOV: -148,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DOMINICK_REYES,
                        'stats': '11-0-0',
                    },
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '23-12-0',
                    },
                ],
                'winner': {
                    'fighter': DOMINICK_REYES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    DOMINICK_REYES: -217,
                    OVINCE_SAINT_PREUX: 190,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_PETTIS,
                        'stats': '22-8-0',
                    },
                    {
                        'name': TONY_FERGUSON,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': TONY_FERGUSON,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    TONY_FERGUSON: -345,
                    ANTHONY_PETTIS: 280,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KHABIB_NURMAGOMEDIV,
                        'stats': '27-0-0',
                    },
                    {
                        'name': CONOR_MCGREGOR,
                        'stats': '21-4-0',
                    },
                ],
                'winner': {
                    'fighter': KHABIB_NURMAGOMEDIV,
                    'by': 'submission',
                    'round': 4,
                    'time': '3:03',
                },
                'time': '23:59',
                'odds': {
                    KHABIB_NURMAGOMEDIV: -192,
                    CONOR_MCGREGOR: 169,
                },
            },
        ]
    },

    {
        'date': '2018-11-03',
        'name': 'UFC 230',
        'location': 'New York City, New York',
        'venue': 'Madison Square Garden',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ADAM_WIECZOREK,
                        'stats': '10-2-0',
                    },
                    {
                        'name': MARCOS_ROGERIO_DE_LIMA,
                        'stats': '16-7-1',
                    },
                ],
                'winner': {
                    'fighter': MARCOS_ROGERIO_DE_LIMA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:15',
                'odds': {
                    MARCOS_ROGERIO_DE_LIMA: 147,
                    ADAM_WIECZOREK: -166,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHANE_BURGOS,
                        'stats': '11-1-0',
                    },
                    {
                        'name': KURT_HOLOBAUGH,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': SHANE_BURGOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:11',
                },
                'time': '19:00',
                'odds': {
                    SHANE_BURGOS: -423,
                    KURT_HOLOBAUGH: 335,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MATT_FREVOLA,
                        'stats': '6-1-1',
                    },
                    {
                        'name': LANDO_VANNATA,
                        'stats': '10-3-2',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': None,
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    LANDO_VANNATA: -223,
                    MATT_FREVOLA: 195,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LYMAN_GOOD,
                        'stats': '20-5-0',
                    },
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                ],
                'winner': {
                    'fighter': LYMAN_GOOD,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:32',
                },
                'time': '20:00',
                'odds': {
                    LYMAN_GOOD: -265,
                    BEN_SAUNDERS: 230,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHEYMON_DA_SILVA_MORAES,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JULIO_ACRE,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': SHEYMON_DA_SILVA_MORAES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    SHEYMON_DA_SILVA_MORAES: 215,
                    JULIO_ACRE: -247,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SIJARA_EUBANKS,
                        'stats': '5-2-0',
                    },
                    {
                        'name': ROXANNE_MODAFFERI,
                        'stats': '3-3-0',
                    },
                ],
                'winner': {
                    'fighter': SIJARA_EUBANKS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    SIJARA_EUBANKS: -583,
                    ROXANNE_MODAFFERI: 455,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_RINALDI,
                        'stats': '14-7-0',
                    },
                    {
                        'name': JASON_KNIGHT,
                        'stats': '20-6-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_RINALDI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    JORDAN_RINALDI: 260,
                    JASON_KNIGHT: -302,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ISRAEL_ADESANYA,
                        'stats': '16-0-0',
                    },
                    {
                        'name': DEREK_BRUNSON,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': ISRAEL_ADESANYA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:51',
                },
                'time': '22:00',
                'odds': {
                    ISRAEL_ADESANYA: -272,
                    DEREK_BRUNSON: 236,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KARL_ROBERSON,
                        'stats': '7-2-0',
                    },
                    {
                        'name': JACK_MARSHMAN,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': KARL_ROBERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    KARL_ROBERSON: -321,
                    JACK_MARSHMAN: 275,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JARED_CANNONIER,
                        'stats': '11-4-0',
                    },
                    {
                        'name': DAVID_BRANCH,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': JARED_CANNONIER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:39',
                },
                'time': '23:00',
                'odds': {
                    JARED_CANNONIER: 280,
                    DAVID_BRANCH: -327,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_WEIDMAN,
                        'stats': '14-4-0',
                    },
                    {
                        'name': JACARE_SOUZA,
                        'stats': '26-6-0',
                    },
                ],
                'winner': {
                    'fighter': JACARE_SOUZA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:46',
                },
                'time': '23:30',
                'odds': {
                    JACARE_SOUZA: 145,
                    CHRIS_WEIDMAN: -164,
                },
            },
            {
                'weight_class': DERRICK_LEWIS,
                'fighters': [
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                    {
                        'name': DANIEL_CORMIER,
                        'stats': '22-1-0',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_CORMIER,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:14',
                },
                'time': '23:59',
                'odds': {
                    DANIEL_CORMIER: -426,
                    DERRICK_LEWIS: 356,
                },
            },
        ]
    },

    {
        'date': '2018-11-10',
        'name': 'UFC Fight Night',
        'location': 'Denver, Colorado',
        'venue': 'Pepsi Center',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARK_DE_LA_ROSA,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JOBY_SANCHEZ,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': MARK_DE_LA_ROSA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    MARK_DE_LA_ROSA: -253,
                    JOBY_SANCHEZ: 220,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOSEPH_MORALES,
                        'stats': '9-2-0',
                    },
                    {
                        'name': ERIC_SHELTON,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': ERIC_SHELTON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ERIC_SHELTON: -147,
                    JOSEPH_MORALES: 130,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DEVONTE_SMITH,
                        'stats': '10-1-0',
                    },
                    {
                        'name': JULIAN_EROSA,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': DEVONTE_SMITH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:46',
                },
                'time': '20:00',
                'odds': {
                    DEVONTE_SMITH: -241,
                    JULIAN_EROSA: 210,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOHN_GUNTHER,
                        'stats': '7-2-0',
                    },
                    {
                        'name': DAVI_RAMOS,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAVI_RAMOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:57',
                },
                'time': '20:30',
                'odds': {
                    DAVI_RAMOS: -1101,
                    JOHN_GUNTHER: 722,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BOBBY_MOFFETT,
                        'stats': '13-4-0',
                    },
                    {
                        'name': CHAS_SKELLY,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': BOBBY_MOFFETT,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:43',
                },
                'time': '21:00',
                'odds': {
                    BOBBY_MOFFETT: -118,
                    CHAS_SKELLY: 105,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ASHLEY_YODER,
                        'stats': '6-4-0',
                    },
                    {
                        'name': AMANDA_COOPER,
                        'stats': '4-5-0',
                    },
                ],
                'winner': {
                    'fighter': ASHLEY_YODER,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    ASHLEY_YODER: -139,
                    AMANDA_COOPER: 123,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_TRIZANO,
                        'stats': '9-0-0',
                    },
                    {
                        'name': LUIS_PENA,
                        'stats': '6-1-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAEL_TRIZANO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    MICHAEL_TRIZANO: 149,
                    LUIS_PENA: -169,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': HANNA_CIFERS,
                        'stats': '9-3-0',
                    },
                    {
                        'name': MAYCEE_BARBER,
                        'stats': '5-0-0',
                    },
                ],
                'winner': {
                    'fighter': MAYCEE_BARBER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:01',
                },
                'time': '22:30',
                'odds': {
                    MAYCEE_BARBER: -474,
                    HANNA_CIFERS: 375,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': THIAGO_MOISES,
                        'stats': '11-3-0',
                    },
                    {
                        'name': BENEIL_DARIUSH,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': BENEIL_DARIUSH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    BENEIL_DARIUSH: -157,
                    THIAGO_MOISES: 139,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RAQUEL_PENNINGTON,
                        'stats': '9-8-0',
                    },
                    {
                        'name': GERMAINE_DE_RANDAMIE,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': GERMAINE_DE_RANDAMIE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    GERMAINE_DE_RANDAMIE: -205,
                    RAQUEL_PENNINGTON: 180,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_PERRY,
                        'stats': '12-4-0',
                    },
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                ],
                'winner': {
                    'fighter': DONALD_CERRONE,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:46',
                },
                'time': '23:53',
                'odds': {
                    DONALD_CERRONE: 180,
                    MIKE_PERRY: -205,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': YAIR_RODRIGUEZ,
                        'stats': '12-2-0',
                    },
                    {
                        'name': CHAN_SUNG_JUNG,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': YAIR_RODRIGUEZ,
                    'by': 'ko/tko',
                    'round': 5,
                    'time': '4:59',
                },
                'time': '23:59',
                'odds': {
                    YAIR_RODRIGUEZ: -131,
                    CHAN_SUNG_JUNG: 116,
                },
            },
        ]
    },

    {
        'date': '2018-11-17',
        'name': 'UFC Fight Night',
        'location': 'Beunos Aires, Argentina',
        'venue': 'Parque Roca Arena',
        'fights': [
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': NAD_NARIMANI,
                        'stats': '12-3-0',
                    },
                    {
                        'name': ANDERSON_DOS_SANTOS,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': NAD_NARIMANI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    NAD_NARIMANI: -398,
                    ANDERSON_DOS_SANTOS: 335,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JESUS_PINEDO,
                        'stats': '16-5-1',
                    },
                    {
                        'name': DEVIN_POWELL,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': JESUS_PINEDO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    JESUS_PINEDO: -241,
                    DEVIN_POWELL: 210,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LAUREANO_STAROPOLI,
                        'stats': '8-1-0',
                    },
                    {
                        'name': HECTOR_ALDANA,
                        'stats': '4-3-0',
                    },
                ],
                'winner': {
                    'fighter': LAUREANO_STAROPOLI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    LAUREANO_STAROPOLI: 111,
                    HECTOR_ALDANA: -125,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': AUSTIN_ARNETT,
                        'stats': '16-6-0',
                    },
                    {
                        'name': HUMBERTO_BANDENAY,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': AUSTIN_ARNETT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    AUSTIN_ARNETT: 199,
                    HUMBERTO_BANDENAY: -228,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDRE_PANTOJA,
                        'stats': '20-3-0',
                    },
                    {
                        'name': ULKA_SASAKI,
                        'stats': '21-6-2',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDRE_PANTOJA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:18',
                },
                'time': '20:30',
                'odds': {
                    ALEXANDRE_PANTOJA: -302,
                    ULKA_SASAKI: 260,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BARTOSZ_FABINSKI,
                        'stats': '14-3-0',
                    },
                    {
                        'name': MICHEL_PRAZERES,
                        'stats': '26-3-0',
                    },
                ],
                'winner': {
                    'fighter': MICHEL_PRAZERES,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:02',
                },
                'time': '21:00',
                'odds': {
                    MICHEL_PRAZERES: -156,
                    BARTOSZ_FABINSKI: 138,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CYNTHIA_CALVILLO,
                        'stats': '8-1-0',
                    },
                    {
                        'name': POLIANA_BOTELHO,
                        'stats': '7-2-0',
                    },
                ],
                'winner': {
                    'fighter': CYNTHIA_CALVILLO,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:48',
                },
                'time': '22:00',
                'odds': {
                    CYNTHIA_CALVILLO: 165,
                    POLIANA_BOTELHO: -187,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                    {
                        'name': GUIDO_CANNETTI,
                        'stats': '8-5-0',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:31',
                },
                'time': '22:30',
                'odds': {
                    MARLON_VERA: -315,
                    GUIDO_CANNETTI: 270,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': IAN_HEINISCH,
                        'stats': '12-1-0',
                    },
                    {
                        'name': CEZAR_FERREIRA,
                        'stats': '14-7-0',
                    },
                ],
                'winner': {
                    'fighter': IAN_HEINISCH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    IAN_HEINISCH: 167,
                    CEZAR_FERREIRA: -190,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JOHNNY_WALKER,
                        'stats': '17-3-0',
                    },
                    {
                        'name': KHALIL_ROUNTREE,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOHNNY_WALKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:57',
                },
                'time': '23:31',
                'odds': {
                    JOHNNY_WALKER: 130,
                    KHALIL_ROUNTREE: -147,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RICARDO_LAMAS,
                        'stats': '19-7-0',
                    },
                    {
                        'name': DARREN_ELKINS,
                        'stats': '25-7-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_LAMAS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:09',
                },
                'time': '23:55',
                'odds': {
                    RICARDO_LAMAS: -190,
                    DARREN_ELKINS: 167,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SANTIAGO_PONZINIBBIO,
                        'stats': '28-3-0',
                    },
                    {
                        'name': NEIL_MAGNY,
                        'stats': '21-8-0',
                    },
                ],
                'winner': {
                    'fighter': SANTIAGO_PONZINIBBIO,
                    'by': 'ko/tko',
                    'round': 4,
                    'time': '2:36',
                },
                'time': '23:59',
                'odds': {
                    SANTIAGO_PONZINIBBIO: -217,
                    NEIL_MAGNY: 190,
                },
            },
        ]
    },

    {
        'date': '2018-11-24',
        'name': 'UFC Fight Night',
        'location': 'Beijing, China',
        'venue': 'Cadillac Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LOUIS_SMOLKA,
                        'stats': '15-6-0',
                    },
                    {
                        'name': SU_MUDAERJI,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': LOUIS_SMOLKA,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:07',
                },
                'time': '3:30',
                'odds': {
                    LOUIS_SMOLKA: -165,
                    SU_MUDAERJI: 146,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_HOLLAND,
                        'stats': '15-4-0',
                    },
                    {
                        'name': JOHN_PHILLIPS,
                        'stats': '21-9-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_HOLLAND,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:05',
                },
                'time': '4:00',
                'odds': {
                    KEVIN_HOLLAND: -581,
                    JOHN_PHILLIPS: 440,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': YAN_XIAONAN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': SYURI_KONDO,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': YAN_XIAONAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '4:30',
                'odds': {
                    YAN_XIAONAN: -420,
                    SYURI_KONDO: 333,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LIU_PINGYUAN,
                        'stats': '13-5-0',
                    },
                    {
                        'name': MARTIN_DAY,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': LIU_PINGYUAN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '5:00',
                'odds': {
                    LIU_PINGYUAN: -180,
                    MARTIN_DAY: 159,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ZHANG_WEILI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': JESSICA_AGUILAR,
                        'stats': '20-8-0',
                    },
                ],
                'winner': {
                    'fighter': ZHANG_WEILI,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:41',
                },
                'time': '5:30',
                'odds': {
                    ZHANG_WEILI: -624,
                    JESSICA_AGUILAR: 466,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': HU_YAOZONG,
                        'stats': '3-2-0',
                    },
                    {
                        'name': RASHAD_COULTER,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': RASHAD_COULTER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '6:00',
                'odds': {
                    RASHAD_COULTER: 100,
                    HU_YAOZONG: -112,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': WU_YANAN,
                        'stats': '10-2-0',
                    },
                    {
                        'name': LAUREN_MUELLER,
                        'stats': '5-1-0',
                    },
                ],
                'winner': {
                    'fighter': WU_YANAN,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:00',
                },
                'time': '6:30',
                'odds': {
                    WU_YANAN: 284,
                    LAUREN_MUELLER: -350,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SONG_KENAN,
                        'stats': '13-5-0',
                    },
                    {
                        'name': ALEX_MORONO,
                        'stats': '16-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_MORONO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    ALEX_MORONO: 123,
                    SONG_KENAN: -138,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_ZAWADA,
                        'stats': '16-5-0',
                    },
                    {
                        'name': LI_JINGLIANG,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': LI_JINGLIANG,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:07',
                },
                'time': '19:30',
                'odds': {
                    LI_JINGLIANG: -208,
                    DAVID_ZAWADA: 183,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': VINCE_MORALES,
                        'stats': '0-0-0',
                    },
                    {
                        'name': SONG_YADONG,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': SONG_YADONG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    SONG_YADONG: -560,
                    VINCE_MORALES: 426,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SERGEI_PAVLOVICH,
                        'stats': '12-1-0',
                    },
                    {
                        'name': ALISTAIR_OVEREEM,
                        'stats': '44-17-0',
                    },
                ],
                'winner': {
                    'fighter': ALISTAIR_OVEREEM,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:21',
                },
                'time': '20:30',
                'odds': {
                    ALISTAIR_OVEREEM: 113,
                    SERGEI_PAVLOVICH: -127,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_BLAYDES,
                        'stats': '11-2-0',
                    },
                    {
                        'name': FRANCIS_NGANNOU,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCIS_NGANNOU,
                    'by': 'kko/tko',
                    'round': 1,
                    'time': '0:45',
                },
                'time': '20:59',
                'odds': {
                    FRANCIS_NGANNOU: 189,
                    CURTIS_BLAYDES: -216,
                },
            },
        ]
    },

    {
        'date': '2018-11-30',
        'name': 'UFC - TUF 28 Finale',
        'location': 'Las Vegas, Nevada',
        'venue': 'Pearl Concert Theater',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_GUTIERREZ,
                        'stats': '12-3-0',
                    },
                    {
                        'name': RAONI_BARCELOS,
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': RAONI_BARCELOS,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:12',
                },
                'time': '20:30',
                'odds': {
                    RAONI_BARCELOS: -504,
                    CHRIS_GUTIERREZ: 390,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': RICKEY_RAINEY,
                        'stats': '13-6-0',
                    },
                    {
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                ],
                'winner': {
                    'fighter': TIM_MEANS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:18',
                },
                'time': '21:00',
                'odds': {
                    TIM_MEANS: -373,
                    RICKEY_RAINEY: 300,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ROOSEVELT_ROBERTS,
                        'stats': '7-0-0',
                    },
                    {
                        'name': DARRELL_HORCHER,
                        'status': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': ROOSEVELT_ROBERTS,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:50',
                },
                'time': '21:30',
                'odds': {
                    ROOSEVELT_ROBERTS: -345,
                    DARRELL_HORCHER: 280,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': LEAH_LETSON,
                        'stats': '4-2-0',
                    },
                    {
                        'name': JULIJA_STOLIARENKO,
                        'stats': '4-3-1',
                    },
                ],
                'winner': {
                    'fighter': LEAH_LETSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MICHEL_BATISTA,
                        'stats': '4-1-0',
                    },
                    {
                        'name': MAURICE_GREEN,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAURICE_GREEN,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:14',
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_PEREZ,
                        'stats': '22-5-0',
                    },
                    {
                        'name': JOSEPH_BENAVIDEZ,
                        'stats': '27-5-0',
                    },
                ],
                'winner': {
                    'fighter': JOSEPH_BENAVIDEZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:19',
                },
                'time': '22:00',
                'odds': {
                    JOSEPH_BENAVIDEZ: 101,
                    ALEX_PEREZ: -114,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_AGUILAR,
                        'stats': '0-0-0',
                    },
                    {
                        'name': RICK_GLENN,
                        'stats': '21-6-1',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_AGUILAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    KEVIN_AGUILAR: 110,
                    RICK_GLENN: -124,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANTONINA_SHEVCHENKO,
                        'stats': '7-0-0',
                    },
                    {
                        'name': JI_YEAN_KIM,
                        'stats': '7-2-2',
                    },
                ],
                'winner': {
                    'fighter': ANTONINA_SHEVCHENKO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    ANTONINA_SHEVCHENKO: -271,
                    JI_YEAN_KIM: 235,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': EDMEN_SHAHBAZYAN,
                        'stats': '9-0-0',
                    },
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': EDMEN_SHAHBAZYAN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    EDMEN_SHAHBAZYAN: -113,
                    DARREN_STEWART: 101,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                    {
                        'name': BRYAN_CARAWAY,
                        'stats': '21-10-0',
                    },
                ],
                'winner': {
                    'fighter': PEDRO_MUNHOZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:39',
                },
                'time': '23:50',
                'odds': {
                    PEDRO_MUNHOZ: -296,
                    BRYAN_CARAWAY: 255,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MACY_CHIASSON,
                        'stats': '5-0-0',
                    },
                    {
                        'name': PANNIE_KIANZAD,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': MACY_CHIASSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:11',
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_FRAZIER,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JUAN_ESPINO,
                        'stats': '9-1-0',
                    },
                ],
                'winner': {
                    'fighter': JUAN_ESPINO,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:36',
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KAMARU_USMAN,
                        'stats': '15-1-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': KAMARU_USMAN,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    KAMARU_USMAN: -315,
                    RAFAEL_DOS_ANJOS: 270,
                },
            },
        ]
    },

    {
        'date': '2018-12-01',
        'name': 'UFC Fight Night',
        'location': 'Adelaide, Australia',
        'venue': 'Adelaide Entertainment Centre',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAMIR_ISMAGULOV,
                        'stats': '17-2-0',
                    },
                    {
                        'name': ALEX_GORGEES,
                        'stats': '6-0-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIR_ISMAGULOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    DAMIR_ISMAGULOV: -550,
                    ALEX_GORGEES: 420,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHRISTOS_GIAGOS,
                        'stats': '16-7-0',
                    },
                    {
                        'name': MIZUTO_HIROTA,
                        'stats': '19-10-2',
                    },
                ],
                'winner': {
                    'fighter': CHRISTOS_GIAGOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    CHRISTOS_GIAGOS: -394,
                    MIZUTO_HIROTA: 315,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KAI_KARA_FRANCE,
                        'stats': '19-7-0',
                    },
                    {
                        'name': ELIAS_GARCIA,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': KAI_KARA_FRANCE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    KAI_KARA_FRANCE: -385,
                    ELIAS_GARCIA: 325,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SALIM_TOUAHRI,
                        'stats': '10-3-0',
                    },
                    {
                        'name': KEITA_NAKAMURA,
                        'stats': '34-9-2',
                    },
                ],
                'winner': {
                    'fighter': KEITA_NAKAMURA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    KEITA_NAKAMURA: -149,
                    SALIM_TOUAHRI: 132,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': BEN_NGUYEN,
                        'stats': '17-8-0',
                    },
                    {
                        'name': WILSON_REIS,
                        'stats': '23-9-0',
                    },
                ],
                'winner': {
                    'fighter': WILSON_REIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    WILSON_REIS: 135,
                    BEN_NGUYEN: -152,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSEI_KUNCHENKO,
                        'stats': '20-0-0',
                    },
                    {
                        'name': YUSHIN_OKAMI,
                        'stats': '34-13-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSEI_KUNCHENKO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    ALEKSEI_KUNCHENKO: -285,
                    YUSHIN_OKAMI: 235,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JIMMY_CRUTE,
                        'stats': '10-0-0',
                    },
                    {
                        'name': PAUL_CRAIG,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': JIMMY_CRUTE,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:51',
                },
                'time': '22:00',
                'odds': {
                    JIMMY_CRUTE: -302,
                    PAUL_CRAIG: 260,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SODIQ_YUSUFF,
                        'stats': '9-1-0',
                    },
                    {
                        'name': SUMAN_MOKHTARIAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': SODIQ_YUSUFF,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:14',
                },
                'time': '22:30',
                'odds': {
                    SODIQ_YUSUFF: -496,
                    SUMAN_MOKHTARIAN: 385,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JAKE_MATTHEWS,
                        'stats': '13-4-0',
                    },
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_ROCCO_MARTIN,
                    'by': 'submission',
                    'round': 3,
                    'time': '1:19',
                },
                'time': '23:00',
                'odds': {
                    ANTHONY_ROCCO_MARTIN: 131,
                    JAKE_MATTHEWS: -148,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_WILLIS,
                        'stats': '8-2-0',
                    },
                    {
                        'name': MARK_HUNT,
                        'stats': '13-14-1',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_WILLIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    JUSTIN_WILLIS: -101,
                    MARK_HUNT: -111,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TYSON_PEDRO,
                        'stats': '7-2-0',
                    },
                    {
                        'name': MAURICIO_RUA,
                        'stats': '26-11-0',
                    },
                ],
                'winner': {
                    'fighter': MAURICIO_RUA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:43',
                },
                'time': '23:55',
                'odds': {
                    MAURICIO_RUA: 370,
                    TYSON_PEDRO: -473,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TAI_TUIVASA,
                        'stats': '10-1-0',
                    },
                    {
                        'name': JUNIOR_DOS_SANTOS,
                        'status': '21-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUNIOR_DOS_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:30',
                },
                'time': '23:59',
                'odds': {
                    JUNIOR_DOS_SANTOS: -153,
                    TAI_TUIVASA: 136,
                },
            },
        ]
    },

    {
        'date': '2018-12-08',
        'name': 'UFC 231',
        'location': 'Toronto, Ontario',
        'venue': 'Scotiabank Arena',
        'fights': [
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSANDAR_RAKIC,
                        'stats': '1-1-0',
                    },
                    {
                        'name': DEVIN_CLARK,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSANDAR_RAKIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:05',
                },
                'time': '18:30',
                'odds': {
                    ALEKSANDAR_RAKIC: -485,
                    DEVIN_CLARK: 400,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KYLE_NELSON,
                        'stats': '12-2-0',
                    },
                    {
                        'name': DIEGO_FERREIRA,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': DIEGO_FERREIRA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:23',
                },
                'time': '19:00',
                'odds': {
                    DIEGO_FERREIRA: -499,
                    KYLE_NELSON: 410,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DHIEGO_LIMA,
                        'stats': '15-7-0',
                    },
                    {
                        'name': CHAD_LAPRISE,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': DHIEGO_LIMA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:37',
                },
                'time': '19:30',
                'odds': {
                    DHIEGO_LIMA: 325,
                    CHAD_LAPRISE: -385,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRAD_KATONA,
                        'stats': '9-0-0',
                    },
                    {
                        'name': MATTHEW_LOPEZ,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': BRAD_KATONA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    BRAD_KATONA: -152,
                    MATTHEW_LOPEZ: 135,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                    {
                        'name': ELIAS_THEODOROU,
                        'stats': '17-2-0',
                    },
                ],
                'winner': {
                    'fighter': ELIAS_THEODOROU,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    ELIAS_THEODOROU: -135,
                    ERYK_ANDERS: 120,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JESSICA_EYE,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_EYE,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    JESSICA_EYE: 190,
                    KATLYN_CHOOKAGIAN: -217,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GILBERT_BURNS,
                        'stats': '14-3-0',
                    },
                    {
                        'name': OLIVIER_AUBIN_MERCIER,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': GILBERT_BURNS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    GILBERT_BURNS: 125,
                    OLIVIER_AUBIN_MERCIER: -141,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': NINA_ANSAROFF,
                        'stats': '10-5-0',
                    },
                    {
                        'name': CLAUDIA_GADELHA,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': NINA_ANSAROFF,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    NINA_ANSAROFF: 240,
                    CLAUDIA_GADELHA: -277,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                    {
                        'name': JIMI_MANUWA,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:41',
                },
                'time': '22:30',
                'odds': {
                    THIAGO_SANTOS: -187,
                    JIMI_MANUWA: 165,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HAKEEM_DAWODU,
                        'stats': '9-0-1',
                    },
                    {
                        'name': KYLE_BOCHNIAK,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': HAKEEM_DAWODU,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    HAKEEM_DAWODU: -199,
                    KYLE_BOCHNIAK: 175,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_OLIVEIRA,
                        'stats': '19-6-1',
                    },
                    {
                        'name': GUNNAR_NELSON,
                        'stats': '17-4-1',
                    },
                ],
                'winner': {
                    'fighter': GUNNAR_NELSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:17',
                },
                'time': '23:30',
                'odds': {
                    ALEX_OLIVEIRA: 142,
                    GUNNAR_NELSON: -160,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': VALENTINA_SHEVCHENKO,
                        'stats': '16-3-0',
                    },
                    {
                        'name': JOANNA_JEDRZEJCZYK,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': VALENTINA_SHEVCHENKO,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:54',
                'odds': {
                    VALENTINA_SHEVCHENKO: -302,
                    JOANNA_JEDRZEJCZYK: 260,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BRIAN_ORTEGA,
                        'stats': '14-1-0',
                    },
                    {
                        'name': MAX_HOLLOWAY,
                        'stats': '20-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAX_HOLLOWAY,
                    'by': 'tko',
                    'round': 4,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    MAX_HOLLOWAY: -110,
                    BRIAN_ORTEGA: -102,
                },
            },
        ]
    },

    {
        'date': '2018-12-15',
        'name': 'UFC Fight Night',
        'location': 'Milwaukee, Wisconsin',
        'venue': 'Fiserv Forum',
        'fights': [
            {
                'time': '15:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUAN_ADAMS,
                        'stats': '5-0-0',
                    },
                    {
                        'name': CHRIS_DE_LA_ROCHA,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': JUAN_ADAMS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:58',
                },
                'odds': {
                    JUAN_ADAMS: -481,
                    CHRIS_DE_LA_ROCHA: 375,
                },
            },
            {
                'time': '16:00',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TREVOR_SMITH,
                        'stats': '15-9-0',
                    },
                    {
                        'name': ZAK_CUMMINGS,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': ZAK_CUMMINGS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ZAK_CUMMINGS: -302,
                    TREVOR_SMITH: 260,
                },
            },
            {
                'time': '16:30',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_RODRIGUEZ,
                        'stats': '10-3-0',
                    },
                    {
                        'name': ADAM_MILSTEAD,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': MIKE_RODRIGUEZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:59',
                },
                'odds': {
                    MIKE_RODRIGUEZ: -105,
                    ADAM_MILSTEAD: -107,
                },
            },
            {
                'time': '17:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_GRIFFIN,
                        'stats': '17-6-0',
                    },
                    {
                        'name': DAN_IGE,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_IGE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DAN_IGE: -170,
                    JORDAN_GRIFFIN: 150,
                },
            },
            {
                'time': '18:15',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': GERALD_MEERSCHAERT,
                        'stats': '28-11-0',
                    },
                    {
                        'name': JACK_HERMANSSON,
                        'stats': '19-4-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_HERMANSSON,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:25',
                },
                'odds': {
                    JACK_HERMANSSON: -158,
                    GERALD_MEERSCHAERT: 140,
                },
            },
            {
                'time': '18:45',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JARED_GORDON,
                        'stats': '14-3-0',
                    },
                    {
                        'name': JOAQUIM_SILVA,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': JOAQUIM_SILVA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:39',
                },
                'odds': {
                    JOAQUIM_SILVA: 105,
                    JARED_GORDON: -118,
                },
            },
            {
                'time': '19:15',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DRAKKAR_KLOSE,
                        'stats': '10-1-1',
                    },
                    {
                        'name': BOBBY_GREEN,
                        'stats': '24-9-1',
                    },
                ],
                'winner': {
                    'fighter': DRAKKAR_KLOSE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DRAKKAR_KLOSE: -229,
                    BOBBY_GREEN: 200,
                },
            },
            {
                'time': '19:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DWIGHT_GRANT,
                        'stats': '9-2-0',
                    },
                    {
                        'name': ZAK_OTTOW,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': ZAK_OTTOW,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ZAK_OTTOW: 250,
                    DWIGHT_GRANT: -290,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:15',
                },
                'odds': {
                    CHARLES_OLIVEIRA: -290,
                    JIM_MILLER: 250,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ROB_FONT,
                        'stats': '16-4-0',
                    },
                    {
                        'name': SERGIO_PETTIS,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': ROB_FONT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ROB_FONT: -160,
                    SERGIO_PETTIS: 142,
                },
            },
            {
                'time': '21:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_HOOKER,
                        'stats': '18-8-0',
                    },
                    {
                        'name': EDSON_BARBOZA,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': EDSON_BARBOZA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:19',
                },
                'odds': {
                    EDSON_BARBOZA: -106,
                    DAN_HOOKER: -106,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                    {
                        'name': AL_IAQUINTA,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': AL_IAQUINTA,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    AL_IAQUINTA: 285,
                    KEVIN_LEE: -334,
                },
            },
        ]
    },

    {
        'date': '2018-12-29',
        'name': 'UFC 232',
        'location': 'Los Angeles, California',
        'venue': 'The Forum',
        'fights': [
            {
                'time': '18:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MONTEL_JACKSON,
                        'stats': '7-1-0',
                    },
                    {
                        'name': BRIAN_KELLEHER,
                        'stats': '19-10-0',
                    },
                ],
                'winner': {
                    'fighter': MONTEL_JACKSON,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:40',
                },
                'odds': {
                    MONTEL_JACKSON: -180,
                    BRIAN_KELLEHER: 159,
                },
            },
            {
                'time': '18:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_MILLENDER,
                        'stats': '17-4-0',
                    },
                    {
                        'name': SIYAR_BAHADURZADA,
                        'stats': '24-7-1',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_MILLENDER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CURTIS_MILLENDER: -147,
                    SIYAR_BAHADURZADA: 130,
                },
            },
            {
                'time': '19:12',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': BEVON_LEWIS,
                        'stats': '5-1-0',
                    },
                    {
                        'name': URIAH_HALL,
                        'stats': '19-10-0',
                    },
                ],
                'winner': {
                    'fighter': URIAH_HALL,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:32',
                },
                'odds': {
                    URIAH_HALL: 150,
                    BEVON_LEWIS: -170,
                },
            },
            {
                'time': '19:39',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_EWELL,
                        'stats': '13-5-0',
                    },
                    {
                        'name': NATHANIEL_WOOD,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': NATHANIEL_WOOD,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:12',
                },
                'odds': {
                    ANDRE_EWELL: 111,
                    NATHANIEL_WOOD: -125,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_HALL,
                        'stats': '7-1-0',
                    },
                    {
                        'name': BJ_PENN,
                        'stats': '16-13-2',
                    },
                ],
                'winner': {
                    'fighter': RYAN_HALL,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:46',
                },
                'odds': {
                    RYAN_HALL: -481,
                    BJ_PENN: 375,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PETR_YAN,
                        'stats': '12-1-0',
                    },
                    {
                        'name': DOUGLAS_SILVA_DE_ANDRADE,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': PETR_YAN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'odds': {
                    PETR_YAN: -330,
                    DOUGLAS_SILVA_DE_ANDRADE: 275,
                },
            },
            {
                'time': '21:00',
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MEGAN_ANDERSON,
                        'stats': '9-3-0',
                    },
                    {
                        'name': CAT_ZINGANO,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': MEGAN_ANDERSON,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:01',
                },
                'odds': {
                    MEGAN_ANDERSON: 106,
                    CAT_ZINGANO: -119,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': WALT_HARRIS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    WALT_HARRIS: -199,
                    ANDREI_ARLOVSKI: 175,
                },
            },
            {
                'time': '22:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': CHAD_MENDES,
                        'stats': '18-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:14',
                },
                'odds': {
                    ALEXANDER_VOLKANOVSKI: 120,
                    CHAD_MENDES: -135,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': COREY_ANDERSON,
                        'stats': '13-4-0',
                    },
                    {
                        'name': ILIR_LATIFI,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': COREY_ANDERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    COREY_ANDERSON: 114,
                    ILIR_LATIFI: -128,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CARLOS_CONDIT,
                        'stats': '30-13-0',
                    },
                    {
                        'name': MICHAEL_CHIESA,
                        'stats': '15-4-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAEL_CHIESA,
                    'by': 'submission',
                    'round': 2,
                    'time': '0:56',
                },
                'odds': {
                    MICHAEL_CHIESA: -103,
                    CARLOS_CONDIT: -109,
                },
            },
            {
                'time': '23:30',
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CRIS_CYBORG,
                        'stats': '20-2-0',
                    },
                    {
                        'name': AMANDA_NUNES,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': AMANDA_NUNES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:51',
                },
                'odds': {
                    AMANDA_NUNES: 163,
                    CRIS_CYBORG: -185,
                },
            },
            {
                'time': '23:59',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JON_JONES,
                        'stats': '24-1-0',
                    },
                    {
                        'name': ALEXANDER_GUSTAFSSON,
                        'stats': '18-5-0',
                    },
                ],
                'winner': {
                    'fighter': JON_JONES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:02',
                },
                'odds': {
                    JON_JONES: -294,
                    ALEXANDER_GUSTAFSSON: 253,
                },
            },
        ]
    },

    {
        'date': '2019-01-19',
        'name': 'UFC Fight Night',
        'location': 'New York, New York',
        'venue': 'Barclays Center',
        'fights': [
            {
                'time': '18:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CHANCE_RENCOUNTRE,
                        'stats': '13-3-0',
                    },
                    {
                        'name': KYLE_STEWART,
                        'stats': '8-1-0',
                    },
                ],
                'winner': {
                    'fighter': CHANCE_RENCOUNTRE,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:36',
                },
                'odds': {
                    CHANCE_RENCOUNTRE: 140,
                    KYLE_STEWART: -158,
                },
            },
            {
                'time': '18:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GEOFF_NEAL,
                        'stats': '11-2-0',
                    },
                    {
                        'name': BELAL_MUHAMMAD,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': GEOFF_NEAL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    GEOFF_NEAL: -199,
                    BELAL_MUHAMMAD: 175,
                },
            },
            {
                'time': '19:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': TE_EDWARDS,
                        'stats': '6-3-0',
                    },
                    {
                        'name': DENNIS_BERMUDEZ,
                        'stats': '18-9-0',
                    },
                ],
                'winner': {
                    'fighter': DENNIS_BERMUDEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DENNIS_BERMUDEZ: 103,
                    TE_EDWARDS: -116,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARIO_BAUTISTA,
                        'stats': '0-0-0',
                    },
                    {
                        'name': CORY_SANDHAGEN,
                        'stats': '10-1-0',
                    },
                ],
                'winner': {
                    'fighter': CORY_SANDHAGEN,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:31',
                },
                'odds': {
                    CORY_SANDHAGEN: -542,
                    MARIO_BAUTISTA: 415,
                },
            },
            {
                'time': '21:00',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ARIANE_LIPSKI,
                        'stats': '11-4-0',
                    },
                    {
                        'name': JOANNE_CALDERWOOD,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': JOANNE_CALDERWOOD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JOANNE_CALDERWOOD: 210,
                    ARIANE_LIPSKI: -241,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_HERNANDEZ,
                        'stats': '10-2-0',
                    },
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                ],
                'winner': {
                    'fighter': DONALD_CERRONE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:43',
                },
                'odds': {
                    DONALD_CERRONE: 180,
                    ALEXANDER_HERNANDEZ: -205,
                },
            },
            {
                'time': '22:00',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': KARL_ROBERSON,
                        'stats': '7-2-0',
                    },
                    {
                        'name': GLOVER_TEIXEIRA,
                        'stats': '28-7-0',
                    },
                ],
                'winner': {
                    'fighter': GLOVER_TEIXEIRA,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:22',
                },
                'odds': {
                    GLOVER_TEIXEIRA: -106,
                    KARL_ROBERSON: -106,
                },
            },
            {
                'time': '22:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': RACHAEL_OSTOVICH,
                        'stats': '4-5-0',
                    },
                    {
                        'name': PAIGE_VANZANT,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': PAIGE_VANZANT,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:51',
                },
                'odds': {
                    PAIGE_VANZANT: -181,
                    RACHAEL_OSTOVICH: 160,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': DUSTIN_ORTIZ,
                        'stats': '19-8-0',
                    },
                    {
                        'name': JOSEPH_BENAVIDEZ,
                        'stats': '27-5-0',
                    },
                ],
                'winner': {
                    'fighter': JOSEPH_BENAVIDEZ,
                    'by': '27-5-0',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JOSEPH_BENAVIDEZ: -223,
                    DUSTIN_ORTIZ: 195,
                },
            },
            {
                'time': '23:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GREGOR_GILLESPIE,
                        'stats': '13-0-0',
                    },
                    {
                        'name': YANCY_MEDEIROS,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': GREGOR_GILLESPIE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:59',
                },
                'odds': {
                    GREGOR_GILLESPIE: -481,
                    YANCY_MEDEIROS: 375,
                },
            },
            {
                'time': '23:45',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GREG_HARDY,
                        'stats': '3-1-0',
                    },
                    {
                        'name': ALLEN_CROWDER,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALLEN_CROWDER,
                    'by': 'dq',
                    'round': 2,
                    'time': '2:28',
                },
                'odds': {
                    GREG_HARDY: -473,
                    ALLEN_CROWDER: 370,
                },
            },
            {
                'time': '23:50',
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': HENRY_CEJUDO,
                        'stats': '14-2-0',
                    },
                    {
                        'name': TJ_DILLASHAW,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': HENRY_CEJUDO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:33',
                },
            },
        ]
    },

    {
        'date': '2019-02-02',
        'name': 'UFC Fight Ngiht',
        'location': 'Fortalexa, Brazil',
        'venue': 'Estadio Catelao',
        'fights': [
            {
                'time': '17:00',
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ROGERIO_BONTORIN,
                        'stats': '15-1-0',
                    },
                    {
                        'name': MAGOMED_BIBULATOV,
                        'stats': '14-1-0',
                    },
                ],
                'winner': {
                    'fighter': ROGERIO_BONTORIN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ROGERIO_BONTORIN: 250,
                    MAGOMED_BIBULATOV: -305,
                },
            },
            {
                'time': '17:35',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': SAID_NURMAGOMEDOV,
                        'stats': '13-1-0',
                    },
                    {
                        'name': RICARDO_RAMOS,
                        'stats': '12-1-0',
                    },
                ],
                'winner': {
                    'fighter': SAID_NURMAGOMEDOV,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:28',
                },
                'odds': {
                    SAID_NURMAGOMEDOV: 155,
                    RICARDO_RAMOS: -176,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': FELIPE_COLARES,
                        'stats': '8-1-0',
                    },
                    {
                        'name': GERALDO_DE_FREITAS,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': GERALDO_DE_FREITAS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
            },
            {
                'time': '18:35',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JAIRZINHO_ROZENSTRUIK,
                        'stats': '6-0-0',
                    },
                    {
                        'name': JUNIOR_ALBINI,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': JAIRZINHO_ROZENSTRUIK,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:54',
                },
                'odds': {
                    JAIRZINHO_ROZENSTRUIK: 125,
                    JUNIOR_ALBINI: -141,
                },
            },
            {
                'time': '18:55',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MAX_GRIFFIN,
                        'stats': '14-6-0',
                    },
                    {
                        'name': THIAGO_ALVES,
                        'stats': '28-13-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_ALVES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    THIAGO_ALVES: 155,
                    MAX_GRIFFIN: -176,
                },
            },
            {
                'time': '19:20',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': TAILA_SANTOS,
                        'stats': '15-1-0',
                    },
                    {
                        'name': MARA_ROMERO_BORELLA,
                        'stats': '13-5-0',
                    },
                ],
                'winner': {
                    'fighter': MARA_ROMERO_BORELLA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MARA_ROMERO_BORELLA: 195,
                    TAILA_SANTOS: -223,
                },
            },
            {
                'time': '19:45',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_HERNANDEZ,
                        'stats': '6-1-0',
                    },
                    {
                        'name': MARKUS_PEREZ,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': MARKUS_PEREZ,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:07',
                },
                'odds': {
                    MARKUS_PEREZ: 121,
                    ANTHONY_HERNANDEZ: -136,
                },
            },
            {
                'time': '20:10',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SARAH_FROTA,
                        'stats': '9-1-0',
                    },
                    {
                        'name': LIVINHA_SOUZA,
                        'stats': '12-1-0',
                    },
                ],
                'winner': {
                    'fighter': LIVINHA_SOUZA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LIVINHA_SOUZA: -235,
                    SARAH_FROTA: 205,
                },
            },
            {
                'time': '20:40',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JOHNNY_WALKER,
                        'stats': '17-3-0',
                    },
                    {
                        'name': JUSTIN_LEDET,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOHNNY_WALKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:15',
                },
                'odds': {
                    JOHNNY_WALKER: -211,
                    JUSTIN_LEDET: 185,
                },
            },
            {
                'time': '21:10',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_TEYMUR,
                        'stats': '8-2-0',
                    },
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'submission',
                    'round': 2,
                    'time': '0:55',
                },
                'odds': {
                    CHARLES_OLIVEIRA: -111,
                    DAVID_TEYMUR: -101,
                },
            },
            {
                'time': '21:40',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LYMAN_GOOD,
                        'stats': '20-5-0',
                    },
                    {
                        'name': DAMIAN_MAIA,
                        'stats': '26-9-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIAN_MAIA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:38',
                },
                'odds': {
                    DAMIAN_MAIA: -205,
                    LYMAN_GOOD: 180,
                },
            },
            {
                'time': '22:10',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RENATO_MOICANO,
                        'stats': '13-2-1',
                    },
                    {
                        'name': JOSE_ALDO,
                        'stats': '28-4-0',
                    },
                ],
                'winner': {
                    'fighter': JOSE_ALDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:44',
                },
                'odds': {
                    JOSE_ALDO: -112,
                    RENATO_MOICANO: 100,
                },
            },
            {
                'time': '22:40',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARLON_MORAES,
                        'stats': '22-5-1',
                    },
                    {
                        'name': RAPHAEL_ASSUNCAO,
                        'stats': '27-6-0',
                    },
                ],
                'winner': {
                    'fighter': MARLON_MORAES,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:17',
                },
                'odds': {
                    MARLON_MORAES: -152,
                    RAPHAEL_ASSUNCAO: 135,
                },
            },
        ]
    },

    {
        'date': '2019-02-09',
        'name': 'UFC 234',
        'location': 'Melbourne, Australia',
        'venue': 'Rod Laver Arena',
        'fights': [
            {
                'time': '19:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JONATHAN_MARTINEZ,
                        'stats': '0-0-0',
                    },
                    {
                        'name': WULIJI_BUREN,
                        'stats': '10-7-0',
                    },
                ],
                'winner': {
                    'fighter': JONATHAN_MARTINEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JONATHAN_MARTINEZ: -129,
                    WULIJI_BUREN: 115,
                },
            },
            {
                'time': '19:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CALLAN_POTTER,
                        'stats': '0-0-0',
                    },
                    {
                        'name': JALIN_TURNER,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': JALIN_TURNER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:53',
                },
                'odds': {
                    JALIN_TURNER: -211,
                    CALLAN_POTTER: 185,
                },
            },
            {
                'time': '19:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MARCOS_ROSA_MARIANO,
                        'stats': '6-4-0',
                    },
                    {
                        'name': LANDO_VANNATA,
                        'stats': '10-3-2',
                    },
                ],
                'winner': {
                    'fighter': LANDO_VANNATA,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:55',
                },
                'odds': {
                    LANDO_VANNATA: -431,
                    MARCOS_ROSA_MARIANO: 360,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': TERUTO_ISHIHARA,
                        'stats': '11-6-2',
                    },
                    {
                        'name': KYUNG_HO_KANG,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': KYUNG_HO_KANG,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:59',
                },
                'odds': {
                    KYUNG_HO_KANG: -372,
                    TERUTO_ISHIHARA: 315,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': RAULIAN_PAIVA,
                        'stats': '18-2-0',
                    },
                    {
                        'name': KAI_KARA_FRANCE,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': KAI_KARA_FRANCE,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KAI_KARA_FRANCE: -253,
                    RAULIAN_PAIVA: 220,
                },
            },
            {
                'time': '21:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHANE_YOUNG,
                        'stats': '12-4-0',
                    },
                    {
                        'name': AUSTIN_ARNETT,
                        'stats': '16-6-0',
                    },
                ],
                'winner': {
                    'fighter': SHANE_YOUNG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SHANE_YOUNG: -385,
                    AUSTIN_ARNETT: 325,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DEVONTE_SMITH,
                        'stats': '10-1-0',
                    },
                    {
                        'name': DONG_HYUN_KIM,
                        'stats': '22-4-1',
                    },
                ],
                'winner': {
                    'fighter': DEVONTE_SMITH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:53',
                },
                'odds': {
                    DEVONTE_SMITH: -260,
                    DONG_HYUN_KIM: 226,
                },
            },
            {
                'time': '22:00',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JIMMY_CRUTE,
                        'stats': '10-0-0',
                    },
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': JIMMY_CRUTE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:49',
                },
                'odds': {
                    JIMMY_CRUTE: -129,
                    SAM_ALVEY: 115,
                },
            },
            {
                'time': '22:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MONTANA_DE_LA_ROSA,
                        'stats': '10-4-0',
                    },
                    {
                        'name': NADIA_KASSEM,
                        'stats': '5-1-0',
                    },
                ],
                'winner': {
                    'fighter': MONTANA_DE_LA_ROSA,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:37',
                },
                'odds': {
                    MONTANA_DE_LA_ROSA: -235,
                    NADIA_KASSEM: 205,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RICKY_SIMON,
                        'stats': '11-1-0',
                    },
                    {
                        'name': RANI_YAHYA,
                        'stats': '26-10-0',
                    },
                ],
                'winner': {
                    'fighter': RICKY_SIMON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    RICKY_SIMON: -106,
                    RANI_YAHYA: -106,
                },
            },
            {
                'time': '23:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ISRAEL_ADESANYA,
                        'stats': '16-0-0',
                    },
                    {
                        'name': ANDERSON_SILVA,
                        'stats': '34-9-0',
                    },
                ],
                'winner': {
                    'fighter': ISRAEL_ADESANYA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ISRAEL_ADESANYA: -519,
                    ANDERSON_SILVA: 400,
                },
            },
        ]
    },

    {
        'date': '2019-02-17',
        'name': 'UFC Fight Night',
        'location': 'PHoenix, Arizona',
        'venue': 'Talking Stick Resort Arena',
        'fights': [
            {
                'time': '18:05',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': EMILY_WHITMIRE,
                        'stats': '4-2-0',
                    },
                    {
                        'name': ALEXANDRA_ALBU,
                        'stats': '7-1-0',
                    },
                ],
                'winner': {
                    'fighter': EMILY_WHITMIRE,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:01',
                },
                'odds': {
                    EMILY_WHITMIRE: -106,
                    ALEXANDRA_ALBU: -106,
                },
            },
            {
                'time': '18:35',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUKE_SANDERS,
                        'stats': '13-3-0',
                    },
                    {
                        'name': RENAN_BARAO,
                        'stats': '36-8-0',
                    },
                ],
                'winner': {
                    'fighter': LUKE_SANDERS,
                    'by': 'ko/kto',
                    'round': 2,
                    'time': '1:01',
                },
                'odds': {
                    LUKE_SANDERS: -140,
                    RENAN_BARAO: 124,
                },
            },
            {
                'time': '19:35',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': SCOTT_HOLTZMAN,
                        'stats': '12-3-0',
                    },
                    {
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                ],
                'winner': {
                    'fighter': NIK_LENTZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    NIK_LENTZ: 140,
                    SCOTT_HOLTZMAN: -158,
                },
            },
            {
                'time': '20:05',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANDREA_LEE,
                        'stats': '10-2-0',
                    },
                    {
                        'name': ASHLEE_EVANS_SMITH,
                        'stats': '6-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANDREA_LEE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANDREA_LEE: -176,
                    ASHLEE_EVANS_SMITH: 155,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MANNY_BERMUDEZ,
                        'stats': '14-0-0',
                    },
                    {
                        'name': BENITO_LOPEZ,
                        'stats': '9-1-0',
                    },
                ],
                'winner': {
                    'fighter': MANNY_BERMUDEZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:09',
                },
                'odds': {
                    MANNY_BERMUDEZ: -176,
                    BENITO_LOPEZ: 155,
                },
            },
            {
                'time': '20:35',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JIMMIE_RIVERA,
                        'stats': '22-3-0',
                    },
                    {
                        'name': ALJAMAIN_STERLING,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALJAMAIN_STERLING,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALJAMAIN_STERLING: 115,
                    JIMMIE_RIVERA: -129,
                },
            },
            {
                'time': '21:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MYLES_JURY,
                        'stats': '17-4-0',
                    },
                    {
                        'name': ANDRE_FILI,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_FILI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANDRE_FILI: 126,
                    MYLES_JURY: -142,
                },
            },
            {
                'time': '21:35',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': VICENTE_LUQUE,
                        'stats': '15-6-1',
                    },
                    {
                        'name': BRYAN_BARBERENA,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': VICENTE_LUQUE,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:54',
                },
                'odds': {
                    VICENTE_LUQUE: -451,
                    BRYAN_BARBERENA: 355,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': KRON_GRACIE,
                        'stats': '4-0-0',
                    },
                    {
                        'name': ALEX_CACERES,
                        'stats': '14-12-0',
                    },
                ],
                'winner': {
                    'fighter': KRON_GRACIE,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:06',
                },
                'odds': {
                    KRON_GRACIE: -259,
                    ALEX_CACERES: 225,
                },
            },
            {
                'time': '20:35',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CYNTHIA_CALVILLO,
                        'stats': '8-1-0',
                    },
                    {
                        'name': CORTNEY_CASEY_SANCHEZ,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': CYNTHIA_CALVILLO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CYNTHIA_CALVILLO: -366,
                    CORTNEY_CASEY_SANCHEZ: 310,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': PAUL_FELDER,
                        'stats': '16-4-0',
                    },
                    {
                        'name': JAMES_VICK,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': PAUL_FELDER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    PAUL_FELDER: 102,
                    JAMES_VICK: -115,
                },
            },
            {
                'time': '',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': FRANCIS_NGANNOU,
                        'stats': '13-3-0',
                    },
                    {
                        'name': CAIN_VELASQUEZ,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCIS_NGANNOU,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:26',
                },
                'odds': {
                    FRANCIS_NGANNOU: 169,
                    CAIN_VELASQUEZ: -192,
                },
            },
        ]
    },

    {
        'date': '2019-02-23',
        'name': 'UFC Fight Night',
        'location': 'Prague, Czech Republic',
        'venue': 'O2 Arena',
        'fights': [
            {
                'time': '11:20',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JOEL_ALVAREZ,
                        'stats': '15-2-0',
                    },
                    {
                        'name': DAMIR_ISMAGULOV,
                        'stats': '17-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIR_ISMAGULOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DAMIR_ISMAGULOV: -282,
                    JOEL_ALVAREZ: 244,
                },
            },
            {
                'time': '11:40',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DIEGO_FERREIRA,
                        'stats': '15-2-0',
                    },
                    {
                        'name': RUSTAM_KHABILOV,
                        'stats': '23-4-0',
                    },
                ],
                'winner': {
                    'fighter': DIEGO_FERREIRA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DIEGO_FERREIRA: 121,
                    RUSTAM_KHABILOV: -136,
                },
            },
            {
                'time': '12:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_FISHGOLD,
                        'stats': '18-2-1',
                    },
                    {
                        'name': DANIEL_TEYMUR,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': CHRIS_FISHGOLD,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:10',
                },
                'odds': {
                    CHRIS_FISHGOLD: -228,
                    DANIEL_TEYMUR: 199,
                },
            },
            {
                'time': '12:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ISMAIL_NAURDIEV,
                        'stats': '15-2-0',
                    },
                    {
                        'name': MICHEL_PRAZERES,
                        'stats': '26-3-0',
                    },
                ],
                'winner': {
                    'fighter': ISMAIL_NAURDIEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ISMAIL_NAURDIEV: 374,
                    MICHEL_PRAZERES: -450,
                },
            },
            {
                'time': '13:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MARC_POLO_REYES,
                        'stats': '8-5-0',
                    },
                    {
                        'name': DAMIR_HADZOVIC,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIR_HADZOVIC,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:03',
                },
                'odds': {
                    DAMIR_HADZOVIC: -132,
                    MARC_POLO_REYES: 117,
                },
            },
            {
                'time': '13:35',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DWIGHT_GRANT,
                        'stats': '9-2-0',
                    },
                    {
                        'name': CARLO_PEDERSOLI_JR,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': DWIGHT_GRANT,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:59',
                },
                'odds': {
                    DWIGHT_GRANT: 137,
                    CARLO_PEDERSOLI_JR: -154,
                },
            },
            {
                'time': '14:00',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': GILLIAN_ROBERTSON,
                        'stats': '6-3-0',
                    },
                    {
                        'name': VERONICA_MACEDO,
                        'stats': '5-3-1',
                    },
                ],
                'winner': {
                    'fighter': GILLIAN_ROBERTSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:27',
                },
                'odds': {
                    GILLIAN_ROBERTSON: -173,
                    VERONICA_MACEDO: 153,
                },
            },
            {
                'time': '14:30',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': KLIDSON_DE_ABREU,
                        'stats': '0-0-0',
                    },
                    {
                        'name': MAGOMED_ANKALAEV,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': MAGOMED_ANKALAEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MAGOMED_ANKALAEV: -211,
                    KLIDSON_DE_ABREU: 185,
                },
            },
            {
                'time': '15:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PETR_YAN,
                        'stats': '12-1-0',
                    },
                    {
                        'name': JOHN_DODSON,
                        'stats': '21-11-0',
                    },
                ],
                'winner': {
                    'fighter': PETR_YAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    PETR_YAN: -250,
                    JOHN_DODSON: 218,
                },
            },
            {
                'time': '15:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': LUCIE_PUDILOVA,
                        'stats': '8-4-0',
                    },
                    {
                        'name': LIZ_CARMOUCHE,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter':LIZ_CARMOUCHE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LIZ_CARMOUCHE: -153,
                    LUCIE_PUDILOVA: 136,
                },
            },
            {
                'time': '16:00',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MICHAL_OLEKSIEJCZUK,
                        'stats': '13-2-0',
                    },
                    {
                        'name': GIAN_VILLANTE,
                        'stats': '17-11-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAL_OLEKSIEJCZUK,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:34',
                },
                'odds': {
                    MICHAL_OLEKSIEJCZUK: -204,
                    GIAN_VILLANTE: 179,
                },
            },
            {
                'time': '16:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCOS_ROGERIO_DE_LIMA,
                        'stats': '16-7-1',
                    },
                    {
                        'name': STEFAN_STRUVE,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': STEFAN_STRUVE,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:21',
                },
                'odds': {
                    STEFAN_STRUVE: -112,
                    MARCOS_ROGERIO_DE_LIMA: 100,
                },
            },
            {
                'time': '17:00',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                    {
                        'name': JAN_BLACHOWICZ,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:39',
                },
                'odds': {
                    THIAGO_SANTOS: -118,
                    JAN_BLACHOWICZ: 105,
                },
            },
        ]
    },

    {
        'date': '2019-03-02',
        'name': 'UFC 235',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'time': '18:00',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': HANNA_CIFERS,
                        'stats': '9-3-0',
                    },
                    {
                        'name': POLYANA_VIANA,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': HANNA_CIFERS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    HANNA_CIFERS: 240,
                    POLYANA_VIANA: -277,
                },
            },
            {
                'time': '19:05',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MACY_CHIASSON,
                        'stats': '5-0-0',
                    },
                    {
                        'name': GINA_MAZANY,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': MACY_CHIASSON,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:49',
                },
                'odds': {
                    MACY_CHIASSON: -485,
                    GINA_MAZANY: 400,
                },
            },
            {
                'time': '19:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_BYRD,
                        'stats': '10-6-0',
                    },
                    {
                        'name': EDMEN_SHAHBAZYAN,
                        'stats': '9-0-0',
                    },
                ],
                'winner': {
                    'fighter': EDMEN_SHAHBAZYAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:38',
                },
                'odds': {
                    EDMEN_SHAHBAZYAN: -141,
                    CHARLES_BYRD: 125,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICKEY_GALL,
                        'stats': '5-2-0',
                    },
                    {
                        'name': DIEGO_SANCHEZ,
                        'stats': '31-11-0',
                    },
                ],
                'winner': {
                    'fighter': DIEGO_SANCHEZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:14',
                },
                'odds': {
                    DIEGO_SANCHEZ: 218,
                    MICKEY_GALL: -250,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ALEJANDRO_PEREZ,
                        'stats': '22-7-1',
                    },
                    {
                        'name': CODY_STAMANN,
                        'stats': '18-2-0',
                    },
                ],
                'winner': {
                    'fighter': CODY_STAMANN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CODY_STAMANN: -187,
                    ALEJANDRO_PEREZ: 165,
                },
            },
            {
                'time': '21:00',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JOHNNY_WALKER,
                        'stats': '17-3-0',
                    },
                    {
                        'name': MISHA_CIRKUNOV,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': JOHNNY_WALKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:37',
                },
                'odds': {
                    JOHNNY_WALKER: -164,
                    MISHA_CIRKUNOV: 145,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ZABIT_MAGOMEDSHARIPOV,
                        'stats': '17-1-0',
                    },
                    {
                        'name': JEREMY_STEPHENS,
                        'stats': '28-16-0',
                    },
                ],
                'winner': {
                    'fighter': ZABIT_MAGOMEDSHARIPOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ZABIT_MAGOMEDSHARIPOV: -296,
                    JEREMY_STEPHENS: 255,
                },
            },
            {
                'time': '22:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                    {
                        'name': CODY_GARBRANDT,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': PEDRO_MUNHOZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:54',
                },
                'odds': {
                    PEDRO_MUNHOZ: 150,
                    CODY_GARBRANDT: -170,
                },
            },
            {
                'time': '22:30',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': WEILI_ZHANG,
                        'stats': '0-0-0',
                    },
                    {
                        'name': TECIA_TORRES,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': WEILI_ZHANG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    WEILI_ZHANG: -150,
                    TECIA_TORRES: 133,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BEN_ASKREN,
                        'stats': '18-0-0',
                    },
                    {
                        'name': ROBBIE_LAWLER,
                        'stats': '28-13-0',
                    },
                ],
                'winner': {
                    'fighter': BEN_ASKREN,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:21',
                },
                'odds': {
                    BEN_ASKREN: -280,
                    ROBBIE_LAWLER: 242,
                },
            },
            {
                'time': '23:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KAMARU_USMAN,
                        'stats': '15-1-0',
                    },
                    {
                        'name': TYRON_WOODLEY,
                        'stats': '19-4-1',
                    },
                ],
                'winner': {
                    'fighter': KAMARU_USMAN,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    KAMARU_USMAN: 176,
                    TYRON_WOODLEY: -200,
                },
            },
            {
                'time': '23:59',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': JON_JONES,
                        'stats': '24-1-0',
                    },
                ],
                'winner': {
                    'fighter': JON_JONES,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    JON_JONES: -830,
                    ANTHONY_SMITH: 585,
                },
            },
        ]
    },

    {
        'date': '2019-03-09',
        'name': 'UFC Fight Night',
        'location': 'Wichita, Kansas',
        'venue': 'Intrust Bank Arena',
        'fights': [
            {
                'time': '17:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_MORET,
                        'stats': '13-5-0',
                    },
                    {
                        'name': ALEX_WHITE,
                        'stats': '13-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_WHITE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEX_WHITE: -135,
                    DAN_MORET: 120,
                },
            },
            {
                'time': '17:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ZAK_OTTOW,
                        'stats': '17-7-0',
                    },
                    {
                        'name': ALEX_MORONO,
                        'stats': '16-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_MORONO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:34',
                },
                'odds': {
                    ALEX_MORONO: -179,
                    ZAK_OTTOW: 158,
                },
            },
            {
                'time': '18:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MATT_SCHNELL,
                        'stats': '13-4-0',
                    },
                    {
                        'name': LOUIS_SMOLKA,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': MATT_SCHNELL,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:18',
                },
                'odds': {
                    MATT_SCHNELL: 110,
                    LOUIS_SMOLKA: -124,
                },
            },
            {
                'time': '18:36',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JEFF_HUGHES,
                        'stats': '10-2-0',
                    },
                    {
                        'name': MAURICE_GREEN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': MAURICE_GREEN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MAURICE_GREEN: 225,
                    JEFF_HUGHES: -259,
                },
            },
            {
                'time': '19:06',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': YANA_KUNITSKAYA,
                        'stats': '12-4-0',
                    },
                    {
                        'name': MARION_RENEAU,
                        'stats': '9-5-1',
                    },
                ],
                'winner': {
                    'fighter': YANA_KUNITSKAYA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    YANA_KUNITSKAYA: -229,
                    MARION_RENEAU: 200,
                },
            },
            {
                'time': '19:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_ROCCO_MARTIN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANTHONY_ROCCO_MARTIN: -220,
                    SERGIO_MORAES: 193,
                },
            },
            {
                'time': '20:03',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JULIAN_EROSA,
                        'stats': '22-8-0',
                    },
                    {
                        'name': GRANT_DAWSON,
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': GRANT_DAWSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    GRANT_DAWSON: -190,
                    JULIAN_EROSA: 167,
                },
            },
            {
                'time': '20:33',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': OMARI_AKHMEDOV,
                        'stats': '18-4-1',
                    },
                    {
                        'name': TIM_BOETSCH,
                        'stats': '21-13-0',
                    },
                ],
                'winner': {
                    'fighter': OMARI_AKHMEDOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    OMARI_AKHMEDOV: -152,
                    TIM_BOETSCH: 135,
                },
            },
            {
                'time': '21:06',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DREW_DOBER,
                        'stats': '20-9-0',
                    },
                    {
                        'name': BENEIL_DARIUSH,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': BENEIL_DARIUSH,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:42',
                },
                'odds': {
                    BENEIL_DARIUSH: -211,
                    DREW_DOBER: 185,
                },
            },
            {
                'time': '21:35',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': BEN_ROTHWELL,
                        'stats': '36-11-0',
                    },
                    {
                        'name': BLAGOY_IVANOV,
                        'stats': '17-2-0',
                    },
                ],
                'winner': {
                    'fighter': BLAGOY_IVANOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    BLAGOY_IVANOV: 100,
                    BEN_ROTHWELL: -112,
                },
            },
            {
                'time': '22:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NIKO_PRICE,
                        'stats': '13-2-0',
                    },
                    {
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                ],
                'winner': {
                    'fighter': NIKO_PRICE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:50',
                },
                'odds': {
                    NIKO_PRICE: 175,
                    TIM_MEANS: -199,
                },
            },
            {
                'time': '22:35',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_MILLENDER,
                        'stats': '17-4-0',
                    },
                    {
                        'name': ELIZEU_ZALESKI_DOS_SANTOS,
                        'stats': '20-5-0',
                    },
                ],
                'winner': {
                    'fighter': ELIZEU_ZALESKI_DOS_SANTOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:35',
                },
                'odds': {
                    ELIZEU_ZALESKI_DOS_SANTOS: 105,
                    CURTIS_MILLENDER: -118,
                },
            },
            {
                'time': '23:03',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUNIOR_DOS_SANTOS,
                        'stats': '21-5-0',
                    },
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': JUNIOR_DOS_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:58',
                },
                'odds': {
                    JUNIOR_DOS_SANTOS: -240,
                    DERRICK_LEWIS: 209,
                },
            },
        ]
    },

    {
        'date': '2019-03-16',
        'name': 'UFC Fight Night',
        'location': 'United Kingdom',
        'venue': 'The O2 Arena',
        'fights': [
            {
                'time': '13:20',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': NAD_NARIMANI,
                        'stats': '12-3-0',
                    },
                    {
                        'name': MIKE_GRUNDY,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': MIKE_GRUNDY,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:42',
                },
                'odds': {
                    MIKE_GRUNDY: 115,
                    NAD_NARIMANI: -129,
                },
            },
            {
                'time': '13:50',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': PRISCILA_CACHOEIRA,
                        'stats': '8-2-0',
                    },
                    {
                        'name': MOLLY_MCCANN,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': MOLLY_MCCANN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MOLLY_MCCANN: -193,
                    PRISCILA_CACHOEIRA: 170,
                },
            },
            {
                'time': '14:20',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': DAN_IGE,
                        'stats': '11-2-0',
                    },
                    {
                        'name': DANNY_HENRY,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_IGE,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:17',
                },
                'odds': {
                    DAN_IGE: -133,
                    DANNY_HENRY: 118,
                },
            },
            {
                'time': '14:50',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SAPARBEG_SAFAROV,
                        'stats': '8-2-0',
                    },
                    {
                        'name': NICK_NEGUMEREANU,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': SAPARBEG_SAFAROV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SAPARBEG_SAFAROV: 155,
                    NICK_NEGUMEREANU: -176,
                },
            },
            {
                'time': '15:10',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOE_DUFFY,
                        'stats': '16-4-0',
                    },
                    {
                        'name': MARC_DIAKIESE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': MARC_DIAKIESE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MARC_DIAKIESE: 150,
                    JOE_DUFFY: -170,
                },
            },
            {
                'time': '15:40',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_RINALDI,
                        'stats': '14-7-0',
                    },
                    {
                        'name': ARNOLD_ALLEN,
                        'stats': '14-1-0',
                    },
                ],
                'winner': {
                    'fighter': ARNOLD_ALLEN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ARNOLD_ALLEN: -152,
                    JORDAN_RINALDI: 135,
                },
            },
            {
                'time': '16:15',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JOHN_PHILLIPS,
                        'stats': '21-9-0',
                    },
                    {
                        'name': JACK_MARSHMAN,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_MARSHMAN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JACK_MARSHMAN: -133,
                    JOHN_PHILLIPS: 118,
                },
            },
            {
                'time': '16:40',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CLAUDIO_DA_SILVA,
                        'stats': '13-1-0',
                    },
                    {
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': CLAUDIO_DA_SILVA,
                    'by': 'submission',
                    'round': 3,
                    'time': '2:37',
                },
                'odds': {
                    CLAUDIO_DA_SILVA: -150,
                    DANNY_ROBERTS: 133,
                },
            },
            {
                'time': '17:15',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JOSE_QUINONEZ,
                        'stats': '8-3-0',
                    },
                    {
                        'name': NATHANIEL_WOOD,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': NATHANIEL_WOOD,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:46',
                },
                'odds': {
                    NATHANIEL_WOOD: -340,
                    JOSE_QUINONEZ: 290,
                },
            },
            {
                'time': '17:42',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DOMINICK_REYES,
                        'stats': '11-0-0',
                    },
                    {
                        'name': VOLKAN_OEZDEMIR,
                        'stats': '15-4-0',
                    },
                ],
                'winner': {
                    'fighter': DOMINICK_REYES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DOMINICK_REYES: -253,
                    VOLKAN_OEZDEMIR: 220,
                },
            },
            {
                'time': '18:21',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GUNNAR_NELSON,
                        'stats': '17-4-1',
                    },
                    {
                        'name': LEON_EDWARDS,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': LEON_EDWARDS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LEON_EDWARDS: -141,
                    GUNNAR_NELSON: 125,
                },
            },
            {
                'time': '18:45',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JORGE_MASVIDAL,
                        'stats': '33-13-0',
                    },
                    {
                        'name': DARREN_TILL,
                        'stats': '17-2-1',
                    },
                ],
                'winner': {
                    'fighter': JORGE_MASVIDAL,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:05',
                },
                'odds': {
                    JORGE_MASVIDAL: 190,
                    DARREN_TILL: -217,
                },
            },
        ]
    },

    {
        'date': '2019-03-23',
        'name': 'UFC Fight Night',
        'location': 'Nashville, Tennessee',
        'venue': 'Bridgestone Arena',
        'fights': [
            {
                'time': '19:05',
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_ESPINOSA,
                        'stats': '13-5-0',
                    },
                    {
                        'name': ERIC_SHELTON,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_ESPINOSA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JORDAN_ESPINOSA: 125,
                    ERIC_SHELTON: -141,
                },
            },
            {
                'time': '19:15',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': FRANKIE_SAENZ,
                        'stats': '13-6-0',
                    },
                    {
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:25',
                },
                'odds': {
                    MARLON_VERA: -170,
                    FRANKIE_SAENZ: 150,
                },
            },
            {
                'time': '19:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_GUTIERREZ,
                        'stats': '12-3-0',
                    },
                    {
                        'name': RYAN_MACDONALD,
                        'stats': '10-1-0',
                    },
                ],
                'winner': {
                    'fighter': CHRIS_GUTIERREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CHRIS_GUTIERREZ: -297,
                    RYAN_MACDONALD: 256,
                },
            },
            {
                'time': '19:45',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BOBBY_MOFFETT,
                        'stats': '13-4-0',
                    },
                    {
                        'name': BRYCE_MITCHELL,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': BRYCE_MITCHELL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    BRYCE_MITCHELL: 130,
                    BOBBY_MOFFETT: -147,
                },
            },
            {
                'time': '20:00',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                    {
                        'name': RANDA_MARKOS,
                        'stats': '9-7-1',
                    },
                ],
                'winner': {
                    'fighter': RANDA_MARKOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:24',
                },
                'odds': {
                    RANDA_MARKOS: 125,
                    ANGELA_HILL: -141,
                },
            },
            {
                'time': '20:06',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JJ_ALDRICH,
                        'stats': '7-3-0',
                    },
                    {
                        'name': MAYCEE_BARBER,
                        'stats': '5-0-0',
                    },
                ],
                'winner': {
                    'fighter': MAYCEE_BARBER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:01',
                },
                'odds': {
                    MAYCEE_BARBER: -260,
                    JJ_ALDRICH: 226,
                },
            },
            {
                'time': '20:33',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': STEVEN_PETERSON,
                        'stats': '17-8-0',
                    },
                    {
                        'name': LUIS_PENA,
                        'stats': '6-1-0',
                    },
                ],
                'winner': {
                    'fighter': LUIS_PENA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LUIS_PENA: -229,
                    STEVEN_PETERSON: 200,
                },
            },
            {
                'time': '21:00',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JENNIFER_MAIA,
                        'stats': '16-5-1',
                    },
                    {
                        'name': ALEXIS_DAVIS,
                        'stats': '19-9-0',
                    },
                ],
                'winner': {
                    'fighter': JENNIFER_MAIA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JENNIFER_MAIA: 129,
                    ALEXIS_DAVIS: -145,
                },
            },
            {
                'time': '21:06',
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': DEIVESON_FIGUEIREDO,
                        'stats': '15-1-0',
                    },
                    {
                        'name': JUSSIER_FORMIGA,
                        'stats': '23-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUSSIER_FORMIGA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JUSSIER_FORMIGA: 155,
                    DEIVESON_FIGUEIREDO: -176,
                },
            },
            {
                'time': '21:36',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JESUS_PINEDO,
                        'stats': '16-5-1',
                    },
                    {
                        'name': JOHN_MAKDESSI,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_MAKDESSI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JOHN_MAKDESSI: -309,
                    JESUS_PINEDO: 265,
                },
            },
            {
                'time': '22:06',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_WILLIS,
                        'stats': '8-2-0',
                    },
                    {
                        'name': CURTIS_BLAYDES,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_BLAYDES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CURTIS_BLAYDES: -265,
                    JUSTIN_WILLIS: 230,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': STEPHEN_THOMPSON,
                        'stats': '14-4-1',
                    },
                    {
                        'name': ANTHONY_PETTIS,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_PETTIS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:55',
                },
                'odds': {
                    ANTHONY_PETTIS: 340,
                    STEPHEN_THOMPSON: -405,
                },
            },
        ]
    },

    {
        'date': '2019-03-30',
        'name': 'UFC Fight Night',
        'location': 'Philadelphia, Pennsylvania',
        'venue': 'Wells Fargo Center',
        'fights': [
            {
                'time': '16:10',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARK_DE_LA_ROSA,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ALEX_PEREZ,
                        'stats': '22-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_PEREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEX_PEREZ: -384,
                    MARK_DE_LA_ROSA: 308,
                },
            },
            {
                'time': '16:35',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MARYNA_MOROZ,
                        'stats': '9-3-0',
                    },
                    {
                        'name': SABINA_MAZO_ISAZA,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': MARYNA_MOROZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MARYNA_MOROZ: 155,
                    SABINA_MAZO_ISAZA: -176,
                },
            },
            {
                'time': '17:35',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': GERALD_MEERSCHAERT,
                        'stats': '28-11-0',
                    },
                    {
                        'name': KEVIN_HOLLAND,
                        'stats': '15-4-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_HOLLAND,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KEVIN_HOLLAND: -223,
                    GERALD_MEERSCHAERT: 195,
                },
            },
            {
                'time': '18:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_AGUILAR,
                        'stats': '0-0-0',
                    },
                    {
                        'name': ENRIQUE_BARZOLA,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_AGUILAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KEVIN_AGUILAR: 119,
                    ENRIQUE_BARZOLA: -134,
                },
            },
            {
                'time': '18:35',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MARINA_RODRIGUEZ,
                        'stats': '11-0-1',
                    },
                    {
                        'name': JESSICA_AGUILAR,
                        'stats': '20-8-0',
                    },
                ],
                'winner': {
                    'fighter': MARINA_RODRIGUEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'tme': '5:00',
                },
                'odds': {
                    MARINA_RODRIGUEZ: -380,
                    JESSICA_AGUILAR: 305,
                },
            },
            {
                'time': '19:35',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHEYMON_DA_SILVA_MORAES,
                        'stats': '0-0-0',
                    },
                    {
                        'name': SODIQ_YUSUFF,
                        'stats': '9-1-0',
                    },
                ],
                'winner': {
                    'fighter': SODIQ_YUSUFF,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SODIQ_YUSUFF: -148,
                    SHEYMON_DA_SILVA_MORAES: 131,
                },
            },
            {
                'time': '20:05',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': PAUL_CRAIG,
                        'stats': '11-3-0',
                    },
                    {
                        'name': KENNEDY_NZECHUKWU,
                        'stats': '6-1-0',
                    },
                ],
                'winner': {
                    'fighter': PAUL_CRAIG,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:20',
                },
                'odds': {
                    PAUL_CRAIG: 172,
                    KENNEDY_NZECHUKWU: -195,
                },
            },
            {
                'time': '20:35',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MICHELLE_WATERSON,
                        'stats': '17-6-0',
                    },
                    {
                        'name': KAROLINA_KOWALKIEWICZ,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter':MICHELLE_WATERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MICHELLE_WATERSON: 146,
                    KAROLINA_KOWALKIEWICZ: -165,
                },
            },
            {
                'time': '21:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_JOHNSON,
                        'stats': '20-14-0',
                    },
                    {
                        'name': JOSH_EMMETT,
                        'stats': '14-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOSH_EMMETT,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:14',
                },
                'odds': {
                    JOSH_EMMETT: 133,
                    MICHAEL_JOHNSON: -150,
                },
            },
            {
                'time': '21:35',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACK_HERMANSSON,
                        'stats': '19-4-0',
                    },
                    {
                        'name': DAVID_BRANCH,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_HERMANSSON,
                    'by': 'submission',
                    'round': 1,
                    'time': '0:49',
                },
                'odds': {
                    JACK_HERMANSSON: -147,
                    DAVID_BRANCH: 130,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_GAETHJE,
                        'stats': '20-2-0',
                    },
                    {
                        'name': EDSON_BARBOZA,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_GAETHJE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:30',
                },
                'odds': {
                    JUSTIN_GAETHJE: -100,
                    EDSON_BARBOZA: -112,
                },
            },
        ]
    },

    {
        'date': '2019-04-13',
        'name': 'UFC 236',
        'location': 'Atlanta, Georgia',
        'venue': 'State Farm Arena',
        'fights': [
            {
                'time': '18:15',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RANDY_COSTA,
                        'stats': '4-0-0',
                    },
                    {
                        'name': BRANDON_DAVIS,
                        'stats': '9-5-0',
                    },
                ],
                'winner': {
                    'fighter': BRANDON_DAVIS,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:13',
                },
                'odds': {
                    BRANDON_DAVIS: -178,
                    RANDY_COSTA: 157,
                },
            },
            {
                'time': '18:45',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': POLIANA_BOTELHO,
                        'stats': '7-2-0',
                    },
                    {
                        'name': LAUREN_MUELLER,
                        'stats': '5-1-0',
                    },
                ],
                'winner': {
                    'fighter': POLIANA_BOTELHO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    POLIANA_BOTELHO: -159,
                    LAUREN_MUELLER: 141,
                },
            },
            {
                'time': '19:15',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_SOUKHAMTHATH,
                        'stats': '13-6-0',
                    },
                    {
                        'name': MONTEL_JACKSON,
                        'stats': '7-1-0',
                    },
                ],
                'winner': {
                    'fighter': MONTEL_JACKSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MONTEL_JACKSON: -555,
                    ANDRE_SOUKHAMTHATH: 436,
                },
            },
            {
                'time': '19:45',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BELAL_MUHAMMAD,
                        'stats': '14-3-0',
                    },
                    {
                        'name': CURTIS_MILLENDER,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': BELAL_MUHAMMAD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    BELAL_MUHAMMAD: -150,
                    CURTIS_MILLENDER: 133,
                },
            },
            {
                'time': '20:10',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': KHALID_TAHA,
                        'stats': '12-2-0',
                    },
                    {
                        'name': BOSTON_SALMON,
                        'stats': '6-1-0',
                    },
                ],
                'winner': {
                    'fighter': KHALID_TAHA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:26',
                },
                'odds': {
                    KHALID_TAHA: 150,
                    BOSTON_SALMON: -170,
                },
            },
            {
                'time': '20:40',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ZELIM_IMADAEV,
                        'stats': '8-0-0',
                    },
                    {
                        'name': MAX_GRIFFIN,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': MAX_GRIFFIN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MAX_GRIFFIN: 113,
                    ZELIM_IMADAEV: -127,
                },
            },
            {
                'time': '21:10',
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDRE_PANTOJA,
                        'stats': '20-3-0',
                    },
                    {
                        'name': WILSON_REIS,
                        'stats': '23-9-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDRE_PANTOJA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:57',
                },
                'odds': {
                    ALEXANDRE_PANTOJA: -165,
                    WILSON_REIS: 146,
                },
            },
            {
                'time': '21:40',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MATT_FREVOLA,
                        'stats': '6-1-1',
                    },
                    {
                        'name': JALIN_TURNER,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': MATT_FREVOLA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MATT_FREVOLA: 141,
                    JALIN_TURNER: -159,
                },
            },
            {
                'time': '22:10',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': NIKITA_KRYLOV,
                        'stats': '6-1-1',
                    },
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': NIKITA_KRYLOV,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:29',
                },
                'odds': {
                    NIKITA_KRYLOV: -129,
                    OVINCE_SAINT_PREUX: 115,
                },
            },
            {
                'time': '20:40',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DWIGHT_GRANT,
                        'stats': '9-2-0',
                    },
                    {
                        'name': ALAN_JOUBAN,
                        'stats': '16-6-0',
                    },
                ],
                'winner': {
                    'fighter': DWIGHT_GRANT,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DWIGHT_GRANT: -113,
                    ALAN_JOUBAN: 101,
                },
            },
            {
                'time': '23:10',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': KHALIL_ROUNTREE,
                        'stats': '0-0-0',
                    },
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': KHALIL_ROUNTREE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KHALIL_ROUNTREE: 150,
                    ERYK_ANDERS: -170,
                },
            },
            {
                'time': '23:40',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ISRAEL_ADESANYA,
                        'stats': '16-0-0',
                    },
                    {
                        'name': KELVIN_GASTELUM,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': ISRAEL_ADESANYA,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    ISRAEL_ADESANYA: -184,
                    KELVIN_GASTELUM: 162,
                },
            },
            {
                'time': '23:59',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DUSTIN_POIRIER,
                        'stats': '24-5-0',
                    },
                    {
                        'name': MAX_HOLLOWAY,
                        'stats': '20-3-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_POIRIER,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    DUSTIN_POIRIER: 201,
                    MAX_HOLLOWAY: -230,
                },
            },
        ]
    },

    {
        'date': '2019-04-20',
        'name': 'UFC Fight Night',
        'location': 'Saint Petersburg, Russia',
        'venue': 'Yubileyny Sports Palace',
        'fights': [
            {
                'time': '10:22',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': RAFAEL_FIZIEV,
                        'stats': '6-1-0',
                    },
                    {
                        'name': MAGOMED_MUSTAFAEV,
                        'stats': '13-2-0',
                    },
                ],
                'winner': {
                    'fighter': MAGOMED_MUSTAFAEV,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:26',
                },
                'odds': {
                    MAGOMED_MUSTAFAEV: 115,
                    RAFAEL_FIZIEV: -129,
                },
            },
            {
                'time': '10:40',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MICHAL_OLEKSIEJCZUK,
                        'stats': '13-2-0',
                    },
                    {
                        'name': GADZHIMURAD_ANTIGULOV,
                        'stats': '20-5-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAL_OLEKSIEJCZUK,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:44',
                },
                'odds': {
                    MICHAL_OLEKSIEJCZUK: -201,
                    GADZHIMURAD_ANTIGULOV: 177,
                },
            },
            {
                'time': '10:55',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SHAMIL_ABDURAKHIMOV,
                        'stats': '19-4-0',
                    },
                    {
                        'name': MARCIN_TYBURA,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': SHAMIL_ABDURAKHIMOV,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:15',
                },
                'odds': {
                    SHAMIL_ABDURAKHIMOV: 115,
                    MARCIN_TYBURA: -129,
                },
            },
            {
                'time': '11:15',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_DA_SILVA,
                        'stats': '20-1-0',
                    },
                    {
                        'name': ALEXANDER_YAKOVLEV,
                        'stats': '23-8-1',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_YAKOVLEV,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:10',
                },
                'odds': {
                    ALEXANDER_YAKOVLEV: -153,
                    ALEX_DA_SILVA: 136,
                },
            },
            {
                'time': '11:35',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KEITA_NAKAMURA,
                        'stats': '34-9-2',
                    },
                    {
                        'name': SULTAN_ALIEV,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': SULTAN_ALIEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SULTAN_ALIEV: -114,
                    KEITA_NAKAMURA: 101,
                },
            },
            {
                'time': '11:55',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SEUNGWOO_CHOI,
                        'stats': '7-1-0',
                    },
                    {
                        'name': MOVSAR_EVLOEV,
                        'stats': '10-0-0',
                    },
                ],
                'winner': {
                    'fighter': MOVSAR_EVLOEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MOVSAR_EVLOEV: -480,
                    SEUNGWOO_CHOI: 396,
                },
            },
            {
                'time': '13:00',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ALEN_AMEDOVSKI,
                        'stats': '8-0-0',
                    },
                    {
                        'name': KRZYSZTOF_JOTKO,
                        'stats': '19-4-0',
                    },
                ],
                'winner': {
                    'fighter': KRZYSZTOF_JOTKO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KRZYSZTOF_JOTKO: -225,
                    ALEN_AMEDOVSKI: 197,
                },
            },
            {
                'time': '13:20',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANTONINA_SHEVCHENKO,
                        'stats': '7-0-0',
                    },
                    {
                        'name': ROXANNE_MODAFFERI,
                        'stats': '3-3-0',
                    },
                ],
                'winner': {
                    'fighter': ROXANNE_MODAFFERI,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ROXANNE_MODAFFERI: 254,
                    ANTONINA_SHEVCHENKO: -295
                },
            },
            {
                'time': '14:00',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCELO_GOLM,
                        'stats': '6-2-0',
                    },
                    {
                        'name': SERGEI_PAVLOVICH,
                        'stats': '12-1-0',
                    },
                ],
                'winner': {
                    'fighter': SERGEI_PAVLOVICH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:06',
                },
                'odds': {
                    SERGEI_PAVLOVICH: -282,
                    MARCELO_GOLM: 244,
                },
            },
            {
                'time': '14:20',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ARMAN_TSARUKYAN,
                        'stats': '12-1-0',
                    },
                    {
                        'name': ISLAM_MAKHACHEV,
                        'stats': '16-1-0',
                    },
                ],
                'winner': {
                    'fighter': ISLAM_MAKHACHEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ISLAM_MAKHACHEV: -359,
                    ARMAN_TSARUKYAN: 305,
                },
            },
            {
                'time': '14:40',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSEI_OLEINIK,
                        'stats': '57-11-1',
                    },
                    {
                        'name': ALISTAIR_OVEREEM,
                        'stats': '44-17-0,'
                    },
                ],
                'winner': {
                    'fighter': ALISTAIR_OVEREEM,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:45',
                },
                'odds': {
                    ALISTAIR_OVEREEM: -250,
                    ALEKSEI_OLEINIK: 218,
                },
            },
        ]
    },

    {
        'date': '2019-04-27',
        'name': 'UFC Fight Night',
        'location': 'Sunrise, Florida',
        'venue': 'Bb&t Center',
        'fights': [
            {
                'time': '19:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DHIEGO_LIMA,
                        'stats': '15-7-0',
                    },
                    {
                        'name': COURT_MCGEE,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': DHIEGO_LIMA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DHIEGO_LIMA: 140,
                    COURT_MCGEE: -158,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JASON_GONZALEZ,
                        'stats': '11-4-0',
                    },
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0,'
                    },
                ],
                'winner': {
                    'fighter': JIM_MILLER,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:12',
                },
                'odds': {
                    JIM_MILLER: -124,
                    JASON_GONZALEZ: 110,
                },
            },
            {
                'time': '21:05',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': AUGUSTO_SAKAI,
                        'stats': '12-1-1',
                    },
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                ],
                'winner': {
                    'fighter': AUGUSTO_SAKAI,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    AUGUSTO_SAKAI: -173,
                    ANDREI_ARLOVSKI: 153,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': TAKASHI_SATO,
                        'stats': '14-2-0',
                    },
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                ],
                'winner': {
                    'fighter': TAKASHI_SATO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:18',
                },
                'odds': {
                    TAKASHI_SATO: -235,
                    BEN_SAUNDERS: 205,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': THOMAS_GIFFORD,
                        'stats': '17-7-0',
                    },
                    {
                        'name': ROOSEVELT_ROBERTS,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': ROOSEVELT_ROBERTS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ROOSEVELT_ROBERTS: -438,
                    THOMAS_GIFFORD: 365,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CORY_SANDHAGEN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': JOHN_LINEKER,
                        'stats': '31-8-0',
                    },
                ],
                'winner': {
                    'fighter': CORY_SANDHAGEN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CORY_SANDHAGEN: 140,
                    JOHN_LINEKER: -158,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_PERRY,
                        'stats': '12-4-0',
                    },
                    {
                        'name': ALEX_OLIVEIRA,
                        'stats': '19-6-1',
                    },
                ],
                'winner': {
                    'fighter': MIKE_PERRY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MIKE_PERRY: 145,
                    ALEX_OLIVEIRA: -164,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ION_CUTELABA,
                        'stats': '14-3-0',
                    },
                    {
                        'name': GLOVER_TEIXEIRA,
                        'stats': '28-7-0',
                    },
                ],
                'winner': {
                    'fighter': GLOVER_TEIXEIRA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:37',
                },
                'odds': {
                    GLOVER_TEIXEIRA: -115,
                    ION_CUTELABA: 102,
                },
            },
            {
                'time': '23:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACK_HERMANSSON,
                        'stats': '19-4-0',
                    },
                    {
                        'name': RONALDO_SOUZA,
                        'stats': '26-6-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_HERMANSSON,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    JACK_HERMANSSON: 174,
                    RONALDO_SOUZA: -198,
                },
            },
            {
                'time': '23:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DMITRY_SMOLYAKOV,
                        'stats': '0-0-0',
                    },
                    {
                        'name': GREG_HARDY,
                        'stats': '3-1-0',
                    },
                ],
                'winner': {
                    'fighter': GREG_HARDY,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:15',
                },
                'odds': {
                    GREG_HARDY: -315,
                    DMITRY_SMOLYAKOV: 270,
                },
            },
        ]
    },

    {
        'date': '2019-05-04',
        'name': 'UFC Fight Night',
        'location': 'Ottawa, Ontario',
        'venue': 'Canadian Tire Centre',
        'fights': [
            {
                'time': '18:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': COLE_SMITH,
                        'stats': '6-0-0',
                    },
                    {
                        'name': MITCH_GAGNON,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': COLE_SMITH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    COLE_SMITH: 115,
                    MITCH_GAGNON: -129,
                },
            },
            {
                'time': '18:05',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NORDINE_TALEB,
                        'stats': '14-6-0',
                    },
                    {
                        'name': KYLE_PREPOLEC,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': NORDINE_TALEB,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    NORDINE_TALEB: -519,
                    KYLE_PREPOLEC: 400,
                },
            },
            {
                'time': '18:40',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUAN_ADAMS,
                        'stats': '5-0-0',
                    },
                    {
                        'name': ARJAN_BHULLAR,
                        'stats': '8-1-0',
                    },
                ],
                'winner': {
                    'fighter': ARJAN_BHULLAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ARJAN_BHULLAR: 120,
                    JUAN_ADAMS: -135,
                },
            },
            {
                'time': '19:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MATT_SAYLES,
                        'stats': '6-2-0',
                    },
                    {
                        'name': KYLE_NELSON,
                        'stats': '12-2-0',
                    },
                ],
                'winner': {
                    'fighter': MATT_SAYLES,
                    'by': 'submission',
                    'round': 3,
                    'time': '3:16',
                },
                'odds': {
                    MATT_SAYLES: -187,
                    KYLE_NELSON: 165,
                },
            },
            {
                'time': '20:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': VINCE_MORALES,
                        'stats': '0-0-0',
                    },
                    {
                        'name': AIEMANN_ZAHABI,
                        'stats': '7-1-0',
                    },
                ],
                'winner': {
                    'fighter': VINCE_MORALES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    VINCE_MORALES: 160,
                    AIEMANN_ZAHABI: -181,
                },
            },
            {
                'time': '21:05',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANDREW_SANCHEZ,
                        'stats': '11-4-0',
                    },
                    {
                        'name': MARC_ANDRE_BARRIAULT,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter':ANDREW_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANDREW_SANCHEZ: -153,
                    MARC_ANDRE_BARRIAULT: 136,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SERGEY_SPIVAK,
                        'stats': '9-0-0',
                    },
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': WALT_HARRIS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:50',
                },
                'odds': {
                    WALT_HARRIS: -170,
                    SERGEY_SPIVAK: 150,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHANE_BURGOS,
                        'stats': '11-1-0',
                    },
                    {
                        'name': CUB_SWANSON,
                        'stats': '25-10-0',
                    },
                ],
                'winner': {
                    'fighter': SHANE_BURGOS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SHANE_BURGOS: -181,
                    CUB_SWANSON: 160,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MERAB_DVALISHVILI,
                        'stats': '8-4-0',
                    },
                    {
                        'name': BRAD_KATONA,
                        'stats': '9-0-0',
                    },
                ],
                'winner': {
                    'fighter': MERAB_DVALISHVILI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MERAB_DVALISHVILI: -152,
                    BRAD_KATONA: 135,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                    {
                        'name': AL_IAQUINTA,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': DONALD_CERRONE,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    DONALD_CERRONE: 115,
                    AL_IAQUINTA: -129,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ELIAS_THEODOROU,
                        'stats': '17-2-0',
                    },
                    {
                        'name': DEREK_BRUNSON,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': DEREK_BRUNSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DEREK_BRUNSON: 102,
                    ELIAS_THEODOROU: -115,
                },
            },
        ]
    },

    {
        'date': '2019-05-11',
        'name': 'UFC 237',
        'location': 'Rio de Janeiro, Brazil',
        'venue': 'Jeunesse Arena',
        'fights': [
            {
                'time': '19:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RAONI_BARCELOS,
                        'stats': '13-1-0',
                    },
                    {
                        'name': CARLOS_HUACHIN_QUIROZ,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': RAONI_BARCELOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:49',
                },
                'odds': {
                    CARLOS_HUACHIN_QUIROZ: 721,
                    RAONI_BARCELOS: -1099,
                },
            },
            {
                'time': '19:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': LUANA_CAROLINA,
                        'stats': '5-1-0',
                    },
                    {
                        'name': PRISCILA_CACHOEIRA,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': LUANA_CAROLINA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    PRISCILA_CACHOEIRA: 155,
                    LUANA_CAROLINA: -176,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CLAY_GUIDA,
                        'stats': '34-15-0',
                    },
                    {
                        'name': BJ_PENN,
                        'stats': '16-13-2'
                    },
                ],
                'winner': {
                    'fighter': CLAY_GUIDA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CLAY_GUIDA: -697,
                    BJ_PENN: 510,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                    {
                        'name': WARLLEY_ALVES,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': WARLLEY_ALVES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:13',
                },
                'odds': {
                    SERGIO_MORAES: 118,
                    WARLLEY_ALVES: -133,
                },
            },
            {
                'time': '21:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KURT_HOLOBAUGH,
                        'stats': '17-6-0',
                    },
                    {
                        'name': THIAGO_MOISES,
                        'stats': '11-3-0',
                    }
                ],
                'winner': {
                    'fighter': THIAGO_MOISES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KURT_HOLOBAUGH: 115,
                    THIAGO_MOISES: -129,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_SPANN,
                        'stats': '15-5-0',
                    },
                    {
                        'name': ROGERIO_NOGUEIRA,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_SPANN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:07',
                },
                'odds': {
                    RYAN_SPANN: -135,
                    ROGERIO_NOGUEIRA: 120,
                },
            },
            {
                'time': '22:00',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BETHE_CORREIA,
                        'stats': '10-3-1',
                    },
                    {
                        'name': IRENE_ALDANA,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': IRENE_ALDANA,
                    'by': 'submission',
                    'round': 3,
                    'time': '3:24',
                },
                'odds': {
                    BETHE_CORREIA: 310,
                    IRENE_ALDANA: -387,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LAUREANO_STAROPOLI,
                        'stats': '8-1-0',
                    },
                    {
                        'name': THIAGO_ALVES,
                        'stats': '28-13-0',
                    },
                ],
                'winner': {
                    'fighter': LAUREANO_STAROPOLI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LAUREANO_STAROPOLI: 110,
                    THIAGO_ALVES: -124,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': JOSE_ALDO,
                        'stats': '28-4-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEXANDER_VOLKANOVSKI: 114,
                    JOSE_ALDO: -128,
                },
            },
            {
                'time': '23:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANDERSON_SILVA,
                        'stats': '34-9-0',
                    },
                    {
                        'name': JARED_CANNONIER,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': JARED_CANNONIER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:47',
                },
                'odds': {
                    JARED_CANNONIER: -124,
                    ANDERSON_SILVA: 110,
                },
            },
            {
                'time': '23:59',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ROSE_NAMAJUNAS,
                        'stats': '9-3-0',
                    },
                    {
                        'name': JESSICA_ANDRADE,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ANDRADE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:58',
                },
                'odds': {
                    ROSE_NAMAJUNAS: 134,
                    JESSICA_ANDRADE: -151,
                },
            },
        ]
    },

    {
        'date': '2019-05-18',
        'name': 'UFC Fight Night',
        'location': 'Rochester, Michigan',
        'venue': 'Blue Cross Arena',
        'fights': [
            {
                'time': '17:35',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TREVIN_GILES,
                        'stats': '11-0-0',
                    },
                    {
                        'name': ZAK_CUMMINGS,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': ZAK_CUMMINGS,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:01',
                },
                'odds': {
                    TREVIN_GILES: -193,
                    ZAK_CUMMINGS: 170,
                },
            },
            {
                'time': '18:05',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ED_HERMAN,
                        'stats': '24-14-0',
                    },
                    {
                        'name': PATRICK_CUMMINS,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': ED_HERMAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:39',
                },
                'odds': {
                    ED_HERMAN: 230,
                    PATRICK_CUMMINS: -265,
                },
            },
            {
                'time': '18:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JULIAN_EROSA,
                        'stats': '22-8-0',
                    },
                    {
                        'name': JULIO_ACRE,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': JULIO_ACRE,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:49',
                },
                'odds': {
                    JULIAN_EROSA: 560,
                    JULIO_ACRE: -822,
                },
            },
            {
                'time': '18:24',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': GRANT_DAWSON,
                        'stats': '13-1-0',
                    },
                    {
                        'name': MICHAEL_TRIZANO,
                        'stats': '9-0-0',
                    },
                ],
                'winner': {
                    'fighter': GRANT_DAWSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:27',
                },
                'odds': {
                    GRANT_DAWSON: -158,
                    MICHAEL_TRIZANO: 140,
                },
            },
            {
                'time': '18:45',
                'gender': 'mens',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICHEL_PEREIRA,
                        'stats': '22-9-0',
                    },
                    {
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': MICHEL_PEREIRA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:47',
                },
                'odds': {
                    MICHEL_PEREIRA: 200,
                    DANNY_ROBERTS: -229,
                },
            },
            {
                'time': '19:12',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_JOURDAIN,
                        'stats': '0-0-0',
                    },
                    {
                        'name': DESMOND_GREEN,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': DESMOND_GREEN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CHARLES_JOURDAIN: 550,
                    DESMOND_GREEN: -803,
                },
            },
            {
                'time': '19:45',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': SIJARA_EUBANKS,
                        'stats': '5-2-0',
                    },
                    {
                        'name': ASPEN_LADD,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': ASPEN_LADD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SIJARA_EUBANKS: 220,
                    ASPEN_LADD: -253,
                },
            },
            {
                'time': '20:45',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:11',
                },
                'odds': {
                    NIK_LENTZ: 320,
                    CHARLES_OLIVEIRA: -401,
                },
            },
            {
                'time': '21:35',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': AUSTIN_HUBBARD,
                        'stats': '10-2-0',
                    },
                    {
                        'name': DAVI_RAMOS,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAVI_RAMOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    AUSTIN_HUBBARD: 390,
                    DAVI_RAMOS: -504,
                },
            },
            {
                'time': '21:35',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DERRICK_KRANTZ,
                        'stats': '0-0-0',
                    },
                    {
                        'name': VICENTE_LUQUE,
                        'stats': '15-6-1',
                    },
                ],
                'winner': {
                    'fighter': VICENTE_LUQUE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:52',
                },
                'odds': {
                    DERRICK_KRANTZ: 700,
                    VICENTE_LUQUE: -1120,
                },
            },
            {
                'time': '21:59',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': IAN_HEINISCH,
                        'stats': '12-1-0',
                    },
                    {
                        'name': ANTONIO_CARLOS_JUNIOR,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': IAN_HEINISCH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    IAN_HEINISCH: 145,
                    ANTONIO_CARLOS_JUNIOR: -164,
                },
            },
            {
                'time': '22:15',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': RAFAEL_DOS_ANJOS,
                    'by': 'submission',
                    'round': 4,
                    'time': '3;47',
                },
                'odds': {
                    KEVIN_LEE: -144,
                    RAFAEL_DOS_ANJOS: 128,
                },
            },
            {
                'time': '23:05',
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': FELICIA_SPENCER,
                        'stats': '6-0-0',
                    },
                    {
                        'name': MEGAN_ANDERSON,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': FELICIA_SPENCER,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:24',
                },
                'odds': {
                    FELICIA_SPENCER: 180,
                    MEGAN_ANDERSON: -205,
                },
            },
        ]
    },

    {
        'date': '2019-06-01',
        'name': 'UFC Fight Night',
        'location': 'Stockholm, Sweden',
        'venue': 'Ericsson Globe',
        'fights': [
            {
                'time': '10:10',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DANILO_BELLUARDO,
                        'stats': '12-3-0',
                    },
                    {
                        'name': JOEL_ALVAREZ,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOEL_ALVAREZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:22',
                },
                'odds': {
                    DANILO_BELLUARDO: -103,
                    JOEL_ALVAREZ: -109,
                },
            },
            {
                'time': '10:35',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DEVIN_CLARK,
                        'stats': '9-3-0',
                    },
                    {
                        'name': DARKO_STOSIC,
                        'surname': 'STOSIC',
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': DEVIN_CLARK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DEVIN_CLARK: -115,
                    DARKO_STOSIC: 102,
                },
            },
            {
                'time': '11:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': EDUARDA_SANTANA,
                        'stats': '0-0-0',
                    },
                    {
                        'name': BEA_MALECKI,
                        'stats': '2-0-0',
                    },
                ],
                'winner': {
                    'fighter': BEA_MALECKI,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:59',
                },
                'odds': {
                    EDUARDA_SANTANA: 108,
                    BEA_MALECKI: -121,
                },
            },
            {
                'time': '11:35',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FRANK_CAMACHO,
                        'stats': '21-7-0',
                    },
                    {
                        'name': NICK_HEIN,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': FRANK_CAMACHO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:56',
                },
                'odds': {
                    FRANK_CAMACHO: -138,
                    NICK_HEIN: 123,
                },
            },
            {
                'time': '12:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': LEONARDO_SANTOS,
                        'stats': '16-4-1',
                    },
                    {
                        'name': STEVIE_RAY,
                        'stats': '22-7-0',
                    },
                ],
                'winner': {
                    'fighter': LEONARDO_SANTOS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:17',
                },
                'odds': {
                    LEONARDO_SANTOS: -150,
                    STEVIE_RAY: 133,
                },
            },
            {
                'time': '12:35',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LINA_LANSBERG,
                        'stats': '8-4-0',
                    },
                    {
                        'name': TONYA_EVINGER,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': LINA_LANSBERG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LINA_LANSBERG: 323,
                    TONYA_EVINGER: -382,
                },
            },
            {
                'time': '13:05',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SERGEY_KHANDOZHKO,
                        'stats': '25-5-0',
                    },
                    {
                        'name': ROSTEM_AKMAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': SERGEY_KHANDOZHKO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SERGEY_KHANDOZHKO: -155,
                    ROSTEM_AKMAN: 137,
                },
            },
            {
                'time': '13:35',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SUNG_BIN_JO,
                        'stats': '0-0-0',
                    },
                    {
                        'name': DANIEL_TEYMUR,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_TEYMUR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SUNG_BIN_JO: -118,
                    DANIEL_TEYMUR: 105,
                },
            },
            {
                'time': '14:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHRISTOS_GIAGOS,
                        'stats': '16-7-0',
                    },
                    {
                        'name': DAMIR_HADZOVIC,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': CHRISTOS_GIAGOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CHRISTOS_GIAGOS: 133,
                    DAMIR_HADZOVIC: -150,
                },
            },
            {
                'time': '14:35',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_FISHGOLD,
                        'stats': '18-2-1',
                    },
                    {
                        'name': MAKWAN_AMIRKHANI,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAKWAN_AMIRKHANI,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:25',
                },
                'odds': {
                    CHRIS_FISHGOLD: 112,
                    MAKWAN_AMIRKHANI: -126,
                },
            },
            {
                'time': '15:05',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSANDAR_RAKIC,
                        'surname': 'RAKIC',
                        'stats': '1-1-0',
                    },
                    {
                        'name': JIMI_MANUWA,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSANDAR_RAKIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:42',
                },
                'odds': {
                    ALEKSANDAR_RAKIC: -270,
                    JIMI_MANUWA: 234,
                },
            },
            {
                'time': '15:35',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': ALEXANDER_GUSTAFSSON,
                        'stats': '18-5-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_SMITH,
                    'by': 'submission',
                    'round': 4,
                    'time': '2:38',
                },
                'odds': {
                    ANTHONY_SMITH: 277,
                    ALEXANDER_GUSTAFSSON: -324,
                },
            },
        ],
    },

    {
        'date': '2019-06-08',
        'name': 'UFC 238',
        'location': 'Chicago, Illinois',
        'venue': 'United Center',
        'fights': [
            {
                'time': '18:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOANNE_CALDERWOOD,
                        'stats': '13-3-0',
                    },
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    }
                ],
                'winner': {
                    'fighter': KATLYN_CHOOKAGIAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JOANNE_CALDERWOOD: -102,
                    KATLYN_CHOOKAGIAN: -110,
                },
            },
            {
                'time': '18:48',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GRIGORY_POPOV,
                        'stats': '0-0-0',
                    },
                    {
                        'name': EDDIE_WINELAND,
                        'stats': '23-13-1',
                    },
                ],
                'winner': {
                    'fighter': EDDIE_WINELAND,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:47',
                },
                'odds': {
                    GRIGORY_POPOV: 142,
                    EDDIE_WINELAND: -160,
                },
            },
            {
                'time': '19:15',
                'class_weight': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                    {
                        'name': BEVON_LEWIS,
                        'stats': '5-1-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_STEWART,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DARREN_STEWART: 158,
                    BEVON_LEWIS: -179,
                },
            },
            {
                'time': '19:35',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                    {
                        'name': YAN_XIAONAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': YAN_XIAONAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANGELA_HILL: 205,
                    YAN_XIAONAN: -235,
                },
            },
            {
                'time': '20:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CALVIN_KATTAR,
                        'stats': '19-3-0',
                    },
                    {
                        'name': RICARDO_LAMAS,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': CALVIN_KATTAR,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:06',
                },
                'odds': {
                    CALVIN_KATTAR: -164,
                    RICARDO_LAMAS: 145,
                },
            },
            {
                'time': '20:30',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ALEXA_GRASSO,
                        'stats': '10-2-0',
                    },
                    {
                        'name': KAROLINA_KOWALKIEWICZ,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXA_GRASSO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEXA_GRASSO: -121,
                    KAROLINA_KOWALKIEWICZ: 108,
                },
            },
            {
                'time': '21:12',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                    {
                        'name': ALJAMAIN_STERLING,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALJAMAIN_STERLING,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    PEDRO_MUNHOZ: 145,
                    ALJAMAIN_STERLING: -164,
                },
            },
            {
                'time': '21:30',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': NINA_ANSAROFF,
                        'stats': '10-5-0',
                    },
                    {
                        'name': TATIANA_SUAREZ,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': TATIANA_SUAREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    NINA_ANSAROFF: 525,
                    TATIANA_SUAREZ: -755,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': BLAGOY_IVANOV,
                        'stats': '17-2-0',
                    },
                    {
                        'name': TAI_TUIVASA,
                        'stats': '10-1-0',
                    },
                ],
                'winner': {
                    'fighter': BLAGOY_IVANOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    BLAGOY_IVANOV: 140,
                    TAI_TUIVASA: -158,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PETR_YAN,
                        'stats': '12-1-0',
                    },
                    {
                        'name': JIMMIE_RIVERA,
                        'stats': '22-3-0',
                    },
                ],
                'winner': {
                    'fighter': PETR_YAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    PETR_YAN: -334,
                    JIMMIE_RIVERA: 285,
                },
            },
            {
                'time': '23:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                    {
                        'name': TONY_FERGUSON,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': TONY_FERGUSON,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'odds': {
                    DONALD_CERRONE: 193,
                    TONY_FERGUSON: -220,
                },
            },
            {
                'time': '23:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JESSICA_EYE,
                        'stats': '14-6-0',
                    },
                    {
                        'name': VALENTINA_SHEVCHENKO,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': VALENTINA_SHEVCHENKO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:26',
                },
                'odds': {
                    JESSICA_EYE: 775,
                    VALENTINA_SHEVCHENKO: -1305,
                },
            },
            {
                'time': '23:57',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': HENRY_CEJUDO,
                        'stats': '14-2-0',
                    },
                    {
                        'name': MARLON_MORAES,
                        'stats': '22-5-1',
                    },
                ],
                'winner': {
                    'fighter': HENRY_CEJUDO,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:51',
                },
                'odds': {
                    HENRY_CEJUDO: 137,
                    MARLON_MORAES: -155,
                },
            },
        ]
    },

    {
        'date': '2019-06-22',
        'name': 'UFC Fight Night',
        'location': 'Greenville, South Carolina',
        'venue': 'Bon Secours Wellness Arena',
        'fights': [
            {
                'time': '16:05',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DERON_WINN,
                        'stats': '7-1-0',
                    },
                    {
                        'name': ERIC_SPICELY,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': DERON_WINN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ERIC_SPICELY: 290,
                    DERON_WINN: -340,
                }
            },
            {
                'time': '16:35',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MATT_WIMAN,
                        'stats': '16-7-0',
                    },
                    {
                        'name': LUIS_PENA,
                        'stats': '6-1-0',
                    },
                ],
                'winner': {
                    'fighter': LUIS_PENA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:14',
                },
                'odds': {
                    MATT_WIMAN: 285,
                    LUIS_PENA: -352,
                }
            },
            {
                'time': '17:35',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': DAN_IGE,
                        'stats': '11-2-0',
                    },
                    {
                        'name': KEVIN_AGUILAR,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_IGE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DAN_IGE: 121,
                    KEVIN_AGUILAR: -136,
                }
            },
            {
                'time': '18:35',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ARIANE_LIPSKI,
                        'stats': '11-4-0',
                    },
                    {
                        'name': MOLLY_MCCANN,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': MOLLY_MCCANN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MOLLY_MCCANN: 205,
                    ARIANE_LIPSKI: -235,
                },
            },
            {
                'time': '20:00',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ASHLEY_YODER,
                        'stats': '6-4-0',
                    },
                    {
                        'name': SYURI_KONDO,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': ASHLEY_YODER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SYURI_KONDO: 120,
                    ASHLEY_YODER: -135,
                }
            },
            {
                'time': '20:22',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_EWELL,
                        'stats': '13-5-0',
                    },
                    {
                        'name': ANDERSON_BERLINGERI_DOS_SANTOS,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_EWELL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANDERSON_BERLINGERI_DOS_SANTOS: 120,
                    ANDRE_EWELL: -135,
                }
            },
            {
                'time': '20:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_HOLLAND,
                        'stats': '15-4-0',
                    },
                    {
                        'name': ALESSIO_DI_CHRICO,
                        'stats': '12-2-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_HOLLAND,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALESSIO_DI_CHRICO: 186,
                    KEVIN_HOLLAND: -212,
                },
            },
            {
                'time': '20:45',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BRYAN_BARBERENA,
                        'stats': '14-6-0',
                    },
                    {
                        'name': RANDY_BROWN,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': RANDY_BROWN,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:54',
                },
                'odds': {
                    RANDY_BROWN: 198,
                    BRYAN_BARBERENA: -237,
                },
            },
            {
                'time': '21:10',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RENATO_MOICANO,
                        'stats': '13-2-1',
                    },
                    {
                        'name': CHAN_SUNG_JUNG,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': CHAN_SUNG_JUNG,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:58'
                },
                'odds': {
                    CHAN_SUNG_JUNG: 187,
                    RENATO_MOICANO: -213,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALLEN_CROWDER,
                        'stats': '10-3-0',
                    },
                    {
                        'name': JAIRZINHO_ROZENSTRUIK,
                        'stats': '6-0-0',
                    },
                ],
                'winner': {
                    'fighter': JAIRZINHO_ROZENSTRUIK,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:09',
                },
                'odds': {
                    JAIRZINHO_ROZENSTRUIK: -223,
                    ALLEN_CROWDER: 195,
                },
            },
            {
                'time': '22:00',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANDREA_LEE,
                        'stats': '10-2-0',
                    },
                    {
                        'name': MONTANA_DE_LA_ROSA,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANDREA_LEE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MONTANA_DE_LA_ROSA: 150,
                    ANDREA_LEE: -170,
                },
            },
        ]
    }
]
