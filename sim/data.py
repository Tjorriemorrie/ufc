from .fighters import *

# acc   roi   profit  desc
# 70.7  22.7  741     added learning rate and gamma
# 68.0  12.5  408     optimized bets                        (1, 237), (4, 54), (3, 43), (2, 35)
# 68.0  10.0  438     splitted hyper and bet params         (1, 154), (4, 108), (3, 73), (2, 34)
# 69.4  21.2  927     2019-08-11 UFC Fight Night: Shevchenko vs Carmouche (1, 154), (4, 108)
# 69.1  20.6  897     optimized                             (1, 154), (4, 108), (3, 73), (2, 34)
# 67.4  17.4  770     reverted back to 3 params             (1, 138), (4, 103), (3, 81), (2, 46)
# 67.4  17.5  801     added exponential param                (1, 138), (4, 125), (3, 65), (2, 40)
# 67.4  16.5  524     added odds diff
# 65.8  10.1  285     removed redundant gradients!               (2, 196), (1, 172)
# 64.1  46.9  2891    multi changed to 4                         (5, 206), (1, 141)
# 64.1  54.1  6186    bet gradients not to be combined           [(11, 155), (1, 141), (5, 10), (10, 10)]
# 65.8  54.1  6716    estimators capped to 500
# 64.7  55    7013    added max depth (optimized)
# 67    12.09 415     removed max bet of 10 (no diff)
# 67    12.09 415     fixed cutoff with all_data :(

# 59    7.87  709     add estimators number as parameter (1, 707), (2, 78), (3, 70), (4, 44), (5, 36), (6, 18), (7, 16), (8, 8), (9, 4), (11, 3)
# 60    3.11  596     2x3    reduced pred (bad?) and added prob scaling (4, 262), (3, 258), (5, 183)
# 55    1.3   101     ufc 240
# 65    13.1          bet multi for LOWER pred
# 65    1.55          bet unit fixed at 5

# 63    7.44          <- scaling bets on diff?
# 67    1.08          <- xgb1k
# 64    0.66
# 63    -0.48

# 59    -1.16
# 92    6.49
# 88    5.37          <- 1000 estimators


