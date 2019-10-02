from men import *
from location import *


DATA_2018_07 = [
    {
        'location': UMAG,
        'date': '2018-07-22',
        'matches': [

            # 2018-07-15
            {
                'round': 512,
                'players': [
                    KENNY_DE_SCHEPPER,
                    ZSOMBOR_PIROS
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    KENNY_DE_SCHEPPER: 1.74,
                    ZSOMBOR_PIROS: 1.90
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREJ_MARTIN,
                    ROBERTO_QUIROZ
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    ANDREJ_MARTIN: 1.40,
                    ROBERTO_QUIROZ: 2.55
                }
            },
            {
                'round': 512,
                'players': [
                    PEDJA_KRSTIN,
                    ENRIQUE_LOPEZ_PEREZ
                ],
                'score': [(3, 1)],
                'retired': True,
                'odds': {
                    PEDJA_KRSTIN: 1.95,
                    ENRIQUE_LOPEZ_PEREZ: 1.67
                }
            },
            {
                'round': 512,
                'players': [
                    MARCO_TRUNGELLITI,
                    FACUNDO_BAGNIS
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    MARCO_TRUNGELLITI: 1.91,
                    FACUNDO_BAGNIS: 1.70
                }
            },
            {
                'round': 512,
                'players': [
                    STEFANO_TRAVAGLIA,
                    GIAN_MARCO_MORONI
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    STEFANO_TRAVAGLIA: 1.69,
                    GIAN_MARCO_MORONI: 2.00
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEY_VATUTIN,
                    NIK_RAZBORSEK
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ALEXEY_VATUTIN: 1.16,
                    NIK_RAZBORSEK: 4.35
                }
            },
            {
                'round': 512,
                'players': [
                    ROGERIO_DUTRA_SILVA,
                    ADMIR_KALENDER
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ROGERIO_DUTRA_SILVA: 1.01,
                    ADMIR_KALENDER: 9.60
                }
            },
            {
                'round': 512,
                'players': [
                    MARTIN_KLIZAN,
                    DANILO_PETROVIC
                ],
                'score': [(2, 6), (7, 6), (6, 4)],
                'odds': {
                    MARTIN_KLIZAN: 1.20,
                    DANILO_PETROVIC: 4.00
                }
            },

            # 2018-07-16
            {
                'round': 256,
                'players': [
                    STEFANO_TRAVAGLIA,
                    PEDJA_KRSTIN
                ],
                'score': [(1, 6), (6, 3), (6, 2)],
                'odds': {
                    STEFANO_TRAVAGLIA: 1.33,
                    PEDJA_KRSTIN: 3.00
                }
            },
            {
                'round': 256,
                'players': [
                    MARCO_TRUNGELLITI,
                    ALEXEY_VATUTIN
                ],
                'score': [(3, 2)],
                'retired': True,
                'odds': {
                    MARCO_TRUNGELLITI: 1.63,
                    ALEXEY_VATUTIN: 2.10
                }
            },
            {
                'round': 256,
                'players': [
                    ROGERIO_DUTRA_SILVA,
                    ANDREJ_MARTIN
                ],
                'score': [(6, 2), (5, 7), (6, 2)],
                'odds': {
                    ROGERIO_DUTRA_SILVA: 1.74,
                    ANDREJ_MARTIN: 2.00
                }
            },
            {
                'round': 256,
                'players': [
                    MARTIN_KLIZAN,
                    KENNY_DE_SCHEPPER
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MARTIN_KLIZAN: 1.26,
                    KENNY_DE_SCHEPPER: 2.90
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    TARO_DANIEL
                ],
                'score': [(1, 6), (6, 3), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 1.45,
                    TARO_DANIEL: 2.70
                }
            },
            {
                'round': 32,
                'players': [
                    LASLO_DJERE,
                    PABLO_CUEVAS
                ],
                'score': [(6, 4), (1, 6), (6, 3)],
                'odds': {
                    LASLO_DJERE: 2.40,
                    PABLO_CUEVAS: 1.53
                }
            },

            # 2018-07-17
            {
                'round': 32,
                'players': [
                    JIRI_VESELY,
                    STEFANO_TRAVAGLIA
                ],
                'score': [(6, 3), (3, 6), (6, 2)],
                'odds': {
                    JIRI_VESELY: 1.50,
                    STEFANO_TRAVAGLIA: 2.55
                }
            },
            {
                'round': 32,
                'players': [
                    MARCO_TRUNGELLITI,
                    FRANKO_SKUGOR
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MARCO_TRUNGELLITI: 1.40,
                    FRANKO_SKUGOR: 2.90
                }
            },
            {
                'round': 32,
                'players': [
                    DUSAN_LAJOVIC,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    DUSAN_LAJOVIC: 1.32,
                    NIKOLOZ_BASILASHVILI: 3.10
                }
            },
            {
                'round': 32,
                'players': [
                    MARTIN_KLIZAN,
                    NICOLAS_JARRY
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    MARTIN_KLIZAN: 1.85,
                    NICOLAS_JARRY: 1.87
                }
            },
            {
                'round': 32,
                'players': [
                    EVGENY_DONSKOY,
                    PAOLO_LORENZI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    EVGENY_DONSKOY: 2.30,
                    PAOLO_LORENZI: 1.60
                }
            },
            {
                'round': 32,
                'players': [
                    MAXIMILIAN_MARTERER,
                    NINO_SERDARUSIC
                ],
                'score': [(3, 6), (7, 5), (6, 3)],
                'odds': {
                    MAXIMILIAN_MARTERER: 1.25,
                    NINO_SERDARUSIC: 3.75
                }
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    BENOIT_PAIRE
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    MARTON_FUCSOVICS: 1.90,
                    BENOIT_PAIRE: 1.80
                }
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    JOAO_SOUSA
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    ALJAZ_BEDENE: 1.74,
                    JOAO_SOUSA: 2.05
                }
            },
            {
                'round': 32,
                'players': [
                    ROBIN_HAASE,
                    ROGERIO_DUTRA_SILVA
                ],
                'score': [(4, 6), (7, 5), (6, 3)],
                'odds': {
                    ROBIN_HAASE: 1.74,
                    ROGERIO_DUTRA_SILVA: 2.00
                }
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    ANDREJ_MARTIN
                ],
                'score': [(6, 4), (6, 3)]
                # no odds
            },

            # 2018-07-18
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    ALJAZ_BEDENE
                ],
                'score': [(5, 7), (6, 4), (6, 4)],
                'odds': {
                    GUIDO_PELLA: 1.65,
                    ALJAZ_BEDENE: 2.20
                }
            },
            {
                'round': 16,
                'players': [
                    LASLO_DJERE,
                    MAXIMILIAN_MARTERER
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    LASLO_DJERE: 2.05,
                    MAXIMILIAN_MARTERER: 1.69
                }
            },
            {
                'round': 16,
                'players': [
                    DUSAN_LAJOVIC,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 3), (1, 6), (6, 0)],
                'odds': {
                    DUSAN_LAJOVIC: 1.50,
                    ALBERT_RAMOS_VINOLAS: 2.40
                }
            },
            {
                'round': 16,
                'players': [
                    MARCO_CECCHINATO,
                    JIRI_VESELY
                ],
                'score': [(2, 6), (7, 5), (7, 5)],
                'odds': {
                    MARCO_CECCHINATO: 1.74,
                    JIRI_VESELY: 2.05
                }
            },

            # 2018-07-19
            {
                'round': 16,
                'players': [
                    MARCO_TRUNGELLITI,
                    MARTON_FUCSOVICS
                ],
                'score': [(5, 7), (6, 4), (6, 2)],
                'odds': {
                    MARCO_TRUNGELLITI: 2.95,
                    MARTON_FUCSOVICS: 1.36
                }
            },
            {
                'round': 16,
                'players': [
                    ROBIN_HAASE,
                    MARTIN_KLIZAN
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    ROBIN_HAASE: 2.10,
                    MARTIN_KLIZAN: 1.67
                }
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 1.77,
                    FELIX_AUGER_ALIASSIME: 1.83
                }
            },
            {
                'round': 16,
                'players': [
                    EVGENY_DONSKOY,
                    DAMIR_DZUMHUR
                ],
                'score': [(7, 6), (3, 6), (6, 4)],
                'odds': {
                    EVGENY_DONSKOY: 3.40,
                    DAMIR_DZUMHUR: 1.25
                }
            },

            # 2018-07-20
            {
                'round': 8,
                'players': [
                    MARCO_TRUNGELLITI,
                    EVGENY_DONSKOY
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    MARCO_TRUNGELLITI: 1.60,
                    EVGENY_DONSKOY: 2.30
                }
            },
            {
                'round': 8,
                'players': [
                    GUIDO_PELLA,
                    DUSAN_LAJOVIC
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    GUIDO_PELLA: 1.90,
                    DUSAN_LAJOVIC: 1.71
                }
            },
            {
                'round': 8,
                'players': [
                    ROBIN_HAASE,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    ROBIN_HAASE: 1.80,
                    ANDREY_RUBLEV: 1.93
                }
            },
            {
                'round': 8,
                'players': [
                    MARCO_CECCHINATO,
                    LASLO_DJERE
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    MARCO_CECCHINATO: 1.59,
                    LASLO_DJERE: 2.30
                }
            },

            # 2018-07-21
            {
                'round': 4,
                'players': [
                    GUIDO_PELLA,
                    ROBIN_HAASE,
                ],
                'score': [(6, 3), (1, 6), (6, 2)],
                'odds': {
                    GUIDO_PELLA: 1.67,
                    ROBIN_HAASE: 2.10
                }
            },
            {
                'round': 4,
                'players': [
                    MARCO_CECCHINATO,
                    MARCO_TRUNGELLITI
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    MARCO_CECCHINATO: 1.36,
                    MARCO_TRUNGELLITI: 3.10
                }
            },

            # 2018-07-22
            {
                'round': 2,
                'players': [
                    MARCO_CECCHINATO,
                    GUIDO_PELLA
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    MARCO_CECCHINATO: 1.74,
                    GUIDO_PELLA: 2.05
                }
            }
        ]
    },

    {
        'location': HAMBURG,
        'date': '2018-07-29',
        'matches': [

            # 2018-07-21
            {
                'round': 512,
                'players': [
                    DANIEL_MASUR,
                    CARLOS_BERLOCQ
                ],
                'score': [(7, 6), (4, 6), (6, 3)],
                'odds': {
                    DANIEL_MASUR: 2.55,
                    CARLOS_BERLOCQ: 1.36
                }
            },
            {
                'round': 512,
                'players': [
                    DANILO_PETROVIC,
                    CALVIN_HEMERY
                ],
                'score': [(5, 7), (7, 6), (7, 5)],
                'odds': {
                    DANILO_PETROVIC: 1.95,
                    CALVIN_HEMERY: 1.60
                }
            },
            {
                'round': 512,
                'players': [
                    THIAGO_MONTEIRO,
                    ROBERTO_QUIROZ
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    THIAGO_MONTEIRO: 1.24,
                    ROBERTO_QUIROZ: 3.20
                }
            },
            {
                'round': 512,
                'players': [
                    JURGEN_MELZER,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JURGEN_MELZER: 2.55,
                    MARTIN_KLIZAN: 1.40
                }
            },
            {
                'round': 512,
                'players': [
                    RENZO_OLIVO,
                    LORENZO_SONEGO
                ],
                'score': [(3, 6), (6, 1), (7, 6)],
                'odds': {
                    RENZO_OLIVO: 2.75,
                    LORENZO_SONEGO: 1.35
                }
            },
            {
                'round': 512,
                'players': [
                    CORENTIN_MOUTET,
                    MARVIN_MOELLER
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    CORENTIN_MOUTET: 1.20,
                    MARVIN_MOELLER: 3.75
                }
            },
            {
                'round': 512,
                'players': [
                    JOZEF_KOVALIK,
                    NIKLAS_GUTTAU
                ],
                'score': [(6, 0), (6, 1)],
                'odds': {
                    JOZEF_KOVALIK: 1.01,
                    NIKLAS_GUTTAU: 9.70
                }
            },
            {
                'round': 512,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    TOBIAS_KAMKE
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.40,
                    TOBIAS_KAMKE: 2.40
                }
            },

            # 2018-07-22
            {
                'round': 256,
                'players': [
                    DANIEL_MASUR,
                    RENZO_OLIVO
                ],
                'score': [(4, 6), (7, 5), (7, 5)],
                'odds': {
                    DANIEL_MASUR: 1.55,
                    RENZO_OLIVO: 2.15
                }
            },
            {
                'round': 256,
                'players': [
                    CORENTIN_MOUTET,
                    DANILO_PETROVIC
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    CORENTIN_MOUTET: 1.36,
                    DANILO_PETROVIC: 2.90
                }
            },
            {
                'round': 256,
                'players': [
                    JOZEF_KOVALIK,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 3), (3, 6), (6, 0)],
                'odds': {
                    JOZEF_KOVALIK: 1.50,
                    THIAGO_MONTEIRO: 2.40
                }
            },
            {
                'round': 256,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JURGEN_MELZER
                ],
                'score': [(6, 4), (4, 6), (7, 5)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.77,
                    JURGEN_MELZER: 1.80
                }
            },

            # 2018-07-23
            {
                'round': 32,
                'players': [
                    RUDOLF_MOLLEKER,
                    DAVID_FERRER
                ],
                'score': [(7, 5), (5, 7), (6, 3)],
                'odds': {
                    RUDOLF_MOLLEKER: 2.90,
                    DAVID_FERRER: 1.34
                }
            },
            {
                'round': 32,
                'players': [
                    LEONARDO_MAYER,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    LEONARDO_MAYER: 1.61,
                    ALBERT_RAMOS_VINOLAS: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    DANIEL_MASUR,
                    MAXIMILIAN_MARTERER
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DANIEL_MASUR: 3.10,
                    MAXIMILIAN_MARTERER: 1.27
                }
            },
            {
                'round': 32,
                'players': [
                    JOZEF_KOVALIK,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    JOZEF_KOVALIK: 2.20,
                    DAMIR_DZUMHUR: 1.65
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    FLORIAN_MAYER
                ],
                'score': [(2, 6), (6, 1), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.15,
                    FLORIAN_MAYER: 5.40,
                }
            },
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    CASPER_RUUD
                ],
                'score': [(6, 4), (2, 6), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.25,
                    CASPER_RUUD: 3.60
                }
            },

            # 2018-07-24
            {
                'round': 32,
                'players': [
                    THIAGO_MONTEIRO,
                    GILLES_SIMON
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    THIAGO_MONTEIRO: 2.40,
                    GILLES_SIMON: 1.55
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    JOHN_MILLMAN: 2.00,
                    JAN_LENNARD_STRUFF: 1.80
                }
            },
            {
                'round': 32,
                'players': [
                    NICOLAS_JARRY,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    NICOLAS_JARRY: 2.00,
                    PETER_GOJOWCZYK: 1.80,
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_CUEVAS,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 1.74,
                    MARTON_FUCSOVICS: 2.05
                }
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    HENRI_LAAKSONEN
                ],
                'score': [(6, 3), (1, 6), (6, 4)],
                'odds': {
                    ALJAZ_BEDENE: 1.32,
                    HENRI_LAAKSONEN: 3.40
                }
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 3), (4, 6), (7, 6)],
                'odds': {
                    FERNANDO_VERDASCO: 1.85,
                    DUSAN_LAJOVIC: 1.83
                }
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    BENOIT_PAIRE
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    RICHARD_GASQUET: 1.69,
                    BENOIT_PAIRE: 2.10,
                }
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 4), (3, 6), (6, 4)],
                'odds': {
                    GAEL_MONFILS: 1.77,
                    MARCO_CECCHINATO: 2.00
                }
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(7, 5), (1, 6), (6, 4)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 3.80,
                    PHILIPP_KOHLSCHREIBER: 3.75
                }
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    CORENTIN_MOUTET
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.11,
                    CORENTIN_MOUTET: 5.50
                }
            },

            # 2018-07-25
            {
                'round': 16,
                'players': [
                    LEONARDO_MAYER,
                    GAEL_MONFILS
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    LEONARDO_MAYER: 2.30,
                    GAEL_MONFILS: 1.61,
                }
            },
            {
                'round': 16,
                'players': [
                    JOZEF_KOVALIK,
                    RUDOLF_MOLLEKER
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    JOZEF_KOVALIK: 1.35,
                    RUDOLF_MOLLEKER: 3.10
                }
            },
            {
                'round': 16,
                'players': [
                    THIAGO_MONTEIRO,
                    FERNANDO_VERDASCO
                ],
                'score': [(3, 6), (6, 2), (7, 5)],
                'odds': {
                    THIAGO_MONTEIRO: 3.10,
                    FERNANDO_VERDASCO: 1.31
                }
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    DANIEL_MASUR
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.15,
                    DANIEL_MASUR: 5.00
                }
            },

            # 2018-07-26
            {
                'round': 16,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    PABLO_CUEVAS
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 3.10,
                    PABLO_CUEVAS: 1.36
                }
            },
            {
                'round': 16,
                'players': [
                    NICOLAS_JARRY,
                    RICHARD_GASQUET
                ],
                'score': [],
                'retired': True,
                'odds': {
                    NICOLAS_JARRY: 2.70,
                    RICHARD_GASQUET: 1.45
                }
            },
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    ALJAZ_BEDENE
                ],
                'score': [(6, 2), (4, 0)],
                'retired': True,
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.65,
                    ALJAZ_BEDENE: 2.20
                }
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    JOHN_MILLMAN
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.16,
                    JOHN_MILLMAN: 5.25
                }
            },

            # 2018-07-27
            {
                'round': 8,
                'players': [
                    JOZEF_KOVALIK,
                    THIAGO_MONTEIRO
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    JOZEF_KOVALIK: 1.50,
                    THIAGO_MONTEIRO: 2.55
                }
            },
            {
                'round': 8,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 3.15,
                    PABLO_CARRENO_BUSTA: 1.36
                }
            },
            {
                'round': 8,
                'players': [
                    LEONARDO_MAYER,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 3), (4, 6), (6, 3)],
                'odds': {
                    LEONARDO_MAYER: 2.20,
                    DIEGO_SCHWARTZMAN: 1.65
                }
            },
            {
                'round': 8,
                'players': [
                    NICOLAS_JARRY,
                    DOMINIC_THIEM
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    NICOLAS_JARRY: 6.00,
                    DOMINIC_THIEM: 1.12
                }
            },

            # 2018-07-28
            {
                'round': 4,
                'players': [
                    LEONARDO_MAYER,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 7), (6, 4), (7, 6)],
                'odds': {
                    LEONARDO_MAYER: 1.54,
                    JOZEF_KOVALIK: 2.65
                }
            },
            {
                'round': 4,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    NICOLAS_JARRY
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.20,
                    NICOLAS_JARRY: 1.67
                }
            },

            # 2018-07-29
            {
                'round': 2,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    LEONARDO_MAYER
                ],
                'score': [(6, 4), (0, 6), (7, 5)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.55,
                    LEONARDO_MAYER: 1.50
                }
            }
        ]
    },

    {
        'location': ATLANTA,
        'date': '2018-07-29',
        'matches': [

            # 2018-07-21
            {
                'round': 512,
                'players': [
                    ALEX_BOLT,
                    GARRETT_JOHNS,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    ALEX_BOLT: 1.02,
                    GARRETT_JOHNS: 15.50
                }
            },
            {
                'round': 512,
                'players': [
                    THANASI_KOKKINAKIS,
                    KIRANPAL_PANNU,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    THANASI_KOKKINAKIS: 1.01,
                    KIRANPAL_PANNU: 19.50,
                }
            },
            {
                'round': 512,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    MOHAMED_SAFWAT
                ],
                'score': [(0, 6), (6, 3), (6, 1)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 1.65,
                    MOHAMED_SAFWAT: 2.15
                }
            },
            {
                'round': 512,
                'players': [
                    NOAH_RUBIN,
                    EVAN_KING
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    NOAH_RUBIN: 1.30,
                    EVAN_KING: 3.20
                }
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    BERNARD_TOMIC,
                ],
                'score': [(6, 3), (4, 6), (6, 3)],
                'odds': {
                    TOMMY_PAUL: 2.20,
                    BERNARD_TOMIC: 1.59
                }
            },
            {
                'round': 512,
                'players': [
                    JASON_JUNG,
                    CHRISTOPHER_EUBANKS,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    JASON_JUNG: 1.91,
                    CHRISTOPHER_EUBANKS: 1.74
                }
            },
            {
                'round': 512,
                'players': [
                    HUBERT_HURKACZ,
                    ILLYA_MARCHENKO
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    HUBERT_HURKACZ: 1.54,
                    ILLYA_MARCHENKO: 2.40,
                }
            },
            {
                'round': 512,
                'players': [
                    DENIS_KUDLA,
                    JOHN_PATRICK_SMITH
                ],
                'score': [(3, 6), (7, 6), (6, 3)],
                'odds': {
                    DENIS_KUDLA: 1.48,
                    JOHN_PATRICK_SMITH: 2.45
                }
            },

            # 2018-07-22
            {
                'round': 256,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    TOMMY_PAUL
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 2.80,
                    TOMMY_PAUL: 1.30
                }
            },
            {
                'round': 256,
                'players': [
                    NOAH_RUBIN,
                    JASON_JUNG
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    NOAH_RUBIN: 1.69,
                    JASON_JUNG: 1.95
                }
            },
            {
                'round': 256,
                'players': [
                    THANASI_KOKKINAKIS,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    THANASI_KOKKINAKIS: 1.60,
                    HUBERT_HURKACZ: 2.20
                }
            },
            {
                'round': 256,
                'players': [
                    ALEX_BOLT,
                    DENIS_KUDLA
                ],
                'score': [(6, 7), (6, 3), (6, 3)],
                'odds': {
                    ALEX_BOLT: 2.90,
                    DENIS_KUDLA: 1.36
                }
            },

            # 2018-07-23
            {
                'round': 32,
                'players': [
                    DONALD_YOUNG,
                    IVO_KARLOVIC
                ],
                'score': [(2, 6), (7, 6), (7, 6)],
                'odds': {
                    DONALD_YOUNG: 2.55,
                    IVO_KARLOVIC: 1.50
                }
            },
            {
                'round': 32,
                'players': [
                    LUKAS_LACKO,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    LUKAS_LACKO: 1.50,
                    PRAJNESH_GUNNESWARAN: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    ALEX_DE_MINAUR,
                    HUBERT_HURKACZ
                ],
                'score': [(1, 6), (7, 6), (7, 6)],
                'odds': {
                    ALEX_DE_MINAUR: 1.47,
                    HUBERT_HURKACZ: 2.55
                }
            },

            # 2018-07-24
            {
                'round': 32,
                'players': [
                    MIKHAIL_YOUZHNY,
                    EMIL_REINBERG
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    MIKHAIL_YOUZHNY: 1.10,
                    EMIL_REINBERG: 5.75
                }
            },
            {
                'round': 32,
                'players': [
                    NOAH_RUBIN,
                    THANASI_KOKKINAKIS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    NOAH_RUBIN: 2.50,
                    THANASI_KOKKINAKIS: 1.45
                }
            },
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    MALEK_JAZIRI
                ],
                'score': [(7, 5), (6, 0)],
                'odds': {
                    CAMERON_NORRIE: 1.60,
                    MALEK_JAZIRI: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    TAYLOR_FRITZ,
                    RAMKUMAR_RAMANATHAN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 1.32,
                    RAMKUMAR_RAMANATHAN: 3.30
                }
            },
            {
                'round': 32,
                'players': [
                    MARCOS_BAGHDATIS,
                    ALEX_BOLT
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    MARCOS_BAGHDATIS: 1.61,
                    ALEX_BOLT: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    RYAN_HARRISON,
                    JAMES_DUCKWORTH
                ],
                'score': [(4, 6), (7, 6), (6, 1)],
                'odds': {
                    RYAN_HARRISON: 1.42,
                    JAMES_DUCKWORTH: 2.70
                }
            },
            {
                'round': 32,
                'players': [
                    MISCHA_ZVEREV,
                    TIM_SMYCZEK
                ],
                'score': [(6, 3), (6, 7), (6, 3)],
                'odds': {
                    MISCHA_ZVEREV: 1.57,
                    TIM_SMYCZEK: 2.40
                }
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    RICARDAS_BERANKIS
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    JEREMY_CHARDY: 1.48,
                    RICARDAS_BERANKIS: 2.55
                }
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    MARIUS_COPIL
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    FRANCES_TIAFOE: 1.30,
                    MARIUS_COPIL: 3.40
                }
            },

            # 2018-07-25
            {
                'round': 16,
                'players': [
                    RYAN_HARRISON,
                    LUKAS_LACKO
                ],
                'score': [(2, 6), (6, 2), (6, 3)],
                'odds': {
                    RYAN_HARRISON: 1.61,
                    LUKAS_LACKO: 2.20
                }
            },
            {
                'round': 16,
                'players': [
                    MISCHA_ZVEREV,
                    MIKHAIL_YOUZHNY
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MISCHA_ZVEREV: 1.47,
                    MIKHAIL_YOUZHNY: 2.55
                }
            },
            {
                'round': 16,
                'players': [
                    HYEON_CHUNG,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    HYEON_CHUNG: 1.90,
                    TAYLOR_FRITZ: 1.80
                }
            },
            {
                'round': 16,
                'players': [
                    JOHN_ISNER,
                    ALEX_DE_MINAUR
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JOHN_ISNER: 1.24,
                    ALEX_DE_MINAUR: 3.75
                }
            },

            # 2018-07-26
            {
                'round': 16,
                'players': [
                    CAMERON_NORRIE,
                    JEREMY_CHARDY
                ],
                'score': [(5, 7), (6, 4), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 2.30,
                    JEREMY_CHARDY: 1.56
                }
            },
            {
                'round': 16,
                'players': [
                    MARCOS_BAGHDATIS,
                    FRANCES_TIAFOE
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    MARCOS_BAGHDATIS: 2.55,
                    FRANCES_TIAFOE: 1.48
                }
            },
            {
                'round': 16,
                'players': [
                    MATTHEW_EBDEN,
                    DONALD_YOUNG
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MATTHEW_EBDEN: 1.54,
                    DONALD_YOUNG: 2.40
                }
            },
            {
                'round': 16,
                'players': [
                    NICK_KYRGIOS,
                    NOAH_RUBIN
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    NICK_KYRGIOS: 1.19,
                    NOAH_RUBIN: 4.50
                }
            },

            # 2018-07-27
            {
                'round': 8,
                'players': [
                    MATTHEW_EBDEN,
                    MARCOS_BAGHDATIS
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    MATTHEW_EBDEN: 2.15,
                    MARCOS_BAGHDATIS: 1.61
                }
            },
            {
                'round': 8,
                'players': [
                    RYAN_HARRISON,
                    HYEON_CHUNG
                ],
                'score': [(6, 7), (6, 2), (7, 6)],
                'odds': {
                    RYAN_HARRISON: 2.70,
                    HYEON_CHUNG: 1.42
                }
            },
            {
                'round': 8,
                'players': [
                    CAMERON_NORRIE,
                    NICK_KYRGIOS
                ],
                'score': [(7, 5), (3, 0)],
                'retired': True,
                'odds': {
                    CAMERON_NORRIE: 4.05,
                    NICK_KYRGIOS: 1.22
                }
            },
            {
                'round': 8,
                'players': [
                    JOHN_ISNER,
                    MISCHA_ZVEREV
                ],
                'score': [(7, 5), (4, 6), (6, 1)],
                'odds': {
                    JOHN_ISNER: 1.33,
                    MISCHA_ZVEREV: 3.10
                }
            },

            # 2018-07-28
            {
                'round': 4,
                'players': [
                    RYAN_HARRISON,
                    CAMERON_NORRIE
                ],
                'score': [(2, 6), (6, 3), (6, 2)],
                'odds': {
                    RYAN_HARRISON: 1.80,
                    CAMERON_NORRIE: 2.00
                }
            },
            {
                'round': 4,
                'players': [
                    JOHN_ISNER,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 4), (6, 7), (6, 1)],
                'odds': {
                    JOHN_ISNER: 1.20,
                    MATTHEW_EBDEN: 4.20
                }
            },

            # 2018-07-29
            {
                'round': 2,
                'players': [
                    JOHN_ISNER,
                    RYAN_HARRISON
                ],
                'score': [(5, 7), (6, 3), (6, 4)],
                'odds': {
                    JOHN_ISNER: 1.25,
                    RYAN_HARRISON: 3.65
                }
            }
        ],
    },

    {
        'location': GSTAAD,
        'date': '2018-07-29',
        'matches': [

            # 2018-07-21
            {
                'round': 512,
                'players': [
                    YANN_MARTI,
                    ADRIAN_BODMER
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    YANN_MARTI: 1.55,
                    ADRIAN_BODMER: 2.55
                }
            },
            {
                'round': 512,
                'players': [
                    VIKTOR_GALOVIC,
                    GONZALO_ESCOBAR
                ],
                'score': [(6, 3), (3, 6), (7, 6)],
                'odds': {
                    VIKTOR_GALOVIC: 1.50,
                    GONZALO_ESCOBAR: 2.15
                }
            },
            {
                'round': 512,
                'players': [
                    ORIOL_ROCA_BATALLA,
                    KENNY_DE_SCHEPPER
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    ORIOL_ROCA_BATALLA: 2.10,
                    KENNY_DE_SCHEPPER: 1.67
                }
            },
            {
                'round': 512,
                'players': [
                    JAKUB_PAUL,
                    MATTEO_DONATI
                ],
                'score': [(4, 6), (6, 4), (6, 4)],
                'odds': {
                    JAKUB_PAUL: 11.00,
                    MATTEO_DONATI: 1.04
                }
            },
            {
                'round': 512,
                'players': [
                    FACUNDO_BAGNIS,
                    KEVIN_KRAWIETZ
                ],
                'score': [(6, 3), (3, 6), (6, 2)],
                'odds': {
                    FACUNDO_BAGNIS: 1.27,
                    KEVIN_KRAWIETZ: 3.15
                }
            },
            {
                'round': 512,
                'players': [
                    ADRIAN_MENENDEZ_MACEIRAS,
                    SANTIAGO_GIRALDO
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    ADRIAN_MENENDEZ_MACEIRAS: 2.62,
                    SANTIAGO_GIRALDO: 1.47
                }
            },
            {
                'round': 512,
                'players': [
                    JURGEN_ZOPP,
                    ANDRES_MOLTENI
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    JURGEN_ZOPP: 1.10,
                    ANDRES_MOLTENI: 2.60
                }
            },
            {
                'round': 512,
                'players': [
                    YANNICK_HANFMANN,
                    LUCA_MARGAROLI
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    YANNICK_HANFMANN: 1.01,
                    LUCA_MARGAROLI: 14.82
                }
            },

            # 2018-07-22
            {
                'round': 256,
                'players': [
                    FACUNDO_BAGNIS,
                    YANN_MARTI
                ],
                'score': [],
                'retired': True,
                'odds': {
                    FACUNDO_BAGNIS: 1.15,
                    YANN_MARTI: 5.00
                }
            },
            {
                'round': 256,
                'players': [
                    ADRIAN_MENENDEZ_MACEIRAS,
                    JAKUB_PAUL
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    ADRIAN_MENENDEZ_MACEIRAS: 1.16,
                    JAKUB_PAUL: 4.80
                }
            },
            {
                'round': 256,
                'players': [
                    JURGEN_ZOPP,
                    ORIOL_ROCA_BATALLA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JURGEN_ZOPP: 1.47,
                    ORIOL_ROCA_BATALLA: 2.63
                }
            },
            {
                'round': 256,
                'players': [
                    YANNICK_HANFMANN,
                    VIKTOR_GALOVIC
                ],
                'score': [(6, 7), (7, 6), (6, 4)],
                'odds': {
                    YANNICK_HANFMANN: 1.24,
                    VIKTOR_GALOVIC: 3.65
                }
            },

            # 2018-07-23
            {
                'round': 32,
                'players': [
                    JURGEN_ZOPP,
                    YANNICK_HANFMANN
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    JURGEN_ZOPP: 2.80,
                    YANNICK_HANFMANN: 1.38
                }
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    ADRIAN_MENENDEZ_MACEIRAS
                ],
                'score': [(6, 1), (6, 0)],
                'odds': {
                    JAUME_MUNAR: 1.36,
                    ADRIAN_MENENDEZ_MACEIRAS: 2.73
                }
            },
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    ELIAS_YMER
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    TARO_DANIEL: 1.67,
                    ELIAS_YMER: 2.10
                }
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.63,
                    GUIDO_ANDREOZZI: 2.27
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 2.22,
                    GUILLERMO_GARCIA_LOPEZ: 1.69
                }
            },

            # 2018-07-24
            {
                'round': 32,
                'players': [
                    ORIOL_ROCA_BATALLA,
                    PAOLO_LORENZI
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    MARC_ANDREA_HUESLER,
                    NICOLAS_ALMAGRO
                ],
                'score': [(6, 7), (6, 3), (7, 6)],
                'odds': {
                    MARC_ANDREA_HUESLER: 3.05,
                    NICOLAS_ALMAGRO: 1.37
                }
            },
            {
                'round': 32,
                'players': [
                    LASLO_DJERE,
                    DENIS_ISTOMIN
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    LASLO_DJERE: 1.48,
                    DENIS_ISTOMIN: 2.65
                }
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    RADU_ALBOT
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 1.57,
                    RADU_ALBOT: 2.40
                }
            },
            {
                'round': 32,
                'players': [
                    FELICIANO_LOPEZ,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    FELICIANO_LOPEZ: 2.05,
                    FEDERICO_DELBONIS: 1.71
                }
            },
            {
                'round': 32,
                'players': [
                    FACUNDO_BAGNIS,
                    JOAO_SOUSA
                ],
                'score': [(4, 6), (6, 3), (7, 5)],
                'odds': {
                    FACUNDO_BAGNIS: 2.43,
                    JOAO_SOUSA: 1.50
                }
            },
            {
                'round': 32,
                'players': [
                    VIKTOR_GALOVIC,
                    ROBIN_HAASE
                ],
                'score': [(6, 1), (3, 6), (6, 3)],
                'odds': {
                    VIKTOR_GALOVIC: 3.99,
                    ROBIN_HAASE: 1.24
                }
            },

            # 2018-07-25
            {
                'round': 16,
                'players': [
                    TARO_DANIEL,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    TARO_DANIEL: 2.27,
                    ROBERTO_CARBALLES_BAENA: 1.67
                }
            },
            {
                'round': 16,
                'players': [
                    FELICIANO_LOPEZ,
                    ORIOL_ROCA_BATALLA
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 1.27,
                    ORIOL_ROCA_BATALLA: 3.90
                }
            },
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 2.10,
                    ANDREY_RUBLEV: 1.69
                }
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    JAUME_MUNAR
                ],
                'score': [(2, 6), (6, 3), (6, 2)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.50,
                    JAUME_MUNAR: 2.60
                }
            },

            # 2018-07-26
            {
                'round': 16,
                'players': [
                    VIKTOR_GALOVIC,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(3, 6), (6, 4), (6, 2)],
                'odds': {
                    VIKTOR_GALOVIC: 3.00,
                    FELIX_AUGER_ALIASSIME: 1.39
                }
            },
            {
                'round': 16,
                'players': [
                    FACUNDO_BAGNIS,
                    MARC_ANDREA_HUESLER
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    FACUNDO_BAGNIS: 1.17,
                    MARC_ANDREA_HUESLER: 4.57
                }
            },
            {
                'round': 16,
                'players': [
                    LASLO_DJERE,
                    BORNA_CORIC
                ],
                'score': [(6, 4), (1, 6), (6, 1)],
                'odds': {
                    LASLO_DJERE: 3.15,
                    BORNA_CORIC: 1.29
                }
            },
            {
                'round': 16,
                'players': [
                    JURGEN_ZOPP,
                    FABIO_FOGNINI
                ],
                'score': [(6, 1), (3, 6), (6, 3)],
                'odds': {
                    JURGEN_ZOPP: 4.05,
                    FABIO_FOGNINI: 1.26
                }
            },

            # 2018-07-27
            {
                'round': 8,
                'players': [
                    JURGEN_ZOPP,
                    FACUNDO_BAGNIS
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    JURGEN_ZOPP: 2.05,
                    FACUNDO_BAGNIS: 1.71
                }
            },
            {
                'round': 8,
                'players': [
                    LASLO_DJERE,
                    VIKTOR_GALOVIC
                ],
                'score': [(6, 7), (6, 3), (7, 6)],
                'odds': {
                    LASLO_DJERE: 1.38,
                    VIKTOR_GALOVIC: 3.00
                }
            },
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    FELICIANO_LOPEZ
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.74,
                    FELICIANO_LOPEZ: 2.05
                }
            },
            {
                'round': 8,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    TARO_DANIEL
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.34,
                    TARO_DANIEL: 3.30
                }
            },

            # 2018-07-28
            {
                'round': 4,
                'players': [
                    MATTEO_BERRETTINI,
                    JURGEN_ZOPP
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 1.35,
                    JURGEN_ZOPP: 3.12
                }
            },
            {
                'round': 4,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    LASLO_DJERE
                ],
                'score': [(6, 7), (6, 4), (6, 4)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.32,
                    LASLO_DJERE: 3.50
                }
            },

            # 2018-07-29
            {
                'round': 2,
                'players': [
                    MATTEO_BERRETTINI,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 2.50,
                    ROBERTO_BAUTISTA_AGUT: 1.50
                }
            }
        ]
    },
]
