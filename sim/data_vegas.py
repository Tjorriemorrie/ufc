from fighters import *


DATA = [
    {
        'date': '2017-01-15',
        'name': 'UFC Fight Night: Rodriguez vs Penn',
        'location': 'Phoenix, Arizona',
        'venue': 'Talking Stick Resort Arena',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DMITRII_SMOLIAKOV,
                        'stats': '8-2-0',
                    },
                    {
                        'name': CYRIL_ASKER,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': CYRIL_ASKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:41',
                },
                'time': '18:25',
                'odds': {
                    CYRIL_ASKER: -118,
                    DMITRII_SMOLIAKOV: -102,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JOACHIM_CHRISTENSEN,
                        'stats': '14-6-0',
                    },
                    {
                        'name': BOJAN_MIHAJLOVIC,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': JOACHIM_CHRISTENSEN,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:05',
                },
                'time': '18:25',
                'odds': {
                    JOACHIM_CHRISTENSEN: -235,
                    BOJAN_MIHAJLOVIC: 205,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': CHASE_SHERMAN,
                        'stats': '11-5-0',
                    },
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': WALT_HARRIS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:41',
                },
                'time': '19:10',
                'odds': {
                    WALT_HARRIS: -150,
                    CHASE_SHERMAN: 133,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JOCELYN_JONES_LYBARGER,
                        'stats': '6-4-0',
                    },
                    {
                        'name': NINA_ANSAROFF,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': NINA_ANSAROFF,
                    'by': 'submission',
                    'round': 3,
                    'time': '3:39',
                },
                'time': '19:35',
                'odds': {
                    NINA_ANSAROFF: -176,
                    JOCELYN_JONES_LYBARGER: 155,
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
                'time': '20:05',
                'odds': {
                    ANTHONY_ROCCO_MARTIN: -164,
                    ALEX_WHITE: 145,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': VIKTOR_PESTA,
                        'stats': '10-4-0',
                    },
                    {
                        'name': ALEKSEI_OLEINIK,
                        'stats': '57-11-1',
                    },
                ],
                'winner': {
                    'fighter': ALEKSEI_OLEINIK,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:57',
                },
                'time': '20:35',
                'odds': {
                    ALEKSEI_OLEINIK: -135,
                    VIKTOR_PESTA: 120,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': AUGUSTO_MENDES,
                        'stats': '6-2-0',
                    },
                    {
                        'name': FRANKIE_SAENZ,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': AUGUSTO_MENDES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:05',
                'odds': {
                    AUGUSTO_MENDES: 135,
                    FRANKIE_SAENZ: -152,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DRAKKAR_KLOSE,
                        'stats': '10-1-1',
                    },
                    {
                        'name': DEVIN_POWELL,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': DRAKKAR_KLOSE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:35',
                'odds': {
                    DRAKKAR_KLOSE: -305,
                    DEVIN_POWELL: 262,
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
                        'name': JOHN_MORAGA,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': SERGIO_PETTIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:10',
                'odds': {
                    SERGIO_PETTIS: -147,
                    JOHN_MORAGA: 130,
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
                        'name': COURT_MCGEE,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': BEN_SAUNDERS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:35',
                'odds': {
                    BEN_SAUNDERS: 115,
                    COURT_MCGEE: -129,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MARCIN_HELD,
                        'stats': '23-7-0',
                    },
                    {
                        'name': JOE_LAUZON,
                        'stats': '27-16-0',
                    },
                ],
                'winner': {
                    'fighter': JOE_LAUZON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:05',
                'odds': {
                    JOE_LAUZON: -135,
                    MARCIN_HELD: 120,
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
                        'name': BJ_PENN,
                        'stats': '16-13-2',
                    },
                ],
                'winner': {
                    'fighter': YAIR_RODRIGUEZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:24',
                },
                'time': '23:35',
                'odds': {
                    YAIR_RODRIGUEZ: -359,
                    BJ_PENN: 305,
                },
            },
        ]
    },

    {
        'date': '2017-01-28',
        'name': 'UFC Fight Night: Shevchenko vs Pena',
        'location': 'Denver, Colorado',
        'venue': 'Pepsi Center',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JASON_GONZALEZ,
                        'stats': '11-4-0',
                    },
                    {
                        'name': JC_COTTRELL,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': JASON_GONZALEZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:54',
                },
                'time': '16:05',
                'odds': {
                    JASON_GONZALEZ: 110,
                    JC_COTTRELL: -124,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ERIC_SHELTON,
                        'stats': '12-6-0',
                    },
                    {
                        'name': ALEXANDRE_PANTOJA,
                        'stats': '20-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDRE_PANTOJA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:35',
                'odds': {
                    ALEXANDRE_PANTOJA: -100,
                    ERIC_SHELTON: -112,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JEREMY_KIMBALL,
                        'stats': '15-8-0',
                    },
                    {
                        'name': MARCOS_ROGERIO_DE_LIMA,
                        'stats': '16-7-1',
                    },
                ],
                'winner': {
                    'fighter': MARCOS_ROGERIO_DE_LIMA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:27',
                },
                'time': '17:05',
                'odds': {
                    MARCOS_ROGERIO_DE_LIMA: -141,
                    JEREMY_KIMBALL: 125,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ERIC_SPICELY,
                        'stats': '10-5-0',
                    },
                    {
                        'name': ALESSIO_DI_CHRICO,
                        'stats': '12-2-0',
                    },
                ],
                'winner': {
                    'fighter': ERIC_SPICELY,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:14',
                },
                'time': '17:35',
                'odds': {
                    ERIC_SPICELY: -101,
                    ALESSIO_DI_CHRICO: -111,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_JOHNSON,
                        'stats': '10-0-0',
                    },
                    {
                        'name': HENRIQUE_DA_SILVA,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_JOHNSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:05',
                'odds': {
                    JORDAN_JOHNSON: -190,
                    HENRIQUE_DA_SILVA: 167,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BOBBY_NASH,
                        'stats': '8-4-0',
                    },
                    {
                        'name': LI_JINGLIANG,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': LI_JINGLIANG,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:45',
                },
                'time': '18:35',
                'odds': {
                    LI_JINGLIANG: -140,
                    BOBBY_NASH: 124,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ALJAMAIN_STERLING,
                        'stats': '17-3-0',
                    },
                    {
                        'name': RAPHAEL_ASSUNCAO,
                        'stats': '27-6-0',
                    },
                ],
                'winner': {
                    'fighter': RAPHAEL_ASSUNCAO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:05',
                'odds': {
                    RAPHAEL_ASSUNCAO: -139,
                    ALJAMAIN_STERLING: 123,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
                    },
                    {
                        'name': NATE_MARQUARDT,
                        'stats': '38-19-2',
                    },
                ],
                'winner': {
                    'fighter': SAM_ALVEY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    SAM_ALVEY: -141,
                    NATE_MARQUARDT: 125,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JASON_KNIGHT,
                        'stats': '20-6-0',
                    },
                    {
                        'name': ALEX_CACERES,
                        'stats': '14-12-0',
                    },
                ],
                'winner': {
                    'fighter': JASON_KNIGHT,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:21',
                },
                'time': '20:10',
                'odds': {
                    JASON_KNIGHT: -127,
                    ALEX_CACERES: 113,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': FRANCIS_NGANNOU,
                        'stats': '13-3-0',
                    },
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCIS_NGANNOU,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:32',
                },
                'time': '20:40',
                'odds': {
                    FRANCIS_NGANNOU: -385,
                    ANDREI_ARLOVSKI: 325,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JORGE_MASVIDAL,
                        'stats': '33-13-0',
                    },
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                ],
                'winner': {
                    'fighter': JORGE_MASVIDAL,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:00',
                },
                'time': '21:05',
                'odds': {
                    JORGE_MASVIDAL: 145,
                    DONALD_CERRONE: -164,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': VALENTINA_SHEVCHENKO,
                        'stats': '16-3-0',
                    },
                    {
                        'name': JULIANNA_PENA,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': VALENTINA_SHEVCHENKO,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:29',
                },
                'time': '21:35',
                'odds': {
                    VALENTINA_SHEVCHENKO: -173,
                    JULIANNA_PENA: 153,
                },
            },
        ]
    },

    {
        'date': '2017-02-04',
        'name': 'UFC Fight Night: Bermudez vs The Korean Zombie',
        'location': 'Houston, Texas',
        'venue': 'Toyota Center',
        'fights': [
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': KHALIL_ROUNTREE,
                        'stats': '8-2-0',
                    },
                    {
                        'name': DANIEL_JOLLY,
                        'stats': '5-2-0',
                    },
                ],
                'winner': {
                    'fighter': KHALIL_ROUNTREE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:52',
                },
                'time': '19:05',
                'odds': {
                    KHALIL_ROUNTREE: -170,
                    DANIEL_JOLLY: 150,
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
                        'name': ALEX_MORONO,
                        'stats': '16-5-0',
                    },
                ],
                'winner': {
                    'fighter': NIKO_PRICE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    NIKO_PRICE: -112,
                    ALEX_MORONO: -100,
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
                        'name': BEC_RAWLINGS,
                        'stats': '7-8-0',
                    },
                ],
                'winner': {
                    'fighter': TECIA_TORRES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    TECIA_TORRES: -385,
                    BEC_RAWLINGS: 325,
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
                        'name': MICHINORI_TANAKA,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_RAMOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    RICARDO_RAMOS: 110,
                    MICHINORI_TANAKA: -124,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CHAS_SKELLY,
                        'stats': '17-3-0',
                    },
                    {
                        'name': CHRIS_GRUETZEMACHER,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': CHAS_SKELLY,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:01',
                },
                'time': '21:05',
                'odds': {
                    CHAS_SKELLY: -315,
                    CHRIS_GRUETZEMACHER: 270,
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
                        'name': ADAM_MILSTEAD,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_BLAYDES,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:59',
                },
                'time': '21:35',
                'odds': {
                    CURTIS_BLAYDES: -353,
                    ADAM_MILSTEAD: 300,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                    {
                        'name': JESSICA_ANDRADE,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ANDRADE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:10',
                'odds': {
                    JESSICA_ANDRADE: -634,
                    ANGELA_HILL: 505,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCEL_FORTUNA,
                        'stats': '9-3-0',
                    },
                    {
                        'name': ANTHONY_HAMILTON,
                        'stats': '15-9-0',
                    },
                ],
                'winner': {
                    'fighter': MARCEL_FORTUNA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:10',
                },
                'time': '22:30',
                'odds': {
                    MARCEL_FORTUNA: 220,
                    ANTHONY_HAMILTON: -253,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': VOLKAN_OEZDEMIR,
                        'stats': '15-4-0',
                    },
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '23-12-0',
                    },
                ],
                'winner': {
                    'fighter': VOLKAN_OEZDEMIR,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:05',
                'odds': {
                    VOLKAN_OEZDEMIR: 325,
                    OVINCE_SAINT_PREUX: -385,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JAMES_VICK,
                        'stats': '13-3-0',
                    },
                    {
                        'name': ABEL_TRUJILLO,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': JAMES_VICK,
                    'by': 'submission',
                    'round': 3,
                    'time': '0:49',
                },
                'time': '23:35',
                'odds': {
                    JAMES_VICK: -131,
                    ABEL_TRUJILLO: 116,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ALEXA_GRASSO,
                        'stats': '10-2-0',
                    },
                    {
                        'name': FELICE_HERRIG,
                        'stats': '14-8-0',
                    },
                ],
                'winner': {
                    'fighter': FELICE_HERRIG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:45',
                'odds': {
                    FELICE_HERRIG: 325,
                    ALEXA_GRASSO: -385,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CHAN_SUNG_JUNG,
                        'stats': '14-5-0',
                    },
                    {
                        'name': DENNIS_BERMUDEZ,
                        'stats': '18-9-0',
                    },
                ],
                'winner': {
                    'fighter': CHAN_SUNG_JUNG,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:49',
                },
                'time': '23:59',
                'odds': {
                    CHAN_SUNG_JUNG: 160,
                    DENNIS_BERMUDEZ: -181,
                },
            },
        ]
    },

    {
        'date': '2017-02-11',
        'name': 'UFC 208: Holm vs de Randamie',
        'location': 'Brooklyn, New York',
        'venue': 'Barclays Center',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ROAN_CARNEIRO,
                        'stats': '21-11-0',
                    },
                    {
                        'name': RYAN_LAFLARE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_LAFLARE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    RYAN_LAFLARE: -296,
                    ROAN_CARNEIRO: 255,
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
                        'name': PHILLIPE_NOVER,
                        'stats': '12-8-1',
                    },
                ],
                'winner': {
                    'fighter': RICK_GLENN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    RICK_GLENN: -176,
                    PHILLIPE_NOVER: 155,
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
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                ],
                'winner': {
                    'fighter': ISLAM_MAKHACHEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    ISLAM_MAKHACHEV: -309,
                    NIK_LENTZ: 265,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ULKA_SASAKI,
                        'stats': '21-6-2',
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
                'time': '21:05',
                'odds': {
                    WILSON_REIS: -591,
                    ULKA_SASAKI: 475,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BELAL_MUHAMMAD,
                        'stats': '14-3-0',
                    },
                    {
                        'name': RANDY_BROWN,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': BELAL_MUHAMMAD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:35',
                'odds': {
                    BELAL_MUHAMMAD: 127,
                    RANDY_BROWN: -143,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DUSTIN_POIRIER,
                        'stats': '24-5-0',
                    },
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_POIRIER,
                    'by': '24-5-0',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:15',
                'odds': {
                    DUSTIN_POIRIER: -485,
                    JIM_MILLER: 400,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JARED_CANNONIER,
                        'stats': '11-4-0',
                    },
                    {
                        'name': GLOVER_TEIXEIRA,
                        'stats': '28-7-0',
                    },
                ],
                'winner': {
                    'fighter': GLOVER_TEIXEIRA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:45',
                'odds': {
                    GLOVER_TEIXEIRA: -223,
                    JARED_CANNONIER: 195,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACARE_SOUZA,
                        'stats': '26-6-0',
                    },
                    {
                        'name': TIM_BOETSCH,
                        'stats': '21-13-0',
                    },
                ],
                'winner': {
                    'fighter': JACARE_SOUZA,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:41',
                },
                'time': '23:10',
                'odds': {
                    JACARE_SOUZA: -555,
                    TIM_BOETSCH: 450,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANDERSON_SILVA,
                        'stats': '34-9-0',
                    },
                    {
                        'name': DEREK_BRUNSON,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': ANDERSON_SILVA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:40',
                'odds': {
                    ANDERSON_SILVA: 107,
                    DEREK_BRUNSON: -120,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HOLLY_HOLM,
                        'stats': '12-4-0',
                    },
                    {
                        'name': GERMAINE_DE_RANDAMIE,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': GERMAINE_DE_RANDAMIE,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    GERMAINE_DE_RANDAMIE: -127,
                    HOLLY_HOLM: 113,
                },
            },
        ]
    },

    {
        'date': '2017-02-19',
        'name': 'UFC Fight Night: Lewis vs Browne',
        'location': 'Halifax, Nova Scotia',
        'venue': 'Scotiabank Centre',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': GERALD_MEERSCHAERT,
                        'stats': '28-11-0',
                    },
                    {
                        'name': RYAN_JANES,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': GERALD_MEERSCHAERT,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:34',
                },
                'time': '18:35',
                'odds': {
                    GERALD_MEERSCHAERT: -277,
                    RYAN_JANES: 240,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACK_MARSHMAN,
                        'stats': '23-8-0',
                    },
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:21',
                },
                'time': '19:05',
                'odds': {
                    THIAGO_SANTOS: -158,
                    JACK_MARSHMAN: 140,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': AIEMANN_ZAHABI,
                        'stats': '7-1-0',
                    },
                    {
                        'name': REGINALDO_VIEIRA,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': AIEMANN_ZAHABI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    AIEMANN_ZAHABI: -253,
                    REGINALDO_VIEIRA: 220,
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
                        'name': CARLA_ESPARZA,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': RANDA_MARKOS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    RANDA_MARKOS: 220,
                    CARLA_ESPARZA: -253,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NORDINE_TALEB,
                        'stats': '14-6-0',
                    },
                    {
                        'name': SANTIAGO_PONZINIBBIO,
                        'stats': '28-3-0',
                    },
                ],
                'winner': {
                    'fighter': SANTIAGO_PONZINIBBIO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    SANTIAGO_PONZINIBBIO: -302,
                    NORDINE_TALEB: 260,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALESSANDRO_RICCI,
                        'stats': '10-5-0',
                    },
                    {
                        'name': PAUL_FELDER,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': PAUL_FELDER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:44',
                },
                'time': '21:10',
                'odds': {
                    PAUL_FELDER: -340,
                    ALESSANDRO_RICCI: 290,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GINA_MAZANY,
                        'stats': '5-3-0',
                    },
                    {
                        'name': SARA_MCMANN,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': SARA_MCMANN,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:14',
                },
                'time': '21:35',
                'odds': {
                    SARA_MCMANN: -702,
                    GINA_MAZANY: 550,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ELIAS_THEODOROU,
                        'stats': '17-2-0',
                    },
                    {
                        'name': CEZAR_FERREIRA,
                        'stats': '14-7-0',
                    },
                ],
                'winner': {
                    'fighter': ELIAS_THEODOROU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:05',
                'odds': {
                    ELIAS_THEODOROU: 100,
                    CEZAR_FERREIRA: -112,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': GAVIN_TUCKER,
                        'stats': '10-1-0',
                    },
                    {
                        'name': SAM_SICILIA,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': GAVIN_TUCKER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:35',
                'odds': {
                    GAVIN_TUCKER: -158,
                    SAM_SICILIA: 140,
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
                        'name': JOHNY_HENDRICKS,
                        'stats': '18-8-0',
                    },
                ],
                'winner': {
                    'fighter': JOHNY_HENDRICKS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:05',
                'odds': {
                    JOHNY_HENDRICKS: 113,
                    HECTOR_LOMBARD: -127,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                    {
                        'name': TRAVIS_BROWNE,
                        'stats': '18-7-1',
                    },
                ],
                'winner': {
                    'fighter': DERRICK_LEWIS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:12',
                },
                'time': '23:35',
                'odds': {
                    DERRICK_LEWIS: 103,
                    TRAVIS_BROWNE: -116,
                },
            },
        ]
    },

    {
        'date': '2017-03-04',
        'name': 'UFC 209: Woodley vs Thompson 2',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_SOUKHAMTHATH,
                        'stats': '13-6-0',
                    },
                    {
                        'name': ALBERT_MORALES,
                        'stats': '7-4-1',
                    },
                ],
                'winner': {
                    'fighter': ALBERT_MORALES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:35',
                'odds': {
                    ALBERT_MORALES: -158,
                    ANDRE_SOUKHAMTHATH: 140,
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
                        'name': PAUL_CRAIG,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': TYSON_PEDRO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:10',
                },
                'time': '19:35',
                'odds': {
                    TYSON_PEDRO: -123,
                    PAUL_CRAIG: 109,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARK_GODBEER,
                        'stats': '13-4-0',
                    },
                    {
                        'name': DANIEL_SPITZ,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': MARK_GODBEER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    DANIEL_SPITZ: 130,
                    MARK_GODBEER: -147,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUKE_SANDERS,
                        'stats': '13-3-0',
                    },
                    {
                        'name': IURI_ALCANTARA,
                        'stats': '35-10-0',
                    },
                ],
                'winner': {
                    'fighter': IURI_ALCANTARA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:13',
                },
                'time': '20:35',
                'odds': {
                    IURI_ALCANTARA: 133,
                    LUKE_SANDERS: -150,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MIRSAD_BEKTIC,
                        'stats': '13-1-0',
                    },
                    {
                        'name': DARREN_ELKINS,
                        'stats': '25-7-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_ELKINS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:19',
                },
                'time': '21:00',
                'odds': {
                    DARREN_ELKINS: 500,
                    MIRSAD_BEKTIC: -627,
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
                        'name': LUIS_HENRIQUE,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': MARCIN_TYBURA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:46',
                },
                'time': '21:36',
                'odds': {
                    MARCIN_TYBURA: -171,
                    LUIS_HENRIQUE: 151,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALISTAIR_OVEREEM,
                        'stats': '44-17-0',
                    },
                    {
                        'name': MARK_HUNT,
                        'stats': '13-14-1',
                    },
                ],
                'winner': {
                    'fighter': ALISTAIR_OVEREEM,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:44',
                },
                'time': '22:15',
                'odds': {
                    ALISTAIR_OVEREEM: -124,
                    MARK_HUNT: 110,
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
                        'name': AMANDA_COOPER,
                        'stats': '4-5-0',
                    },
                ],
                'winner': {
                    'fighter': CYNTHIA_CALVILLO,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:19',
                },
                'time': '19:05',
                'odds': {
                    CYNTHIA_CALVILLO: -170,
                    AMANDA_COOPER: 150,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DANIEL_KELLY,
                        'stats': '13-4-0',
                    },
                    {
                        'name': RASHAD_EVANS,
                        'stats': '24-8-1',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_KELLY,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:05',
                'odds': {
                    DANIEL_KELLY: 220,
                    RASHAD_EVANS: -253,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': LANDO_VANNATA,
                        'stats': '10-3-2',
                    },
                    {
                        'name': DAVID_TEYMUR,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAVID_TEYMUR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:40',
                'odds': {
                    DAVID_TEYMUR: 290,
                    LANDO_VANNATA: -340,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': TYRON_WOODLEY,
                        'stats': '19-4-1',
                    },
                    {
                        'name': STEPHEN_THOMPSON,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': TYRON_WOODLEY,
                    'by': 'm.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    TYRON_WOODLEY: 119,
                    STEPHEN_THOMPSON: -134,
                },
            },
        ]
    },

    {
        'date': '2017-03-11',
        'name': 'UFC Fight Night: Belfort vs Gastelum',
        'location': 'Fortaleza, Brazil',
        'venue': 'Centro de Formacao',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': PAULO_COSTA,
                        'stats': '12-0-0',
                    },
                    {
                        'name': GARRETH_MCLELLAN,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': PAULO_COSTA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:17',
                },
                'time': '19:05',
                'odds': {
                    PAULO_COSTA: -309,
                    GARRETH_MCLELLAN: 265,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JEREMY_KENNEDY,
                        'stats': '11-1-0',
                    },
                    {
                        'name': RONY_JASON,
                        'stats': '15-7-0',
                    },
                ],
                'winner': {
                    'fighter': JEREMY_KENNEDY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    JEREMY_KENNEDY: -125,
                    RONY_JASON: 111,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOSHUA_BURKMAN,
                        'stats': '29-17-0',
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
                    'time': '1:42',
                },
                'time': '19:05',
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JOE_SOTO,
                        'stats': '18-7-0',
                    },
                    {
                        'name': RANI_YAHYA,
                        'stats': '26-10-0',
                    },
                ],
                'winner': {
                    'fighter': JOE_SOTO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    JOE_SOTO: 195,
                    RANI_YAHYA: -223,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAVI_RAMOS,
                        'stats': '9-2-0',
                    },
                    {
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                ],
                'winner': {
                    'fighter': SERGIO_MORAES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    SERGIO_MORAES: -190,
                    DAVI_RAMOS: 160,
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
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_LEE,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:12',
                },
                'time': '21:35',
                'odds': {
                    KEVIN_LEE: -170,
                    FRANCISCO_TRINALDO: 150,
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
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                ],
                'winner': {
                    'fighter': ALEX_OLIVEIRA,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:38',
                },
                'time': '22:10',
                'odds': {
                    ALEX_OLIVEIRA: 180,
                    TIM_MEANS: -205,
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
                        'name': BETHE_CORREIA,
                        'stats': '10-3-1',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': 'm.dec',
                    'round': 3,
                    'tme': '5:00',
                },
                'time': '22:35',
                'odds': {
                    BETHE_CORREIA: -112,
                    MARION_RENEAU: 100,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': RAY_BORG,
                        'stats': '11-4-0',
                    },
                    {
                        'name': JUSSIER_FORMIGA,
                        'stats': '23-5-0',
                    },
                ],
                'winner': {
                    'fighter': RAY_BORG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:05',
                'odds': {
                    RAY_BORG: -133,
                    JUSSIER_FORMIGA: 118,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': BENEIL_DARIUSH,
                        'stats': '16-4-1',
                    },
                    {
                        'name': EDSON_BARBOZA,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': EDSON_BARBOZA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:35',
                },
                'time': '23:36',
                'odds': {
                    EDSON_BARBOZA: -162,
                    BENEIL_DARIUSH: 143,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GIAN_VILLANTE,
                        'stats': '17-11-0',
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
                    'time': '0:59',
                },
                'time': '23:59',
                'odds': {
                    MAURICIO_RUA: -160,
                    GIAN_VILLANTE: 142,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KELVIN_GASTELUM,
                        'stats': '16-3-0',
                    },
                    {
                        'name': VITOR_BELFORT,
                        'stats': '26-14-0',
                    },
                ],
                'winner': {
                    'fighter': KELVIN_GASTELUM,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:52',
                },
                'time': '23:59',
                'odds': {
                    KELVIN_GASTELUM: -385,
                    VITOR_BELFORT: 325,
                },
            },
        ]
    },

    {
        'date': '2017-03-18',
        'name': 'UFC Fight Night: Manuwa vs Anderson',
        'location': 'London, United Kingdom',
        'venue': 'The O2 Arena',
        'fights': [
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUCIE_PUDILOVA,
                        'stats': '8-4-0',
                    },
                    {
                        'name': LINA_LANSBERG,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': LINA_LANSBERG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '13:30',
                'odds': {
                    LINA_LANSBERG: -366,
                    LUCIE_PUDILOVA: 310,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': SCOTT_ASKHAM,
                        'stats': '14-4-0',
                    },
                    {
                        'name': BRADLEY_SCOTT,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': BRADLEY_SCOTT,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:00',
                'odds': {
                    BRADLEY_SCOTT: 140,
                    SCOTT_ASKHAM: -158,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MARC_DIAKIESE,
                        'stats': '13-3-0',
                    },
                    {
                        'name': TEEMU_PACKALEN,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': MARC_DIAKIESE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:30',
                },
                'time': '15:30',
                'odds': {
                    MARC_DIAKIESE: -172,
                    TEEMU_PACKALEN: 152,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': VICENTE_LUQUE,
                        'stats': '15-6-1',
                    },
                    {
                        'name': LEON_EDWARDS,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': LEON_EDWARDS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:50',
                'odds': {
                    LEON_EDWARDS: -100,
                    VICENTE_LUQUE: -112,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TIM_JOHNSON,
                        'stats': '12-4-0',
                    },
                    {
                        'name': DANIEL_OMIELANCZUK,
                        'stats': '19-8-1',
                    },
                ],
                'winner': {
                    'fighter': TIM_JOHNSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:55',
                'odds': {
                    TIM_JOHNSON: -199,
                    DANIEL_OMIELANCZUK: 175,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                    {
                        'name': FRANCIMAR_BARROSO,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCIMAR_BARROSO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:15',
                'odds': {
                    FRANCIMAR_BARROSO: 175,
                    DARREN_STEWART: -199,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOE_DUFFY,
                        'stats': '16-4-0',
                    },
                    {
                        'name': REZA_MADADI,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': JOE_DUFFY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:30',
                'odds': {
                    JOE_DUFFY: -520,
                    REZA_MADADI: 425,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ARNOLD_ALLEN,
                        'stats': '14-1-0',
                    },
                    {
                        'name': MAKWAN_AMIRKHANI,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': ARNOLD_ALLEN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:10',
                'odds': {
                    ARNOLD_ALLEN: -106,
                    MAKWAN_AMIRKHANI: -106,
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
                        'name': BRAD_PICKETT,
                        'stats': '26-14-0',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:50',
                },
                'time': '17:30',
                'odds': {
                    MARLON_VERA: 133,
                    BRAD_PICKETT: -150,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALAN_JOUBAN,
                        'stats': '16-6-0',
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
                    'time': '0:46',
                },
                'time': '18:00',
                'odds': {
                    GUNNAR_NELSON: -290,
                    ALAN_JOUBAN: 250,
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
                        'name': JIMI_MANUWA,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': JIMI_MANUWA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:05',
                },
                'time': '18:25',
                'odds': {
                    JIMI_MANUWA: -152,
                    COREY_ANDERSON: 135,
                },
            },
        ]
    },

    {
        'date': '2017-04-08',
        'name': 'UFC 210: Cormier vs Johnson 2',
        'location': 'Buffalo, New York',
        'venue': 'KeyBank Center',
        'fights': [
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MAGOMED_BIBULATOV,
                        'stats': '14-1-0',
                    },
                    {
                        'name': JENEL_LAUSA,
                        'stats': '7-5-0',
                    },
                ],
                'winner': {
                    'fighter': MAGOMED_BIBULATOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:20',
                'odds': {
                    MAGOMED_BIBULATOV: -600,
                    JENEL_LAUSA: 481,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': IRENE_ALDANA,
                        'stats': '9-4-0',
                    },
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': KATLYN_CHOOKAGIAN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:50',
                'odds': {
                    KATLYN_CHOOKAGIAN: -125,
                    IRENE_ALDANA: 111,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DESMOND_GREEN,
                        'stats': '22-8-0',
                    },
                    {
                        'name': JOSH_EMMETT,
                        'stats': '14-2-0',
                    },
                ],
                'winner': {
                    'fighter': DESMOND_GREEN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:15',
                'odds': {
                    DESMOND_GREEN: 167,
                    JOSH_EMMETT: -190,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GREGOR_GILLESPIE,
                        'stats': '13-0-0',
                    },
                    {
                        'name': ANDREW_HOLBROOK,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': GREGOR_GILLESPIE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:21',
                },
                'time': '19:35',
                'odds': {
                    GREGOR_GILLESPIE: -287,
                    ANDREW_HOLBROOK: 248,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JAN_BLACHOWICZ,
                        'stats': '23-8-0',
                    },
                    {
                        'name': PATRICK_CUMMINS,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': JAN_BLACHOWICZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    JAN_BLACHOWICZ: -106,
                    PATRICK_CUMMINS: -106,
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
                        'name': CHARLES_ROSA,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': SHANE_BURGOS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:59',
                },
                'time': '20:35',
                'odds': {
                    SHANE_BURGOS: -230,
                    CHARLES_ROSA: 201,
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
                        'name': SEAN_STRICKLAND,
                        'stats': '20-3-0',
                    },
                ],
                'winner': {
                    'fighter': KAMARU_USMAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    KAMARU_USMAN: -262,
                    SEAN_STRICKLAND: 227,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_DE_LA_TORRE,
                        'stats': '14-7-0',
                    },
                    {
                        'name': MYLES_JURY,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': MYLES_JURY,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:30',
                },
                'time': '21:35',
                'odds': {
                    MYLES_JURY: -432,
                    MIKE_DE_LA_TORRE: 361,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': WILL_BROOKS,
                        'stats': '18-4-0',
                    },
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:30',
                },
                'time': '22:15',
                'odds': {
                    CHARLES_OLIVEIRA: 176,
                    WILL_BROOKS: -200,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': PATRICK_COTE,
                        'stats': '24-11-0',
                    },
                    {
                        'name': THIAGO_ALVES,
                        'stats': '28-13-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_ALVES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:45',
                 'odds': {
                    THIAGO_ALVES: 120,
                    PATRICK_COTE: -135,
                 },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': PEARL_GONZALEZ,
                        'stats': '6-3-0',
                    },
                    {
                        'name': CYNTHIA_CALVILLO,
                        'stats': '8-1-0',
                    },
                ],
                'winner': {
                    'fighter': CYNTHIA_CALVILLO,
                    'by': 'submission',
                    'round': 3,
                    'tmie': '3:45',
                },
                'time': '23:15',
                'odds': {
                    CYNTHIA_CALVILLO: -258,
                    PEARL_GONZALEZ: 224,
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
                        'name': GEGARD_MOUSASI,
                        'stats': '42-6-2',
                    },
                ],
                'winner': {
                    'fighter': GEGARD_MOUSASI,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:13',
                },
                'time': '23:45',
                'odds': {
                    GEGARD_MOUSASI: -118,
                    CHRIS_WEIDMAN: 105,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_JOHNSON,
                        'stats': '22-6-0',
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
                    'time': '3:37',
                },
                'time': '23:59',
                'odds': {
                    DANIEL_CORMIER: -115,
                    ANTHONY_JOHNSON: -143,
                },
            },
        ]
    },

    {
        'date': '2017-04-15',
        'name': 'UFC Fight Night: Johnson vs Reis',
        'location': 'Kansas City, Missouri',
        'venue': 'Sprint Center',
        'fights': [
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': KETLEN_VIEIRA,
                        'stats': '10-0-0',
                    },
                    {
                        'name': ASHLEE_EVANS_SMITH,
                        'stats': '6-4-0',
                    },
                ],
                'winner': {
                    'fighter': KETLEN_VIEIRA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:00',
                'odds': {
                    KETLEN_VIEIRA: 155,
                    ASHLEE_EVANS_SMITH: -176,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NATHAN_COY,
                        'stats': '15-7-0',
                    },
                    {
                        'name': ZAK_CUMMINGS,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': ZAK_CUMMINGS,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:21',
                },
                'time': '16:25',
                'odds': {
                    ZAK_CUMMINGS: -555,
                    NATHAN_COY: 450,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANDREW_SANCHEZ,
                        'stats': '11-4-0',
                    },
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_SMITH,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:52',
                },
                'time': '17:15',
                'odds': {
                    ANTHONY_SMITH: 290,
                    ANDREW_SANCHEZ: -340,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DEVIN_CLARK,
                        'stats': '9-3-0',
                    },
                    {
                        'name': JAKE_COLLIER,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': DEVIN_CLARK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:40',
                'odds': {
                    DEVIN_CLARK: -141,
                    JAKE_COLLIER: 125,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': AUGUSTO_MENDES,
                        'stats': '6-2-0',
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
                'time': '16:50',
                'odds': {
                    ALJAMAIN_STERLING: -346,
                    AUGUSTO_MENDES: 295,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': LOUIS_SMOLKA,
                        'stats': '15-6-0',
                    },
                    {
                        'name': TIM_ELLIOTT,
                        'stats': '16-8-1',
                    },
                ],
                'winner': {
                    'fighter': TIM_ELLIOTT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:05',
                'odds': {
                    TIM_ELLIOTT: -170,
                    LOUIS_SMOLKA: 150,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': RASHID_MAGOMEDOV,
                        'stats': '20-2-0',
                    },
                    {
                        'name': BOBBY_GREEN,
                        'stats': '24-9-1',
                    },
                ],
                'winner': {
                    'fighter': RASHID_MAGOMEDOV,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:40',
                'odds': {
                    RASHID_MAGOMEDOV: -353,
                    BOBBY_GREEN: 300,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': TOM_DUQUESNOY,
                        'stats': '16-2-0',
                    },
                    {
                        'name': PATRICK_WILLIAMS,
                        'stats': '8-6-0',
                    },
                ],
                'winner': {
                    'fighter': TOM_DUQUESNOY,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:28',
                },
                'time': '19:15',
                'odds': {
                    TOM_DUQUESNOY: -1000,
                    PATRICK_WILLIAMS: 733,
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
                        'name': ROY_NELSON,
                        'stats': '23-14-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:45',
                'odds': {
                    ALEXANDER_VOLKOV: -155,
                    ROY_NELSON: 137,
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
                        'name': JEREMY_STEPHENS,
                        'stats': '28-16-0',
                    },
                ],
                'winner': {
                    'fighter': RENATO_MOICANO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:15',
                'odds': {
                    RENATO_MOICANO: 145,
                    JEREMY_STEPHENS: -164,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ROBERT_WHITTAKER,
                        'stats': '21-4-0',
                    },
                    {
                        'name': JACARE_SOUZA,
                        'stats': '26-6-0',
                    },
                ],
                'winner': {
                    'fighter': ROBERT_WHITTAKER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:28',
                },
                'time': '20:45',
                'odds': {
                    ROBERT_WHITTAKER: 234,
                    JACARE_SOUZA: -270,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ROSE_NAMAJUNAS,
                        'stats': '9-3-0',
                    },
                    {
                        'name': MICHELLE_WATERSON,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': ROSE_NAMAJUNAS,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:47',
                },
                'time': '21:15',
                'odds': {
                    ROSE_NAMAJUNAS: 111,
                    MICHELLE_WATERSON: -125,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': WILSON_REIS,
                        'stats': '23-9-0',
                    },
                    {
                        'name': DEMETRIOUS_JOHNSON,
                        'stats': '27-3-1',
                    },
                ],
                'winner': {
                    'fighter': DEMETRIOUS_JOHNSON,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:49',
                },
                'time': '21:45',
                'odds': {
                    DEMETRIOUS_JOHNSON: -902,
                    WILSON_REIS: 676,
                },
            },
        ]
    },

    {
        'date': '2017-04-22',
        'name': 'UFC Fight Night: Swanson vs Lobov',
        'location': 'Nashville, Tennessee',
        'venue': 'Bridgestone Arena',
        'fights': [
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MATT_SCHNELL,
                        'stats': '13-4-0',
                    },
                    {
                        'name': HECTOR_SANDOVAL,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': HECTOR_SANDOVAL,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:24',
                },
                'time': '18:40',
                'odds': {
                    HECTOR_SANDOVAL: 135,
                    MATT_SCHNELL: -152,
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
                        'name': JOE_PROCTOR,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': BRYAN_BARBERENA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:30',
                },
                'time': '19:05',
                'odds': {
                    BRYAN_BARBERENA: -315,
                    JOE_PROCTOR: 270,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CINDY_DANDOIS,
                        'stats': '8-3-0',
                    },
                    {
                        'name': ALEXIS_DAVIS,
                        'stats': '19-9-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXIS_DAVIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ALEXIS_DAVIS: -259,
                    CINDY_DANDOIS: 225,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': DANIELLE_TAYLOR,
                        'stats': '9-4-0',
                    },
                    {
                        'name': JESSICA_PENNE,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': DANIELLE_TAYLOR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    DANIELLE_TAYLOR: -100,
                    JESSICA_PENNE: -112,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_MCBRIDE,
                        'stats': '8-3-0',
                    },
                    {
                        'name': SCOTT_HOLTZMAN,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': SCOTT_HOLTZMAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    SCOTT_HOLTZMAN: -277,
                    MICHAEL_MCBRIDE: 240,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': BRANDON_MORENO,
                        'stats': '14-5-0',
                    },
                    {
                        'name': DUSTIN_ORTIZ,
                        'stats': '19-8-0',
                    },
                ],
                'winner': {
                    'fighter': BRANDON_MORENO,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:06',
                },
                'time': '21:00',
                'odds': {
                    BRANDON_MORENO: 106,
                    DUSTIN_ORTIZ: -119,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
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
                'time': '21:30',
                'odds': {
                    THALES_LEITES: -125,
                    SAM_ALVEY: 111,
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
                        'name': JAKE_ELLENBERGER,
                        'stats': '31-15-0',
                    },
                ],
                'winner': {
                    'fighter': MIKE_PERRY,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:05',
                },
                'time': '22:00',
                'odds': {
                    MIKE_PERRY: -125,
                    JAKE_ELLENBERGER: 111,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': STEVIE_RAY,
                        'stats': '22-7-0',
                    },
                    {
                        'name': JOE_LAUZON,
                        'stats': '27-16--0',
                    },
                ],
                'winner': {
                    'fighter': STEVIE_RAY,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    STEVIE_RAY: -158,
                    JOE_LAUZON: 140,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': EDDIE_WINELAND,
                        'stats': '23-13-1',
                    },
                    {
                        'name': JOHN_DODSON,
                        'stats': '21-11-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_DODSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    JOHN_DODSON: -353,
                    EDDIE_WINELAND: 300,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCOS_ROGERIO_DE_LIMA,
                        'stats': '16-7-1',
                    },
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '23-12-0',
                    },
                ],
                'winner': {
                    'fighter': OVINCE_SAINT_PREUX,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:11',
                },
                'time': '23:30',
                'odds': {
                    OVINCE_SAINT_PREUX: -164,
                    MARCOS_ROGERIO_DE_LIMA: 145,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DIEGO_SANCHEZ,
                        'stats': '31-11-0',
                    },
                    {
                        'name': AL_IAQUINTA,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': AL_IAQUINTA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:38',
                },
                'time': '23:59',
                'odds': {
                    AL_IAQUINTA: -405,
                    DIEGO_SANCHEZ: 340,
                },
            },
        ]
    },

    {
        'date': '2017-05-13',
        'name': 'UFC 211: Miocic vs Dos Dantos',
        'location': 'Dallas, Texas',
        'venue': 'American Airlines Center',
        'fights': [
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GADZHIMURAD_ANTIGULOV,
                        'stats': 'submission',
                    },
                    {
                        'name': JOACHIM_CHRISTENSEN,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': GADZHIMURAD_ANTIGULOV,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:21',
                },
                'time': '18:00',
                'odds': {
                    GADZHIMURAD_ANTIGULOV: -380,
                    JOACHIM_CHRISTENSEN: 321,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ENRIQUE_BARZOLA,
                        'stats': '16-4-1',
                    },
                    {
                        'name': GABRIEL_BENITEZ,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': ENRIQUE_BARZOLA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    ENRIQUE_BARZOLA: 114,
                    GABRIEL_BENITEZ: -128,
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
                        'name': JESSICA_AGUILAR,
                        'stats': '20-8-0',
                    },
                ],
                'winner': {
                    'fighter': CORTNEY_CASEY_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    CORTNEY_CASEY_SANCHEZ: -181,
                    JESSICA_AGUILAR: 160,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MARC_POLO_REYES,
                        'stats': '8-5-0',
                    },
                    {
                        'name': JAMES_VICK,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': JAMES_VICK,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:39',
                },
                'time': '20:00',
                'odds': {
                    JAMES_VICK: -390,
                    MARC_POLO_REYES: 329,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': RASHAD_COULTER,
                        'stats': '9-4-0',
                    },
                    {
                        'name': CHASE_SHERMAN,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': CHASE_SHERMAN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:36',
                },
                'time': '20:30',
                'odds': {
                    CHASE_SHERMAN: -107,
                    RASHAD_COULTER: -105,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JASON_KNIGHT,
                        'stats': '8-5-0',
                    },
                    {
                        'name': CHAS_SKELLY,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': JASON_KNIGHT,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:39',
                },
                'time': '21:00',
                'odds': {
                    JASON_KNIGHT: -104,
                    CHAS_SKELLY: -108,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_BRANCH,
                        'stats': '22-6-0',
                    },
                    {
                        'name': KRZYSZTOF_JOTKO,
                        'stats': '19-4-0',
                    },
                ],
                'winner': {
                    'fighter': DAVID_BRANCH,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    DAVID_BRANCH: 153,
                    KRZYSZTOF_JOTKO: -173,
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
                        'name': FRANKIE_EDGAR,
                        'stats': '22-6-1',
                    },
                ],
                'winner': {
                    'fighter': FRANKIE_EDGAR,
                    'by': 'tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    FRANKIE_EDGAR: -131,
                    YAIR_RODRIGUEZ: 116,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JORGE_MASVIDAL,
                        'stats': '33-13-0',
                    },
                    {
                        'name': DEMIAN_MAIA,
                        'stats': '26-9-0',
                    },
                ],
                'winner': {
                    'fighter': DEMIAN_MAIA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    DEMIAN_MAIA: -114,
                    JORGE_MASVIDAL: 101,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JOANNA_JEDRZEJCZYK,
                        'stats': '15-3-0',
                    },
                    {
                        'name': JESSICA_ANDRADE,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': JOANNA_JEDRZEJCZYK,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    JOANNA_JEDRZEJCZYK: -177,
                    JESSICA_ANDRADE: 156,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': STIPE_MIOCIC,
                        'stats': '18-3-0',
                    },
                    {
                        'name': JUNIOR_DOS_SANTOS,
                        'stats': '21-5-0',
                    },
                ],
                'winner': {
                    'fighter': STIPE_MIOCIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:22',
                },
                'time': '23:59',
                'odds': {
                    STIPE_MIOCIC: -162,
                    JUNIOR_DOS_SANTOS: 143,
                },
            },
        ]
    },

    {
        'date': '2017-05-28',
        'name': 'UFC Fight Night: Gustafsson vs Teixeira',
        'location': 'Stockholm, Sweden',
        'venue': 'Ericsson Globe',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MARCIN_HELD,
                        'stats': '23-7-0',
                    },
                    {
                        'name': DAMIR_HADZOVIC,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIR_HADZOVIC,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:07',
                },
                'time': '10:00',
                'odds': {
                    DAMIR_HADZOVIC: 255,
                    MARCIN_HELD: -296,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JESSIN_AYARI,
                        'stats': '16-5-0',
                    },
                    {
                        'name': DARREN_TILL,
                        'stats': '17-2-1',
                    },
                ],
                'winner': {
                    'fighter': DARREN_TILL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '10:30',
                'odds': {
                    DARREN_TILL: -253,
                    JESSIN_AYARI: 220,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BOJAN_VELICKOVIC,
                        'stats': '15-6-1',
                    },
                    {
                        'name': NICO_MUSOKE,
                        'stats': '13-5-0',
                    },
                ],
                'winner': {
                    'fighter': BOJAN_VELICKOVIC,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:37',
                },
                'time': '11:05',
                'odds': {
                    BOJAN_VELICKOVIC: 107,
                    NICO_MUSOKE: -120,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOAQUIM_SILVA,
                        'stats': '11-1-0',
                    },
                    {
                        'name': REZA_MADADI,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': JOAQUIM_SILVA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '11:40',
                'odds': {
                    JOAQUIM_SILVA: -165,
                    REZA_MADADI: 146,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TREVOR_SMITH,
                        'stats': '15-9-0',
                    },
                    {
                        'name': CHRIS_CAMOZZI,
                        'stats': '24-13-0',
                    },
                ],
                'winner': {
                    'fighter': TREVOR_SMITH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:10',
                'odds': {
                    TREVOR_SMITH: 135,
                    CHRIS_CAMOZZI: -152,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': DAMIAN_STASIAK,
                        'stats': '10-6-0',
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
                'time': '12:40',
                'odds': {
                    PEDRO_MUNHOZ: -555,
                    DAMIAN_STASIAK: 450,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACK_HERMANSSON,
                        'stats': '19-4-0',
                    },
                    {
                        'name': ALEX_NICHOLSON,
                        'stats': '7-4-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_HERMANSSON,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:00',
                },
                'time': '13:10',
                'odds': {
                    JACK_HERMANSSON: -170,
                    ALEX_NICHOLSON: 150,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': OLIVER_ENKAMP,
                        'stats': '7-2-0',
                    },
                    {
                        'name': NORDINE_TALEB,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': NORDINE_TALEB,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '13:40',
                'odds': {
                    NORDINE_TALEB: -321,
                    OLIVER_ENKAMP: 275,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ABDUL_RAZAK_ALHASSAN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': OMARI_AKHMEDOV,
                        'stats': '18-4-1',
                    },
                ],
                'winner': {
                    'fighter': OMARI_AKHMEDOV,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:10',
                'odds': {
                    OMARI_AKHMEDOV: 242,
                    ABDUL_RAZAK_ALHASSAN: -280,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': PETER_SOBOTTA,
                        'stats': '17-6-1',
                    },
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                ],
                'winner': {
                    'fighter': PETER_SOBOTTA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:29',
                },
                'time': '14:40',
                'odds': {
                    PETER_SOBOTTA: -129,
                    BEN_SAUNDERS: 115,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': VOLKAN_OEZDEMIR,
                        'stats': '15-4-0',
                    },
                    {
                        'name': MISHA_CIRKUNOV,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': VOLKAN_OEZDEMIR,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:28',
                },
                'time': '15:10',
                'odds': {
                    VOLKAN_OEZDEMIR: 375,
                    MISHA_CIRKUNOV: -451,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GLOVER_TEIXEIRA,
                        'stats': '28-7-0',
                    },
                    {
                        'name': ALEXANDER_GUSTAFSSON,
                        'stats': '18-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_GUSTAFSSON,
                    'by': 'ko/tko',
                    'round': 5,
                    'time': '1:07',
                },
            },
        ]
    },

    {
        'date': '2017-06-03',
        'name': 'UFC 212: Aldo vs Holloway',
        'location': 'Rio de Janeiro, Brazil',
        'venue': 'Jeunesse Arena',
        'fights': [
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': DEIVESON_FIGUEIREDO,
                        'stats': '15-1-0',
                    },
                    {
                        'name': MARCO_BELTRAN,
                        'stats': '8-7-0',
                    },
                ],
                'winner': {
                    'fighter': DEIVESON_FIGUEIREDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '18:40',
                'odds': {
                    DEIVESON_FIGUEIREDO: -147,
                    MARCO_BELTRAN: 130,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JIMMY_WALLHEAD,
                        'stats': '29-11-0',
                    },
                    {
                        'name': LUAN_CHAGAS,
                        'stats': '15-3-1',
                    },
                ],
                'winner': {
                    'fighter': LUAN_CHAGAS,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:48',
                },
                'time': '19:10',
                'odds': {
                    LUAN_CHAGAS: -259,
                    JIMMY_WALLHEAD: 225,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': VIVIANE_PEREIRA,
                        'stats': '13-2-0',
                    },
                    {
                        'name': JAMIE_MOYLE,
                        'stats': '4-3-0',
                    },
                ],
                'winner': {
                    'fighter': VIVIANE_PEREIRA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    VIVIANE_PEREIRA: -180,
                    JAMIE_MOYLE: 159,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRIAN_KELLEHER,
                        'stats': '19-10-0',
                    },
                    {
                        'name': IURI_ALCANTARA,
                        'stats': '35-10-0',
                    },
                ],
                'winner': {
                    'fighter': BRIAN_KELLEHER,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:48',
                },
                'time': '20:00',
                'odds': {
                    BRIAN_KELLEHER: 305,
                    IURI_ALCANTARA: -359,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MATTHEW_LOPEZ,
                        'stats': '10-5-0',
                    },
                    {
                        'name': JOHNNY_EDUARDO,
                        'stats': '28-12-0',
                    },
                ],
                'winner': {
                    'fighter': MATTHEW_LOPEZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:57',
                },
                'time': '20:30',
                'odds': {
                    MATTHEW_LOPEZ: -109,
                    JOHNNY_EDUARDO: -103,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ERIC_SPICELY,
                        'stats': '10-5-0',
                    },
                    {
                        'name': ANTONIO_CARLOS_JUNIOR,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': ANTONIO_CARLOS_JUNIOR,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:49',
                },
                'time': '21:00',
                'odds': {
                    ANTONIO_CARLOS_JUNIOR: -327,
                    ERIC_SPICELY: 280,
                },
            },
            {
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
                    'fighter': RAPHAEL_ASSUNCAO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    RAPHAEL_ASSUNCAO: 226,
                    MARLON_MORAES: -260,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ERICK_SILVA,
                        'stats': '19-9-0',
                    },
                    {
                        'name': YANCY_MEDEIROS,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': YANCY_MEDEIROS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:01',
                },
                'time': '22:00',
                'odds': {
                    YANCY_MEDEIROS: -140,
                    ERICK_SILVA: 124,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': PAULO_COSTA,
                        'stats': '12-0-0',
                    },
                    {
                        'name': OLUWALE_BAMGBOSE,
                        'stats': '6-4-0',
                    },
                ],
                'winner': {
                    'fighter': PAULO_COSTA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:06',
                },
                'time': '22:30',
                'odds': {
                    PAULO_COSTA: -253,
                    OLUWALE_BAMGBOSE: 220,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': NATE_MARQUARDT,
                        'stats': '38-19-2',
                    },
                    {
                        'name': VITOR_BELFORT,
                        'stats': '26-14-0',
                    },
                ],
                'winner': {
                    'fighter': VITOR_BELFORT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    VITOR_BELFORT: -185,
                    NATE_MARQUARDT: 163,
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
                        'name': CLAUDIA_GADELHA,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': CLAUDIA_GADELHA,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:03',
                },
                'time': '23:30',
                'odds': {
                    CLAUDIA_GADELHA: -277,
                    KAROLINA_KOWALKIEWICZ: 240,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MAX_HOLLOWAY,
                        'stats': '20-3-0',
                    },
                    {
                        'name': JOSE_ALDO,
                        'stats': '28-4-0',
                    },
                ],
                'winner': {
                    'fighter': MAX_HOLLOWAY,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:13',
                },
            }
        ]
    },

    {
        'date': '2017-06-10',
        'name': 'UFC Fight Night: Lewis vs Hunt',
        'location': 'Auckland, New Zealand',
        'venue': 'Spark Arena',
        'fights': [
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CHANMI_JEON,
                        'stats': '5-2-0',
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
                'time': '19:30',
                'odds': {
                    JJ_ALDRICH: -211,
                    CHANMI_JEON: 185,
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
                        'name': KIICHI_KUNIMOTO,
                        'stats': '18-7-2',
                    },
                ],
                'winner': {
                    'fighter': ZAK_OTTOW,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    ZAK_OTTOW: -366,
                    KIICHI_KUNIMOTO: 310,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ASHKAN_MOKHTARIAN,
                        'stats': '13-3-0',
                    },
                    {
                        'name': JOHN_MORAGA,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_MORAGA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    JOHN_MORAGA: -205,
                    ASHKAN_MOKHTARIAN: 180,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LUKE_JUMEAU,
                        'stats': '13-4-0',
                    },
                    {
                        'name': DOMINIQUE_STEELE,
                        'stats': '14-9-0',
                    },
                ],
                'winner': {
                    'fighter': LUKE_JUMEAU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    LUKE_JUMEAU: 175,
                    DOMINIQUE_STEELE: 199,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAMIEN_BROWN,
                        'stats': '17-12-0',
                    },
                    {
                        'name': VINC_PICHEL,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': VINC_PICHEL,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:37',
                },
                'time': '21:30',
                'odds': {
                    VINC_PICHEL: -125,
                    DAMIEN_BROWN: 111,
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
                        'name': MIZUTO_HIROTA,
                        'stats': '19-10-2',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    ALEXANDER_VOLKANOVSKI: -767,
                    MIZUTO_HIROTA: 440,
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
                        'name': TIM_ELLIOTT,
                        'stats': '16-8-1',
                    },
                ],
                'winner': {
                    'fighter': BEN_NGUYEN,
                    'by': 'submission',
                    'round': 1,
                    'time': '0:49',
                },
                'time': '22:30',
                'odds': {
                    BEN_NGUYEN: 154,
                    TIM_ELLIOTT: -174,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': HENRIQUE_DA_SILVA,
                        'stats': '14-5-0',
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
                    'time': '0:22',
                },
                'time': '23:00',
                'odds': {
                    ION_CUTELABA: -302,
                    HENRIQUE_DA_SILVA: 260,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_HOOKER,
                        'stats': '18-8-0',
                    },
                    {
                        'name': ROSS_PEARSON,
                        'stats': '22-16-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_HOOKER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:02',
                },
                'time': '23:30',
                'odds': {
                    DAN_HOOKER: -145,
                    ROSS_PEARSON: 129,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DANIEL_KELLY,
                        'stats': '13-4-0',
                    },
                    {
                        'name': DEREK_BRUNSON,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': DEREK_BRUNSON,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:16',
                },
                'time': '23:45',
                'odds': {
                    DEREK_BRUNSON: -253,
                    DANIEL_KELLY: 220,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                    {
                        'name': MARK_HUNT,
                        'stats': '13-14-1',
                    },
                ],
                'winner': {
                    'fighter': MARK_HUNT,
                    'by': 'ko/tko',
                    'round': 4,
                    'time': '3:51',
                },
                'time': '23:59',
                'odds': {
                    MARK_HUNT: 130,
                    DERRICK_LEWIS: -147,
                },
            },
        ]
    },

    {
        'date': '2017-06-17',
        'name': 'UFC Fight Night: Holm vs Correia',
        'location': 'Kallang, Singapore',
        'venue': 'Singapore Indoor Stadium',
        'fights': [
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JI_YEON_KIM,
                        'stats': '7-2-2',
                    },
                    {
                        'name': LUCIE_PUDILOVA,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': LUCIE_PUDILOVA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:30',
                'odds': {
                    LUCIE_PUDILOVA: -116,
                    JI_YEON_KIM: 103,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': CARLS_JOHN_DE_TOMAS,
                        'stats': '8-2-0',
                    },
                    {
                        'name': NAOKI_INOUE,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': NAOKI_INOUE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:55',
                'odds': {
                    NAOKI_INOUE: -274,
                    CARLS_JOHN_DE_TOMAS: 237,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': KWAN_HO_KWAK,
                        'stats': '9-2-0',
                    },
                    {
                        'name': RUSSEL_DOANE,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': RUSSEL_DOANE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:09',
                },
                'time': '17:15',
                'odds': {
                    RUSSEL_DOANE: 109,
                    KWAN_HO_KWAK: -123,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': FRANK_CAMACHO,
                        'stats': '21-7-0',
                    },
                    {
                        'name': LI_JINGLIANG,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': LI_JINGLIANG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:45',
                'odds': {
                    LI_JINGLIANG: -485,
                    FRANK_CAMACHO: 400,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ULKA_SASAKI,
                        'stats': '21-6-2',
                    },
                    {
                        'name': JUSTIN_SCOGGINS,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': ULKA_SASAKI,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:19',
                },
                'time': '18:15',
                'odds': {
                    ULKA_SASAKI: 393,
                    JUSTIN_SCOGGINS: -475,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ROLANDO_DY,
                        'stats': '9-7-1',
                    },
                    {
                        'name': ALEX_CACERES,
                        'stats': '14-12-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_CACERES,
                    'by': 'tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '18:45',
                'odds': {
                    ALEX_CACERES: -290,
                    ROLANDO_DY: 250,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': CYRIL_ASKER,
                        'stats': '9-4-0',
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
                    'time': '1:44',
                },
                'time': '19:15',
                'odds': {
                    WALT_HARRIS: -330,
                    CYRIL_ASKER: 282,
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
                        'name': TAKANORI_GOMI,
                        'stats': '35-14-0',
                    },
                ],
                'winner': {
                    'fighter': JON_TUCK,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:12',
                },
                'time': '19:45',
                'odds': {
                    JON_TUCK: -344,
                    TAKANORI_GOMI: 293,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': TAREC_SAFFIEDINE,
                        'stats': '16-7-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': RAFAEL_DOS_ANJOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:15',
                'odds': {
                    RAFAEL_DOS_ANJOS: -199,
                    TAREC_SAFFIEDINE: 175,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': COLBY_COVINGTON,
                        'stats': '14-1-0',
                    },
                    {
                        'name': DONG_HYUN_KIM,
                        'stats': '22-4-1',
                    },
                ],
                'winner': {
                    'fighter': COLBY_COVINGTON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:45',
                'odds': {
                    COLBY_COVINGTON: -223,
                    DONG_HYUN_KIM: 195,
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
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                ],
                'winner': {
                    'fighter': MARCIN_TYBURA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:15',
                'odds': {
                    MARCIN_TYBURA: -225,
                    ANDREI_ARLOVSKI: 197,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': HOLLY_HOLM,
                        'stats': '12-4-0',
                    },
                    {
                        'name': BETHE_CORREIA,
                        'stats': '10-3-1',
                    },
                ],
                'winner': {
                    'fighter': HOLLY_HOLM,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:09',
                },
                'time': '21:45',
                'odds': {
                    HOLLY_HOLM: -466,
                    BETHE_CORREIA: 386,
                },
            },
        ]
    },

]

PREDICTIONS = [
]