DATA = [
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
                    CHANCE_RENCOUNTRE: 2.35,
                    KYLE_STEWART: 1.58,
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
                    GEOFF_NEAL: 1.48,
                    BELAL_MUHAMMAD: 2.70,
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
                    DENNIS_BERMUDEZ: 1.93,
                    TE_EDWARDS: 1.74,
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
                    CORY_SANDHAGEN: 1.16,
                    MARIO_BAUTISTA: 4.75,
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
                    JOANNE_CALDERWOOD: 2.95,
                    ARIANE_LIPSKI: 1.38,
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
                    DONALD_CERRONE: 2.70,
                    ALEXANDER_HERNANDEZ: 1.44,
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
                    GLOVER_TEIXEIRA: 1.87,
                    KARL_ROBERSON: 1.86,
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
                    PAIGE_VANZANT: 1.53,
                    RACHAEL_OSTOVICH: 2.50,
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
                    JOSEPH_BENAVIDEZ: 1.43,
                    DUSTIN_ORTIZ: 2.80,
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
                    GREGOR_GILLESPIE: 1.18,
                    YANCY_MEDEIROS: 4.75,
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
                    GREG_HARDY: 1.18,
                    ALLEN_CROWDER: 4.70,
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
                'odds': {
                    HENRY_CEJUDO: 2.95,
                    TJ_DILLASHAW: 1.38
                }
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
                    ROGERIO_BONTORIN: 3.45,
                    MAGOMED_BIBULATOV: 1.31,
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
                    SAID_NURMAGOMEDOV: 2.45,
                    RICARDO_RAMOS: 1.54,
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
                    JAIRZINHO_ROZENSTRUIK: 2.25,
                    JUNIOR_ALBINI: 1.65,
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
                    THIAGO_ALVES: 2.50,
                    MAX_GRIFFIN: 1.50,
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
                    MARA_ROMERO_BORELLA: 2.70,
                    TAILA_SANTOS: 1.43,
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
                    MARKUS_PEREZ: 2.15,
                    ANTHONY_HERNANDEZ: 1.69,
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
                    LIVINHA_SOUZA: 1.43,
                    SARAH_FROTA: 2.80,
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
                    JOHNNY_WALKER: 1.43,
                    JUSTIN_LEDET: 2.80,
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
                    CHARLES_OLIVEIRA: 1.53,
                    DAVID_TEYMUR: 1.91,
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
                        'name': DEMIAN_MAIA,
                        'stats': '26-9-0',
                    },
                ],
                'winner': {
                    'fighter': DEMIAN_MAIA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:38',
                },
                'odds': {
                    DEMIAN_MAIA: 1.44,
                    LYMAN_GOOD: 2.60,
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
                    JOSE_ALDO: 1.80,
                    RENATO_MOICANO: 1.86,
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
                    MARLON_MORAES: 1.61,
                    RAPHAEL_ASSUNCAO: 2.30,
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
                    JONATHAN_MARTINEZ: 1.69,
                    WULIJI_BUREN: 2.10,
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
                    JALIN_TURNER: 1.44,
                    CALLAN_POTTER: 2.75,
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
                    LANDO_VANNATA: 1.22,
                    MARCOS_ROSA_MARIANO: 4.25,
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
                    KYUNG_HO_KANG: 1.25,
                    TERUTO_ISHIHARA: 3.65,
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
                    KAI_KARA_FRANCE: 1.35,
                    RAULIAN_PAIVA: 3.00,
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
                    SHANE_YOUNG: 1.23,
                    AUSTIN_ARNETT: 4.00,
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
                    DEVONTE_SMITH: 1.33,
                    DONG_HYUN_KIM: 3.15,
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
                    JIMMY_CRUTE: 1.71,
                    SAM_ALVEY: 2.10,
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
                    MONTANA_DE_LA_ROSA: 1.42,
                    NADIA_KASSEM: 2.85,
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
                    RICKY_SIMON: 1.80,
                    RANI_YAHYA: 1.80,
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
                    ISRAEL_ADESANYA: 1.19,
                    ANDERSON_SILVA: 4.25,
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
                    EMILY_WHITMIRE: 1.87,
                    ALEXANDRA_ALBU: 1.83,
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
                    LUKE_SANDERS: 1.66,
                    RENAN_BARAO: 2.15,
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
                    NIK_LENTZ: 2.20,
                    SCOTT_HOLTZMAN: 1.61,
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
                    ANDREA_LEE: 1.53,
                    ASHLEE_EVANS_SMITH: 2.36,
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
                    MANNY_BERMUDEZ: 1.49,
                    BENITO_LOPEZ: 2.50,
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
                    ALJAMAIN_STERLING: 2.06,
                    JIMMIE_RIVERA: 1.71,
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
                    ANDRE_FILI: 2.20,
                    MYLES_JURY: 1.65,
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
                    VICENTE_LUQUE: 1.19,
                    BRYAN_BARBERENA: 4.50,
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
                    KRON_GRACIE: 1.35,
                    ALEX_CACERES: 3.05,
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
                    CYNTHIA_CALVILLO: 1.27,
                    CORTNEY_CASEY_SANCHEZ: 3.65,
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
                    PAUL_FELDER: 1.90,
                    JAMES_VICK: 1.78,
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
                    FRANCIS_NGANNOU: 2.65,
                    CAIN_VELASQUEZ: 1.47,
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
                    DAMIR_ISMAGULOV: 1.31,
                    JOEL_ALVAREZ: 3.44,
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
                    DIEGO_FERREIRA: 2.06,
                    RUSTAM_KHABILOV: 1.71,
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
                    CHRIS_FISHGOLD: 1.38,
                    DANIEL_TEYMUR: 2.80,
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
                    ISMAIL_NAURDIEV: 3.25,
                    MICHEL_PRAZERES: 1.22,
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
                    DAMIR_HADZOVIC: 1.68,
                    MARC_POLO_REYES: 2.10,
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
                    DWIGHT_GRANT: 2.37,
                    CARLO_PEDERSOLI_JR: 1.57,
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
                    GILLIAN_ROBERTSON: 1.51,
                    VERONICA_MACEDO: 2.40,
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
                    MAGOMED_ANKALAEV: 1.44,
                    KLIDSON_DE_ABREU: 2.75,
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
                    PETR_YAN: 1.38,
                    JOHN_DODSON: 3.00,
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
                    'fighter': LIZ_CARMOUCHE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LIZ_CARMOUCHE: 1.57,
                    LUCIE_PUDILOVA: 2.34,
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
                    MICHAL_OLEKSIEJCZUK: 1.42,
                    GIAN_VILLANTE: 2.75,
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
                    STEFAN_STRUVE: 1.83,
                    MARCOS_ROGERIO_DE_LIMA: 1.91,
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
                    THIAGO_SANTOS: 1.74,
                    JAN_BLACHOWICZ: 2.00,
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
                    HANNA_CIFERS: 3.35,
                    POLYANA_VIANA: 1.33,
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
                    MACY_CHIASSON: 1.18,
                    GINA_MAZANY: 4.75,
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
                    EDMEN_SHAHBAZYAN: 1.63,
                    CHARLES_BYRD: 2.25,
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
                    DIEGO_SANCHEZ: 2.95,
                    MICKEY_GALL: 1.38,
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
                    CODY_STAMANN: 1.53,
                    ALEJANDRO_PEREZ: 2.43,
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
                    JOHNNY_WALKER: 1.54,
                    MISHA_CIRKUNOV: 2.45,
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
                    ZABIT_MAGOMEDSHARIPOV: 1.30,
                    JEREMY_STEPHENS: 3.45,
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
                    PEDRO_MUNHOZ: 2.42,
                    CODY_GARBRANDT: 1.54,
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
                    WEILI_ZHANG: 1.67,
                    TECIA_TORRES: 2.13,
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
                    BEN_ASKREN: 1.35,
                    ROBBIE_LAWLER: 3.22,
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
                    KAMARU_USMAN: 2.65,
                    TYRON_WOODLEY: 1.48,
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
                    JON_JONES: 1.12,
                    ANTHONY_SMITH: 5.50,
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
                    ALEX_WHITE: 1.69,
                    DAN_MORET: 2.10,
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
                    ALEX_MORONO: 1.53,
                    ZAK_OTTOW: 2.50,
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
                    MATT_SCHNELL: 2.00,
                    LOUIS_SMOLKA: 1.71,
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
                    MAURICE_GREEN: 2.85,
                    JEFF_HUGHES: 1.37,
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
                    YANA_KUNITSKAYA: 1.43,
                    MARION_RENEAU: 2.85,
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
                    ANTHONY_ROCCO_MARTIN: 1.43,
                    SERGIO_MORAES: 2.85,
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
                    GRANT_DAWSON: 1.44,
                    JULIAN_EROSA: 2.67,
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
                    OMARI_AKHMEDOV: 1.65,
                    TIM_BOETSCH: 2.21,
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
                    BENEIL_DARIUSH: 1.43,
                    DREW_DOBER: 2.75,
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
                    BLAGOY_IVANOV: 2.00,
                    BEN_ROTHWELL: 1.77,
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
                    NIKO_PRICE: 2.60,
                    TIM_MEANS: 1.45,
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
                    ELIZEU_ZALESKI_DOS_SANTOS: 1.92,
                    CURTIS_MILLENDER: 1.77,
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
                    JUNIOR_DOS_SANTOS: 1.42,
                    DERRICK_LEWIS: 2.71,
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
                    MIKE_GRUNDY: 1.95,
                    NAD_NARIMANI: 1.74,
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
                    MOLLY_MCCANN: 1.44,
                    PRISCILA_CACHOEIRA: 2.55,
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
                    DAN_IGE: 1.69,
                    DANNY_HENRY: 2.10,
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
                    SAPARBEG_SAFAROV: 2.41,
                    NICK_NEGUMEREANU: 1.57,
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
                    MARC_DIAKIESE: 2.45,
                    JOE_DUFFY: 1.53,
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
                    ARNOLD_ALLEN: 1.65,
                    JORDAN_RINALDI: 2.20,
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
                    JACK_MARSHMAN: 1.69,
                    JOHN_PHILLIPS: 2.05,
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
                    CLAUDIO_DA_SILVA: 1.63,
                    DANNY_ROBERTS: 2.20,
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
                    NATHANIEL_WOOD: 1.27,
                    JOSE_QUINONEZ: 3.55,
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
                    DOMINICK_REYES: 1.37,
                    VOLKAN_OEZDEMIR: 3.10,
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
                    LEON_EDWARDS: 1.65,
                    GUNNAR_NELSON: 2.21,
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
                    JORGE_MASVIDAL: 2.80,
                    DARREN_TILL: 1.41,
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
                    JORDAN_ESPINOSA: 2.15,
                    ERIC_SHELTON: 1.67,
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
                    MARLON_VERA: 1.57,
                    FRANKIE_SAENZ: 2.44,
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
                    CHRIS_GUTIERREZ: 1.29,
                    RYAN_MACDONALD: 3.15,
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
                    BRYCE_MITCHELL: 2.20,
                    BOBBY_MOFFETT: 1.65,
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
                    RANDA_MARKOS: 2.25,
                    ANGELA_HILL: 1.63,
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
                    MAYCEE_BARBER: 1.35,
                    JJ_ALDRICH: 3.00,
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
                    LUIS_PENA: 1.40,
                    STEVEN_PETERSON: 2.85,
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
                    JENNIFER_MAIA: 2.13,
                    ALEXIS_DAVIS: 1.67,
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
                    JUSSIER_FORMIGA: 2.30,
                    DEIVESON_FIGUEIREDO: 1.56,
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
                    JOHN_MAKDESSI: 1.32,
                    JESUS_PINEDO: 3.30,
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
                    CURTIS_BLAYDES: 1.36,
                    JUSTIN_WILLIS: 3.00,
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
                    ANTHONY_PETTIS: 4.00,
                    STEPHEN_THOMPSON: 1.22,
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
                    ALEX_PEREZ: 1.22,
                    MARK_DE_LA_ROSA: 4.08,
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
                    MARYNA_MOROZ: 2.40,
                    SABINA_MAZO_ISAZA: 1.57,
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
                    KEVIN_HOLLAND: 1.43,
                    GERALD_MEERSCHAERT: 2.80,
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
                    KEVIN_AGUILAR: 2.10,
                    ENRIQUE_BARZOLA: 1.67,
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
                    MARINA_RODRIGUEZ: 1.25,
                    JESSICA_AGUILAR: 3.95,
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
                    SODIQ_YUSUFF: 1.63,
                    SHEYMON_DA_SILVA_MORAES: 2.25,
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
                    PAUL_CRAIG: 2.60,
                    KENNEDY_NZECHUKWU: 1.50,
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
                    'fighter': MICHELLE_WATERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MICHELLE_WATERSON: 2.30,
                    KAROLINA_KOWALKIEWICZ: 1.61,
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
                    JOSH_EMMETT: 2.15,
                    MICHAEL_JOHNSON: 1.57,
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
                    JACK_HERMANSSON: 1.59,
                    DAVID_BRANCH: 2.15,
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
                    JUSTIN_GAETHJE: 1.91,
                    EDSON_BARBOZA: 1.77,
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
                    BRANDON_DAVIS: 1.47,
                    RANDY_COSTA: 2.55,
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
                    POLIANA_BOTELHO: 1.59,
                    LAUREN_MUELLER: 2.26,
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
                    MONTEL_JACKSON: 1.17,
                    ANDRE_SOUKHAMTHATH: 5.00,
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
                    BELAL_MUHAMMAD: 1.61,
                    CURTIS_MILLENDER: 2.28,
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
                    KHALID_TAHA: 2.34,
                    BOSTON_SALMON: 1.59,
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
                    MAX_GRIFFIN: 2.10,
                    ZELIM_IMADAEV: 1.71,
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
                    ALEXANDRE_PANTOJA: 1.54,
                    WILSON_REIS: 2.35,
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
                    MATT_FREVOLA: 2.25,
                    JALIN_TURNER: 1.56,
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
                    NIKITA_KRYLOV: 1.71,
                    OVINCE_SAINT_PREUX: 2.09,
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
                    DWIGHT_GRANT: 1.80,
                    ALAN_JOUBAN: 1.92,
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
                    KHALIL_ROUNTREE: 2.55,
                    ERYK_ANDERS: 1.50,
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
                    ISRAEL_ADESANYA: 1.48,
                    KELVIN_GASTELUM: 2.53,
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
                    DUSTIN_POIRIER: 2.85,
                    MAX_HOLLOWAY: 1.42,
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
                    MAGOMED_MUSTAFAEV: 2.10,
                    RAFAEL_FIZIEV: 1.71,
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
                    MICHAL_OLEKSIEJCZUK: 1.44,
                    GADZHIMURAD_ANTIGULOV: 2.75,
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
                    SHAMIL_ABDURAKHIMOV: 2.09,
                    MARCIN_TYBURA: 1.69,
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
                    ALEXANDER_YAKOVLEV: 1.61,
                    ALEX_DA_SILVA: 2.17,
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
                    SULTAN_ALIEV: 1.80,
                    KEITA_NAKAMURA: 1.87,
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
                    MOVSAR_EVLOEV: 1.20,
                    SEUNGWOO_CHOI: 4.40,
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
                    KRZYSZTOF_JOTKO: 1.40,
                    ALEN_AMEDOVSKI: 2.85,
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
                    ROXANNE_MODAFFERI: 3.40,
                    ANTONINA_SHEVCHENKO: 1.28
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
                    SERGEI_PAVLOVICH: 1.33,
                    MARCELO_GOLM: 3.15,
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
                    ISLAM_MAKHACHEV: 1.27,
                    ARMAN_TSARUKYAN: 3.60,
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
                    ALISTAIR_OVEREEM: 1.37,
                    ALEKSEI_OLEINIK: 2.90,
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
                    DHIEGO_LIMA: 2.25,
                    COURT_MCGEE: 1.59,
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
                    JIM_MILLER: 1.77,
                    JASON_GONZALEZ: 2.00,
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
                    AUGUSTO_SAKAI: 1.57,
                    ANDREI_ARLOVSKI: 2.40,
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
                    TAKASHI_SATO: 1.40,
                    BEN_SAUNDERS: 2.95,
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
                    ROOSEVELT_ROBERTS: 1.19,
                    THOMAS_GIFFORD: 4.50,
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
                    CORY_SANDHAGEN: 2.30,
                    JOHN_LINEKER: 1.63,
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
                    MIKE_PERRY: 2.36,
                    ALEX_OLIVEIRA: 1.59,
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
                    GLOVER_TEIXEIRA: 1.79,
                    ION_CUTELABA: 1.91,
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
                    JACK_HERMANSSON: 2.74,
                    RONALDO_SOUZA: 1.40,
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
                    GREG_HARDY: 1.29,
                    DMITRY_SMOLYAKOV: 3.50,
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
                    COLE_SMITH: 2.00,
                    MITCH_GAGNON: 1.71,
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
                    NORDINE_TALEB: 1.19,
                    KYLE_PREPOLEC: 4.50,
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
                    ARJAN_BHULLAR: 2.03,
                    JUAN_ADAMS: 1.69,
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
                    MATT_SAYLES: 1.50,
                    KYLE_NELSON: 2.56,
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
                    VINCE_MORALES: 2.52,
                    AIEMANN_ZAHABI: 1.53,
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
                    'fighter': ANDREW_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANDREW_SANCHEZ: 1.55,
                    MARC_ANDRE_BARRIAULT: 2.35,
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
                    WALT_HARRIS: 1.57,
                    SERGEY_SPIVAK: 2.38,
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
                    SHANE_BURGOS: 1.53,
                    CUB_SWANSON: 2.40,
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
                    MERAB_DVALISHVILI: 1.60,
                    BRAD_KATONA: 2.34,
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
                    DONALD_CERRONE: 2.05,
                    AL_IAQUINTA: 1.74,
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
                    DEREK_BRUNSON: 1.89,
                    ELIAS_THEODOROU: 1.83,
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
                    CARLOS_HUACHIN_QUIROZ: 8.00,
                    RAONI_BARCELOS: 1.05,
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
                    PRISCILA_CACHOEIRA: 2.32,
                    LUANA_CAROLINA: 1.53,
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
                    CLAY_GUIDA: 1.10,
                    BJ_PENN: 5.50,
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
                    SERGIO_MORAES: 2.10,
                    WARLLEY_ALVES: 1.71,
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
                    KURT_HOLOBAUGH: 1.93,
                    THIAGO_MOISES: 1.71,
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
                    RYAN_SPANN: 1.69,
                    ROGERIO_NOGUEIRA: 2.01,
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
                    BETHE_CORREIA: 4.00,
                    IRENE_ALDANA: 1.25,
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
                    LAUREANO_STAROPOLI: 1.96,
                    THIAGO_ALVES: 1.74,
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
                    ALEXANDER_VOLKANOVSKI: 2.10,
                    JOSE_ALDO: 1.67,
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
                    JARED_CANNONIER: 1.77,
                    ANDERSON_SILVA: 1.88,
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
                    ROSE_NAMAJUNAS: 2.20,
                    JESSICA_ANDRADE: 1.65,
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
                    TREVIN_GILES: 1.50,
                    ZAK_CUMMINGS: 2.55,
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
                    ED_HERMAN: 3.16,
                    PATRICK_CUMMINS: 1.36,
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
                    JULIAN_EROSA: 6.00,
                    JULIO_ACRE: 1.12,
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
                    GRANT_DAWSON: 1.61,
                    MICHAEL_TRIZANO: 2.33,
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
                    MICHEL_PEREIRA: 2.90,
                    DANNY_ROBERTS: 1.40,
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
                    CHARLES_JOURDAIN: 6.25,
                    DESMOND_GREEN: 1.09,
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
                    SIJARA_EUBANKS: 3.20,
                    ASPEN_LADD: 1.36,
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
                    NIK_LENTZ: 3.60,
                    CHARLES_OLIVEIRA: 1.24,
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
                    AUSTIN_HUBBARD: 4.75,
                    DAVI_RAMOS: 1.18,
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
                    DERRICK_KRANTZ: 8.00,
                    VICENTE_LUQUE: 1.07,
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
                    IAN_HEINISCH: 2.40,
                    ANTONIO_CARLOS_JUNIOR: 1.53,
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
                    KEVIN_LEE: 1.65,
                    RAFAEL_DOS_ANJOS: 2.20,
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
                    FELICIA_SPENCER: 2.67,
                    MEGAN_ANDERSON: 1.44,
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
                    DANILO_BELLUARDO: 1.87,
                    JOEL_ALVAREZ: 1.85,
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
                    DEVIN_CLARK: 1.83,
                    DARKO_STOSIC: 1.80,
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
                    EDUARDA_SANTANA: 1.89,
                    BEA_MALECKI: 1.80,
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
                    FRANK_CAMACHO: 1.72,
                    NICK_HEIN: 2.05,
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
                    LEONARDO_SANTOS: 1.63,
                    STEVIE_RAY: 2.24,
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
                    LINA_LANSBERG: 3.65,
                    TONYA_EVINGER: 1.24,
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
                    SERGEY_KHANDOZHKO: 1.61,
                    ROSTEM_AKMAN: 2.25,
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
                    SUNG_BIN_JO: 1.67,
                    DANIEL_TEYMUR: 1.86,
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
                    CHRISTOS_GIAGOS: 2.20,
                    DAMIR_HADZOVIC: 1.61,
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
                    CHRIS_FISHGOLD: 1.91,
                    MAKWAN_AMIRKHANI: 1.77,
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
                    ALEKSANDAR_RAKIC: 1.36,
                    JIMI_MANUWA: 2.95,
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
                    ANTHONY_SMITH: 3.50,
                    ALEXANDER_GUSTAFSSON: 1.27,
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
                    JOANNE_CALDERWOOD: 1.86,
                    KATLYN_CHOOKAGIAN: 1.87,
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
                    GRIGORY_POPOV: 2.30,
                    EDDIE_WINELAND: 1.57,
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
                    DARREN_STEWART: 2.45,
                    BEVON_LEWIS: 1.52,
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
                    ANGELA_HILL: 2.75,
                    YAN_XIAONAN: 1.39,
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
                    CALVIN_KATTAR: 1.57,
                    RICARDO_LAMAS: 2.30,
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
                    ALEXA_GRASSO: 1.72,
                    KAROLINA_KOWALKIEWICZ: 1.91,
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
                    PEDRO_MUNHOZ: 2.30,
                    ALJAMAIN_STERLING: 1.57,
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
                    NINA_ANSAROFF: 5.25,
                    TATIANA_SUAREZ: 1.12,
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
                    BLAGOY_IVANOV: 2.30,
                    TAI_TUIVASA: 1.56,
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
                    PETR_YAN: 1.25,
                    JIMMIE_RIVERA: 3.70,
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
                    DONALD_CERRONE: 2.85,
                    TONY_FERGUSON: 1.41,
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
                    JESSICA_EYE: 8.50,
                    VALENTINA_SHEVCHENKO: 1.06,
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
                    HENRY_CEJUDO: 2.35,
                    MARLON_MORAES: 1.57,
                },
            },
        ]
    },

    {
        'date': '2019-06-22',
        'name': 'UFC Fight Night: Greenville 2019',
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
                    ERIC_SPICELY: 3.85,
                    DERON_WINN: 1.26,
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
                    MATT_WIMAN: 3.84,
                    LUIS_PENA: 1.26,
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
                    DAN_IGE: 2.11,
                    KEVIN_AGUILAR: 1.69,
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
                    MOLLY_MCCANN: 2.90,
                    ARIANE_LIPSKI: 1.36,
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
                    SYURI_KONDO: 2.10,
                    ASHLEY_YODER: 1.70,
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
                    ANDERSON_BERLINGERI_DOS_SANTOS: 2.05,
                    ANDRE_EWELL: 1.70,
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
                    ALESSIO_DI_CHRICO: 2.72,
                    KEVIN_HOLLAND: 1.44,
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
                    RANDY_BROWN: 2.95,
                    BRYAN_BARBERENA: 1.39,
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
                    CHAN_SUNG_JUNG: 2.75,
                    RENATO_MOICANO: 1.40,
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
                    JAIRZINHO_ROZENSTRUIK: 1.43,
                    ALLEN_CROWDER: 2.63,
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
                    MONTANA_DE_LA_ROSA: 2.50,
                    ANDREA_LEE: 1.53,
                },
            },
        ]
    },

    {
        'date': '2019-06-29',
        'name': 'UFC Fight Night: Minneapolis 2019',
        'location': 'Minneapolis, Minnesota',
        'venue': 'Target Center',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUNIOR_ALBINI,
                        'stats': '14-5-0',
                    },
                    {
                        'name': MAURICE_GREEN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': MAURICE_GREEN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:38',
                },
                'time': '18:00',
                'odds': {
                    MAURICE_GREEN: 1.79,
                    JUNIOR_ALBINI: 1.87,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': AMANDA_RIBAS,
                        'stats': '6-1-0',
                    },
                    {
                        'name': EMILY_WHITMIRE,
                        'stats': '4-2-0',
                    },
                ],
                'winner': {
                    'fighter': AMANDA_RIBAS,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:10',
                },
                'time': '18:35',
                'odds': {
                    AMANDA_RIBAS: 2.50,
                    EMILY_WHITMIRE: 1.51,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DEQUAN_TOWNSEND,
                        'stats': '0-0-0',
                    },
                    {
                        'name': DALCHA_LUNGIAMBULA,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': DALCHA_LUNGIAMBULA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:42',
                },
                'time': '19:05',
                'odds': {
                    DALCHA_LUNGIAMBULA: 1.20,
                    DEQUAN_TOWNSEND: 3.65,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_MORET,
                        'stats': '13-5-0',
                    },
                    {
                        'name': JARED_GORDON,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': JARED_GORDON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    JARED_GORDON: 1.29,
                    DAN_MORET: 3.55,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': VINICIUS_CASTRO,
                        'stats': '9-2-0',
                    },
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': ERYK_ANDERS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:18',
                },
                'time': '20:04',
                'odds': {
                    ERYK_ANDERS: 1.32,
                    VINICIUS_CASTRO: 3.36,
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
                        'name': JOURNEY_NEWSON,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_RAMOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    RICARDO_RAMOS: 1.24,
                    JOURNEY_NEWSON: 3.65,
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
                        'name': ALONZO_MENIFIELD,
                        'stats': '8-0-0',
                    },
                ],
                'winner': {
                    'fighter': ALONZO_MENIFIELD,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:19',
                },
                'time': '21:05',
                'odds': {
                    ALONZO_MENIFIELD: 1.27,
                    PAUL_CRAIG: 3.70,
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
                        'name': DREW_DOBER,
                        'stats': '20-9-0',
                    },
                ],
                'winner': {
                    'fighter': DREW_DOBER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:07',
                },
                'time': '21:35',
                'odds': {
                    DREW_DOBER: 1.22,
                    MARC_POLO_REYES: 3.99,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': VINC_PICHEL,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ROOSEVELT_ROBERTS,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': VINC_PICHEL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:05',
                'odds': {
                    VINC_PICHEL: 3.10,
                    ROOSEVELT_ROBERTS: 1.33,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                    {
                        'name': DEMIAN_MAIA,
                        'stats': '26-9-0',
                    },
                ],
                'winner': {
                    'fighter': DEMIAN_MAIA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:35',
                'odds': {
                    DEMIAN_MAIA: 1.54,
                    ANTHONY_ROCCO_MARTIN: 2.40,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOSEPH_BENAVIDEZ,
                        'stats': '27-5-0',
                    },
                    {
                        'name': JUSSIER_FORMIGA,
                        'stats': '23-5-0',
                    },
                ],
                'winner': {
                    'fighter': JOSEPH_BENAVIDEZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:47',
                },
                'time': '23:05',
                'odds': {
                    JOSEPH_BENAVIDEZ: 1.74,
                    JUSSIER_FORMIGA: 1.99,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUNIOR_DOS_SANTOS,
                        'stats': '21-5-0',
                    },
                    {
                        'name': FRANCIS_NGANNOU,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCIS_NGANNOU,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:11',
                },
                'time': '23:35',
                'odds': {
                    FRANCIS_NGANNOU: 1.43,
                    JUNIOR_DOS_SANTOS: 2.65,
                },
            },
        ]
    },

    {
        'date': '2019-07-06',
        'name': 'UFC 239: Las Vegas 2019',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PANNIE_KIANZAD,
                        'stats': '11-3-0',
                    },
                    {
                        'name': JULIA_AVILA,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': JULIA_AVILA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    JULIA_AVILA: 1.38,
                    PANNIE_KIANZAD: 3.00,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CHANCE_RENCOUNTRE,
                        'stats': '13-3-0',
                    },
                    {
                        'name': ISMAIL_NAURDIEV,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': CHANCE_RENCOUNTRE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:05',
                'odds': {
                    CHANCE_RENCOUNTRE: 4.80,
                    ISMAIL_NAURDIEV: 1.17,
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
                        'name': EDMEN_SHAHBAZYAN,
                        'stats': '9-0-0',
                    },
                ],
                'winner': {
                    'fighter': EDMEN_SHAHBAZYAN,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:12',
                },
                'time': '19:35',
                'odds': {
                    EDMEN_SHAHBAZYAN: 1.13,
                    JACK_MARSHMAN: 5.25,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': SONG_YADONG,
                        'stats': '13-3-0',
                    },
                    {
                        'name': ALEJANDRO_PEREZ,
                        'stats': '22-7-1',
                    },
                ],
                'winner': {
                    'fighter': SONG_YADONG,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:04',
                },
                'time': '20:05',
                'odds': {
                    SONG_YADONG: 1.46,
                    ALEJANDRO_PEREZ: 2.66,
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
                        'name': CLAUDIA_GADELHA,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': CLAUDIA_GADELHA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    CLAUDIA_GADELHA: 1.49,
                    RANDA_MARKOS: 2.44,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': NOHELN_HERNANDEZ,
                        'stats': '0-0-0',
                    },
                    {
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:25',
                },
                'time': '21:00',
                'odds': {
                    MARLON_VERA: 1.18,
                    NOHELN_HERNANDEZ: 4.50,
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
                        'name': GILBERT_MELENDEZ,
                        'stats': '22-7-0',
                    },
                ],
                'winner': {
                    'fighter': ARNOLD_ALLEN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:35',
                'odds': {
                    ARNOLD_ALLEN: 1.29,
                    GILBERT_MELENDEZ: 3.55,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_CHIESA,
                        'stats': '15-4-0',
                    },
                    {
                        'name': DIEGO_SANCHEZ,
                        'stats': '31-11-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAEL_CHIESA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:05',
                'odds': {
                    MICHAEL_CHIESA: 1.22,
                    DIEGO_SANCHEZ: 4.00,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': LUKE_ROCKHOLD,
                        'stats': '16-4-0',
                    },
                    {
                        'name': JAN_BLACHOWICZ,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': JAN_BLACHOWICZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:39',
                },
                'time': '22:35',
                'odds': {
                    JAN_BLACHOWICZ: 2.95,
                    LUKE_ROCKHOLD: 1.39,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BEN_ASKREN,
                        'stats': '18-0-0',
                    },
                    {
                        'name': JORGE_MASVIDAL,
                        'stats': '33-13-0',
                    },
                ],
                'winner': {
                    'fighter': JORGE_MASVIDAL,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:05',
                },
                'time': '23:00',
                'odds': {
                    JORGE_MASVIDAL: 2.59,
                    BEN_ASKREN: 1.48,
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
                        'name': AMANDA_NUNES,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': AMANDA_NUNES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:10',
                },
                'time': '23:35',
                'odds': {
                    AMANDA_NUNES: 1.22,
                    HOLLY_HOLM: 4.00,
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
                        'name': JON_JONES,
                        'stats': '24-1-0',
                    },
                ],
                'winner': {
                    'fighter': JON_JONES,
                    'by': 's.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:55',
                'odds': {
                    JON_JONES: 1.15,
                    THIAGO_SANTOS: 4.50,
                },
            },
        ]
    },

    {
        'date': '2019-07-13',
        'name': 'UFC Fight Night: Sacramento 2019',
        'location': 'Sacramento, United States',
        'venue': 'Golden 1 Center',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BENITO_LOPEZ,
                        'stats': '9-1-0',
                    },
                    {
                        'name': VINCE_MORALES,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': BENITO_LOPEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:05',
                'odds': {
                    VINCE_MORALES: 1.93,  # 1.83
                    BENITO_LOPEZ: 1.95,  # 1.83
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': LIVINHA_SOUZA,
                        'stats': '12-1-0',
                    },
                    {
                        'name': BRIANNA_VAN_BUREN,
                        'stats': '8-1-0',
                    },
                ],
                'winner': {
                    'fighter': BRIANNA_VAN_BUREN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:35',
                'odds': {
                    BRIANNA_VAN_BUREN: 1.85,  # 1.87
                    LIVINHA_SOUZA: 1.95,  # 1.80
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LIU_PINGYUAN,
                        'stats': '0-0-0',
                    },
                    {
                        'name': JONATHAN_MARTINEZ,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': JONATHAN_MARTINEZ,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:54',
                },
                'time': '18:05',
                'odds': {
                    JONATHAN_MARTINEZ: 2.20,  # 2.55
                    LIU_PINGYUAN: 1.65,  # 1.44
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
                        'name': RYAN_HALL,
                        'stats': '7-1-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_HALL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:35',
                'odds': {
                    DARREN_ELKINS: 1.90,  # 1.80
                    RYAN_HALL: 1.90,  # 1.89
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JULIANNA_PENA,
                        'stats': '9-3-0',
                    },
                    {
                        'name': NICCO_MONTANO,
                        'stats': '5-2-0',
                    },
                ],
                'winner': {
                    'fighter': JULIANNA_PENA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:05',
                'odds': {
                    NICCO_MONTANO: 2.25,  # 2.95
                    JULIANNA_PENA: 1.60,  # 1.40
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_FILI,
                        'stats': '19-6-0',
                    },
                    {
                        'name': SHEYMON_DA_SILVA_MORAES,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_FILI,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:07',
                },
                'time': '19:35',
                'odds': {
                    ANDRE_FILI: 1.85,  # 1.55
                    SHEYMON_DA_SILVA_MORAES: 1.95,  # 2.33
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_RODRIGUEZ,
                        'stats': '10-3-0',
                    },
                    {
                        'name': JOHN_ALLAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_ALLAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    JOHN_ALLAN: 4.20,  # 3.75
                    MIKE_RODRIGUEZ: 1.22,  # 1.22
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
                        'name': CEZAR_FERREIRA,
                        'stats': '14-7-0',
                    },
                ],
                'winner': {
                    'fighter': MARVIN_VETTORI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    CEZAR_FERREIRA: 2.25,  # 2.69
                    MARVIN_VETTORI: 1.62,  # 1.44
                },
                'prediction': CEZAR_FERREIRA,
                'bet': 10,
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KARL_ROBERSON,
                        'stats': '7-2-0',
                    },
                    {
                        'name': WELLINGTON_TURMAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': KARL_ROBERSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:05',
                'odds': {
                    KARL_ROBERSON: 1.47,  # 1.44
                    WELLINGTON_TURMAN: 2.60,  # 2.70
                },
                'prediction': WELLINGTON_TURMAN,
                'bet': 10,
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JOSH_EMMETT,
                        'stats': '14-2-0',
                    },
                    {
                        'name': MIRSAD_BEKTIC,
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': JOSH_EMMETT,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:25',
                },
                'time': '21:35',
                'odds': {
                    JOSH_EMMETT: 2.25,  # 2.40
                    MIRSAD_BEKTIC: 1.70,  # 1.54
                },
                'prediction': JOSH_EMMETT,
                'bet': 10,
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': URIJAH_FABER,
                        'stats': '34-10-0',
                    },
                    {
                        'name': RICKY_SIMON,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': URIJAH_FABER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:46',
                },
                'time': '22:05',
                'odds': {
                    RICKY_SIMON: 1.30,  # 1.26
                    URIJAH_FABER: 3.50,  # 3.80
                },
                'prediction': RICKY_SIMON,
                'bet': 10,
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GERMAINE_DE_RANDAMIE,
                        'stats': '8-3-0',
                    },
                    {
                        'name': ASPEN_LADD,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': GERMAINE_DE_RANDAMIE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:16',
                },
                'time': '22:35',
                'odds': {
                    GERMAINE_DE_RANDAMIE: 1.95,  # 1.92
                    ASPEN_LADD: 1.85,  # 1.74
                },
                'prediction': GERMAINE_DE_RANDAMIE,
                'bet': 10,
            },
        ]
    },

    {
        'date': '2019-07-20',
        'name': 'UFC Fight Night - San Antonio 2019',
        'location': 'San Antonio, Texas',
        'venue': 'AT&T Center',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': FELIPE_COLARES,
                        'stats': '8-1-0'
                    },
                    {
                        'name': DOM_PILARTE,
                        'stats': '8-1-0'
                    }
                ],
                'winner': {
                    'fighter': FELIPE_COLARES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:05',
                'odds': {
                    FELIPE_COLARES: 4.00,
                    DOM_PILARTE: 1.25
                },
                'prediction': DOM_PILARTE
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JIN_SOON_SON,
                        'stats': '0-0-0'
                    },
                    {
                        'name': MARIO_BAUTISTA,
                        'stats': '0-0-0'
                    },
                ],
                'winner': {
                    'fighter': MARIO_BAUTISTA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:35',
                'odds': {
                    JIN_SOON_SON: 1.54,
                    MARIO_BAUTISTA: 2.43
                },
                'prediction': MARIO_BAUTISTA
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GABRIEL_SILVA,
                        'stats': '0-0-0'
                    },
                    {
                        'name': RAY_BORG,
                        'stats': '11-4-0'
                    }
                ],
                'winner': {
                    'fighter': RAY_BORG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:05',
                'odds': {
                    GABRIEL_SILVA: 2.45,
                    RAY_BORG: 1.54
                },
                'prediction': RAY_BORG
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JENNIFER_MAIA,
                        'stats': '16-5-1'
                    },
                    {
                        'name': ROXANNE_MODAFFERI,
                        'stats': '3-3-0'
                    }
                ],
                'winner': {
                    'fighter': JENNIFER_MAIA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'time': '19:35',
                'odds': {
                    JENNIFER_MAIA: 1.71,
                    ROXANNE_MODAFFERI: 2.10
                },
                'prediction': JENNIFER_MAIA
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': KLIDSON_DE_ABREU,
                        'stats': '0-0-0'
                    },
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0'
                    }
                ],
                'winner': {
                    'fighter': KLIDSON_DE_ABREU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'time': '20:05',
                'odds': {
                    KLIDSON_DE_ABREU: 1.56,
                    SAM_ALVEY: 2.37
                },
                'prediction': SAM_ALVEY
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': IRENE_ALDANA,
                        'stats': '9-4-0'
                    },
                    {
                        'name': RAQUEL_PENNINGTON,
                        'stats': '9-8-0'
                    }
                ],
                'winner': {
                    'fighter': RAQUEL_PENNINGTON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'odds': {
                    IRENE_ALDANA: 1.69,
                    RAQUEL_PENNINGTON: 2.10
                },
                'prediction': RAQUEL_PENNINGTON
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': STEVEN_PETERSON,
                        'stats': '17-8-0'
                    },
                    {
                        'name': ALEX_CACERES,
                        'stats': '14-12-0'
                    }
                ],
                'winner': {
                    'fighter': ALEX_CACERES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'odds': {
                    STEVEN_PETERSON: 1.85,
                    ALEX_CACERES: 1.83
                },
                'prediction': STEVEN_PETERSON
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': BEN_ROTHWELL,
                        'stats': '36-11-0'
                    },
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0'
                    }
                ],
                'winner': {
                    'fighter': ANDREI_ARLOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'odds': {
                    BEN_ROTHWELL: 1.54,
                    ANDREI_ARLOVSKI: 2.43
                },
                'prediction': ANDREI_ARLOVSKI
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FRANCISCO_TRINALDO,
                        'stats': '23-6-0'
                    },
                    {
                        'name': ALEXANDER_HERNANDEZ,
                        'stats': '10-2-0'
                    }
                ],
                'winner': {
                    'fighter': ALEXANDER_HERNANDEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'odds': {
                    FRANCISCO_TRINALDO: 2.73,
                    ALEXANDER_HERNANDEZ: 1.38
                },
                'prediction': ALEXANDER_HERNANDEZ
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_HOOKER,
                        'stats': '18-8-0'
                    },
                    {
                        'name': JAMES_VICK,
                        'stats': '13-3-0'
                    }
                ],
                'winner': {
                    'fighter': DAN_HOOKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:33'
                },
                'odds': {
                    DAN_HOOKER: 1.70,
                    JAMES_VICK: 2.05
                },
                'prediction': DAN_HOOKER
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUAN_ADAMS,
                        'stats': '5-0-0'
                    },
                    {
                        'name': GREG_HARDY,
                        'stats': '3-1-0'
                    }
                ],
                'winner': {
                    'fighter': GREG_HARDY,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:45'
                },
                'odds': {
                    JUAN_ADAMS: 1.74,
                    GREG_HARDY: 1.83
                },
                'prediction': JUAN_ADAMS
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0'
                    },
                    {
                        'name': ALEKSEI_OLEINIK,
                        'stats': '57-11-1'
                    }
                ],
                'winner': {
                    'fighter': WALT_HARRIS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:12'
                },
                'odds': {
                    WALT_HARRIS: 1.65,
                    ALEKSEI_OLEINIK: 2.25
                },
                'prediction': ALEKSEI_OLEINIK
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LEON_EDWARDS,
                        'stats': '17-3-0'
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0'
                    }
                ],
                'winner': {
                    'fighter': LEON_EDWARDS,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00'
                },
                'odds': {
                    LEON_EDWARDS: 1.77,
                    RAFAEL_DOS_ANJOS: 1.87
                },
                'prediction': LEON_EDWARDS
            }
        ]
    },

    {
        'date': '2019-07-28',
        'name': 'UFC 240: Edmonton 2019',
        'location': '',
        'venue': '',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ERIK_KOCH,
                        'stats': '15-6-0'
                    },
                    {
                        'name': KYLE_STEWART,
                        'stats': '8-1-0'
                    }
                ],
                'winner': {
                    'fighter': ERIK_KOCH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ERIK_KOCH: 1.90,
                    KYLE_STEWART: 1.90
                },
                'prediction': KYLE_STEWART,
                'bet': 10,
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': GILLIAN_ROBERTSON,
                        'stats': '6-3-0',
                    },
                    {
                        'name': SARAH_FROTA,
                        'stats': '9-1-0',
                    }
                ],
                'winner': {
                    'fighter': GILLIAN_ROBERTSON,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:13',
                },
                'odds': {
                    GILLIAN_ROBERTSON: 1.75,
                    SARAH_FROTA: 2.05
                },
                'prediction': SARAH_FROTA,
                'bet': 5
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDRE_PANTOJA,
                        'stats': '20-3-0'
                    },
                    {
                        'name': DEIVESON_FIGUEIREDO,
                        'stats': '15-1-0'
                    }
                ],
                'winner': {
                    'fighter': DEIVESON_FIGUEIREDO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'odds': {
                    ALEXANDRE_PANTOJA: 1.85,
                    DEIVESON_FIGUEIREDO: 1.95
                },
                'prediction': DEIVESON_FIGUEIREDO,
                'bet': 20,
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': GAVIN_TUCKER,
                        'stats': '10-1-0'
                    },
                    {
                        'name': SEUNGWOO_CHOI,
                        'stats': '7-1-0'
                    }
                ],
                'winner': {
                    'fighter': GAVIN_TUCKER,
                    'by': 'submission',
                    'round': 3,
                    'time': '3:17'
                },
                'odds': {
                    GAVIN_TUCKER: 1.90,
                    SEUNGWOO_CHOI: 1.90
                },
                'prediction': GAVIN_TUCKER,
                'bet': 0,
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HAKEEM_DAWODU,
                        'stats': '9-0-1'
                    },
                    {
                        'name': YOSHINORI_HORIE,
                        'stats': '0-0-0'
                    }
                ],
                'winner': {
                    'fighter': HAKEEM_DAWODU,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:09',
                },
                'odds': {
                    HAKEEM_DAWODU: 1.25,
                    YOSHINORI_HORIE: 3.75
                },
                'prediction': YOSHINORI_HORIE,
                'bet': 5,
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXIS_DAVIS,
                        'stats': '19-9-0'
                    },
                    {
                        'name': VIVIANE_ARAUJO,
                        'stats': '6-1-0'
                    }
                ],
                'winner': {
                    'fighter': VIVIANE_ARAUJO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEXIS_DAVIS: 2.50,
                    VIVIANE_ARAUJO: 1.52
                },
                'prediction': VIVIANE_ARAUJO,
                'bet': 20,
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KRZYSZTOF_JOTKO,
                        'stats': '19-4-0'
                    },
                    {
                        'name': MARC_ANDRE_BARRIAULT,
                        'stats': '11-1-0',
                    }
                ],
                'winner': {
                    'fighter': KRZYSZTOF_JOTKO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KRZYSZTOF_JOTKO: 1.55,
                    MARC_ANDRE_BARRIAULT: 2.40
                },
                'prediction': MARC_ANDRE_BARRIAULT,
                'bet': 20,
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': OLIVIER_AUBIN_MERCIER,
                        'stats': '12-4-0'
                    },
                    {
                        'name': ARMAN_TSARUKYAN,
                        'stats': '12-1-0'
                    }
                ],
                'winner': {
                    'fighter': ARMAN_TSARUKYAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    OLIVIER_AUBIN_MERCIER: 2.50,
                    ARMAN_TSARUKYAN: 1.62
                },
                'prediction': ARMAN_TSARUKYAN,
                'bet': 5,
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GEOFF_NEAL,
                        'stats': '11-2-0'
                    },
                    {
                        'name': NIKO_PRICE,
                        'stats': '13-2-0'
                    }
                ],
                'winner': {
                    'fighter': GEOFF_NEAL,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:39'
                },
                'odds': {
                    GEOFF_NEAL: 1.30,
                    NIKO_PRICE: 3.30
                },
                'prediction': NIKO_PRICE,
                'bet': 5,
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CRIS_CYBORG,
                        'stats': '20-2-0'
                    },
                    {
                        'name': FELICIA_SPENCER,
                        'stats': '6-0-0'
                    }
                ],
                'winner': {
                    'fighter': CRIS_CYBORG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00'
                },
                'odds': {
                    CRIS_CYBORG: 1.22,
                    FELICIA_SPENCER: 3.91
                }
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MAX_HOLLOWAY,
                        'stats': '20-3-0'
                    },
                    {
                        'name': FRANKIE_EDGAR,
                        'stats': '22-6-1'
                    }
                ],
                'winner': {
                    'fighter': MAX_HOLLOWAY,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    MAX_HOLLOWAY: 1.26,
                    FRANKIE_EDGAR: 4.00
                },
                'prediction': MAX_HOLLOWAY,
                'bet': 10,
            }
        ]
    },

    {
        'date': '2019-08-04',
        'name': 'UFC Fight Night: Covington vs Lawler',
        'location': 'Newark, United States',
        'venue': 'Prudential Center',
        'fights': [
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MIRANDA_GRANGER,
                        'stats': '0-0-0'
                    },
                    {
                        'name': HANNAH_GOLDY,
                        'stats': '0-0-0'
                    }
                ],
                'winner': {
                    'fighter': MIRANDA_GRANGER,
                    'by': 'dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MIRANDA_GRANGER: 2.35,
                    HANNAH_GOLDY: 1.57,
                },
                'prediction': MIRANDA_GRANGER,
                'bet': 5,
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CLAUDIO_DA_SILVA,
                        'stats': '13-1-0'
                    },
                    {
                        'name': COLE_WILLIAMS,
                        'stats': '11-1-0'
                    }
                ],
                'winner': {
                    'fighter': CLAUDIO_DA_SILVA,
                    'by': 'sub',
                    'round': 1,
                    'time': '2:33',
                },
                'odds': {
                    CLAUDIO_DA_SILVA: 1.23,
                    COLE_WILLIAMS: 4.00,
                },
                'prediction': CLAUDIO_DA_SILVA,
                'bet': 5,
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': LAUREN_MURPHY,
                        'stats': '10-4-0',
                    },
                    {
                        'name': MARA_ROMERO_BORELLA,
                        'stats': '13-5-0'
                    }
                ],
                'winner': {
                    'fighter': LAUREN_MURPHY,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LAUREN_MURPHY: 2.40,
                    MARA_ROMERO_BORELLA: 1.55,
                },
                'prediction': MARA_ROMERO_BORELLA,
                'bet': 5,
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_ESPINOSA,
                        'stats': '13-5-0',
                    },
                    {
                        'name': MATT_SCHNELL,
                        'stats': '13-4-0'
                    }
                ],
                'winner': {
                    'fighter': MATT_SCHNELL,
                    'by': 'sub',
                    'round': 1,
                    'time': '1:23',
                },
                'odds': {
                    JORDAN_ESPINOSA: 1.85,
                    MATT_SCHNELL: 1.95,
                },
                'prediction': JORDAN_ESPINOSA,
                'bet': 5,
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANTONINA_SHEVCHENKO,
                        'stats': '7-0-0'
                    },
                    {
                        'name': LUCIE_PUDILOVA,
                        'stats': '8-4-0',
                    }
                ],
                'winner': {
                    'fighter': ANTONINA_SHEVCHENKO,
                    'by': 'sub',
                    'round': 2,
                    'time': '',
                },
                'odds': {
                    ANTONINA_SHEVCHENKO: 1.60,
                    LUCIE_PUDILOVA: 2.30,
                },
                'prediction': ANTONINA_SHEVCHENKO,
                'bet': 10,
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICKEY_GALL,
                        'stats': '5-2-0',
                    },
                    {
                        'name': SALIM_TOUAHRI,
                        'stats': '10-3-0'
                    }
                ],
                'winner': {
                    'fighter': MICKEY_GALL,
                    'by': 'dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MICKEY_GALL: 2.05,
                    SALIM_TOUAHRI: 1.75,
                },
                'prediction': SALIM_TOUAHRI,
                'bet': 5,
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DARKO_STOSIC,
                        'stats': '13-1-0'
                    },
                    {
                        'name': KENNEDY_NZECHUKWU,
                        'stats': '6-1-0'
                    }
                ],
                'winner': {
                    'fighter': KENNEDY_NZECHUKWU,
                    'by': 'dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DARKO_STOSIC: 1.75,
                    KENNEDY_NZECHUKWU: 2.05,
                },
                'prediction': KENNEDY_NZECHUKWU,
                'bet': 5,
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': SCOTT_HOLTZMAN,
                        'stats': '12-3-0'
                    },
                    {
                        'name': DONG_HYUN_MA,
                        'stats': '16-9-3'
                    }
                ],
                'winner': {
                    'fighter': SCOTT_HOLTZMAN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:00',
                },
                'odds': {
                    SCOTT_HOLTZMAN: 1.25,
                    DONG_HYUN_MA: 3.85,
                },
                'prediction': SCOTT_HOLTZMAN,
                'bet': 5,
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TREVIN_GILES,
                        'stats': '11-0-0'
                    },
                    {
                        'name': GERALD_MEERSCHAERT,
                        'stats': '28-11-0'
                    }
                ],
                'winner': {
                    'fighter': GERALD_MEERSCHAERT,
                    'by': 'sub',
                    'round': 3,
                    'time': '1:54',
                },
                'odds': {
                    TREVIN_GILES: 1.63,
                    GERALD_MEERSCHAERT: 2.25,
                },
                'prediction': TREVIN_GILES,
                'bet': 10,
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOAQUIM_SILVA,
                        'stats': '11-1-0'
                    },
                    {
                        'name': NASRAT_HAQPARAST,
                        'stats': '10-2-0'
                    }
                ],
                'winner': {
                    'fighter': NASRAT_HAQPARAST,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:37',
                },
                'odds': {
                    JOAQUIM_SILVA: 2.90,
                    NASRAT_HAQPARAST: 1.40,
                },
                'prediction': NASRAT_HAQPARAST,
                'bet': 5,
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0'
                    },
                    {
                        'name': CLAY_GUIDA,
                        'stats': '34-15-0'
                    }
                ],
                'winner': {
                    'fighter': JIM_MILLER,
                    'by': 'sub',
                    'round': 1,
                    'time': '0:57',
                },
                'odds': {
                    JIM_MILLER: 1.60,
                    CLAY_GUIDA: 2.30,
                },
                'prediction': CLAY_GUIDA,
                'bet': 5,
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': COLBY_COVINGTON,
                        'stats': '14-1-0',
                    },
                    {
                        'name': ROBBIE_LAWLER,
                        'stats': '28-13-0',
                    }
                ],
                'winner': {
                    'fighter': COLBY_COVINGTON,
                    'by': 'dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    COLBY_COVINGTON: 1.45,
                    ROBBIE_LAWLER: 2.75,
                },
                'prediction': COLBY_COVINGTON,
                'bet': 20,
            }
        ]
    },

    {
        'date': '2019-08-11',
        'name': 'UFC Fight Night: Shevchenko vs Carmouche',
        'location': 'Montevideo Uruguay',
        'venue': 'Antel Arena',
        'fights': [
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': POLYANA_VIANA,
                        'stats': '10-3-0'
                    },
                    {
                        'name': VERONICA_MACEDO,
                        'stats': '5-3-1'
                    }
                ],
                'winner': {
                    'fighter': VERONICA_MACEDO,
                    'by': 'sub',
                    'round': 1,
                    'time': '1:09',
                },
                'odds': {
                    POLYANA_VIANA: 2.10,
                    VERONICA_MACEDO: 1.72
                },
                'prediction': POLYANA_VIANA,
                'bet': 20,
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_DA_SILVA,
                        'stats': '20-2-0',
                    },
                    {
                        'name': KAZULA_VARGAS,
                        'stats': '10-2-0'
                    },
                ],
                'winner': {
                    'fighter': ALEX_DA_SILVA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEX_DA_SILVA: 1.36,
                    KAZULA_VARGAS: 3.00
                },
                'prediction': ALEX_DA_SILVA,
                'bet': 5,
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_GUTIERREZ,
                        'stats': '13-4-1'
                    },
                    {
                        'name': GERALDO_DE_FREITAS,
                        'stats': '12-4-0'
                    }
                ],
                'winner': {
                    'fighter': CHRIS_GUTIERREZ,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CHRIS_GUTIERREZ: 2.05,
                    GERALDO_DE_FREITAS: 1.75
                },
                'prediction': GERALDO_DE_FREITAS,
                'bet': 20,
            },
            {
                'fighters': [
                    {
                        'name': RAULIAN_PAIVA,
                        'stats': '18-2-0'
                    },
                    {
                        'name': ROGERIO_BONTORIN,
                        'stats': '15-1-0'
                    }
                ],
                'winner': {
                    'fighter': ROGERIO_BONTORIN,
                    'by': 'tko',
                    'round': 1,
                    'time': '2:56',
                },
                'odds': {
                    RAULIAN_PAIVA: 1.95,
                    ROGERIO_BONTORIN: 1.85
                },
                'prediction': ROGERIO_BONTORIN,
                'bet': 20,
            },
            {
                'fighters': [
                    {
                        'name': MARINA_RODRIGUEZ,
                        'stats': '11-0-1'
                    },
                    {
                        'name': TECIA_TORRES,
                        'stats': '10-4-0'
                    }
                ],
                'winner': {
                    'fighter': MARINA_RODRIGUEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MARINA_RODRIGUEZ: 2.25,
                    TECIA_TORRES: 1.65
                },
                'prediction': MARINA_RODRIGUEZ,
                'bet': 15,
            },
            {
                'fighters': [
                    {
                        'name': CIRYL_GANE,
                        'stats': '3-0-0'
                    },
                    {
                        'name': RAPHAEL_PESSOA_NUNES,
                        'stats': '9-0-0'
                    }
                ],
                'winner': {
                    'fighter': CIRYL_GANE,
                    'by': 'sub',
                    'round': 1,
                    'time': '4:12',
                },
                'odds': {
                    CIRYL_GANE: 1.20,
                    RAPHAEL_PESSOA_NUNES: 4.20
                },
                'prediction': CIRYL_GANE,
                'bet': 5,
            },
            {
                'fighters': [
                    {
                        'name': GILBERT_BURNS,
                        'stats': '15-3-0'
                    },
                    {
                        'name': ALEKSEI_KUNCHENKO,
                        'stats': '20-0-0'
                    },
                ],
                'winner': {
                    'fighter': GILBERT_BURNS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    GILBERT_BURNS: 2.10,
                    ALEKSEI_KUNCHENKO: 1.72
                },
                'prediction': ALEKSEI_KUNCHENKO,
                'bet': 20,
            },
            {
                'fighters': [
                    {
                        'name': BOBBY_MOFFETT,
                        'stats': '14-4-0'
                    },
                    {
                        'name': ENRIQUE_BARZOLA,
                        'stats': '15-4-1'
                    }
                ],
                'winner': {
                    'fighter': ENRIQUE_BARZOLA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    BOBBY_MOFFETT: 2.10,
                    ENRIQUE_BARZOLA: 1.72
                },
                'prediction': BOBBY_MOFFETT,
                'bet': 20,
            },
            {
                'fighters': [
                    {
                        'name': OSKAR_PIECHOTA,
                        'stats': '11-1-1'
                    },
                    {
                        'name': RODOLFO_VIEIRA,
                        'stats': '5-0-0'
                    }
                ],
                'winner': {
                    'fighter': RODOLFO_VIEIRA,
                    'by': 'sub',
                    'round': 2,
                    'time': '4:26',
                },
                'odds': {
                    OSKAR_PIECHOTA: 2.85,
                    RODOLFO_VIEIRA: 1.40
                },
                'prediction': RODOLFO_VIEIRA,
                'bet': 5,
            },
            {
                'fighters': [
                    {
                        'name': ILIR_LATIFI,
                        'stats': '14-6-0'
                    },
                    {
                        'name': VOLKAN_OEZDEMIR,
                        'stats': '15-4-0'
                    }
                ],
                'winner': {
                    'fighter': VOLKAN_OEZDEMIR,
                    'by': 'ko',
                    'round': 2,
                    'time': '4:31',
                },
                'odds': {
                    ILIR_LATIFI: 2.25,
                    VOLKAN_OEZDEMIR: 1.65
                },
                'prediction': VOLKAN_OEZDEMIR,
                'bet': 15,
            },
            {
                'fighters': [
                    {
                        'name': HUMBERTO_BANDENAY,
                        'stats': '14-6-0'
                    },
                    {
                        'name': EDUARDO_GARAGORRI,
                        'stats': '12-0-0'
                    }
                ],
                'winner': {
                    'fighter': EDUARDO_GARAGORRI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    HUMBERTO_BANDENAY: 2.00,
                    EDUARDO_GARAGORRI: 1.80
                },
                'prediction': EDUARDO_GARAGORRI,
                'bet': 20,
            },
            {
                'fighters': [
                    {
                        'name': MIKE_PERRY,
                        'stats': '13-4-0'
                    },
                    {
                        'name': VICENTE_LUQUE,
                        'stats': '16-6-1'
                    }
                ],
                'winner': {
                    'fighter': VICENTE_LUQUE,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MIKE_PERRY: 2.75,
                    VICENTE_LUQUE: 1.45
                },
                'prediction': VICENTE_LUQUE,
                'bet': 10,
            },
            {
                'fighters': [
                    {
                        'name': VALENTINA_SHEVCHENKO,
                        'stats': '17-3-0'
                    },
                    {
                        'name': LIZ_CARMOUCHE,
                        'stats': '13-6-0'
                    }
                ],
                'winner': {
                    'fighter': VALENTINA_SHEVCHENKO,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    VALENTINA_SHEVCHENKO: 1.08,
                    LIZ_CARMOUCHE: 7.50
                },
                'prediction': VALENTINA_SHEVCHENKO,
                'by': 5,
            },
        ]
    }

]
