from men import *
from location import *

# acc   roi     profit  desc
# 100   40.9    1306    2018 gstaad                         (2, 1013), (3, 385), (1, 1), (5, 1)
# 72.1  10.0    1191    2018 washington                     (3, 1187), (4, 538), (6, 337), (1, 283)
# 94.0  33.6    1476    2019 us open                        (3, 1239), (1, 105), (4, 100), (2, 24)
# 71.5  9.6     1165    2018 los cabollas                   (3, 1598), (6, 1052), (7, 71), (4, 71)
# 99.8  37.0    1483    2018 kitzhbuhel                     (3, 1324), (6, 5), (4, 1)

# 71.4  11.5    351     2018 toronto                        (1, 1541), (2, 592), (3, 65), (4, 15)
# 75.1  12.6    1009    2019-09-03 results and bets         (2, 1351), (5, 621), (3, 295), (7, 53)
# 72.9  7.9     349     2019-08-31                          (1, 1534), (2, 974), (0, 819), (3, 160)
# 71.3  30.2    1306    2018 winston done                   (2, 444), (3, 166), (1, 115), (4, 110)

# 68.6  26.5    1312    2018 winston r64                    (3, 319), (2, 253), (4, 129), (5, 98)
# 67.7  25.3    954     2018 us open r16 p1                 (3, 272), (2, 234), (4, 140), (5, 133)
# 65.2  13.0    648     2018 us open 3rd qual               (6, 243), (4, 212), (3, 179), (5, 152)

# 68.6  26.2    459     sst petersburg 2018                 (2, 436), (1, 385), (3, 127), (4, 28)
# 65.4  20.6    551     opt win losses                      (3, 277), (1, 249), (5, 185), (2, 103)

# 65.7  17.2    327     opt lambda & tie & ups              (2, 387), (1, 233), (3, 196), (4, 59)
# 67.7  19.4    288     opt step/subsample/scale

# 71.8  23.2  865    2019-08-16


