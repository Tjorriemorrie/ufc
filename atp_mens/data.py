from men import *
from location import *

# acc   roi     profit  desc
# 93.6  38.8    3474    2019 antwerp                (4, 335), (2, 323), (3, 268), (7, 251), (1, 247)
# 84.5  31.3    3462    2018 london                 (1, 680), (7, 470), (3, 409), (2, 282), (6, 279)
# 76.7  24.7    3453    2019 stockholm              (1, 707), (3, 409), (2, 407), (6, 322), (9, 293)
# 77.4  24.1    2742    2018 antalya                        (2, 729), (1, 690), (5, 531), (3, 397)
# 75.4  29.3    2619    2019 moscow                         (1, 992), (2, 428), (5, 214), (6, 206)
# 72.9  24.4    2480    2018 eastbourne                     (1, 841), (2, 696), (5, 301), (3, 240)

# 76.4  30.6    2743    2019 shanghai                        (1, 1311), (3, 315), (4, 310), (2, 277)
# 78.7  26.3    2111    2019 beijing                        (1, 1098), (3, 658), (4, 648), (2, 646)
# 71.3  19.9    2675    2018 newport                        (2, 915), (1, 897), (4, 779), (5, 707)
# 79.1  24.2    1431    2018 umag                           (1, 1143), (2, 758), (3, 445), (4, 264)
# 79.2  29.1    1627    2019 zhuhai                         (1, 951), (2, 408), (4, 331), (3, 312)

# 77.4  24.3    1460    2019 chengdu                        (1, 1396), (2, 650), (3, 377), (4, 348)
# 72.1  10.0    1191    2018 washington                     (3, 1187), (4, 538), (6, 337), (1, 283)
# 71.4  11.5    351     2018 toronto                        (1, 1541), (2, 592), (3, 65), (4, 15)

# 72.9  7.9     349     2019-08-31                          (1, 1534), (2, 974), (0, 819), (3, 160)
# 67.7  25.3    954     2018 us open r16 p1                 (3, 272), (2, 234), (4, 140), (5, 133)

# 68.6  26.2    459     sst petersburg 2018                 (2, 436), (1, 385), (3, 127), (4, 28)

# 65.7  17.2    327     opt lambda & tie & ups              (2, 387), (1, 233), (3, 196), (4, 59)


