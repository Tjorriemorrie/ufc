from fighters import *

DATA_2017 = [
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
                    CYRIL_ASKER: 1.85,
                    DMITRII_SMOLIAKOV: 1.95,
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
                    JOACHIM_CHRISTENSEN: 1.42,
                    BOJAN_MIHAJLOVIC: 2.90,
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
                    WALT_HARRIS: 1.63,
                    CHASE_SHERMAN: 2.25,
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
                    NINA_ANSAROFF: 1.57,
                    JOCELYN_JONES_LYBARGER: 2.43,
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
                    ANTHONY_ROCCO_MARTIN: 1.59,
                    ALEX_WHITE: 2.37,
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
                    ALEKSEI_OLEINIK: 1.69,
                    VIKTOR_PESTA: 2.10,
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
                    AUGUSTO_MENDES: 2.25,
                    FRANKIE_SAENZ: 1.59,
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
                    DRAKKAR_KLOSE: 1.32,
                    DEVIN_POWELL: 3.45,
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
                    SERGIO_PETTIS: 1.65,
                    JOHN_MORAGA: 2.20,
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
                    BEN_SAUNDERS: 2.10,
                    COURT_MCGEE: 1.71,
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
                    JOE_LAUZON: 1.69,
                    MARCIN_HELD: 2.15,
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
                    YAIR_RODRIGUEZ: 1.25,
                    BJ_PENN: 3.60,
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
                    JASON_GONZALEZ: 2.05,
                    JC_COTTRELL: 1.73,
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
                    ALEXANDRE_PANTOJA: 1.91,
                    ERIC_SHELTON: 1.81,
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
                    MARCOS_ROGERIO_DE_LIMA: 1.65,
                    JEREMY_KIMBALL: 2.15,
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
                    ERIC_SPICELY: 1.91,
                    ALESSIO_DI_CHRICO: 1.83,
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
                    JORDAN_JOHNSON: 1.49,
                    HENRIQUE_DA_SILVA: 2.62,
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
                    LI_JINGLIANG: 1.67,
                    BOBBY_NASH: 2.12,
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
                    RAPHAEL_ASSUNCAO: 1.67,
                    ALJAMAIN_STERLING: 2.20,
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
                    SAM_ALVEY: 1.67,
                    NATE_MARQUARDT: 2.20,
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
                    JASON_KNIGHT: 1.67,
                    ALEX_CACERES: 2.13,
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
                    FRANCIS_NGANNOU: 1.24,
                    ANDREI_ARLOVSKI: 3.90,
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
                    JORGE_MASVIDAL: 2.45,
                    DONALD_CERRONE: 1.53,
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
                    VALENTINA_SHEVCHENKO: 1.51,
                    JULIANNA_PENA: 2.50,
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
                    KHALIL_ROUNTREE: 1.55,
                    DANIEL_JOLLY: 1.55,
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
                    NIKO_PRICE: 1.87,
                    ALEX_MORONO: 1.87,
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
                    TECIA_TORRES: 1.23,
                    BEC_RAWLINGS: 4.00,
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
                    RICARDO_RAMOS: 2.05,
                    MICHINORI_TANAKA: 1.74,
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
                    CHAS_SKELLY: 1.28,
                    CHRIS_GRUETZEMACHER: 3.45,
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
                    CURTIS_BLAYDES: 1.25,
                    ADAM_MILSTEAD: 3.85,
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
                    JESSICA_ANDRADE: 1.13,
                    ANGELA_HILL: 5.25,
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
                    MARCEL_FORTUNA: 3.00,
                    ANTHONY_HAMILTON: 1.37,
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
                    VOLKAN_OEZDEMIR: 3.95,
                    OVINCE_SAINT_PREUX: 1.25,
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
                    JAMES_VICK: 1.74,
                    ABEL_TRUJILLO: 1.99,
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
                    FELICE_HERRIG: 3.85,
                    ALEXA_GRASSO: 1.25,
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
                    CHAN_SUNG_JUNG: 2.45,
                    DENNIS_BERMUDEZ: 1.50,
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
                    RYAN_LAFLARE: 1.32,
                    ROAN_CARNEIRO: 3.40,
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
                    RICK_GLENN: 1.54,
                    PHILLIPE_NOVER: 2.50,
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
                    ISLAM_MAKHACHEV: 1.29,
                    NIK_LENTZ: 3.65,
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
                    WILSON_REIS: 1.15,
                    ULKA_SASAKI: 5.00,
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
                    BELAL_MUHAMMAD: 2.25,
                    RANDY_BROWN: 1.65,
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
                    DUSTIN_POIRIER: 1.21,
                    JIM_MILLER: 4.25,
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
                    GLOVER_TEIXEIRA: 1.43,
                    JARED_CANNONIER: 2.75,
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
                    JACARE_SOUZA: 1.14,
                    TIM_BOETSCH: 4.75,
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
                    ANDERSON_SILVA: 1.91,
                    DEREK_BRUNSON: 1.80,
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
                    GERMAINE_DE_RANDAMIE: 1.74,
                    HOLLY_HOLM: 1.97,
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
                    GERALD_MEERSCHAERT: 1.33,
                    RYAN_JANES: 3.30,
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
                    THIAGO_SANTOS: 1.59,
                    JACK_MARSHMAN: 2.32,
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
                    AIEMANN_ZAHABI: 1.36,
                    REGINALDO_VIEIRA: 3.10,
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
                    RANDA_MARKOS: 3.10,
                    CARLA_ESPARZA: 1.37,
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
                    SANTIAGO_PONZINIBBIO: 1.29,
                    NORDINE_TALEB: 3.50,
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
                    PAUL_FELDER: 1.27,
                    ALESSANDRO_RICCI: 3.70,
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
                    SARA_MCMANN: 1.13,
                    GINA_MAZANY: 5.75,
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
                    ELIAS_THEODOROU: 1.87,
                    CEZAR_FERREIRA: 1.85,
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
                    GAVIN_TUCKER: 1.57,
                    SAM_SICILIA: 2.35,
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
                    JOHNY_HENDRICKS: 1.98,
                    HECTOR_LOMBARD: 1.74,
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
                    DERRICK_LEWIS: 1.91,
                    TRAVIS_BROWNE: 1.83,
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
                    ALBERT_MORALES: 1.63,
                    ANDRE_SOUKHAMTHATH: 2.10,
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
                    TYSON_PEDRO: 1.69,
                    PAUL_CRAIG: 1.98,
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
                    DANIEL_SPITZ: 2.18,
                    MARK_GODBEER: 1.67,
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
                    IURI_ALCANTARA: 2.25,
                    LUKE_SANDERS: 1.65,
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
                    DARREN_ELKINS: 5.50,
                    MIRSAD_BEKTIC: 1.13,
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
                    MARCIN_TYBURA: 1.56,
                    LUIS_HENRIQUE: 2.40,
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
                    ALISTAIR_OVEREEM: 1.69,
                    MARK_HUNT: 2.10,
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
                    CYNTHIA_CALVILLO: 1.57,
                    AMANDA_COOPER: 2.10,
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
                    DANIEL_KELLY: 2.94,
                    RASHAD_EVANS: 1.38,
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
                    DAVID_TEYMUR: 3.75,
                    LANDO_VANNATA: 1.26,
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
                    TYRON_WOODLEY: 1.87,
                    STEPHEN_THOMPSON: 1.71,
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
                    PAULO_COSTA: 1.31,
                    GARRETH_MCLELLAN: 3.45,
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
                    JEREMY_KENNEDY: 1.71,
                    RONY_JASON: 2.05,
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
                    JOE_SOTO: 2.85,
                    RANI_YAHYA: 1.41,
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
                    SERGIO_MORAES: 1.53,
                    DAVI_RAMOS: 2.60,
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
                    KEVIN_LEE: 1.56,
                    FRANCISCO_TRINALDO: 2.45,
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
                    ALEX_OLIVEIRA: 2.74,
                    TIM_MEANS: 1.44,
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
                    BETHE_CORREIA: 1.83,
                    MARION_RENEAU: 1.91,
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
                    RAY_BORG: 1.71,
                    JUSSIER_FORMIGA: 2.00,
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
                    EDSON_BARBOZA: 1.59,
                    BENEIL_DARIUSH: 2.31,
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
                    MAURICIO_RUA: 1.59,
                    GIAN_VILLANTE: 2.34,
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
                    KELVIN_GASTELUM: 1.25,
                    VITOR_BELFORT: 4.00,
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
                    LINA_LANSBERG: 1.26,
                    LUCIE_PUDILOVA: 3.90,
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
                    BRADLEY_SCOTT: 2.33,
                    SCOTT_ASKHAM: 1.61,
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
                    MARC_DIAKIESE: 1.54,
                    TEEMU_PACKALEN: 2.39,
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
                    LEON_EDWARDS: 1.95,
                    VICENTE_LUQUE: 1.80,
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
                    TIM_JOHNSON: 1.48,
                    DANIEL_OMIELANCZUK: 2.70,
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
                    FRANCIMAR_BARROSO: 2.70,
                    DARREN_STEWART: 1.48,
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
                    JOE_DUFFY: 1.17,
                    REZA_MADADI: 5.00,
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
                    ARNOLD_ALLEN: 1.87,
                    MAKWAN_AMIRKHANI: 1.87,
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
                    MARLON_VERA: 2.20,
                    BRAD_PICKETT: 1.67,
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
                    GUNNAR_NELSON: 1.29,
                    ALAN_JOUBAN: 3.35,
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
                    JIMI_MANUWA: 1.57,
                    COREY_ANDERSON: 2.25,
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
                    MAGOMED_BIBULATOV: 1.15,
                    JENEL_LAUSA: 5.25,
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
                    KATLYN_CHOOKAGIAN: 1.69,
                    IRENE_ALDANA: 2.13,
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
                    DESMOND_GREEN: 2.60,
                    JOSH_EMMETT: 1.50,
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
                    GREGOR_GILLESPIE: 1.33,
                    ANDREW_HOLBROOK: 3.20,
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
                    JAN_BLACHOWICZ: 1.83,
                    PATRICK_CUMMINS: 1.87,
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
                    SHANE_BURGOS: 1.38,
                    CHARLES_ROSA: 3.00,
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
                    KAMARU_USMAN: 1.33,
                    SEAN_STRICKLAND: 3.10,
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
                    MYLES_JURY: 1.20,
                    MIKE_DE_LA_TORRE: 4.25,
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
                    CHARLES_OLIVEIRA: 2.75,
                    WILL_BROOKS: 1.43,
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
                    THIAGO_ALVES: 2.15,
                    PATRICK_COTE: 1.69,
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
                    CYNTHIA_CALVILLO: 1.37,
                    PEARL_GONZALEZ: 3.10,
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
                    GEGARD_MOUSASI: 1.80,
                    CHRIS_WEIDMAN: 1.93,
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
                    DANIEL_CORMIER: 2.12,
                    ANTHONY_JOHNSON: 1.68,
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
                    KETLEN_VIEIRA: 2.35,
                    ASHLEE_EVANS_SMITH: 1.56,
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
                    ZAK_CUMMINGS: 1.15,
                    NATHAN_COY: 5.00,
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
                    ANTHONY_SMITH: 3.70,
                    ANDREW_SANCHEZ: 1.28,
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
                    DEVIN_CLARK: 1.67,
                    JAKE_COLLIER: 2.20,
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
                    ALJAMAIN_STERLING: 1.24,
                    AUGUSTO_MENDES: 3.90,
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
                    TIM_ELLIOTT: 1.54,
                    LOUIS_SMOLKA: 2.49,
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
                    RASHID_MAGOMEDOV: 1.27,
                    BOBBY_GREEN: 3.70,
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
                    TOM_DUQUESNOY: 1.09,
                    PATRICK_WILLIAMS: 7.50,
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
                    ALEXANDER_VOLKOV: 1.63,
                    ROY_NELSON: 2.25,
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
                    RENATO_MOICANO: 2.40,
                    JEREMY_STEPHENS: 1.59,
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
                    ROBERT_WHITTAKER: 3.25,
                    JACARE_SOUZA: 1.35,
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
                    ROSE_NAMAJUNAS: 2.01,
                    MICHELLE_WATERSON: 1.74,
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
                    DEMETRIOUS_JOHNSON: 1.10,
                    WILSON_REIS: 6.25,
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
                    HECTOR_SANDOVAL: 2.21,
                    MATT_SCHNELL: 1.63,
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
                    BRYAN_BARBERENA: 1.29,
                    JOE_PROCTOR: 3.55,
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
                    ALEXIS_DAVIS: 1.35,
                    CINDY_DANDOIS: 3.15,
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
                    DANIELLE_TAYLOR: 1.87,
                    JESSICA_PENNE: 1.83,
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
                    SCOTT_HOLTZMAN: 1.33,
                    MICHAEL_MCBRIDE: 3.16,
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
                    BRANDON_MORENO: 2.00,
                    DUSTIN_ORTIZ: 1.77,
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
                    THALES_LEITES: 1.74,
                    SAM_ALVEY: 2.01,
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
                    MIKE_PERRY: 1.72,
                    JAKE_ELLENBERGER: 2.02,
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
                    STEVIE_RAY: 1.61,
                    JOE_LAUZON: 2.35,
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
                    JOHN_DODSON: 1.22,
                    EDDIE_WINELAND: 3.85,
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
                    OVINCE_SAINT_PREUX: 1.57,
                    MARCOS_ROGERIO_DE_LIMA: 2.37,
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
                    AL_IAQUINTA: 1.22,
                    DIEGO_SANCHEZ: 4.25,
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
                        'stats': '20-5-0',
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
                    GADZHIMURAD_ANTIGULOV: 1.25,
                    JOACHIM_CHRISTENSEN: 4.00,
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
                    ENRIQUE_BARZOLA: 2.10,
                    GABRIEL_BENITEZ: 1.69,
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
                    CORTNEY_CASEY_SANCHEZ: 1.53,
                    JESSICA_AGUILAR: 2.35,
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
                    JAMES_VICK: 1.24,
                    MARC_POLO_REYES: 4.00,
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
                    CHASE_SHERMAN: 1.78,
                    RASHAD_COULTER: 1.87,
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
                    JASON_KNIGHT: 1.83,
                    CHAS_SKELLY: 1.78,
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
                    DAVID_BRANCH: 2.42,
                    KRZYSZTOF_JOTKO: 1.54,
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
                    FRANKIE_EDGAR: 1.74,
                    YAIR_RODRIGUEZ: 2.00,
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
                    DEMIAN_MAIA: 1.79,
                    JORGE_MASVIDAL: 1.95,
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
                    JOANNA_JEDRZEJCZYK: 1.47,
                    JESSICA_ANDRADE: 2.56,
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
                    STIPE_MIOCIC: 1.57,
                    JUNIOR_DOS_SANTOS: 2.35,
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
                    DAMIR_HADZOVIC: 3.39,
                    MARCIN_HELD: 1.29,
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
                    DARREN_TILL: 1.31,
                    JESSIN_AYARI: 3.29,
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
                    BOJAN_VELICKOVIC: 1.95,
                    NICO_MUSOKE: 1.77,
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
                    JOAQUIM_SILVA: 1.59,
                    REZA_MADADI: 2.28,
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
                    TREVOR_SMITH: 2.20,
                    CHRIS_CAMOZZI: 1.65,
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
                    PEDRO_MUNHOZ: 1.14,
                    DAMIAN_STASIAK: 5.50,
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
                    JACK_HERMANSSON: 1.53,
                    ALEX_NICHOLSON: 2.45,
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
                    NORDINE_TALEB: 1.26,
                    OLIVER_ENKAMP: 3.70,
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
                    OMARI_AKHMEDOV: 3.10,
                    ABDUL_RAZAK_ALHASSAN: 1.36,
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
                    PETER_SOBOTTA: 1.74,
                    BEN_SAUNDERS: 1.95,
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
                    VOLKAN_OEZDEMIR: 4.25,
                    MISHA_CIRKUNOV: 1.21,
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
                'odds': {
                    GLOVER_TEIXEIRA: 3.30,
                    ALEXANDER_GUSTAFSSON: 1.28
                }
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
                    DEIVESON_FIGUEIREDO: 1.67,
                    MARCO_BELTRAN: 2.20,
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
                    LUAN_CHAGAS: 1.38,
                    JIMMY_WALLHEAD: 3.05,
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
                    VIVIANE_PEREIRA: 1.54,
                    JAMIE_MOYLE: 2.35,
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
                    BRIAN_KELLEHER: 3.65,
                    IURI_ALCANTARA: 1.26,
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
                    MATTHEW_LOPEZ: 1.80,
                    JOHNNY_EDUARDO: 1.91,
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
                    ANTONIO_CARLOS_JUNIOR: 1.26,
                    ERIC_SPICELY: 3.35,
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
                    RAPHAEL_ASSUNCAO: 2.80,
                    MARLON_MORAES: 1.36,
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
                    YANCY_MEDEIROS: 1.65,
                    ERICK_SILVA: 3.35,
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
                    PAULO_COSTA: 1.33,
                    OLUWALE_BAMGBOSE: 3.10,
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
                    VITOR_BELFORT: 1.52,
                    NATE_MARQUARDT: 2.50,
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
                    CLAUDIA_GADELHA: 1.26,
                    KAROLINA_KOWALKIEWICZ: 3.25,
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
                    JJ_ALDRICH: 1.47,
                    CHANMI_JEON: 2.45,
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
                    ZAK_OTTOW: 1.27,
                    KIICHI_KUNIMOTO: 3.65,
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
                    JOHN_MORAGA: 1.49,
                    ASHKAN_MOKHTARIAN: 2.50,
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
                    LUKE_JUMEAU: 2.60,
                    DOMINIQUE_STEELE: 1.49,
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
                    VINC_PICHEL: 1.80,
                    DAMIEN_BROWN: 1.87,
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
                    ALEXANDER_VOLKANOVSKI: 1.13,
                    MIZUTO_HIROTA: 5.20,
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
                    BEN_NGUYEN: 2.54,
                    TIM_ELLIOTT: 1.49,
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
                    ION_CUTELABA: 1.29,
                    HENRIQUE_DA_SILVA: 3.30,
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
                    DAN_HOOKER: 1.64,
                    ROSS_PEARSON: 2.15,
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
                    DEREK_BRUNSON: 1.35,
                    DANIEL_KELLY: 3.15,
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
                    MARK_HUNT: 2.30,
                    DERRICK_LEWIS: 1.59,
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
                    LUCIE_PUDILOVA: 1.69,
                    JI_YEON_KIM: 2.00,
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
                    NAOKI_INOUE: 1.35,
                    CARLS_JOHN_DE_TOMAS: 3.25,
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
                    RUSSEL_DOANE: 1.96,
                    KWAN_HO_KWAK: 1.74,
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
                    LI_JINGLIANG: 1.19,
                    FRANK_CAMACHO: 4.45,
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
                    ULKA_SASAKI: 4.50,
                    JUSTIN_SCOGGINS: 1.18,
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
                    ALEX_CACERES: 1.32,
                    ROLANDO_DY: 3.35,
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
                    WALT_HARRIS: 1.29,
                    CYRIL_ASKER: 3.65,
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
                    JON_TUCK: 1.27,
                    TAKANORI_GOMI: 3.45,
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
                    RAFAEL_DOS_ANJOS: 1.46,
                    TAREC_SAFFIEDINE: 2.69,
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
                    COLBY_COVINGTON: 1.29,
                    DONG_HYUN_KIM: 2.85,
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
                    MARCIN_TYBURA: 1.39,
                    ANDREI_ARLOVSKI: 2.90,
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
                    HOLLY_HOLM: 1.15,
                    BETHE_CORREIA: 3.50,
                },
            },
        ]
    },

    {
        'date': '2017-06-25',
        'name': 'UFC Fight Night: Chiesa vs Lee',
        'location': 'Oklahoma City, Oklahoma',
        'venue': 'Chesapeake Energy Arena',
        'fights': [
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JEREMY_KIMBALL,
                        'stats': '15-8-0',
                    },
                    {
                        'name': JOSH_STANSBURY,
                        'stats': '8-5-0',
                    },
                ],
                'winner': {
                    'fighter': JEREMY_KIMBALL,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:21',
                },
                'time': '18:00',
                'odds': {
                    JEREMY_KIMBALL: 2.15,
                    JOSH_STANSBURY: 1.61,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOHNNY_CASE,
                        'stats': '22-6-0',
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
                'time': '17:30',
                'odds': {
                    ANTHONY_ROCCO_MARTIN: 1.71,
                    JOHNNY_CASE: 1.98,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JARED_GORDON,
                        'stats': '14-3-0',
                    },
                    {
                        'name': MICHEL_QUINONES,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': JARED_GORDON,
                    'by': 'ko/tkko',
                    'round': 2,
                    'time': '4:24',
                },
                'time': '18:30',
                'odds': {
                    JARED_GORDON: 1.67,
                    MICHEL_QUINONES: 2.10,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DEVIN_POWELL,
                        'stats': '9-4-0',
                    },
                    {
                        'name': DARRELL_HORCHER,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': DARRELL_HORCHER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    DARRELL_HORCHER: 1.22,
                    DEVIN_POWELL: 4.25,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MARYNA_MOROZ,
                        'stats': '9-3-0',
                    },
                    {
                        'name': CARLA_ESPARZA,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': CARLA_ESPARZA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    CARLA_ESPARZA: 1.45,
                    MARYNA_MOROZ: 2.50,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': MARVIN_VETTORI,
                        'stats': '12-4-1',
                    },
                    {
                        'name': VITOR_MIRANDA,
                        'stats': '13-7-0',
                    },
                ],
                'winner': {
                    'fighter': MARVIN_VETTORI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:30',
                'odds': {
                    MARVIN_VETTORI: 1.27,
                    VITOR_MIRANDA: 3.70,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ERIK_KOCH,
                        'stats': '15-6-0',
                    },
                    {
                        'name': CLAY_GUIDA,
                        'stats': '34-15-0',
                    },
                ],
                'winner': {
                    'fighter': CLAY_GUIDA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    CLAY_GUIDA: 3.65,
                    ERIK_KOCH: 1.29,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': DENNIS_SIVER,
                        'stats': '23-11-0',
                    },
                    {
                        'name': BJ_PENN,
                        'stats': '16-13-2',
                    },
                ],
                'winner': {
                    'fighter': DENNIS_SIVER,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    DENNIS_SIVER: 1.69,
                    BJ_PENN: 2.05,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                    {
                        'name': ALEX_GARCIA,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': TIM_MEANS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    TIM_MEANS: 1.33,
                    ALEX_GARCIA: 3.25,
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
                        'name': JOACHIM_CHRISTENSEN,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': DOMINICK_REYES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:29',
                },
                'time': '22:00',
                'odds': {
                    DOMINICK_REYES: 1.29,
                    JOACHIM_CHRISTENSEN: 3.50,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JUSTINE_KISH,
                        'stats': '6-2-0',
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
                'time': '22:30',
                'odds': {
                    FELICE_HERRIG: 2.40,
                    JUSTINE_KISH: 1.57,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JOHNY_HENDRICKS,
                        'stats': '18-8-0',
                    },
                    {
                        'name': TIM_BOETSCH,
                        'stats': '21-13-0',
                    },
                ],
                'winner': {
                    'fighter': TIM_BOETSCH,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:46',
                },
                'time': '23:00',
                'odds': {
                    TIM_BOETSCH: 2.25,
                    JOHNY_HENDRICKS: 1.63,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                    {
                        'name': MICHAEL_CHIESA,
                        'stats': '15-4-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_LEE,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:37',
                },
                'time': '23:30',
                'odds': {
                    KEVIN_LEE: 1.63,
                    MICHAEL_CHIESA: 2.20,
                },
            },
        ]
    },

    {
        'date': '2017-07-07',
        'name': 'The Ultimate Fighter 25',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': TERUTO_ISHIHARA,
                        'stats': '11-6-2',
                    },
                    {
                        'name': GRAY_MAYNARD,
                        'stats': '14-8-1',
                    },
                ],
                'winner': {
                    'fighter': GRAY_MAYNARD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    GRAY_MAYNARD: 3.70,
                    TERUTO_ISHIHARA: 1.27,
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
                        'name': JULIANA_LIMA,
                        'stats': '9-5-0',
                    },
                ],
                'winner': {
                    'fighter': TECIA_TORRES,
                    'by': 'submission',
                    'round': 2,
                    'time': '0:53',
                },
                'time': '18:00',
                'odds': {
                    TECIA_TORRES: 1.20,
                    JULIANA_LIMA: 4.50,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ED_HERMAN,
                        'stats': '24-14-0',
                    },
                    {
                        'name': CB_DOLLAWAY,
                        'stats': '18-10-0',
                    },
                ],
                'winner': {
                    'fighter': CB_DOLLAWAY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    CB_DOLLAWAY: 1.57,
                    ED_HERMAN: 2.30,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': TOM_GALLICCHIO,
                        'stats': '19-11-0',
                    },
                    {
                        'name': JAMES_KRAUSE,
                        'stats': '25-8-0',
                    },
                ],
                'winner': {
                    'fighter': JAMES_KRAUSE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:20',
                'odds': {
                    JAMES_KRAUSE: 1.18,
                    TOM_GALLICCHIO: 4.75,
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
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                ],
                'winner': {
                    'fighter': ANGELA_HILL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    ANGELA_HILL: 1.28,
                    ASHLEY_YODER: 3.63,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCEL_FORTUNA,
                        'stats': '9-3-0',
                    },
                    {
                        'name': JORDAN_JOHNSON,
                        'stats': '10-0-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_JOHNSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    JORDAN_JOHNSON: 1.44,
                    MARCEL_FORTUNA: 2.45,
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
                        'name': BRAD_TAVARES,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': BRAD_TAVARES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    BRAD_TAVARES: 1.83,
                    ELIAS_THEODOROU: 1.89,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': NICK_ROEHRICK,
                        'stats': '7-1-0',
                    },
                    {
                        'name': JARED_CANNONIER,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': JARED_CANNONIER,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:08',
                },
                'time': '21:00',
                'odds': {
                    JARED_CANNONIER: 1.29,
                    NICK_ROEHRICK: 3.60,
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
                        'name': MARC_DIAKIESE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': DRAKKAR_KLOSE,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    DRAKKAR_KLOSE: 2.95,
                    MARC_DIAKIESE: 1.38,
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
                        'name': JESSE_TAYLOR,
                        'stats': '33-15-0',
                    },
                ],
                'winner': {
                    'fighter': JESSE_TAYLOR,
                    'by': 'submission',
                    'round': 2,
                    'time': '0:43',
                },
                'time': '23:00',
                'odds': {
                    JESSE_TAYLOR: 1.54,
                    DHIEGO_LIMA: 2.41,
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
                        'name': MICHAEL_JOHNSON,
                        'stats': '20-14-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_GAETHJE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:48',
                },
                'time': '23:30',
                'odds': {
                    JUSTIN_GAETHJE: 2.28,
                    MICHAEL_JOHNSON: 1.62,
                },
            },
        ]
    },

    {
        'date': '2017-07-08',
        'name': 'UFC 213: Romero vs Whittaker',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JAMES_BOCHNOVIC,
                        'stats': '8-3-0',
                    },
                    {
                        'name': TREVIN_GILES,
                        'stats': '11-0-0',
                    },
                ],
                'winner': {
                    'fighter': TREVIN_GILES,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:54',
                },
                'time': '18:30',
                'odds': {
                    TREVIN_GILES: 1.36,
                    JAMES_BOCHNOVIC: 3.10,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': TERRION_WARE,
                        'stats': '17-8-0',
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
                'time': '18:55',
                'odds': {
                    CODY_STAMANN: 1.40,
                    TERRION_WARE: 2.95,
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
                        'name': JORDAN_MEIN,
                        'stats': '31-12-0',
                    },
                ],
                'winner': {
                    'fighter': BELAL_MUHAMMAD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    BELAL_MUHAMMAD: 1.70,
                    JORDAN_MEIN: 2.10,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': GERALD_MEERSCHAERT,
                        'stats': '28-11-0',
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
                    'time': '2:04',
                },
                'time': '20:30',
                'odds': {
                    THIAGO_SANTOS: 1.61,
                    GERALD_MEERSCHAERT: 2.31,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BRIAN_CAMOZZI,
                        'stats': '7-5-0',
                    },
                    {
                        'name': CHAD_LAPRISE,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': CHAD_LAPRISE,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:27',
                },
                'time': '21:00',
                'odds': {
                    CHAD_LAPRISE: 1.15,
                    BRIAN_CAMOZZI: 5.25,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSEI_OLEINIK,
                        'stats': '57-11-1',
                    },
                    {
                        'name': TRAVIS_BROWNE,
                        'stats': '18-7-1',
                    },
                ],
                'winner': {
                    'fighter': ALEKSEI_OLEINIK,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:44',
                },
                'time': '21:30',
                'odds': {
                    ALEKSEI_OLEINIK: 3.25,
                    TRAVIS_BROWNE: 1.33,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ROB_FONT,
                        'stats': '16-4-0',
                    },
                    {
                        'name': DOUGLAS_SILVA_DE_ANDRADE,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': ROB_FONT,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:36',
                },
                'time': '19:30',
                'odds': {
                    ROB_FONT: 1.33,
                    DOUGLAS_SILVA_DE_ANDRADE: 3.25,
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
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_PETTIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    ANTHONY_PETTIS: 1.38,
                    JIM_MILLER: 3.00,
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
                        'name': DANIEL_OMIELANCZUK,
                        'stats': '19-8-1',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_BLAYDES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    CURTIS_BLAYDES: 1.15,
                    DANIEL_OMIELANCZUK: 5.00,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': FABRICIO_WERDUM,
                        'stats': '23-8-1',
                    },
                    {
                        'name': ALISTAIR_OVEREEM,
                        'stats': '44-17-0',
                    },
                ],
                'winner': {
                    'fighter': ALISTAIR_OVEREEM,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ALISTAIR_OVEREEM: 1.68,
                    FABRICIO_WERDUM: 2.15,
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
                        'name': YOEL_ROMERO,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': ROBERT_WHITTAKER,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    ROBERT_WHITTAKER: 1.78,
                    YOEL_ROMERO: 1.95,
                },
            },
        ]
    },

    {
        'date': '2017-07-16',
        'name': 'UFC Fight Night: Nelson vs Ponzinibbio',
        'location': 'Glasgow, United Kingdom',
        'venue': 'The SSE Hydro',
        'fights': [
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': AMANDA_LEMOS,
                        'stats': '6-1-1',
                    },
                    {
                        'name': LESLIE_SMITH,
                        'stats': '10-7-1',
                    },
                ],
                'winner': {
                    'fighter': LESLIE_SMITH,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:53',
                },
                'time': '12:00',
                'odds': {
                    LESLIE_SMITH: 1.44,
                    AMANDA_LEMOS: 2.70,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRETT_JOHNS,
                        'stats': '15-2-0',
                    },
                    {
                        'name': ALBERT_MORALES,
                        'stats': '7-4-1',
                    },
                ],
                'winner': {
                    'fighter': BRETT_JOHNS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:30',
                'odds': {
                    BRETT_JOHNS: 1.27,
                    ALBERT_MORALES: 3.65,
                }
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DANIEL_TEYMUR,
                        'stats': '6-3-0',
                    },
                    {
                        'name': DANNY_HENRY,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': DANNY_HENRY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '13:00',
                'odds': {
                    DANNY_HENRY: 2.40,
                    DANIEL_TEYMUR: 1.52,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GALORE_BOFANDO,
                        'stats': '5-3-0',
                    },
                    {
                        'name': CHARLIE_WARD,
                        'stats': '3-3-0',
                    },
                ],
                'winner': {
                    'fighter': GALORE_BOFANDO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:10',
                },
                'time': '13:30',
                'odds': {
                    GALORE_BOFANDO: 1.44,
                    CHARLIE_WARD: 2.60,
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
                        'name': NEIL_SEERY,
                        'stats': '16-13-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDRE_PANTOJA,
                    'by': 'submission',
                    'round': 3,
                    'time': '2:31',
                },
                'time': '14:00',
                'odds': {
                    ALEXANDRE_PANTOJA: 1.28,
                    NEIL_SEERY: 3.70,
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
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': DANNY_ROBERTS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:59',
                },
                'time': '14:30',
                'odds': {
                    DANNY_ROBERTS: 1.50,
                    BOBBY_NASH: 2.54,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JAMES_MULHERON,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JUSTIN_WILLIS,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_WILLIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:00',
                'odds': {
                    JUSTIN_WILLIS: 1.54,
                    JAMES_MULHERON: 2.33,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': PAUL_CRAIG,
                        'stats': '11-3-0',
                    },
                    {
                        'name': KHALIL_ROUNTREE,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': KHALIL_ROUNTREE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:56',
                },
                'time': '15:30',
                'odds': {
                    KHALIL_ROUNTREE: 1.63,
                    PAUL_CRAIG: 2.20,
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
                        'name': RYAN_JANES,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_MARSHMAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:00',
                'odds': {
                    JACK_MARSHMAN: 1.17,
                    RYAN_JANES: 4.75,
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
                        'name': PAUL_FELDER,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': PAUL_FELDER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:57',
                },
                'time': '16:30',
                'odds': {
                    PAUL_FELDER: 2.58,
                    STEVIE_RAY: 1.50,
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
                        'name': JOANNE_CALDERWOOD,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': CYNTHIA_CALVILLO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:00',
                'odds': {
                    CYNTHIA_CALVILLO: 1.48,
                    JOANNE_CALDERWOOD: 2.69,
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
                        'name': GUNNAR_NELSON,
                        'stats': '17-4-1',
                    },
                ],
                'winner': {
                    'fighter': SANTIAGO_PONZINIBBIO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:22',
                },
                'time': '17:30',
                'odds': {
                    SANTIAGO_PONZINIBBIO: 2.46,
                    GUNNAR_NELSON: 1.52,
                },
            },
        ]
    },

    {
        'date': '2017-07-22',
        'name': 'UFC Fight Night: Weidman vs Gastelum',
        'location': 'Uniondale, New York',
        'venue': 'Nassau Veterans Memorial Coliseum',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FRANKIE_PEREZ,
                        'stats': '10-4-0',
                    },
                    {
                        'name': CHRIS_WADE,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': CHRIS_WADE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:00',
                'odds': {
                    CHRIS_WADE: 1.28,
                    FRANKIE_PEREZ: 3.67,
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
                        'name': GODOFREDO_PEPEY,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': SHANE_BURGOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:30',
                'odds': {
                    SHANE_BURGOS: 1.13,
                    GODOFREDO_PEPEY: 5.50,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUNIOR_ALBINI,
                        'stats': '14-5-0',
                    },
                    {
                        'name': TIM_JOHNSON,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': JUNIOR_ALBINI,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:51',
                },
                'time': '17:00',
                'odds': {
                    JUNIOR_ALBINI: 3.25,
                    TIM_JOHNSON: 1.33,
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
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:18',
                },
                'time': '17:12',
                'odds': {
                    MARLON_VERA: 2.80,
                    BRIAN_KELLEHER: 1.43,
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
                        'name': KYLE_BOCHNIAK,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': JEREMY_KENNEDY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:06',
                'odds': {
                    JEREMY_KENNEDY: 1.32,
                    KYLE_BOCHNIAK: 3.31,
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
                        'name': DAMIAN_GRABOWSKI,
                        'stats': '20-5-0',
                    },
                ],
                'winner': {
                    'fighter': CHASE_SHERMAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:06',
                'odds': {
                    CHASE_SHERMAN: 1.40,
                    DAMIAN_GRABOWSKI: 2.90,
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
                        'name': RYAN_LAFLARE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_OLIVEIRA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:50',
                },
                'time': '18:39',
                'odds': {
                    ALEX_OLIVEIRA: 2.38,
                    RYAN_LAFLARE: 1.57,
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
                        'name': RAFAEL_NATAL,
                        'stats': '21-9-1',
                    },
                ],
                'winner': {
                    'fighter': ERYK_ANDERS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:54',
                },
                'time': '19:06',
                'odds': {
                    ERYK_ANDERS: 1.80,
                    RAFAEL_NATAL: 1.95,
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
                        'name': ELIZEU_DOS_SANTOS,
                        'stats': '20-5-0',
                    },
                ],
                'winner': {
                    'fighter': ELIZEU_DOS_SANTOS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    ELIZEU_DOS_SANTOS: 2.25,
                    LYMAN_GOOD: 1.63,
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
                        'name': THOMAS_ALMEIDA,
                        'stats': '21-3-0',
                    },
                ],
                'winner': {
                    'fighter': JIMMIE_RIVERA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:15',
                'odds': {
                    JIMMIE_RIVERA: 1.49,
                    THOMAS_ALMEIDA: 2.60,
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
                        'name': PATRICK_CUMMINS,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': PATRICK_CUMMINS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:54',
                'odds': {
                    PATRICK_CUMMINS: 2.65,
                    GIAN_VILLANTE: 1.44,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_ELKINS,
                        'stats': '25-7-0',
                    },
                    {
                        'name': DENNIS_BERMUDEZ,
                        'stats': '18-9-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_ELKINS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:27',
                'odds': {
                    DARREN_ELKINS: 2.65,
                    DENNIS_BERMUDEZ: 1.45,
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
                        'name': KELVIN_GASTELUM,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': CHRIS_WEIDMAN,
                    'by': 'submission',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    CHRIS_WEIDMAN: 2.30,
                    KELVIN_GASTELUM: 1.56,
                },
            },
        ]
    },

    {
        'date': '2017-07-29',
        'name': 'UFC 214: Cormier vs Jones 2',
        'location': 'Anaheim, California',
        'venue': 'Honda Center',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOSHUA_BURKMAN,
                        'stats': '29-17-0',
                    },
                    {
                        'name': DREW_DOBER,
                        'stats': '20-9-0',
                    },
                ],
                'winner': {
                    'fighter': DREW_DOBER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:04',
                },
                'time': '18:30',
                'odds': {
                    DREW_DOBER: 1.31,
                    JOSHUA_BURKMAN: 3.35,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JARRED_BROOKS,
                        'stats': '14-2-0',
                    },
                    {
                        'name': ERIC_SHELTON,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': JARRED_BROOKS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    JARRED_BROOKS: 1.66,
                    ERIC_SHELTON: 2.20,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': KAILIN_CURRAN,
                        'stats': '4-6-0',
                    },
                    {
                        'name': ALEXANDRA_ALBU,
                        'stats': '7-1-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDRA_ALBU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ALEXANDRA_ALBU: 1.53,
                    KAILIN_CURRAN: 2.52,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CALVIN_KATTAR,
                        'stats': '19-3-0',
                    },
                    {
                        'name': ANDRE_FILI,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': CALVIN_KATTAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    CALVIN_KATTAR: 3.83,
                    ANDRE_FILI: 1.26,
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
                        'name': BRIAN_ORTEGA,
                        'stats': '14-1-0',
                    },
                ],
                'winner': {
                    'fighter': BRIAN_ORTEGA,
                    'by': 'submission',
                    'round': 3,
                    'time': '2:59',
                },
                'time': '20:30',
                'odds': {
                    BRIAN_ORTEGA: 2.35,
                    RENATO_MOICANO: 1.50,
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
                        'name': RENAN_BARAO,
                        'stats': '36-8-0',
                    },
                ],
                'winner': {
                    'fighter': ALJAMAIN_STERLING,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    ALJAMAIN_STERLING: 2.08,
                    RENAN_BARAO: 1.70,
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
                        'name': RICARDO_LAMAS,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_LAMAS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:34',
                },
                'time': '21:30',
                'odds': {
                    RICARDO_LAMAS: 1.91,
                    JASON_KNIGHT: 1.79,
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
                        'name': JIMI_MANUWA,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': VOLKAN_OEZDEMIR,
                    'by': 'ko/kto',
                    'round': 1,
                    'time': '0:42',
                },
                'time': '22:00',
                'odds': {
                    VOLKAN_OEZDEMIR: 2.54,
                    JIMI_MANUWA: 1.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ROBBIE_LAWLER,
                        'stats': '28-13-0',
                    },
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                ],
                'winner': {
                    'fighter': ROBBIE_LAWLER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ROBBIE_LAWLER: 1.61,
                    DONALD_CERRONE: 2.28,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CRIS_CYBORG,
                        'stats': '20-2-0',
                    },
                    {
                        'name': TONYA_EVINGER,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': CRIS_CYBORG,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:56',
                },
                'time': '22:45',
                'odds': {
                    CRIS_CYBORG: 1.08,
                    TONYA_EVINGER: 8.50,
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
                        'name': DEMIAN_MAIA,
                        'stats': '26-9-0',
                    },
                ],
                'winner': {
                    'fighter': TYRON_WOODLEY,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:10',
                'odds': {
                    TYRON_WOODLEY: 1.41,
                    DEMIAN_MAIA: 2.85,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JON_JONES,
                        'stats': '24-1-0',
                    },
                    {
                        'name': DANIEL_CORMIER,
                        'stats': '22-1-0',
                    },
                ],
                'winner': {
                    'fighter': JON_JONES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:01',
                },
                'time': '23:40',
                'odds': {
                    JON_JONES: 1.30,
                    DANIEL_CORMIER: 3.50,
                },
            },
        ]
    },

    {
        'date': '2017-08-05',
        'name': 'UFC Fight Night: Pettis vs Moreno',
        'location': 'Mexico City, Mexico',
        'venue': 'Mexico City Arena',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_RINALDI,
                        'stats': '14-7-0',
                    },
                    {
                        'name': ALVARO_HERRERA,
                        'stats': '9-6-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_RINALDI,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:01',
                },
                'time': '19:00',
                'odds': {
                    ALVARO_HERRERA: 2.75,
                    JORDAN_RINALDI: 1.43,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ROBERTO_SANCHEZ,
                        'stats': '8-2-0',
                    },
                    {
                        'name': JOSEPH_MORALES,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOSEPH_MORALES,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:56',
                },
                'time': '19:30',
                'odds': {
                    JOSEPH_MORALES: 1.95,
                    ROBERTO_SANCHEZ: 1.80,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JOSE_QUINONEZ,
                        'stats': '8-3-0',
                    },
                    {
                        'name': DIEGO_RIVAS,
                        'stats': '7-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOSE_QUINONEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    JOSE_QUINONEZ: 1.40,
                    DIEGO_RIVAS: 2.85,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': HENRY_BRIONES,
                        'stats': '19-8-1',
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
                    'time': '2:01',
                },
                'time': '20:30',
                'odds': {
                    RANI_YAHYA: 1.44,
                    HENRY_BRIONES: 2.75,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': HECTOR_SANDOVAL,
                        'stats': '14-4-0',
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
                    'time': '0:15',
                },
                'time': '21:00',
                'odds': {
                    DUSTIN_ORTIZ: 1.53,
                    HECTOR_SANDOVAL: 2.50,
                },
            },
            {
                'wiehgt_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACK_HERMANSSON,
                        'stats': '19-4-0',
                    },
                    {
                        'name': BRADLEY_SCOTT,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_HERMANSSON,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:50',
                },
                'time': '21:30',
                'odds': {
                    JACK_HERMANSSON: 1.35,
                    BRADLEY_SCOTT: 3.25,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_SOUKHAMTHATH,
                        'stats': '13-6-0',
                    },
                    {
                        'name': ALEJANDRO_PEREZ,
                        'stats': '22-7-1',
                    },
                ],
                'winner': {
                    'fighter': ALEJANDRO_PEREZ,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    ALEJANDRO_PEREZ: 1.57,
                    ANDRE_SOUKHAMTHATH: 2.15,
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
                        'name': RASHAD_EVANS,
                        'stats': '24-8-1',
                    },
                ],
                'winner': {
                    'fighter': SAM_ALVEY,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    SAM_ALVEY: 1.71,
                    RASHAD_EVANS: 2.05,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HUMBERTO_BANDENAY,
                        'stats': '14-6-0',
                    },
                    {
                        'name': MARTIN_BRAVO,
                        'stats': '12-2-0',
                    },
                ],
                'winner': {
                    'fighter': HUMBERTO_BANDENAY,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:26',
                },
                'time': '23:00',
                'odds': {
                    HUMBERTO_BANDENAY: 3.15,
                    MARTIN_BRAVO: 1.33,
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
                        'name': ALAN_JOUBAN,
                        'stats': '16-6-0',
                    },
                ],
                'winner': {
                    'fighter': NIKO_PRICE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:44',
                },
                'time': '23:30',
                'odds': {
                    NIKO_PRICE: 2.45,
                    ALAN_JOUBAN: 1.53,
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
                        'name': RANDA_MARKOS,
                        'stats': '9-7-1',
                    },
                ],
                'winner': {
                    'fighter': ALEXA_GRASSO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:45',
                'odds': {
                    ALEXA_GRASSO: 1.45,
                    RANDA_MARKOS: 2.60,
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
                        'name': SERGIO_PETTIS,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': SERGIO_PETTIS,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:58',
                'odds': {
                    SERGIO_PETTIS: 2.35,
                    BRANDON_MORENO: 1.57,
                },
            },
        ]
    },

    {
        'date': '2017-09-02',
        'name': 'UFC Fight Night: Volkov vs Struve',
        'location': 'Rotterdam, Netherlands',
        'venue': 'Ahoy Rotterdam',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': THIBAULT_GOUTI,
                        'stats': '12-5-0',
                    },
                    {
                        'name': ANDREW_HOLBROOK,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': THIBAULT_GOUTI,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:28',
                },
                'time': '11:30',
                'odds': {
                    THIBAULT_GOUTI: 2.40,
                    ANDREW_HOLBROOK: 1.56,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': BOJAN_MIHAJLOVIC,
                        'stats': '10-6-0',
                    },
                    {
                        'name': ABDUL_KERIM_EDILOV,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': ABDUL_KERIM_EDILOV,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:32',
                },
                'time': '12:00',
                'odds': {
                    ABDUL_KERIM_EDILOV: 1.15,
                    BOJAN_MIHAJLOVIC: 5.25,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_SANTIAGO,
                        'stats': '21-12-0',
                    },
                    {
                        'name': ZABIT_MAGOMEDSHARIPOV,
                        'stats': '17-1-0',
                    },
                ],
                'winner': {
                    'fighter': ZABIT_MAGOMEDSHARIPOV,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:22',
                },
                'time': '11:49',
                'odds': {
                    ZABIT_MAGOMEDSHARIPOV: 1.22,
                    MIKE_SANTIAGO: 4.00,
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
                        'name': FRANCIMAR_BARROSO,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSANDAR_RAKIC,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '13:00',
                'odds': {
                    ALEKSANDAR_RAKIC: 1.65,
                    FRANCIMAR_BARROSO: 2.10,
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
                        'name': RUSTAM_KHABILOV,
                        'stats': '23-4-0',
                    },
                ],
                'winner': {
                    'fighter': RUSTAM_KHABILOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '13:30',
                'odds': {
                    RUSTAM_KHABILOV: 1.37,
                    DESMOND_GREEN: 3.10,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MADS_BURNELL,
                        'stats': '9-3-0',
                    },
                    {
                        'name': MICHEL_PRAZERES,
                        'stats': '26-3-0',
                    },
                ],
                'winner': {
                    'fighter': MICHEL_PRAZERES,
                    'by': 'submission',
                    'round': 3,
                    'time': '1:26',
                },
                'time': '14:00',
                'odds': {
                    MICHEL_PRAZERES: 1.25,
                    MADS_BURNELL: 4.00,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FELIPE_SILVA,
                        'stats': '8-2-0',
                    },
                    {
                        'name': MAIRBEK_TAISUMOV,
                        'stats': '27-5-0',
                    },
                ],
                'winner': {
                    'fighter': MAIRBEK_TAISUMOV,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:24',
                },
                'time': '14:00',
                'odds': {
                    MAIRBEK_TAISUMOV: 1.17,
                    FELIPE_SILVA: 5.00,
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
                'time': '14:45',
                'odds': {
                    DARREN_TILL: 1.50,
                    BOJAN_VELICKOVIC: 2.60,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LEON_EDWARDS,
                        'stats': '17-3-0',
                    },
                    {
                        'name': BRYAN_BARBERENA,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': LEON_EDWARDS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:00',
                'odds': {
                    LEON_EDWARDS: 1.37,
                    BRYAN_BARBERENA: 3.00,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': TALITA_BERNARDO,
                        'stats': '6-3-0',
                    },
                    {
                        'name': MARION_RENEAU,
                        'stats': '9-5-1',
                    },
                ],
                'winner': {
                    'fighter': MARION_RENEAU,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:54',
                },
                'time': '16:00',
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ROB_WILKINSON,
                        'stats': '11-2-0',
                    },
                    {
                        'name': SIYAR_BAHADURZADA,
                        'stats': '24-7-1',
                    },
                ],
                'winner': {
                    'fighter': SIYAR_BAHADURZADA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:10',
                },
                'time': '16:10',
                'odds': {
                    SIYAR_BAHADURZADA: 1.74,
                    ROB_WILKINSON: 1.95,
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
                        'name': STEFAN_STRUVE,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKOV,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:30',
                },
                'time': '16:00',
                'odds': {
                    ALEXANDER_VOLKOV: 1.67,
                    STEFAN_STRUVE: 2.01,
                },
            },
        ]
    },

    {
        'date': '2017-09-09',
        'name': 'UFC 215: Nunes vs Shevchenko 2',
        'location': 'Edmonton, Alberta',
        'venue': 'Rogers Place',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KAJAN_JOHNSON,
                        'stats': '23-14-1',
                    },
                    {
                        'name': ADRIANO_MARTINS,
                        'stats': '28-9-0',
                    },
                ],
                'winner': {
                    'fighter': KAJAN_JOHNSON,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:49',
                },
                'time': '18:15',
                'odds': {
                    KAJAN_JOHNSON: 5.00,
                    ADRIANO_MARTINS: 1.17,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ARJAN_BHULLAR,
                        'stats': '8-1-0',
                    },
                    {
                        'name': LUIS_HENRIQUE,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': ARJAN_BHULLAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:45',
                'odds': {
                    ARJAN_BHULLAR: 1.47,
                    LUIS_HENRIQUE: 2.70,
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
                        'name': MITCH_CLARKE,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_WHITE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:36',
                },
                'time': '19:15',
                'odds': {
                    ALEX_WHITE: 1.44,
                    MITCH_CLARKE: 2.75,
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
                        'name': RICK_GLENN,
                        'stats': '21-6-1',
                    },
                ],
                'winner': {
                    'fighter': RICK_GLENN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    GAVIN_TUCKER: 1.27,
                    RICK_GLENN: 3.85
                }
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ASHLEE_EVANS_SMITH,
                        'stats': '6-4-0',
                    },
                    {
                        'name': SARAH_MORAS,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': SARAH_MORAS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:36',
                },
                'time': '20:30',
                'odds': {
                    SARAH_MORAS: 3.40,
                    ASHLEE_EVANS_SMITH: 1.31,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': KETLEN_VIEIRA,
                        'stats': '10-0-0',
                    },
                    {
                        'name': SARA_MCMANN,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': KETLEN_VIEIRA,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:16',
                },
                'time': '21:30',
                'odds': {
                    KETLEN_VIEIRA: 2.65,
                    SARA_MCMANN: 1.44,
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
                        'name': GILBERT_MELENDEZ,
                        'stats': '22-7-0',
                    },
                ],
                'winner': {
                    'fighter': JEREMY_STEPHENS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    JEREMY_STEPHENS: 1.80,
                    GILBERT_MELENDEZ: 1.87,
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
                        'name': ILIR_LATIFI,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': ILIR_LATIFI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ILIR_LATIFI: 2.11,
                    TYSON_PEDRO: 1.67,
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
                        'name': WILSON_REIS,
                        'stats': '23-9-0',
                    },
                ],
                'winner': {
                    'fighter': HENRY_CEJUDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:25',
                },
                'time': '21:00',
                'odds': {
                    HENRY_CEJUDO: 1.22,
                    WILSON_REIS: 4.00,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NEIL_MAGNY,
                        'stats': '21-8-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': RAFAEL_DOS_ANJOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:43',
                },
                'time': '23:00',
                'odds': {
                    RAFAEL_DOS_ANJOS: 1.48,
                    NEIL_MAGNY: 2.58,
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
                        'name': AMANDA_NUNES,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': AMANDA_NUNES,
                    'by': 's.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    AMANDA_NUNES: 2.15,
                    VALENTINA_SHEVCHENKO: 1.69,
                },
            },
        ]
    },

    {
        'date': '2017-09-16',
        'name': 'UFC Fight Night: Rockhold vs Branch',
        'location': 'Pittsburgh, Pennsylvania',
        'venue': 'PPG Paints Arena',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GILBERT_BURNS,
                        'stats': '14-3-0',
                    },
                    {
                        'name': JASON_SAGGO,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': GILBERT_BURNS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:55',
                },
                'time': '20:00',
                'odds': {
                    GILBERT_BURNS: 1.65,
                    JASON_SAGGO: 2.20,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KRZYSZTOF_JOTKO,
                        'stats': '19-4-0',
                    },
                    {
                        'name': URIAH_HALL,
                        'stats': '15-9-0',
                    },
                ],
                'winner': {
                    'fighter': URIAH_HALL,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:25',
                },
                'time': '20:15',
                'odds': {
                    URIAH_HALL: 2.60,
                    KRZYSZTOF_JOTKO: 1.48,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DANIEL_SPITZ,
                        'stats': '6-2-0',
                    },
                    {
                        'name': ANTHONY_HAMILTON,
                        'stats': '15-9-0',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_SPITZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:24',
                },
                'time': '20:30',
                'odds': {
                    DANIEL_SPITZ: 2.58,
                    ANTHONY_HAMILTON: 1.49,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': OLIVIER_AUBIN_MERCIER,
                        'stats': '12-4-0',
                    },
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': OLIVIER_AUBIN_MERCIER,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:36',
                'odds': {
                    OLIVIER_AUBIN_MERCIER: 1.82,
                    ANTHONY_ROCCO_MARTIN: 1.77,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ZU_ANYANWU,
                        'stats': '14-5-0',
                    },
                    {
                        'name': JUSTIN_LEDET,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_LEDET,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    JUSTIN_LEDET: 1.20,
                    ZU_ANYANWU: 4.34,
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
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                ],
                'winner': {
                    'fighter': KAMARU_USMAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:48',
                },
                'time': '22:15',
                'odds': {
                    KAMARU_USMAN: 1.10,
                    SERGIO_MORAES: 6.50,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JASON_GONZALEZ,
                        'stats': '11-4-0',
                    },
                    {
                        'name': GREGOR_GILLESPIE,
                        'stats': '13-0-0',
                    },
                ],
                'winner': {
                    'fighter': GREGOR_GILLESPIE,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:11',
                },
                'time': '22:30',
                'odds': {
                    GREGOR_GILLESPIE: 1.22,
                    JASON_GONZALEZ: 4.00,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': HECTOR_LOMBARD,
                        'stats': '34-9-1',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_SMITH,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:33',
                },
                'time': '23:40',
                'odds': {
                    ANTHONY_SMITH: 1.61,
                    HECTOR_LOMBARD: 2.19,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_REYES,
                        'stats': '13-3-0',
                    },
                    {
                        'name': MIKE_PERRY,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': MIKE_PERRY,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:19',
                },
                'time': '23:00',
                'odds': {
                    MIKE_PERRY: 1.22,
                    ALEX_REYES: 4.20,
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
                        'name': LUKE_ROCKHOLD,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': LUKE_ROCKHOLD,
                    'by': 'koo/tko',
                    'round': 2,
                    'time': '4:05',
                },
                'time': '23:15',
                'odds': {
                    LUKE_ROCKHOLD: 1.17,
                    DAVID_BRANCH: 4.75,
                },
            },
        ]
    },

    {
        'date': '2017-09-22',
        'name': 'UFC Fight Night: Saint Preux vs Okami',
        'location': 'Saitama, Japan',
        'venue': 'Saitama Super Arena',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAICHI_ABE,
                        'stats': '6-2-0',
                    },
                    {
                        'name': HYUN_GYU_KIM,
                        'stats': '13-7-1',
                    },
                ],
                'winner': {
                    'fighter': DAICHI_ABE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    DAICHI_ABE: 1.87,
                    HYUN_GYU_KIM: 1.77,
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
                        'name': SHINSHO_ANZAI,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': SHINSHO_ANZAI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:40',
                'odds': {
                    SHINSHO_ANZAI: 3.00,
                    LUKE_JUMEAU: 1.38,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': SYURI_KONDO,
                        'stats': '6-2-0',
                    },
                    {
                        'name': CHANMI_JEON,
                        'stats': '5-2-0',
                    },
                ],
                'winner': {
                    'fighter': SYURI_KONDO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:11',
                'odds': {
                    SYURI_KONDO: 1.61,
                    CHANMI_JEON: 2.25,
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
                'time': '21:39',
                'odds': {
                    KEITA_NAKAMURA: 1.86,
                    ALEX_MORONO: 1.83,
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
                        'name': JUSSIER_FORMIGA,
                        'stats': '23-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUSSIER_FORMIGA,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:30',
                },
                'time': '22:14',
                'odds': {
                    JUSSIER_FORMIGA: 1.23,
                    ULKA_SASAKI: 4.00,
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
                        'name': TERUTO_ISHIHARA,
                        'stats': '11-6-2',
                    },
                ],
                'winner': {
                    'fighter': TERUTO_ISHIHARA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:35',
                'odds': {
                    TERUTO_ISHIHARA: 1.54,
                    ROLANDO_DY: 2.40,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GOKHAN_SAKI,
                        'stats': '1-2-0',
                    },
                    {
                        'name': HENRIQUE_DA_SILVA,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': GOKHAN_SAKI,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:45',
                },
                'time': '23:00',
                'odds': {
                    GOKHAN_SAKI: 1.47,
                    HENRIQUE_DA_SILVA: 2.54,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DONG_HYUN_KIM,
                        'stats': '16-8-3',
                    },
                    {
                        'name': TAKANORI_GOMI,
                        'stats': '35-14-0',
                    },
                ],
                'winner': {
                    'fighter': DONG_HYUN_KIM,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:30',
                },
                'time': '23:30',
                'odds': {
                    DONG_HYUN_KIM: 1.27,
                    TAKANORI_GOMI: 3.80,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CLAUDIA_GADELHA,
                        'stats': '16-4-0',
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
                'time': '23:45',
                'odds': {
                    JESSICA_ANDRADE: 3.39,
                    CLAUDIA_GADELHA: 1.31,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': YUSHIN_OKAMI,
                        'stats': '34-13-0',
                    },
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '23-12-0',
                    },
                ],
                'winner': {
                    'fighter': OVINCE_SAINT_PREUX,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:50',
                },
                'time': '23:59',
                'odds': {
                    OVINCE_SAINT_PREUX: 1.20,
                    YUSHIN_OKAMI: 4.40,
                },
            },
        ]
    },

    {
        'date': '2017-10-07',
        'name': 'UFC 216: Ferguson vs Lee',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': BRAD_TAVARES,
                        'stats': '17-5-0',
                    },
                    {
                        'name': THALES_LEITES,
                        'stats': '28-9-0',
                    },
                ],
                'winner': {
                    'fighter': BRAD_TAVARES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    BRAD_TAVARES: 1.53,
                    THALES_LEITES: 2.40,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MAGOMED_BIBULATOV,
                        'stats': '14-1-0',
                    },
                    {
                        'name': JOHN_MORAGA,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_MORAGA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:38',
                },
                'time': '19:00',
                'odds': {
                    JOHN_MORAGA: 4.50,
                    MAGOMED_BIBULATOV: 1.19,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MATT_SCHNELL,
                        'stats': '13-4-0',
                    },
                    {
                        'name': MARCO_BELTRAN,
                        'stats': '8-7-0',
                    },
                ],
                'winner': {
                    'fighter': MATT_SCHNELL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:00',
                'odds': {
                    MATT_SCHNELL: 1.71,
                    MARCO_BELTRAN: 2.05,
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
                        'name': POLIANA_BOTELHO,
                        'stats': '7-2-0',
                    },
                ],
                'winner': {
                    'fighter': POLIANA_BOTELHO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    POLIANA_BOTELHO: 1.59,
                    PEARL_GONZALEZ: 2.30,
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
                        'name': BOBBY_GREEN,
                        'stats': '24-9-1',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    BOBBY_GREEN: 2.50,
                    LANDO_VANNATA: 1.53,
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
                        'name': TOM_DUQUESNOY,
                        'stats': '16-2-0',
                    },
                ],
                'winner': {
                    'fighter': CODY_STAMANN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    CODY_STAMANN: 2.33,
                    TOM_DUQUESNOY: 1.59,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': EVAN_DUNHAM,
                        'stats': '18-7-1',
                    },
                    {
                        'name': BENEIL_DARIUSH,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    BENEIL_DARIUSH: 1.42,
                    EVAN_DUNHAM: 2.75,
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
                        'name': MARA_ROMERO_BORELLA,
                        'stats': '13-5-0',
                    },
                ],
                'winner': {
                    'fighter': MARA_ROMERO_BORELLA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:54',
                },
                'time': '22:30',
                'odds': {
                    MARA_ROMERO_BORELLA: 2.95,
                    KALINDRA_FARIA: 1.39,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': FABRICIO_WERDUM,
                        'stats': '23-8-1',
                    },
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': FABRICIO_WERDUM,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:05',
                },
                'time': '23:00',
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': RAY_BORG,
                        'stats': '11-4-0',
                    },
                    {
                        'name': DEMETRIOUS_JOHNSON,
                        'stats': '27-3-1',
                    },
                ],
                'winner': {
                    'fighter': DEMETRIOUS_JOHNSON,
                    'by': 'submission',
                    'round': 5,
                    'time': '3:15',
                },
                'time': '23:30',
                'odds': {
                    DEMETRIOUS_JOHNSON: 1.09,
                    RAY_BORG: 7.47,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                    {
                        'name': TONY_FERGUSON,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': TONY_FERGUSON,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:02',
                },
                'time': '23:55',
                'odds': {
                    TONY_FERGUSON: 1.34,
                    KEVIN_LEE: 3.25,
                },
            },
        ]
    },

    {
        'date': '2017-10-21',
        'name': 'UFC Fight Night: Cerrone vs Till',
        'location': 'Gdansk, Poland',
        'venue': 'Ergo Arena',
        'fights': [
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JOSH_EMMETT,
                        'stats': '14-2-0',
                    },
                    {
                        'name': FELIPE_ARANTES,
                        'stats': '18-10-1',
                    },
                ],
                'winner': {
                    'fighter': JOSH_EMMETT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '11:45',
                'odds': {
                    JOSH_EMMETT: 1.42,
                    FELIPE_ARANTES: 2.90,
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
                        'name': LINA_LANSBERG,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': ASPEN_LADD,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:33',
                },
                'time': '12:00',
                'odds': {
                    ASPEN_LADD: 1.40,
                    LINA_LANSBERG: 2.90,
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
                        'name': WARLLEY_ALVES,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': WARLLEY_ALVES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:15',
                'odds': {
                    WARLLEY_ALVES: 1.31,
                    SALIM_TOUAHRI: 3.35,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ARTEM_LOBOV,
                        'stats': '14-15-1',
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
                'time': '13:30',
                'odds': {
                    ANDRE_FILI: 1.54,
                    ARTEM_LOBOV: 2.40,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': RAMAZAN_EMEEV,
                        'stats': '18-3-0',
                    },
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': RAMAZAN_EMEEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '13:55',
                'odds': {
                    RAMAZAN_EMEEV: 1.61,
                    SAM_ALVEY: 2.30,
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
                        'name': DAMIAN_STASIAK,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': BRIAN_KELLEHER,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:39',
                },
                'time': '14:20',
                'odds': {
                    BRIAN_KELLEHER: 1.91,
                    DAMIAN_STASIAK: 1.83,
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
                        'name': MARCIN_HELD,
                        'stats': '23-7-0',
                    },
                ],
                'winner': {
                    'fighter': MARCIN_HELD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:45',
                'odds': {
                    MARCIN_HELD: 1.27,
                    NASRAT_HAQPARAST: 3.80,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': OSKAR_PIECHOTA,
                        'stats': '11-1-1',
                    },
                    {
                        'name': JONATHAN_WILSON,
                        'stats': '7-3-0',
                    },
                ],
                'winner': {
                    'fighter': OSKAR_PIECHOTA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:24',
                'odds': {
                    OSKAR_PIECHOTA: 1.44,
                    JONATHAN_WILSON: 2.75,
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
                        'name': JAN_BLACHOWICZ,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': JAN_BLACHOWICZ,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:02',
                },
                'time': '15:50',
                'odds': {
                    JAN_BLACHOWICZ: 2.22,
                    DEVIN_CLARK: 1.65,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JODIE_ESQUIBEL,
                        'stats': '6-4-0',
                    },
                    {
                        'name': KAROLINA_KOWALKIEWICZ,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': KAROLINA_KOWALKIEWICZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:21',
                'odds': {
                    KAROLINA_KOWALKIEWICZ: 1.15,
                    JODIE_ESQUIBEL: 5.25,
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
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_TILL,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:20',
                },
                'time': '16:50',
                'odds': {
                    DARREN_TILL: 2.20,
                    DONALD_CERRONE: 1.66,
                },
            },
        ]
    },

    {
        'date': '2017-10-28',
        'name': 'UFC Fight Night: Brunson vs Machida',
        'location': 'Sao Paulo, Brazil',
        'venue': 'Ginasio do Ibirpuera',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCELO_GOLM,
                        'stats': '6-2-0',
                    },
                    {
                        'name': CHRISTIAN_COLOMBO,
                        'stats': '8-3-1',
                    },
                ],
                'winner': {
                    'fighter': MARCELO_GOLM,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:08',
                },
                'time': '19:00',
                'odds': {
                    MARCELO_GOLM: 1.37,
                    CHRISTIAN_COLOMBO: 3.10,
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
                        'name': JARRED_BROOKS,
                        'stats': '14-2-0',
                    },
                ],
                'winner': {
                    'fighter': DEIVESON_FIGUEIREDO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    DEIVESON_FIGUEIREDO: 2.20,
                    JARRED_BROOKS: 1.65,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MAX_GRIFFIN,
                        'stats': '14-6-0',
                    },
                    {
                        'name': ELIZEU_DOS_SANTOS,
                        'stats': '20-5-0',
                    },
                ],
                'winner': {
                    'fighter': ELIZEU_DOS_SANTOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    ELIZEU_DOS_SANTOS: 1.43,
                    MAX_GRIFFIN: 2.85,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JARED_GORDON,
                        'stats': '14-3-0',
                    },
                    {
                        'name': HACRAN_DIAS,
                        'stats': '23-6-1',
                    },
                ],
                'winner': {
                    'fighter': JARED_GORDON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    JARED_GORDON: 1.61,
                    HACRAN_DIAS: 2.25,
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
                        'name': ANTONIO_CARLOS_JUNIOR,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': ANTONIO_CARLOS_JUNIOR,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:30',
                },
                'time': '21:00',
                'odds': {
                    ANTONIO_CARLOS_JUNIOR: 1.22,
                    JACK_MARSHMAN: 4.25,
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
                        'name': VICENTE_LUQUE,
                        'stats': '15-6-1',
                    },
                ],
                'winner': {
                    'fighter': VICENTE_LUQUE,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:08',
                },
                'time': '21:30',
                'odds': {
                    VICENTE_LUQUE: 1.74,
                    NIKO_PRICE: 2.05,
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
                        'name': JOHN_LINEKER,
                        'stats': '31-8-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_LINEKER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    JOHN_LINEKER: 1.18,
                    MARLON_VERA: 4.75,
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
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:59',
                },
                'time': '22:30',
                'odds': {
                    THIAGO_SANTOS: 1.87,
                    JACK_HERMANSSON: 1.83,
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
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCISCO_TRINALDO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    FRANCISCO_TRINALDO: 1.44,
                    JIM_MILLER: 2.70,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ROB_FONT,
                        'stats': '16-4-0',
                    },
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                ],
                'winner': {
                    'fighter': PEDRO_MUNHOZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:03',
                },
                'time': '23:30',
                'odds': {
                    PEDRO_MUNHOZ: 2.35,
                    ROB_FONT: 1.54,
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
                        'name': DEMIAN_MAIA,
                        'stats': '26-9-0',
                    },
                ],
                'winner': {
                    'fighter': COLBY_COVINGTON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:50',
                'odds': {
                    COLBY_COVINGTON: 1.93,
                    DEMIAN_MAIA: 1.80,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': LYOTO_MACHIDA,
                        'stats': '24-8-0',
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
                    'time': '2:30',
                },
                'time': '23:59',
                'odds': {
                    DEREK_BRUNSON: 1.63,
                    LYOTO_MACHIDA: 2.25,
                },
            },
        ]
    },

    {
        'date': '2017-11-04',
        'name': 'UFC 217: Bisping vs St-Pierre',
        'location': 'New York City, New York',
        'venue': 'Madison Square Garden',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RICARDO_RAMOS,
                        'stats': '12-1-0',
                    },
                    {
                        'name': AIEMANN_ZAHABI,
                        'stats': '7-1-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_RAMOS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:58',
                },
                'time': '19:00',
                'odds': {
                    RICARDO_RAMOS: 1.49,
                    AIEMANN_ZAHABI: 2.60,
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
                        'name': ALEKSEI_OLEINIK,
                        'stats': '57-11-1',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_BLAYDES,
                    'by': 'tko',
                    'round': 2,
                    'time': '1:56',
                },
                'time': '19:30',
                'odds': {
                    CURTIS_BLAYDES: 1.30,
                    ALEKSEI_OLEINIK: 3.45,
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
                        'name': RANDY_BROWN,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': RANDY_BROWN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    RANDY_BROWN: 1.96,
                    MICKEY_GALL: 1.77,
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
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '57-11-1',
                    },
                ],
                'winner': {
                    'fighter': OVINCE_SAINT_PREUX,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:25',
                },
                'time': '20:30',
                'odds': {
                    OVINCE_SAINT_PREUX: 1.54,
                    COREY_ANDERSON: 2.40,
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
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': MARK_GODBEER,
                    'by': 'dq',
                    'round': 1,
                    'time': '4:29',
                },
                'time': '21:00',
                'odds': {
                    MARK_GODBEER: 3.85,
                    WALT_HARRIS: 1.25,
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
                        'name': JAMES_VICK,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': JAMES_VICK,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:59',
                },
                'time': '21:30',
                'odds': {
                    JAMES_VICK: 2.33,
                    JOE_DUFFY: 1.58,
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
                        'name': JOHNY_HENDRICKS,
                        'stats': '18-8-0',
                    },
                ],
                'winner': {
                    'fighter': PAULO_COSTA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:23',
                },
                'time': '22:00',
                'odds': {
                    PAULO_COSTA: 1.27,
                    JOHNY_HENDRICKS: 3.85,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': STEPHEN_THOMPSON,
                        'stats': '14-4-1',
                    },
                    {
                        'name': JORGE_MASVIDAL,
                        'stats': '33-13-0',
                    },
                ],
                'winner': {
                    'fighter': STEPHEN_THOMPSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    STEPHEN_THOMPSON: 1.50,
                    JORGE_MASVIDAL: 2.55,
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
                        'name': JOANNA_JEDRZEJCZYK,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': ROSE_NAMAJUNAS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:03',
                },
                'time': '23:00',
                'odds': {
                    ROSE_NAMAJUNAS: 5.50,
                    JOANNA_JEDRZEJCZYK: 1.12,
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
                    'round': 2,
                    'time': '2:41',
                },
                'time': '23:30',
                'odds': {
                    TJ_DILLASHAW: 2.75,
                    CODY_GARBRANDT: 1.43,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': GEORGES_ST_PIERRE,
                        'stats': '26-2-0',
                    },
                    {
                        'name': MICHAEL_BISPING,
                        'stats': '31-9-0',
                    },
                ],
                'winner': {
                    'fighter': GEORGES_ST_PIERRE,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:23',
                },
                'time': '23:59',
                'odds': {
                    GEORGES_ST_PIERRE: 1.95,
                    MICHAEL_BISPING: 1.80,
                },
            },
        ]
    },

    {
        'date': '2017-11-11',
        'name': 'UFC Fight Night: Poirier vs Pettis',
        'location': 'Norfolk, Virginia',
        'venue': 'Ted Constant Convocation Center',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KARL_ROBERSON,
                        'stats': '7-2-0',
                    },
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': KARL_ROBERSON,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:41',
                },
                'time': '18:30',
                'odds': {
                    KARL_ROBERSON: 1.42,
                    DARREN_STEWART: 2.80,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCEL_FORTUNA,
                        'stats': '9-3-0',
                    },
                    {
                        'name': JAKE_COLLIER,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': JAKE_COLLIER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    JAKE_COLLIER: 2.95,
                    MARCEL_FORTUNA: 1.35,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SEAN_STRICKLAND,
                        'stats': '20-3-0',
                    },
                    {
                        'name': COURT_MCGEE,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': SEAN_STRICKLAND,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    SEAN_STRICKLAND: 1.31,
                    COURT_MCGEE: 3.25,
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
                'time': '20:00',
                'odds': {
                    NINA_ANSAROFF: 2.35,
                    ANGELA_HILL: 1.56,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MICHEL_QUINONES,
                        'stats': '8-3-0',
                    },
                    {
                        'name': SAGE_NORTHCUTT,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': SAGE_NORTHCUTT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    SAGE_NORTHCUTT: 1.49,
                    MICHEL_QUINONES: 2.51,
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
                'time': '21:00',
                'odds': {
                    TATIANA_SUAREZ: 1.32,
                    VIVIANE_PEREIRA: 3.15,
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
                        'name': JOHN_DODSON,
                        'stats': '21-11-0',
                    },
                ],
                'winner': {
                    'fighter': MARLON_MORAES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    MARLON_MORAES: 1.93,
                    JOHN_DODSON: 1.74,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOE_LAUZON,
                        'stats': '27-16-0',
                    },
                    {
                        'name': CLAY_GUIDA,
                        'stats': '34-15-0',
                    },
                ],
                'winner': {
                    'fighter': CLAY_GUIDA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:07',
                },
                'time': '22:00',
                'odds': {
                    CLAY_GUIDA: 1.76,
                    JOE_LAUZON: 2.00,
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
                        'name': RAPHAEL_ASSUNCAO,
                        'stats': '27-6-0',
                    },
                ],
                'winner': {
                    'fighter': RAPHAEL_ASSUNCAO,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:50',
                },
                'time': '22:30',
                'odds': {
                    RAPHAEL_ASSUNCAO: 1.27,
                    MATTHEW_LOPEZ: 3.70,
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
                        'name': CEZAR_FERREIRA,
                        'stats': '14-7-0',
                    },
                ],
                'winner': {
                    'fighter': CEZAR_FERREIRA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    CEZAR_FERREIRA: 1.37,
                    NATE_MARQUARDT: 3.00,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUNIOR_ALBINI,
                        'stats': '14-5-0',
                    },
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                ],
                'winner': {
                    'fighter': ANDREI_ARLOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    ANDREI_ARLOVSKI: 3.65,
                    JUNIOR_ALBINI: 1.29,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DIEGO_SANCHEZ,
                        'stats': '31-11-0',
                    },
                    {
                        'name': MATT_BROWN,
                        'stats': '23-16-0',
                    },
                ],
                'winner': {
                    'fighter': MATT_BROWN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:44',
                },
                'time': '23:59',
                'odds': {
                    MATT_BROWN: 1.26,
                    DIEGO_SANCHEZ: 3.70,
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
                        'name': ANTHONY_PETTIS,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_POIRIER,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:08',
                },
                'time': '23:59',
                'odds': {
                    DUSTIN_POIRIER: 1.87,
                    ANTHONY_PETTIS: 1.85,
                },
            },
        ]
    },

    {
        'date': '2017-11-18',
        'name': 'UFC Fight Night: Werdum vs Tybura',
        'location': 'Sydney, Australia',
        'venue': 'Qudos Bank Arena',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ADAM_WIECZOREK,
                        'stats': '10-2-0',
                    },
                    {
                        'name': ANTHONY_HAMILTON,
                        'stats': '15-9-0',
                    },
                ],
                'winner': {
                    'fighter': ADAM_WIECZOREK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:40',
                'odds': {
                    ADAM_WIECZOREK: 1.53,
                    ANTHONY_HAMILTON: 2.46,
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
                        'name': JENEL_LAUSA,
                        'stats': '7-5-0',
                    },
                ],
                'winner': {
                    'fighter': ERIC_SHELTON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:08',
                'odds': {
                    ERIC_SHELTON: 1.28,
                    JENEL_LAUSA: 3.60,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': NADIA_KASSEM,
                        'stats': '5-1-0',
                    },
                    {
                        'name': ALEX_CHAMBERS,
                        'stats': '5-4-0',
                    },
                ],
                'winner': {
                    'fighter': NADIA_KASSEM,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    NADIA_KASSEM: 1.49,
                    ALEX_CHAMBERS: 2.60,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FRANK_CAMACHO,
                        'stats': '21-7-0',
                    },
                    {
                        'name': DAMIEN_BROWN,
                        'stats': '17-12-0',
                    },
                ],
                'winner': {
                    'fighter': FRANK_CAMACHO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    FRANK_CAMACHO: 1.71,
                    DAMIEN_BROWN: 2.04,
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
                        'name': RASHAD_COULTER,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': TAI_TUIVASA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:35',
                },
                'time': '20:30',
                'odds': {
                    TAI_TUIVASA: 1.51,
                    RASHAD_COULTER: 2.47,
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
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                ],
                'winner': {
                    'fighter': NIK_LENTZ,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:05',
                },
                'time': '21:00',
                'odds': {
                    NIK_LENTZ: 4.05,
                    WILL_BROOKS: 1.22,
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
                        'name': RYAN_BENOIT,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_BENOIT,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:38',
                },
                'time': '21:30',
                'odds': {
                    RYAN_BENOIT: 1.29,
                    ASHKAN_MOKHTARIAN: 3.25,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHANE_YOUNG,
                        'stats': '12-4-0',
                    },
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
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
                    ALEXANDER_VOLKANOVSKI: 1.15,
                    SHANE_YOUNG: 5.25,
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
                        'name': ELIAS_THEODOROU,
                        'stats': '17-2-0',
                    },
                ],
                'winner': {
                    'fighter': ELIAS_THEODOROU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ELIAS_THEODOROU: 1.29,
                    DANIEL_KELLY: 3.40,
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
                        'name': JAKE_MATTHEWS,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': JAKE_MATTHEWS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:15',
                'odds': {
                    JAKE_MATTHEWS: 1.69,
                    BOJAN_VELICKOVIC: 2.15,
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
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                ],
                'winner': {
                    'fighter': BELAL_MUHAMMAD,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    BELAL_MUHAMMAD: 2.70,
                    TIM_MEANS: 1.42,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JESSICA_ROSE_CLARK,
                        'stats': '9-5-0',
                    },
                    {
                        'name': BEC_RAWLINGS,
                        'stats': '7-8-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ROSE_CLARK,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:45',
                'odds': {
                    JESSICA_ROSE_CLARK: 1.95,
                    BEC_RAWLINGS: 1.74,
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
                        'name': FABRICIO_WERDUM,
                        'stats': '23-8-1',
                    },
                ],
                'winner': {
                    'fighter': FABRICIO_WERDUM,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    FABRICIO_WERDUM: 1.30,
                    MARCIN_TYBURA: 3.45,
                },
            },
        ]
    },

    {
        'date': '2017-11-25',
        'name': 'UFC Fight Night: Bisping vs Gastelum',
        'location': 'Shanghai, China',
        'venue': 'Mercedes-Benz Arena',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': HU_YAOZONG,
                        'stats': '3-2-0',
                    },
                    {
                        'name': CYRIL_ASKER,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': CYRIL_ASKER,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:33',
                },
                'time': '3:45',
                'odds': {
                    CYRIL_ASKER: 1.38,
                    HU_YAOZONG: 2.93,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': WULIJI_BUREN,
                        'stats': '10-7-0',
                    },
                    {
                        'name': ROLANDO_DY,
                        'stats': '9-7-1',
                    },
                ],
                'winner': {
                    'fighter': ROLANDO_DY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '4:00',
                'odds': {
                    ROLANDO_DY: 1.61,
                    WULIJI_BUREN: 2.30,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': WU_YANAN,
                        'stats': '10-2-0',
                    },
                    {
                        'name': GINA_MAZANY,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': GINA_MAZANY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '4:15',
                'odds': {
                    GINA_MAZANY: 1.65,
                    WU_YANAN: 1.69,
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
                        'name': SHAMIL_ABDURAKHIMOV,
                        'stats': '19-4-0',
                    },
                ],
                'winner': {
                    'fighter': SHAMIL_ABDURAKHIMOV,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:24',
                },
                'time': '4:30',
                'odds': {
                    SHAMIL_ABDURAKHIMOV: 1.67,
                    CHASE_SHERMAN: 2.10,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SONG_YADONG,
                        'stats': '13-3-0',
                    },
                    {
                        'name': BHARAT_KANDARE,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': SONG_YADONG,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:16',
                },
                'time': '4:45',
                'odds': {
                    SONG_YADONG: 1.56,
                    BHARAT_KANDARE: 2.15,
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
                        'name': KAILIN_CURRAN,
                        'stats': '4-6-0',
                    },
                ],
                'winner': {
                    'fighter': YAN_XIAONAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '5:30',
                'odds': {
                    YAN_XIAONAN: 1.65,
                    KAILIN_CURRAN: 2.15,
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
                        'name': BOBBY_NASH,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': SONG_KENAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:15',
                },
                'time': '6:00',
                'odds': {
                    SONG_KENAN: 3.30,
                    BOBBY_NASH: 1.30,
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
                        'name': ZABIT_MAGOMEDSHARIPOV,
                        'stats': '17-1-0',
                    },
                ],
                'winner': {
                    'fighter': ZABIT_MAGOMEDSHARIPOV,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:30',
                },
                'time': '6:30',
                'odds': {
                    ZABIT_MAGOMEDSHARIPOV: 1.19,
                    SHEYMON_DA_SILVA_MORAES: 4.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MUSLIM_SALIKHOV,
                        'stats': '14-2-0',
                    },
                    {
                        'name': ALEX_GARCIA,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_GARCIA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:22',
                },
                'time': '7:00',
                'odds': {
                    ALEX_GARCIA: 2.75,
                    MUSLIM_SALIKHOV: 1.43,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': WANG_GUAN,
                        'stats': '20-1-1',
                    },
                    {
                        'name': ALEX_CACERES,
                        'stats': '14-12-0',
                    },
                ],
                'winner': {
                    'fighter': WANG_GUAN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '7:30',
                'odds': {
                    WANG_GUAN: 2.10,
                    ALEX_CACERES: 1.65,
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
                        'name': LI_JINGLIANG,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': LI_JINGLIANG,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:57',
                },
                'time': '8:00',
                'odds': {
                    LI_JINGLIANG: 1.47,
                    ZAK_OTTOW: 2.50,
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
                        'name': MICHAEL_BISPING,
                        'stats': '31-9-0',
                    },
                ],
                'winner': {
                    'fighter': KELVIN_GASTELUM,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:30',
                },
                'time': '8:30',
                'odds': {
                    KELVIN_GASTELUM: 1.32,
                    MICHAEL_BISPING: 3.25,
                },
            },
        ]
    },

    {
        'date': '2017-12-01',
        'name': 'The Ultimate Fighter 26 Finale',
        'location': 'Las Vegas, Nevada',
        'venue': 'Park Theatre',
        'fights': [
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': EMILY_WHITMIRE,
                        'stats': '4-2-0',
                    },
                    {
                        'name': GILLIAN_ROBERTSON,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': GILLIAN_ROBERTSON,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:12',
                },
                'time': '19:30',
                'odds': {
                    GILLIAN_ROBERTSON: 2.55,
                    EMILY_WHITMIRE: 1.50,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SHANA_DOBSON,
                        'stats': '3-2-0',
                    },
                    {
                        'name': ARIEL_BECK,
                        'stats': '4-5-0',
                    },
                ],
                'winner': {
                    'fighter': SHANA_DOBSON,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:53',
                },
                'time': '20:00',
                'odds': {
                    SHANA_DOBSON: 1.44,
                    ARIEL_BECK: 2.58,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': RACHAEL_OSTOVICH,
                        'stats': '4-5-0',
                    },
                    {
                        'name': KARINE_GEVORGYAN,
                        'stats': '3-3-0',
                    },
                ],
                'winner': {
                    'fighter': RACHAEL_OSTOVICH,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:40',
                },
                'time': '20:30',
                'odds': {
                    RACHAEL_OSTOVICH: 1.22,
                    KARINE_GEVORGYAN: 3.85,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_JANES,
                        'stats': '10-3-0',
                    },
                    {
                        'name': ANDREW_SANCHEZ,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_JANES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:58',
                },
                'time': '21:00',
                'odds': {
                    RYAN_JANES: 5.00,
                    ANDREW_SANCHEZ: 1.14,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MONTANA_DE_LA_ROSA,
                        'stats': '10-4-0',
                    },
                    {
                        'name': CHRISTINA_MARKS,
                        'stats': '8-9-0',
                    },
                ],
                'winner': {
                    'fighter': MONTANA_DE_LA_ROSA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:00',
                },
                'time': '21:30',
                'odds': {
                    MONTANA_DE_LA_ROSA: 1.24,
                    CHRISTINA_MARKS: 3.70,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRETT_JOHNS,
                        'stats': '15-2-0',
                    },
                    {
                        'name': JOE_SOTO,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': BRETT_JOHNS,
                    'by': 'submission',
                    'round': 1,
                    'time': '0:30',
                },
                'time': '22:00',
                'odds': {
                    BRETT_JOHNS: 1.54,
                    JOE_SOTO: 2.40,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MELINDA_FABIAN,
                        'stats': '4-4-2',
                    },
                    {
                        'name': DEANNA_BENNETT,
                        'stats': '8-3-1',
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
                    DEANNA_BENNETT: 1.18,
                    MELINDA_FABIAN: 4.50,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': GERALD_MEERSCHAERT,
                        'stats': '28-11-0',
                    },
                    {
                        'name': ERIC_SPICELY,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': GERALD_MEERSCHAERT,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:18',
                },
                'time': '23:00',
                'odds': {
                    GERALD_MEERSCHAERT: 1.53,
                    ERIC_SPICELY: 2.35,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': BARB_HONCHAK,
                        'stats': '0-0-0',
                    },
                    {
                        'name': LAUREN_MURPHY,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': LAUREN_MURPHY,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    LAUREN_MURPHY: 2.90,
                    BARB_HONCHAK: 1.40,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': SEAN_O_MALLEY,
                        'stats': '10-0-0',
                    },
                    {
                        'name': TERRION_WARE,
                        'stats': '17-8-0',
                    },
                ],
                'winner': {
                    'fighter': SEAN_O_MALLEY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    SEAN_O_MALLEY: 1.39,
                    TERRION_WARE: 2.95,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': NICCO_MONTANO,
                        'stats': '5-2-0',
                    },
                    {
                        'name': ROXANNE_MODAFFERI,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': NICCO_MONTANO,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:55',
                'odds': {
                    NICCO_MONTANO: 1.44,
                    ROXANNE_MODAFFERI: 2.60,
                },
            },
        ]
    },

    {
        'date': '2017-12-02',
        'name': 'UFC 218: Holloway vs Aldo 2',
        'location': 'Detroit, Michigan',
        'venue': 'Little Caesars Arena',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALLEN_CROWDER,
                        'stats': '10-3-0',
                    },
                    {
                        'name': JUSTIN_WILLIS,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_WILLIS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:33',
                },
                'time': '18:15',
                'odds': {
                    JUSTIN_WILLIS: 1.43,
                    ALLEN_CROWDER: 2.75,
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
                        'name': JEREMY_KIMBALL,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': DOMINICK_REYES,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:39',
                },
                'time': '18:45',
                'odds': {
                    DOMINICK_REYES: 1.19,
                    JEREMY_KIMBALL: 4.50,
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
                        'name': SABAH_HOMASI,
                        'stats': '11-8-0',
                    },
                ],
                'winner': {
                    'fighter': ABDUL_RAZAK_ALHASSAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:21',
                },
                'time': '19:15',
                'odds': {
                    ABDUL_RAZAK_ALHASSAN: 1.34,
                    SABAH_HOMASI: 3.25,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': AMANDA_COOPER,
                        'stats': '4-5-0',
                    },
                    {
                        'name': ANGELA_MAGANA,
                        'stats': '11-9-0',
                    },
                ],
                'winner': {
                    'fighter': AMANDA_COOPER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:34',
                },
                'time': '19:45',
                'odds': {
                    AMANDA_COOPER: 1.20,
                    ANGELA_MAGANA: 4.50,
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
                        'name': FELICE_HERRIG,
                        'stats': '14-8-0',
                    },
                ],
                'winner': {
                    'fighter': FELICE_HERRIG,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    FELICE_HERRIG: 1.77,
                    CORTNEY_CASEY_SANCHEZ: 1.94,
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
                'time': '20:30',
                'odds': {
                    DAVID_TEYMUR: 1.69,
                    DRAKKAR_KLOSE: 2.05,
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
                        'name': YANCY_MEDEIROS,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': YANCY_MEDEIROS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:02',
                },
                'time': '21:00',
                'odds': {
                    YANCY_MEDEIROS: 3.65,
                    ALEX_OLIVEIRA: 1.25,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': PAUL_FELDER,
                        'stats': '16-4-0',
                    },
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                ],
                'winner': {
                    'fighter': PAUL_FELDER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:06',
                },
                'time': '21:30',
                'odds': {
                    PAUL_FELDER: 2.10,
                    CHARLES_OLIVEIRA: 1.64,
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
                        'name': MICHELLE_WATERSON,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': TECIA_TORRES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    TECIA_TORRES: 1.42,
                    MICHELLE_WATERSON: 2.90,
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
                        'name': EDDIE_ALVAREZ,
                        'stats': '29-6-0',
                    },
                ],
                'winner': {
                    'fighter': EDDIE_ALVAREZ,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:59',
                },
                'time': '22:30',
                'odds': {
                    EDDIE_ALVAREZ: 2.50,
                    JUSTIN_GAETHJE: 1.53,
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
                        'name': SERGIO_PETTIS,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': HENRY_CEJUDO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    HENRY_CEJUDO: 1.29,
                    SERGIO_PETTIS: 3.45,
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
                        'name': ALISTAIR_OVEREEM,
                        'stats': '44-17-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCIS_NGANNOU,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:42',
                },
                'time': '23:30',
                'odds': {
                    FRANCIS_NGANNOU: 1.43,
                    ALISTAIR_OVEREEM: 2.74,
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
                    'time': '4:51',
                },
                'time': '23:59',
                'odds': {
                    MAX_HOLLOWAY: 1.35,
                    JOSE_ALDO: 3.20,
                },
            },
        ]
    },

    {
        'date': '2017-12-09',
        'name': 'UFC Fight Night: Swanson vs Ortega',
        'location': 'Fresno, California',
        'venue': 'Save Mart Center',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TREVIN_GILES,
                        'stats': '11-0-0',
                    },
                    {
                        'name': ANTONIO_BRAGA_NETO,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': TREVIN_GILES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:27',
                },
                'time': '18:30',
                'odds': {
                    TREVIN_GILES: 1.35,
                    ANTONIO_BRAGA_NETO: 3.20,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAVI_RAMOS,
                        'stats': '9-2-0',
                    },
                    {
                        'name': CHRIS_GRUETZEMACHER,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': DAVI_RAMOS,
                    'by': 'submission',
                    'round': 3,
                    'time': '0:50',
                },
                'time': '19:00',
                'odds': {
                    DAVI_RAMOS: 1.22,
                    CHRIS_GRUETZEMACHER: 4.20,
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
                        'name': IURI_ALCANTARA,
                        'stats': '35-10-0',
                    },
                ],
                'winner': {
                    'fighter': ALEJANDRO_PEREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ALEJANDRO_PEREZ: 2.45,
                    IURI_ALCANTARA: 1.54,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MERAB_DVALISHVILI,
                        'stats': '8-4-0',
                    },
                    {
                        'name': FRANKIE_SAENZ,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': FRANKIE_SAENZ,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    FRANKIE_SAENZ: 2.60,
                    MERAB_DVALISHVILI: 1.48,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_PEREZ,
                        'stats': '22-5-0',
                    },
                    {
                        'name': CARLS_JOHN_DE_TOMAS,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_PEREZ,
                    'by': 'u.dec',
                    'round': 2,
                    'time': '1:54',
                },
                'time': '20:30',
                'odds': {
                    ALEX_PEREZ: 1.22,
                    CARLS_JOHN_DE_TOMAS: 4.20,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_SOUKHAMTHATH,
                        'stats': '13-6-0',
                    },
                    {
                        'name': LUKE_SANDERS,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_SOUKHAMTHATH,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:06',
                },
                'time': '21:00',
                'odds': {
                    ANDRE_SOUKHAMTHATH: 3.65,
                    LUKE_SANDERS: 1.29,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXIS_DAVIS,
                        'stats': '19-9-0',
                    },
                    {
                        'name': LIZ_CARMOUCHE,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXIS_DAVIS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    ALEXIS_DAVIS: 2.06,
                    LIZ_CARMOUCHE: 1.69,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BENITO_LOPEZ,
                        'stats': '9-1-0',
                    },
                    {
                        'name': ALBERT_MORALES,
                        'stats': '7-4-1',
                    },
                ],
                'winner': {
                    'fighter': BENITO_LOPEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    BENITO_LOPEZ: 1.74,
                    ALBERT_MORALES: 1.99,
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
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': ERYK_ANDERS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ERYK_ANDERS: 1.22,
                    MARKUS_PEREZ: 4.25,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DARRELL_HORCHER,
                        'stats': '13-4-0',
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
                'time': '23:00',
                'odds': {
                    SCOTT_HOLTZMAN: 1.65,
                    DARRELL_HORCHER: 2.25,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARLON_MORAES,
                        'stats': '2-5-1',
                    },
                    {
                        'name': ALJAMAIN_STERLING,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': MARLON_MORAES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:07',
                },
                'time': '23:30',
                'odds': {
                    MARLON_MORAES: 1.60,
                    ALJAMAIN_STERLING: 2.20,
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
                        'name': GABRIEL_BENITEZ,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': GABRIEL_BENITEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    GABRIEL_BENITEZ: 3.48,
                    JASON_KNIGHT: 1.29,
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
                        'name': CUB_SWANSON,
                        'stats': '25-10-0',
                    },
                ],
                'winner': {
                    'fighter': BRIAN_ORTEGA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:22',
                },
                'time': '23:59',
                'odds': {
                    BRIAN_ORTEGA: 1.87,
                    CUB_SWANSON: 1.87,
                },
            },
        ]
    },

    {
        'date': '2017-12-16',
        'name': 'UFC Fight Night: Lawler vs Dos Anjos',
        'location': 'Winnipeg, Manitoba',
        'venue': 'Bell, MTS Place',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ERICK_SILVA,
                        'stats': '19-9-0',
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
                'time': '16:30',
                'odds': {
                    JORDAN_MEIN: 1.59,
                    ERICK_SILVA: 2.26,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ALESSIO_DI_CHRICO,
                        'stats': '12-2-0',
                    },
                    {
                        'name': OLUWALE_BAMGBOSE,
                        'stats': '6-4-0',
                    },
                ],
                'winner': {
                    'fighter': ALESSIO_DI_CHRICO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:14',
                },
                'time': '17:00',
                'odds': {
                    ALESSIO_DI_CHRICO: 1.63,
                    OLUWALE_BAMGBOSE: 2.13,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ABEL_TRUJILLO,
                        'stats': '15-8-0',
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
                'time': '17:50',
                'odds': {
                    JOHN_MAKDESSI: 2.25,
                    ABEL_TRUJILLO: 1.63,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                    {
                        'name': NORDINE_TALEB,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': NORDINE_TALEB,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:59',
                },
                'time': '18:10',
                'odds': {
                    NORDINE_TALEB: 1.61,
                    DANNY_ROBERTS: 2.25,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GALORE_BOFANDO,
                        'stats': '5-3-0',
                    },
                    {
                        'name': CHAD_LAPRISE,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': CHAD_LAPRISE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:10',
                },
                'time': '18:35',
                'odds': {
                    CHAD_LAPRISE: 1.67,
                    GALORE_BOFANDO: 2.15,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JULIAN_MARQUEZ,
                        'stats': '7-2-0',
                    },
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': JULIAN_MARQUEZ,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:42',
                },
                'time': '19:00',
                'odds': {
                    JULIAN_MARQUEZ: 1.28,
                    DARREN_STEWART: 3.70,
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
                        'name': JAN_BLACHOWICZ,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': JAN_BLACHOWICZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    JAN_BLACHOWICZ: 2.58,
                    JARED_CANNONIER: 1.50,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MISHA_CIRKUNOV,
                        'stats': '14-5-0',
                    },
                    {
                        'name': GLOVER_TEIXEIRA,
                        'stats': '28-7-0',
                    },
                ],
                'winner': {
                    'fighter': GLOVER_TEIXEIRA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:45',
                },
                'time': '20:00',
                'odds': {
                    GLOVER_TEIXEIRA: 2.30,
                    MISHA_CIRKUNOV: 1.63,
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
                'time': '20:30',
                'odds': {
                    SANTIAGO_PONZINIBBIO: 1.60,
                    MIKE_PERRY: 2.35,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JOSH_EMMETT,
                        'stats': '14-2-0',
                    },
                    {
                        'name': RICARDO_LAMAS,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': JOSH_EMMETT,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:33',
                },
                'time': '21:00',
                'odds': {
                    JOSH_EMMETT: 3.19,
                    RICARDO_LAMAS: 1.33,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ROBBIE_LAWLER,
                        'stats': '28-13-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': RAFAEL_DOS_ANJOS,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    RAFAEL_DOS_ANJOS: 1.76,
                    ROBBIE_LAWLER: 1.91,
                },
            },
        ]
    },

    {
        'date': '2017-12-30',
        'name': 'UFC 219: Cyborg vs Holm',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARK_DE_LA_ROSA,
                        'stats': '11-2-0',
                    },
                    {
                        'name': TIM_ELLIOTT,
                        'stats': '16-8-1',
                    },
                ],
                'winner': {
                    'fighter': TIM_ELLIOTT,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:41',
                },
                'time': '19:30',
                'odds': {
                    TIM_ELLIOTT: 1.50,
                    MARK_DE_LA_ROSA: 2.57,
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
                        'name': LOUIS_SMOLKA,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': MATHEUS_NICOLAU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    MATHEUS_NICOLAU: 1.44,
                    LOUIS_SMOLKA: 2.70,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': MARVIN_VETTORI,
                        'stats': '12-4-1',
                    },
                    {
                        'name': OMARI_AKHMEDOV,
                        'stats': '18-4-1',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    OMARI_AKHMEDOV: 3.10,
                    MARVIN_VETTORI: 1.33,
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
                        'name': MYLES_JURY,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': MYLES_JURY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    MYLES_JURY: 1.49,
                    RICK_GLENN: 2.40,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MICHAL_OLEKSIEJCZUK,
                        'stats': '13-2-0',
                    },
                    {
                        'name': KHALIL_ROUNTREE,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAL_OLEKSIEJCZUK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    MICHAL_OLEKSIEJCZUK: 3.85,
                    KHALIL_ROUNTREE: 1.25,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NEIL_MAGNY,
                        'stats': '21-8-0',
                    },
                    {
                        'name': CARLOS_CONDIT,
                        'stats': '30-13-0',
                    },
                ],
                'winner': {
                    'fighter': NEIL_MAGNY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    NEIL_MAGNY: 2.05,
                    CARLOS_CONDIT: 1.74,
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
                        'name': CARLA_ESPARZA,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': CARLA_ESPARZA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    CARLA_ESPARZA: 2.70,
                    CYNTHIA_CALVILLO: 1.44,
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
                        'name': DAN_HOOKER,
                        'stats': '18-8-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_HOOKER,
                    'by': 'submission',
                    'round': 3,
                    'time': '0:42',
                },
                'time': '23:00',
                'odds': {
                    DAN_HOOKER: 2.50,
                    MARC_DIAKIESE: 1.53,
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
                        'name': EDSON_BARBOZA,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': KHABIB_NURMAGOMEDIV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    KHABIB_NURMAGOMEDIV: 1.26,
                    EDSON_BARBOZA: 3.90,
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
                        'name': CRIS_CYBORG,
                        'stats': '20-2-0',
                    },
                ],
                'winner': {
                    'fighter': CRIS_CYBORG,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    CRIS_CYBORG: 1.31,
                    HOLLY_HOLM: 3.40,
                },
            },
        ]
    }
]