DATA = [
    {
        'location': WASHINGTON,
        'date': '2019-08-04',
        'matches': [

            # 2019-07-27
            {
                'round': 512,
                'players': [
                    DONALD_YOUNG,
                    NICHOLAS_REYES
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    DONALD_YOUNG: 1.04,
                    NICHOLAS_REYES: 9.74
                }
            },
            {
                'round': 512,
                'players': [
                    TIM_SMYCZEK,
                    RAMKUMAR_RAMANATHAN
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    TIM_SMYCZEK: 2.00,
                    RAMKUMAR_RAMANATHAN: 1.69
                }
            },
            {
                'round': 512,
                'players': [
                    MARC_POLMANS,
                    JAMIE_CERRETANI
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    MARC_POLMANS: 1.03,
                    JAMIE_CERRETANI: 12.08
                }
            },
            {
                'round': 512,
                'players': [
                    MIKAEL_TORPEGAARD,
                    ALEXIS_GALARNEAU
                ],
                'score': [(6, 4), (2, 6), (6, 4)],
                'odds': {
                    MIKAEL_TORPEGAARD: 1.19,
                    ALEXIS_GALARNEAU: 3.82
                }
            },
            {
                'round': 512,
                'players': [
                    THAI_SON_KWIATKOWSKI,
                    NOAH_RUBIN
                ],
                'score': [(7, 5), (4, 6), (6, 1)],
                'odds': {
                    THAI_SON_KWIATKOWSKI: 2.51,
                    NOAH_RUBIN: 1.47
                }
            },
            {
                'round': 512,
                'players': [
                    NICOLAS_MAHUT,
                    ROBERT_MACIAG
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    NICOLAS_MAHUT: 1.06,
                    ROBERT_MACIAG: 7.85
                }
            },
            {
                'round': 512,
                'players': [
                    VIKTOR_TROICKI,
                    ANDREW_FENTY
                ],
                'score': [(4, 6), (6, 1), (7, 5)],
                'odds': {
                    VIKTOR_TROICKI: 1.06,
                    ANDREW_FENTY: 8.00
                }
            },
            {
                'round': 512,
                'players': [
                    GLEB_SAKHAROV,
                    MICHAEL_MMOH
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    GLEB_SAKHAROV: 3.28,
                    MICHAEL_MMOH: 1.26
                }
            },

            # 2019-07-28
            {
                'round': 256,
                'players': [
                    DONALD_YOUNG,
                    PETER_GOJOWCZYK,
                ],
                'score': [(2, 6), (6, 3), (6, 4)],
                'odds': {
                    DONALD_YOUNG: 1.95,
                    PETER_GOJOWCZYK: 1.80,
                },
                'prediction': PETER_GOJOWCZYK,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    MIKAEL_TORPEGAARD,
                    ILYA_IVASHKA,
                ],
                'score': [(4, 6), (6, 4), (6, 3)],
                'odds': {
                    MIKAEL_TORPEGAARD: 2.05,
                    ILYA_IVASHKA: 1.72,
                },
                'prediction': ILYA_IVASHKA,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    TIM_SMYCZEK,
                    NORBERT_GOMBOS,
                ],
                'score': [(7, 6), (5, 7), (6, 3)],
                'odds': {
                    TIM_SMYCZEK: 2.35,
                    NORBERT_GOMBOS: 1.55,
                },
                'prediction': NORBERT_GOMBOS,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    MARC_POLMANS,
                    NICOLAS_MAHUT,
                ],
                'score': [(6, 7), (6, 2), (6, 4)],
                'odds': {
                    MARC_POLMANS: 2.35,
                    NICOLAS_MAHUT: 1.55,
                },
                'prediction': NICOLAS_MAHUT,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    THAI_SON_KWIATKOWSKI,
                    VIKTOR_TROICKI,
                ],
                'score': [(6, 3), (6, 7), (6, 4)],
                'odds': {
                    THAI_SON_KWIATKOWSKI: 2.70,
                    VIKTOR_TROICKI: 1.44,
                },
                'prediction': VIKTOR_TROICKI,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    BRAYDEN_SCHNUR,
                    GLEB_SAKHAROV
                ],
                'score': [(4, 6), (6, 2), (6, 4)],
                'odds': {
                    BRAYDEN_SCHNUR: 1.32,
                    GLEB_SAKHAROV: 3.20
                },
                'prediction': BRAYDEN_SCHNUR,
                'bet': 15,
            },

            # 2019-07-29
            {
                'round': 64,
                'players': [
                    JO_WILFRIED_TSONGA,
                    BRAYDEN_SCHNUR
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.22,
                    BRAYDEN_SCHNUR: 4.24
                }
            },
            {
                'round': 64,
                'players': [
                    TIM_SMYCZEK,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    TIM_SMYCZEK: 2.10,
                    MATTHEW_EBDEN: 1.71
                }
            },
            {
                'round': 64,
                'players': [
                    TOMMY_PAUL,
                    DENIS_KUDLA
                ],
                'score': [(6, 0), (6, 4)],
                'odds': {
                    TOMMY_PAUL: 1.74,
                    DENIS_KUDLA: 2.05
                }
            },
            {
                'round': 64,
                'players': [
                    ADRIAN_MANNARINO,
                    ILYA_IVASHKA
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ADRIAN_MANNARINO: 1.56,
                    ILYA_IVASHKA: 2.40
                }
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    DONALD_YOUNG
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 1.29,
                    DONALD_YOUNG: 3.40
                }
            },
            {
                'round': 64,
                'players': [
                    LLOYD_HARRIS,
                    RICARDAS_BERANKIS
                ],
                'score': [(4, 6), (6, 3), (6, 1)],
                'odds': {
                    LLOYD_HARRIS: 1.98,
                    RICARDAS_BERANKIS: 1.80
                }
            },
            {
                'round': 64,
                'players': [
                    BJORN_FRATANGELO,
                    IVO_KARLOVIC
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    BJORN_FRATANGELO: 1.80,
                    IVO_KARLOVIC: 1.91
                }
            },
            {
                'round': 64,
                'players': [
                    MARIUS_COPIL,
                    MIKAEL_TORPEGAARD
                ],
                'score': [(6, 1), (5, 7), (6, 3)],
                # no odds
            },
            {
                'round': 64,
                'players': [
                    ALEXANDER_BUBLIK,
                    BRADLEY_KLAHN
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.92,
                    BRADLEY_KLAHN: 1.79
                }
            },
            {
                'round': 64,
                'players': [
                    MARC_POLMANS,
                    MALEK_JAZIRI
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    MARC_POLMANS: 1.71,
                    MALEK_JAZIRI: 2.10
                }
            },

            # 2019-07-30
            {
                'round': 64,
                'players': [
                    JORDAN_THOMPSON,
                    JACK_SOCK,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    JORDAN_THOMPSON: 1.65,
                    JACK_SOCK: 2.20,
                },
                'prediction': JORDAN_THOMPSON,
                'bet': 11,
            },
            {
                'round': 64,
                'players': [
                    REILLY_OPELKA,
                    CHRISTOPHER_EUBANKS
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 1.34,
                    CHRISTOPHER_EUBANKS: 3.20,
                },
                'prediction': REILLY_OPELKA,
                'bet': 12,
            },
            {
                'round': 64,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    DANIEL_EVANS,
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 3.10,
                    DANIEL_EVANS: 1.36,
                },
                'prediction': DANIEL_EVANS,
                'bet': 12,
            },
            {
                'round': 64,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ALEXEI_POPYRIN
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.58,
                    ALEXEI_POPYRIN: 2.35,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 11,
            },
            {
                'round': 64,
                'players': [
                    PETER_GOJOWCZYK,
                    ANDREY_RUBLEV
                ],
                'score': [(7, 6), (4, 6), (7, 6)],
                'odds': {
                    PETER_GOJOWCZYK: 3.00,
                    ANDREY_RUBLEV: 1.38
                }
            },
            {
                'round': 64,
                'players': [
                    NICK_KYRGIOS,
                    THAI_SON_KWIATKOWSKI,
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    NICK_KYRGIOS: 1.24,
                    THAI_SON_KWIATKOWSKI: 4.00,
                },
                'prediction': NICK_KYRGIOS,
                'bet': 11,
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    ALEXANDER_BUBLIK
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    FRANCES_TIAFOE: 1.57,
                    ALEXANDER_BUBLIK: 2.45
                }
            },
            {
                'round': 32,
                'players': [
                    KYLE_EDMUND,
                    LLOYD_HARRIS
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    KYLE_EDMUND: 1.38,
                    LLOYD_HARRIS: 2.86
                }
            },
            {
                'round': 32,
                'players': [
                    MARIN_CILIC,
                    MARIUS_COPIL
                ],
                'score': [(7, 6), (7, 6)]
            },
            {
                'round': 32,
                'players': [
                    DANIIL_MEDVEDEV,
                    BJORN_FRATANGELO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.22,
                    BJORN_FRATANGELO: 4.20,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 11,
            },
            {
                'round': 32,
                'players': [
                    JO_WILFRIED_TSONGA,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 4), (2, 6), (7, 5)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.83,
                    KAREN_KHACHANOV: 1.87
                }
            },

            # 2019-07-31
            {
                'round': 32,
                'players': [
                    NORBERT_GOMBOS,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 4), (7, 6)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(3, 6), (6, 4), (7, 6)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.55,
                    PIERRE_HUGUES_HERBERT: 2.30,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    PETER_GOJOWCZYK,
                    ALEX_DE_MINAUR
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    PETER_GOJOWCZYK: 4.55,
                    ALEX_DE_MINAUR: 1.16
                }
            },
            {
                'round': 32,
                'players': [
                    NICK_KYRGIOS,
                    GILLES_SIMON,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 1.42,
                    GILLES_SIMON: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    MARC_POLMANS
                ],
                'score': [(6, 3), (6, 7), (6, 7)],
                'odds': {
                    BENOIT_PAIRE: 1.48,
                    MARC_POLMANS: 2.60,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    REILLY_OPELKA,
                ],
                'score': [(6, 4), (3, 6), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.95,
                    REILLY_OPELKA: 1.85,
                },
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    MILOS_RAONIC,
                    TIM_SMYCZEK
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    MILOS_RAONIC: 1.16,
                    TIM_SMYCZEK: 5.00,
                },
                'prediction': MILOS_RAONIC,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    DAVID_GOFFIN
                ],
                'score': [(6, 7), (6, 2), (7, 6)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 3.30,
                    DAVID_GOFFIN: 1.32,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    JOHN_ISNER,
                    HUBERT_HURKACZ,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JOHN_ISNER: 1.62,
                    HUBERT_HURKACZ: 2.25,
                },
                'prediction': HUBERT_HURKACZ,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    TOMMY_PAUL
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.26,
                    TOMMY_PAUL: 3.80,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    JORDAN_THOMPSON,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 7), (6, 4), (7, 5)],
                'odds': {
                    JORDAN_THOMPSON: 1.85,
                    JAN_LENNARD_STRUFF: 1.95,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 4,
            },

            # 2019-08-01
            {
                'round': 16,
                'players': [
                    NORBERT_GOMBOS,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(1, 6), (6, 3), (7, 6)],
                'odds': {
                    NORBERT_GOMBOS: 3.20,
                    MIOMIR_KECMANOVIC: 1.34,
                },
                'prediction': NORBERT_GOMBOS,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    KYLE_EDMUND,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    KYLE_EDMUND: 2.35,
                    JO_WILFRIED_TSONGA: 1.58,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    PETER_GOJOWCZYK,
                    MILOS_RAONIC,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    PETER_GOJOWCZYK: 4.50,
                    MILOS_RAONIC: 1.20
                }
            },
            {
                'round': 16,
                'players': [
                    MARIN_CILIC,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MARIN_CILIC: 2.00,
                    FELIX_AUGER_ALIASSIME: 1.80,
                },
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    BENOIT_PAIRE,
                    JOHN_ISNER
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 3.63,
                    JOHN_ISNER: 1.27
                }
            },
            {
                'round': 16,
                'players': [
                    DANIIL_MEDVEDEV,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.45,
                    FRANCES_TIAFOE: 2.70,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    JORDAN_THOMPSON
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.27,
                    JORDAN_THOMPSON: 3.60
                }
            },
            {
                'round': 16,
                'players': [
                    NICK_KYRGIOS,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    NICK_KYRGIOS: 1.40,
                    YOSHIHITO_NISHIOKA: 2.75
                }
            },

            # 2019-08-02
            {
                'round': 8,
                'players': [
                    PETER_GOJOWCZYK,
                    KYLE_EDMUND
                ],
                'score': [(6, 3), (4, 6), (6, 3)],
                'odds': {
                    PETER_GOJOWCZYK: 3.60,
                    KYLE_EDMUND: 1.28,
                },
                'prediction': KYLE_EDMUND,
                'bet': 3,
            },
            {
                'round': 8,
                'players': [
                    DANIIL_MEDVEDEV,
                    MARIN_CILIC,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.68,
                    MARIN_CILIC: 2.15,
                },
                'prediction': MARIN_CILIC,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    BENOIT_PAIRE
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.32,
                    BENOIT_PAIRE: 3.30,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    NICK_KYRGIOS,
                    NORBERT_GOMBOS,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    NICK_KYRGIOS: 1.16,
                    NORBERT_GOMBOS: 4.60,
                },
                'prediction': NICK_KYRGIOS,
                'bet': 3,
            },

            # 2019-08-03
            {
                'round': 4,
                'players': [
                    DANIIL_MEDVEDEV,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.16,
                    PETER_GOJOWCZYK: 5.00,
                },
                'prediction': PETER_GOJOWCZYK,
                'bet': 3,
            },
            {
                'round': 4,
                'players': [
                    NICK_KYRGIOS,
                    STEFANOS_TSITSIPAS,
                ],
                'score': [(6, 4), (3, 6), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 2.10,
                    STEFANOS_TSITSIPAS: 1.70,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 4,
            },

            # 2019-08-04
            {
                'round': 2,
                'players': [
                    NICK_KYRGIOS,
                    DANIIL_MEDVEDEV
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 2.10,
                    DANIIL_MEDVEDEV: 1.65,
                },
            }
        ]
    },

    {
        'location': LOS_CABOS,
        'date': '2019-08-03',
        'matches': [

            # 2019-07-27
            {
                'round': 512,
                'players': [
                    JACOB_GRILLS,
                    LUKAS_LACKO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JACOB_GRILLS: 4.34,
                    LUKAS_LACKO: 1.17
                }
            },
            {
                'round': 512,
                'players': [
                    MAXIME_JANVIER,
                    JUAN_IGNACIO_BATALLA
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    MAXIME_JANVIER: 1.02,
                    JUAN_IGNACIO_BATALLA: 9.00
                }
            },
            {
                'round': 512,
                'players': [
                    DANILO_PETROVIC,
                    SERGIY_STAKHOVSKY
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DANILO_PETROVIC: 2.25,
                    SERGIY_STAKHOVSKY: 1.59
                }
            },
            {
                'round': 512,
                'players': [
                    MARCELO_AREVALO,
                    MARCOS_GIRON
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    MARCELO_AREVALO: 3.15,
                    MARCOS_GIRON: 1.25
                }
            },
            {
                'round': 512,
                'players': [
                    JASON_JUNG,
                    GERARDO_LOPEZ_VILLASENOR
                ],
                'score': [(6, 1), (3, 6), (6, 0)],
                'odds': {
                    JASON_JUNG: 1.16,
                    GERARDO_LOPEZ_VILLASENOR: 4.93
                }
            },
            {
                'round': 512,
                'players': [
                    DOMINIK_KOEPFER,
                    JOHN_PATRICK_SMITH
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    DOMINIK_KOEPFER: 1.59,
                    JOHN_PATRICK_SMITH: 2.27
                }
            },
            {
                'round': 512,
                'players': [
                    SOONWOO_KWON,
                    LUIS_PATINO
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    SOONWOO_KWON: 1.05,
                    LUIS_PATINO: 9.21
                }
            },
            {
                'round': 512,
                'players': [
                    EGOR_GERASIMOV,
                    DENNIS_NOVIKOV
                ],
                'score': [(4, 6), (6, 2), (7, 5)],
                'odds': {
                    EGOR_GERASIMOV: 1.28,
                    DENNIS_NOVIKOV: 3.50
                }
            },

            # 2019-07-28
            {
                'round': 256,
                'players': [
                    MAXIME_JANVIER,
                    EGOR_GERASIMOV,
                ],
                'score': [(3, 6), (6, 1), (7, 6)],
                'odds': {
                    MAXIME_JANVIER: 2.60,
                    EGOR_GERASIMOV: 1.46,
                },
                'prediction': EGOR_GERASIMOV,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    JASON_JUNG,
                    DANILO_PETROVIC
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    JASON_JUNG: 1.36,
                    DANILO_PETROVIC: 3.00
                },
                'prediction': JASON_JUNG,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    DOMINIK_KOEPFER,
                    JACOB_GRILLS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DOMINIK_KOEPFER: 1.18,
                    JACOB_GRILLS: 4.20
                },
                'prediction': DOMINIK_KOEPFER,
                'bet': 15,
            },
            {
                'round': 256,
                'players': [
                    SOONWOO_KWON,
                    MARCELO_AREVALO
                ],
                'score': [(7, 6), (5, 7), (6, 3)],
                'odds': {
                    SOONWOO_KWON: 1.16,
                    MARCELO_AREVALO: 4.50
                },
                'prediction': SOONWOO_KWON,
                'bet': 15,
            },

            # 2019-07-29
            {
                'round': 32,
                'players': [
                    THANASI_KOKKINAKIS,
                    MAXIME_JANVIER
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    THANASI_KOKKINAKIS: 1.42,
                    MAXIME_JANVIER: 2.70
                }
            },
            {
                'round': 32,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    JOHN_MILLMAN
                ],
                'score': [(6, 4), (1, 6), (6, 2)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 3.35,
                    JOHN_MILLMAN: 1.33
                }
            },
            {
                'round': 32,
                'players': [
                    MARCEL_GRANOLLERS,
                    LUCAS_GOMEZ
                ],
                'score': [(6, 0), (6, 1)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.09,
                    LUCAS_GOMEZ: 7.50
                }
            },
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    DAMIR_DZUMHUR
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.74,
                    DAMIR_DZUMHUR: 2.08
                }
            },
            {
                'round': 32,
                'players': [
                    ERNESTS_GULBIS,
                    JASON_JUNG
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ERNESTS_GULBIS: 2.34,
                    JASON_JUNG: 1.51
                }
            },

            # 2019-07-30
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    GREGOIRE_BARRERE,
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    CAMERON_NORRIE: 1.30,
                    GREGOIRE_BARRERE: 3.40,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    SOONWOO_KWON,
                    CEDRIC_MARCEL_STEBE,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    SOONWOO_KWON: 1.28,
                    CEDRIC_MARCEL_STEBE: 3.60,
                },
                'prediction': SOONWOO_KWON,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    TENNYS_SANDGREN
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    TARO_DANIEL: 3.10,
                    TENNYS_SANDGREN: 1.36,
                },
                'prediction': TARO_DANIEL,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    RADU_ALBOT,
                    JANKO_TIPSAREVIC,
                ],
                'score': [(7, 5), (2, 6), (6, 0)],
                'odds': {
                    RADU_ALBOT: 1.36,
                    JANKO_TIPSAREVIC: 3.10,
                },
                'prediction': JANKO_TIPSAREVIC,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    CHRISTIAN_GARIN,
                ],
                'score': [(3, 6), (6, 2), (6, 3)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 2.50,
                    CHRISTIAN_GARIN: 1.52,
                },
                'prediction': CHRISTIAN_GARIN,
                'bet': 9,
            },
            {
                'round': 32,
                'players': [
                    GRIGOR_DIMITROV,
                    STEVE_JOHNSON
                ],
                'score': [(7, 6), (4, 6), (7, 6)],
                'odds': {
                    GRIGOR_DIMITROV: 1.65,
                    STEVE_JOHNSON: 2.20,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 6,
            },

            # 2019-07-31
            {
                'round': 16,
                'players': [
                    SOONWOO_KWON,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 4), (6, 3), (6, 3)],
                'odds': {
                    SOONWOO_KWON: 1.38,
                    JUAN_IGNACIO_LONDERO: 2.90,
                },
            },
            {
                'round': 16,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    CAMERON_NORRIE
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 2.30,
                    CAMERON_NORRIE: 1.56
                }
            },
            {
                'round': 16,
                'players': [
                    RADU_ALBOT,
                    TARO_DANIEL,
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    RADU_ALBOT: 1.40,
                    TARO_DANIEL: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    TAYLOR_FRITZ,
                    PRAJNESH_GUNNESWARAN,
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    TAYLOR_FRITZ: 1.30,
                    PRAJNESH_GUNNESWARAN: 3.40,
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 6,
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ERNESTS_GULBIS,
                ],
                'score': [(7, 5), (6, 0)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.26,
                    ERNESTS_GULBIS: 3.80,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    GRIGOR_DIMITROV
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    GUIDO_PELLA: 2.20,
                    GRIGOR_DIMITROV: 1.61,
                }
            },
            {
                'round': 16,
                'players': [
                    THANASI_KOKKINAKIS,
                    LUCAS_POUILLE,
                ],
                'score': [(2, 6), (6, 4), (6, 3)],
                'odds': {
                    THANASI_KOKKINAKIS: 2.20,
                    LUCAS_POUILLE: 1.65,
                },
                'prediction': LUCAS_POUILLE,
                'bet': 4,
            },

            # 2019-08-01
            {
                'round': 16,
                'players': [
                    FABIO_FOGNINI,
                    MARCEL_GRANOLLERS,
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.65,
                    MARCEL_GRANOLLERS: 2.20,
                },
                'prediction': FABIO_FOGNINI,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    RADU_ALBOT,
                    TARO_DANIEL
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    RADU_ALBOT: 1.40,
                    TARO_DANIEL: 2.75
                }
            },
            {
                'round': 16,
                'players': [
                    TAYLOR_FRITZ,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    TAYLOR_FRITZ: 1.16,
                    PRAJNESH_GUNNESWARAN: 4.50,
                }
            },
            {
                'round': 16,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    CAMERON_NORRIE
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 2.20,
                    CAMERON_NORRIE: 1.56,
                }
            },
            {
                'round': 16,
                'players': [
                    THANASI_KOKKINAKIS,
                    LUCAS_POUILLE
                ],
                'score': [(2, 6), (6, 4), (6, 3)],
                'odds': {
                    THANASI_KOKKINAKIS: 2.10,
                    LUCAS_POUILLE: 1.69,
                }
            },
            {
                'round': 16,
                'players': [
                    SOONWOO_KWON,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    SOONWOO_KWON: 1.38,
                    JUAN_IGNACIO_LONDERO: 2.90
                }
            },
            {
                'round': 16,
                'players': [
                    FABIO_FOGNINI,
                    MARCEL_GRANOLLERS
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.71,
                    MARCEL_GRANOLLERS: 1.91
                }
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    GRIGOR_DIMITROV
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    GUIDO_PELLA: 2.20,
                    GRIGOR_DIMITROV: 1.61,
                }
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ERNESTS_GULBIS
                ],
                'score': [(7, 5), (6, 0)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.23,
                    ERNESTS_GULBIS: 3.85,
                },
            },

            # 2019-08-01
            {
                'round': 8,
                'players': [
                    RADU_ALBOT,
                    THANASI_KOKKINAKIS
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    RADU_ALBOT: 1.80,
                    THANASI_KOKKINAKIS: 1.92,
                },
            },
            {
                'round': 8,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.51,
                    MIKHAIL_KUKUSHKIN: 2.50,
                }
            },
            {
                'round': 8,
                'players': [
                    GUIDO_PELLA,
                    SOONWOO_KWON
                ],
                'score': [(4, 6), (6, 1), (6, 2)],
                'odds': {
                    GUIDO_PELLA: 1.59,
                    SOONWOO_KWON: 2.16,
                },
            },
            {
                'round': 8,
                'players': [
                    TAYLOR_FRITZ,
                    FABIO_FOGNINI
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    TAYLOR_FRITZ: 1.61,
                    FABIO_FOGNINI: 2.20,
                },
            },

            # 2019-08-02
            {
                'round': 4,
                'players': [
                    TAYLOR_FRITZ,
                    RADU_ALBOT
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    TAYLOR_FRITZ: 1.53,
                    RADU_ALBOT: 2.45,
                },
            },
            {
                'round': 4,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    GUIDO_PELLA
                ],
                'score': [(6, 3), (3, 6), (6, 1)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.52,
                    GUIDO_PELLA: 2.50,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 4,
            },

            # 2019-08-03
            {
                'round': 2,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    TAYLOR_FRITZ,
                ],
                'score': [(7, 6), (6, 3)],
                # no odds
            }
        ]
    },

    {
        'location': KITZBUHEL,
        'date': '2019-08-03',
        'matches': [

            # 2019-07-27
            {
                'round': 512,
                'players': [
                    YANNICK_HANFMANN,
                    CHENG_PENG_HSIEH
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    YANNICK_HANFMANN: 1.02,
                    CHENG_PENG_HSIEH: 12.60
                }
            },
            {
                'round': 512,
                'players': [
                    ELLIOT_BENCHETRIT,
                    MORITZ_THIEM
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    ELLIOT_BENCHETRIT: 1.03,
                    MORITZ_THIEM: 11.46
                }
            },
            {
                'round': 512,
                'players': [
                    CARLOS_BERLOCQ,
                    MILJAN_ZEKIC
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    CARLOS_BERLOCQ: 1.27,
                    MILJAN_ZEKIC: 3.54
                }
            },
            {
                'round': 512,
                'players': [
                    SANDRO_KOPP,
                    VIKTOR_GALOVIC
                ],
                'score': [(7, 6), (4, 6), (7, 6)],
                'odds': {
                    SANDRO_KOPP: 7.21,
                    VIKTOR_GALOVIC: 1.05
                }
            },
            {
                'round': 512,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    IGOR_ZELENAY
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    GUILLERMO_GARCIA_LOPEZ: 1.02,
                    IGOR_ZELENAY: 10.77
                }
            },
            {
                'round': 512,
                'players': [
                    MATTHIAS_BACHINGER,
                    MARC_ANDREA_HUESLER
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    MATTHIAS_BACHINGER: 1.50,
                    MARC_ANDREA_HUESLER: 2.58
                }
            },
            {
                'round': 512,
                'players': [
                    LUCAS_MIEDLER,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    LUCAS_MIEDLER: 2.30,
                    DENIS_ISTOMIN: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    HUGO_DELLIEN,
                    PEDJA_KRSTIN
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    HUGO_DELLIEN: 1.17,
                    PEDJA_KRSTIN: 4.40
                }
            },

            # 2019-07-28
            {
                'round': 256,
                'players': [
                    HUGO_DELLIEN,
                    SANDRO_KOPP
                ],
                'score': [(4, 6), (6, 1), (6, 2)],
                'odds': {
                    HUGO_DELLIEN: 1.04,
                    SANDRO_KOPP: 10.74
                }
            },
            {
                'round': 256,
                'players': [
                    MATTHIAS_BACHINGER,
                    YANNICK_HANFMANN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MATTHIAS_BACHINGER: 3.40,
                    YANNICK_HANFMANN: 1.23
                }
            },
            {
                'round': 256,
                'players': [
                    LUCAS_MIEDLER,
                    CARLOS_BERLOCQ
                ],
                'score': [(6, 7), (7, 5), (6, 3)],
                'odds': {
                    LUCAS_MIEDLER: 1.65,
                    CARLOS_BERLOCQ: 2.05
                }
            },
            {
                'round': 256,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    ELLIOT_BENCHETRIT
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    GUILLERMO_GARCIA_LOPEZ: 1.41,
                    ELLIOT_BENCHETRIT: 2.60
                }
            },

            # 2019-07-29
            {
                'round': 32,
                'players': [
                    DENNIS_NOVAK,
                    JURIJ_RODIONOV
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DENNIS_NOVAK: 1.21,
                    JURIJ_RODIONOV: 4.35
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    HUGO_DELLIEN
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.69,
                    HUGO_DELLIEN: 2.11
                }
            },
            {
                'round': 32,
                'players': [
                    MATTHIAS_BACHINGER,
                    MARTIN_KLIZAN
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    MATTHIAS_BACHINGER: 2.70,
                    MARTIN_KLIZAN: 1.47
                }
            },
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    FEDERICO_DELBONIS
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    LORENZO_SONEGO: 2.01,
                    FEDERICO_DELBONIS: 1.80
                }
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    MARCO_CECCHINATO
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    JEREMY_CHARDY: 1.76,
                    MARCO_CECCHINATO: 2.00
                }
            },

            # 2019-07-30
            {
                'round': 32,
                'players': [
                    SEBASTIAN_OFNER,
                    LUCAS_MIEDLER
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    SEBASTIAN_OFNER: 2.02,
                    LUCAS_MIEDLER: 1.71
                }
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    THOMAS_FABBIANO
                ],
                'score': [(7, 6), (1, 6), (6, 1)],
                'odds': {
                    JAUME_MUNAR: 1.34,
                    THOMAS_FABBIANO: 3.10
                }
            },
            {
                'round': 32,
                'players': [
                    JOZEF_KOVALIK,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(6, 7), (6, 2), (6, 3)],
                'odds': {
                    JOZEF_KOVALIK: 2.00,
                    GUILLERMO_GARCIA_LOPEZ: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    RICHARD_GASQUET
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.89,
                    RICHARD_GASQUET: 1.80
                }
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(6, 1), (3, 6), (6, 1)],
                'odds': {
                    CASPER_RUUD: 2.10,
                    PABLO_CARRENO_BUSTA: 1.63
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_ANDUJAR,
                    LEONARDO_MAYER
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    PABLO_ANDUJAR: 2.10,
                    LEONARDO_MAYER: 1.67
                }
            },
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 7), (6, 4), (6, 4)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.05,
                    MARTON_FUCSOVICS: 1.74
                }
            },

            # 2019-07-31
            {
                'round': 16,
                'players': [
                    CASPER_RUUD,
                    MATTHIAS_BACHINGER
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    CASPER_RUUD: 1.24,
                    MATTHIAS_BACHINGER: 4.00,
                },
                'prediction': CASPER_RUUD,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    JAUME_MUNAR
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.95,
                    JAUME_MUNAR: 1.85,
                },
                'prediction': JAUME_MUNAR,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    PABLO_ANDUJAR,
                    PHILIPP_KOHLSCHREIBER,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    PABLO_ANDUJAR: 1.85,
                    PHILIPP_KOHLSCHREIBER: 1.95,
                },
                'prediction': PABLO_ANDUJAR,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    LORENZO_SONEGO,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'score': [(2, 6), (7, 6), (7, 6)],
                'odds': {
                    LORENZO_SONEGO: 2.10,
                    ROBERTO_CARBALLES_BAENA: 1.70,
                },
                'prediction': ROBERTO_CARBALLES_BAENA,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    PABLO_CUEVAS,
                    DENNIS_NOVAK,
                ],
                'score': [(6, 7), (6, 0), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 1.48,
                    DENNIS_NOVAK: 2.60,
                },
                'prediction': PABLO_CUEVAS,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    FERNANDO_VERDASCO,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    FERNANDO_VERDASCO: 1.42,
                    JOZEF_KOVALIK: 2.80,
                },
                'prediction': FERNANDO_VERDASCO,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    JEREMY_CHARDY,
                    DUSAN_LAJOVIC
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    JEREMY_CHARDY: 2.15,
                    DUSAN_LAJOVIC: 1.68,
                },
                'prediction': DUSAN_LAJOVIC,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    SEBASTIAN_OFNER
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.06,
                    SEBASTIAN_OFNER: 8.50,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 4,
            },

            # 2019-08-01
            {
                'round': 8,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    JEREMY_CHARDY
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.55,
                    JEREMY_CHARDY: 2.40,
                },
                'prediction': JEREMY_CHARDY,
                'bet': 3,
            },
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    PABLO_ANDUJAR
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 1.16,
                    PABLO_ANDUJAR: 5.00,
                },
                'prediction': PABLO_ANDUJAR,
                'bet': 3,
            },
            {
                'round': 8,
                'players': [
                    LORENZO_SONEGO,
                    FERNANDO_VERDASCO,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 2.10,
                    FERNANDO_VERDASCO: 1.70,
                },
                'prediction': LORENZO_SONEGO,
                'bet': 3,
            },
            {
                'round': 8,
                'players': [
                    CASPER_RUUD,
                    PABLO_CUEVAS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    CASPER_RUUD: 2.05,
                    PABLO_CUEVAS: 1.75,
                },
                'prediction': CASPER_RUUD,
                'bet': 4,
            },

            # 2019-08-02
            {
                'round': 4,
                'players': [
                    DOMINIC_THIEM,
                    LORENZO_SONEGO
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 1.14,
                    LORENZO_SONEGO: 5.50,
                },
                'prediction': LORENZO_SONEGO,
                'bet': 3,
            },
            {
                'round': 4,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    CASPER_RUUD,
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.55,
                    CASPER_RUUD: 2.40,
                },
                'prediction': CASPER_RUUD,
                'bet': 4,
            },

            # 2019-08-03
            {
                'round': 2,
                'players': [
                    DOMINIC_THIEM,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    DOMINIC_THIEM: 1.22,
                    ALBERT_RAMOS_VINOLAS: 4.20,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 4,
            }
        ]
    },

    {
        'location': MONTREAL,
        'date': '2019-08-11',
        'matches': [

            # 2019-08-03
            {
                'round': 512,
                'players': [
                    MARC_POLMANS,
                    ANDREY_RUBLEV
                ],
                'score': [(1, 6), (7, 5), (7, 6)],
                'odds': {
                    MARC_POLMANS: 4.25,
                    ANDREY_RUBLEV: 1.22
                }
            },
            {
                'round': 512,
                'players': [
                    BERNARD_TOMIC,
                    ERNESTS_GULBIS
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    BERNARD_TOMIC: 1.56,
                    ERNESTS_GULBIS: 2.15
                }
            },
            {
                'round': 512,
                'players': [
                    BRADLEY_KLAHN,
                    VIKTOR_TROICKI
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    BRADLEY_KLAHN: 1.63,
                    VIKTOR_TROICKI: 1.87
                }
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 4), (5, 7), (6, 4)],
                'odds': {
                    TOMMY_PAUL: 1.71,
                    ALEXEI_POPYRIN: 1.82
                }
            },
            {
                'round': 512,
                'players': [
                    SOONWOO_KWON,
                    ROBIN_HAASE
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    SOONWOO_KWON: 1.59,
                    ROBIN_HAASE: 2.21
                }
            },
            {
                'round': 512,
                'players': [
                    ILYA_IVASHKA,
                    LLOYD_HARRIS
                ],
                'score': [(5, 7), (6, 2), (6, 4)],
                'odds': {
                    ILYA_IVASHKA: 2.15,
                    LLOYD_HARRIS: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    MARCEL_GRANOLLERS,
                    MARIUS_COPIL
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.67,
                    MARIUS_COPIL: 1.87
                }
            },
            {
                'round': 512,
                'players': [
                    IVO_KARLOVIC,
                    EVGENY_DONSKOY
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    IVO_KARLOVIC: 1.71,
                    EVGENY_DONSKOY: 1.87
                }
            },
            {
                'round': 512,
                'players': [
                    RICARDAS_BERANKIS,
                    ALEXIS_GALARNEAU
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    RICARDAS_BERANKIS: 1.24,
                    ALEXIS_GALARNEAU: 3.68
                }
            },
            {
                'round': 512,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    MALEK_JAZIRI
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.24,
                    MALEK_JAZIRI: 3.80
                }
            },
            {
                'round': 512,
                'players': [
                    STEVEN_DIEZ,
                    ALEXANDER_BUBLIK
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    STEVEN_DIEZ: 2.60,
                    ALEXANDER_BUBLIK: 1.44
                }
            },
            {
                'round': 512,
                'players': [
                    JOHN_MILLMAN,
                    FILIP_PELIWO
                ],
                'score': [(6, 1), (6, 0)],
                'odds': {
                    JOHN_MILLMAN: 1.09,
                    FILIP_PELIWO: 6.05
                }
            },
            {
                'round': 512,
                'players': [
                    FELICIANO_LOPEZ,
                    GREGOIRE_BARRERE
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    FELICIANO_LOPEZ: 1.53,
                    GREGOIRE_BARRERE: 2.35
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_EVANS,
                    THAI_SON_KWIATKOWSKI
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    DANIEL_EVANS: 1.19,
                    THAI_SON_KWIATKOWSKI: 4.40
                }
            },

            # 2019-08-04
            {
                'round': 256,
                'players': [
                    BERNARD_TOMIC,
                    MARC_POLMANS
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    BERNARD_TOMIC: 1.43,
                    MARC_POLMANS: 2.45
                }
            },
            {
                'round': 256,
                'players': [
                    TOMMY_PAUL,
                    RICARDAS_BERANKIS
                ],
                'score': [(4, 6), (7, 6), (6, 3)],
                'odds': {
                    TOMMY_PAUL: 1.63,
                    RICARDAS_BERANKIS: 2.00
                }
            },
            {
                'round': 256,
                'players': [
                    ILYA_IVASHKA,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    ILYA_IVASHKA: 3.45,
                    YOSHIHITO_NISHIOKA: 1.24
                }
            },
            {
                'round': 256,
                'players': [
                    SOONWOO_KWON,
                    JOHN_MILLMAN
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    SOONWOO_KWON: 2.20,
                    JOHN_MILLMAN: 1.56
                }
            },
            {
                'round': 256,
                'players': [
                    FELICIANO_LOPEZ,
                    IVO_KARLOVIC
                ],
                'score': [],
                'retired': True,
                'odds': {
                    FELICIANO_LOPEZ: 1.74,
                    IVO_KARLOVIC: 1.91
                }
            },
            {
                'round': 256,
                'players': [
                    DANIEL_EVANS,
                    MARCEL_GRANOLLERS
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    DANIEL_EVANS: 1.40,
                    MARCEL_GRANOLLERS: 2.60
                }
            },
            {
                'round': 256,
                'players': [
                    BRADLEY_KLAHN,
                    STEVEN_DIEZ
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    BRADLEY_KLAHN: 1.41,
                    STEVEN_DIEZ: 2.55
                }
            },

            # 2019-08-05
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    GRIGOR_DIMITROV
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    STAN_WAWRINKA: 1.37,
                    GRIGOR_DIMITROV: 2.90
                }
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.35,
                    JO_WILFRIED_TSONGA: 1.58,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    TOMMY_PAUL,
                    BRAYDEN_SCHNUR
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    TOMMY_PAUL: 1.50,
                    BRAYDEN_SCHNUR: 2.48
                }
            },
            {
                'round': 64,
                'players': [
                    CAMERON_NORRIE,
                    MARTON_FUCSOVICS,
                ],
                'score': [(5, 7), (6, 2), (6, 3)],
                'odds': {
                    CAMERON_NORRIE: 1.80,
                    MARTON_FUCSOVICS: 2.00,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    ADRIAN_MANNARINO,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ADRIAN_MANNARINO: 1.84,
                    MIKHAIL_KUKUSHKIN: 1.88,
                }
            },
            {
                'round': 64,
                'players': [
                    ILYA_IVASHKA,
                    SOONWOO_KWON
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ILYA_IVASHKA: 2.56,
                    SOONWOO_KWON: 1.43
                }
            },
            {
                'round': 64,
                'players': [
                    RICHARD_GASQUET,
                    BENOIT_PAIRE,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    RICHARD_GASQUET: 2.20,
                    BENOIT_PAIRE: 1.65,
                }
            },
            {
                'round': 64,
                'players': [
                    CHRISTIAN_GARIN,
                    LASLO_DJERE,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    CHRISTIAN_GARIN: 1.75,
                    LASLO_DJERE: 2.05,
                },
                'prediction': LASLO_DJERE,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    MILOS_RAONIC,
                    LUCAS_POUILLE,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MILOS_RAONIC: 1.38,
                    LUCAS_POUILLE: 3.00,
                },
                'prediction': MILOS_RAONIC,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    DUSAN_LAJOVIC
                ],
                'score': [(3, 6), (6, 4), (6, 4)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.58,
                    DUSAN_LAJOVIC: 2.35,
                },
                'prediction': DUSAN_LAJOVIC,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    BERNARD_TOMIC
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.14,
                    BERNARD_TOMIC: 5.50
                }
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    PIERRE_HUGUES_HERBERT,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.45,
                    PIERRE_HUGUES_HERBERT: 2.55,
                }
            },

            # 2019-08-06
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MARCO_CECCHINATO,
                ],
                'score': [(3, 6), (7, 6), (6, 4)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.22,
                    MARCO_CECCHINATO: 4.20,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    JOHN_MILLMAN,
                    FELICIANO_LOPEZ
                ],
                'score': [(6, 7), (7, 6), (6, 3)],
                'odds': {
                    JOHN_MILLMAN: 1.59,
                    FELICIANO_LOPEZ: 2.30,
                },
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    HUBERT_HURKACZ: 1.70,
                    TAYLOR_FRITZ: 2.10,
                },
                'prediction': HUBERT_HURKACZ,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    DANIEL_EVANS,
                    ALEX_DE_MINAUR,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DANIEL_EVANS: 2.50,
                    ALEX_DE_MINAUR: 1.52,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    KYLE_EDMUND,
                    NICK_KYRGIOS,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    KYLE_EDMUND: 1.80,
                    NICK_KYRGIOS: 2.00,
                },
                'prediction': NICK_KYRGIOS,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    VASEK_POSPISIL
                ],
                'score': [(6, 2), (6, 7), (7, 6)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.16,
                    VASEK_POSPISIL: 5.00,
                },
                'prediction': VASEK_POSPISIL,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    RADU_ALBOT,
                    GILLES_SIMON
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    RADU_ALBOT: 2.00,
                    GILLES_SIMON: 1.71,
                },
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    DAVID_GOFFIN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    GUIDO_PELLA: 2.80,
                    DAVID_GOFFIN: 1.42,
                },
                'prediction': GUIDO_PELLA,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    MARIN_CILIC,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    MARIN_CILIC: 1.28,
                    BRADLEY_KLAHN: 3.60,
                },
                'prediction': MARIN_CILIC,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    JOHN_ISNER,
                    JORDAN_THOMPSON,
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.45,
                    JORDAN_THOMPSON: 2.70,
                },
                'prediction': JOHN_ISNER,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    BORNA_CORIC,
                    PETER_GOJOWCZYK
                ],
                'score': [(2, 6), (6, 1), (7, 6)],
                'odds': {
                    BORNA_CORIC: 1.36,
                    PETER_GOJOWCZYK: 3.10,
                },
                'prediction': BORNA_CORIC,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(2, 6), (6, 2), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.50,
                    JAN_LENNARD_STRUFF: 1.52,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    CAMERON_NORRIE,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.30,
                    CAMERON_NORRIE: 3.40,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 3,
            },

            # 2018-08-07
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    RADU_ALBOT,
                ],
                'score': [(6, 3), (2, 6), (7, 6)],
                'odds': {
                    GUIDO_PELLA: 1.65,
                    RADU_ALBOT: 2.25,
                },
                'prediction': GUIDO_PELLA,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    MILOS_RAONIC
                ],
                'score': [(6, 3), (3, 6), (0, 0)],
                'retired': True,
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.30,
                    MILOS_RAONIC: 1.60,
                },
                # bet refunded
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    ILYA_IVASHKA,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    GAEL_MONFILS: 1.24,
                    ILYA_IVASHKA: 4.00,
                },
                'prediction': GAEL_MONFILS,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    MARIN_CILIC,
                    JOHN_MILLMAN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MARIN_CILIC: 1.32,
                    JOHN_MILLMAN: 3.30,
                },
                'prediction': MARIN_CILIC,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    CHRISTIAN_GARIN,
                    JOHN_ISNER
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    CHRISTIAN_GARIN: 3.20,
                    JOHN_ISNER: 1.34,
                },
                'prediction': JOHN_ISNER,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    ADRIAN_MANNARINO,
                    BORNA_CORIC,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    ADRIAN_MANNARINO: 2.90,
                    BORNA_CORIC: 1.40,
                },
                'prediction': BORNA_CORIC,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.42,
                    DIEGO_SCHWARTZMAN: 2.90,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    DANIIL_MEDVEDEV,
                    KYLE_EDMUND
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.48,
                    KYLE_EDMUND: 2.50,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    KEI_NISHIKORI
                ],
                'score': [(6, 7), (6, 2), (7, 6)],
                'odds': {
                    RICHARD_GASQUET: 3.60,
                    KEI_NISHIKORI: 1.28,
                },
                'prediction': KEI_NISHIKORI,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    DENIS_SHAPOVALOV,
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    DOMINIC_THIEM: 1.60,
                    DENIS_SHAPOVALOV: 2.30,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    DANIEL_EVANS
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.08,
                    DANIEL_EVANS: 7.50,
                },
                'prediction': RAFAEL_NADAL,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    STAN_WAWRINKA
                ],
                'score': [(6, 4), (6, 7), (6, 2)],
                'odds': {
                    KAREN_KHACHANOV: 2.30,
                    STAN_WAWRINKA: 1.60
                },
                'prediction': STAN_WAWRINKA,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    TOMMY_PAUL,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    FABIO_FOGNINI: 1.62,
                    TOMMY_PAUL: 2.25,
                },
                'prediction': TOMMY_PAUL,
                'bet': 4,
            },

            # 2019-08-08
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    MARIN_CILIC,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 1.75,
                    MARIN_CILIC: 2.05,
                },
                'prediction': MARIN_CILIC,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    DANIIL_MEDVEDEV,
                    CHRISTIAN_GARIN
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.16,
                    CHRISTIAN_GARIN: 5.00,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(7, 5), (5, 7), (7, 6)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.42,
                    NIKOLOZ_BASILASHVILI: 2.80,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    GUIDO_PELLA,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.05,
                    GUIDO_PELLA: 9.00,
                },
                'prediction': RAFAEL_NADAL,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    RICHARD_GASQUET,
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.26,
                    RICHARD_GASQUET: 3.80,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    KAREN_KHACHANOV,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 7), (7, 5), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 1.65,
                    FELIX_AUGER_ALIASSIME: 2.15
                }
            },
            {
                'round': 16,
                'players': [
                    FABIO_FOGNINI,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    FABIO_FOGNINI: 1.83,
                    ADRIAN_MANNARINO: 1.95
                }
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    GAEL_MONFILS: 2.20,
                    HUBERT_HURKACZ: 1.62
                }
            },

            # 2019-08-09
            {
                'round': 8,
                'players': [
                    DANIIL_MEDVEDEV,
                    DOMINIC_THIEM
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.60,
                    DOMINIC_THIEM: 2.30,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    KAREN_KHACHANOV,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 1.85,
                    ALEXANDER_ZVEREV: 1.95,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 3,
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    FABIO_FOGNINI
                ],
                'score': [(2, 6), (6, 1), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.12,
                    FABIO_FOGNINI: 6.00,
                },
                'prediction': RAFAEL_NADAL,
                'bet': 3,
            },
            {
                'round': 8,
                'players': [
                    GAEL_MONFILS,
                    ROBERTO_BAUTISTA_AGUT,
                ],
                'score': [(6, 4), (3, 6), (7, 6)],
                'odds': {
                    GAEL_MONFILS: 2.20,
                    ROBERTO_BAUTISTA_AGUT: 1.65,
                },
                'prediction': GAEL_MONFILS,
                'bet': 3,
            },

            # 2019-08-10
            {
                'round': 4,
                'players': [
                    DANIIL_MEDVEDEV,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.49,
                    KAREN_KHACHANOV: 2.55
                }
            },
            {
                'round': 4,
                'players': [
                    RAFAEL_NADAL,
                    GAEL_MONFILS
                ],
                'score': [],
                'retired': True,
                'odds': {
                    RAFAEL_NADAL: 1.05,
                    GAEL_MONFILS: 11.00
                }
            },

            # 2019-08-11
            {
                'round': 2,
                'players': [
                    RAFAEL_NADAL,
                    DANIIL_MEDVEDEV,
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    RAFAEL_NADAL: 1.40,
                    DANIIL_MEDVEDEV: 2.90,
                },
            }
        ]
    },

    {
        'location': CINCINNATI,
        'date': '2019-08-18',
        'matches': [

            # 2019-08-10
            {
                'round': 512,
                'players': [
                    JJ_WOLF,
                    ALEXANDER_BUBLIK
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    JJ_WOLF: 2.80,
                    ALEXANDER_BUBLIK: 1.37
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREY_RUBLEV,
                    BERNARD_TOMIC
                ],
                'score': [(2, 1)],
                'retired': True,
                'odds': {
                    ANDREY_RUBLEV: 1.41,
                    BERNARD_TOMIC: 2.72
                }
            },
            {
                'round': 512,
                'players': [
                    FELICIANO_LOPEZ,
                    LLOYD_HARRIS
                ],
                'score': [(3, 6), (6, 2), (6, 2)],
                'odds': {
                    FELICIANO_LOPEZ: 1.60,
                    LLOYD_HARRIS: 2.18
                }
            },
            {
                'round': 512,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    JOHN_MILLMAN
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.85,
                    JOHN_MILLMAN: 1.77
                }
            },
            {
                'round': 512,
                'players': [
                    FEDERICO_DELBONIS,
                    JOHN_MCNALLY
                ],
                'score': [(3, 6), (6, 0), (6, 2)],
                'odds': {
                    FEDERICO_DELBONIS: 1.20,
                    JOHN_MCNALLY: 3.91
                }
            },
            {
                'round': 512,
                'players': [
                    DENIS_KUDLA,
                    CAMERON_NORRIE
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DENIS_KUDLA: 3.06,
                    CAMERON_NORRIE: 1.29
                }
            },
            {
                'round': 512,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ANTOINE_HOANG
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.25,
                    ANTOINE_HOANG: 3.80
                }
            },
            {
                'round': 512,
                'players': [
                    CASPER_RUUD,
                    BRADLEY_KLAHN
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    CASPER_RUUD: 2.03,
                    BRADLEY_KLAHN: 1.67
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    ALEXEI_POPYRIN: 2.20,
                    MARTON_FUCSOVICS: 1.59
                }
            },
            {
                'round': 512,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    DANIEL_EVANS
                ],
                'score': [(7, 6), (1, 6), (6, 1)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 2.58,
                    DANIEL_EVANS: 1.36
                }
            },
            {
                'round': 512,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    MARIUS_COPIL
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.33,
                    MARIUS_COPIL: 2.86
                }
            },
            {
                'round': 512,
                'players': [
                    JOAO_SOUSA,
                    SEBASTIAN_KORDA
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    JOAO_SOUSA: 1.27,
                    SEBASTIAN_KORDA: 3.45
                }
            },
            {
                'round': 512,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    JACK_SOCK
                ],
                'score': [(6, 7), (6, 2), (6, 3)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.69,
                    JACK_SOCK: 2.04
                }
            },
            {
                'round': 512,
                'players': [
                    IVO_KARLOVIC,
                    TENNYS_SANDGREN
                ],
                'score': [(4, 6), (6, 4), (7, 6)],
                'odds': {
                    IVO_KARLOVIC: 2.15,
                    TENNYS_SANDGREN: 1.63
                }
            },

            # 2019-08-11
            {
                'round': 256,
                'players': [
                    DENIS_KUDLA,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 3), (4, 6), (6, 3)],
                'odds': {
                    DENIS_KUDLA: 2.60,
                    ALEXEI_POPYRIN: 1.46,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    CASPER_RUUD,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 7), (7, 5), (6, 3)],
                'odds': {
                    CASPER_RUUD: 1.46,
                    FEDERICO_DELBONIS: 2.40
                },
                'prediction': CASPER_RUUD,
                'bet': 4,
            },
            {
                'round': 256,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JJ_WOLF
                ],
                'score': [(6, 3), (4, 6), (6, 2)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.22,
                    JJ_WOLF: 4.00,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    MIOMIR_KECMANOVIC,
                    FELICIANO_LOPEZ
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.62,
                    FELICIANO_LOPEZ: 2.20
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 6,
            },
            {
                'round': 256,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    JOAO_SOUSA,
                ],
                'score': [(6, 4), (0, 6), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.62,
                    JOAO_SOUSA: 2.20,
                },
                'prediction': JOAO_SOUSA,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    ALEX_DE_MINAUR,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 7), (6, 1), (6, 2)],
                'odds': {
                    ALEX_DE_MINAUR: 1.18,
                    MARCO_CECCHINATO: 4.60
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    ANDREY_RUBLEV,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 1.75,
                    MIKHAIL_KUKUSHKIN: 2.10,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    JOHN_ISNER,
                    DUSAN_LAJOVIC,
                ],
                'score': [(7, 6), (1, 6), (7, 5)],
                'odds': {
                    JOHN_ISNER: 1.28,
                    DUSAN_LAJOVIC: 3.60,
                },
                'prediction': JOHN_ISNER,
                'bet': 2,
            },
            {
                'round': 512,
                'players': [
                    IVO_KARLOVIC,
                    PHILIPP_KOHLSCHREIBER,
                ],
                'score': [(7, 6), (6, 7), (6, 4)],
                'odds': {
                    IVO_KARLOVIC: 2.55,
                    PHILIPP_KOHLSCHREIBER: 1.41,
                },
            },

            # 2018-08-12
            {
                'round': 64,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    MATTEO_BERRETTINI,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 3.00,
                    MATTEO_BERRETTINI: 1.38,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    RADU_ALBOT,
                    MARIN_CILIC,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    RADU_ALBOT: 3.30,
                    MARIN_CILIC: 1.32,
                },
                'prediction': MARIN_CILIC,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ADRIAN_MANNARINO,
                    CHRISTIAN_GARIN,
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    ADRIAN_MANNARINO: 1.80,
                    CHRISTIAN_GARIN: 2.00,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    RICHARD_GASQUET,
                    ANDY_MURRAY,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    RICHARD_GASQUET: 1.55,
                    ANDY_MURRAY: 2.40,
                },
                'prediction': RICHARD_GASQUET,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    SAM_QUERREY,
                    PIERRE_HUGUES_HERBERT,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    SAM_QUERREY: 1.62,
                    PIERRE_HUGUES_HERBERT: 2.25,
                },
                'prediction': SAM_QUERREY,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    LUCAS_POUILLE,
                    DENIS_KUDLA,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    LUCAS_POUILLE: 1.53,
                    DENIS_KUDLA: 2.35,
                },
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    CASPER_RUUD,
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    GUIDO_PELLA: 1.50,
                    CASPER_RUUD: 2.00,
                },
            },
            {
                'round': 64,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    JORDAN_THOMPSON,
                ],
                'score': [(7, 5), (5, 7), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.65,
                    JORDAN_THOMPSON: 2.10,
                },
            },
            {
                'round': 64,
                'players': [
                    MIOMIR_KECMANOVIC,
                    FELIX_AUGER_ALIASSIME,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.25,
                    FELIX_AUGER_ALIASSIME: 1.57,
                },
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    IVO_KARLOVIC,
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.33,
                    IVO_KARLOVIC: 3.00,
                },
            },
            {
                'round': 64,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    GILLES_SIMON,
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.65,
                    GILLES_SIMON: 2.25
                }
            },
            {
                'round': 64,
                'players': [
                    NICK_KYRGIOS,
                    LORENZO_SONEGO,
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    NICK_KYRGIOS: 1.32,
                    LORENZO_SONEGO: 3.30,
                },
                'prediction': NICK_KYRGIOS,
                'bet': 2,
            },

            # 2019-08-13
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    GRIGOR_DIMITROV,
                ],
                'score': [(5, 7), (6, 4), (7, 6)],
                'odds': {
                    STAN_WAWRINKA: 1.36,
                    GRIGOR_DIMITROV: 3.10,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 4), (4, 6), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 1.70,
                    TAYLOR_FRITZ: 2.10,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    LASLO_DJERE,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.20,
                    LASLO_DJERE: 4.40,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    DANIIL_MEDVEDEV,
                    KYLE_EDMUND,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.42,
                    KYLE_EDMUND: 2.80,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    FRANCES_TIAFOE,
                    GAEL_MONFILS,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    FRANCES_TIAFOE: 1.95,
                    GAEL_MONFILS: 1.85,
                },
                'prediction': GAEL_MONFILS,
                'bet': 0,  # 6 refunded
            },
            {
                'round': 64,
                'players': [
                    BENOIT_PAIRE,
                    FERNANDO_VERDASCO,
                ],
                'score': [(6, 4), (0, 0)],
                'retired': True,
                'odds': {
                    BENOIT_PAIRE: 1.80,
                    FERNANDO_VERDASCO: 2.00,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 0,  # refunded
            },
            {
                'round': 64,
                'players': [
                    REILLY_OPELKA,
                    BORNA_CORIC,
                ],
                'score': [(4, 6), (6, 3), (7, 5)],
                'odds': {
                    REILLY_OPELKA: 1.75,
                    BORNA_CORIC: 2.05,
                },
                'prediction': REILLY_OPELKA,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    ANDREY_RUBLEV,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(6, 7), (6, 3), (7, 5)],
                'odds': {
                    ANDREY_RUBLEV: 2.15,
                    NIKOLOZ_BASILASHVILI: 1.68,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    HUBERT_HURKACZ,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.52,
                    HUBERT_HURKACZ: 2.50,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    JOAO_SOUSA,
                ],
                'score': [(2, 6), (6, 3), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.48,
                    JOAO_SOUSA: 2.60,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 2,
                # previous opponent refunded
            },
            {
                'round': 64,
                'players': [
                    NOVAK_DJOKOVIC,
                    SAM_QUERREY,
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.09,
                    SAM_QUERREY: 7.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ROGER_FEDERER,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.03,
                    JUAN_IGNACIO_LONDERO: 11.00,
                },
                'prediction': ROGER_FEDERER,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JOHN_ISNER,
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 2.20,
                    JOHN_ISNER: 1.65,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 2,
            },

            # 2018-08-14
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    RADU_ALBOT
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.62,
                    RADU_ALBOT: 2.15
                }
            },
            {
                'round': 32,
                'players': [
                    ADRIAN_MANNARINO,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    ADRIAN_MANNARINO: 1.54,
                    MIKHAIL_KUKUSHKIN: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    FEDERICO_DELBONIS
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    RICHARD_GASQUET: 1.30,
                    FEDERICO_DELBONIS: 3.20
                }
            },
            {
                'round': 32,
                'players': [
                    ALEX_DE_MINAUR,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ALEX_DE_MINAUR: 1.65,
                    REILLY_OPELKA: 2.10

                }
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    STAN_WAWRINKA
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 2.30,
                    STAN_WAWRINKA: 1.55
                }
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    GUIDO_PELLA
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    DAVID_GOFFIN: 1.53,
                    GUIDO_PELLA: 2.35
                }
            },
            {
                'round': 32,
                'players': [
                    DANIIL_MEDVEDEV,
                    BENOIT_PAIRE
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.25,
                    BENOIT_PAIRE: 3.45
                }
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ALEXANDER_ZVEREV
                ],
                'score': [(6, 7), (6, 2), (6, 4)],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.30,
                    ALEXANDER_ZVEREV: 1.55
                }
            },
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    KEI_NISHIKORI
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 3.20,
                    KEI_NISHIKORI: 1.30
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.30,
                    STEFANOS_TSITSIPAS: 1.51
                }
            },
            {
                'round': 32,
                'players': [
                    LUCAS_POUILLE,
                    DENIS_SHAPOVALOV
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    LUCAS_POUILLE: 2.40,
                    DENIS_SHAPOVALOV: 1.50
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 3), (3, 6), (6, 1)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    NICK_KYRGIOS
                ],
                'score': [(6, 7), (7, 6), (6, 2)]
                # no odds
            },

            # 2018-08-15
            {
                'round': 16,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    ALEX_DE_MINAUR
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.70,
                    ALEX_DE_MINAUR: 1.45,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    RICHARD_GASQUET,
                    DIEGO_SCHWARTZMAN,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    RICHARD_GASQUET: 2.40,
                    DIEGO_SCHWARTZMAN: 1.55,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 8,
            },
            {
                'round': 16,
                'players': [
                    DAVID_GOFFIN,
                    ADRIAN_MANNARINO,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.42,
                    ADRIAN_MANNARINO: 2.80,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    DANIIL_MEDVEDEV,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.40,
                    JAN_LENNARD_STRUFF: 2.80,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    ROGER_FEDERER,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 6.50,
                    ROGER_FEDERER: 1.10,
                },
                'prediction': ROGER_FEDERER,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.34,
                    MIOMIR_KECMANOVIC: 3.20,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    LUCAS_POUILLE,
                    KAREN_KHACHANOV,
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    LUCAS_POUILLE: 2.50,
                    KAREN_KHACHANOV: 1.52,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.02,
                    PABLO_CARRENO_BUSTA: 12.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 2,
            },

            # 2018-08-16
            {
                'round': 8,
                'players': [
                    RICHARD_GASQUET,
                    ROBERTO_BAUTISTA_AGUT,
                ],
                'score': [(7, 6), (3, 6), (6, 2)],
                'odds': {
                    RICHARD_GASQUET: 3.80,
                    ROBERTO_BAUTISTA_AGUT: 1.24,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    DAVID_GOFFIN,
                    YOSHIHITO_NISHIOKA,
                ],
                'score': [],
                'retired': True,
                'odds': {
                    DAVID_GOFFIN: 1.48,
                    YOSHIHITO_NISHIOKA: 2.60,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 0,  # refunded 10,
            },
            {
                'round': 8,
                'players': [
                    DANIIL_MEDVEDEV,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.30,
                    ANDREY_RUBLEV: 3.40,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    NOVAK_DJOKOVIC,
                    LUCAS_POUILLE,
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.03,
                    LUCAS_POUILLE: 10.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 4,
            },

            # 2019-08-17
            {
                'round': 4,
                'players': [
                    DAVID_GOFFIN,
                    RICHARD_GASQUET,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 1.42,
                    RICHARD_GASQUET: 2.80,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 10,
            },
            {
                'round': 4,
                'players': [
                    DANIIL_MEDVEDEV,
                    NOVAK_DJOKOVIC,
                ],
                'score': [(3, 6), (6, 3), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 3.40,
                    NOVAK_DJOKOVIC: 1.30,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 4,
            },

            # 2019-08-18
            {
                'round': 2,
                'players': [
                    DANIIL_MEDVEDEV,
                    DAVID_GOFFIN,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.40,
                    DAVID_GOFFIN: 2.90,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 4,
            }
        ]
    },

    {
        'location': WINSTON_SALEM,
        'date': '2019-08-24',
        'matches': [

            # 2019-08-17
            {
                'round': 512,
                'players': [
                    STRONG_KIRCHHEIMER,
                    KEVIN_KRAWIETZ,
                ],
                'score': [(4, 6), (6, 2), (6, 4)],
                'odds': {
                    STRONG_KIRCHHEIMER: 2.60,
                    KEVIN_KRAWIETZ: 1.44
                }
            },
            {
                'round': 512,
                'players': [
                    BORNA_GOJO,
                    TAHA_BAADI
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    BORNA_GOJO: 1.02,
                    TAHA_BAADI: 7.50
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_NGUYEN,
                    MARCELO_AREVALO
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    PETROS_CHRYSOCHOS,
                    FILIP_PELIWO
                ],
                'score': [(6, 1), (6, 0)],
                'odds': {
                    PETROS_CHRYSOCHOS: 1.61,
                    FILIP_PELIWO: 2.15
                }
            },
            {
                'round': 512,
                'players': [
                    RAYMOND_SARMIENTO,
                    CHRISTOPHER_EUBANKS,
                ],
                'score': [(3, 6), (6, 4), (6, 4)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    MARCOS_GIRON,
                    ROY_SMITH
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    MARCOS_GIRON: 1.18,
                    ROY_SMITH: 4.00
                }
            },
            {
                'round': 512,
                'players': [
                    BJORN_FRATANGELO,
                    JURGEN_MELZER
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    BJORN_FRATANGELO: 1.22,
                    JURGEN_MELZER: 3.50
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    KEVIN_KING
                ],
                'score': [(6, 4), (2, 6), (6, 1)],
                'odds': {
                    DAMIR_DZUMHUR: 1.25,
                    KEVIN_KING: 3.47
                }
            },

            # 2019-08-18
            {
                'round': 256,
                'players': [
                    RAYMOND_SARMIENTO,
                    DANIEL_NGUYEN
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    RAYMOND_SARMIENTO: 1.69,
                    DANIEL_NGUYEN: 1.95
                }
            },
            {
                'round': 256,
                'players': [
                    MARCOS_GIRON,
                    BORNA_GOJO
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MARCOS_GIRON: 1.45,
                    BORNA_GOJO: 2.45
                }
            },
            {
                'round': 256,
                'players': [
                    BJORN_FRATANGELO,
                    PETROS_CHRYSOCHOS
                ],
                'score': [(7, 5), (4, 6), (6, 1)],
                'odds': {
                    BJORN_FRATANGELO: 1.25,
                    PETROS_CHRYSOCHOS: 3.30
                }
            },
            {
                'round': 256,
                'players': [
                    DAMIR_DZUMHUR,
                    STRONG_KIRCHHEIMER
                ],
                'score': [(4, 6), (6, 2), (6, 1)],
                'odds': {
                    DAMIR_DZUMHUR: 1.10,
                    STRONG_KIRCHHEIMER: 5.50
                }
            },
            {
                'round': 64,
                'players': [
                    LLOYD_HARRIS,
                    JAUME_MUNAR
                ],
                'score': [(7, 6), (4, 6), (6, 1)],
                'odds': {
                    LLOYD_HARRIS: 1.65,
                    JAUME_MUNAR: 2.01
                }
            },
            {
                'round': 64,
                'players': [
                    ROBIN_HAASE,
                    DENIS_KUDLA
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ROBIN_HAASE: 1.96,
                    DENIS_KUDLA: 1.70
                }
            },
            {
                'round': 64,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    CEDRIC_MARCEL_STEBE
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 1.60,
                    CEDRIC_MARCEL_STEBE: 2.16
                }
            },
            {
                'round': 64,
                'players': [
                    TOMAS_BERDYCH,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 1), (3, 6), (6, 3)],
                'odds': {
                    TOMAS_BERDYCH: 1.71,
                    ANDREAS_SEPPI: 1.95
                }
            },

            # 2019-08-19
            {
                'round': 64,
                'players': [
                    PABLO_ANDUJAR,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    PABLO_ANDUJAR: 3.10,
                    NICOLAS_JARRY: 1.36,
                },
                'prediction': PABLO_ANDUJAR,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    MARCO_CECCHINATO,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(7, 6), (1, 0)],
                'retired': True,
                'odds': {
                    MARCO_CECCHINATO: 2.10,
                    ALEXANDER_BUBLIK: 1.70,
                },
                'prediction': ALEXANDER_BUBLIK,
                'bet': 0,  # refunded 2,
            },
            {
                'round': 64,
                'players': [
                    DUCKHEE_LEE,
                    HENRI_LAAKSONEN,
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    DUCKHEE_LEE: 1.95,
                    HENRI_LAAKSONEN: 1.85,
                },
                'prediction': DUCKHEE_LEE,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    ALEXEI_POPYRIN,
                    THIAGO_MONTEIRO,
                ],
                'score': [(5, 7), (6, 4), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 1.34,
                    THIAGO_MONTEIRO: 3.20,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    MARCOS_GIRON,
                ],
                'score': [(6, 2), (2, 6), (6, 3)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 2.40,
                    MARCOS_GIRON: 1.55,
                },
                'prediction': ROBERTO_CARBALLES_BAENA,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    JEREMY_CHARDY,
                    RAYMOND_SARMIENTO,
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    JEREMY_CHARDY: 1.26,
                    RAYMOND_SARMIENTO: 3.80,
                },
                'prediction': RAYMOND_SARMIENTO,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    BJORN_FRATANGELO,
                    AMIR_WEINTRAUB,
                ],
                'score': [(6, 0), (6, 0)],
                'odds': {
                    BJORN_FRATANGELO: 1.09,
                    AMIR_WEINTRAUB: 7.00,
                },
                'prediction': BJORN_FRATANGELO,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    TENNYS_SANDGREN,
                    ANDY_MURRAY,
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    TENNYS_SANDGREN: 2.15,
                    ANDY_MURRAY: 1.68,
                },
                'prediction': TENNYS_SANDGREN,
                'bet': 2,
            },

            # 2019-08-20
            {
                'round': 64,
                'players': [
                    ANDREY_RUBLEV,
                    THOMAS_FABBIANO,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ANDREY_RUBLEV: 1.32,
                    THOMAS_FABBIANO: 3.30,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    STEVE_JOHNSON,
                    CORENTIN_MOUTET,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    STEVE_JOHNSON: 1.34,
                    CORENTIN_MOUTET: 3.20,
                },
                'prediction': STEVE_JOHNSON,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    DAMIR_DZUMHUR,
                    ANTOINE_HOANG,
                ],
                'score': [(6, 7), (6, 0), (6, 2)],
                'odds': {
                    DAMIR_DZUMHUR: 1.60,
                    ANTOINE_HOANG: 2.30,
                },
                'prediction': DAMIR_DZUMHUR,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    FELICIANO_LOPEZ,
                    PABLO_ANDUJAR,
                ],
                'score': [(6, 4), (1, 6), (7, 5)],
                'odds': {
                    FELICIANO_LOPEZ: 1.60,
                    PABLO_ANDUJAR: 2.30,
                },
                'prediction': FELICIANO_LOPEZ,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    BJORN_FRATANGELO,
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    UGO_HUMBERT: 1.80,
                    BJORN_FRATANGELO: 2.00,
                },
                'prediction': UGO_HUMBERT,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    MARCO_CECCHINATO,
                ],
                'score': [(6, 7), (6, 4), (6, 3)],
                'odds': {
                    JOHN_MILLMAN: 1.45,
                    MARCO_CECCHINATO: 2.70,
                },
                'prediction': JOHN_MILLMAN,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ALEXEI_POPYRIN,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.55,
                    ALEXEI_POPYRIN: 2.40,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    LLOYD_HARRIS,
                ],
                'score': [(6, 1), (0, 0)],
                'retired': True,
                'odds': {
                    CASPER_RUUD: 1.58,
                    LLOYD_HARRIS: 2.35,
                },
                'prediction': CASPER_RUUD,
                'bet': 0,  # refunded 2,
            },
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    MARIUS_COPIL,
                ],
                'score': [(6, 3), (6, 7), (6, 4)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.30,
                    MARIUS_COPIL: 3.40,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    JEREMY_CHARDY,
                ],
                'score': [(4, 2)],
                'retired': True,
                'odds': {
                    FRANCES_TIAFOE: 1.52,
                    JEREMY_CHARDY: 2.50,
                },
                'prediction': FRANCES_TIAFOE,
                'bet': 0,  # refunded 2,
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'score': [(6, 7), (6, 3), (6, 1)],
                'odds': {
                    ANDREY_RUBLEV: 1.31,
                    ALBERT_RAMOS_VINOLAS: 3.30,
                },
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    TOMAS_BERDYCH,
                ],
                'score': [(3, 6), (7, 5), (6, 1)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.90,
                    TOMAS_BERDYCH: 1.90,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    DAMIR_DZUMHUR,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 1.45,
                    DAMIR_DZUMHUR: 2.75,
                },
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    SAM_QUERREY: 1.26,
                    ROBERTO_CARBALLES_BAENA: 3.80,
                },
                'prediction': SAM_QUERREY,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    STEVE_JOHNSON,
                    DANIEL_EVANS,
                ],
                'score': [(6, 3), (6, 1)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    ROBIN_HAASE,
                    JOAO_SOUSA,
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    ROBIN_HAASE: 2.15,
                    JOAO_SOUSA: 1.68,
                },
                'prediction': JOAO_SOUSA,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    DUCKHEE_LEE,
                ],
                'score': [(4, 6), (6, 0), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 1.20,
                    DUCKHEE_LEE: 4.40,
                },
                'prediction': DUCKHEE_LEE,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    DENIS_SHAPOVALOV,
                    TENNYS_SANDGREN,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.32,
                    TENNYS_SANDGREN: 3.30,
                },
                'prediction': TENNYS_SANDGREN,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    PRAJNESH_GUNNESWARAN,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    BENOIT_PAIRE: 1.48,
                    PRAJNESH_GUNNESWARAN: 2.60,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 2,
            },

            # 2019-08-21
            {
                'round': 16,
                'players': [
                    JOHN_MILLMAN,
                    ROBIN_HAASE,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JOHN_MILLMAN: 1.52,
                    ROBIN_HAASE: 2.50,
                },
                'prediction': ROBIN_HAASE,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    BENOIT_PAIRE,
                    UGO_HUMBERT,
                ],
                'score': [(3, 6), (7, 6), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 1.90,
                    UGO_HUMBERT: 1.90,
                },
                'prediction': UGO_HUMBERT,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    STEVE_JOHNSON,
                    CASPER_RUUD,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    STEVE_JOHNSON: 1.42,
                    CASPER_RUUD: 2.80,
                },
                'prediction': CASPER_RUUD,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    LORENZO_SONEGO,
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.68,
                    LORENZO_SONEGO: 2.15,
                },
                'prediction': LORENZO_SONEGO,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    DENIS_SHAPOVALOV,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.70,
                    MIOMIR_KECMANOVIC: 2.10,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    FELICIANO_LOPEZ,
                ],
                'score': [(6, 3), (3, 1)],
                'retired': True,
                'odds': {
                    HUBERT_HURKACZ: 1.42,
                    FELICIANO_LOPEZ: 2.80,
                },
                'prediction': HUBERT_HURKACZ,
                'bet': 0,  # refunded 2,
            },
            {
                'round': 16,
                'players': [
                    FRANCES_TIAFOE,
                    FILIP_KRAJINOVIC,
                ],
                'score': [(6, 2), (0, 0)],
                'retired': True,
                'odds': {
                    FRANCES_TIAFOE: 1.65,
                    FILIP_KRAJINOVIC: 2.20,
                },
                'prediction': FRANCES_TIAFOE,
                'bet': 0,  # refunded 8,
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    SAM_QUERREY,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    ANDREY_RUBLEV: 2.20,
                    SAM_QUERREY: 1.60,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 2,
            },

            # 2019-08-22
            {
                'round': 8,
                'players': [
                    STEVE_JOHNSON,
                    JOHN_MILLMAN,
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    STEVE_JOHNSON: 1.52,
                    JOHN_MILLMAN: 2.50,
                },
                'prediction': STEVE_JOHNSON,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    DENIS_SHAPOVALOV,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.85,
                    ANDREY_RUBLEV: 1.95,
                },
            },
            {
                'round': 8,
                'players': [
                    HUBERT_HURKACZ,
                    FRANCES_TIAFOE,
                ],
                'score': [(4, 6), (7, 6), (6, 1)],
                'odds': {
                    HUBERT_HURKACZ: 1.80,
                    FRANCES_TIAFOE: 2.00,
                },
                'prediction': FRANCES_TIAFOE,
                'bet': 4,
            },

            # 2019-08-23
            {
                'round': 8,
                'players': [
                    BENOIT_PAIRE,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(7, 6), (1, 6), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 1.93,
                    PABLO_CARRENO_BUSTA: 1.83,
                }
            },
            {
                'round': 4,
                'players': [
                    HUBERT_HURKACZ,
                    DENIS_SHAPOVALOV,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 2.60,
                    DENIS_SHAPOVALOV: 1.50,
                }
            },
            {
                'round': 4,
                'players': [
                    BENOIT_PAIRE,
                    STEVE_JOHNSON,
                ],
                'score': [(1, 6), (6, 0), (6, 0)],
                'odds': {
                    BENOIT_PAIRE: 2.45,
                    STEVE_JOHNSON: 1.54,
                },
            },

            # 2019-08-24
            {
                'round': 2,
                'players': [
                    HUBERT_HURKACZ,
                    BENOIT_PAIRE,
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 1.51,
                    BENOIT_PAIRE: 2.55,
                }
            }
        ]
    },

    {
        'location': US_OPEN,
        'date': '2019-09-08',
        'matches': [

            # 2019-08-22
            {
                'round': 512,
                'players': [
                    LUKAS_ROSOL,
                    SALVATORE_CARUSO,
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    LUKAS_ROSOL: 2.90,
                    SALVATORE_CARUSO: 1.38,
                },
                'prediction': LUKAS_ROSOL,
                'bet': 6,
            },
            {
                'round': 512,
                'players': [
                    NORBERT_GOMBOS,
                    JOAO_MENEZES,
                ],
                'score': [(1, 6), (6, 2), (7, 6)],
                'odds': {
                    NORBERT_GOMBOS: 1.46,
                    JOAO_MENEZES: 2.60,
                },
            },
            {
                'round': 512,
                'players': [
                    EGOR_GERASIMOV,
                    MITCHELL_KRUEGER,
                ],
                'score': [(6, 3), (5, 7), (6, 4)],
                'odds': {
                    EGOR_GERASIMOV: 1.50,
                    MITCHELL_KRUEGER: 2.50,
                },
                'prediction': MITCHELL_KRUEGER,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    PAOLO_LORENZI,
                    ENZO_COUACAUD,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    PAOLO_LORENZI: 2.60,
                    ENZO_COUACAUD: 1.46,
                },
                'prediction': PAOLO_LORENZI,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    SUMIT_NAGAL,
                    PETER_POLANSKY,
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    SUMIT_NAGAL: 2.15,
                    PETER_POLANSKY: 1.65,
                },
                'prediction': PETER_POLANSKY,
                'bet': 8,
            },
            {
                'round': 512,
                'players': [
                    JIRI_VESELY,
                    JASON_JUNG,
                ],
                'score': [(6, 4), (5, 7), (7, 5)],
                'odds': {
                    JIRI_VESELY: 1.72,
                    JASON_JUNG: 2.05,
                },
            },
            {
                'round': 512,
                'players': [
                    ILYA_IVASHKA,
                    RUBEN_BEMELMANS,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    ILYA_IVASHKA: 1.38,
                    RUBEN_BEMELMANS: 2.90,
                },
            },
            {
                'round': 512,
                'players': [
                    EVGENY_DONSKOY,
                    JOAO_DOMINGUES,
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    EVGENY_DONSKOY: 1.30,
                    JOAO_DOMINGUES: 3.30,
                },
            },
            {
                'round': 512,
                'players': [
                    JANNIK_SINNER,
                    VIKTOR_GALOVIC,
                ],
                'score': [(4, 6), (7, 6), (7, 5)],
                'odds': {
                    JANNIK_SINNER: 1.26,
                    VIKTOR_GALOVIC: 3.60,
                },
                'prediction': VIKTOR_GALOVIC,
                'bet': 6,
            },
            {
                'round': 512,
                'players': [
                    TALLON_GRIEKSPOOR,
                    CEM_ILKEL,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    TALLON_GRIEKSPOOR: 1.65,
                    CEM_ILKEL: 2.15,
                },
                'prediction': TALLON_GRIEKSPOOR,
                'bet': 2,
            },
            {
                'round': 512,
                'players': [
                    DARIAN_KING,
                    ADRIAN_MENENDEZ_MACEIRAS,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    DARIAN_KING: 1.50,
                    ADRIAN_MENENDEZ_MACEIRAS: 2.50,
                },
            },
            {
                'round': 512,
                'players': [
                    CONSTANT_LESTIENNE,
                    ALESSANDRO_GIANNESSI,
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    CONSTANT_LESTIENNE: 1.46,
                    ALESSANDRO_GIANNESSI: 2.60,
                },
                'prediction': CONSTANT_LESTIENNE,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    KAMIL_MAJCHRZAK,
                    TOMMY_ROBREDO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.34,
                    TOMMY_ROBREDO: 3.10,
                },
            },
            {
                'round': 512,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    NOAH_RUBIN,
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    GUILLERMO_GARCIA_LOPEZ: 1.62,
                    NOAH_RUBIN: 2.25,
                },
                'prediction': NOAH_RUBIN,
                'bet': 6,
            },
            {
                'round': 512,
                'players': [
                    MARIO_VILELLA_MARTINEZ,
                    AKIRA_SANTILLAN,
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    MARIO_VILELLA_MARTINEZ: 2.90,
                    AKIRA_SANTILLAN: 1.38,
                },
            },
            {
                'round': 512,
                'players': [
                    MARCO_TRUNGELLITI,
                    JAMES_WARD,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    MARCO_TRUNGELLITI: 2.20,
                    JAMES_WARD: 1.62,
                },
                'prediction': JAMES_WARD,
                'bet': 3,
            },

            # 2019-08-23
            {
                'round': 256,
                'players': [
                    ELLIOT_BENCHETRIT,
                    KIMMER_COPPEJANS,
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    ELLIOT_BENCHETRIT: 2.15,
                    KIMMER_COPPEJANS: 1.65,
                },
                'prediction': KIMMER_COPPEJANS,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    TOBIAS_KAMKE,
                    LUKAS_LACKO,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    TOBIAS_KAMKE: 2.60,
                    LUKAS_LACKO: 1.46,
                },
                'prediction': TOBIAS_KAMKE,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    SOONWOO_KWON,
                    STEVEN_DIEZ,
                ],
                'score': [(4, 6), (6, 3), (6, 3)],
                'odds': {
                    SOONWOO_KWON: 1.26,
                    STEVEN_DIEZ: 3.60,
                },
                'prediction': SOONWOO_KWON,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    MARCO_TRUNGELLITI,
                    TALLON_GRIEKSPOOR,
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    MARCO_TRUNGELLITI: 2.70,
                    TALLON_GRIEKSPOOR: 1.44,
                },
                'prediction': TALLON_GRIEKSPOOR,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    DOMINIK_KOEPFER,
                    YASUTAKA_UCHIYAMA,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DOMINIK_KOEPFER: 1.52,
                    YASUTAKA_UCHIYAMA: 2.40,
                },
                'prediction': DOMINIK_KOEPFER,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    JIRI_VESELY,
                    PAOLO_LORENZI,
                ],
                'score': [(6, 4), (5, 7), (7, 6)],
                'odds': {
                    JIRI_VESELY: 1.36,
                    PAOLO_LORENZI: 3.00,
                },
                'prediction': JIRI_VESELY,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    ILYA_IVASHKA,
                    KAMIL_MAJCHRZAK,
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    ILYA_IVASHKA: 1.68,
                    KAMIL_MAJCHRZAK: 2.10,
                },
                'prediction': ILYA_IVASHKA,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    SUMIT_NAGAL,
                    JOAO_MENEZES,
                ],
                'score': [(5, 7), (6, 4), (6, 3)],
                'odds': {
                    SUMIT_NAGAL: 2.50,
                    JOAO_MENEZES: 1.50,
                },
                'prediction': JOAO_MENEZES,
                'bet': 3,
            },
            {
                'round': 256,
                'players': [
                    EGOR_GERASIMOV,
                    LUKAS_ROSOL,
                ],
                'score': [(6, 2), (6, 7), (7, 6)],
                'odds': {
                    EGOR_GERASIMOV: 1.65,
                    LUKAS_ROSOL: 2.15,
                },
                'prediction': EGOR_GERASIMOV,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    HYEON_CHUNG,
                    MIKAEL_YMER,
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    HYEON_CHUNG: 1.36,
                    MIKAEL_YMER: 3.00,
                },
                'prediction': HYEON_CHUNG,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    EVGENY_DONSKOY,
                    DARIAN_KING,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    EVGENY_DONSKOY: 1.60,
                    DARIAN_KING: 2.25,
                },
                'prediction': EVGENY_DONSKOY,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    CONSTANT_LESTIENNE,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    GUILLERMO_GARCIA_LOPEZ: 1.87,
                    CONSTANT_LESTIENNE: 1.87,
                },
                'prediction': CONSTANT_LESTIENNE,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    JANNIK_SINNER,
                    MARIO_VILELLA_MARTINEZ,
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    JANNIK_SINNER: 1.40,
                    MARIO_VILELLA_MARTINEZ: 2.80,
                },
                'prediction': MARIO_VILELLA_MARTINEZ,
                'bet': 2,
            },

            # 2019-08-27
            {
                'round': 128,
                'players': [
                    JENSON_BROOKSBY,
                    TOMAS_BERDYCH,
                ],
                'score': [(6, 1), (2, 6), (6, 4), (6, 4)],
                'odds': {
                    JENSON_BROOKSBY: 3.80,
                    TOMAS_BERDYCH: 1.28,
                },
                'prediction': TOMAS_BERDYCH,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    DUSAN_LAJOVIC,
                    STEVE_DARCIS,
                ],
                'score': [(7, 6), (6, 3), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 1.18,
                    STEVE_DARCIS: 4.60,
                },
                'prediction': STEVE_DARCIS,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    MARTON_FUCSOVICS,
                ],
                'score': [(3, 6), (6, 4), (6, 2), (3, 6), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.62,
                    MARTON_FUCSOVICS: 2.30,
                },
                'prediction': MARTON_FUCSOVICS,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    CHRISTIAN_GARIN,
                    CHRISTOPHER_EUBANKS,
                ],
                'score': [(3, 6), (7, 6), (6, 4), (6, 7), (6, 3)],
                'odds': {
                    CHRISTIAN_GARIN: 1.30,
                    CHRISTOPHER_EUBANKS: 3.40,
                },
                'prediction': CHRISTOPHER_EUBANKS,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    DENIS_KUDLA,
                    JANKO_TIPSAREVIC,
                ],
                'score': [(3, 6), (6, 1), (7, 6), (6, 1)],
                'odds': {
                    DENIS_KUDLA: 1.48,
                    JANKO_TIPSAREVIC: 2.60,
                },
                'prediction': DENIS_KUDLA,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    BRADLEY_KLAHN,
                    THIAGO_MONTEIRO,
                ],
                'score': [(6, 3), (6, 2), (6, 3)],
                'odds': {
                    BRADLEY_KLAHN: 1.55,
                    THIAGO_MONTEIRO: 2.50,
                },
                'prediction': THIAGO_MONTEIRO,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    KEI_NISHIKORI,
                    MARCO_TRUNGELLITI,
                ],
                'score': [(6, 1), (4, 1)],
                'retired': True,
                'odds': {
                    KEI_NISHIKORI: 1.05,
                    MARCO_TRUNGELLITI: 9.00,
                },
                'prediction': MARCO_TRUNGELLITI,
                'bet': 0,  # refunded 4,
            },
            {
                'round': 128,
                'players': [
                    REILLY_OPELKA,
                    FABIO_FOGNINI,
                ],
                'score': [(6, 3), (6, 4), (6, 7), (6, 3)],
                'odds': {
                    REILLY_OPELKA: 1.65,
                    FABIO_FOGNINI: 2.20,
                },
                'prediction': REILLY_OPELKA,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    DANIIL_MEDVEDEV,
                    PRAJNESH_GUNNESWARAN,
                ],
                'score': [(6, 4), (6, 1), (6, 2)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.00,
                    PRAJNESH_GUNNESWARAN: 21.00,
                }
            },
            {
                'round': 128,
                'players': [
                    ALEX_DE_MINAUR,
                    PIERRE_HUGUES_HERBERT,
                ],
                'score': [(6, 4), (6, 2), (6, 7), (7, 5)],
                'odds': {
                    ALEX_DE_MINAUR: 1.24,
                    PIERRE_HUGUES_HERBERT: 4.00,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    DANIEL_EVANS,
                    ADRIAN_MANNARINO,
                ],
                'score': [(6, 4), (6, 3), (2, 6), (6, 3)],
                'odds': {
                    DANIEL_EVANS: 1.95,
                    ADRIAN_MANNARINO: 2.00,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    HUGO_DELLIEN,
                    SOONWOO_KWON,
                ],
                'score': [(6, 3), (6, 4), (2, 6), (2, 3)],
                'retired': True,
                'odds': {
                    HUGO_DELLIEN: 7.00,
                    SOONWOO_KWON: 1.09,
                },
                'prediction': SOONWOO_KWON,
                'bet': 0,  # refunded 1,
            },
            {
                'round': 128,
                'players': [
                    NOVAK_DJOKOVIC,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'score': [(6, 4), (6, 1), (6, 4)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.00,
                    ROBERTO_CARBALLES_BAENA: 21.00,
                },
            },
            {
                'round': 128,
                'players': [
                    MIOMIR_KECMANOVIC,
                    LASLO_DJERE,
                ],
                'score': [(6, 2), (6, 1), (7, 5)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.18,
                    LASLO_DJERE: 4.60,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    LUCAS_POUILLE,
                    PHILIPP_KOHLSCHREIBER,
                ],
                'score': [(6, 3), (7, 6), (4, 6), (6, 3)],
                'odds': {
                    LUCAS_POUILLE: 1.42,
                    PHILIPP_KOHLSCHREIBER: 2.80,
                },
                'prediction': LUCAS_POUILLE,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    DAVID_GOFFIN,
                    CORENTIN_MOUTET,
                ],
                'score': [(6, 3), (3, 6), (6, 4), (6, 0)],
                'odds': {
                    DAVID_GOFFIN: 1.08,
                    CORENTIN_MOUTET: 7.50,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    PAOLO_LORENZI,
                    ZACHARY_SVAJDA,
                ],
                'score': [(3, 6), (6, 7), (6, 4), (7, 6), (6, 2)],
                'odds': {
                    PAOLO_LORENZI: 1.06,
                    ZACHARY_SVAJDA: 8.50,
                },
                'prediction': PAOLO_LORENZI,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    GREGOIRE_BARRERE,
                    CAMERON_NORRIE,
                ],
                'score': [(7, 6), (6, 4), (4, 6), (6, 7), (7, 6)],
                'odds': {
                    GREGOIRE_BARRERE: 3.80,
                    CAMERON_NORRIE: 1.26,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    BORNA_CORIC,
                    EVGENY_DONSKOY,
                ],
                'score': [(7, 6), (6, 4), (6, 0)],
                'odds': {
                    BORNA_CORIC: 1.24,
                    EVGENY_DONSKOY: 4.00,
                },
                'prediction': BORNA_CORIC,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    DOMINIK_KOEPFER,
                    JAUME_MUNAR,
                ],
                'score': [(6, 4), (7, 6), (5, 7), (7, 5)],
                'odds': {
                    DOMINIK_KOEPFER: 1.52,
                    JAUME_MUNAR: 2.50,
                },
                'prediction': DOMINIK_KOEPFER,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    SAM_QUERREY,
                ],
                'score': [(3, 6), (6, 1), (7, 6), (7, 5)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 4.00,
                    SAM_QUERREY: 1.22,
                },
                'prediction': SAM_QUERREY,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    GRIGOR_DIMITROV,
                    ANDREAS_SEPPI,
                ],
                'score': [(6, 1), (6, 7), (6, 4), (6, 3)],
                'odds': {
                    GRIGOR_DIMITROV: 1.30,
                    ANDREAS_SEPPI: 3.40,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    RICARDAS_BERANKIS,
                    JIRI_VESELY,
                ],
                'score': [(4, 6), (7, 6), (3, 6), (7, 6), (6, 4)],
                'odds': {
                    RICARDAS_BERANKIS: 1.65,
                    JIRI_VESELY: 2.20,
                },
                'prediction': RICARDAS_BERANKIS,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    FELICIANO_LOPEZ,
                    TAYLOR_FRITZ,
                ],
                'score': [(3, 6), (6, 4), (6, 3), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 5.00,
                    TAYLOR_FRITZ: 1.16,
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    JEREMY_CHARDY,
                    HUBERT_HURKACZ,
                ],
                'score': [(3, 6), (6, 3), (6, 7), (6, 1), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 3.30,
                    HUBERT_HURKACZ: 1.32,
                },
                'prediction': HUBERT_HURKACZ,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    KAMIL_MAJCHRZAK,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 7), (7, 6), (7, 6), (1, 6), (6, 4)],
                'odds': {
                    KAMIL_MAJCHRZAK: 2.05,
                    NICOLAS_JARRY: 1.75,
                },
                'prediction': KAMIL_MAJCHRZAK,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    MARCOS_GIRON,
                ],
                'score': [(3, 6), (6, 4), (6, 4), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.24,
                    MARCOS_GIRON: 4.00,
                },
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    GUIDO_PELLA,
                ],
                'score': [(6, 3), (4, 6), (7, 6), (6, 3)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.80,
                    GUIDO_PELLA: 2.00,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    PABLO_CUEVAS,
                    JACK_SOCK,
                ],
                'score': [(6, 4), (7, 5), (7, 6)],
                'odds': {
                    PABLO_CUEVAS: 1.68,
                    JACK_SOCK: 2.15,
                },
                'prediction': JACK_SOCK,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    DAMIR_DZUMHUR,
                    ELLIOT_BENCHETRIT,
                ],
                'score': [(4, 6), (6, 2), (6, 3), (6, 0)],
                'odds': {
                    DAMIR_DZUMHUR: 1.42,
                    ELLIOT_BENCHETRIT: 2.80,
                },
                'prediction': ELLIOT_BENCHETRIT,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    STAN_WAWRINKA,
                    JANNIK_SINNER,
                ],
                'score': [(6, 4), (7, 6), (4, 6), (6, 3)],
                'odds': {
                    STAN_WAWRINKA: 1.18,
                    JANNIK_SINNER: 4.60,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    ROGER_FEDERER,
                    SUMIT_NAGAL,
                ],
                'score': [(4, 6), (6, 1), (6, 2), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.00,
                    SUMIT_NAGAL: 21.00,
                },
            },

            # 2019-08-28
            {
                'round': 128,
                'players': [
                    MATTEO_BERRETTINI,
                    RICHARD_GASQUET,
                ],
                'score': [(6, 4), (6, 3), (2, 6), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 2.40,
                    RICHARD_GASQUET: 1.55,
                },
                'prediction': RICHARD_GASQUET,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    ALEXANDER_BUBLIK,
                    SANTIAGO_GIRALDO,
                ],
                'score': [(2, 6), (6, 0), (7, 5), (3, 6), (6, 4)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.62,
                    SANTIAGO_GIRALDO: 2.20,
                },
                'prediction': ALEXANDER_BUBLIK,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    GILLES_SIMON,
                    BJORN_FRATANGELO,
                ],
                'score': [(5, 7), (7, 5), (7, 5), (7, 5)],
                'odds': {
                    GILLES_SIMON: 1.42,
                    BJORN_FRATANGELO: 2.80,
                },
                'prediction': GILLES_SIMON,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    ROBERTO_BAUTISTA_AGUT,
                ],
                'score': [(3, 6), (6, 1), (6, 4), (3, 6), (6, 3)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 8.00,
                    ROBERTO_BAUTISTA_AGUT: 1.07,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    ALEXEI_POPYRIN,
                    FEDERICO_DELBONIS,
                ],
                'score': [(6, 1), (7, 5), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 1.52,
                    FEDERICO_DELBONIS: 2.50,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    LORENZO_SONEGO,
                    MARCEL_GRANOLLERS,
                ],
                'score': [(6, 3), (6, 4), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 1.48,
                    MARCEL_GRANOLLERS: 2.60,
                },
                'prediction': MARCEL_GRANOLLERS,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    ANDREY_RUBLEV,
                    STEFANOS_TSITSIPAS,
                ],
                'score': [(6, 4), (6, 7), (7, 6), (7, 5)],
                'odds': {
                    ANDREY_RUBLEV: 2.90,
                    STEFANOS_TSITSIPAS: 1.40,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    PABLO_ANDUJAR,
                    KYLE_EDMUND,
                ],
                'score': [(3, 6), (7, 6), (7, 5), (5, 7), (6, 2)],
                'odds': {
                    PABLO_ANDUJAR: 4.40,
                    KYLE_EDMUND: 1.20,
                },
                'prediction': KYLE_EDMUND,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    JOHN_ISNER,
                    GUILLERMO_GARCIA_LOPEZ,
                ],
                'score': [(6, 3), (6, 4), (6, 4)],
                'odds': {
                    JOHN_ISNER: 1.18,
                    GUILLERMO_GARCIA_LOPEZ: 5.00,
                },
                'prediction': JOHN_ISNER,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    MARIN_CILIC,
                    MARTIN_KLIZAN,
                ],
                'score': [(6, 3), (6, 2), (7, 6)],
                'odds': {
                    MARIN_CILIC: 1.14,
                    MARTIN_KLIZAN: 5.50,
                },
                'prediction': MARIN_CILIC,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    JORDAN_THOMPSON,
                    JOAO_SOUSA,
                ],
                'score': [(6, 3), (6, 2), (6, 4)],
                'odds': {
                    JORDAN_THOMPSON: 1.68,
                    JOAO_SOUSA: 2.20,
                },
                'prediction': JOAO_SOUSA,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    FERNANDO_VERDASCO,
                    TOBIAS_KAMKE,
                ],
                'score': [(6, 3), (3, 6), (6, 1), (6, 2)],
                'odds': {
                    FERNANDO_VERDASCO: 1.26,
                    TOBIAS_KAMKE: 3.80,
                },
                'prediction': FERNANDO_VERDASCO,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    FILIP_KRAJINOVIC,
                ],
                'score': [(6, 3), (4, 6), (6, 4), (7, 6)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 4.00,
                    FILIP_KRAJINOVIC: 1.22,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    VASEK_POSPISIL,
                    KAREN_KHACHANOV,
                ],
                'score': [(4, 6), (7, 5), (7, 5), (4, 6), (6, 3)],
                'odds': {
                    VASEK_POSPISIL: 6.50,
                    KAREN_KHACHANOV: 1.10,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    THOMAS_FABBIANO,
                    DOMINIC_THIEM,
                ],
                'score': [(6, 4), (3, 6), (6, 3), (6, 2)],
                'odds': {
                    THOMAS_FABBIANO: 5.50,
                    DOMINIC_THIEM: 1.14,
                },
                'prediction': THOMAS_FABBIANO,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    HYEON_CHUNG,
                    ERNESTO_ESCOBEDO,
                ],
                'score': [(3, 6), (6, 4), (6, 7), (6, 4), (6, 2)],
                'odds': {
                    HYEON_CHUNG: 1.22,
                    ERNESTO_ESCOBEDO: 4.20,
                },
                'prediction': HYEON_CHUNG,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    JAN_LENNARD_STRUFF,
                    CASPER_RUUD,
                ],
                'score': [(6, 4), (6, 4), (6, 2)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.32,
                    CASPER_RUUD: 3.30,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    ALEXANDER_ZVEREV,
                    RADU_ALBOT,
                ],
                'score': [(6, 1), (6, 3), (3, 6), (4, 6), (6, 2)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.38,
                    RADU_ALBOT: 3.00,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    EGOR_GERASIMOV,
                    LLOYD_HARRIS,
                ],
                'score': [(7, 5), (7, 6), (7, 6)],
                'odds': {
                    EGOR_GERASIMOV: 1.55,
                    LLOYD_HARRIS: 2.40,
                },
                'prediction': LLOYD_HARRIS,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    MARIUS_COPIL,
                    UGO_HUMBERT,
                ],
                'score': [(6, 3), (5, 7), (7, 6), (4, 6), (6, 1)],
                'odds': {
                    MARIUS_COPIL: 2.90,
                    UGO_HUMBERT: 1.40,
                },
                'prediction': UGO_HUMBERT,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ROBIN_HAASE,
                ],
                'score': [(6, 3), (7, 6), (6, 0)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.24,
                    ROBIN_HAASE: 4.00,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    TENNYS_SANDGREN,
                    JO_WILFRIED_TSONGA,
                ],
                'score': [(1, 6), (6, 7), (6, 4), (7, 6), (7, 5)],
                'odds': {
                    TENNYS_SANDGREN: 3.00,
                    JO_WILFRIED_TSONGA: 1.40,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    ANTOINE_HOANG,
                    LEONARDO_MAYER,
                ],
                'score': [(3, 6), (6, 2), (6, 7), (6, 1), (6, 3)],
                'odds': {
                    ANTOINE_HOANG: 2.35,
                    LEONARDO_MAYER: 1.58,
                },
                'prediction': LEONARDO_MAYER,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    FRANCES_TIAFOE,
                    IVO_KARLOVIC,
                ],
                'score': [(6, 2), (6, 3), (1, 2)],
                'retired': True,
                'odds': {
                    FRANCES_TIAFOE: 1.26,
                    IVO_KARLOVIC: 3.80,
                },
                'prediction': FRANCES_TIAFOE,
                'bet': 0,  # refunded 2,
            },
            {
                'round': 128,
                'players': [
                    THANASI_KOKKINAKIS,
                    ILYA_IVASHKA,
                ],
                'score': [(6, 3), (7, 6), (6, 7), (6, 2)],
                'odds': {
                    THANASI_KOKKINAKIS: 1.85,
                    ILYA_IVASHKA: 2.00,
                },
                'prediction': THANASI_KOKKINAKIS,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    ALJAZ_BEDENE,
                    JOZEF_KOVALIK,
                ],
                'score': [(6, 3), (6, 4), (7, 5)],
                'odds': {
                    ALJAZ_BEDENE: 1.22,
                    JOZEF_KOVALIK: 4.20,
                },
                'prediction': JOZEF_KOVALIK,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    HENRI_LAAKSONEN,
                    MARCO_CECCHINATO,
                ],
                'score': [(7, 6), (7, 6), (2, 6), (3, 6), (7, 6)],
                'odds': {
                    HENRI_LAAKSONEN: 2.35,
                    MARCO_CECCHINATO: 1.58,
                },
                'prediction': HENRI_LAAKSONEN,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    GAEL_MONFILS,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'score': [(7, 6), (6, 4), (6, 3)],
                'odds': {
                    GAEL_MONFILS: 1.24,
                    ALBERT_RAMOS_VINOLAS: 4.00,
                },
                'prediction': GAEL_MONFILS,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    BENOIT_PAIRE,
                    BRAYDEN_SCHNUR,
                ],
                'score': [(6, 2), (6, 4), (6, 4)],
                'odds': {
                    BENOIT_PAIRE: 1.24,
                    BRAYDEN_SCHNUR: 4.00,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    DENIS_SHAPOVALOV,
                    FELIX_AUGER_ALIASSIME,
                ],
                'score': [(6, 1), (6, 1), (6, 4)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.85,
                    FELIX_AUGER_ALIASSIME: 1.90,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    RAFAEL_NADAL,
                    JOHN_MILLMAN,
                ],
                'score': [(6, 3), (6, 2), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    JOHN_MILLMAN: 14.00,
                },
                'prediction': JOHN_MILLMAN,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    NICK_KYRGIOS,
                    STEVE_JOHNSON,
                ],
                'score': [(6, 3), (7, 6), (6, 4)],
                'odds': {
                    NICK_KYRGIOS: 1.32,
                    STEVE_JOHNSON: 3.30,
                },
                'prediction': NICK_KYRGIOS,
                'bet': 2,
            },

            # 2019-08-28
            {
                'round': 64,
                'players': [
                    GRIGOR_DIMITROV,
                    BORNA_CORIC
                ],
                'score': [],
                'retired': True,
                'odds': {
                    GRIGOR_DIMITROV: 2.15,
                    BORNA_CORIC: 1.55
                }
            },
            {
                'round': 64,
                'players': [
                    KEI_NISHIKORI,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 2), (4, 6), (6, 3), (7, 5)],
                'odds': {
                    KEI_NISHIKORI: 1.11,
                    BRADLEY_KLAHN: 6.00
                }
            },
            {
                'round': 64,
                'players': [
                    ROGER_FEDERER,
                    DAMIR_DZUMHUR
                ],
                'score': [(3, 6), (6, 2), (6, 3), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.04,
                    DAMIR_DZUMHUR: 10.00
                }
            },
            {
                'round': 64,
                'players': [
                    KAMIL_MAJCHRZAK,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 7), (6, 4), (2, 6), (6, 4), (6, 1)],
                'odds': {
                    KAMIL_MAJCHRZAK: 2.15,
                    PABLO_CUEVAS: 1.68,
                },
                'prediction': PABLO_CUEVAS,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    DANIIL_MEDVEDEV,
                    HUGO_DELLIEN,
                ],
                'score': [(6, 3), (7, 5), (5, 7), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.02,
                    HUGO_DELLIEN: 12.00,
                },
                'prediction': HUGO_DELLIEN,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    DANIEL_EVANS,
                    LUCAS_POUILLE,
                ],
                'score': [(6, 4), (6, 3), (6, 7), (6, 4)],
                'odds': {
                    DANIEL_EVANS: 1.95,
                    LUCAS_POUILLE: 1.85,
                },
                'prediction': LUCAS_POUILLE,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    PAOLO_LORENZI,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(7, 6), (6, 7), (7, 6), (3, 6), (6, 3)],
                'odds': {
                    PAOLO_LORENZI: 9.00,
                    MIOMIR_KECMANOVIC: 1.05,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    FELICIANO_LOPEZ,
                    YOSHIHITO_NISHIOKA,
                ],
                'score': [(6, 7), (6, 0), (6, 4), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 2.80,
                    YOSHIHITO_NISHIOKA: 1.42,
                },
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    JEREMY_CHARDY,
                ],
                'score': [(6, 4), (6, 3), (6, 7), (6, 3)],
                'odds': {
                    STAN_WAWRINKA: 1.30,
                    JEREMY_CHARDY: 3.40,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 4), (6, 7), (6, 2), (6, 0)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.24,
                    RICARDAS_BERANKIS: 4.00,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    NOVAK_DJOKOVIC,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 4), (7, 6), (6, 1)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.00,
                    JUAN_IGNACIO_LONDERO: 17.00,
                },
                # pred na
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    GREGOIRE_BARRERE,
                ],
                'score': [(6, 2), (6, 2), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.05,
                    GREGOIRE_BARRERE: 9.00,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JENSON_BROOKSBY,
                ],
                'score': [(3, 6), (7, 6), (7, 5), (6, 2)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.22,
                    JENSON_BROOKSBY: 4.20,
                },
                'prediction': JENSON_BROOKSBY,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    DOMINIK_KOEPFER,
                    REILLY_OPELKA,
                ],
                'score': [(6, 4), (6, 4), (7, 6)],
                'odds': {
                    DOMINIK_KOEPFER: 3.00,
                    REILLY_OPELKA: 1.38,
                },
                'prediction': REILLY_OPELKA,
                'bet': 3,
            },

            # 2019-08-29
            {
                'round': 64,
                'players': [
                    ALEX_DE_MINAUR,
                    CHRISTIAN_GARIN
                ],
                'score': [(6, 3), (7, 5), (6, 3)],
                'odds': {
                    ALEX_DE_MINAUR: 1.20,
                    CHRISTIAN_GARIN: 4.00
                }
            },

            # 2019-08-30
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    GREGOIRE_BARRERE,
                ],
                'score': [(6, 2), (6, 2), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.05,
                    GREGOIRE_BARRERE: 10.00,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    KAMIL_MAJCHRZAK,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 7), (6, 4), (2, 6), (6, 4), (6, 1)],
                'odds': {
                    KAMIL_MAJCHRZAK: 2.15,
                    PABLO_CUEVAS: 1.75,
                },
                'prediction': PABLO_CUEVAS,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    DANIEL_EVANS,
                    LUCAS_POUILLE,
                ],
                'score': [(6, 4), (6, 3), (6, 7), (6, 4)],
                'odds': {
                    DANIEL_EVANS: 2.05,
                    LUCAS_POUILLE: 1.80,
                },
                'prediction': LUCAS_POUILLE,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    DENIS_KUDLA,
                    DUSAN_LAJOVIC,
                ],
                'score': [(7, 5), (7, 5), (0, 6), (6, 3)],
                'odds': {
                    DENIS_KUDLA: 2.70,
                    DUSAN_LAJOVIC: 1.45,
                },
                # na
            },
            {
                'round': 64,
                'players': [
                    ALEXANDER_ZVEREV,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 3), (3, 6), (6, 2), (2, 6), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.55,
                    FRANCES_TIAFOE: 2.50,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    MATTEO_BERRETTINI,
                    JORDAN_THOMPSON,
                ],
                'score': [(7, 5), (7, 6), (4, 6), (6, 1)],
                'odds': {
                    MATTEO_BERRETTINI: 1.52,
                    JORDAN_THOMPSON: 2.50,
                },
                'prediction': JORDAN_THOMPSON,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JENSON_BROOKSBY,
                ],
                'score': [(3, 6), (7, 6), (7, 5), (6, 2)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.22,
                    JENSON_BROOKSBY: 4.20,
                },
                'prediction': JENSON_BROOKSBY,
                'bet': 7,
            },
            {
                'round': 64,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 4), (6, 7), (6, 2), (6, 0)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.24,
                    RICARDAS_BERANKIS: 4.00,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    DANIIL_MEDVEDEV,
                    HUGO_DELLIEN,
                ],
                'score': [(6, 3), (7, 5), (5, 7), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.02,
                    HUGO_DELLIEN: 11.00,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    PAOLO_LORENZI,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(7, 6), (6, 7), (7, 6), (3, 6), (6, 3)],
                'odds': {
                    PAOLO_LORENZI: 9.00,
                    MIOMIR_KECMANOVIC: 1.05,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    FELICIANO_LOPEZ,
                    YOSHIHITO_NISHIOKA,
                ],
                'score': [(6, 7), (6, 0), (6, 4), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 2.90,
                    YOSHIHITO_NISHIOKA: 1.40,
                },
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    JEREMY_CHARDY,
                ],
                'score': [(6, 4), (6, 3), (6, 7), (6, 3)],
                'odds': {
                    STAN_WAWRINKA: 1.30,
                    JEREMY_CHARDY: 3.40,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ALJAZ_BEDENE,
                    BENOIT_PAIRE,
                ],
                'score': [(4, 6), (6, 7), (6, 2), (7, 5), (7, 6)],
                'odds': {
                    ALJAZ_BEDENE: 3.00,
                    BENOIT_PAIRE: 1.38,
                },
                'prediction': ALJAZ_BEDENE,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    ALEXEI_POPYRIN,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(2, 6), (7, 5), (6, 3), (6, 2)],
                'odds': {
                    ALEXEI_POPYRIN: 2.05,
                    MIKHAIL_KUKUSHKIN: 1.75,
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    JOHN_ISNER,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(6, 3), (7, 6), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.70,
                    JAN_LENNARD_STRUFF: 2.00,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    PABLO_ANDUJAR,
                    LORENZO_SONEGO,
                ],
                'score': [(6, 2), (6, 4), (6, 2)],
                'odds': {
                    PABLO_ANDUJAR: 3.60,
                    LORENZO_SONEGO: 1.28,
                },
                'prediction': LORENZO_SONEGO,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ALEXANDER_BUBLIK,
                    THOMAS_FABBIANO,
                ],
                'score': [(6, 7), (5, 7), (6, 4), (6, 3), (6, 3)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.50,
                    THOMAS_FABBIANO: 1.52,
                },
                'prediction': THOMAS_FABBIANO,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ANDREY_RUBLEV,
                    GILLES_SIMON,
                ],
                'score': [(6, 2)],
                'retired': True,
                'odds': {
                    ANDREY_RUBLEV: 1.28,
                    GILLES_SIMON: 3.80,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 0,  # refunded 3,
            },
            {
                'round': 64,
                'players': [
                    TENNYS_SANDGREN,
                    VASEK_POSPISIL,
                ],
                'score': [(6, 3), (6, 7), (6, 3), (6, 4)],
                'odds': {
                    TENNYS_SANDGREN: 1.52,
                    VASEK_POSPISIL: 2.50,
                },
                'prediction': TENNYS_SANDGREN,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    ANTOINE_HOANG,
                    NICK_KYRGIOS,
                ],
                'score': [(6, 4), (6, 2), (6, 4)],
                'odds': {
                    ANTOINE_HOANG: 7.50,
                    NICK_KYRGIOS: 1.08,
                },
                'prediction': NICK_KYRGIOS,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    HENRI_LAAKSONEN,
                ],
                'score': [(6, 4), (7, 6), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.07,
                    HENRI_LAAKSONEN: 8.00,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    EGOR_GERASIMOV,
                ],
                'score': [(6, 4), (6, 2), (6, 0)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.12,
                    EGOR_GERASIMOV: 5.50,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    GAEL_MONFILS,
                    MARIUS_COPIL,
                ],
                'score': [(6, 3), (6, 2), (6, 2)],
                'odds': {
                    GAEL_MONFILS: 1.14,
                    MARIUS_COPIL: 5.50,
                },
                'prediction': GAEL_MONFILS,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    HYEON_CHUNG,
                    FERNANDO_VERDASCO,
                ],
                'score': [(1, 6), (2, 6), (7, 5), (6, 3), (7, 6)],
                'odds': {
                    HYEON_CHUNG: 1.75,
                    FERNANDO_VERDASCO: 2.05,
                },
                'prediction': FERNANDO_VERDASCO,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    RAFAEL_NADAL,
                    THANASI_KOKKINAKIS,
                ],
                'score': [],
                'retired': True,
                'odds': {
                    RAFAEL_NADAL: 1.04,
                    THANASI_KOKKINAKIS: 10.00,
                },
                'prediction': THANASI_KOKKINAKIS,
                'bet': 0,  # refunded 10,
            },
            {
                'round': 64,
                'players': [
                    MARIN_CILIC,
                    CEDRIC_MARCEL_STEBE,
                ],
                'score': [(4, 6), (6, 3), (7, 5), (6, 3)],
                'odds': {
                    MARIN_CILIC: 1.08,
                    CEDRIC_MARCEL_STEBE: 7.50,
                },
                'prediction': MARIN_CILIC,
                'bet': 2,
            },

            # 2019-08-30
            {
                'round': 32,
                'players': [
                    ALEX_DE_MINAUR,
                    KEI_NISHIKORI,
                ],
                'score': [(6, 2), (6, 4), (2, 6), (6, 3)],
                'odds': {
                    ALEX_DE_MINAUR: 2.40,
                    KEI_NISHIKORI: 1.55,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 9,
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    DANIEL_EVANS,
                ],
                'score': [(6, 2), (6, 2), (6, 1)],
                'odds': {
                    ROGER_FEDERER: 1.14,
                    DANIEL_EVANS: 5.50,
                },
                'prediction': ROGER_FEDERER,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(7, 6), (7, 6), (7, 5)],
                'odds': {
                    DAVID_GOFFIN: 1.40,
                    PABLO_CARRENO_BUSTA: 2.90,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    GRIGOR_DIMITROV,
                    KAMIL_MAJCHRZAK,
                ],
                'score': [(7, 5), (7, 6), (6, 2)],
                'odds': {
                    GRIGOR_DIMITROV: 1.24,
                    KAMIL_MAJCHRZAK: 4.00,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    PAOLO_LORENZI,
                ],
                'score': [(6, 4), (7, 6), (7, 6)],
                'odds': {
                    STAN_WAWRINKA: 1.03,
                    PAOLO_LORENZI: 11.00,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    DOMINIK_KOEPFER,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(6, 3), (7, 6), (4, 6), (6, 1)],
                'odds': {
                    DOMINIK_KOEPFER: 2.20,
                    NIKOLOZ_BASILASHVILI: 1.65,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    DENIS_KUDLA,
                ],
                'score': [(6, 3), (6, 4), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.05,
                    DENIS_KUDLA: 9.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    DANIIL_MEDVEDEV,
                    FELICIANO_LOPEZ,
                ],
                'score': [(7, 6), (4, 6), (7, 6), (6, 4)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.38,
                    FELICIANO_LOPEZ: 3.00,
                },
                'prediction': FELICIANO_LOPEZ,
                'bet': 9,
            },

            # 2019-08-31
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    HYEON_CHUNG,
                ],
                'score': [(6, 3), (6, 4), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    HYEON_CHUNG: 14.00,
                },
            },
            {
                'round': 32,
                'players': [
                    PABLO_ANDUJAR,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(6, 4), (6, 3), (6, 2)],
                'odds': {
                    PABLO_ANDUJAR: 1.62,
                    ALEXANDER_BUBLIK: 2.25,
                },
            },
            {
                'round': 32,
                'players': [
                    MARIN_CILIC,
                    JOHN_ISNER,
                ],
                'score': [(7, 5), (3, 6), (7, 6), (6, 4)],
                'odds': {
                    MARIN_CILIC: 2.00,
                    JOHN_ISNER: 1.80,
                },
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    ALJAZ_BEDENE,
                ],
                'score': [(6, 7), (7, 6), (6, 3), (6, 7)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.22,
                    ALJAZ_BEDENE: 4.20,
                },
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 4), (6, 4), (6, 7), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 1.36,
                    ALEXEI_POPYRIN: 3.10,
                },
            },
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    TENNYS_SANDGREN,
                ],
                'score': [(6, 4), (6, 1), (6, 3)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.30,
                    TENNYS_SANDGREN: 3.40,
                },
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    DENIS_SHAPOVALOV,
                ],
                'score': [(6, 7), (7, 6), (6, 4), (6, 7), (6, 3)],
                'odds': {
                    GAEL_MONFILS: 1.68,
                    DENIS_SHAPOVALOV: 2.15,
                },
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    NICK_KYRGIOS,
                ],
                'score': [(7, 6), (7, 6), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 2.60,
                    NICK_KYRGIOS: 1.48,
                },
            },

            # 2019-09-01
            {
                'round': 16,
                'players': [
                    GRIGOR_DIMITROV,
                    ALEX_DE_MINAUR,
                ],
                'score': [(7, 5), (6, 3), (6, 4)],
                'odds': {
                    GRIGOR_DIMITROV: 2.75,
                    ALEX_DE_MINAUR: 1.42,
                },
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    DAVID_GOFFIN,
                ],
                'score': [(6, 2), (6, 2), (6, 0)],
                'odds': {
                    ROGER_FEDERER: 1.16,
                    DAVID_GOFFIN: 5.00,
                },
            },
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    NOVAK_DJOKOVIC,
                ],
                'score': [(6, 4), (7, 5), (2, 1)],
                'retired': True,
                'odds': {
                    STAN_WAWRINKA: 4.60,
                    NOVAK_DJOKOVIC: 1.18,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 0,  # refunded 1,
            },
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 1), (6, 4), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 2.60,
                    ANDREY_RUBLEV: 1.48,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(3, 6), (6, 2), (6, 4), (6, 3)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.95,
                    ALEXANDER_ZVEREV: 1.85,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    PABLO_ANDUJAR,
                ],
                'score': [(6, 1), (6, 2), (6, 2)],
                'odds': {
                    GAEL_MONFILS: 1.18,
                    PABLO_ANDUJAR: 4.60,
                },
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    MARIN_CILIC,
                ],
                'score': [(6, 3), (3, 6), (6, 1), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.10,
                    MARIN_CILIC: 6.50,
                },
                'prediction': RAFAEL_NADAL,
                'bet': 1,
            },

            # 2019-09-02
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 1), (6, 4), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 2.70,
                    ANDREY_RUBLEV: 1.45,
                },
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(3, 6), (6, 2), (6, 4), (6, 3)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 2.00,
                    ALEXANDER_ZVEREV: 1.80,
                },
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    PABLO_ANDUJAR,
                ],
                'score': [(6, 1), (6, 2), (6, 2)],
                'odds': {
                    GAEL_MONFILS: 1.16,
                    PABLO_ANDUJAR: 5.00,
                },
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    MARIN_CILIC,
                ],
                'score': [(6, 3), (3, 6), (6, 1), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.10,
                    MARIN_CILIC: 6.50,
                },
                'prediction': RAFAEL_NADAL,
                'bet': 1,
            },

            # 2019-09-03
            {
                'round': 8,
                'players': [
                    DANIIL_MEDVEDEV,
                    STAN_WAWRINKA,
                ],
                'score': [(7, 6), (6, 3), (3, 6), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 2.05,
                    STAN_WAWRINKA: 1.75,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    GRIGOR_DIMITROV,
                    ROGER_FEDERER,
                ],
                'score': [(3, 6), (6, 4), (3, 6), (6, 4), (6, 2)],
                'odds': {
                    GRIGOR_DIMITROV: 8.00,
                    ROGER_FEDERER: 1.07,
                },
                'prediction': ROGER_FEDERER,
                'bet': 9,
            },

            # 2019-09-04
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    GAEL_MONFILS,
                ],
                'score': [(3, 6), (6, 3), (6, 2), (3, 6), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 2.60,
                    GAEL_MONFILS: 1.48,
                },
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    DIEGO_SCHWARTZMAN,
                ],
                'score': [(6, 4), (7, 5), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.04,
                    DIEGO_SCHWARTZMAN: 10.00,
                },
            },

            # 2019-09-06
            {
                'round': 4,
                'players': [
                    RAFAEL_NADAL,
                    MATTEO_BERRETTINI,
                ],
                'score': [(7, 6), (6, 4), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.06,
                    MATTEO_BERRETTINI: 9.00,
                },
                'prediction': RAFAEL_NADAL,
                'bet': 2,
            },
            {
                'round': 4,
                'players': [
                    DANIIL_MEDVEDEV,
                    GRIGOR_DIMITROV,
                ],
                'score': [(7, 6), (6, 4), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.52,
                    GRIGOR_DIMITROV: 2.50,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 4,
            },

            # 2019-09-08
            {
                'round': 2,
                'players': [
                    RAFAEL_NADAL,
                    DANIIL_MEDVEDEV
                ],
                'score': [(7, 5), (6, 3), (5, 7), (4, 6), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.18,
                    DANIIL_MEDVEDEV: 4.74
                }
            }
        ]
    },

    ###############################################################################
    # Active
    ###############################################################################

    {
        'location': METZ,
        'date': '2019-09-22',
        'matches': [

            # 2019-09-15
            {
                'round': 512,
                'players': [
                    ADRIAN_MENENDEZ_MACEIRAS,
                    HARDOLD_MAYOT
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    ADRIAN_MENENDEZ_MACEIRAS: 1.14,
                    HARDOLD_MAYOT: 4.70
                }
            },
            {
                'round': 512,
                'players': [
                    JULIAN_LENZ,
                    CONSTANT_LESTIENNE
                ],
                'score': [(4, 6), (6, 3), (7, 5)],
                'odds': {
                    JULIAN_LENZ: 3.10,
                    CONSTANT_LESTIENNE: 1.30
                }
            },
            {
                'round': 512,
                'players': [
                    MAXIME_JANVIER,
                    MISCHA_ZVEREV
                ],
                'score': [(7, 6), (2, 0)],
                'retired': True,
                'odds': {
                    MAXIME_JANVIER: 1.51,
                    MISCHA_ZVEREV: 2.35
                }
            },
            {
                'round': 512,
                'players': [
                    NICOLAS_MAHUT,
                    TRISTAN_LAMASINE
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    NICOLAS_MAHUT: 1.38,
                    TRISTAN_LAMASINE: 2.75
                }
            },
            {
                'round': 512,
                'players': [
                    YANNICK_MADEN,
                    MANUEL_GUINARD
                ],
                'score': [(6, 0), (6, 4)],
                'odds': {
                    YANNICK_MADEN: 1.40,
                    MANUEL_GUINARD: 2.70
                }
            },
            {
                'round': 512,
                'players': [
                    MATTHIAS_BACHINGER,
                    LUCAS_MIEDLER
                ],
                'score': [(4, 6), (6, 4), (6, 3)],
                'odds': {
                    MATTHIAS_BACHINGER: 1.50,
                    LUCAS_MIEDLER: 2.30
                }
            },
            {
                'round': 512,
                'players': [
                    MARCEL_GRANOLLERS,
                    ALBANO_OLIVETTI
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.19,
                    ALBANO_OLIVETTI: 3.75
                }
            },
            {
                'round': 512,
                'players': [
                    OSCAR_OTTE,
                    ARTEM_DUBRIVNYY
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    OSCAR_OTTE: 1.26,
                    ARTEM_DUBRIVNYY: 2.90
                }
            },

            # 2019-09-16
            {
                'round': 256,
                'players': [
                    JULIAN_LENZ,
                    MATTHIAS_BACHINGER,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JULIAN_LENZ: 3.10,
                    MATTHIAS_BACHINGER: 1.36,
                },
            },
            {
                'round': 256,
                'players': [
                    MARCEL_GRANOLLERS,
                    ADRIAN_MENENDEZ_MACEIRAS
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.28,
                    ADRIAN_MENENDEZ_MACEIRAS: 3.60
                },
            },
            {
                'round': 256,
                'players': [
                    YANNICK_MADEN,
                    NICOLAS_MAHUT
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    YANNICK_MADEN: 2.00,
                    NICOLAS_MAHUT: 1.80
                },
            },
            {
                'round': 256,
                'players': [
                    OSCAR_OTTE,
                    MAXIME_JANVIER
                ],
                'score': [(2, 6), (6, 3), (6, 2)],
                'odds': {
                    OSCAR_OTTE: 1.90,
                    MAXIME_JANVIER: 1.90
                },
            },
            {
                'round': 32,
                'players': [
                    ANTOINE_HOANG,
                    CEDRIC_MARCEL_STEBE
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ANTOINE_HOANG: 1.68,
                    CEDRIC_MARCEL_STEBE: 2.15,
                },
                'prediction': ANTOINE_HOANG,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    STEVE_DARCIS,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    FERNANDO_VERDASCO: 1.24,
                    STEVE_DARCIS: 3.75
                }
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    PETER_GOJOWCZYK
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.69,
                    PETER_GOJOWCZYK: 2.10
                }
            },

            # 2019-09-17
            {
                'round': 32,
                'players': [
                    GREGOIRE_BARRERE,
                    HUBERT_HURKACZ,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    GREGOIRE_BARRERE: 2.80,
                    HUBERT_HURKACZ: 1.42,
                },
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 2.60,
                    JAN_LENNARD_STRUFF: 1.48,
                },
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    MARCEL_GRANOLLERS,
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    RICHARD_GASQUET: 1.36,
                    MARCEL_GRANOLLERS: 3.10,
                },
            },
            {
                'round': 32,
                'players': [
                    JO_WILFRIED_TSONGA,
                    PABLO_ANDUJAR,
                ],
                'score': [(3, 6), (6, 1), (6, 2)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.18,
                    PABLO_ANDUJAR: 4.60,
                },
            },
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    OSCAR_OTTE,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    LORENZO_SONEGO: 1.34,
                    OSCAR_OTTE: 3.20,
                },
                'prediction': LORENZO_SONEGO,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    RAYANE_ROUMANE
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALJAZ_BEDENE: 1.38,
                    RAYANE_ROUMANE: 3.00,
                },
            },
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JULIAN_LENZ,
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.24,
                    JULIAN_LENZ: 4.00,
                },
            },

            # 2019-09-18
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    MARIUS_COPIL,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    GILLES_SIMON: 1.42,
                    MARIUS_COPIL: 2.80,
                },
                'prediction': GILLES_SIMON,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    YANNICK_MADEN,
                    UGO_HUMBERT,
                ],
                'score': [(6, 4), (6, 7), (6, 4)],
                'odds': {
                    YANNICK_MADEN: 3.80,
                    UGO_HUMBERT: 1.26,
                },
            },
            {
                'round': 16,
                'players': [
                    GREGOIRE_BARRERE,
                    ANTOINE_HOANG,
                ],
                'score': [(3, 6), (7, 6), (6, 2)],
                'odds': {
                    GREGOIRE_BARRERE: 1.55,
                    ANTOINE_HOANG: 2.40,
                },
                'prediction': GREGOIRE_BARRERE,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    BENOIT_PAIRE,
                    RICHARD_GASQUET,
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    BENOIT_PAIRE: 2.30,
                    RICHARD_GASQUET: 1.60,
                },
                'prediction': RICHARD_GASQUET,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    FILIP_KRAJINOVIC,
                    FERNANDO_VERDASCO,
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.80,
                    FERNANDO_VERDASCO: 2.00,
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 1,
            },

            # 2019-09-19
            {
                'round': 16,
                'players': [
                    ALJAZ_BEDENE,
                    GILLES_SIMON,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    ALJAZ_BEDENE: 2.40,
                    GILLES_SIMON: 1.52,
                },
            },
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    DAVID_GOFFIN,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 2.60,
                    DAVID_GOFFIN: 1.48,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    LUCAS_POUILLE,
                    LORENZO_SONEGO,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    LUCAS_POUILLE: 1.68,
                    LORENZO_SONEGO: 2.15,
                },
            },
            {
                'round': 16,
                'players': [
                    JO_WILFRIED_TSONGA,
                    PIERRE_HUGUES_HERBERT,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.36,
                    PIERRE_HUGUES_HERBERT: 3.10,
                },
            },
            {
                'round': 16,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    YANNICK_MADEN,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.48,
                    YANNICK_MADEN: 2.60,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 3,
            },

            #
        ]
    },

    {
        'location': ST_PETERSBURG,
        'date': '2019-09-22',
        'matches': [

            # 2019-09-15
            {
                'round': 512,
                'players': [
                    ROMAN_SAFIULLIN,
                    KEVIN_KRAWIETZ
                ],
                'score': [(6, 4), (6, 1)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    MATTEO_VIOLA,
                    ALEXANDER_VASILENKO
                ],
                'score': [(6, 2), (5, 7), (6, 2)],
                'odds': {
                    MATTEO_VIOLA: 1.22,
                    ALEXANDER_VASILENKO: 3.40
                }
            },
            {
                'round': 512,
                'players': [
                    LUKAS_ROSOL,
                    EVGENY_KARLOVSKIY
                ],
                'score': [(6, 4), (3, 6), (6, 4)],
                'odds': {
                    LUKAS_ROSOL: 1.53,
                    EVGENY_KARLOVSKIY: 2.10
                }
            },
            {
                'round': 512,
                'players': [
                    ILYA_IVASHKA,
                    EVGENII_TIURNEV
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    ILYA_IVASHKA: 1.29,
                    EVGENII_TIURNEV: 3.30
                }
            },
            {
                'round': 512,
                'players': [
                    ERNESTS_GULBIS,
                    AMIR_WEINTRAUB
                ],
                'score': [(6, 1), (6, 0)],
                'odds': {
                    ERNESTS_GULBIS: 1.04,
                    AMIR_WEINTRAUB: 7.00
                }
            },
            {
                'round': 512,
                'players': [
                    EGOR_GERASIMOV,
                    ALEJANDRO_TABILO
                ],
                'score': [(6, 0), (6, 4)],
                'odds': {
                    EGOR_GERASIMOV: 1.12,
                    ALEJANDRO_TABILO: 3.55
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    ASLAN_KARATSEV
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DAMIR_DZUMHUR: 1.28,
                    ASLAN_KARATSEV: 3.30
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEY_VATUTIN,
                    ALEKSANDR_NEDOVYESOV
                ],
                'score': [(1, 6), (6, 3), (7, 5)],
                'odds': {
                    ALEXEY_VATUTIN: 1.59,
                    ALEKSANDR_NEDOVYESOV: 2.20
                }
            },

            # 2019-09-16
            {
                'round': 256,
                'players': [
                    LUKAS_ROSOL,
                    DAMIR_DZUMHUR,
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    LUKAS_ROSOL: 3.20,
                    DAMIR_DZUMHUR: 1.34,
                },
                'prediction': DAMIR_DZUMHUR,
                'bet': 3,
            },
            {
                'round': 256,
                'players': [
                    EGOR_GERASIMOV,
                    ROMAN_SAFIULLIN
                ],
                'score': [(7, 5), (6, 7), (6, 4)],
                'odds': {
                    EGOR_GERASIMOV: 1.32,
                    ROMAN_SAFIULLIN: 3.30
                },
            },
            {
                'round': 256,
                'players': [
                    ILYA_IVASHKA,
                    MATTEO_VIOLA
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ILYA_IVASHKA: 1.24,
                    MATTEO_VIOLA: 4.00
                },
                'prediction': ILYA_IVASHKA,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    ALEXEY_VATUTIN,
                    ERNESTS_GULBIS,
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    ALEXEY_VATUTIN: 1.85,
                    ERNESTS_GULBIS: 1.95,
                },
            },
            {
                'round': 32,
                'players': [
                    ADRIAN_MANNARINO,
                    STEFANO_TRAVAGLIA,
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    ADRIAN_MANNARINO: 1.55,
                    STEFANO_TRAVAGLIA: 2.40,
                },
            },
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    JANNIK_SINNER
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.63,
                    JANNIK_SINNER: 2.40
                }
            },

            # 2019-09-17
            {
                'round': 32,
                'players': [
                    DAMIR_DZUMHUR,
                    JANKO_TIPSAREVIC,
                ],
                'score': [(7, 5), (3, 6), (3, 1)],
                'retired': None,
                'odds': {
                    DAMIR_DZUMHUR: 1.36,
                    JANKO_TIPSAREVIC: 3.10,
                },
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    MARTIN_KLIZAN,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 2.05,
                    MARTIN_KLIZAN: 1.75,
                },
            },
            {
                'round': 32,
                'players': [
                    EGOR_GERASIMOV,
                    LUKAS_ROSOL,
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    EGOR_GERASIMOV: 1.58,
                    LUKAS_ROSOL: 2.35,
                },
            },
            {
                'round': 32,
                'players': [
                    EVGENY_DONSKOY,
                    MATTEO_VIOLA,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    EVGENY_DONSKOY: 1.30,
                    MATTEO_VIOLA: 3.40,
                },
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    ILYA_IVASHKA,
                ],
                'score': [(4, 6), (6, 0), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 1.32,
                    ILYA_IVASHKA: 3.30,
                },
            },
            {
                'round': 32,
                'players': [
                    RICARDAS_BERANKIS,
                    DUDI_SELA,
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    RICARDAS_BERANKIS: 1.30,
                    DUDI_SELA: 3.40,
                },
            },

            # 2019-09-18
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    JOZEF_KOVALIK,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    JOAO_SOUSA: 1.28,
                    JOZEF_KOVALIK: 3.60,
                },
                'prediction': JOAO_SOUSA,
                'bet': 12,
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    ALEXEY_VATUTIN,
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    MARTON_FUCSOVICS: 1.38,
                    ALEXEY_VATUTIN: 3.00,
                },
                'prediction': MARTON_FUCSOVICS,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    SALVATORE_CARUSO,
                    THOMAS_FABBIANO,
                ],
                'score': [(2, 6), (6, 3), (6, 3)],
                'odds': {
                    SALVATORE_CARUSO: 2.35,
                    THOMAS_FABBIANO: 1.58,
                },
                'prediction': THOMAS_FABBIANO,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    DAMIR_DZUMHUR,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.60,
                    DAMIR_DZUMHUR: 2.30,
                },
                'prediction': MIKHAIL_KUKUSHKIN,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    CASPER_RUUD: 2.20,
                    ALEXANDER_BUBLIK: 1.65,
                },
                'prediction': ALEXANDER_BUBLIK,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    EGOR_GERASIMOV,
                    ADRIAN_MANNARINO,
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    EGOR_GERASIMOV: 2.15,
                    ADRIAN_MANNARINO: 1.68,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 1,
            },

            # 2019-09-19
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    MARTON_FUCSOVICS,
                ],
                'score': [(6, 7), (7, 5), (3, 0)],
                'retired': True,
                'odds': {
                    BORNA_CORIC: 1.62,
                    MARTON_FUCSOVICS: 2.25,
                },
            },
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 1.24,
                    ROBERTO_CARBALLES_BAENA: 4.00,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    CASPER_RUUD,
                    SALVATORE_CARUSO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    CASPER_RUUD: 1.42,
                    SALVATORE_CARUSO: 2.80,
                },
                'prediction': CASPER_RUUD,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    JOAO_SOUSA,
                    KAREN_KHACHANOV,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 3.30,
                    KAREN_KHACHANOV: 1.30,
                },
            },
            {
                'round': 16,
                'players': [
                    DANIIL_MEDVEDEV,
                    EVGENY_DONSKOY,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.09,
                    EVGENY_DONSKOY: 7.00,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 7,
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 4), (6, 7), (6, 1)],
                'odds': {
                    ANDREY_RUBLEV: 1.34,
                    RICARDAS_BERANKIS: 3.20,
                },
            },

            #
        ]
    }
]