DATA = [
    {
        'location': TOKYO,
        'date': '2019-10-06',
        'matches': [

            # 2019-09-28
            {
                'round': 512,
                'players': [
                    YASUTAKA_UCHIYAMA,
                    STEVE_JOHNSON,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    YASUTAKA_UCHIYAMA: 2.30,
                    STEVE_JOHNSON: 1.57,
                }
            },
            {
                'round': 512,
                'players': [
                    TATSUMA_ITO,
                    PETER_GOJOWCZYK,
                ],
                'score': [(5, 7), (6, 1), (6, 4)],
                'odds': {
                    TATSUMA_ITO: 1.67,
                    PETER_GOJOWCZYK: 1.74,
                }
            },
            {
                'round': 512,
                'players': [
                    SOONWOO_KWON,
                    HENRI_LAAKSONEN,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    SOONWOO_KWON: 1.33,
                    HENRI_LAAKSONEN: 3.20
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    YOSUKE_WATANUKI,
                ],
                'score': [(4, 6), (6, 1), (6, 4)],
                'odds': {
                    ALEXEI_POPYRIN: 1.47,
                    YOSUKE_WATANUKI: 2.35
                }
            },
            {
                'round': 512,
                'players': [
                    JAMES_DUCKWORTH,
                    THOMAS_FABBIANO,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    JAMES_DUCKWORTH: 1.67,
                    THOMAS_FABBIANO: 1.91,
                }
            },
            {
                'round': 512,
                'players': [
                    JOHN_MILLMAN,
                    BRADLEY_KLAHN,
                ],
                'score': [(3, 6), (7, 6), (6, 2)],
                'odds': {
                    JOHN_MILLMAN: 1.43,
                    BRADLEY_KLAHN: 2.55,
                }
            },
            {
                'round': 512,
                'players': [
                    MARCEL_GRANOLLERS,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 1), (1, 6), (6, 2)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.71,
                    NICOLAS_JARRY: 1.91
                }
            },
            {
                'round': 512,
                'players': [
                    PABLO_ANDUJAR,
                    BRAYDEN_SCHNUR,
                ],
                'score': [(6, 0), (6, 0)],
                'odds': {
                    PABLO_ANDUJAR: 1.42,
                    BRAYDEN_SCHNUR: 2.45
                }
            },

            # 2019-09-29
            {
                'round': 256,
                'players': [
                    YASUTAKA_UCHIYAMA,
                    MARCEL_GRANOLLERS,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    YASUTAKA_UCHIYAMA: 2.05,
                    MARCEL_GRANOLLERS: 1.80,
                },
                'prediction': MARCEL_GRANOLLERS,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    JOHN_MILLMAN,
                    TATSUMA_ITO,
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    JOHN_MILLMAN: 1.34,
                    TATSUMA_ITO: 3.10,
                },
                'prediction': JOHN_MILLMAN,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    PABLO_ANDUJAR,
                    SOONWOO_KWON,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PABLO_ANDUJAR: 2.05,
                    SOONWOO_KWON: 1.72,
                },
                'prediction': SOONWOO_KWON,
                'bet': 3,
            },
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    JAMES_DUCKWORTH,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 1.72,
                    JAMES_DUCKWORTH: 2.00,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 1,
            },

            # 2019-09-30
            {
                'round': 32,
                'players': [
                    GO_SOEDA,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(4, 6), (7, 6), (6, 3)],
                'odds': {
                    GO_SOEDA: 3.60,
                    JAN_LENNARD_STRUFF: 1.28,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    LUCAS_POUILLE,
                    HUBERT_HURKACZ,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    LUCAS_POUILLE: 1.85,
                    HUBERT_HURKACZ: 1.95,
                },
                'prediction': LUCAS_POUILLE,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    MARIN_CILIC,
                    YUICHI_SUGITA,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MARIN_CILIC: 1.20,
                    YUICHI_SUGITA: 4.40,
                },
            },
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    JOAO_SOUSA,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.85,
                    JOAO_SOUSA: 1.95,
                },
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    HYEON_CHUNG,
                    LORENZO_SONEGO,
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    HYEON_CHUNG: 1.45,
                    LORENZO_SONEGO: 2.70,
                },
                'prediction': HYEON_CHUNG,
                'bet': 1,
            },

            # 2019-10-01
            {
                'round': 32,
                'players': [
                    REILLY_OPELKA,
                    TAYLOR_FRITZ,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    REILLY_OPELKA: 2.40,
                    TAYLOR_FRITZ: 1.55,
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    YASUTAKA_UCHIYAMA,
                    BENOIT_PAIRE,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    YASUTAKA_UCHIYAMA: 2.30,
                    BENOIT_PAIRE: 1.60,
                },
            },
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    PABLO_ANDUJAR,
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    GILLES_SIMON: 1.90,
                    PABLO_ANDUJAR: 1.90,
                },
            },
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    BORNA_CORIC,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    TARO_DANIEL: 4.20,
                    BORNA_CORIC: 1.22,
                },
                'prediction': BORNA_CORIC,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    RADU_ALBOT,
                    FILIP_KRAJINOVIC,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    RADU_ALBOT: 2.20,
                    FILIP_KRAJINOVIC: 1.65,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.09,
                    ALEXEI_POPYRIN: 7.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    DENIS_SHAPOVALOV,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.42,
                    MIOMIR_KECMANOVIC: 2.80,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JORDAN_THOMPSON,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    JORDAN_THOMPSON: 1.45,
                    JUAN_IGNACIO_LONDERO: 2.70,
                },
                'prediction': JORDAN_THOMPSON,
                'bet': 5,
            },

            # 2019-10-02
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(1, 6), (7, 6), (6, 0)],
                'odds': {
                    DAVID_GOFFIN: 1.70,
                    PABLO_CARRENO_BUSTA: 2.10,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    ADRIAN_MANNARINO,
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    JOHN_MILLMAN: 1.68,
                    ADRIAN_MANNARINO: 2.15,
                },
                'prediction': JOHN_MILLMAN,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    YASUTAKA_UCHIYAMA,
                    RADU_ALBOT,
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    YASUTAKA_UCHIYAMA: 2.40,
                    RADU_ALBOT: 1.55,
                },
                'prediction': RADU_ALBOT,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    LLOYD_HARRIS,
                    ALEX_DE_MINAUR,
                ],
                'score': [(6, 3), (6, 7), (7, 6)],
                'odds': {
                    LLOYD_HARRIS: 4.00,
                    ALEX_DE_MINAUR: 1.24,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    GO_SOEDA,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.03,
                    GO_SOEDA: 11.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    REILLY_OPELKA,
                    GILLES_SIMON,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 1.65,
                    GILLES_SIMON: 2.20,
                },
                'prediction': REILLY_OPELKA,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    LUCAS_POUILLE,
                    YOSHIHITO_NISHIOKA,
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    LUCAS_POUILLE: 1.85,
                    YOSHIHITO_NISHIOKA: 1.95,
                },
            },

            # 2019-10-03
            {
                'round': 16,
                'players': [
                    TARO_DANIEL,
                    JORDAN_THOMPSON,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    TARO_DANIEL: 2.50,
                    JORDAN_THOMPSON: 1.52,
                },
            },
            {
                'round': 16,
                'players': [
                    JOHN_MILLMAN,
                    LLOYD_HARRIS,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JOHN_MILLMAN: 1.55,
                    LLOYD_HARRIS: 2.40,
                },
            },
            {
                'round': 16,
                'players': [
                    DAVID_GOFFIN,
                    DENIS_SHAPOVALOV,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    DAVID_GOFFIN: 1.80,
                    DENIS_SHAPOVALOV: 2.00,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    HYEON_CHUNG,
                    MARIN_CILIC,
                ],
                'score': [(6, 4), (3, 6), (6, 1)],
                'odds': {
                    HYEON_CHUNG: 2.90,
                    MARIN_CILIC: 1.40,
                },
            },

            # 2019-10-04
            {
                'round': 8,
                'players': [
                    REILLY_OPELKA,
                    YASUTAKA_UCHIYAMA,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    REILLY_OPELKA: 1.55,
                    YASUTAKA_UCHIYAMA: 2.40,
                },
            },
            {
                'round': 8,
                'players': [
                    JOHN_MILLMAN,
                    TARO_DANIEL,
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    JOHN_MILLMAN: 1.42,
                    TARO_DANIEL: 2.80,
                },
                'prediction': JOHN_MILLMAN,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    NOVAK_DJOKOVIC,
                    LUCAS_POUILLE,
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.12,
                    LUCAS_POUILLE: 6.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    DAVID_GOFFIN,
                    HYEON_CHUNG,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.45,
                    HYEON_CHUNG: 2.70,
                },
            },

            # 2019-10-05
            {
                'round': 4,
                'players': [
                    JOHN_MILLMAN,
                    REILLY_OPELKA,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    JOHN_MILLMAN: 2.20,
                    REILLY_OPELKA: 1.65,
                },
                'prediction': REILLY_OPELKA,
                'bet': 4,
            },
            {
                'round': 4,
                'players': [
                    NOVAK_DJOKOVIC,
                    DAVID_GOFFIN,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.14,
                    DAVID_GOFFIN: 5.50,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 1,
            },

            # 2019-10-06
            {
                'round': 2,
                'players': [
                    NOVAK_DJOKOVIC,
                    JOHN_MILLMAN,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.02,
                    JOHN_MILLMAN: 12.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 6,
            }
        ]
    },

    {
        'location': BEIJING,
        'date': '2019-10-06',
        'matches': [

            # 2019-09-28
            {
                'round': 512,
                'players': [
                    DOMINIK_KOEPFER,
                    JASON_JUNG,
                ],
                'score': [(6, 3), (6, 7), (6, 4)],
                'odds': {
                    DOMINIK_KOEPFER: 1.50,
                    JASON_JUNG: 2.50
                }
            },
            {
                'round': 512,
                'players': [
                    VASEK_POSPISIL,
                    ANDREAS_SEPPI,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    VASEK_POSPISIL: 1.71,
                    ANDREAS_SEPPI: 2.00
                }
            },
            {
                'round': 512,
                'players': [
                    JEREMY_CHARDY,
                    FRANK_DANCEVIC,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 1.05,
                    FRANK_DANCEVIC: 6.55
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 3), (6, 7), (6, 1)],
                'odds': {
                    DAMIR_DZUMHUR: 2.05,
                    RICARDAS_BERANKIS: 1.63
                }
            },
            {
                'round': 512,
                'players': [
                    CAMERON_NORRIE,
                    YECONG_HE,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    CAMERON_NORRIE: 1.01,
                    YECONG_HE: 15.00
                }
            },
            {
                'round': 512,
                'players': [
                    BERNARD_TOMIC,
                    MARTON_FUCSOVICS,
                ],
                'score': [],
                'retired': True,
                'odds': {
                    BERNARD_TOMIC: 3.00,
                    MARTON_FUCSOVICS: 1.36
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_EVANS,
                    JIE_CUI,
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DANIEL_EVANS: 1.02,
                    JIE_CUI: 14.00,
                }
            },
            {
                'round': 512,
                'players': [
                    PABLO_CUEVAS,
                    DI_WU,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    PABLO_CUEVAS: 1.36,
                    DI_WU: 2.75
                }
            },

            # 2019-09-29
            {
                'round': 256,
                'players': [
                    JEREMY_CHARDY,
                    BERNARD_TOMIC,
                ],
                'score': [(2, 2)],
                'retired': True,
                'odds': {
                    JEREMY_CHARDY: 1.28,
                    BERNARD_TOMIC: 3.50,
                },
            },
            {
                'round': 256,
                'players': [
                    CAMERON_NORRIE,
                    DAMIR_DZUMHUR,
                ],
                'score': [(1, 6), (6, 3), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 1.52,
                    DAMIR_DZUMHUR: 2.40,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    PABLO_CUEVAS,
                    DOMINIK_KOEPFER,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    PABLO_CUEVAS: 1.87,
                    DOMINIK_KOEPFER: 1.87,
                },
            },
            {
                'round': 256,
                'players': [
                    DANIEL_EVANS,
                    VASEK_POSPISIL,
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    DANIEL_EVANS: 1.75,
                    VASEK_POSPISIL: 2.05,
                },
                'prediction': DANIEL_EVANS,
                'bet': 2,
            },

            # 2019-09-30
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    GRIGOR_DIMITROV,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    ANDREY_RUBLEV: 1.95,
                    GRIGOR_DIMITROV: 1.85,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    MARCO_CECCHINATO,
                ],
                'score': [(6, 7), (6, 3), (7, 6)],
                'odds': {
                    JEREMY_CHARDY: 1.28,
                    MARCO_CECCHINATO: 3.60,
                },
                'prediction': JEREMY_CHARDY,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    KAREN_KHACHANOV: 1.48,
                    PABLO_CUEVAS: 2.60,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    ZHIZHEN_ZHANG,
                    KYLE_EDMUND,
                ],
                'score': [(6, 4), (3, 6), (7, 6)],
                'odds': {
                    ZHIZHEN_ZHANG: 2.90,
                    KYLE_EDMUND: 1.40,
                },
                'prediction': KYLE_EDMUND,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    CHRISTIAN_GARIN,
                ],
                'score': [(7, 6), (1, 0)],
                'retired': True,
                'odds': {
                    CAMERON_NORRIE: 1.70,
                    CHRISTIAN_GARIN: 2.10,
                },
            },
            {
                'round': 32,
                'players': [
                    DANIEL_EVANS,
                    ZHE_LI,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DANIEL_EVANS: 1.16,
                    ZHE_LI: 5.00,
                },
                'prediction': DANIEL_EVANS,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.42,
                    FRANCES_TIAFOE: 2.80,
                },
            },

            # 2019-10-01
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.55,
                    ALBERT_RAMOS_VINOLAS: 2.40,
                },
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    JOHN_ISNER,
                    GAEL_MONFILS,
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    JOHN_ISNER: 2.15,
                    GAEL_MONFILS: 1.68,
                },
                'prediction': GAEL_MONFILS,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    ANDY_MURRAY,
                    MATTEO_BERRETTINI,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    ANDY_MURRAY: 2.50,
                    MATTEO_BERRETTINI: 1.52,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    GUIDO_PELLA,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.58,
                    GUIDO_PELLA: 2.35,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    FABIO_FOGNINI: 1.75,
                    MIKHAIL_KUKUSHKIN: 2.05,
                },
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    RICHARD_GASQUET,
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    DOMINIC_THIEM: 1.52,
                    RICHARD_GASQUET: 2.50,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    DUSAN_LAJOVIC,
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.26,
                    DUSAN_LAJOVIC: 3.80,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    ROBERTO_BAUTISTA_AGUT,
                ],
                'score': [(7, 6), (4, 1)],
                'retired': True,
                'odds': {
                    SAM_QUERREY: 3.80,
                    ROBERTO_BAUTISTA_AGUT: 1.26,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 0,  # refunded 4,
            },
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    FERNANDO_VERDASCO,
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.48,
                    FERNANDO_VERDASCO: 2.60,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 2,
            },

            # 2019-10-02
            {
                'round': 16,
                'players': [
                    ANDY_MURRAY,
                    CAMERON_NORRIE,
                ],
                'score': [(7, 6), (6, 7), (6, 1)],
                'odds': {
                    ANDY_MURRAY: 1.38,
                    CAMERON_NORRIE: 3.00,
                },
            },
            {
                'round': 16,
                'players': [
                    KAREN_KHACHANOV,
                    JEREMY_CHARDY,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    KAREN_KHACHANOV: 1.34,
                    JEREMY_CHARDY: 3.20,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    FABIO_FOGNINI,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 2.80,
                    ANDREY_RUBLEV: 1.42,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    ZHIZHEN_ZHANG,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    DOMINIC_THIEM: 1.14,
                    ZHIZHEN_ZHANG: 5.50,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 3,
            },

            # 2018-10-03
            {
                'round': 16,
                'players': [
                    JOHN_ISNER,
                    DANIEL_EVANS,
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    JOHN_ISNER: 1.55,
                    DANIEL_EVANS: 2.40,
                },
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.60,
                    NIKOLOZ_BASILASHVILI: 2.30,
                },
            },
            {
                'round': 16,
                'players': [
                    SAM_QUERREY,
                    DIEGO_SCHWARTZMAN,
                ],
                'score': [(7, 6), (6, 7), (6, 3)],
                'odds': {
                    SAM_QUERREY: 2.50,
                    DIEGO_SCHWARTZMAN: 1.52,
                },
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    FELIX_AUGER_ALIASSIME,
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.48,
                    FELIX_AUGER_ALIASSIME: 2.60,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 1,
            },

            # 2019-10-04
            {
                'round': 8,
                'players': [
                    KAREN_KHACHANOV,
                    FABIO_FOGNINI,
                ],
                'score': [(3, 6), (6, 3), (6, 1)],
                'odds': {
                    KAREN_KHACHANOV: 1.60,
                    FABIO_FOGNINI: 2.30,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    ANDY_MURRAY,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    DOMINIC_THIEM: 1.42,
                    ANDY_MURRAY: 2.80,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    JOHN_ISNER,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.75,
                    JOHN_ISNER: 2.05,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    ALEXANDER_ZVEREV,
                    SAM_QUERREY,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.26,
                    SAM_QUERREY: 3.80,
                },
            },

            # 2019-10-05
            {
                'round': 4,
                'players': [
                    DOMINIC_THIEM,
                    KAREN_KHACHANOV,
                ],
                'score': [(2, 6), (7, 6), (7, 5)],
                'odds': {
                    DOMINIC_THIEM: 1.55,
                    KAREN_KHACHANOV: 2.40,
                },
            },
            {
                'round': 4,
                'players': [
                    STEFANOS_TSITSIPAS,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 2.25,
                    ALEXANDER_ZVEREV: 1.62,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 2,
            },

            # 2019-10-06
            {
                'round': 2,
                'players': [
                    DOMINIC_THIEM,
                    STEFANOS_TSITSIPAS,
                ],
                'score': [(3, 6), (6, 4), (6, 1)],
                'odds': {
                    DOMINIC_THIEM: 1.95,
                    STEFANOS_TSITSIPAS: 1.85,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 2,
            }
        ]
    },

    {
        'location': SHANGAI,
        'date': '2019-10-13',
        'matches': [

            # 2019-10-05
            {
                'round': 512,
                'players': [
                    MARCEL_GRANOLLERS,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MARCEL_GRANOLLERS: 2.37,
                    ALEXEI_POPYRIN: 1.62
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    TATSUMA_ITO,
                ],
                'score': [(4, 6), (7, 6), (6, 2)],
                'odds': {
                    DAMIR_DZUMHUR: 1.41,
                    TATSUMA_ITO: 3.03
                }
            },
            {
                'round': 512,
                'players': [
                    THOMAS_FABBIANO,
                    RUNHAO_HUA,
                ],
                'score': [(3, 6), (6, 0), (7, 6)],
                'odds': {
                    THOMAS_FABBIANO: 1.15,
                    RUNHAO_HUA: 6.00
                }
            },
            {
                'round': 512,
                'players': [
                    DOMINIK_KOEPFER,
                    YECONG_HE
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    DOMINIK_KOEPFER: 1.06,
                    YECONG_HE: 10.47
                }
            },
            {
                'round': 512,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 3), (2, 6), (6, 3)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.38,
                    PETER_GOJOWCZYK: 3.19
                }
            },
            {
                'round': 512,
                'players': [
                    BRADLEY_KLAHN,
                    NICOLAS_JARRY
                ],
                'score': [(7, 6), (3, 6), (7, 5)],
                'odds': {
                    BRADLEY_KLAHN: 1.61,
                    NICOLAS_JARRY: 2.40
                }
            },
            {
                'round': 512,
                'players': [
                    JEREMY_CHARDY,
                    ASLAN_KARATSEV
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    JEREMY_CHARDY: 1.09,
                    ASLAN_KARATSEV: 8.16
                }
            },
            {
                'round': 512,
                'players': [
                    CAMERON_NORRIE,
                    BRAYDEN_SCHNUR
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    CAMERON_NORRIE: 1.22,
                    BRAYDEN_SCHNUR: 4.60
                }
            },
            {
                'round': 512,
                'players': [
                    MARCO_CECCHINATO,
                    FAJING_SUN
                ],
                'score': [(6, 3), (6, 7), (6, 2)],
                'odds': {
                    MARCO_CECCHINATO: 1.13,
                    FAJING_SUN: 6.50
                }
            },
            {
                'round': 512,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    VIKTOR_TROICKI
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.53,
                    VIKTOR_TROICKI: 2.61
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXANDER_BUBLIK,
                    GONCALO_OLIVEIRA
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.13,
                    GONCALO_OLIVEIRA: 6.36
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_EVANS,
                    BERNARD_TOMIC
                ],
                'score': [(6, 2), (3, 6), (6, 0)],
                'odds': {
                    DANIEL_EVANS: 1.22,
                    BERNARD_TOMIC: 4.58
                }
            },
            {
                'round': 512,
                'players': [
                    VASEK_POSPISIL,
                    ADRIAN_MANNARINO
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    VASEK_POSPISIL: 2.27,
                    ADRIAN_MANNARINO: 1.67
                }
            },
            {
                'round': 512,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    DI_WU
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.09,
                    DI_WU: 8.42
                }
            },

            # 2019-10-06
            {
                'round': 256,
                'players': [
                    VASEK_POSPISIL,
                    MARCEL_GRANOLLERS
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    VASEK_POSPISIL: 1.74,
                    MARCEL_GRANOLLERS: 2.15
                }
            },
            {
                'round': 256,
                'players': [
                    CAMERON_NORRIE,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 1.33,
                    THOMAS_FABBIANO: 3.52
                }
            },
            {
                'round': 256,
                'players': [
                    MARCO_CECCHINATO,
                    DAMIR_DZUMHUR
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    MARCO_CECCHINATO: 2.64,
                    DAMIR_DZUMHUR: 1.52
                }
            },
            {
                'round': 256,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 2.16,
                    BRADLEY_KLAHN: 1.74
                }
            },
            {
                'round': 256,
                'players': [
                    ALEXANDER_BUBLIK,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.89,
                    YOSHIHITO_NISHIOKA: 1.97
                }
            },
            {
                'round': 256,
                'players': [
                    JEREMY_CHARDY,
                    DANIEL_EVANS
                ],
                'score': [(2, 6), (6, 4), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 2.17,
                    DANIEL_EVANS: 1.73
                }
            },
            {
                'round': 256,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    DOMINIK_KOEPFER
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.28,
                    DOMINIK_KOEPFER: 3.86
                }
            },
            {
                'round': 64,
                'players': [
                    JOAO_SOUSA,
                    FILIP_KRAJINOVIC
                ],
                'score': [(2, 6), (6, 4), (7, 6)],
                'odds': {
                    JOAO_SOUSA: 1.91,
                    FILIP_KRAJINOVIC: 2.00
                }
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    ZHIZHEN_ZHANG
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 1.31,
                    ZHIZHEN_ZHANG: 3.81
                }
            },
            {
                'round': 64,
                'players': [
                    TAYLOR_FRITZ,
                    FERNANDO_VERDASCO
                ],
                'score': [(7, 6), (6, 7), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 1.93,
                    FERNANDO_VERDASCO: 1.98
                }
            },
            {
                'round': 64,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    RADU_ALBOT
                ],
                'score': [(4, 6), (6, 1), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.75,
                    RADU_ALBOT: 2.21
                }
            },

            # 2019-07-07
            {
                'round': 64,
                'players': [
                    CAMERON_NORRIE,
                    GILLES_SIMON
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    CAMERON_NORRIE: 1.85,
                    GILLES_SIMON: 1.95
                },
                'prediction': CAMERON_NORRIE,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    MARIN_CILIC,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 3.10,
                    MARIN_CILIC: 1.38,
                },
                'prediction': MARIN_CILIC,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.48,
                    FRANCES_TIAFOE: 2.60,
                },
            },
            {
                'round': 64,
                'players': [
                    BENOIT_PAIRE,
                    MARCO_CECCHINATO,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    BENOIT_PAIRE: 1.70,
                    MARCO_CECCHINATO: 2.10,
                },
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    SAM_QUERREY,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    FABIO_FOGNINI: 1.95,
                    SAM_QUERREY: 1.85,
                },
            },
            {
                'round': 64,
                'players': [
                    VASEK_POSPISIL,
                    DIEGO_SCHWARTZMAN,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    VASEK_POSPISIL: 3.00,
                    DIEGO_SCHWARTZMAN: 1.38,
                },
            },
            {
                'round': 64,
                'players': [
                    CHRISTIAN_GARIN,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    CHRISTIAN_GARIN: 2.05,
                    PABLO_CUEVAS: 1.75,
                },
                'prediction': PABLO_CUEVAS,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    JEREMY_CHARDY,
                    KYLE_EDMUND,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    JEREMY_CHARDY: 1.95,
                    KYLE_EDMUND: 1.85,
                },
            },
            {
                'round': 64,
                'players': [
                    GAEL_MONFILS,
                    LORENZO_SONEGO,
                ],
                'score': [(7, 5), (6, 7), (6, 3)],
                'odds': {
                    GAEL_MONFILS: 1.28,
                    LORENZO_SONEGO: 3.60,
                },
                'prediction': GAEL_MONFILS,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.95,
                    MIOMIR_KECMANOVIC: 1.85,
                },
            },
            {
                'round': 64,
                'players': [
                    ANDY_MURRAY,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(2, 6), (6, 2), (6, 3)],
                'odds': {
                    ANDY_MURRAY: 1.30,
                    JUAN_IGNACIO_LONDERO: 3.40,
                },
                'prediction': ANDY_MURRAY,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    ZE_ZHANG,
                ],
                'score': [(6, 3), (2, 6), (6, 4)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.08,
                    ZE_ZHANG: 7.50,
                },
            },

            # 2019-10-08
            {
                'round': 64,
                'players': [
                    JOHN_ISNER,
                    ALEX_DE_MINAUR,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JOHN_ISNER: 2.15,
                    ALEX_DE_MINAUR: 1.68,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    LUCAS_POUILLE,
                    ZHE_LI,
                ],
                'score': [(6, 7), (6, 4), (6, 4)],
                'odds': {
                    LUCAS_POUILLE: 1.10,
                    ZHE_LI: 6.50,
                },
            },
            {
                'round': 64,
                'players': [
                    REILLY_OPELKA,
                    DUSAN_LAJOVIC,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    REILLY_OPELKA: 1.42,
                    DUSAN_LAJOVIC: 2.80,
                },
                'prediction': REILLY_OPELKA,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ANDREY_RUBLEV,
                    BORNA_CORIC,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ANDREY_RUBLEV: 1.60,
                    BORNA_CORIC: 2.30,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    JOHN_MILLMAN,
                    GUIDO_PELLA,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    JOHN_MILLMAN: 1.80,
                    GUIDO_PELLA: 1.95,
                },
                'prediction': JOHN_MILLMAN,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    RICHARD_GASQUET,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    DAVID_GOFFIN: 1.40,
                    RICHARD_GASQUET: 3.22,
                }
            },
            {
                'round': 64,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(7, 6), (4, 0)],
                'retired': True,
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.80,
                    ALEXANDER_BUBLIK: 2.00,
                },
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 0,  # refunded 2,
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    BENOIT_PAIRE,
                ],
                'score': [(6, 4), (1, 6), (6, 1)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.75,
                    BENOIT_PAIRE: 2.05,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    MATTEO_BERRETTINI,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    MATTEO_BERRETTINI: 1.48,
                    JAN_LENNARD_STRUFF: 2.60,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    GAEL_MONFILS,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    HUBERT_HURKACZ: 2.70,
                    GAEL_MONFILS: 1.45,
                },
                'prediction': GAEL_MONFILS,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    VASEK_POSPISIL,
                    JOAO_SOUSA
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    VASEK_POSPISIL: 1.81,
                    JOAO_SOUSA: 2.11
                }
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    ANDY_MURRAY
                ],
                'score': [(7, 6), (2, 6), (7, 6)],
                'odds': {
                    FABIO_FOGNINI: 1.81,
                    ANDY_MURRAY: 2.12
                }
            },
            {
                'round': 32,
                'players': [
                    DANIIL_MEDVEDEV,
                    CAMERON_NORRIE
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.11,
                    CAMERON_NORRIE: 8.05
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    ROGER_FEDERER: 1.07,
                    ALBERT_RAMOS_VINOLAS: 11.49
                }
            },

            # 2019-10-09
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    FELIX_AUGER_ALIASSIME,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.40,
                    FELIX_AUGER_ALIASSIME: 2.90,
                },
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    CHRISTIAN_GARIN,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.28,
                    CHRISTIAN_GARIN: 3.60,
                },
            },
            {
                'round': 32,
                'players': [
                    JOHN_ISNER,
                    LUCAS_POUILLE,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    JOHN_ISNER: 1.55,
                    LUCAS_POUILLE: 2.40,
                },
                'prediction': JOHN_ISNER,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    REILLY_OPELKA,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.65,
                    REILLY_OPELKA: 2.20,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    TAYLOR_FRITZ,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    KAREN_KHACHANOV: 1.45,
                    TAYLOR_FRITZ: 2.70,
                },
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    JEREMY_CHARDY,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.30,
                    JEREMY_CHARDY: 3.40,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    JOHN_MILLMAN,
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    ANDREY_RUBLEV: 1.55,
                    JOHN_MILLMAN: 2.40,
                },
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    DENIS_SHAPOVALOV,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.10,
                    DENIS_SHAPOVALOV: 6.50,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(6, 2), (3, 0)],
                'retired': True,
                'odds': {
                    DAVID_GOFFIN: 1.24,
                    MIKHAIL_KUKUSHKIN: 4.00,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 0,  # refunded 2,
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    DOMINIC_THIEM: 1.40,
                    PABLO_CARRENO_BUSTA: 2.90,
                },
            },

            # 2019-10-10
            {
                'round': 16,
                'players': [
                    FABIO_FOGNINI,
                    KAREN_KHACHANOV,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    FABIO_FOGNINI: 2.60,
                    KAREN_KHACHANOV: 1.45,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    DANIIL_MEDVEDEV,
                    VASEK_POSPISIL,
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.07,
                    VASEK_POSPISIL: 7.50,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    ROBERTO_BAUTISTA_AGUT,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 1.68,
                    ROBERTO_BAUTISTA_AGUT: 2.10,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    JOHN_ISNER,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.12,
                    JOHN_ISNER: 6.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 8,
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    HUBERT_HURKACZ,
                ],
                'score': [(7, 5), (3, 6), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.34,
                    HUBERT_HURKACZ: 3.10,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    DAVID_GOFFIN,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.24,
                    DAVID_GOFFIN: 4.00,
                },
                'prediction': ROGER_FEDERER,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 1.24,
                    NIKOLOZ_BASILASHVILI: 4.00,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 0), (7, 6)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.60,
                    ANDREY_RUBLEV: 2.40,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 2,
            },

            # 2019-10-11
            {
                'round': 8,
                'players': [
                    DANIIL_MEDVEDEV,
                    FABIO_FOGNINI,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.20,
                    FABIO_FOGNINI: 4.40,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    NOVAK_DJOKOVIC,
                ],
                'score': [(3, 6), (7, 5), (6, 3)],
                'odds': {
                    STEFANOS_TSITSIPAS: 6.00,
                    NOVAK_DJOKOVIC: 1.12,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 5,
            },
            {
                'round': 8,
                'players': [
                    ALEXANDER_ZVEREV,
                    ROGER_FEDERER,
                ],
                'score': [(6, 3), (6, 7), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 2.70,
                    ROGER_FEDERER: 1.45,
                },
                'prediction': ROGER_FEDERER,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    DOMINIC_THIEM,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 2.50,
                    DOMINIC_THIEM: 1.52,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 2,
            },

            # 2019-10-12
            {
                'round': 4,
                'players': [
                    DANIIL_MEDVEDEV,
                    STEFANOS_TSITSIPAS,
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.40,
                    STEFANOS_TSITSIPAS: 2.90,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 1,
            },
            {
                'round': 4,
                'players': [
                    ALEXANDER_ZVEREV,
                    MATTEO_BERRETTINI,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.60,
                    MATTEO_BERRETTINI: 2.30,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 4,
            },

            # 2019-10-13
            {
                'round': 2,
                'players': [
                    DANIIL_MEDVEDEV,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.52,
                    ALEXANDER_ZVEREV: 2.50,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 6,
            }
        ]
    },

    {
        'location': MOSCOW,
        'date': '2019-10-20',
        'matches': [

            # 2019-10-12
            {
                'round': 512,
                'players': [
                    FILIP_HORANSKY,
                    EVGENY_KARLOVSKIY
                ],
                'score': [(4, 6), (6, 3), (6, 0)],
                'odds': {
                    FILIP_HORANSKY: 1.76,
                    EVGENY_KARLOVSKIY: 2.09
                }
            },
            {
                'round': 512,
                'players': [
                    RUDOLF_MOLLEKER,
                    MAXIME_JANVIER
                ],
                'score': [(4, 6), (6, 1), (6, 3)],
                'odds': {
                    RUDOLF_MOLLEKER: 3.89,
                    MAXIME_JANVIER: 1.27
                }
            },
            {
                'round': 512,
                'players': [
                    SEBASTIAN_OFNER,
                    MIRZA_BASIC
                ],
                'score': [(7, 6), (3, 6), (6, 3)],
                'odds': {
                    SEBASTIAN_OFNER: 1.92,
                    MIRZA_BASIC: 1.90
                }
            },
            {
                'round': 512,
                'players': [
                    NIKOLA_MILOJEVIC,
                    ROBERTO_MARCORA,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    NIKOLA_MILOJEVIC: 2.00,
                    ROBERTO_MARCORA: 1.83
                }
            },
            {
                'round': 512,
                'players': [
                    LUKAS_ROSOL,
                    ROMAN_SAFIULLIN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    LUKAS_ROSOL: 1.74,
                    ROMAN_SAFIULLIN: 2.12
                }
            },
            {
                'round': 512,
                'players': [
                    ARTEM_DUBRIVNYY,
                    ILYA_IVASHKA
                ],
                'score': [(5, 7), (6, 2), (6, 2)],
                'odds': {
                    ARTEM_DUBRIVNYY: 6.23,
                    ILYA_IVASHKA: 1.13
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    ALEXEY_VATUTIN
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    DAMIR_DZUMHUR: 1.40,
                    ALEXEY_VATUTIN: 2.98
                }
            },
            {
                'round': 512,
                'players': [
                    EGOR_GERASIMOV,
                    ELLIOT_BENCHETRIT
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    EGOR_GERASIMOV: 1.08,
                    ELLIOT_BENCHETRIT: 7.99
                }
            },

            # 2019-10-13
            {
                'round': 256,
                'players': [
                    EGOR_GERASIMOV,
                    RUDOLF_MOLLEKER,
                ],
                'score': [(6, 3), (4, 6), (6, 3)],
                'odds': {
                    EGOR_GERASIMOV: 1.14,
                    RUDOLF_MOLLEKER: 5.50,
                },
                'prediction': EGOR_GERASIMOV,
                'bet': 4,
            },
            {
                'round': 256,
                'players': [
                    ARTEM_DUBRIVNYY,
                    FILIP_HORANSKY,
                ],
                'score': [(6, 4, (7, 5))],
                'odds': {
                    ARTEM_DUBRIVNYY: 2.80,
                    FILIP_HORANSKY: 1.40,
                },
                'prediction': FILIP_HORANSKY,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    DAMIR_DZUMHUR,
                    SEBASTIAN_OFNER,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DAMIR_DZUMHUR: 1.28,
                    SEBASTIAN_OFNER: 3.60,
                },
                'prediction': DAMIR_DZUMHUR,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    LUKAS_ROSOL,
                    NIKOLA_MILOJEVIC,
                ],
                'score': [(7, 5), (6, 7), (6, 3)],
                'odds': {
                    LUKAS_ROSOL: 1.58,
                    NIKOLA_MILOJEVIC: 2.35,
                },
                'prediction': LUKAS_ROSOL,
                'bet': 4,
            },

            # 2019-10-14
            {
                'round': 256,
                'players': [
                    ANDREAS_SEPPI,
                    CHRISTIAN_GARIN,
                ],
                'score': [(3, 6), (7, 6), (7, 6)],
                'odds': {
                    ANDREAS_SEPPI: 1.95,
                    CHRISTIAN_GARIN: 1.85,
                },
            },
            {
                'round': 256,
                'players': [
                    LUKAS_ROSOL,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 7), (7, 6), (6, 3)],
                'odds': {
                    LUKAS_ROSOL: 2.10,
                    JUAN_IGNACIO_LONDERO: 1.70,
                },
            },
            {
                'round': 32,
                'players': [
                    ADRIAN_MANNARINO,
                    DAMIR_DZUMHUR,
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    ADRIAN_MANNARINO: 1.80,
                    DAMIR_DZUMHUR: 2.00,
                },
            },

            # 2019-10-15
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 2), (4, 6), (6, 3)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 3.40,
                    RICARDAS_BERANKIS: 1.30,
                },
                'prediction': RICARDAS_BERANKIS,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ARTEM_DUBRIVNYY,
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.20,
                    ARTEM_DUBRIVNYY: 4.40,
                },
            },
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    EVGENY_DONSKOY,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.52,
                    EVGENY_DONSKOY: 2.50,
                },
                'prediction': MIKHAIL_KUKUSHKIN,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    PIERRE_HUGUES_HERBERT,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.62,
                    PIERRE_HUGUES_HERBERT: 2.25,
                },
                'prediction': PHILIPP_KOHLSCHREIBER,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JEREMY_CHARDY: 1.38,
                    NICOLAS_JARRY: 3.00,
                },
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(6, 1), (3, 6), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 1.36,
                    ALEXANDER_BUBLIK: 3.10,
                },
            },
            {
                'round': 32,
                'players': [
                    IVO_KARLOVIC,
                    ALJAZ_BEDENE,
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    IVO_KARLOVIC: 3.10,
                    ALJAZ_BEDENE: 1.36,
                },
            },

            # 2019-10-16
            {
                'round': 32,
                'players': [
                    EGOR_GERASIMOV,
                    THOMAS_FABBIANO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    EGOR_GERASIMOV: 1.26,
                    THOMAS_FABBIANO: 3.80,
                },
                'prediction': EGOR_GERASIMOV,
                'bet': 9,
            },
            {
                'round': 16,
                'players': [
                    ANDREAS_SEPPI,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'score': [(5, 7), (6, 1), (6, 3)],
                'odds': {
                    ANDREAS_SEPPI: 1.36,
                    ROBERTO_CARBALLES_BAENA: 3.10,
                },
                'prediction': ANDREAS_SEPPI,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    ALEN_AVIDZBA,
                    ALIBEK_KACHMAZOV,
                ],
                'score': [(6, 1), (4, 6), (6, 1)],
                'odds': {
                    ALEN_AVIDZBA: 1.34,
                    ALIBEK_KACHMAZOV: 3.20,
                },
            },
            {
                'round': 16,
                'players': [
                    ADRIAN_MANNARINO,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    ADRIAN_MANNARINO: 1.52,
                    MIKHAIL_KUKUSHKIN: 2.50,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    DUSAN_LAJOVIC,
                    LUKAS_ROSOL,
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 1.68,
                    LUKAS_ROSOL: 2.15,
                },
                'prediction': DUSAN_LAJOVIC,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    KAREN_KHACHANOV,
                    PHILIPP_KOHLSCHREIBER,
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    KAREN_KHACHANOV: 1.30,
                    PHILIPP_KOHLSCHREIBER: 3.40,
                },
            },

            # 2019-10-17
            {
                'round': 16,
                'players': [
                    NIKOLA_MILOJEVIC,
                    ALEN_AVIDZBA,
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    NIKOLA_MILOJEVIC: 1.24,
                    ALEN_AVIDZBA: 4.00,
                },
                'prediction': NIKOLA_MILOJEVIC,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    EGOR_GERASIMOV,
                ],
                'score': [(7, 6), (6, 7), (6, 2)],
                'odds': {
                    ANDREY_RUBLEV: 1.45,
                    EGOR_GERASIMOV: 2.70,
                },
            },
            {
                'round': 16,
                'players': [
                    JEREMY_CHARDY,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 1.62,
                    MIOMIR_KECMANOVIC: 2.25,
                },
                'prediction': JEREMY_CHARDY,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    MARIN_CILIC,
                    IVO_KARLOVIC,
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    MARIN_CILIC: 1.30,
                    IVO_KARLOVIC: 3.40,
                },
                'prediction': MARIN_CILIC,
                'bet': 1,
            },

            # 2019-10-18
            {
                'round': 8,
                'players': [
                    ADRIAN_MANNARINO,
                    DUSAN_LAJOVIC,
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    ADRIAN_MANNARINO: 1.55,
                    DUSAN_LAJOVIC: 2.40,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    ANDREAS_SEPPI,
                    KAREN_KHACHANOV,
                ],
                'score': [(3, 6), (6, 3), (6, 3)],
                'odds': {
                    ANDREAS_SEPPI: 3.80,
                    KAREN_KHACHANOV: 1.26,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    MARIN_CILIC,
                    JEREMY_CHARDY,
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    MARIN_CILIC: 1.65,
                    JEREMY_CHARDY: 2.20,
                },
                'prediction': MARIN_CILIC,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    ANDREY_RUBLEV,
                    NIKOLA_MILOJEVIC,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 1.08,
                    NIKOLA_MILOJEVIC: 7.50,
                },
            },

            # 2019-10-19
            {
                'round': 4,
                'players': [
                    ADRIAN_MANNARINO,
                    ANDREAS_SEPPI,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ADRIAN_MANNARINO: 1.60,
                    ANDREAS_SEPPI: 2.30,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 1,
            },
            {
                'round': 4,
                'players': [
                    ANDREY_RUBLEV,
                    MARIN_CILIC,
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 1.60,
                    MARIN_CILIC: 2.30,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 7,
            },

            # 2019-10-20
            {
                'round': 2,
                'players': [
                    ANDREY_RUBLEV,
                    ADRIAN_MANNARINO,
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    ANDREY_RUBLEV: 1.28,
                    ADRIAN_MANNARINO: 3.60,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 6,
            }
        ]
    },

    {
        'location': STOCKHOLM,
        'date': '2019-10-20',
        'matches': [

            # 2019-10-13
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    TOBIAS_KAMKE,
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 1.34,
                    TOBIAS_KAMKE: 3.20,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    LUCAS_RENARD,
                    ERNESTS_GULBIS,
                ],
                'score': [(7, 6), (0, 0)],
                'retired': True,
                'odds': {
                    LUCAS_RENARD: 7.00,
                    ERNESTS_GULBIS: 1.09,
                },
            },
            {
                'round': 512,
                'players': [
                    YUICHI_SUGITA,
                    ENZO_COUACAUD,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    YUICHI_SUGITA: 1.85,
                    ENZO_COUACAUD: 1.95,
                },
                'prediction': YUICHI_SUGITA,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    MARKUS_ERIKSSON,
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    TOMMY_PAUL: 1.20,
                    MARKUS_ERIKSSON: 4.40,
                },
                'prediction': TOMMY_PAUL,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    OSCAR_OTTE,
                    TOMMY_ROBREDO,
                ],
                'score': [(6, 0), (4, 6), (6, 1)],
                'odds': {
                    OSCAR_OTTE: 1.38,
                    TOMMY_ROBREDO: 3.00,
                },
                'prediction': OSCAR_OTTE,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    HYEON_CHUNG,
                ],
                'score': [(3, 6), (6, 3), (6, 3)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 3.50,
                    HYEON_CHUNG: 1.28,
                },
                'prediction': HYEON_CHUNG,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    DENNIS_NOVAK,
                    VIKTOR_TROICKI,
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    DENNIS_NOVAK: 1.60,
                    VIKTOR_TROICKI: 2.25,
                },
                'prediction': DENNIS_NOVAK,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    GIANLUCA_MAGER,
                    SIMON_YITBAREK,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    GIANLUCA_MAGER: 1.05,
                    SIMON_YITBAREK: 8.50,
                },
                'prediction': GIANLUCA_MAGER,
                'bet': 4,
            },

            # 2019-10-14
            {
                'round': 256,
                'players': [
                    TOMMY_PAUL,
                    LUCAS_RENARD,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    TOMMY_PAUL: 1.02,
                    LUCAS_RENARD: 12.00,
                },
            },
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    YUICHI_SUGITA,
                ],
                'score': [(1, 6), (6, 2), (6, 3)],
                'odds': {
                    ALEXEI_POPYRIN: 1.34,
                    YUICHI_SUGITA: 3.20,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    DENNIS_NOVAK,
                    GIANLUCA_MAGER,
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    DENNIS_NOVAK: 1.40,
                    GIANLUCA_MAGER: 2.90,
                },
            },
            {
                'round': 256,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    OSCAR_OTTE,
                ],
                'score': [(6, 4), (4, 6), (6, 1)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 1.75,
                    OSCAR_OTTE: 2.05,
                },
                'prediction': CEDRIC_MARCEL_STEBE,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    STEFANO_TRAVAGLIA,
                    REILLY_OPELKA,
                ],
                'score': [(7, 5), (4, 6), (6, 4)],
                'odds': {
                    STEFANO_TRAVAGLIA: 3.80,
                    REILLY_OPELKA: 1.26,
                },
            },
            {
                'round': 32,
                'players': [
                    DANIEL_EVANS,
                    BERNARD_TOMIC,
                ],
                'score': [(6, 4), (1, 6), (6, 3)],
                'odds': {
                    DANIEL_EVANS: 1.26,
                    BERNARD_TOMIC: 3.80,
                },
                'prediction': DANIEL_EVANS,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JANKO_TIPSAREVIC,
                    CORENTIN_MOUTET,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    JANKO_TIPSAREVIC: 2.80,
                    CORENTIN_MOUTET: 1.42,
                },
            },

            # 2019-10-15
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    RADU_ALBOT,
                ],
                'score': [(3, 6), (6, 4), (6, 1)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.10,
                    RADU_ALBOT: 1.70,
                },
                'prediction': RADU_ALBOT,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JOHN_MILLMAN,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.58,
                    JOHN_MILLMAN: 2.35,
                },
            },
            {
                'round': 32,
                'players': [
                    TOMMY_PAUL,
                    PABLO_ANDUJAR,
                ],
                'score': [(5, 7), (6, 1), (6, 1)],
                'odds': {
                    TOMMY_PAUL: 1.45,
                    PABLO_ANDUJAR: 2.70,
                },
                'prediction': TOMMY_PAUL,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    DENNIS_NOVAK,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    SAM_QUERREY: 1.58,
                    DENNIS_NOVAK: 2.35,
                },
                'prediction': SAM_QUERREY,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    BRAYDEN_SCHNUR,
                ],
                'score': [(6, 2), (3, 6), (6, 1)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 1.28,
                    BRAYDEN_SCHNUR: 3.60,
                },
                'prediction': CEDRIC_MARCEL_STEBE,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    YUICHI_SUGITA,
                    ELIAS_YMER,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    YUICHI_SUGITA: 1.75,
                    ELIAS_YMER: 2.05,
                },
                'prediction': YUICHI_SUGITA,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ALEXEI_POPYRIN,
                    OSCAR_OTTE,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 1.45,
                    OSCAR_OTTE: 2.70,
                },
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    CASPER_RUUD,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.40,
                    CASPER_RUUD: 2.90,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 5,
            },

            # 2019-10-16
            {
                'round': 16,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    TAYLOR_FRITZ,
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.25,
                    TAYLOR_FRITZ: 1.62,
                },
            },
            {
                'round': 32,
                'players': [
                    MIKAEL_YMER,
                    JOAO_SOUSA,
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    MIKAEL_YMER: 1.62,
                    JOAO_SOUSA: 2.25,
                },
                'prediction': MIKAEL_YMER,
                'bet': 7,
            },
            {
                'round': 16,
                'players': [
                    SAM_QUERREY,
                    GRIGOR_DIMITROV,
                ],
                'score': [(6, 7), (6, 3), (7, 6)],
                'odds': {
                    SAM_QUERREY: 2.30,
                    GRIGOR_DIMITROV: 1.60,
                },
            },
            {
                'round': 16,
                'players': [
                    FILIP_KRAJINOVIC,
                    DANIEL_EVANS,
                ],
                'score': [(7, 5), (2, 6), (6, 3)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.75,
                    DANIEL_EVANS: 2.05,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 1,
            },

            # 2019-10-17
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    GIANLUCA_MAGER,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.09,
                    GIANLUCA_MAGER: 7.00,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    YUICHI_SUGITA,
                    STEFANO_TRAVAGLIA,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    YUICHI_SUGITA: 2.05,
                    STEFANO_TRAVAGLIA: 1.75,
                },
                'prediction': STEFANO_TRAVAGLIA,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    JANKO_TIPSAREVIC,
                    FABIO_FOGNINI,
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    JANKO_TIPSAREVIC: 4.00,
                    FABIO_FOGNINI: 1.24,
                },
                'prediction': FABIO_FOGNINI,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    DENIS_SHAPOVALOV,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.36,
                    ALEXEI_POPYRIN: 3.10,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 6,
            },
            {
                'round': 16,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    MIKAEL_YMER,
                ],
                'score': [(6, 0), (7, 6)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 3.80,
                    MIKAEL_YMER: 1.26,
                },
                'prediction': MIKAEL_YMER,
                'bet': 3,
            },

            # 2019-10-18
            {
                'round': 8,
                'players': [
                    FILIP_KRAJINOVIC,
                    YOSHIHITO_NISHIOKA,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.65,
                    YOSHIHITO_NISHIOKA: 2.20,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 11,
            },
            {
                'round': 8,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    SAM_QUERREY,
                ],
                'score': [(4, 6), (6, 1), (6, 4)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.70,
                    SAM_QUERREY: 2.10,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    DENIS_SHAPOVALOV,
                    CEDRIC_MARCEL_STEBE,
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.20,
                    CEDRIC_MARCEL_STEBE: 4.40,
                },
            },
            {
                'round': 8,
                'players': [
                    YUICHI_SUGITA,
                    JANKO_TIPSAREVIC,
                ],
                'score': [(6, 2), (4, 6), (7, 6)],
                'odds': {
                    YUICHI_SUGITA: 1.95,
                    JANKO_TIPSAREVIC: 1.85,
                },
                'prediction': JANKO_TIPSAREVIC,
                'bet': 4,
            },

            # 2019-10-19
            {
                'round': 4,
                'players': [
                    FILIP_KRAJINOVIC,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(4, 6), (6, 3), (6, 3)],
                'odds': {
                    FILIP_KRAJINOVIC: 2.25,
                    PABLO_CARRENO_BUSTA: 1.62,
                },
            },
            {
                'round': 4,
                'players': [
                    DENIS_SHAPOVALOV,
                    YUICHI_SUGITA,
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.14,
                    YUICHI_SUGITA: 5.50,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },

            # 2019-10-20
            {
                'round': 2,
                'players': [
                    DENIS_SHAPOVALOV,
                    FILIP_KRAJINOVIC,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.42,
                    FILIP_KRAJINOVIC: 2.80,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            }
        ],
    },

    {
        'location': ANTWERP,
        'date': '2019-10-20',
        'matches': [

            # 2019-10-13
            {
                'round': 512,
                'players': [
                    KAMIL_MAJCHRZAK,
                    SERGIY_STAKHOVSKY,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.65,
                    SERGIY_STAKHOVSKY: 2.20
                },
                'prediction': KAMIL_MAJCHRZAK,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    JAUME_MUNAR,
                    MARCO_TRUNGELLITI,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JAUME_MUNAR: 1.48,
                    MARCO_TRUNGELLITI: 2.60,
                },
                'prediction': JAUME_MUNAR,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    NORBERT_GOMBOS,
                    KYLE_EDMUND,
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    NORBERT_GOMBOS: 3.60,
                    KYLE_EDMUND: 1.28,
                },
                'prediction': KYLE_EDMUND,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    YANNICK_MADEN,
                    SALVATORE_CARUSO,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    YANNICK_MADEN: 1.60,
                    SALVATORE_CARUSO: 2.30,
                },
                'prediction': YANNICK_MADEN,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    MARIUS_COPIL,
                    RUBEN_BEMELMANS,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MARIUS_COPIL: 1.85,
                    RUBEN_BEMELMANS: 1.95,
                },
                'prediction': MARIUS_COPIL,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    ANTOINE_HOANG,
                    CARLOS_TABERNER,
                ],
                'score': [(6, 2), (3, 6), (6, 2)],
                'odds': {
                    ANTOINE_HOANG: 1.34,
                    CARLOS_TABERNER: 3.20,
                },
                'prediction': ANTOINE_HOANG,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    PAOLO_LORENZI,
                    ARNAUD_BOVY,
                ],
                'score': [(6, 7), (6, 1), (6, 4)],
                'odds': {
                    PAOLO_LORENZI: 1.06,
                    ARNAUD_BOVY: 8.00,
                },
                'prediction': PAOLO_LORENZI,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    GREGOIRE_BARRERE,
                    PEDRO_MARTINEZ,
                ],
                'score': [(6, 0), (6, 4)],
                'odds': {
                    GREGOIRE_BARRERE: 1.16,
                    PEDRO_MARTINEZ: 4.80
                },
                'prediction': GREGOIRE_BARRERE,
                'bet': 1,
            },

            # 2019-10-14
            {
                'round': 256,
                'players': [
                    YANNICK_MADEN,
                    NORBERT_GOMBOS,
                ],
                'score': [(6, 1), (3, 6), (6, 4)],
                'odds': {
                    YANNICK_MADEN: 1.58,
                    NORBERT_GOMBOS: 2.35,
                },
            },
            {
                'round': 256,
                'players': [
                    KAMIL_MAJCHRZAK,
                    JAUME_MUNAR,
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.52,
                    JAUME_MUNAR: 2.50,
                },
                'prediction': KAMIL_MAJCHRZAK,
                'bet': 4,
            },
            {
                'round': 256,
                'players': [
                    GREGOIRE_BARRERE,
                    PAOLO_LORENZI,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    GREGOIRE_BARRERE: 1.20,
                    PAOLO_LORENZI: 4.40,
                },
            },
            {
                'round': 256,
                'players': [
                    MARIUS_COPIL,
                    ANTOINE_HOANG,
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    MARIUS_COPIL: 2.10,
                    ANTOINE_HOANG: 1.70,
                },
                'prediction': ANTOINE_HOANG,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    PETER_GOJOWCZYK,
                ],
                'score': [(5, 7), (6, 4), (7, 6)],
                'odds': {
                    GUIDO_PELLA: 1.52,
                    PETER_GOJOWCZYK: 2.50,
                },
                'prediction': GUIDO_PELLA,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    JO_WILFRIED_TSONGA,
                    LORENZO_SONEGO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.28,
                    LORENZO_SONEGO: 3.60,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 1,
            },

            # 2019-10-15
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    GREGOIRE_BARRERE,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.62,
                    GREGOIRE_BARRERE: 2.25,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    FELICIANO_LOPEZ,
                    CAMERON_NORRIE,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 2.25,
                    CAMERON_NORRIE: 1.62,
                },
            },
            {
                'round': 32,
                'players': [
                    MARIUS_COPIL,
                    FEDERICO_DELBONIS,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    MARIUS_COPIL: 1.34,
                    FEDERICO_DELBONIS: 3.20,
                },
                'prediction': MARIUS_COPIL,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    SOONWOO_KWON,
                    RICHARD_GASQUET,
                ],
                'score': [(1, 6), (6, 3), (6, 4)],
                'odds': {
                    SOONWOO_KWON: 2.40,
                    RICHARD_GASQUET: 1.55,
                },
                'prediction': RICHARD_GASQUET,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JANNIK_SINNER,
                    KAMIL_MAJCHRZAK,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JANNIK_SINNER: 1.80,
                    KAMIL_MAJCHRZAK: 2.00,
                },
                'prediction': JANNIK_SINNER,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    STEVE_DARCIS,
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    GILLES_SIMON: 1.26,
                    STEVE_DARCIS: 3.80,
                },
                'prediction': GILLES_SIMON,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    JOZEF_KOVALIK,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    UGO_HUMBERT: 1.26,
                    JOZEF_KOVALIK: 3.80,
                },
                'prediction': UGO_HUMBERT,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    ANDY_MURRAY,
                    KIMMER_COPPEJANS,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ANDY_MURRAY: 1.07,
                    KIMMER_COPPEJANS: 8.00,
                },
                'prediction': ANDY_MURRAY,
                'bet': 2,
            },

            # 2019-10-16
            {
                'round': 16,
                'players': [
                    FRANCES_TIAFOE,
                    YANNICK_MADEN,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    FRANCES_TIAFOE: 1.55,
                    YANNICK_MADEN: 2.40,
                },
                'prediction': FRANCES_TIAFOE,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    PABLO_CUEVAS,
                    HUGO_DELLIEN,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    PABLO_CUEVAS: 1.26,
                    HUGO_DELLIEN: 3.80,
                },
                'prediction': PABLO_CUEVAS,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    SOONWOO_KWON,
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    GUIDO_PELLA: 1.90,
                    SOONWOO_KWON: 1.90,
                },
            },
            {
                'round': 16,
                'players': [
                    GILLES_SIMON,
                    JO_WILFRIED_TSONGA,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    GILLES_SIMON: 3.40,
                    JO_WILFRIED_TSONGA: 1.30,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    FELICIANO_LOPEZ,
                ],
                'score': [(6, 7), (6, 4), (7, 6)],
                'odds': {
                    STAN_WAWRINKA: 1.42,
                    FELICIANO_LOPEZ: 2.80,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 3,
            },

            # 2019-10-17
            {
                'round': 16,
                'players': [
                    FRANCES_TIAFOE,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    FRANCES_TIAFOE: 2.35,
                    JAN_LENNARD_STRUFF: 1.58,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    MARIUS_COPIL,
                    DIEGO_SCHWARTZMAN,
                ],
                'score': [(6, 4), (5, 7), (7, 6)],
                'odds': {
                    MARIUS_COPIL: 3.30,
                    DIEGO_SCHWARTZMAN: 1.32,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    JANNIK_SINNER,
                    GAEL_MONFILS,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JANNIK_SINNER: 3.40,
                    GAEL_MONFILS: 1.30,
                },
                'prediction': GAEL_MONFILS,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    ANDY_MURRAY,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    ANDY_MURRAY: 1.26,
                    PABLO_CUEVAS: 3.80,
                },
                'prediction': ANDY_MURRAY,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    UGO_HUMBERT,
                    DAVID_GOFFIN,
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    UGO_HUMBERT: 3.30,
                    DAVID_GOFFIN: 1.32,
                },
            },

            # 2019-10-18
            {
                'round': 8,
                'players': [
                    JANNIK_SINNER,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    JANNIK_SINNER: 1.95,
                    FRANCES_TIAFOE: 1.85,
                },
            },
            {
                'round': 8,
                'players': [
                    STAN_WAWRINKA,
                    GILLES_SIMON,
                ],
                'score': [(6, 3), (6, 7), (6, 2)],
                'odds': {
                    STAN_WAWRINKA: 1.48,
                    GILLES_SIMON: 2.60,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    ANDY_MURRAY,
                    MARIUS_COPIL,
                ],
                'score': [(6, 3), (6, 7), (6, 4)],
                'odds': {
                    ANDY_MURRAY: 1.24,
                    MARIUS_COPIL: 4.00,
                },
                'prediction': ANDY_MURRAY,
                'bet': 8,
            },
            {
                'round': 8,
                'players': [
                    UGO_HUMBERT,
                    GUIDO_PELLA,
                ],
                'score': [(5, 7), (6, 4), (6, 4)],
                'odds': {
                    UGO_HUMBERT: 1.62,
                    GUIDO_PELLA: 2.25,
                },
                'prediction': UGO_HUMBERT,
                'bet': 3,
            },

            # 2019-10-19
            {
                'round': 4,
                'players': [
                    STAN_WAWRINKA,
                    JANNIK_SINNER,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    STAN_WAWRINKA: 1.38,
                    JANNIK_SINNER: 3.00,
                },
            },
            {
                'round': 4,
                'players': [
                    ANDY_MURRAY,
                    UGO_HUMBERT,
                ],
                'score': [(3, 6), (7, 5), (6, 2)],
                'odds': {
                    ANDY_MURRAY: 1.40,
                    UGO_HUMBERT: 2.90,
                },
                'prediction': ANDY_MURRAY,
                'bet': 3,
            },

            # 2019-10-20
            {

                'round': 2,
                'players': [
                     ANDY_MURRAY,
                     STAN_WAWRINKA,
                 ],
                'score': [(3, 6), (6, 4), (6, 4)],
                'odds': {
                    ANDY_MURRAY: 2.35,
                    STAN_WAWRINKA: 1.58,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 3,
            }
        ]
    },

    ###############################################################################
    # Active
    ###############################################################################

    {
        'location': VIENNA,
        'date': '2019-10-27',
        'matches': [

            # 2019-10-19
            {
                'round': 512,
                'players': [
                    ALEXANDER_BUBLIK,
                    KAMIL_MAJCHRZAK,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.55,
                    KAMIL_MAJCHRZAK: 2.35,
                },
                'prediction': ALEXANDER_BUBLIK,
                'bet': 3,
            },
            {
                'round': 512,
                'players': [
                    CAMERON_NORRIE,
                    ALEXANDER_ERLER,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    CAMERON_NORRIE: 1.11,
                    ALEXANDER_ERLER: 6.00,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DAMIR_DZUMHUR: 1.40,
                    NICOLAS_JARRY: 2.80,
                },
                'prediction': DAMIR_DZUMHUR,
                'bet': 6,
            },
            {
                'round': 512,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    SEBASTIAN_OFNER,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.22,
                    SEBASTIAN_OFNER: 4.00,
                },
                'prediction': PHILIPP_KOHLSCHREIBER,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    FEDERICO_DELBONIS,
                    ILYA_IVASHKA,
                ],
                'score': [(7, 6), (4, 6), (6, 3)],
                'odds': {
                    FEDERICO_DELBONIS: 2.40,
                    ILYA_IVASHKA: 1.52,
                },
                'prediction': ILYA_IVASHKA,
                'bet': 7,
            },
            {
                'round': 512,
                'players': [
                    STEFANO_TRAVAGLIA,
                    LUCAS_MIEDLER,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    STEFANO_TRAVAGLIA: 1.52,
                    LUCAS_MIEDLER: 2.40,
                },
            },
            {
                'round': 512,
                'players': [
                    ALJAZ_BEDENE,
                    JOZEF_KOVALIK,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ALJAZ_BEDENE: 1.16,
                    JOZEF_KOVALIK: 4.80,
                },
            },
            {
                'round': 512,
                'players': [
                    MARTON_FUCSOVICS,
                    EGOR_GERASIMOV,
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    MARTON_FUCSOVICS: 2.50,
                    EGOR_GERASIMOV: 1.50,
                },
                'prediction': EGOR_GERASIMOV,
                'bet': 4,
            },

            # 2019-10-20
            {
                'round': 256,
                'players': [
                    DAMIR_DZUMHUR,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(6, 3), (3, 6), (6, 1)],
                'odds': {
                    DAMIR_DZUMHUR: 2.05,
                    ALEXANDER_BUBLIK: 1.72,
                },
                'prediction': ALEXANDER_BUBLIK,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    CAMERON_NORRIE,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.72,
                    CAMERON_NORRIE: 2.05,
                },
                'prediction': PHILIPP_KOHLSCHREIBER,
                'bet': 6,
            },
            {
                'round': 256,
                'players': [
                    ALJAZ_BEDENE,
                    FEDERICO_DELBONIS,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    ALJAZ_BEDENE: 1.26,
                    FEDERICO_DELBONIS: 2.60,
                },
                'prediction': ALJAZ_BEDENE,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    MARTON_FUCSOVICS,
                    STEFANO_TRAVAGLIA,
                ],
                'score': [(6, 3), (1, 6), (6, 2)],
                'odds': {
                    MARTON_FUCSOVICS: 1.34,
                    STEFANO_TRAVAGLIA: 3.10,
                },
                'prediction': MARTON_FUCSOVICS,
                'bet': 8,
            },

            # 2019-10-21
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    PIERRE_HUGUES_HERBERT,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.38,
                    PIERRE_HUGUES_HERBERT: 3.00,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    LORENZO_SONEGO,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MARTON_FUCSOVICS: 1.62,
                    LORENZO_SONEGO: 2.25,
                },
                'prediction': MARTON_FUCSOVICS,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    KYLE_EDMUND,
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 1.26,
                    KYLE_EDMUND: 3.80,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    GRIGOR_DIMITROV,
                    DAMIR_DZUMHUR,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    GRIGOR_DIMITROV: 1.32,
                    DAMIR_DZUMHUR: 3.30,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    HUBERT_HURKACZ,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    KAREN_KHACHANOV: 1.62,
                    HUBERT_HURKACZ: 2.25,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 1,
            },

            # 2019-10-22
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    FELICIANO_LOPEZ,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    GILLES_SIMON: 1.65,
                    FELICIANO_LOPEZ: 2.20,
                },
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    GUIDO_PELLA,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALJAZ_BEDENE: 1.65,
                    GUIDO_PELLA: 2.20,
                },
                'prediction': ALJAZ_BEDENE,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    HYEON_CHUNG,
                    MILOS_RAONIC,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    HYEON_CHUNG: 2.40,
                    MILOS_RAONIC: 1.55,
                },
                'prediction': MILOS_RAONIC,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(4, 6), (6, 2), (6, 1)],
                'odds': {
                    FERNANDO_VERDASCO: 2.40,
                    NIKOLOZ_BASILASHVILI: 1.55,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 8,
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    JO_WILFRIED_TSONGA,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DOMINIC_THIEM: 1.42,
                    JO_WILFRIED_TSONGA: 2.80,
                },
            },
            {
                'round': 32,
                'players': [
                    JANNIK_SINNER,
                    PHILIPP_KOHLSCHREIBER,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JANNIK_SINNER: 2.10,
                    PHILIPP_KOHLSCHREIBER: 1.70,
                },
                'prediction': PHILIPP_KOHLSCHREIBER,
                'bet': 1,
            },

            # 2019-10-23
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    DENIS_SHAPOVALOV,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 2.20,
                    DENIS_SHAPOVALOV: 1.65,
                },
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    ADRIAN_MANNARINO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    SAM_QUERREY: 1.52,
                    ADRIAN_MANNARINO: 2.50,
                },
            },
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    BORNA_CORIC,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 2.35,
                    BORNA_CORIC: 1.58,
                },
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(6, 1), (6, 7), (7, 6)],
                'odds': {
                    ANDREY_RUBLEV: 1.70,
                    ALEXANDER_BUBLIK: 2.10,
                },
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    DENNIS_NOVAK,
                ],
                'score': [(2, 6), (7, 5), (6, 3)],
                'odds': {
                    GAEL_MONFILS: 1.20,
                    DENNIS_NOVAK: 4.40,
                },
                'prediction': GAEL_MONFILS,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    GRIGOR_DIMITROV,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 1.55,
                    GRIGOR_DIMITROV: 2.40,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    KAREN_KHACHANOV,
                ],
                'score': [(6, 3), (4, 6), (4, 1)],
                'odds': {
                    MARTON_FUCSOVICS: 3.10,
                    KAREN_KHACHANOV: 1.36,
                },
            },

            # 2019-10-24
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    SAM_QUERREY,
                ],
                'score': [(6, 7), (6, 4), (7, 6)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.80,
                    SAM_QUERREY: 2.00,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(6, 7), (6, 4), (6, 1)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.34,
                    MIKHAIL_KUKUSHKIN: 3.20,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 7,
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    HYEON_CHUNG,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ANDREY_RUBLEV: 1.68,
                    HYEON_CHUNG: 2.15,
                },
            },
            {
                'round': 16,
                'players': [
                    ALJAZ_BEDENE,
                    GILLES_SIMON,
                ],
                'score': [(6, 2), (3, 6), (6, 3)],
                'odds': {
                    ALJAZ_BEDENE: 1.70,
                    GILLES_SIMON: 2.10,
                },
                'prediction': ALJAZ_BEDENE,
                'bet': 13,
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    FERNANDO_VERDASCO,
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.24,
                    FERNANDO_VERDASCO: 4.00,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    JANNIK_SINNER,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    GAEL_MONFILS: 1.90,
                    JANNIK_SINNER: 1.90,
                },
            },

            # 2019-10-25
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    ANDREY_RUBLEV,
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 1.60,
                    ANDREY_RUBLEV: 2.30,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 6,
            },
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(5, 0)],
                'retired': True,
                'odds': {
                    DOMINIC_THIEM: 1.26,
                    PABLO_CARRENO_BUSTA: 3.80,
                },
            },
            {
                'round': 8,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    KAREN_KHACHANOV,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 2.25,
                    KAREN_KHACHANOV: 1.62,
                },
            },
            {
                'round': 8,
                'players': [
                    GAEL_MONFILS,
                    ALJAZ_BEDENE,
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    GAEL_MONFILS: 1.52,
                    ALJAZ_BEDENE: 2.50,
                },
            },

            # 2019-10-26
            {
                'round': 4,
                'players': [
                    DOMINIC_THIEM,
                    MATTEO_BERRETTINI,
                ],
                'score': [(3, 6), (7, 5), (6, 3)],
                'odds': {
                    DOMINIC_THIEM: 1.60,
                    MATTEO_BERRETTINI: 2.30,
                },
            },
            {
                'round': 4,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    GAEL_MONFILS,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 2.35,
                    GAEL_MONFILS: 1.58,
                },
            },

            #
            {
                'round': 2,
                'players': [
                    DOMINIC_THIEM,
                    DIEGO_SCHWARTZMAN,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.28,
                    DIEGO_SCHWARTZMAN: 3.60,
                },
                'prediction': None,
            }
        ]
    },

    {
        'location': BASEL,
        'date': '2019-10-27',
        'matches': [

            # 2019-10-19
            {
                'round': 512,
                'players': [
                    RICARDAS_BERANKIS,
                    HUGO_NYS,
                ],
                'score': [(3, 6), (6, 1), (6, 2)],
                'odds': {
                    RICARDAS_BERANKIS: 1.22,
                    HUGO_NYS: 4.00,
                },
                'prediction': RICARDAS_BERANKIS,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    CASPER_RUUD,
                    KIMMER_COPPEJANS,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    CASPER_RUUD: 1.24,
                    KIMMER_COPPEJANS: 3.80,
                },
            },
            {
                'round': 512,
                'players': [
                    PETER_GOJOWCZYK,
                    IVO_KARLOVIC,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    PETER_GOJOWCZYK: 1.68,
                    IVO_KARLOVIC: 2.10,
                },
                'prediction': PETER_GOJOWCZYK,
                'bet': 9,
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    JOAO_SOUSA,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    ALEXEI_POPYRIN: 2.20,
                    JOAO_SOUSA: 1.62,
                },
                'prediction': JOAO_SOUSA,
                'bet': 3,
            },
            {
                'round': 512,
                'players': [
                    SOONWOO_KWON,
                    MARC_ANDREA_HUESLER,
                ],
                'score': [(4, 6), (6, 3), (6, 3)],
                'odds': {
                    SOONWOO_KWON: 1.22,
                    MARC_ANDREA_HUESLER: 4.00,
                },
            },
            {
                'round': 512,
                'players': [
                    GREGOIRE_BARRERE,
                    LUKAS_ROSOL,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    GREGOIRE_BARRERE: 1.55,
                    LUKAS_ROSOL: 2.35,
                },
            },
            {
                'round': 512,
                'players': [
                    HUGO_DELLIEN,
                    SANDRO_EHRAT,
                ],
                'score': [(7, 6), (2, 6), (6, 4)],
                'odds': {
                    HUGO_DELLIEN: 1.55,
                    SANDRO_EHRAT: 2.35,
                },
                'prediction': HUGO_DELLIEN,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    ATTILA_BALAZS,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.18,
                    ATTILA_BALAZS: 4.50,
                },
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 4,
            },

            # 2019-10-20
            {
                'round': 256,
                'players': [
                    RICARDAS_BERANKIS,
                    GREGOIRE_BARRERE,
                ],
                'score': [],
                'retired': True,
                'odds': {
                    RICARDAS_BERANKIS: 2.00,
                    GREGOIRE_BARRERE: 1.75,
                },
                'prediction': GREGOIRE_BARRERE,
                'bet': 0,  # refunded 3,
            },
            {
                'round': 256,
                'players': [
                    PETER_GOJOWCZYK,
                    CASPER_RUUD,
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    PETER_GOJOWCZYK: 2.00,
                    CASPER_RUUD: 1.75,
                },
            },
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    SOONWOO_KWON,
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    ALEXEI_POPYRIN: 1.50,
                    SOONWOO_KWON: 2.50,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 5,
            },
            {
                'round': 256,
                'players': [
                    HUGO_DELLIEN,
                    YOSHIHITO_NISHIOKA,
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    HUGO_DELLIEN: 5.50,
                    YOSHIHITO_NISHIOKA: 1.13,
                },
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 8,
            },

            # 2019-10-21
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    PETER_GOJOWCZYK,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    ROGER_FEDERER: 1.04,
                    PETER_GOJOWCZYK: 10.00,
                },
                'prediction': ROGER_FEDERER,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.62,
                    MIOMIR_KECMANOVIC: 2.25,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    ALEX_DE_MINAUR,
                    HUGO_DELLIEN,
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    ALEX_DE_MINAUR: 1.07,
                    HUGO_DELLIEN: 8.00,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    HENRI_LAAKSONEN,
                    BENOIT_PAIRE,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    HENRI_LAAKSONEN: 2.60,
                    BENOIT_PAIRE: 1.48,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 1,
            },

            # 2019-10-22
            {
                'round': 32,
                'players': [
                    RADU_ALBOT,
                    DUSAN_LAJOVIC,
                ],
                'score': [(2, 6), (6, 3), (6, 4)],
                'odds': {
                    RADU_ALBOT: 1.65,
                    DUSAN_LAJOVIC: 2.20,
                },
                'prediction': RADU_ALBOT,
                'bet': 10,
            },
            {
                'round': 32,
                'players': [
                    REILLY_OPELKA,
                    CHRISTIAN_GARIN,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 1.42,
                    CHRISTIAN_GARIN: 2.80,
                },
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.90,
                    ALEXEI_POPYRIN: 1.90,
                },
            },
            {
                'round': 32,
                'players': [
                    TAYLOR_FRITZ,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 4.20,
                    ALEXANDER_ZVEREV: 1.22,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    RICHARD_GASQUET: 1.48,
                    JUAN_IGNACIO_LONDERO: 2.60,
                },
                'prediction': RICHARD_GASQUET,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.16,
                    ALBERT_RAMOS_VINOLAS: 5.00,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    MARIUS_COPIL,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.28,
                    MARIUS_COPIL: 3.60,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 1,
            },

            # 2019-10-23
            {
                'round': 32,
                'players': [
                    RICARDAS_BERANKIS,
                    PABLO_ANDUJAR,
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    RICARDAS_BERANKIS: 1.42,
                    PABLO_ANDUJAR: 2.80,
                },
                'prediction': RICARDAS_BERANKIS,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    LASLO_DJERE,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.18,
                    LASLO_DJERE: 4.60,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    MARIN_CILIC,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 1.52,
                    MARIN_CILIC: 2.50,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STAN_WAWRINKA: 1.18,
                    PABLO_CUEVAS: 4.60,
                },
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    RADU_ALBOT,
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.01,
                    RADU_ALBOT: 14.00,
                },
                'prediction': ROGER_FEDERER,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    DANIEL_EVANS,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    FRANCES_TIAFOE: 2.10,
                    DANIEL_EVANS: 1.70,
                },
                'prediction': DANIEL_EVANS,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    ALEX_DE_MINAUR,
                    TAYLOR_FRITZ,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    ALEX_DE_MINAUR: 1.58,
                    TAYLOR_FRITZ: 2.35,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    JAN_LENNARD_STRUFF,
                    HENRI_LAAKSONEN,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.30,
                    HENRI_LAAKSONEN: 3.40,
                },
            },

            # 2019-10-24
            {
                'round': 16,
                'players': [
                    REILLY_OPELKA,
                    DAVID_GOFFIN,
                ],
                'score': [(6, 7), (7, 6), (7, 5)],
                'odds': {
                    REILLY_OPELKA: 3.10,
                    DAVID_GOFFIN: 1.36,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    RICHARD_GASQUET,
                ],
                'score': [(6, 2), (4, 6), (6, 3)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.32,
                    RICHARD_GASQUET: 3.30,
                },
                'prediction': RICHARD_GASQUET,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 7), (6, 2), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.16,
                    RICARDAS_BERANKIS: 5.00,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 7,
            },
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 3), (3, 6), (7, 5)],
                'odds': {
                    STAN_WAWRINKA: 1.30,
                    FRANCES_TIAFOE: 3.40,
                },
            },
            {
                'round': 16,
                'players': [
                    FILIP_KRAJINOVIC,
                    FABIO_FOGNINI,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.95,
                    FABIO_FOGNINI: 1.85,
                },
            },

            # 2019-10-25
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    STAN_WAWRINKA,
                ],
                # no odds
                'retired': True,
            },
            {
                'round': 8,
                'players': [
                    REILLY_OPELKA,
                    ROBERTO_BAUTISTA_AGUT,
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    REILLY_OPELKA: 2.70,
                    ROBERTO_BAUTISTA_AGUT: 1.45,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    ALEX_DE_MINAUR,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ALEX_DE_MINAUR: 1.48,
                    JAN_LENNARD_STRUFF: 2.60,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    FILIP_KRAJINOVIC,
                ],
                'score': [(3, 6), (6, 4), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.38,
                    FILIP_KRAJINOVIC: 3.00,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 7,
            },

            # 2019-10-26
            {
                'round': 4,
                'players': [
                    ALEX_DE_MINAUR,
                    REILLY_OPELKA,
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    ALEX_DE_MINAUR: 1.45,
                    REILLY_OPELKA: 2.70,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 2,
            },
            {
                'round': 4,
                'players': [
                    ROGER_FEDERER,
                    STEFANOS_TSITSIPAS,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.24,
                    STEFANOS_TSITSIPAS: 4.00,
                },
                'prediction': ROGER_FEDERER,
                'bet': 6,
            },

            #
            {
                'round': 2,
                'players': [
                    ROGER_FEDERER,
                    ALEX_DE_MINAUR,
                ],
                'odds': {
                    ROGER_FEDERER: 1.09,
                    ALEX_DE_MINAUR: 7.00,
                },
                'prediction': None,
            },
        ]
    },

    {
        'location': PARIS,
        'date': '2019-11-03',
        'matches': [

            # 2019-10-26
            {
                'round': 512,
                'players': [
                    CAMERON_NORRIE,
                    FEDERICO_DELBONIS,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    CAMERON_NORRIE: 1.28,
                    FEDERICO_DELBONIS: 3.50,
                },
            },
            {
                'round': 512,
                'players': [
                    RAYANE_ROUMANE,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(6, 3), (4, 6), (7, 6)],
                'odds': {
                    RAYANE_ROUMANE: 3.30,
                    MIOMIR_KECMANOVIC: 1.30,
                },
            },
            {
                'round': 512,
                'players': [
                    PABLO_CUEVAS,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'score': [(5, 7), (6, 3), (6, 4)],
                'odds': {
                    PABLO_CUEVAS: 1.58,
                    ROBERTO_CARBALLES_BAENA: 2.30,
                },
            },
            {
                'round': 512,
                'players': [
                    SAM_QUERREY,
                    ELLIOT_BENCHETRIT,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    SAM_QUERREY: 1.09,
                    ELLIOT_BENCHETRIT: 6.50,
                },
            },
            {
                'round': 512,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    FELICIANO_LOPEZ,
                ],
                'score': [(6, 7), (6, 3), (6, 2)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.87,
                    FELICIANO_LOPEZ: 1.87,
                },
            },
            {
                'round': 512,
                'players': [
                    JEREMY_CHARDY,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 1.46,
                    ALBERT_RAMOS_VINOLAS: 2.60,
                },
            },
            {
                'round': 512,
                'players': [
                    ANDREAS_SEPPI,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    ANDREAS_SEPPI: 2.15,
                    ALEXANDER_BUBLIK: 1.65,
                },
            },
            {
                'round': 512,
                'players': [
                    CORENTIN_MOUTET,
                    LORENZO_SONEGO,
                ],
                'score': [(3, 6), (6, 3), (6, 0)],
                'odds': {
                    CORENTIN_MOUTET: 2.35,
                    LORENZO_SONEGO: 1.55,
                },
            },
            {
                'round': 512,
                'players': [
                    HUGO_GASTON,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    HUGO_GASTON: 2.35,
                    JUAN_IGNACIO_LONDERO: 1.55,
                },
                'prediction': JUAN_IGNACIO_LONDERO,
                'bet': 6,
            },
            {
                'round': 512,
                'players': [
                    CASPER_RUUD,
                    MIKAEL_YMER,
                ],
                'score': [(6, 4), (3, 6), (6, 4)],
                'odds': {
                    CASPER_RUUD: 2.80,
                    MIKAEL_YMER: 1.40,
                },
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    PABLO_ANDUJAR,
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    DAMIR_DZUMHUR: 1.28,
                    PABLO_ANDUJAR: 3.50,
                },
                'prediction': DAMIR_DZUMHUR,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    RICARDAS_BERANKIS,
                    JOHN_MILLMAN,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    RICARDAS_BERANKIS: 2.40,
                    JOHN_MILLMAN: 1.52,
                },
                'prediction': JOHN_MILLMAN,
                'bet': 7,
            },

            #
            {
                'round': 256,
                'players': [
                    EGOR_GERASIMOV,
                    CAMERON_NORRIE,
                ],
                'odds': {
                    EGOR_GERASIMOV: 2.00,
                    CAMERON_NORRIE: 1.80,
                },
                'prediction': None,
            },
            {
                'round': 256,
                'players': [
                    SAM_QUERREY,
                    RAYANE_ROUMANE,
                ],
                'odds': {
                    SAM_QUERREY: 1.16,
                    RAYANE_ROUMANE: 5.00,
                },
                'prediction': None,
            },
            {
                'round': 256,
                'players': [
                    JEREMY_CHARDY,
                    CORENTIN_MOUTET,
                ],
                'odds': {
                    JEREMY_CHARDY: 1.26,
                    CORENTIN_MOUTET: 3.80,
                },
                'prediction': None,
            },
            {
                'round': 256,
                'players': [
                    ANDREAS_SEPPI,
                    YOSHIHITO_NISHIOKA,
                ],
                'odds': {
                    ANDREAS_SEPPI: 2.00,
                    YOSHIHITO_NISHIOKA: 1.80,
                },
                'prediction': None,
            },
            {
                'round': 256,
                'players': [
                    RICARDAS_BERANKIS,
                    DAMIR_DZUMHUR,
                ],
                'odds': {
                    RICARDAS_BERANKIS: 2.20,
                    DAMIR_DZUMHUR: 1.65,
                },
                'prediction': None,
            },
            {
                'round': 256,
                'players': [
                    HUGO_GASTON,
                    CASPER_RUUD,
                ],
                'odds': {
                    HUGO_GASTON: 3.30,
                    CASPER_RUUD: 1.32,
                },
                'prediction': None,
            },

            #
            # {
            #     'round': 256,
            #     'players': [
            #         NIKOLOZ_BASILASHVILI,
            #         RADU_ALBOT,
            #     ],
            #     'odds': {
            #         NIKOLOZ_BASILASHVILI: 1.52,
            #         RADU_ALBOT: 2.50,
            #     },
            #     'prediction': None,
            # },
        ]
    }
]


