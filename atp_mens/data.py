from men import *

# 65  2.47  2019-03-02 Dubai Duty Free Tennis Championships
# 64  2.27  bet unit fixed at 5
# 64 50.93 <- 2019-03-02 Abierto Mexicano Telcel presentado por HSBC
# 53 1.68 <- bet multiplier added
# 53 -1.74 <- 2019-03-03 Brasil Open
# 50 -1.73 <- 2019-03-17 BNP Paribas Open
# 57 -1.03 <- 2019-03-31 Miami Open presented by Itau
# 65 -0.80 <- 2019-04-14 Fayez Sarofim & Co US Mens Clay Court Championship
# 68 -0.09 <- 2019-04-14 Grand Prix Hassan II
# 69 0.32  <- 2019-04-21 Rolex Monte-Carlo Masters
# 62 -1.15 <- 2019-04-28 Barcelona Open Banc Sabadell
# 68 -0.57 <- 2019-04-22 Hungarian Open
# 65 -0.83 <- 2019-04-29 BMW Open by FWU
# 67 -0.40 <- 2019-04-29 Millennium Estoril Open
# 62 -1.12 <- Mutua Madrid Open
# 52 -2.88 <- added round as variable
# 58 -2.32 <- italia
# 61 -1.57 <- geneva
# 56 -1.58 <- parc auvergne
# 54 -1.41 <- roland garros 2019
# 54 -1.29 <- partial roland garros 2019

DATA = [
    {
        'name': 'Dubai Duty Free Tennis Championships',
        'category': 'ATP500',
        'date': '2019-03-02',
        'location': 'Dubai, United Arab Emirates',
        'matches': [
            {
                'round': 512,
                'players': [
                    MIRZA_BASIC,
                    SIMON_CARR
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    MIRZA_BASIC: 1.04,
                    SIMON_CARR: 7.00
                },
                'prediction': MIRZA_BASIC,
            },
            {
                'round': 512,
                'players': [
                    EGOR_GERASIMOV,
                    ALEKSANDR_NEDOVYESOV
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    EGOR_GERASIMOV: 1.49,
                    ALEKSANDR_NEDOVYESOV: 2.45
                },
                'prediction': EGOR_GERASIMOV
            },
            {
                'round': 512,
                'players': [
                    ANTOINE_HOANG,
                    ADHAM_GABER
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    ANTOINE_HOANG: 1.01,
                    ADHAM_GABER: 20.68
                },
                'prediction': ANTOINE_HOANG,
            },
            {
                'round': 512,
                'players': [
                    CORENTIN_MOUTET,
                    KARIM_MOHAMED_MAAMOUN
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    CORENTIN_MOUTET: 1.24,
                    KARIM_MOHAMED_MAAMOUN: 3.45
                },
                'prediction': CORENTIN_MOUTET
            },
            {
                'round': 512,
                'players': [
                    RICARDAS_BERANKIS,
                    CONSTANT_LESTIENNE
                ],
                'score': [(6, 3), (3, 6), (6, 2)],
                'odds': {
                    RICARDAS_BERANKIS: 1.48,
                    CONSTANT_LESTIENNE: 2.60
                },
                'prediction': CONSTANT_LESTIENNE
            },
            {
                'round': 512,
                'players': [
                    JIRI_VESELY,
                    JAMES_WARD
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JIRI_VESELY: 1.36,
                    JAMES_WARD: 2.88
                },
                'prediction': JIRI_VESELY
            },
            {
                'round': 512,
                'players': [
                    THOMAS_FABBIANO,
                    RUDOLF_MOLLEKER
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    THOMAS_FABBIANO: 1.36,
                    RUDOLF_MOLLEKER: 2.95
                },
                'prediction': THOMAS_FABBIANO
            },
            {
                'round': 512,
                'players': [
                    ILYA_IVASHKA,
                    ALEXEY_VATUTIN
                ],
                'score': [(5, 7), (7, 5), (6, 2)],
                'odds': {
                    ILYA_IVASHKA: 1.54,
                    ALEXEY_VATUTIN: 2.42
                },
                'prediction': ILYA_IVASHKA
            },

            # 2019-02-24
            {
                'round': 256,
                'players': [
                    RICARDAS_BERANKIS,
                    MIRZA_BASIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    RICARDAS_BERANKIS: 1.38,
                    MIRZA_BASIC: 2.85
                },
                'prediction': RICARDAS_BERANKIS
            },
            {
                'round': 256,
                'players': [
                    EGOR_GERASIMOV,
                    JIRI_VESELY
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    EGOR_GERASIMOV: 1.62,
                    JIRI_VESELY: 2.20
                },
                'prediction': EGOR_GERASIMOV
            },
            {
                'round': 256,
                'players': [
                    THOMAS_FABBIANO,
                    ANTOINE_HOANG
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    THOMAS_FABBIANO: 1.65,
                    ANTOINE_HOANG: 2.06
                },
                'prediction': THOMAS_FABBIANO
            },
            {
                'round': 256,
                'players': [
                    CORENTIN_MOUTET,
                    ILYA_IVASHKA
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    CORENTIN_MOUTET: 1.80,
                    ILYA_IVASHKA: 1.81
                },
                'prediction': CORENTIN_MOUTET
            },

            # 2019-02-25
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    THOMAS_FABBIANO
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    FERNANDO_VERDASCO: 1.38,
                    THOMAS_FABBIANO: 3.00
                }
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    MARTON_FUCSOVICS: 1.53,
                    DAMIR_DZUMHUR: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    RAMKUMAR_RAMANATHAN
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.07,
                    RAMKUMAR_RAMANATHAN: 7.50
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    MILOS_RAONIC
                ],
                'score': [(6, 4), (5, 7), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 5.00,
                    MILOS_RAONIC: 1.18
                }
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.66,
                    KAREN_KHACHANOV: 1.48
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 4), (3, 6), (6, 1)],
                'odds': {
                    ROGER_FEDERER: 1.12,
                    PHILIPP_KOHLSCHREIBER: 6.52
                }
            },

            # 2019-02-26
            {
                'round': 32,
                'players': [
                    DENIS_KUDLA,
                    MATTEO_BERRETTINI
                ],
                'score': [(2, 6), (7, 5), (7, 5)],
                'odds': {
                    DENIS_KUDLA: 2.93,
                    MATTEO_BERRETTINI: 1.36
                }
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    CORENTIN_MOUTET
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    HUBERT_HURKACZ: 1.59,
                    CORENTIN_MOUTET: 2.35
                }
            },
            {
                'round': 32,
                'players': [
                    EGOR_GERASIMOV,
                    ROBIN_HAASE
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    EGOR_GERASIMOV: 1.92,
                    ROBIN_HAASE: 1.80
                }
            },
            {
                'round': 32,
                'players': [
                    TOMAS_BERDYCH,
                    ILYA_IVASHKA
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    TOMAS_BERDYCH: 1.14,
                    ILYA_IVASHKA: 5.27
                }
            },
            {
                'round': 32,
                'players': [
                    MARCOS_BAGHDATIS,
                    MOHAMED_SAFWAT
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    MARCOS_BAGHDATIS: 1.15,
                    MOHAMED_SAFWAT: 5.50
                }
            },
            {
                'round': 32,
                'players': [
                    RICARDAS_BERANKIS,
                    DANILL_MEDVEDEV
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    RICARDAS_BERANKIS: 5.00,
                    DANILL_MEDVEDEV: 1.13
                }
            },
            {
                'round': 32,
                'players': [
                    BORNA_CORIC,
                    JIRI_VESELY
                ],
                'score': [(7, 5), (3, 6), (7, 6)],
                'odds': {
                    BORNA_CORIC: 1.20,
                    JIRI_VESELY: 4.31
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.22,
                    MATTHEW_EBDEN: 4.15
                }
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    MARIN_CILIC
                ],
                'score': [(6, 3), (4, 6), (6, 0)],
                'odds': {
                    GAEL_MONFILS: 1.85,
                    MARIN_CILIC: 1.91
                }
            },
            {
                'round': 32,
                'players': [
                    KEI_NISHIKORI,
                    BENOIT_PAIRE
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    KEI_NISHIKORI: 1.19,
                    BENOIT_PAIRE: 4.60
                }
            },

            # 2019-02-27
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    MARCOS_BAGHDATIS
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    GAEL_MONFILS: 1.13,
                    MARCOS_BAGHDATIS: 5.25
                }
            },
            {
                'round': 16,
                'players': [
                    MARTON_FUCSOVICS,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MARTON_FUCSOVICS: 1.59,
                    JAN_LENNARD_STRUFF: 2.35
                }
            },
            {
                'round': 16,
                'players': [
                    RICARDAS_BERANKIS,
                    DENIS_KUDLA
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    RICARDAS_BERANKIS: 1.56,
                    DENIS_KUDLA: 2.42
                }
            },
            {
                'round': 16,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(6, 7), (6, 4), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 3.10,
                    ROBERTO_BAUTISTA_AGUT: 1.34
                }
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    TOMAS_BERDYCH
                ],
                'score': [(1, 6), (6, 1), (7, 6)],
                'odds': {
                    BORNA_CORIC: 1.95,
                    TOMAS_BERDYCH: 1.71
                }
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    EGOR_GERASIMOV
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.21,
                    EGOR_GERASIMOV: 4.33
                }
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.17,
                    FERNANDO_VERDASCO: 5.22
                }
            },
            {
                'round': 16,
                'players': [
                    HUBERT_HURKACZ,
                    KEI_NISHIKORI
                ],
                'score': [(7, 5), (5, 7), (6, 2)],
                'odds': {
                    HUBERT_HURKACZ: 5.50,
                    KEI_NISHIKORI: 1.14
                }
            },

            # 2019-02-28
            {
                'round': 8,
                'players': [
                    GAEL_MONFILS,
                    RICARDAS_BERANKIS
                ],
                'score': [(6, 1), (6, 7), (6, 2)],
                'odds': {
                    GAEL_MONFILS: 1.18,
                    RICARDAS_BERANKIS: 4.78
                }
            },
            {
                'round': 8,
                'players': [
                    BORNA_CORIC,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(4, 6), (6, 2), (7, 6)],
                'odds': {
                    BORNA_CORIC: 1.71,
                    NIKOLOZ_BASILASHVILI: 1.95
                }
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    HUBERT_HURKACZ
                ],
                'score': [(7, 6), (6, 7), (6, 1)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.20,
                    HUBERT_HURKACZ: 4.00
                }
            },
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    MARTON_FUCSOVICS
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.13,
                    MARTON_FUCSOVICS: 5.00
                }
            },

            # 2019-03-01
            {
                'round': 4,
                'players': [
                    STEFANOS_TSITSIPAS,
                    GAEL_MONFILS
                ],
                'score': [(4, 6), (7, 6), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.95,
                    GAEL_MONFILS: 1.74
                }
            },
            {
                'round': 4,
                'players': [
                    ROGER_FEDERER,
                    BORNA_CORIC
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    ROGER_FEDERER: 1.36,
                    BORNA_CORIC: 3.00
                }
            },

            # 2019-03-02
            {
                'round': 2,
                'players': [
                    ROGER_FEDERER,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.32,
                    STEFANOS_TSITSIPAS: 3.45
                }
            }
        ]
    },

    {
        'name': 'Abierto Mexicano Telcel presentado por HSBC',
        'category': 'ATP500',
        'date': '2019-03-02',
        'location': 'Acapulco, Mexico',
        'matches': [

            # 2019-02-23
            {
                'round': 512,
                'players': [
                    EMILIO_GOMEZ,
                    DANIEL_ELAHI_GALAN
                ],
                'score': [(6, 4), (6, 4)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    FEDERICO_GAIO,
                    ANTE_PAVIC
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    FEDERICO_GAIO: 1.57,
                    ANTE_PAVIC: 2.31
                }
            },
            {
                'round': 512,
                'players': [
                    ADRIAN_MENENDEZ_MACEIRAS,
                    LUIS_PATINO
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ADRIAN_MENENDEZ_MACEIRAS: 1.08,
                    LUIS_PATINO: 6.45
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    ROBERTO_ORTEGA_OLMEDO
                ],
                'score': [(6, 2)],
                'retired': True,
                'odds': {
                    ALEXEI_POPYRIN: 1.22,
                    ROBERTO_ORTEGA_OLMEDO: 3.50
                }
            },
            {
                'round': 512,
                'players': [
                    MARCEL_GRANOLLERS,
                    KEVIN_KRAWIETZ
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.24,
                    KEVIN_KRAWIETZ: 4.00
                }
            },
            {
                'round': 512,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    ROBERTO_CID_SUBERVI
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    GUILLERMO_GARCIA_LOPEZ: 1.13,
                    ROBERTO_CID_SUBERVI: 5.50
                }
            },
            {
                'round': 512,
                'players': [
                    RYAN_HARRISON,
                    JUAN_ALEJANDRO_HERNANDEZ
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    RYAN_HARRISON: 1.01,
                    JUAN_ALEJANDRO_HERNANDEZ: 18.35
                }
            },
            {
                'round': 512,
                'players': [
                    BERNARD_TOMIC,
                    LUCAS_GOMEZ
                ],
                'score': [(6, 1), (5, 7), (6, 0)],
                'odds': {
                    BERNARD_TOMIC: 1.07,
                    LUCAS_GOMEZ: 7.00
                }
            },

            # 2019-02-24
            {
                'round': 256,
                'players': [
                    FEDERICO_GAIO,
                    EMILIO_GOMEZ
                ],
                'score': [(6, 1), (4, 6), (7, 6)],
                'odds': {
                    FEDERICO_GAIO: 2.00,
                    EMILIO_GOMEZ: 1.71
                }
            },
            {
                'round': 256,
                'players': [
                    MARCEL_GRANOLLERS,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(6, 4), (3, 6), (6, 1)],
                'odds': {
                    MARCEL_GRANOLLERS: 2.05,
                    GUILLERMO_GARCIA_LOPEZ: 1.67
                }
            },
            {
                'round': 256,
                'players': [
                    RYAN_HARRISON,
                    ADRIAN_MENENDEZ_MACEIRAS
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    RYAN_HARRISON: 1.27,
                    ADRIAN_MENENDEZ_MACEIRAS: 3.49
                }
            },
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    BERNARD_TOMIC
                ],
                'score': [],
                'wo': True,
                'odds': {
                    ALEXEI_POPYRIN: 2.03,
                    BERNARD_TOMIC: 1.63
                }
            },

            # 2019-02-25
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    RYAN_HARRISON
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    STAN_WAWRINKA: 1.33,
                    RYAN_HARRISON: 3.15
                }
            },
            {
                'round': 32,
                'players': [
                    PETER_GOJOWCZYK,
                    FEDERICO_GAIO
                ],
                'score': [(5, 7), (6, 4), (6, 2)],
                'odds': {
                    PETER_GOJOWCZYK: 1.25,
                    FEDERICO_GAIO: 3.70
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    MARCEL_GRANOLLERS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JOHN_MILLMAN: 1.31,
                    MARCEL_GRANOLLERS: 3.40
                }
            },
            {
                'round': 32,
                'players': [
                    STEVE_JOHNSON,
                    GERARDO_LOPEZ_VILLASENOR
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    STEVE_JOHNSON: 1.09,
                    GERARDO_LOPEZ_VILLASENOR: 6.25
                }
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    JORDAN_THOMPSON
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    FRANCES_TIAFOE: 1.63,
                    JORDAN_THOMPSON: 2.24
                }
            },

            # 2019-02-26
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    SAM_QUERREY: 1.32,
                    GUILLERMO_GARCIA_LOPEZ: 3.69
                }
            },
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 2), (2, 6), (6, 2)],
                'odds': {
                    CAMERON_NORRIE: 2.12,
                    YOSHIHITO_NISHIOKA: 1.67
                }
            },
            {
                'round': 32,
                'players': [
                    MACKENZIE_MCDONALD,
                    EMILIO_NAVA
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    MACKENZIE_MCDONALD: 1.06,
                    EMILIO_NAVA: 9.60
                }
            },
            {
                'round': 32,
                'players': [
                    FELICIANO_LOPEZ,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 7), (6, 2), (7, 5)],
                'odds': {
                    FELICIANO_LOPEZ: 2.02,
                    DUSAN_LAJOVIC: 1.77
                }
            },
            {
                'round': 32,
                'players': [
                    NICK_KYRGIOS,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    NICK_KYRGIOS: 2.05,
                    ANDREAS_SEPPI: 1.71
                }
            },
            {
                'round': 32,
                'players': [
                    DAVID_FERRER,
                    TENNYS_SANDGREN
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    DAVID_FERRER: 1.58,
                    TENNYS_SANDGREN: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    ALEX_DE_MINAUR,
                    NICOLAS_JARRY
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    ALEX_DE_MINAUR: 1.31,
                    NICOLAS_JARRY: 3.60
                }
            },
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MARIUS_COPIL
                ],
                'score': [(6, 3), (4, 6), (6, 1)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.65,
                    MARIUS_COPIL: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_ISNER,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 3), (4, 6), (6, 3)],
                'odds': {
                    JOHN_ISNER: 1.31,
                    ADRIAN_MANNARINO: 3.35
                }
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.17,
                    ALEXEI_POPYRIN: 5.50
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.06,
                    MISCHA_ZVEREV: 11.50
                }
            },

            # 2019-02-27
            {
                'round': 16,
                'players': [
                    JOHN_MILLMAN,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 0), (6, 2)],
                'odds': {
                    JOHN_MILLMAN: 1.43,
                    PETER_GOJOWCZYK: 2.80
                }
            },
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    STEVE_JOHNSON
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    STAN_WAWRINKA: 1.29,
                    STEVE_JOHNSON: 3.55
                }
            },
            {
                'round': 16,
                'players': [
                    MACKENZIE_MCDONALD,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 7), (7, 5), (6, 3)],
                'odds': {
                    MACKENZIE_MCDONALD: 2.20,
                    FRANCES_TIAFOE: 1.67
                }
            },
            {
                'round': 16,
                'players': [
                    ALEX_DE_MINAUR,
                    FELICIANO_LOPEZ
                ],
                'score': [],
                'wo': True,
                'odds': {
                    ALEX_DE_MINAUR: 1.28,
                    FELICIANO_LOPEZ: 3.80
                }
            },
            {
                'round': 16,
                'players': [
                    JOHN_ISNER,
                    SAM_QUERREY
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JOHN_ISNER: 1.90,
                    SAM_QUERREY: 1.80
                }
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    DAVID_FERRER
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.20,
                    DAVID_FERRER: 4.86
                }
            },
            {
                'round': 16,
                'players': [
                    NICK_KYRGIOS,
                    RAFAEL_NADAL
                ],
                'score': [(3, 6), (7, 6), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 3.96,
                    RAFAEL_NADAL: 1.22
                }
            },

            # 2019-02-28
            {
                'round': 8,
                'players': [
                    CAMERON_NORRIE,
                    MACKENZIE_MCDONALD
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    CAMERON_NORRIE: 1.67,
                    MACKENZIE_MCDONALD: 2.10
                }
            },
            {
                'round': 8,
                'players': [
                    NICK_KYRGIOS,
                    STAN_WAWRINKA
                ],
                'score': [(7, 5), (6, 7), (6, 4)],
                'odds': {
                    NICK_KYRGIOS: 2.50,
                    STAN_WAWRINKA: 1.54
                }
            },
            {
                'round': 8,
                'players': [
                    JOHN_ISNER,
                    JOHN_MILLMAN
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.65,
                    JOHN_MILLMAN: 2.20
                }
            },
            {
                'round': 8,
                'players': [
                    ALEXANDER_ZVEREV,
                    ALEX_DE_MINAUR
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.36,
                    ALEX_DE_MINAUR: 3.24
                }
            },

            # 2019-03-01
            {
                'round': 4,
                'players': [
                    NICK_KYRGIOS,
                    JOHN_ISNER
                ],
                'score': [(7, 5), (5, 7), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 1.71,
                    JOHN_ISNER: 2.00
                }
            },
            {
                'round': 4,
                'players': [
                    ALEXANDER_ZVEREV,
                    CAMERON_NORRIE
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.18,
                    CAMERON_NORRIE: 5.48
                }
            },

            # 2019-03-02
            {
                'round': 2,
                'players': [
                    NICK_KYRGIOS,
                    ALEXANDER_ZVEREV
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    NICK_KYRGIOS: 3.01,
                    ALEXANDER_ZVEREV: 1.43
                }
            }
        ]
    },

    {
        'name': 'Brasil Open',
        'category': 'ATP250',
        'date': '2019-03-03',
        'location': 'Sao Paulo, Brazil',
        'matches': [

            # 2019-02-23
            {
                'round': 512,
                'players': [
                    PEDRO_SAKAMOTO,
                    MATTEO_DONATI
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    PEDRO_SAKAMOTO: 3.01,
                    MATTEO_DONATI: 1.36
                }
            },
            {
                'round': 512,
                'players': [
                    KIMMER_COPPEJANS,
                    JOAO_DOMINGUES
                ],
                'score': [(4, 6), (6, 0), (6, 3)],
                'odds': {
                    KIMMER_COPPEJANS: 1.61,
                    JOAO_DOMINGUES: 2.25
                }
            },
            {
                'round': 512,
                'players': [
                    FEDERICO_CORIA,
                    FACUNDO_ARGUELLO
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    FEDERICO_CORIA: 2.70,
                    FACUNDO_ARGUELLO: 1.31
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREJ_MARTIN,
                    DANIEL_GIMENO_TRAVER
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    ANDREJ_MARTIN: 1.65,
                    DANIEL_GIMENO_TRAVER: 2.11
                }
            },
            {
                'round': 512,
                'players': [
                    PEDRO_MARTINEZ,
                    JOAO_MENEZES
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    PEDRO_MARTINEZ: 1.36,
                    JOAO_MENEZES: 3.00
                }
            },
            {
                'round': 512,
                'players': [
                    ALESSANDRO_GIANNESSI,
                    JOAO_SOUSA
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALESSANDRO_GIANNESSI: 1.36,
                    JOAO_SOUSA: 2.98
                }
            },
            {
                'round': 512,
                'players': [
                    FACUNDO_BAGNIS,
                    ALEN_AVIDZBA
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    FACUNDO_BAGNIS: 1.21,
                    ALEN_AVIDZBA: 4.00
                }
            },
            {
                'round': 512,
                'players': [
                    CARLOS_BERLOCQ,
                    GIAN_MARCO_MORONI
                ],
                'score': [(1, 6), (6, 3), (6, 4)],
                'odds': {
                    CARLOS_BERLOCQ: 1.73,
                    GIAN_MARCO_MORONI: 2.01
                }
            },

            # 2019-02-24
            {
                'round': 256,
                'players': [
                    PEDRO_MARTINEZ,
                    FEDERICO_CORIA
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    PEDRO_MARTINEZ: 1.61,
                    FEDERICO_CORIA: 2.11
                }
            },
            {
                'round': 256,
                'players': [
                    ALESSANDRO_GIANNESSI,
                    KIMMER_COPPEJANS
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ALESSANDRO_GIANNESSI: 1.83,
                    KIMMER_COPPEJANS: 1.83
                }
            },
            {
                'round': 256,
                'players': [
                    FACUNDO_BAGNIS,
                    ANDREJ_MARTIN
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    FACUNDO_BAGNIS: 1.53,
                    ANDREJ_MARTIN: 2.47
                }
            },
            {
                'round': 256,
                'players': [
                    PEDRO_SAKAMOTO,
                    CARLOS_BERLOCQ
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PEDRO_SAKAMOTO: 3.21,
                    CARLOS_BERLOCQ: 1.33
                }
            },

            # 2019-02-25
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 2.40,
                    FEDERICO_DELBONIS: 1.59
                }
            },
            {
                'round': 32,
                'players': [
                    CRISTIAN_GARIN,
                    PEDRO_SOUSA
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    CRISTIAN_GARIN: 1.30,
                    PEDRO_SOUSA: 3.59
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    MAXIMILIAN_MARTERER
                ],
                'score': [(3, 6), (6, 1), (6, 2)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 2.12,
                    MAXIMILIAN_MARTERER: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    MARCO_TRUNGELLITI,
                    TARO_DANIEL
                ],
                'score': [(6, 4), (3, 6), (7, 6)],
                'odds': {
                    MARCO_TRUNGELLITI: 2.28,
                    TARO_DANIEL: 1.59
                }
            },

            # 2019-02-26
            {
                'round': 32,
                'players': [
                    THIAGO_SEYBOTH_WILD,
                    ELIAS_YMER
                ],
                'score': [(6, 3), (4, 6), (6, 2)],
                'odds': {
                    THIAGO_SEYBOTH_WILD: 2.60,
                    ELIAS_YMER: 1.48
                }
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    CASPER_RUUD: 1.71,
                    THIAGO_MONTEIRO: 2.10
                }
            },
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    FACUNDO_BAGNIS,
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.59,
                    FACUNDO_BAGNIS: 2.35
                }
            },
            {
                'round': 32,
                'players': [
                    HUGO_DELLIEN,
                    PEDRO_MARTINEZ
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    HUGO_DELLIEN: 1.74,
                    PEDRO_MARTINEZ: 2.00
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    PAOLO_LORENZI
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.53,
                    PAOLO_LORENZI: 2.44
                }
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    PEDRO_SAKAMOTO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JAUME_MUNAR: 1.10,
                    PEDRO_SAKAMOTO: 7.00
                }
            },

            # 2019-02-27
            {
                'round': 32,
                'players': [
                    LASLO_DJERE,
                    ALESSANDRO_GIANNESSI
                ],
                'score': [(7, 6), (4, 6), (6, 4)],
                'odds': {
                    LASLO_DJERE: 1.42,
                    ALESSANDRO_GIANNESSI: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    PABLO_CUEVAS
                ],
                'score': [(5, 7), (4, 6), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.48,
                    PABLO_CUEVAS: 1.51
                }
            },
            {
                'round': 16,
                'players': [
                    MARCO_TRUNGELLITI,
                    THIAGO_SEYBOTH_WILD
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    MARCO_TRUNGELLITI: 1.59,
                    THIAGO_SEYBOTH_WILD: 2.35
                }
            },
            {
                'round': 16,
                'players': [
                    CRISTIAN_GARIN,
                    JAUME_MUNAR
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    CRISTIAN_GARIN: 2.18,
                    JAUME_MUNAR: 1.67
                }
            },
            {
                'round': 16,
                'players': [
                    LEONARDO_MAYER,
                    LORENZO_SONEGO
                ],
                'score': [(6, 1), (3, 6), (6, 3)],
                'odds': {
                    LEONARDO_MAYER: 1.71,
                    LORENZO_SONEGO: 2.10
                }
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    GUIDO_PELLA: 1.67,
                    ROBERTO_CARBALLES_BAENA: 2.26
                }
            },

            # 2019-02-28
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.65,
                    ALBERT_RAMOS_VINOLAS: 2.05
                }
            },
            {
                'round': 16,
                'players': [
                    HUGO_DELLIEN,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    HUGO_DELLIEN: 2.43,
                    JUAN_IGNACIO_LONDERO: 1.56
                }
            },
            {
                'round': 16,
                'players': [
                    LASLO_DJERE,
                    MALEK_JAZIRI
                ],
                'score': [(6, 3), (3, 6), (7, 6)],
                'odds': {
                    LASLO_DJERE: 1.35,
                    MALEK_JAZIRI: 3.20
                }
            },
            {
                'round': 16,
                'players': [
                    CASPER_RUUD,
                    JOAO_SOUSA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    CASPER_RUUD: 1.78,
                    JOAO_SOUSA: 1.91
                }
            },

            # 2019-03-01
            {
                'round': 8,
                'players': [
                    CASPER_RUUD,
                    HUGO_DELLIEN
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    CASPER_RUUD: 1.48,
                    HUGO_DELLIEN: 2.60
                }
            },
            {
                'round': 8,
                'players': [
                    LASLO_DJERE,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 2), (3, 6), (6, 3)],
                'odds': {
                    LASLO_DJERE: 2.15,
                    FELIX_AUGER_ALIASSIME: 1.43
                }
            },
            {
                'round': 8,
                'players': [
                    CRISTIAN_GARIN,
                    LEONARDO_MAYER
                ],
                'score': [(4, 6), (6, 4), (6, 4)],
                'odds': {
                    CRISTIAN_GARIN: 2.00,
                    LEONARDO_MAYER: 1.77
                }
            },
            {
                'round': 8,
                'players': [
                    GUIDO_PELLA,
                    MARCO_TRUNGELLITI
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 1.17,
                    MARCO_TRUNGELLITI: 5.00
                }
            },

            # 2019-03-02
            {
                'round': 4,
                'players': [
                    CRISTIAN_GARIN,
                    CASPER_RUUD
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    CRISTIAN_GARIN: 2.16,
                    CASPER_RUUD: 1.65
                }
            },
            {
                'round': 4,
                'players': [
                    GUIDO_PELLA,
                    LASLO_DJERE
                ],
                'score': [(7, 6), (7, 6)],
                # no odds
            },

            # 2019-03-03
            {
                'round': 2,
                'players': [
                    GUIDO_PELLA,
                    CRISTIAN_GARIN
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 1.50,
                    CRISTIAN_GARIN: 2.44
                }
            }
        ]
    },

    {
        'name': 'BNP Paribas Open',
        'category': 'ATP1000',
        'date': '2019-03-17',
        'location': 'Indian Wells, United States',
        'matches': [

            # 2019-03-05
            {
                'round': 512,
                'players': [
                    MIOMIR_KECMANOVIC,
                    LUCA_VANNI
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.51,
                    LUCA_VANNI: 2.55
                }
            },
            {
                'round': 512,
                'players': [
                    BJORN_FRATANGELO,
                    ADRIAN_MENENDEZ_MACEIRAS
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    BJORN_FRATANGELO: 1.38,
                    ADRIAN_MENENDEZ_MACEIRAS: 2.78
                }
            },
            {
                'round': 512,
                'players': [
                    LUKAS_LACKO,
                    PETER_POLANSKY
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    LUKAS_LACKO: 2.20,
                    PETER_POLANSKY: 1.63
                }
            },
            {
                'round': 512,
                'players': [
                    ALEX_BOLT,
                    GIANLUIGI_QUINZI
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    ALEX_BOLT: 1.57,
                    GIANLUIGI_QUINZI: 2.29
                }
            },
            {
                'round': 512,
                'players': [
                    JC_ARAGONE,
                    HENRI_LAAKSONEN
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    JC_ARAGONE: 2.25,
                    HENRI_LAAKSONEN: 1.61
                }
            },
            {
                'round': 512,
                'players': [
                    EGOR_GERASIMOV,
                    EVGENY_DONSKOY
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    EGOR_GERASIMOV: 1.87,
                    EVGENY_DONSKOY: 1.77
                }
            },
            {
                'round': 512,
                'players': [
                    NOAH_RUBIN,
                    YANNICK_MADEN
                ],
                'score': [(6, 4), (3, 6), (6, 1)],
                'odds': {
                    NOAH_RUBIN: 2.45,
                    YANNICK_MADEN: 1.54
                }
            },
            {
                'round': 512,
                'players': [
                    ELIAS_YMER,
                    DARIAN_KING
                ],
                'score': [(1, 6), (6, 1), (6, 2)],
                'odds': {
                    ELIAS_YMER: 2.30,
                    DARIAN_KING: 1.59
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    ALEXEI_POPYRIN: 1.24,
                    JOZEF_KOVALIK: 3.90
                }
            },
            {
                'round': 512,
                'players': [
                    FILIP_KRAJINOVIC,
                    RAMKUMAR_RAMANATHAN
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.23,
                    RAMKUMAR_RAMANATHAN: 3.75
                }
            },
            {
                'round': 512,
                'players': [
                    JJ_WOLF,
                    MARCO_TRUNGELLITI
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    JJ_WOLF: 1.48,
                    MARCO_TRUNGELLITI: 2.55
                }
            },
            {
                'round': 512,
                'players': [
                    SALVATORE_CARUSO,
                    PAOLO_LORENZI
                ],
                'score': [(5, 4)],
                'retired': True,
                'odds': {
                    SALVATORE_CARUSO: 2.05,
                    PAOLO_LORENZI: 1.69
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREY_RUBLEV,
                    KAMIL_MAJCHRZAK
                ],
                'score': [(2, 6), (6, 4), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 1.30,
                    KAMIL_MAJCHRZAK: 3.40
                }
            },
            {
                'round': 512,
                'players': [
                    DENIS_ISTOMIN,
                    EVAN_SONG
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DENIS_ISTOMIN: 1.12,
                    EVAN_SONG: 5.85
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_EVANS,
                    RUBEN_BEMELMANS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DANIEL_EVANS: 1.17,
                    RUBEN_BEMELMANS: 4.90
                }
            },
            {
                'round': 512,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    JASON_JUNG
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 2.19,
                    JASON_JUNG: 1.63
                }
            },
            {
                'round': 512,
                'players': [
                    RICARDAS_BERANKIS,
                    YASUTAKA_UCHIYAMA
                ],
                'score': [(6, 4), (6, 7), (6, 2)],
                'odds': {
                    RICARDAS_BERANKIS: 1.31,
                    YASUTAKA_UCHIYAMA: 3.17
                }
            },
            {
                'round': 512,
                'players': [
                    TATSUMA_ITO,
                    CASPER_RUUD
                ],
                'score': [(6, 7), (6, 1), (6, 4)],
                'odds': {
                    TATSUMA_ITO: 3.10,
                    CASPER_RUUD: 1.34
                }
            },
            {
                'round': 512,
                'players': [
                    CHRISTOPHER_EUBANKS,
                    LLOYD_HARRIS
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    CHRISTOPHER_EUBANKS: 2.70,
                    LLOYD_HARRIS: 1.43
                }
            },
            {
                'round': 512,
                'players': [
                    MARCOS_GIRON,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 3), (2, 6), (6, 3)],
                'odds': {
                    MARCOS_GIRON: 2.20,
                    THOMAS_FABBIANO: 1.63
                }
            },
            {
                'round': 512,
                'players': [
                    LUKAS_ROSOL,
                    BERNARD_TOMIC
                ],
                'score': [(7, 6), (2, 6), (6, 3)],
                'odds': {
                    LUKAS_ROSOL: 2.65,
                    BERNARD_TOMIC: 1.45
                }
            },
            {
                'round': 512,
                'players': [
                    UGO_HUMBERT,
                    JURGEN_ZOPP
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    UGO_HUMBERT: 1.18,
                    JURGEN_ZOPP: 4.61
                }
            },
            {
                'round': 512,
                'players': [
                    CHRISTIAN_HARRISON,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    CHRISTIAN_HARRISON: 1.67,
                    JUAN_IGNACIO_LONDERO: 2.10
                }
            },
            {
                'round': 512,
                'players': [
                    RADU_ALBOT,
                    MITCHELL_KRUEGER
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    RADU_ALBOT: 1.35,
                    MITCHELL_KRUEGER: 2.85
                }
            },

            # 2019-03-06
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    LUKAS_ROSOL
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    ALEXEI_POPYRIN: 1.57,
                    LUKAS_ROSOL: 2.25
                }
            },
            {
                'round': 256,
                'players': [
                    TATSUMA_ITO,
                    JC_ARAGONE
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    TATSUMA_ITO: 2.20,
                    JC_ARAGONE: 1.62
                }
            },
            {
                'round': 256,
                'players': [
                    MARCOS_GIRON,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 7), (7, 5), (7, 6)],
                'odds': {
                    MARCOS_GIRON: 2.63,
                    MIOMIR_KECMANOVIC: 1.36
                }
            },
            {
                'round': 256,
                'players': [
                    ALEX_BOLT,
                    CHRISTOPHER_EUBANKS
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    ALEX_BOLT: 1.80,
                    CHRISTOPHER_EUBANKS: 1.87
                }
            },
            {
                'round': 256,
                'players': [
                    ELIAS_YMER,
                    CHRISTIAN_HARRISON
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    ELIAS_YMER: 1.59,
                    CHRISTIAN_HARRISON: 2.25
                }
            },
            {
                'round': 256,
                'players': [
                    BJORN_FRATANGELO,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 7), (7, 6), (6, 0)],
                'odds': {
                    BJORN_FRATANGELO: 3.45,
                    ANDREY_RUBLEV: 1.30
                }
            },
            {
                'round': 256,
                'players': [
                    DENIS_ISTOMIN,
                    EGOR_GERASIMOV
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DENIS_ISTOMIN: 1.69,
                    EGOR_GERASIMOV: 2.03
                }
            },
            {
                'round': 256,
                'players': [
                    DANIEL_EVANS,
                    NOAH_RUBIN
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    DANIEL_EVANS: 1.25,
                    NOAH_RUBIN: 3.80
                }
            },
            {
                'round': 256,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    SALVATORE_CARUSO
                ],
                'score': [(6, 2), (3, 6), (6, 2)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 1.59,
                    SALVATORE_CARUSO: 2.30
                }
            },
            {
                'round': 256,
                'players': [
                    FILIP_KRAJINOVIC,
                    RICARDAS_BERANKIS
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.57,
                    RICARDAS_BERANKIS: 2.31
                }
            },
            {
                'round': 256,
                'players': [
                    UGO_HUMBERT,
                    JJ_WOLF
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    UGO_HUMBERT: 1.24,
                    JJ_WOLF: 4.01
                }
            },
            {
                'round': 256,
                'players': [
                    RADU_ALBOT,
                    LUKAS_LACKO
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    RADU_ALBOT: 1.24,
                    LUKAS_LACKO: 3.89
                }
            },

            # 2019-03-07
            {
                'round': 128,
                'players': [
                    JORDAN_THOMPSON,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    JORDAN_THOMPSON: 1.59,
                    FEDERICO_DELBONIS: 2.47
                }
            },
            {
                'round': 128,
                'players': [
                    JAN_LENNARD_STRUFF,
                    JOHN_MILLMAN
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.93,
                    JOHN_MILLMAN: 1.41
                }
            },
            {
                'round': 128,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.18,
                    DAMIR_DZUMHUR: 1.69
                }
            },
            {
                'round': 128,
                'players': [
                    SAM_QUERREY,
                    MATTEO_BERRETTINI
                ],
                'score': [(7, 6), (2, 6), (6, 4)],
                'odds': {
                    SAM_QUERREY: 1.56,
                    MATTEO_BERRETTINI: 2.46
                }
            },
            {
                'round': 128,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    DENIS_KUDLA
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.44,
                    DENIS_KUDLA: 2.70
                }
            },
            {
                'round': 128,
                'players': [
                    LEONARDO_MAYER,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    LEONARDO_MAYER: 2.47,
                    REILLY_OPELKA: 1.56
                }
            },
            {
                'round': 128,
                'players': [
                    MAXIMILIAN_MARTERER,
                    UGO_HUMBERT
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MAXIMILIAN_MARTERER: 2.55,
                    UGO_HUMBERT: 1.50
                }
            },
            {
                'round': 128,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.66,
                    PIERRE_HUGUES_HERBERT: 2.20
                }
            },
            {
                'round': 128,
                'players': [
                    MARTIN_KLIZAN,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    MARTIN_KLIZAN: 1.50,
                    MISCHA_ZVEREV: 2.58
                }
            },
            {
                'round': 128,
                'players': [
                    IVO_KARLOVIC,
                    MATTHEW_EBDEN
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    IVO_KARLOVIC: 1.80,
                    MATTHEW_EBDEN: 2.00
                }
            },
            {
                'round': 128,
                'players': [
                    MALEK_JAZIRI,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MALEK_JAZIRI: 1.71,
                    BRADLEY_KLAHN: 2.18
                }
            },
            {
                'round': 128,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    BENOIT_PAIRE
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 2.53,
                    BENOIT_PAIRE: 1.56
                }
            },
            {
                'round': 128,
                'players': [
                    MARCOS_GIRON,
                    JEREMY_CHARDY
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    MARCOS_GIRON: 3.09,
                    JEREMY_CHARDY: 1.36
                }
            },
            {
                'round': 128,
                'players': [
                    BJORN_FRATANGELO,
                    ELIAS_YMER
                ],
                'score': [(4, 6), (6, 2), (6, 2)],
                'odds': {
                    BJORN_FRATANGELO: 1.69,
                    ELIAS_YMER: 2.20
                }
            },
            {
                'round': 128,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    CAMERON_NORRIE
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.25,
                    CAMERON_NORRIE: 1.67
                }
            },
            {
                'round': 128,
                'players': [
                    GUIDO_ANDREOZZI,
                    ILYA_IVASHKA
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    GUIDO_ANDREOZZI: 3.42,
                    ILYA_IVASHKA: 1.31
                }
            },

            # 2019-03-08
            {
                'round': 128,
                'players': [
                    STAN_WAWRINKA,
                    DANIEL_EVANS
                ],
                'score': [(6, 7), (6, 3), (6, 3)],
                'odds': {
                    STAN_WAWRINKA: 1.48,
                    DANIEL_EVANS: 2.71
                }
            },
            {
                'round': 128,
                'players': [
                    ALEXEI_POPYRIN,
                    JAUME_MUNAR
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALEXEI_POPYRIN: 1.91,
                    JAUME_MUNAR: 1.83
                }
            },
            {
                'round': 128,
                'players': [
                    MACKENZIE_MCDONALD,
                    JOAO_SOUSA
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    MACKENZIE_MCDONALD: 1.75,
                    JOAO_SOUSA: 2.05
                }
            },
            {
                'round': 128,
                'players': [
                    ADRIAN_MANNARINO,
                    TENNYS_SANDGREN
                ],
                'score': [(6, 2), (6, 7), (6, 1)],
                'odds': {
                    ADRIAN_MANNARINO: 1.80,
                    TENNYS_SANDGREN: 1.98
                }
            },
            {
                'round': 128,
                'players': [
                    FELICIANO_LOPEZ,
                    TOMAS_BERDYCH
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    FELICIANO_LOPEZ: 5.15,
                    TOMAS_BERDYCH: 1.17
                }
            },
            {
                'round': 128,
                'players': [
                    DUSAN_LAJOVIC,
                    TARO_DANIEL
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    DUSAN_LAJOVIC: 1.60,
                    TARO_DANIEL: 2.37
                }
            },
            {
                'round': 128,
                'players': [
                    FILIP_KRAJINOVIC,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.63,
                    MIKHAIL_KUKUSHKIN: 2.30
                }
            },
            {
                'round': 128,
                'players': [
                    STEVE_JOHNSON,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    STEVE_JOHNSON: 2.05,
                    TAYLOR_FRITZ: 1.74
                }
            },
            {
                'round': 128,
                'players': [
                    NICOLAS_JARRY,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 4), (4, 6), (7, 5)],
                'odds': {
                    NICOLAS_JARRY: 3.03,
                    FRANCES_TIAFOE: 1.41
                }
            },
            {
                'round': 128,
                'players': [
                    HUBERT_HURKACZ,
                    DONALD_YOUNG
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 1.45,
                    DONALD_YOUNG: 2.69
                }
            },
            {
                'round': 128,
                'players': [
                    ROBIN_HAASE,
                    DENIS_ISTOMIN
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    ROBIN_HAASE: 2.24,
                    DENIS_ISTOMIN: 1.67
                }
            },
            {
                'round': 128,
                'players': [
                    PETER_GOJOWCZYK,
                    ANDREAS_SEPPI
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    PETER_GOJOWCZYK: 2.55,
                    ANDREAS_SEPPI: 1.50
                }
            },
            {
                'round': 128,
                'players': [
                    JARED_DONALDSON,
                    TATSUMA_ITO
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    JARED_DONALDSON: 1.63,
                    TATSUMA_ITO: 2.16
                }
            },
            {
                'round': 128,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    RYAN_HARRISON
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 3.55,
                    RYAN_HARRISON: 1.31
                }
            },
            {
                'round': 128,
                'players': [
                    ALEX_BOLT,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 3), (5, 7), (6, 2)],
                'odds': {
                    ALEX_BOLT: 2.34,
                    ERNESTS_GULBIS: 1.63
                }
            },
            {
                'round': 128,
                'players': [
                    RADU_ALBOT,
                    MARIUS_COPIL
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    RADU_ALBOT: 1.43,
                    MARIUS_COPIL: 2.80
                }
            },

            # 2019-03-09
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    RICARDAS_BERANKIS
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.58,
                    RICARDAS_BERANKIS: 2.40
                }
            },
            {
                'round': 64,
                'players': [
                    MIOMIR_KECMANOVIC,
                    MAXIMILIAN_MARTERER
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.65,
                    MAXIMILIAN_MARTERER: 1.65
                }
            },
            {
                'round': 64,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    NICK_KYRGIOS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 2.48,
                    NICK_KYRGIOS: 1.57
                }
            },
            {
                'round': 64,
                'players': [
                    LASLO_DJERE,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    LASLO_DJERE: 1.51,
                    GUIDO_ANDREOZZI: 2.62
                }
            },
            {
                'round': 64,
                'players': [
                    GILLES_SIMON,
                    MALEK_JAZIRI
                ],
                'score': [(6, 3), (6, 7), (6, 4)],
                'odds': {
                    GILLES_SIMON: 1.27,
                    MALEK_JAZIRI: 3.81
                }
            },
            {
                'round': 64,
                'players': [
                    MARCOS_GIRON,
                    ALEX_DE_MINAUR
                ],
                'score': [(1, 6), (6, 4), (6, 2)],
                'odds': {
                    MARCOS_GIRON: 4.11,
                    ALEX_DE_MINAUR: 1.23
                }
            },
            {
                'round': 64,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 3.52,
                    ROBERTO_BAUTISTA_AGUT: 1.30
                }
            },
            {
                'round': 64,
                'players': [
                    GAEL_MONFILS,
                    LEONARDO_MAYER
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    GAEL_MONFILS: 1.22,
                    LEONARDO_MAYER: 4.23
                }
            },
            {
                'round': 64,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 3.70,
                    NIKOLOZ_BASILASHVILI: 1.29
                }
            },
            {
                'round': 64,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.79,
                    MARCO_CECCHINATO: 1.95
                }
            },
            {
                'round': 64,
                'players': [
                    MILOS_RAONIC,
                    SAM_QUERREY
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    MILOS_RAONIC: 1.45,
                    SAM_QUERREY: 2.71
                }
            },
            {
                'round': 64,
                'players': [
                    IVO_KARLOVIC,
                    BORNA_CORIC
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    IVO_KARLOVIC: 3.11,
                    BORNA_CORIC: 1.38
                }
            },
            {
                'round': 64,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.99,
                    STEFANOS_TSITSIPAS: 1.41
                }
            },
            {
                'round': 64,
                'players': [
                    DOMINIC_THIEM,
                    JORDAN_THOMPSON
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    DOMINIC_THIEM: 1.30,
                    JORDAN_THOMPSON: 3.50
                }
            },
            {
                'round': 64,
                'players': [
                    ALEXANDER_ZVEREV,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 3), (2, 0)],
                'retired': True,
                'odds': {
                    ALEXANDER_ZVEREV: 1.13,
                    MARTIN_KLIZAN: 6.25
                }
            },
            {
                'round': 64,
                'players': [
                    NOVAK_DJOKOVIC,
                    BJORN_FRATANGELO
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.02,
                    BJORN_FRATANGELO: 17.28
                }
            },

            # 2019-03-10
            {
                'round': 64,
                'players': [
                    ANDREY_RUBLEV,
                    ROBIN_HAASE
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 1.59,
                    ROBIN_HAASE: 2.32
                }
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    ALEX_BOLT
                ],
                'score': [(7, 6), (2, 6), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 1.43,
                    ALEX_BOLT: 2.80
                }
            },
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 4), (6, 7), (7, 5)],
                'odds': {
                    STAN_WAWRINKA: 1.42,
                    MARTON_FUCSOVICS: 2.90
                }
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    LUCAS_POUILLE
                ],
                'score': [(6, 2), (3, 6), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 1.89,
                    LUCAS_POUILLE: 1.86
                }
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.30,
                    ROBERTO_CARBALLES_BAENA: 3.70
                }
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    STEVE_JOHNSON
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.69,
                    STEVE_JOHNSON: 2.18
                }
            },
            {
                'round': 64,
                'players': [
                    KYLE_EDMUND,
                    NICOLAS_JARRY
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    KYLE_EDMUND: 1.31,
                    NICOLAS_JARRY: 3.59
                }
            },
            {
                'round': 64,
                'players': [
                    FILIP_KRAJINOVIC,
                    DAVID_GOFFIN
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    FILIP_KRAJINOVIC: 2.53,
                    DAVID_GOFFIN: 1.54
                }
            },
            {
                'round': 64,
                'players': [
                    RADU_ALBOT,
                    FABIO_FOGNINI
                ],
                'score': [(6, 0), (7, 6)],
                'odds': {
                    RADU_ALBOT: 1.83,
                    FABIO_FOGNINI: 1.96
                }
            },
            {
                'round': 64,
                'players': [
                    DANILL_MEDVEDEV,
                    MACKENZIE_MCDONALD
                ],
                'score': [(7, 5), (6, 0)],
                'odds': {
                    DANILL_MEDVEDEV: 1.23,
                    MACKENZIE_MCDONALD: 4.13
                }
            },
            {
                'round': 64,
                'players': [
                    KAREN_KHACHANOV,
                    FELICIANO_LOPEZ
                ],
                'score': [(6, 3), (1, 6), (6, 4)],
                'odds': {
                    KAREN_KHACHANOV: 1.31,
                    FELICIANO_LOPEZ: 3.43
                }
            },
            {
                'round': 64,
                'players': [
                    MARIN_CILIC,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MARIN_CILIC: 1.18,
                    DUSAN_LAJOVIC: 5.16
                }
            },
            {
                'round': 64,
                'players': [
                    JOHN_ISNER,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 0), (6, 2)],
                'odds': {
                    JOHN_ISNER: 1.20,
                    ALEXEI_POPYRIN: 4.65
                }
            },
            {
                'round': 64,
                'players': [
                    KEI_NISHIKORI,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    KEI_NISHIKORI: 1.20,
                    ADRIAN_MANNARINO: 4.44
                }
            },
            {
                'round': 64,
                'players': [
                    ROGER_FEDERER,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    ROGER_FEDERER: 1.05,
                    PETER_GOJOWCZYK: 10.47
                }
            },
            {
                'round': 64,
                'players': [
                    RAFAEL_NADAL,
                    JARED_DONALDSON
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.03,
                    JARED_DONALDSON: 13.80
                }
            },

            # 2019-03-11
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 7), (6, 4), (7, 6)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.29,
                    FELIX_AUGER_ALIASSIME: 1.64
                }
            },
            {
                'round': 32,
                'players': [
                    IVO_KARLOVIC,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    IVO_KARLOVIC: 1.63,
                    PRAJNESH_GUNNESWARAN: 2.33
                }
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    LASLO_DJERE
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.71,
                    LASLO_DJERE: 2.14
                }
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    GAEL_MONFILS: 1.13,
                    ALBERT_RAMOS_VINOLAS: 6.40
                }
            },
            {
                'round': 32,
                'players': [
                    MILOS_RAONIC,
                    MARCOS_GIRON
                ],
                'score': [(4, 6), (6, 4), (6, 4)],
                'odds': {
                    MILOS_RAONIC: 1.12,
                    MARCOS_GIRON: 6.45
                }
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    GILLES_SIMON
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DOMINIC_THIEM: 1.40,
                    GILLES_SIMON: 3.03
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    ALEXANDER_ZVEREV
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    JAN_LENNARD_STRUFF: 4.75,
                    ALEXANDER_ZVEREV: 1.18
                }
            },

            # 2019-03-12
            {
                'round': 32,
                'players': [
                    KYLE_EDMUND,
                    RADU_ALBOT
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    KYLE_EDMUND: 1.33,
                    RADU_ALBOT: 3.35
                }
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    DANILL_MEDVEDEV
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    FILIP_KRAJINOVIC: 3.35,
                    DANILL_MEDVEDEV: 1.34
                }
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    ANDREY_RUBLEV
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 1.54,
                    ANDREY_RUBLEV: 2.50
                }
            },
            {
                'round': 32,
                'players': [
                    DENIS_SHAPOVALOV,
                    MARIN_CILIC
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 2.41,
                    MARIN_CILIC: 1.61
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_ISNER,
                    GUIDO_PELLA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JOHN_ISNER: 1.26,
                    GUIDO_PELLA: 4.00
                }
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    KEI_NISHIKORI
                ],
                'score': [(4, 6), (6, 4), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 3.52,
                    KEI_NISHIKORI: 1.32
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    STAN_WAWRINKA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.27,
                    STAN_WAWRINKA: 3.96
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.08,
                    DIEGO_SCHWARTZMAN: 8.23
                }
            },
            {
                'round': 32,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    NOVAK_DJOKOVIC
                ],
                'score': [(6, 4), (6, 4)],
                # no odds
            },

            # 2019-03-13
            {
                'round': 16,
                'players': [
                    MIOMIR_KECMANOVIC,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 4), (0, 0)],
                'retired': True,
                'odds': {
                    MIOMIR_KECMANOVIC: 2.28,
                    YOSHIHITO_NISHIOKA: 1.60
                }
            },
            {
                'round': 16,
                'players': [
                    HUBERT_HURKACZ,
                    DENIS_SHAPOVALOV
                ],
                'score': [(7, 6), (2, 6), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 3.07,
                    DENIS_SHAPOVALOV: 1.39
                }
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 0), (6, 2)],
                'odds': {
                    GAEL_MONFILS: 1.36,
                    PHILIPP_KOHLSCHREIBER: 3.05
                }
            },
            {
                'round': 16,
                'players': [
                    MILOS_RAONIC,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    MILOS_RAONIC: 1.39,
                    JAN_LENNARD_STRUFF: 3.18
                }
            },
            {
                'round': 16,
                'players': [
                    KAREN_KHACHANOV,
                    JOHN_ISNER
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    KAREN_KHACHANOV: 2.25,
                    JOHN_ISNER: 1.66
                }
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    IVO_KARLOVIC
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    DOMINIC_THIEM: 1.34,
                    IVO_KARLOVIC: 3.37
                }
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    KYLE_EDMUND
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.22,
                    KYLE_EDMUND: 4.51
                }
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    FILIP_KRAJINOVIC
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.08,
                    FILIP_KRAJINOVIC: 8.69
                }
            },

            # 2019-03-14
            {
                'round': 8,
                'players': [
                    MILOS_RAONIC,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MILOS_RAONIC: 1.18,
                    MIOMIR_KECMANOVIC: 5.00
                }
            },
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    GAEL_MONFILS
                ],
                'score': [],
                'wo': True,
                'odds': {
                    DOMINIC_THIEM: 2.20,
                    GAEL_MONFILS: 1.65
                }
            },

            # 2019-03-15
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.08,
                    HUBERT_HURKACZ: 8.06
                }
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    KAREN_KHACHANOV
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    RAFAEL_NADAL: 1.16,
                    KAREN_KHACHANOV: 5.31
                }
            },

            # 2019-03-16
            {
                'round': 4,
                'players': [
                    DOMINIC_THIEM,
                    MILOS_RAONIC
                ],
                'score': [(7, 6), (6, 7), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 2.35,
                    MILOS_RAONIC: 1.61
                }
            },
            {
                'round': 4,
                'players': [
                    ROGER_FEDERER,
                    RAFAEL_NADAL
                ],
                'score': [],
                'wo': True,
                'odds': {
                    ROGER_FEDERER: 1.44,
                    RAFAEL_NADAL: 2.80
                }
            },

            # 2019-03-17
            {
                'round': 2,
                'players': [
                    DOMINIC_THIEM,
                    ROGER_FEDERER
                ],
                'score': [(3, 6), (6, 3), (7, 5)],
                'odds': {
                    DOMINIC_THIEM: 4.06,
                    ROGER_FEDERER: 1.26
                }
            }
        ]
    },

    {
        'name': 'Miami Open presented by Itau',
        'category': 'ATP1000',
        'date': '2019-03-31',
        'location': 'Miami, United States',
        'matches': [

            # 2019-03-18
            {
                'round': 512,
                'players': [
                    EVGENY_DONSKOY,
                    ALEX_BOLT
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    EVGENY_DONSKOY: 2.30,
                    ALEX_BOLT: 1.49
                }
            },
            {
                'round': 512,
                'players': [
                    THIAGO_MONTEIRO,
                    KAMIL_MAJCHRZAK
                ],
                'score': [(2, 6), (7, 6), (6, 2)],
                'odds': {
                    THIAGO_MONTEIRO: 2.55,
                    KAMIL_MAJCHRZAK: 1.45
                }
            },
            {
                'round': 512,
                'players': [
                    JO_WILFRIED_TSONGA,
                    LUKAS_ROSOL
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.10,
                    LUKAS_ROSOL: 6.25
                }
            },
            {
                'round': 512,
                'players': [
                    MITCHELL_KRUEGER,
                    ELIAS_YMER
                ],
                'score': [(6, 7), (6, 0), (6, 4)],
                'odds': {
                    MITCHELL_KRUEGER: 2.50,
                    ELIAS_YMER: 1.46
                }
            },
            {
                'round': 512,
                'players': [
                    JAY_CLARKE,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    JAY_CLARKE: 1.91,
                    JOZEF_KOVALIK: 1.77
                }
            },
            {
                'round': 512,
                'players': [
                    MARCEL_GRANOLLERS,
                    ZANE_KHAN
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.09,
                    ZANE_KHAN: 6.25
                }
            },
            {
                'round': 512,
                'players': [
                    LORENZO_SONEGO,
                    RAMKUMAR_RAMANATHAN
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    LORENZO_SONEGO: 1.25,
                    RAMKUMAR_RAMANATHAN: 3.51
                }
            },
            {
                'round': 512,
                'players': [
                    PAOLO_LORENZI,
                    RUBEN_BEMELMANS
                ],
                'score': [(7, 5), (3, 6), (7, 6)],
                'odds': {
                    PAOLO_LORENZI: 1.67,
                    RUBEN_BEMELMANS: 2.05
                }
            },
            {
                'round': 512,
                'players': [
                    MIKAEL_YMER,
                    RYAN_HARRISON
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    MIKAEL_YMER: 3.10,
                    RYAN_HARRISON: 1.32
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREY_RUBLEV,
                    JARED_DONALDSON
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 4.50,
                    JARED_DONALDSON: 1.19
                }
            },
            {
                'round': 512,
                'players': [
                    DENIS_ISTOMIN,
                    DARIAN_KING
                ],
                'score': [(6, 4), (3, 6), (7, 6)],
                'odds': {
                    DENIS_ISTOMIN: 1.59,
                    DARIAN_KING: 2.25
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_EVANS,
                    TATSUMA_ITO
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    DANIEL_EVANS: 1.25,
                    TATSUMA_ITO: 3.80
                }
            },
            {
                'round': 512,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    ADRIAN_MENENDEZ_MACEIRAS
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 1.32,
                    ADRIAN_MENENDEZ_MACEIRAS: 3.30
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXANDER_BUBLIK,
                    RICARDAS_BERANKIS
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.15,
                    RICARDAS_BERANKIS: 1.65
                }
            },
            {
                'round': 512,
                'players': [
                    CASPER_RUUD,
                    JASON_JUNG
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    CASPER_RUUD: 1.33,
                    JASON_JUNG: 3.00
                }
            },
            {
                'round': 512,
                'players': [
                    LLOYD_HARRIS,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    LLOYD_HARRIS: 1.37,
                    ALEXEI_POPYRIN: 2.67
                }
            },
            {
                'round': 512,
                'players': [
                    NOAH_RUBIN,
                    HUGO_DELLIEN
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    NOAH_RUBIN: 1.24,
                    HUGO_DELLIEN: 3.75
                }
            },
            {
                'round': 512,
                'players': [
                    PABLO_CUEVAS,
                    EGOR_GERASIMOV
                ],
                'score': [(2, 6), (6, 4), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 1.53,
                    EGOR_GERASIMOV: 2.20
                }
            },
            {
                'round': 512,
                'players': [
                    BJORN_FRATANGELO,
                    CRISTIAN_GARIN
                ],
                'score': [(4, 6), (7, 6), (6, 1)],
                'odds': {
                    BJORN_FRATANGELO: 1.51,
                    CRISTIAN_GARIN: 2.45
                }
            },
            {
                'round': 512,
                'players': [
                    LUKAS_LACKO,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    LUKAS_LACKO: 1.47,
                    JUAN_IGNACIO_LONDERO: 2.53
                }
            },
            {
                'round': 512,
                'players': [
                    MACKENZIE_MCDONALD,
                    PETER_POLANSKY
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    MACKENZIE_MCDONALD: 1.19,
                    PETER_POLANSKY: 4.50
                }
            },
            {
                'round': 512,
                'players': [
                    REILLY_OPELKA,
                    HENRI_LAAKSONEN
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 1.31,
                    HENRI_LAAKSONEN: 3.35
                }
            },
            {
                'round': 512,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    LUCA_VANNI
                ],
                'score': [(4, 6), (6, 4), (6, 1)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.17,
                    LUCA_VANNI: 4.00
                }
            },
            {
                'round': 512,
                'players': [
                    RADU_ALBOT,
                    GIANLUIGI_QUINZI
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    RADU_ALBOT: 1.17,
                    GIANLUIGI_QUINZI: 4.50
                }
            },

            # 2019-03-20
            {
                'round': 256,
                'players': [
                    MIKAEL_YMER,
                    NOAH_RUBIN
                ],
                'score': [(6, 4), (5, 7), (6, 2)],
                'odds': {
                    MIKAEL_YMER: 1.67,
                    NOAH_RUBIN: 2.00
                }
            },
            {
                'round': 256,
                'players': [
                    ANDREY_RUBLEV,
                    BJORN_FRATANGELO
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 1.37,
                    BJORN_FRATANGELO: 2.75
                }
            },
            {
                'round': 256,
                'players': [
                    LUKAS_LACKO,
                    DENIS_ISTOMIN
                ],
                'score': [],
                'wo': True,
                'odds': {
                    LUKAS_LACKO: 2.40,
                    DENIS_ISTOMIN: 1.54
                }
            },
            {
                'round': 256,
                'players': [
                    ALEXANDER_BUBLIK,
                    DANIEL_EVANS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.90,
                    DANIEL_EVANS: 1.36
                }
            },
            {
                'round': 256,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    JAY_CLARKE
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 1.32,
                    JAY_CLARKE: 3.30
                }
            },
            {
                'round': 256,
                'players': [
                    CASPER_RUUD,
                    EVGENY_DONSKOY
                ],
                'score': [(6, 7), (6, 2), (6, 2)],
                'odds': {
                    CASPER_RUUD: 1.61,
                    EVGENY_DONSKOY: 2.15
                }
            },
            {
                'round': 256,
                'players': [
                    THIAGO_MONTEIRO,
                    LLOYD_HARRIS
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    THIAGO_MONTEIRO: 2.75,
                    LLOYD_HARRIS: 1.41
                }
            },
            {
                'round': 256,
                'players': [
                    PABLO_CUEVAS,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    PABLO_CUEVAS: 3.75,
                    JO_WILFRIED_TSONGA: 1.25
                }
            },
            {
                'round': 256,
                'players': [
                    LORENZO_SONEGO,
                    MACKENZIE_MCDONALD
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 2.20,
                    MACKENZIE_MCDONALD: 1.61
                }
            },
            {
                'round': 256,
                'players': [
                    REILLY_OPELKA,
                    MARCEL_GRANOLLERS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 1.43,
                    MARCEL_GRANOLLERS: 2.61
                }
            },
            {
                'round': 256,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    PAOLO_LORENZI
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.18,
                    PAOLO_LORENZI: 4.75
                }
            },
            {
                'round': 256,
                'players': [
                    RADU_ALBOT,
                    MITCHELL_KRUEGER
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    RADU_ALBOT: 1.14,
                    MITCHELL_KRUEGER: 5.00
                }
            },
            {
                'round': 128,
                'players': [
                    MISCHA_ZVEREV,
                    NICOLA_KUHN
                ],
                'score': [(4, 6), (7, 5), (2, 2)],
                'retired': True,
                'odds': {
                    MISCHA_ZVEREV: 2.02,
                    NICOLA_KUHN: 1.80
                }
            },
            {
                'round': 128,
                'players': [
                    JANKO_TIPSAREVIC,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    JANKO_TIPSAREVIC: 2.20,
                    BRADLEY_KLAHN: 1.69
                }
            },
            {
                'round': 128,
                'players': [
                    HUBERT_HURKACZ,
                    MATTEO_BERRETTINI
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 2.05,
                    MATTEO_BERRETTINI: 1.77
                }
            },
            {
                'round': 128,
                'players': [
                    FEDERICO_DELBONIS,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    FEDERICO_DELBONIS: 2.15,
                    PETER_GOJOWCZYK: 1.67
                }
            },
            {
                'round': 128,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    DENIS_KUDLA
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 2.32,
                    DENIS_KUDLA: 1.65
                }
            },
            {
                'round': 128,
                'players': [
                    GUIDO_ANDREOZZI,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    GUIDO_ANDREOZZI: 4.38,
                    MIKHAIL_KUKUSHKIN: 1.22
                }
            },

            # 2019-03-21
            {
                'round': 128,
                'players': [
                    BERNARD_TOMIC,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    BERNARD_TOMIC: 1.74,
                    THIAGO_MONTEIRO: 2.01
                }
            },
            {
                'round': 128,
                'players': [
                    JORDAN_THOMPSON,
                    CAMERON_NORRIE
                ],
                'score': [(4, 6), (7, 6), (6, 3)],
                'odds': {
                    JORDAN_THOMPSON: 2.64,
                    CAMERON_NORRIE: 1.48
                }
            },
            {
                'round': 128,
                'players': [
                    JOAO_SOUSA,
                    CHUN_HSIN_TSENG
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    JOAO_SOUSA: 1.24,
                    CHUN_HSIN_TSENG: 3.90
                }
            },
            {
                'round': 128,
                'players': [
                    LORENZO_SONEGO,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    LORENZO_SONEGO: 1.49,
                    MARTIN_KLIZAN: 2.58
                }
            },
            {
                'round': 128,
                'players': [
                    ANDREY_RUBLEV,
                    TARO_DANIEL
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 1.24,
                    TARO_DANIEL: 3.75
                }
            },
            {
                'round': 128,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    MARIUS_COPIL
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.67,
                    MARIUS_COPIL: 2.20
                }
            },
            {
                'round': 128,
                'players': [
                    REILLY_OPELKA,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    REILLY_OPELKA: 2.01,
                    JAN_LENNARD_STRUFF: 1.77
                }
            },
            {
                'round': 128,
                'players': [
                    JAUME_MUNAR,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JAUME_MUNAR: 1.83,
                    PRAJNESH_GUNNESWARAN: 1.88
                }
            },
            {
                'round': 128,
                'players': [
                    MACKENZIE_MCDONALD,
                    UGO_HUMBERT
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    MACKENZIE_MCDONALD: 1.74,
                    UGO_HUMBERT: 2.04
                }
            },
            {
                'round': 128,
                'players': [
                    LEONARDO_MAYER,
                    MIKAEL_YMER
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    LEONARDO_MAYER: 1.48,
                    MIKAEL_YMER: 2.55
                }
            },
            {
                'round': 128,
                'players': [
                    MAXIMILIAN_MARTERER,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    MAXIMILIAN_MARTERER: 2.35,
                    TAYLOR_FRITZ: 1.56
                }
            },
            {
                'round': 128,
                'players': [
                    ADRIAN_MANNARINO,
                    ALJAZ_BEDENE
                ],
                'score': [(4, 6), (6, 4), (6, 2)],
                'odds': {
                    ADRIAN_MANNARINO: 1.42,
                    ALJAZ_BEDENE: 2.70
                }
            },
            {
                'round': 128,
                'players': [
                    FELICIANO_LOPEZ,
                    BENOIT_PAIRE
                ],
                'score': [(7, 5), (4, 6), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 1.91,
                    BENOIT_PAIRE: 1.74
                }
            },
            {
                'round': 128,
                'players': [
                    DUSAN_LAJOVIC,
                    PABLO_CUEVAS
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 2.84,
                    PABLO_CUEVAS: 1.42
                }
            },
            {
                'round': 128,
                'players': [
                    FILIP_KRAJINOVIC,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.44,
                    PIERRE_HUGUES_HERBERT: 2.60
                }
            },
            {
                'round': 128,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.54,
                    ERNESTS_GULBIS: 2.50
                }
            },
            {
                'round': 128,
                'players': [
                    ILYA_IVASHKA,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 4), (1, 6), (6, 3)],
                # no odds
            },
            {
                'round': 128,
                'players': [
                    ROBIN_HAASE,
                    LUKAS_LACKO
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ROBIN_HAASE: 1.49,
                    LUKAS_LACKO: 2.65
                }
            },
            {
                'round': 128,
                'players': [
                    DAVID_FERRER,
                    SAM_QUERREY
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    DAVID_FERRER: 2.30,
                    SAM_QUERREY: 1.63
                }
            },
            {
                'round': 128,
                'players': [
                    DANIEL_EVANS,
                    MALEK_JAZIRI
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    DANIEL_EVANS: 1.42,
                    MALEK_JAZIRI: 2.80
                }
            },
            {
                'round': 128,
                'players': [
                    DAMIR_DZUMHUR,
                    CHRISTOPHER_EUBANKS
                ],
                'score': [(1, 6), (6, 4), (7, 6)],
                'odds': {
                    DAMIR_DZUMHUR: 1.74,
                    CHRISTOPHER_EUBANKS: 2.05
                }
            },
            {
                'round': 128,
                'players': [
                    JEREMY_CHARDY,
                    NICOLAS_JARRY
                ],
                'score': [(6, 7), (6, 2), (7, 6)],
                'odds': {
                    JEREMY_CHARDY: 1.61,
                    NICOLAS_JARRY: 2.43
                }
            },
            {
                'round': 128,
                'players': [
                    ALEXANDER_BUBLIK,
                    TENNYS_SANDGREN
                ],
                'score': [(5, 7), (6, 4), (7, 6)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.69,
                    TENNYS_SANDGREN: 2.03
                }
            },
            {
                'round': 128,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    CASPER_RUUD
                ],
                'score': [(3, 6), (6, 1), (6, 2)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.47,
                    CASPER_RUUD: 2.61
                }
            },
            {
                'round': 128,
                'players': [
                    PABLO_ANDUJAR,
                    IVO_KARLOVIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PABLO_ANDUJAR: 3.74,
                    IVO_KARLOVIC: 1.28
                }
            },
            {
                'round': 128,
                'players': [
                    RADU_ALBOT,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 0), (3, 2)],
                'retired': True,
                'odds': {
                    RADU_ALBOT: 1.30,
                    MATTHEW_EBDEN: 3.30
                }
            },

            # 2019-03-22
            {
                'round': 64,
                'players': [
                    ROBIN_HAASE,
                    LLOYD_HARRIS
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    ROBIN_HAASE: 1.64,
                    LLOYD_HARRIS: 2.39
                }
            },
            {
                'round': 64,
                'players': [
                    FEDERICO_DELBONIS,
                    JOHN_MILLMAN
                ],
                'score': [(7, 5), (3, 6), (7, 6)],
                'odds': {
                    FEDERICO_DELBONIS: 2.50,
                    JOHN_MILLMAN: 1.54
                }
            },
            {
                'round': 64,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 4), (4, 6), (6, 0)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.96,
                    MARTON_FUCSOVICS: 1.80
                }
            },
            {
                'round': 64,
                'players': [
                    NICK_KYRGIOS,
                    ALEXANDER_BUBLIK
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    NICK_KYRGIOS: 1.29,
                    ALEXANDER_BUBLIK: 3.65
                }
            },
            {
                'round': 64,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    LUCAS_POUILLE
                ],
                'score': [(4, 6), (6, 4), (6, 3)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.37,
                    LUCAS_POUILLE: 1.61
                }
            },
            {
                'round': 64,
                'players': [
                    JEREMY_CHARDY,
                    GILLES_SIMON
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JEREMY_CHARDY: 2.20,
                    GILLES_SIMON: 1.69
                }
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    JANKO_TIPSAREVIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.19,
                    JANKO_TIPSAREVIC: 4.97
                }
            },
            {
                'round': 64,
                'players': [
                    KYLE_EDMUND,
                    ILYA_IVASHKA
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    KYLE_EDMUND: 1.20,
                    ILYA_IVASHKA: 4.51
                }
            },
            {
                'round': 64,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.26,
                    MISCHA_ZVEREV: 3.70
                }
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    GUIDO_ANDREOZZI
                ],
                'score': [(5, 7), (6, 4), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.45,
                    GUIDO_ANDREOZZI: 2.70
                }
            },
            {
                'round': 64,
                'players': [
                    MILOS_RAONIC,
                    MAXIMILIAN_MARTERER
                ],
                'score': [],
                'wo': True,
                'odds': {
                    MILOS_RAONIC: 1.20,
                    MAXIMILIAN_MARTERER: 4.84
                }
            },
            {
                'round': 64,
                'players': [
                    BORNA_CORIC,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(7, 6), (0, 6), (6, 2)],
                'odds': {
                    BORNA_CORIC: 1.22,
                    ROBERTO_CARBALLES_BAENA: 4.67
                }
            },
            {
                'round': 64,
                'players': [
                    JOHN_ISNER,
                    LORENZO_SONEGO
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.26,
                    LORENZO_SONEGO: 3.96
                }
            },
            {
                'round': 64,
                'players': [
                    DUSAN_LAJOVIC,
                    KEI_NISHIKORI
                ],
                'score': [(2, 6), (6, 2), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 5.50,
                    KEI_NISHIKORI: 1.16
                }
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    DOMINIC_THIEM
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 3.14,
                    DOMINIC_THIEM: 1.35
                }
            },
            {
                'round': 64,
                'players': [
                    NOVAK_DJOKOVIC,
                    BERNARD_TOMIC
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.03,
                    BERNARD_TOMIC: 12.75
                }
            },

            # 2019-03-23
            {
                'round': 64,
                'players': [
                    JOAO_SOUSA,
                    STEVE_JOHNSON
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 2.32,
                    STEVE_JOHNSON: 1.63
                }
            },
            {
                'round': 64,
                'players': [
                    FILIP_KRAJINOVIC,
                    STAN_WAWRINKA
                ],
                'score': [(5, 7), (6, 2), (7, 6)],
                'odds': {
                    FILIP_KRAJINOVIC: 2.27,
                    STAN_WAWRINKA: 1.65
                }
            },
            {
                'round': 64,
                'players': [
                    FRANCES_TIAFOE,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    FRANCES_TIAFOE: 1.87,
                    MIOMIR_KECMANOVIC: 1.93
                }
            },
            {
                'round': 64,
                'players': [
                    LEONARDO_MAYER,
                    GUIDO_PELLA
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    LEONARDO_MAYER: 2.05,
                    GUIDO_PELLA: 1.74
                }
            },
            {
                'round': 64,
                'players': [
                    GRIGOR_DIMITROV,
                    FELICIANO_LOPEZ
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    GRIGOR_DIMITROV: 1.48,
                    FELICIANO_LOPEZ: 2.50
                }
            },
            {
                'round': 64,
                'players': [
                    REILLY_OPELKA,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 4), (3, 6), (6, 4)],
                'odds': {
                    REILLY_OPELKA: 2.05,
                    DIEGO_SCHWARTZMAN: 1.74
                }
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    DANIEL_EVANS
                ],
                'score': [(4, 6), (6, 1), (6, 3)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.54,
                    DANIEL_EVANS: 2.55
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    PABLO_ANDUJAR
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    DAVID_GOFFIN: 1.13,
                    PABLO_ANDUJAR: 6.12
                }
            },
            {
                'round': 64,
                'players': [
                    MARCO_CECCHINATO,
                    DAMIR_DZUMHUR
                ],
                'score': [],
                'wo': True,
                'odds': {
                    MARCO_CECCHINATO: 1.71,
                    DAMIR_DZUMHUR: 2.17
                }
            },
            {
                'round': 64,
                'players': [
                    DANILL_MEDVEDEV,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    DANILL_MEDVEDEV: 1.31,
                    ADRIAN_MANNARINO: 3.49
                }
            },
            {
                'round': 64,
                'players': [
                    JORDAN_THOMPSON,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    JORDAN_THOMPSON: 4.25,
                    KAREN_KHACHANOV: 1.24
                }
            },
            {
                'round': 64,
                'players': [
                    ANDREY_RUBLEV,
                    MARIN_CILIC
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 2.47,
                    MARIN_CILIC: 1.58
                }
            },
            {
                'round': 64,
                'players': [
                    STEFANOS_TSITSIPAS,
                    MACKENZIE_MCDONALD
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.28,
                    MACKENZIE_MCDONALD: 3.89
                }
            },
            {
                'round': 64,
                'players': [
                    KEVIN_ANDERSON,
                    JAUME_MUNAR
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    KEVIN_ANDERSON: 1.50,
                    JAUME_MUNAR: 2.48
                }
            },
            {
                'round': 64,
                'players': [
                    ROGER_FEDERER,
                    RADU_ALBOT
                ],
                'score': [(4, 6), (7, 5), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.10,
                    RADU_ALBOT: 6.75
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_FERRER,
                    ALEXANDER_ZVEREV
                ],
                'score': [(2, 6), (7, 5), (6, 3)],
                'odds': {
                    DAVID_FERRER: 4.33,
                    ALEXANDER_ZVEREV: 1.24
                }
            },

            # 2019-03-24
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    HUBERT_HURKACZ
                ],
                'score': [(7, 6), 6, 4],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.05,
                    HUBERT_HURKACZ: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    NICK_KYRGIOS,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    NICK_KYRGIOS: 1.30,
                    DUSAN_LAJOVIC: 3.62
                }
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    ROBIN_HAASE
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.51,
                    ROBIN_HAASE: 2.58
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    FABIO_FOGNINI
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.38,
                    FABIO_FOGNINI: 2.95
                }
            },
            {
                'round': 32,
                'players': [
                    KYLE_EDMUND,
                    MILOS_RAONIC
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    KYLE_EDMUND: 2.30,
                    MILOS_RAONIC: 1.61
                }
            },
            {
                'round': 32,
                'players': [
                    BORNA_CORIC,
                    JEREMY_CHARDY
                ],
                'score': [(6, 7), (6, 2), (6, 3)],
                'odds': {
                    BORNA_CORIC: 1.45,
                    JEREMY_CHARDY: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_ISNER,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.21,
                    ALBERT_RAMOS_VINOLAS: 4.74
                }
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    FEDERICO_DELBONIS
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.03,
                    FEDERICO_DELBONIS: 12.73
                }
            },

            # 2019-03-25
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    DAVID_FERRER
                ],
                'score': [(5, 7), (6, 3), (6, 3)],
                'odds': {
                    FRANCES_TIAFOE: 1.83,
                    DAVID_FERRER: 1.87
                }
            },
            {
                'round': 32,
                'players': [
                    JORDAN_THOMPSON,
                    GRIGOR_DIMITROV
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    JORDAN_THOMPSON: 3.05,
                    GRIGOR_DIMITROV: 1.43
                }
            },
            {
                'round': 32,
                'players': [
                    DENIS_SHAPOVALOV,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.69,
                    ANDREY_RUBLEV: 2.25
                }
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 1.28,
                    MARCO_CECCHINATO: 3.95
                }
            },
            {
                'round': 32,
                'players': [
                    DANILL_MEDVEDEV,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    DANILL_MEDVEDEV: 1.29,
                    REILLY_OPELKA: 3.80
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    LEONARDO_MAYER
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.26,
                    LEONARDO_MAYER: 4.00
                }
            },
            {
                'round': 32,
                'players': [
                    KEVIN_ANDERSON,
                    JOAO_SOUSA
                ],
                'score': [(6, 4), 7, 6],
                'odds': {
                    KEVIN_ANDERSON: 1.53,
                    JOAO_SOUSA: 2.57
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    FILIP_KRAJINOVIC
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.18,
                    FILIP_KRAJINOVIC: 5.15
                }
            },

            # 2019-03-26
            {
                'round': 16,
                'players': [
                    FRANCES_TIAFOE,
                    DAVID_GOFFIN
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    FRANCES_TIAFOE: 2.65,
                    DAVID_GOFFIN: 1.51
                }
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.77,
                    NIKOLOZ_BASILASHVILI: 2.02
                }
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    NICK_KYRGIOS
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    BORNA_CORIC: 2.25,
                    NICK_KYRGIOS: 1.67
                }
            },
            {
                'round': 16,
                'players': [
                    DENIS_SHAPOVALOV,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(4, 6), (6, 3), (7, 6)],
                'odds': {
                    DENIS_SHAPOVALOV: 2.20,
                    STEFANOS_TSITSIPAS: 1.65
                }
            },
            {
                'round': 16,
                'players': [
                    JOHN_ISNER,
                    KYLE_EDMUND
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.85,
                    KYLE_EDMUND: 1.94
                }
            },
            {
                'round': 16,
                'players': [
                    KEVIN_ANDERSON,
                    JORDAN_THOMPSON
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    KEVIN_ANDERSON: 1.44,
                    JORDAN_THOMPSON: 2.91
                }
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    NOVAK_DJOKOVIC
                ],
                'score': [(1, 6), (7, 5), (6, 3)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 5.20,
                    NOVAK_DJOKOVIC: 1.15
                }
            },

            # 2019-03-27
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    DANILL_MEDVEDEV
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ROGER_FEDERER: 1.31,
                    DANILL_MEDVEDEV: 3.50
                }
            },
            {
                'round': 8,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    BORNA_CORIC
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.25,
                    BORNA_CORIC: 1.63
                }
            },
            {
                'round': 8,
                'players': [
                    JOHN_ISNER,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.83,
                    ROBERTO_BAUTISTA_AGUT: 1.91
                }
            },

            # 2019-03-28
            {
                'round': 8,
                'players': [
                    DENIS_SHAPOVALOV,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.56,
                    FRANCES_TIAFOE: 2.50
                }
            },
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    KEVIN_ANDERSON
                ],
                'score': [(6, 0), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.19,
                    KEVIN_ANDERSON: 4.97
                }
            },

            # 2019-03-29
            {
                'round': 4,
                'players': [
                    JOHN_ISNER,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.49,
                    FELIX_AUGER_ALIASSIME: 2.65
                }
            },
            {
                'round': 4,
                'players': [
                    ROGER_FEDERER,
                    DENIS_SHAPOVALOV
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.18,
                    DENIS_SHAPOVALOV: 4.90
                }
            },

            # 2019-03-31
            {
                'round': 2,
                'players': [
                    ROGER_FEDERER,
                    JOHN_ISNER
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.25,
                    JOHN_ISNER: 3.92
                }
            }
        ]
    },

    {
        'name': 'Fayez Sarofim & Co US Mens Clay Court Championship',
        'category': 'ATP250',
        'date': '2019-04-14',
        'location': 'Houston, United States',
        'matches': [

            # 2019-04-06
            {
                'round': 512,
                'players': [
                    SANTIAGO_GIRALDO,
                    JAMES_WARD
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    SANTIAGO_GIRALDO: 1.27,
                    JAMES_WARD: 3.50
                }
            },
            {
                'round': 512,
                'players': [
                    PEDJA_KRSTIN,
                    MARCOS_GIRON
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    PEDJA_KRSTIN: 1.65,
                    MARCOS_GIRON: 2.15
                }
            },
            {
                'round': 512,
                'players': [
                    ROBERTO_QUIROZ,
                    JC_ARAGONE
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    ROBERTO_QUIROZ: 1.65,
                    JC_ARAGONE: 2.13
                }
            },
            {
                'round': 512,
                'players': [
                    MITCHELL_KRUEGER,
                    DOMINIK_KOEPFER
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    MITCHELL_KRUEGER: 1.67,
                    DOMINIK_KOEPFER: 1.96
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_ELAHI_GALAN,
                    SEBASTIAN_OFNER
                ],
                'score': [(6, 0), (6, 2)],
                'odds': {
                    DANIEL_ELAHI_GALAN: 2.14,
                    SEBASTIAN_OFNER: 1.65
                }
            },
            {
                'round': 512,
                'players': [
                    CHRISTOPHER_EUBANKS,
                    JAY_CLARKE
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    CHRISTOPHER_EUBANKS: 2.40,
                    JAY_CLARKE: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    DARIAN_KING,
                    PETER_POLANSKY
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    DARIAN_KING: 1.63,
                    PETER_POLANSKY: 2.20
                }
            },
            {
                'round': 512,
                'players': [
                    HENRI_LAAKSONEN,
                    TOMMY_PAUL
                ],
                'score': [(6, 4), (6, 7), (6, 4)],
                'odds': {
                    HENRI_LAAKSONEN: 1.93,
                    TOMMY_PAUL: 1.69
                }
            },

            # 2019-04-08
            {
                'round': 256,
                'players': [
                    PEDJA_KRSTIN,
                    DARIAN_KING
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    PEDJA_KRSTIN: 1.48,
                    DARIAN_KING: 2.51
                }
            },
            {
                'round': 256,
                'players': [
                    DANIEL_ELAHI_GALAN,
                    ROBERTO_QUIROZ
                ],
                'score': [(4, 6), (7, 5), (6, 1)],
                # no odds
            },
            {
                'round': 256,
                'players': [
                    SANTIAGO_GIRALDO,
                    CHRISTOPHER_EUBANKS
                ],
                'score': [(6, 4), (6, 4)],
                # no odds
            },
            {
                'round': 256,
                'players': [
                    HENRI_LAAKSONEN,
                    MITCHELL_KRUEGER
                ],
                'score': [(6, 3), (5, 7), (6, 3)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    BERNARD_TOMIC,
                    DENIS_KUDLA
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    BERNARD_TOMIC: 1.77,
                    DENIS_KUDLA: 2.05
                }
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    HUGO_DELLIEN
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    CASPER_RUUD: 1.49,
                    HUGO_DELLIEN: 2.68
                }
            },
            {
                'round': 32,
                'players': [
                    RYAN_HARRISON,
                    IVO_KARLOVIC
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    RYAN_HARRISON: 2.26,
                    IVO_KARLOVIC: 1.65
                }
            },
            {
                'round': 32,
                'players': [
                    CRISTIAN_GARIN,
                    PABLO_CUEVAS
                ],
                'score': [(4, 6), (6, 4), (6, 2)],
                'odds': {
                    CRISTIAN_GARIN: 2.38,
                    PABLO_CUEVAS: 1.59
                }
            },
            {
                'round': 32,
                'players': [
                    MARCEL_GRANOLLERS,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 2), (4, 6), (6, 2)],
                'odds': {
                    MARCEL_GRANOLLERS: 2.20,
                    TAYLOR_FRITZ: 1.59
                }
            },

            # 2019-04-09
            {
                'round': 32,
                'players': [
                    JANKO_TIPSAREVIC,
                    TENNYS_SANDGREN
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    JANKO_TIPSAREVIC: 2.71,
                    TENNYS_SANDGREN: 1.45
                }
            },
            {
                'round': 32,
                'players': [
                    SANTIAGO_GIRALDO,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    SANTIAGO_GIRALDO: 1.43,
                    BRADLEY_KLAHN: 2.78
                }
            },
            {
                'round': 32,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    NOAH_RUBIN
                ],
                'score': [(6, 7), (6, 3), (6, 3)],
                'odds': {
                    GUILLERMO_GARCIA_LOPEZ: 1.57,
                    NOAH_RUBIN: 2.48
                }
            },
            {
                'round': 32,
                'players': [
                    DANIEL_ELAHI_GALAN,
                    PAOLO_LORENZI
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    DANIEL_ELAHI_GALAN: 2.00,
                    PAOLO_LORENZI: 1.77
                }
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    BJORN_FRATANGELO
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    SAM_QUERREY: 1.61,
                    BJORN_FRATANGELO: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    JORDAN_THOMPSON,
                    PEDJA_KRSTIN
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    JORDAN_THOMPSON: 1.58,
                    PEDJA_KRSTIN: 2.48
                }
            },
            {
                'round': 32,
                'players': [
                    HENRI_LAAKSONEN,
                    MACKENZIE_MCDONALD
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    HENRI_LAAKSONEN: 1.71,
                    MACKENZIE_MCDONALD: 2.13
                }
            },

            # 2019-04-10
            {
                'round': 16,
                'players': [
                    HENRI_LAAKSONEN,
                    RYAN_HARRISON
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    HENRI_LAAKSONEN: 1.93,
                    RYAN_HARRISON: 1.83
                }
            },
            {
                'round': 16,
                'players': [
                    MARCEL_GRANOLLERS,
                    BERNARD_TOMIC
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.59,
                    BERNARD_TOMIC: 2.40
                }
            },
            {
                'round': 16,
                'players': [
                    CASPER_RUUD,
                    REILLY_OPELKA
                ],
                'score': [(4, 6), (6, 4), (6, 4)],
                'odds': {
                    CASPER_RUUD: 1.89,
                    REILLY_OPELKA: 1.91
                }
            },
            {
                'round': 16,
                'players': [
                    CRISTIAN_GARIN,
                    JEREMY_CHARDY
                ],
                'score': [(3, 6), (7, 6), (7, 6)],
                'odds': {
                    CRISTIAN_GARIN: 1.67,
                    JEREMY_CHARDY: 2.03
                }
            },

            # 2019-04-11
            {
                'round': 16,
                'players': [
                    SAM_QUERREY,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    SAM_QUERREY: 1.44,
                    GUILLERMO_GARCIA_LOPEZ: 2.79
                }
            },
            {
                'round': 16,
                'players': [
                    JORDAN_THOMPSON,
                    SANTIAGO_GIRALDO
                ],
                'score': [(4, 6), (7, 6), (7, 5)],
                'odds': {
                    JORDAN_THOMPSON: 1.59,
                    SANTIAGO_GIRALDO: 2.30
                }
            },
            {
                'round': 16,
                'players': [
                    JANKO_TIPSAREVIC,
                    CAMERON_NORRIE
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JANKO_TIPSAREVIC: 2.27,
                    CAMERON_NORRIE: 1.63
                }
            },
            {
                'round': 16,
                'players': [
                    DANIEL_ELAHI_GALAN,
                    STEVE_JOHNSON
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    DANIEL_ELAHI_GALAN: 2.85,
                    STEVE_JOHNSON: 1.43
                }
            },

            # 2019-04-12
            {
                'round': 8,
                'players': [
                    CASPER_RUUD,
                    MARCEL_GRANOLLERS
                ],
                'score': [(6, 1), (6, 0)],
                'odds': {
                    CASPER_RUUD: 1.65,
                    MARCEL_GRANOLLERS: 2.30
                }
            },
            {
                'round': 8,
                'players': [
                    CRISTIAN_GARIN,
                    HENRI_LAAKSONEN
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    CRISTIAN_GARIN: 1.49,
                    HENRI_LAAKSONEN: 2.72
                }
            },
            {
                'round': 8,
                'players': [
                    SAM_QUERREY,
                    JANKO_TIPSAREVIC
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    SAM_QUERREY: 1.40,
                    JANKO_TIPSAREVIC: 2.96
                }
            },

            # 2019-04-13
            {
                'round': 8,
                'players': [
                    DANIEL_ELAHI_GALAN,
                    JORDAN_THOMPSON
                ],
                'score': [(6, 1), (4, 6), (6, 4)],
                # no odds
            },
            {
                'round': 4,
                'players': [
                    CASPER_RUUD,
                    DANIEL_ELAHI_GALAN
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    CASPER_RUUD: 1.29,
                    DANIEL_ELAHI_GALAN: 3.60
                }
            },
            {
                'round': 4,
                'players': [
                    CRISTIAN_GARIN,
                    SAM_QUERREY
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    CRISTIAN_GARIN: 2.00,
                    SAM_QUERREY: 1.81
                }
            },

            # 2019-04-13
            {
                'round': 2,
                'players': [
                    CRISTIAN_GARIN,
                    CASPER_RUUD
                ],
                'score': [(7, 6), (4, 6), (6, 3)],
                'odds': {
                    CRISTIAN_GARIN: 1.67,
                    CASPER_RUUD: 2.25
                }
            }
        ]
    },

    {
        'name': 'Grand Prix Hassan II',
        'category': 'ATP250',
        'date': '2019--04-14',
        'location': 'Marrakech, Morocco',
        'matches': [

            # 2019-04-07
            {
                'round': 512,
                'players': [
                    EVGENY_KARLOVSKIY,
                    TIM_PUETZ
                ],
                'score': [(7, 6), (4, 6), (6, 2)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    CARLOS_BERLOCQ,
                    ADAM_MOUNDIR
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    CARLOS_BERLOCQ: 1.07,
                    ADAM_MOUNDIR: 7.18
                }
            },
            {
                'round': 512,
                'players': [
                    FACUNDO_BAGNIS,
                    VIKTOR_TROICKI
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    FACUNDO_BAGNIS: 1.69,
                    VIKTOR_TROICKI: 2.01
                }
            },
            {
                'round': 512,
                'players': [
                    ADRIAN_MENENDEZ_MACEIRAS,
                    LAMINE_OUAHAB
                ],
                'score': [(7, 6), (6, 7), (6, 4)],
                'odds': {
                    ADRIAN_MENENDEZ_MACEIRAS: 2.28,
                    LAMINE_OUAHAB: 1.57
                }
            },
            {
                'round': 512,
                'players': [
                    ELLIOT_BENCHETRIT,
                    CORENTIN_MOUTET
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    ELLIOT_BENCHETRIT: 3.24,
                    CORENTIN_MOUTET: 1.33
                }
            },
            {
                'round': 512,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    GREGOIRE_BARRERE
                ],
                'score': [(7, 5), (3, 6), (6, 4)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.59,
                    GREGOIRE_BARRERE: 2.30
                }
            },
            {
                'round': 512,
                'players': [
                    ELIAS_YMER,
                    KEVIN_KRAWIETZ
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ELIAS_YMER: 1.31,
                    KEVIN_KRAWIETZ: 3.40
                }
            },
            {
                'round': 512,
                'players': [
                    LORENZO_SONEGO,
                    ALEXEY_VATUTIN
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 1.36,
                    ALEXEY_VATUTIN: 3.00
                }
            },

            # 2019-04-08
            {
                'round': 256,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    EVGENY_KARLOVSKIY
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.15,
                    EVGENY_KARLOVSKIY: 5.16
                }
            },
            {
                'round': 256,
                'players': [
                    ADRIAN_MENENDEZ_MACEIRAS,
                    ELLIOT_BENCHETRIT
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    ADRIAN_MENENDEZ_MACEIRAS: 2.55,
                    ELLIOT_BENCHETRIT: 1.48
                }
            },
            {
                'round': 256,
                'players': [
                    FACUNDO_BAGNIS,
                    ELIAS_YMER
                ],
                'score': [(1, 6), (6, 3), (7, 5)],
                'odds': {
                    FACUNDO_BAGNIS: 2.13,
                    ELIAS_YMER: 1.63
                }
            },
            {
                'round': 256,
                'players': [
                    LORENZO_SONEGO,
                    CARLOS_BERLOCQ
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    LORENZO_SONEGO: 1.28,
                    CARLOS_BERLOCQ: 3.34
                }
            },
            {
                'round': 32,
                'players': [
                    JO_WILFRIED_TSONGA,
                    CEDRIC_MARCEL_STEBE
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.11,
                    CEDRIC_MARCEL_STEBE: 6.50
                }
            },
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    TARO_DANIEL: 1.45,
                    MISCHA_ZVEREV: 2.80
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_ANDREOZZI,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    GUIDO_ANDREOZZI: 2.40,
                    ALBERT_RAMOS_VINOLAS: 1.59
                }
            },
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    GILLES_SIMON: 1.38,
                    JOZEF_KOVALIK: 3.00
                }
            },
            {
                'round': 32,
                'players': [
                    KYLE_EDMUND,
                    UGO_HUMBERT
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    KYLE_EDMUND: 1.20,
                    UGO_HUMBERT: 4.70
                }
            },

            # 2019-04-09
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    ALJAZ_BEDENE
                ],
                'score': [(3, 6), (6, 4), (7, 5)],
                'odds': {
                    BENOIT_PAIRE: 1.95,
                    ALJAZ_BEDENE: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    FACUNDO_BAGNIS
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    JAUME_MUNAR: 1.30,
                    FACUNDO_BAGNIS: 3.30
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    CARLOS_BERLOCQ
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.50,
                    CARLOS_BERLOCQ: 2.51
                }
            },
            {
                'round': 32,
                'players': [
                    ROBIN_HAASE,
                    MALEK_JAZIRI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ROBIN_HAASE: 1.44,
                    MALEK_JAZIRI: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_ANDUJAR,
                    FEDERICO_DELBONIS
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    PABLO_ANDUJAR: 2.25,
                    FEDERICO_DELBONIS: 1.63
                }
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 7), (6, 4), (6, 1)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.61,
                    THOMAS_FABBIANO: 2.35
                }
            },
            {
                'round': 32,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.56,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.45
                }
            },
            {
                'round': 32,
                'players': [
                    ADRIAN_MENENDEZ_MACEIRAS,
                    FERNANDO_VERDASCO
                ],
                'score': [(5, 7), (6, 2), (6, 2)],
                'odds': {
                    ADRIAN_MENENDEZ_MACEIRAS: 4.60,
                    FERNANDO_VERDASCO: 1.20
                }
            },
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    LASLO_DJERE
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    LORENZO_SONEGO: 2.13,
                    LASLO_DJERE: 1.63
                }
            },
            {
                'round': 32,
                'players': [
                    JIRI_VESELY,
                    FABIO_FOGNINI
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JIRI_VESELY: 2.32,
                    FABIO_FOGNINI: 1.54
                }
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.10,
                    DENIS_ISTOMIN: 7.70
                }
            },

            # 2019-04-10
            {
                'round': 16,
                'players': [
                    LORENZO_SONEGO,
                    ROBIN_HAASE
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    LORENZO_SONEGO: 1.66,
                    ROBIN_HAASE: 2.20
                }
            },
            {
                'round': 16,
                'players': [
                    TARO_DANIEL,
                    ADRIAN_MENENDEZ_MACEIRAS
                ],
                'score': [(6, 2), (1, 6), (6, 1)],
                'odds': {
                    TARO_DANIEL: 1.30,
                    ADRIAN_MENENDEZ_MACEIRAS: 3.40
                }
            },
            {
                'round': 16,
                'players': [
                    GILLES_SIMON,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    GILLES_SIMON: 1.59,
                    GUIDO_ANDREOZZI: 2.25
                }
            },
            {
                'round': 16,
                'players': [
                    JO_WILFRIED_TSONGA,
                    KYLE_EDMUND
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    JO_WILFRIED_TSONGA: 2.65,
                    KYLE_EDMUND: 1.49
                }
            },

            # 2019-04-11
            {
                'round': 16,
                'players': [
                    JIRI_VESELY,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JIRI_VESELY: 1.77,
                    JUAN_IGNACIO_LONDERO: 2.05
                }
            },
            {
                'round': 16,
                'players': [
                    BENOIT_PAIRE,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    BENOIT_PAIRE: 1.67,
                    PIERRE_HUGUES_HERBERT: 2.15
                }
            },
            {
                'round': 16,
                'players': [
                    PABLO_ANDUJAR,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PABLO_ANDUJAR: 1.95,
                    PHILIPP_KOHLSCHREIBER: 1.74
                }
            },
            {
                'round': 16,
                'players': [
                    JAUME_MUNAR,
                    ALEXANDER_ZVEREV
                ],
                'score': [(7, 6), (2, 6), (6, 3)],
                'odds': {
                    JAUME_MUNAR: 4.11,
                    ALEXANDER_ZVEREV: 1.24
                }
            },

            # 2019-04-12
            {
                'round': 8,
                'players': [
                    JO_WILFRIED_TSONGA,
                    LORENZO_SONEGO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.42,
                    LORENZO_SONEGO: 2.75
                }
            },
            {
                'round': 8,
                'players': [
                    BENOIT_PAIRE,
                    JAUME_MUNAR
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 2.35,
                    JAUME_MUNAR: 1.59
                }
            },
            {
                'round': 8,
                'players': [
                    PABLO_ANDUJAR,
                    JIRI_VESELY
                ],
                'score': [],
                'wo': True,
                'odds': {
                    PABLO_ANDUJAR: 1.77,
                    JIRI_VESELY: 2.05
                }
            },
            {
                'round': 8,
                'players': [
                    GILLES_SIMON,
                    TARO_DANIEL
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    GILLES_SIMON: 1.36,
                    TARO_DANIEL: 3.00
                }
            },

            # 2019-04-13
            {
                'round': 4,
                'players': [
                    BENOIT_PAIRE,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(2, 6), (6, 4), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 3.00,
                    JO_WILFRIED_TSONGA: 1.38
                }
            },
            {
                'round': 4,
                'players': [
                    PABLO_ANDUJAR,
                    GILLES_SIMON
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    PABLO_ANDUJAR: 1.91,
                    GILLES_SIMON: 1.80
                }
            },

            # 2019-04-14
            {
                'round': 2,
                'players': [
                    BENOIT_PAIRE,
                    PABLO_ANDUJAR
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 2.10,
                    PABLO_ANDUJAR: 1.69
                }
            }
        ]
    },

    {
        'name': 'Rolex Monte-Carlo Masters',
        'category': 'ATP1000',
        'date': '2019-04-21',
        'location': 'Monte Carlo, Monaco',
        'matches': [

            # 2019-04-13
            {
                'round': 512,
                'players': [
                    ELIAS_YMER,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    ELIAS_YMER: 2.15,
                    MIOMIR_KECMANOVIC: 1.65
                }
            },
            {
                'round': 512,
                'players': [
                    THOMAS_FABBIANO,
                    FELICIANO_LOPEZ
                ],
                'score': [(3, 6), (6, 4), (6, 2)],
                'odds': {
                    THOMAS_FABBIANO: 1.83,
                    FELICIANO_LOPEZ: 1.82
                }
            },
            {
                'round': 512,
                'players': [
                    MARCO_TRUNGELLITI,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MARCO_TRUNGELLITI: 1.83,
                    PETER_GOJOWCZYK: 1.71
                }
            },
            {
                'round': 512,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    MAXIMILIAN_MARTERER
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.41,
                    MAXIMILIAN_MARTERER: 2.70
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREY_RUBLEV,
                    BERNARD_TOMIC
                ],
                'score': [(4, 6), (7, 6), (7, 6)],
                'odds': {
                    ANDREY_RUBLEV: 1.19,
                    BERNARD_TOMIC: 4.44
                }
            },
            {
                'round': 512,
                'players': [
                    GUIDO_ANDREOZZI,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    GUIDO_ANDREOZZI: 1.50,
                    ERNESTS_GULBIS: 2.40
                }
            },
            {
                'round': 512,
                'players': [
                    TARO_DANIEL,
                    YANNICK_MADEN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    TARO_DANIEL: 1.63,
                    YANNICK_MADEN: 2.10
                }
            },
            {
                'round': 512,
                'players': [
                    FEDERICO_DELBONIS,
                    ILYA_IVASHKA
                ],
                'score': [(6, 2), (3, 4)],
                'retired': True,
                'odds': {
                    FEDERICO_DELBONIS: 1.24,
                    ILYA_IVASHKA: 3.79
                }
            },
            {
                'round': 512,
                'players': [
                    JULIAN_OCLEPPO,
                    MISCHA_ZVEREV
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JULIAN_OCLEPPO: 2.78,
                    MISCHA_ZVEREV: 1.36
                }
            },
            {
                'round': 512,
                'players': [
                    ALJAZ_BEDENE,
                    HUGO_NYS
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ALJAZ_BEDENE: 1.07,
                    HUGO_NYS: 8.00
                }
            },
            {
                'round': 512,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    ROMAIN_ARNEODO
                ],
                'score': [(6, 0), (6, 4)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.06,
                    ROMAIN_ARNEODO: 7.00
                }
            },
            {
                'round': 512,
                'players': [
                    LORENZO_SONEGO,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 2), (4, 6), (6, 0)],
                'odds': {
                    LORENZO_SONEGO: 1.33,
                    YOSHIHITO_NISHIOKA: 3.00
                }
            },
            {
                'round': 512,
                'players': [
                    UGO_HUMBERT,
                    FLORENT_DIEP
                ],
                'score': [(3, 6), (7, 5), (6, 3)],
                'odds': {
                    UGO_HUMBERT: 1.05,
                    FLORENT_DIEP: 11.00
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    LEONARDO_MAYER
                ],
                'score': [(7, 6), (2, 6), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 3.20,
                    LEONARDO_MAYER: 1.33
                }
            },
            {
                'round': 256,
                'players': [
                    LORENZO_SONEGO,
                    MARCO_TRUNGELLITI
                ],
                'score': [],
                'wo': True,
                # no odds
            },

            # 2019-04-14
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    ELIAS_YMER
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 2.35,
                    ELIAS_YMER: 1.57
                }
            },
            {
                'round': 256,
                'players': [
                    GUIDO_ANDREOZZI,
                    JULIAN_OCLEPPO
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    GUIDO_ANDREOZZI: 1.07,
                    JULIAN_OCLEPPO: 7.43
                }
            },
            {
                'round': 256,
                'players': [
                    FEDERICO_DELBONIS,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(7, 5), (6, 0)],
                'odds': {
                    FEDERICO_DELBONIS: 1.80,
                    ALBERT_RAMOS_VINOLAS: 1.81
                }
            },
            {
                'round': 256,
                'players': [
                    ALJAZ_BEDENE,
                    TARO_DANIEL
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALJAZ_BEDENE: 1.54,
                    TARO_DANIEL: 2.39
                }
            },
            {
                'round': 256,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.47,
                    THOMAS_FABBIANO: 2.46
                }
            },
            {
                'round': 256,
                'players': [
                    ANDREY_RUBLEV,
                    UGO_HUMBERT
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 1.36,
                    UGO_HUMBERT: 3.00
                }
            },
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    LUCAS_POUILLE
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    STAN_WAWRINKA: 1.39,
                    LUCAS_POUILLE: 3.03
                }
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    LASLO_DJERE
                ],
                'score': [(6, 7), (6, 2), (6, 4)],
                'odds': {
                    GUIDO_PELLA: 1.69,
                    LASLO_DJERE: 2.15
                }
            },
            {
                'round': 64,
                'players': [
                    GRIGOR_DIMITROV,
                    MATTEO_BERRETTINI
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    GRIGOR_DIMITROV: 1.71,
                    MATTEO_BERRETTINI: 2.10
                }
            },
            {
                'round': 64,
                'players': [
                    BORNA_CORIC,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 4), (5, 7), (7, 5)],
                'odds': {
                    BORNA_CORIC: 1.53,
                    HUBERT_HURKACZ: 2.63
                }
            },

            # 2019-04-15
            {
                'round': 64,
                'players': [
                    LORENZO_SONEGO,
                    ANDREAS_SEPPI
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 1.48,
                    ANDREAS_SEPPI: 2.70
                }
            },
            {
                'round': 64,
                'players': [
                    JAUME_MUNAR,
                    LUCAS_CATARINA
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    JAUME_MUNAR: 1.04,
                    LUCAS_CATARINA: 12.24
                }
            },
            {
                'round': 64,
                'players': [
                    DUSAN_LAJOVIC,
                    MALEK_JAZIRI
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DUSAN_LAJOVIC: 1.37,
                    MALEK_JAZIRI: 3.18
                }
            },
            {
                'round': 64,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    JEREMY_CHARDY
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 2.60,
                    JEREMY_CHARDY: 1.51
                }
            },
            {
                'round': 64,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    TARO_DANIEL
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.36,
                    TARO_DANIEL: 3.22
                }
            },
            {
                'round': 64,
                'players': [
                    MARTIN_KLIZAN,
                    FEDERICO_DELBONIS
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    MARTIN_KLIZAN: 2.99,
                    FEDERICO_DELBONIS: 1.39
                }
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    JOHN_MILLMAN
                ],
                'score': [(3, 6), (6, 1), (6, 1)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.18,
                    JOHN_MILLMAN: 5.16
                }
            },
            {
                'round': 64,
                'players': [
                    RADU_ALBOT,
                    ALJAZ_BEDENE
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    RADU_ALBOT: 2.35,
                    ALJAZ_BEDENE: 1.57
                }
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    KYLE_EDMUND
                ],
                'score': [(4, 6), (6, 3), (6, 1)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 2.15,
                    KYLE_EDMUND: 1.69
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 1.30,
                    GUIDO_ANDREOZZI: 3.57
                }
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    DENIS_SHAPOVALOV
                ],
                'score': [(5, 7), (6, 3), (6, 1)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.20,
                    DENIS_SHAPOVALOV: 1.67
                }
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    ANDREY_RUBLEV
                ],
                'score': [(4, 6), (7, 5), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 2.02,
                    ANDREY_RUBLEV: 1.74
                }
            },
            {
                'round': 64,
                'players': [
                    MARTON_FUCSOVICS,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(7, 5), (3, 6), (6, 1)],
                'odds': {
                    MARTON_FUCSOVICS: 1.75,
                    NIKOLOZ_BASILASHVILI: 2.05
                }
            },
            {
                'round': 64,
                'players': [
                    MARCO_CECCHINATO,
                    DAMIR_DZUMHUR
                ],
                'score': [(4, 0)],
                'retired': True,
                'odds': {
                    MARCO_CECCHINATO: 1.28,
                    DAMIR_DZUMHUR: 3.60
                }
            },
            {
                'round': 64,
                'players': [
                    DANILL_MEDVEDEV,
                    JOAO_SOUSA
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    DANILL_MEDVEDEV: 1.54,
                    JOAO_SOUSA: 2.49
                }
            },

            # 2019-04-16
            {
                'round': 64,
                'players': [
                    GILLES_SIMON,
                    ALEXEI_POPYRIN
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    GILLES_SIMON: 1.41,
                    ALEXEI_POPYRIN: 2.84
                }
            },
            {
                'round': 64,
                'players': [
                    CAMERON_NORRIE,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    CAMERON_NORRIE: 1.62,
                    ADRIAN_MANNARINO: 2.36
                }
            },
            {
                'round': 64,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 2.49,
                    FERNANDO_VERDASCO: 1.54
                }
            },
            {
                'round': 64,
                'players': [
                    TAYLOR_FRITZ,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(6, 4), (2, 0)],
                'retired': True,
                'odds': {
                    TAYLOR_FRITZ: 5.75,
                    JO_WILFRIED_TSONGA: 1.14
                }
            },
            {
                'round': 64,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.48,
                    JUAN_IGNACIO_LONDERO: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    MARCO_CECCHINATO,
                    STAN_WAWRINKA
                ],
                'score': [(0, 6), (7, 5), (6, 3)],
                'odds': {
                    MARCO_CECCHINATO: 2.44,
                    STAN_WAWRINKA: 1.57
                }
            },
            {
                'round': 32,
                'players': [
                    BORNA_CORIC,
                    JAUME_MUNAR
                ],
                'score': [(6, 7), (7, 6), (6, 4)],
                'odds': {
                    BORNA_CORIC: 1.65,
                    JAUME_MUNAR: 2.25
                }
            },
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    KAREN_KHACHANOV
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    LORENZO_SONEGO: 2.35,
                    KAREN_KHACHANOV: 1.59
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    MARIN_CILIC
                ],
                'score': [(6, 3), (5, 7), (6, 1)],
                'odds': {
                    GUIDO_PELLA: 2.23,
                    MARIN_CILIC: 1.67
                }
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 3), (4, 6), (6, 4)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.16,
                    PHILIPP_KOHLSCHREIBER: 5.00
                }
            },

            # 2019-04-17
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    MARTON_FUCSOVICS
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    CAMERON_NORRIE: 2.95,
                    MARTON_FUCSOVICS: 1.41
                }
            },
            {
                'round': 32,
                'players': [
                    TAYLOR_FRITZ,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    TAYLOR_FRITZ: 5.00,
                    DIEGO_SCHWARTZMAN: 1.16
                }
            },
            {
                'round': 32,
                'players': [
                    GRIGOR_DIMITROV,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    GRIGOR_DIMITROV: 1.67,
                    JAN_LENNARD_STRUFF: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    DUSAN_LAJOVIC,
                    DAVID_GOFFIN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DUSAN_LAJOVIC: 3.61,
                    DAVID_GOFFIN: 1.27
                }
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    GILLES_SIMON
                ],
                'score': [],
                'wo': True,
                'odds': {
                    FABIO_FOGNINI: 1.91,
                    GILLES_SIMON: 1.87
                }
            },
            {
                'round': 32,
                'players': [
                    DANILL_MEDVEDEV,
                    RADU_ALBOT
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    DANILL_MEDVEDEV: 1.43,
                    RADU_ALBOT: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.23,
                    MIKHAIL_KUKUSHKIN: 3.95
                }
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    KEI_NISHIKORI
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 4.04,
                    KEI_NISHIKORI: 1.20
                }
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 1.21,
                    MARTIN_KLIZAN: 4.34
                }
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.47,
                    FELIX_AUGER_ALIASSIME: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.07,
                    ROBERTO_BAUTISTA_AGUT: 7.50
                }
            },

            # 2019-04-18
            {
                'round': 16,
                'players': [
                    LORENZO_SONEGO,
                    CAMERON_NORRIE
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    LORENZO_SONEGO: 1.57,
                    CAMERON_NORRIE: 2.40
                }
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 4), (4, 6), (6, 4)],
                'odds': {
                    GUIDO_PELLA: 2.49,
                    MARCO_CECCHINATO: 1.58
                }
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    BORNA_CORIC: 1.42,
                    PIERRE_HUGUES_HERBERT: 2.70
                }
            },
            {
                'round': 16,
                'players': [
                    DANILL_MEDVEDEV,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 2), (1, 6), (6, 4)],
                'odds': {
                    DANILL_MEDVEDEV: 2.00,
                    STEFANOS_TSITSIPAS: 1.79
                }
            },
            {
                'round': 16,
                'players': [
                    DUSAN_LAJOVIC,
                    DOMINIC_THIEM
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 4.90,
                    DOMINIC_THIEM: 1.17
                }
            },
            {
                'round': 16,
                'players': [
                    FABIO_FOGNINI,
                    ALEXANDER_ZVEREV
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    FABIO_FOGNINI: 4.25,
                    ALEXANDER_ZVEREV: 1.26
                }
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    GRIGOR_DIMITROV
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.02,
                    GRIGOR_DIMITROV: 13.19
                }
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.06,
                    TAYLOR_FRITZ: 7.50
                }
            },

            # 2019-04-19
            {
                'round': 8,
                'players': [
                    DUSAN_LAJOVIC,
                    LORENZO_SONEGO
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    DUSAN_LAJOVIC: 1.69,
                    LORENZO_SONEGO: 2.10
                }
            },
            {
                'round': 8,
                'players': [
                    FABIO_FOGNINI,
                    BORNA_CORIC
                ],
                'score': [(1, 6), (6, 3), (6, 2)],
                'odds': {
                    FABIO_FOGNINI: 2.20,
                    BORNA_CORIC: 1.65
                }
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    GUIDO_PELLA
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.02,
                    GUIDO_PELLA: 16.00
                }
            },
            {
                'round': 8,
                'players': [
                    DANILL_MEDVEDEV,
                    NOVAK_DJOKOVIC
                ],
                'score': [(6, 3), (4, 6), (6, 2)],
                'odds': {
                    DANILL_MEDVEDEV: 4.40,
                    NOVAK_DJOKOVIC: 1.20
                }
            },

            # 2019-04-20
            {
                'round': 4,
                'players': [
                    DUSAN_LAJOVIC,
                    DANILL_MEDVEDEV
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    DUSAN_LAJOVIC: 2.75,
                    DANILL_MEDVEDEV: 1.42
                }
            },
            {
                'round': 4,
                'players': [
                    FABIO_FOGNINI,
                    RAFAEL_NADAL
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    FABIO_FOGNINI: 7.50,
                    RAFAEL_NADAL: 1.06
                }
            },

            # 2019-04-21
            {
                'round': 2,
                'players': [
                    FABIO_FOGNINI,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.59,
                    DUSAN_LAJOVIC: 2.25
                }
            }

        ]
    },

    {
        'name': 'Barcelona Open Banc Sabadell',
        'category': 'ATP500',
        'date': '2019-04-28',
        'location': 'Barcelona, Spain',
        'matches': [

            # 2019-04-20
            {
                'round': 512,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    CARLOS_BERLOCQ
                ],
                'score': [(6, 4), (6, 3)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    PEDRO_SOUSA,
                    CARLOS_ALCARAZ_GARFIA
                ],
                'score': [(6, 7), (6, 3), (6, 1)],
                'odds': {
                    PEDRO_SOUSA: 1.27,
                    CARLOS_ALCARAZ_GARFIA: 3.02
                }
            },
            {
                'round': 512,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.34,
                    DENIS_ISTOMIN: 2.70
                }
            },
            {
                'round': 512,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    PEDRO_MARTINEZ
                ],
                'score': [(7, 5), 6, 1],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.36,
                    PEDRO_MARTINEZ: 2.85
                }
            },
            {
                'round': 512,
                'players': [
                    ANTOINE_HOANG,
                    ANDREY_RUBLEV
                ],
                'score': [(5, 7), (7, 6), (7, 6)],
                'odds': {
                    ANTOINE_HOANG: 4.65,
                    ANDREY_RUBLEV: 1.18
                }
            },
            {
                'round': 512,
                'players': [
                    MARCEL_GRANOLLERS,
                    DANIEL_EVANS
                ],
                'score': [(6, 3), (4, 6), (7, 5)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.59,
                    DANIEL_EVANS: 2.25
                }
            },
            {
                'round': 512,
                'players': [
                    GUIDO_ANDREOZZI,
                    TOMMY_ROBREDO
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    GUIDO_ANDREOZZI: 1.32,
                    TOMMY_ROBREDO: 3.30
                }
            },
            {
                'round': 512,
                'players': [
                    NICOLAS_JARRY,
                    CHUN_HSIN_TSENG
                ],
                'score': [(6, 4), (3, 6), (7, 6)],
                'odds': {
                    NICOLAS_JARRY: 1.07,
                    CHUN_HSIN_TSENG: 6.25
                }
            },
            {
                'round': 512,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.34,
                    ALEXEI_POPYRIN: 3.10
                }
            },
            {
                'round': 512,
                'players': [
                    HUGO_DELLIEN,
                    GREGOIRE_BARRERE
                ],
                'score': [(6, 7), (7, 6), (7, 6)],
                'odds': {
                    HUGO_DELLIEN: 1.67,
                    GREGOIRE_BARRERE: 2.10
                }
            },
            {
                'round': 512,
                'players': [
                    FEDERICO_DELBONIS,
                    THIAGO_MONTEIRO
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    FEDERICO_DELBONIS: 1.24,
                    THIAGO_MONTEIRO: 3.81
                }
            },
            {
                'round': 512,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.18,
                    JOZEF_KOVALIK: 4.52
                }
            },

            # 2019-04-21
            {
                'round': 256,
                'players': [
                    PEDRO_SOUSA,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 4), (6, 2)],
                # no odds
            },
            {
                'round': 256,
                'players': [
                    MARCEL_GRANOLLERS,
                    NICOLAS_JARRY
                ],
                'score': [(6, 7), (7, 5), (6, 4)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.77,
                    NICOLAS_JARRY: 1.91
                }
            },
            {
                'round': 256,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.63,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.20
                }
            },
            {
                'round': 256,
                'players': [
                    HUGO_DELLIEN,
                    ANTOINE_HOANG
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    HUGO_DELLIEN: 1.64,
                    ANTOINE_HOANG: 2.05
                }
            },
            {
                'round': 256,
                'players': [
                    FEDERICO_DELBONIS,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    FEDERICO_DELBONIS: 1.38,
                    GUILLERMO_GARCIA_LOPEZ: 2.77
                }
            },
            {
                'round': 256,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.51,
                    ROBERTO_CARBALLES_BAENA: 2.46
                }
            },

            # 2019-04-22
            {
                'round': 64,
                'players': [
                    FERNANDO_VERDASCO,
                    FELICIANO_LOPEZ
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    FERNANDO_VERDASCO: 1.48,
                    FELICIANO_LOPEZ: 2.67
                }
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    HUGO_DELLIEN
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.50,
                    HUGO_DELLIEN: 2.51
                }
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(4, 6), (6, 4), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.25,
                    YOSHIHITO_NISHIOKA: 3.80
                }
            },
            {
                'round': 64,
                'players': [
                    BENOIT_PAIRE,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    BENOIT_PAIRE: 1.54,
                    JUAN_IGNACIO_LONDERO: 2.40
                }
            },
            {
                'round': 64,
                'players': [
                    JAUME_MUNAR,
                    PEDRO_SOUSA
                ],
                'score': [(2, 6), (6, 4), (6, 0)],
                'odds': {
                    JAUME_MUNAR: 1.30,
                    PEDRO_SOUSA: 3.60
                }
            },
            {
                'round': 64,
                'players': [
                    MACKENZIE_MCDONALD,
                    TARO_DANIEL
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    MACKENZIE_MCDONALD: 3.50,
                    TARO_DANIEL: 1.31
                }
            },
            {
                'round': 64,
                'players': [
                    LEONARDO_MAYER,
                    MARIUS_COPIL
                ],
                'score': [(6, 3), (6, 7), (7, 5)],
                'odds': {
                    LEONARDO_MAYER: 1.27,
                    MARIUS_COPIL: 3.52
                }
            },
            {
                'round': 64,
                'players': [
                    NICOLAS_JARRY,
                    MARCEL_GRANOLLERS
                ],
                'score': [(7, 5), (4, 6), (6, 4)],
                'odds': {
                    NICOLAS_JARRY: 1.83,
                    MARCEL_GRANOLLERS: 1.89
                }
            },
            {
                'round': 64,
                'players': [
                    MARTON_FUCSOVICS,
                    DENIS_KUDLA
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    MARTON_FUCSOVICS: 1.18,
                    DENIS_KUDLA: 4.80
                }
            },
            {
                'round': 64,
                'players': [
                    TAYLOR_FRITZ,
                    REILLY_OPELKA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 1.72,
                    REILLY_OPELKA: 1.97
                }
            },

            # 2019-04-23
            {
                'round': 64,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    CAMERON_NORRIE
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.56,
                    CAMERON_NORRIE: 2.35
                }
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    JOAO_SOUSA
                ],
                'score': [(3, 6), (7, 6), (6, 2)],
                'odds': {
                    GUIDO_PELLA: 1.36,
                    JOAO_SOUSA: 3.15
                }
            },
            {
                'round': 64,
                'players': [
                    NICOLA_KUHN,
                    FEDERICO_DELBONIS
                ],
                'score': [(7, 6), (4, 6), (6, 2)],
                'odds': {
                    NICOLA_KUHN: 4.90,
                    FEDERICO_DELBONIS: 1.16
                }
            },
            {
                'round': 64,
                'players': [
                    MALEK_JAZIRI,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 7), (4, 6), (6, 2)],
                'odds': {
                    MALEK_JAZIRI: 2.70,
                    GUIDO_ANDREOZZI: 1.44
                }
            },
            {
                'round': 64,
                'players': [
                    CRISTIAN_GARIN,
                    MARTIN_KLIZAN
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    CRISTIAN_GARIN: 1.71,
                    MARTIN_KLIZAN: 2.10
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_FERRER,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DAVID_FERRER: 1.14,
                    MISCHA_ZVEREV: 6.00
                }
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    JAUME_MUNAR: 1.43,
                    FRANCES_TIAFOE: 2.70
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    DAVID_GOFFIN
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.40,
                    DAVID_GOFFIN: 1.56
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.31,
                    MARTON_FUCSOVICS: 3.44
                }
            },
            {
                'round': 32,
                'players': [
                    KEI_NISHIKORI,
                    TAYLOR_FRITZ
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    KEI_NISHIKORI: 1.27,
                    TAYLOR_FRITZ: 3.65
                }
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    DOMINIC_THIEM: 1.31,
                    DIEGO_SCHWARTZMAN: 3.45
                }
            },
            {
                'round': 32,
                'players': [
                    NICOLAS_JARRY,
                    ALEXANDER_ZVEREV
                ],
                'score': [(3, 6), (7, 5), (7, 6)],
                'odds': {
                    NICOLAS_JARRY: 4.65,
                    ALEXANDER_ZVEREV: 1.20
                }
            },

            # 2019-04-24
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    NICOLA_KUHN
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.37,
                    NICOLA_KUHN: 3.20
                }
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    MALEK_JAZIRI
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.19,
                    MALEK_JAZIRI: 4.20
                }
            },
            {
                'round': 32,
                'players': [
                    DAVID_FERRER,
                    LUCAS_POUILLE
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DAVID_FERRER: 1.62,
                    LUCAS_POUILLE: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    GRIGOR_DIMITROV,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 2), (6, 7), (6, 3)],
                'odds': {
                    GRIGOR_DIMITROV: 1.65,
                    FERNANDO_VERDASCO: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(6, 4), (6, 7), (6, 1)],
                'odds': {
                    BENOIT_PAIRE: 1.42,
                    PABLO_CARRENO_BUSTA: 2.85
                }
            },
            {
                'round': 32,
                'players': [
                    MACKENZIE_MCDONALD,
                    GILLES_SIMON
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    MACKENZIE_MCDONALD: 2.78,
                    GILLES_SIMON: 1.43
                }
            },
            {
                'round': 32,
                'players': [
                    CRISTIAN_GARIN,
                    DENIS_SHAPOVALOV
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    CRISTIAN_GARIN: 1.65,
                    DENIS_SHAPOVALOV: 2.10
                }
            },
            {
                'round': 32,
                'players': [
                    DANILL_MEDVEDEV,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 3), (2, 6), (6, 1)],
                'odds': {
                    DANILL_MEDVEDEV: 1.44,
                    ALBERT_RAMOS_VINOLAS: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    GUIDO_PELLA: 1.87,
                    KAREN_KHACHANOV: 1.87
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    LEONARDO_MAYER
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.02,
                    LEONARDO_MAYER: 13.84
                }
            },

            # 2019-04-25
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    BENOIT_PAIRE
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 1.61,
                    BENOIT_PAIRE: 2.20
                }
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    CRISTIAN_GARIN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 2.76,
                    CRISTIAN_GARIN: 1.42
                }
            },
            {
                'round': 16,
                'players': [
                    NICOLAS_JARRY,
                    GRIGOR_DIMITROV
                ],
                'score': [(2, 6), (6, 4), (7, 6)],
                'odds': {
                    NICOLAS_JARRY: 2.79,
                    GRIGOR_DIMITROV: 1.43
                }
            },
            {
                'round': 16,
                'players': [
                    DANILL_MEDVEDEV,
                    MACKENZIE_MCDONALD
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    DANILL_MEDVEDEV: 1.17,
                    MACKENZIE_MCDONALD: 4.60
                }
            },
            {
                'round': 16,
                'players': [
                    JAN_LENNARD_STRUFF,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 4), (3, 6), (6, 2)],
                'odds': {
                    JAN_LENNARD_STRUFF: 3.70,
                    STEFANOS_TSITSIPAS: 1.28
                }
            },
            {
                'round': 16,
                'players': [
                    KEI_NISHIKORI,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    KEI_NISHIKORI: 1.63,
                    FELIX_AUGER_ALIASSIME: 2.25
                }
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    JAUME_MUNAR
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    DOMINIC_THIEM: 1.27,
                    JAUME_MUNAR: 3.68
                }
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    DAVID_FERRER
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.14,
                    DAVID_FERRER: 5.00
                }
            },

            # 2019-04-26
            {
                'round': 8,
                'players': [
                    DANILL_MEDVEDEV,
                    NICOLAS_JARRY
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DANILL_MEDVEDEV: 1.29,
                    NICOLAS_JARRY: 3.83
                }
            },
            {
                'round': 8,
                'players': [
                    KEI_NISHIKORI,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    KEI_NISHIKORI: 1.30,
                    ROBERTO_CARBALLES_BAENA: 3.84
                }
            },
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    GUIDO_PELLA
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.36,
                    GUIDO_PELLA: 3.15
                }
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    RAFAEL_NADAL: 1.06,
                    JAN_LENNARD_STRUFF: 8.50
                }
            },

            # 2019-04-27
            {
                'round': 4,
                'players': [
                    DANILL_MEDVEDEV,
                    KEI_NISHIKORI
                ],
                'score': [(6, 4), (3, 6), (7, 5)],
                'odds': {
                    DANILL_MEDVEDEV: 1.95,
                    KEI_NISHIKORI: 1.80
                }
            },
            {
                'round': 4,
                'players': [
                    DOMINIC_THIEM,
                    RAFAEL_NADAL
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 3.20,
                    RAFAEL_NADAL: 1.33
                }
            },

            # 2019-04-28
            {
                'round': 2,
                'players': [
                    DOMINIC_THIEM,
                    DANILL_MEDVEDEV
                ],
                'score': [(6, 4), (6, 0)]
            }
        ]
    },

    {
        'name': 'Hungarian Open',
        'date': '2019-04-22',
        'location': 'Budapest, Hungary',
        'matches': [

            # 2019-04-20
            {
                'round': 512,
                'players': [
                    EGOR_GERASIMOV,
                    FILLIPPO_BALDI
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    EGOR_GERASIMOV: 2.45,
                    FILLIPPO_BALDI: 1.43
                }
            },
            {
                'round': 512,
                'players': [
                    JANNIK_SINNER,
                    LUKAS_ROSOL
                ],
                'score': [(6, 2), (3, 0)],
                'retired': True,
                'odds': {
                    JANNIK_SINNER: 2.31,
                    LUKAS_ROSOL: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    MATTHIAS_BACHINGER,
                    FILIP_HORANSKY
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    MATTHIAS_BACHINGER: 2.44,
                    FILIP_HORANSKY: 1.53
                }
            },
            {
                'round': 512,
                'players': [
                    SERGIY_STAKHOVSKY,
                    DANIEL_BRANDS
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    SERGIY_STAKHOVSKY: 1.53,
                    DANIEL_BRANDS: 2.48
                }
            },
            {
                'round': 512,
                'players': [
                    YANNICK_MADEN,
                    ZSOMBOR_PIROS
                ],
                'score': [(6, 4), (1, 6), (6, 3)],
                'odds': {
                    YANNICK_MADEN: 1.32,
                    ZSOMBOR_PIROS: 3.30
                }
            },
            {
                'round': 512,
                'players': [
                    FILIP_KRAJINOVIC,
                    ROBERTO_MARCORA
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.13,
                    ROBERTO_MARCORA: 5.43
                }
            },
            {
                'round': 512,
                'players': [
                    LLOYD_HARRIS,
                    DANIEL_GIMENO_TRAVER
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    LLOYD_HARRIS: 1.69,
                    DANIEL_GIMENO_TRAVER: 2.05
                }
            },
            {
                'round': 512,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ALESSANDRO_GIANNESSI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.57,
                    ALESSANDRO_GIANNESSI: 2.34
                }
            },

            # 2019-04-21
            {
                'round': 256,
                'players': [
                    YANNICK_MADEN,
                    JANNIK_SINNER
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    YANNICK_MADEN: 1.46,
                    JANNIK_SINNER: 2.45
                }
            },
            {
                'round': 256,
                'players': [
                    FILIP_KRAJINOVIC,
                    EGOR_GERASIMOV
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.15,
                    EGOR_GERASIMOV: 5.10
                }
            },
            {
                'round': 256,
                'players': [
                    LLOYD_HARRIS,
                    MATTHIAS_BACHINGER
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    LLOYD_HARRIS: 1.77,
                    MATTHIAS_BACHINGER: 1.91
                }
            },
            {
                'round': 256,
                'players': [
                    MIOMIR_KECMANOVIC,
                    SERGIY_STAKHOVSKY
                ],
                'score': [(6, 4), (6, 4)],
                # no odds
            },

            # 2019-04-22
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 2), (6, 7), (7, 5)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.44,
                    ANDREAS_SEPPI: 2.52
                }
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    BERNARD_TOMIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ALJAZ_BEDENE: 1.41,
                    BERNARD_TOMIC: 2.63
                }
            },
            {
                'round': 32,
                'players': [
                    RADU_ALBOT,
                    SERGIY_STAKHOVSKY
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    RADU_ALBOT: 1.28,
                    SERGIY_STAKHOVSKY: 3.55
                }
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 1.57,
                    MIKHAIL_KUKUSHKIN: 2.30
                }
            },

            # 2019-04-23
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    EGOR_GERASIMOV
                ],
                'score': [(6, 3), 96, 2],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    ROBIN_HAASE,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 7), (6, 3), (6, 2)],
                'odds': {
                    ROBIN_HAASE: 1.45,
                    THOMAS_FABBIANO: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    PETER_GOJOWCZYK,
                    LLOYD_HARRIS
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    PETER_GOJOWCZYK: 2.27,
                    LLOYD_HARRIS: 1.63
                }
            },
            {
                'round': 32,
                'players': [
                    ATTILA_BALAZS,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ATTILA_BALAZS: 3.35,
                    HUBERT_HURKACZ: 1.32
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    JOHN_MILLMAN: 2.20,
                    MIOMIR_KECMANOVIC: 1.69
                }
            },
            {
                'round': 32,
                'players': [
                    LASLO_DJERE,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    LASLO_DJERE: 1.35,
                    ERNESTS_GULBIS: 2.90
                }
            },

            # 2019-04-24
            {
                'round': 32,
                'players': [
                    JANNIK_SINNER,
                    MATE_VALKUSZ
                ],
                'score': [(6, 2), (0, 6), (6, 4)],
                'odds': {
                    JANNIK_SINNER: 1.83,
                    MATE_VALKUSZ: 1.83
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_CUEVAS,
                    YANNICK_MADEN
                ],
                'score': [(6, 3), (3, 6), (6, 4)],
                'odds': {
                    PABLO_CUEVAS: 1.38,
                    YANNICK_MADEN: 3.05
                }
            },
            {
                'round': 16,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    MATTHIAS_BACHINGER
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.26,
                    MATTHIAS_BACHINGER: 3.65
                }
            },
            {
                'round': 16,
                'players': [
                    ATTILA_BALAZS,
                    JOHN_MILLMAN
                ],
                'score': [(6, 4), (2, 6), (6, 2)],
                'odds': {
                    ATTILA_BALAZS: 2.71,
                    JOHN_MILLMAN: 1.43
                }
            },

            # 2019-04-25
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    ALJAZ_BEDENE
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 1.65,
                    ALJAZ_BEDENE: 2.20
                }
            },
            {
                'round': 16,
                'players': [
                    FILIP_KRAJINOVIC,
                    RADU_ALBOT
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.37,
                    RADU_ALBOT: 3.00
                }
            },
            {
                'round': 16,
                'players': [
                    LASLO_DJERE,
                    JANNIK_SINNER
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    LASLO_DJERE: 1.20,
                    JANNIK_SINNER: 4.55
                }
            },
            {
                'round': 16,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 3), (0, 6), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.42,
                    PETER_GOJOWCZYK: 2.90
                }
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    ROBIN_HAASE
                ],
                'score': [(6, 3), (4, 6), (6, 4)],
                'odds': {
                    BORNA_CORIC: 1.33,
                    ROBIN_HAASE: 3.25
                }
            },
            {
                'round': 16,
                'players': [
                    PABLO_CUEVAS,
                    MARIN_CILIC
                ],
                'score': [(5, 7), (7, 6), (7, 6)],
                'odds': {
                    PABLO_CUEVAS: 2.25,
                    MARIN_CILIC: 1.61
                }
            },

            # 2019-04-26
            {
                'round': 8,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    ATTILA_BALAZS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.55,
                    ATTILA_BALAZS: 2.45
                }
            },
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    PABLO_CUEVAS
                ],
                'score': [(6, 3), (1, 6), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.59,
                    PABLO_CUEVAS: 2.30
                }
            },
            {
                'round': 8,
                'players': [
                    LASLO_DJERE,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(3, 6), (6, 2), (6, 3)],
                'odds': {
                    LASLO_DJERE: 1.61,
                    NIKOLOZ_BASILASHVILI: 2.20
                }
            },
            {
                'round': 8,
                'players': [
                    FILIP_KRAJINOVIC,
                    BORNA_CORIC
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    FILIP_KRAJINOVIC: 2.05,
                    BORNA_CORIC: 1.74
                }
            },

            # 2019-04-27
            {
                'round': 4,
                'players': [
                    FILIP_KRAJINOVIC,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.41,
                    PIERRE_HUGUES_HERBERT: 2.95
                }
            },
            {
                'round': 4,
                'players': [
                    MATTEO_BERRETTINI,
                    LASLO_DJERE
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 1.67,
                    LASLO_DJERE: 2.15
                }
            },

            # 2019-04-28
            {
                'round': 2,
                'players': [
                    MATTEO_BERRETTINI,
                    FILIP_KRAJINOVIC
                ],
                'score': [(4, 6), (6, 3), (6, 1)],
                'odds': {
                    MATTEO_BERRETTINI: 2.10,
                    FILIP_KRAJINOVIC: 1.69
                }
            }
        ]
    },

    {
        'name': 'BMW Open by FWU',
        'date': '2019-04-29',
        'location': 'Munich, Germany',
        'matches': [

            # 2019-04-27
            {
                'round': 512,
                'players': [
                    DENIS_ISTOMIN,
                    CEDRIC_MARCEL_STEBE
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DENIS_ISTOMIN: 1.63,
                    CEDRIC_MARCEL_STEBE: 2.20
                }
            },
            {
                'round': 512,
                'players': [
                    YANNICK_MADEN,
                    THOMAS_FABBIANO
                ],
                'score': [(4, 6), (6, 2), (6, 2)],
                'odds': {
                    YANNICK_MADEN: 1.42,
                    THOMAS_FABBIANO: 2.55
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREY_RUBLEV,
                    MATTHIAS_BACHINGER
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    ANDREY_RUBLEV: 1.25,
                    MATTHIAS_BACHINGER: 3.80
                }
            },
            {
                'round': 512,
                'players': [
                    HENRI_LAAKSONEN,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(4, 6), (6, 1), (6, 4)],
                'odds': {
                    HENRI_LAAKSONEN: 2.25,
                    MIOMIR_KECMANOVIC: 1.61
                }
            },
            {
                'round': 512,
                'players': [
                    LUKAS_ROSOL,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 4), (2, 6), (6, 4)],
                'odds': {
                    LUKAS_ROSOL: 2.61,
                    PETER_GOJOWCZYK: 1.47
                }
            },
            {
                'round': 512,
                'players': [
                    THIAGO_MONTEIRO,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 3), (2, 6), (6, 2)],
                'odds': {
                    THIAGO_MONTEIRO: 3.27,
                    ALBERT_RAMOS_VINOLAS: 1.32
                }
            },
            {
                'round': 512,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    ALEXANDER_ERLER
                ],
                'score': [(3, 6), (7, 6), (7, 5)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 1.05,
                    ALEXANDER_ERLER: 10.00
                }
            },
            {
                'round': 512,
                'players': [
                    LORENZO_SONEGO,
                    YANNICK_HANFMANN
                ],
                'score': [(7, 6), (6, 7), (6, 3)],
                'odds': {
                    LORENZO_SONEGO: 1.23,
                    YANNICK_HANFMANN: 3.85
                }
            },

            # 2019-04-28
            {
                'round': 256,
                'players': [
                    YANNICK_MADEN,
                    LUKAS_ROSOL
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    YANNICK_MADEN: 1.32,
                    LUKAS_ROSOL: 3.12
                }
            },
            {
                'round': 256,
                'players': [
                    THIAGO_MONTEIRO,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 3), (6, 7), (6, 4)],
                'odds': {
                    THIAGO_MONTEIRO: 2.70,
                    ANDREY_RUBLEV: 1.43
                }
            },
            {
                'round': 256,
                'players': [
                    DENIS_ISTOMIN,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(4, 6), (6, 2), (6, 2)],
                'odds': {
                    DENIS_ISTOMIN: 1.67,
                    PRAJNESH_GUNNESWARAN: 1.93
                }
            },
            {
                'round': 256,
                'players': [
                    LORENZO_SONEGO,
                    HENRI_LAAKSONEN
                ],
                'score': [(6, 0), (5, 7), (7, 6)],
                'odds': {
                    LORENZO_SONEGO: 1.38,
                    HENRI_LAAKSONEN: 2.73
                }
            },

            # 2019-04-29
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    UGO_HUMBERT,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    TARO_DANIEL: 1.65,
                    UGO_HUMBERT: 2.15
                }
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    LORENZO_SONEGO
                ],
                'score': [(7, 5), (4, 6), (7, 6)],
                'odds': {
                    MARTON_FUCSOVICS: 1.91,
                    LORENZO_SONEGO: 1.80
                }
            },

            # 2019-04-30
            {
                'round': 32,
                'players': [
                    THIAGO_MONTEIRO,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    THIAGO_MONTEIRO: 3.50,
                    JAN_LENNARD_STRUFF: 1.29
                }
            },
            {
                'round': 32,
                'players': [
                    RUDOLF_MOLLEKER,
                    MARIUS_COPIL
                ],
                'score': [(7, 6), (4, 6), (6, 4)],
                'odds': {
                    RUDOLF_MOLLEKER: 1.77,
                    MARIUS_COPIL: 1.97
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    MAXIMILIAN_MARTERER
                ],
                'score': [(6, 2), (4, 6), (6, 2)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.50,
                    MAXIMILIAN_MARTERER: 2.53
                }
            },
            {
                'round': 32,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.32,
                    ANDREAS_SEPPI: 3.30
                }
            },
            {
                'round': 32,
                'players': [
                    MARTIN_KLIZAN,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    MARTIN_KLIZAN: 1.50,
                    ERNESTS_GULBIS: 2.54
                }
            },
            {
                'round': 32,
                'players': [
                    CRISTIAN_GARIN,
                    YANNICK_MADEN
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    CRISTIAN_GARIN: 1.50,
                    YANNICK_MADEN: 2.55
                }
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    DENIS_ISTOMIN
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.33,
                    DENIS_ISTOMIN: 3.10
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    GUIDO_PELLA: 1.11,
                    MISCHA_ZVEREV: 7.04
                }
            },
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    BENOIT_PAIRE
                ],
                'score': [(6, 4), (1, 6), (6, 1)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.60,
                    BENOIT_PAIRE: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    DENIS_KUDLA,
                    KYLE_EDMUND
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    DENIS_KUDLA: 6.00,
                    KYLE_EDMUND: 1.11
                }
            },

            # 2019-05-01
            {
                'round': 16,
                'players': [
                    MARTON_FUCSOVICS,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 7), (6, 4), (6, 3)],
                'odds': {
                    MARTON_FUCSOVICS: 1.57,
                    THIAGO_MONTEIRO: 2.30
                }
            },
            {
                'round': 16,
                'players': [
                    CRISTIAN_GARIN,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    CRISTIAN_GARIN: 2.02,
                    DIEGO_SCHWARTZMAN: 1.74
                }
            },
            {
                'round': 16,
                'players': [
                    MARCO_CECCHINATO,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    MARCO_CECCHINATO: 1.65,
                    MARTIN_KLIZAN: 2.31
                }
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.18,
                    JUAN_IGNACIO_LONDERO: 5.15
                }
            },

            # 2019-05-02
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    DENIS_KUDLA
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.26,
                    DENIS_KUDLA: 3.85
                }
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    TARO_DANIEL
                ],
                'score': [(6, 1), (6, 7), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 1.17,
                    TARO_DANIEL: 5.00
                }
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    RUDOLF_MOLLEKER
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.22,
                    RUDOLF_MOLLEKER: 4.10
                }
            },
            {
                'round': 16,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    KAREN_KHACHANOV
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.50,
                    KAREN_KHACHANOV: 2.35
                }
            },

            # 2019-05-03
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(4, 6), (7, 5), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 2.20,
                    PHILIPP_KOHLSCHREIBER: 1.65
                }
            },
            {
                'round': 8,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    GUIDO_PELLA
                ],
                'score': [(4, 6), (6, 4), (6, 0)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.79,
                    GUIDO_PELLA: 1.95
                }
            },
            {
                'round': 8,
                'players': [
                    MARCO_CECCHINATO,
                    MARTON_FUCSOVICS
                ],
                'score': [(1, 6), (7, 5), (7, 5)],
                'odds': {
                    MARCO_CECCHINATO: 1.57,
                    MARTON_FUCSOVICS: 2.41
                }
            },
            {
                'round': 8,
                'players': [
                    CRISTIAN_GARIN,
                    ALEXANDER_ZVEREV
                ],
                'score': [(6, 4), (5, 7), (7, 5)],
                'odds': {
                    CRISTIAN_GARIN: 3.28,
                    ALEXANDER_ZVEREV: 1.37
                }
            },

            # 2019-05-04
            {
                'round': 4,
                'players': [
                    CRISTIAN_GARIN,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    CRISTIAN_GARIN: 1.92,
                    MARCO_CECCHINATO: 1.83
                }
            },

            # 2019-05-05
            {
                'round': 4,
                'players': [
                    MATTEO_BERRETTINI,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 2.13,
                    ROBERTO_BAUTISTA_AGUT: 1.69
                }
            },
            {
                'round': 2,
                'players': [
                    CRISTIAN_GARIN,
                    MATTEO_BERRETTINI
                ],
                'score': [(6, 1), (3, 6), (7, 6)],
                'odds': {
                    CRISTIAN_GARIN: 1.86,
                    MATTEO_BERRETTINI: 1.95
                }
            },
        ]
    },

    {
        'name': 'Millennium Estoril Open',
        'date': '2019-04-29',
        'location': 'Estoril, Portugal',
        'matches': [

            # 2019-04-27
            {
                'round': 512,
                'players': [
                    SALVATORE_CARUSO,
                    PEDRO_MARTINEZ
                ],
                'score': [(6, 3), (5, 7), (7, 6)],
                'odds': {
                    SALVATORE_CARUSO: 1.83,
                    PEDRO_MARTINEZ: 1.83
                }
            },
            {
                'round': 512,
                'players': [
                    SIMONE_BOLELLI,
                    EGOR_GERASIMOV
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    SIMONE_BOLELLI: 1.41,
                    EGOR_GERASIMOV: 2.66
                }
            },
            {
                'round': 512,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    BJORN_FRATANGELO
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.38,
                    BJORN_FRATANGELO: 2.70
                }
            },
            {
                'round': 512,
                'players': [
                    FILLIPPO_BALDI,
                    JOZEF_KOVALIK
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    FILLIPPO_BALDI: 2.40,
                    JOZEF_KOVALIK: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    GASTAO_ELIAS
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    ALEXEI_POPYRIN: 1.58,
                    GASTAO_ELIAS: 2.25
                }
            },
            {
                'round': 512,
                'players': [
                    JOAO_DOMINGUES,
                    ELIAS_YMER
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    JOAO_DOMINGUES: 1.94,
                    ELIAS_YMER: 1.74
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_EVANS,
                    LORENZO_GUISTINO
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    DANIEL_EVANS: 1.87,
                    LORENZO_GUISTINO: 1.80
                }
            },
            {
                'round': 512,
                'players': [
                    PABLO_CUEVAS,
                    DANIEL_BRANDS
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    PABLO_CUEVAS: 4.65,
                    DANIEL_BRANDS: 4.65
                }
            },

            # 2019-04-28
            {
                'round': 256,
                'players': [
                    JOAO_DOMINGUES,
                    FILLIPPO_BALDI
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    JOAO_DOMINGUES: 1.40,
                    FILLIPPO_BALDI: 2.75
                }
            },
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    SIMONE_BOLELLI
                ],
                'score': [(2, 6), (6, 3), (6, 4)],
                'odds': {
                    ALEXEI_POPYRIN: 2.21,
                    SIMONE_BOLELLI: 1.59
                }
            },
            {
                'round': 256,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    DANIEL_EVANS
                ],
                'score': [(3, 6), (6, 1), (6, 4)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.46,
                    DANIEL_EVANS: 2.40
                }
            },
            {
                'round': 256,
                'players': [
                    SALVATORE_CARUSO,
                    PABLO_CUEVAS
                ],
                'score': [(6, 4), (5, 7), (6, 4)],
                # no odds
            },

            # 2019-04-29
            {
                'round': 32,
                'players': [
                    REILLY_OPELKA,
                    PEDRO_SOUSA
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    REILLY_OPELKA: 2.15,
                    PEDRO_SOUSA: 1.71
                }
            },
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    MACKENZIE_MCDONALD
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.71,
                    MACKENZIE_MCDONALD: 2.10
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_ANDREOZZI,
                    HUGO_DELLIEN
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    GUIDO_ANDREOZZI: 1.91,
                    HUGO_DELLIEN: 1.87
                }
            },
            {
                'round': 32,
                'players': [
                    JOAO_DOMINGUES,
                    ALEX_DE_MINAUR
                ],
                'score': [(6, 2), (2, 6), (6, 2)],
                'odds': {
                    JOAO_DOMINGUES: 2.00,
                    ALEX_DE_MINAUR: 1.74
                }
            },

            # 2019-04-30
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 4), (2, 6), (6, 2)],
                'odds': {
                    JOAO_SOUSA: 1.45,
                    ALEXEI_POPYRIN: 2.55
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    BERNARD_TOMIC
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    JOHN_MILLMAN: 1.39,
                    BERNARD_TOMIC: 2.85
                }
            },
            {
                'round': 32,
                'players': [
                    MALEK_JAZIRI,
                    NICOLAS_JARRY
                ],
                'score': [(6, 3), (3, 6), (6, 4)],
                'odds': {
                    MALEK_JAZIRI: 3.20,
                    NICOLAS_JARRY: 1.38
                }
            },
            {
                'round': 32,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    TAYLOR_FRITZ
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.67,
                    TAYLOR_FRITZ: 2.00
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_CUEVAS,
                    SALVATORE_CARUSO
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 3.25,
                    SALVATORE_CARUSO: 3.25
                }
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    FRANCES_TIAFOE: 1.67,
                    MIKHAIL_KUKUSHKIN: 2.05
                }
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(5, 7), (6, 1), (6, 2)],
                'odds': {
                    JEREMY_CHARDY: 2.05,
                    PABLO_CARRENO_BUSTA: 1.76
                }
            },
            {
                'round': 32,
                'players': [
                    LEONARDO_MAYER,
                    DUSAN_LAJOVIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    LEONARDO_MAYER: 2.03,
                    DUSAN_LAJOVIC: 1.71
                }
            },

            # 2019-05-01
            {
                'round': 16,
                'players': [
                    JOAO_DOMINGUES,
                    JOHN_MILLMAN
                ],
                'score': [(6, 3), (2, 1)],
                'retired': True,
                'odds': {
                    JOAO_DOMINGUES: 2.50,
                    JOHN_MILLMAN: 1.53
                }
            },
            {
                'round': 16,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    JEREMY_CHARDY
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.95,
                    JEREMY_CHARDY: 1.74
                }
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    REILLY_OPELKA
                ],
                'score': [(3, 6), (6, 3), (6, 0)],
                'odds': {
                    GAEL_MONFILS: 1.48,
                    REILLY_OPELKA: 2.60
                }
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.15,
                    GUIDO_ANDREOZZI: 5.00
                }
            },

            # 2019-05-02
            {
                'round': 16,
                'players': [
                    MALEK_JAZIRI,
                    LEONARDO_MAYER
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    MALEK_JAZIRI: 3.35,
                    LEONARDO_MAYER: 1.30
                }
            },
            {
                'round': 16,
                'players': [
                    PABLO_CUEVAS,
                    FILLIPPO_BALDI
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    PABLO_CUEVAS: 1.18,
                    FILLIPPO_BALDI: 4.51
                }
            },
            {
                'round': 16,
                'players': [
                    FRANCES_TIAFOE,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(2, 6), (6, 3), (7, 6)],
                'odds': {
                    FRANCES_TIAFOE: 1.63,
                    YOSHIHITO_NISHIOKA: 2.25
                }
            },
            {
                'round': 16,
                'players': [
                    DAVID_GOFFIN,
                    JOAO_SOUSA
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.48,
                    JOAO_SOUSA: 2.60
                }
            },

            # 2019-05-03
            {
                'round': 8,
                'players': [
                    PABLO_CUEVAS,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 0), (6, 7), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 1.57,
                    FRANCES_TIAFOE: 2.39
                }
            },
            {
                'round': 8,
                'players': [
                    DAVID_GOFFIN,
                    MALEK_JAZIRI
                ],
                'score': [(4, 6), (7, 6), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.20,
                    MALEK_JAZIRI: 4.60
                }
            },
            {
                'round': 8,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    GAEL_MONFILS
                ],
                'score': [(6, 7), (7, 5), (6, 4)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.63,
                    GAEL_MONFILS: 1.41
                }
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    JOAO_DOMINGUES
                ],
                'score': [(7, 6), (6, 4)],
                # no odds
            },

            # 2019-05-04
            {
                'round': 4,
                'players': [
                    PABLO_CUEVAS,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(3, 6), (6, 2), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 1.51,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.45
                }
            },
            {
                'round': 4,
                'players': [
                    STEFANOS_TSITSIPAS,
                    DAVID_GOFFIN
                ],
                'score': [(3, 6), (6, 4), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.53,
                    DAVID_GOFFIN: 2.45
                }
            },

            # 2019-095-05
            {
                'round': 2,
                'players': [
                    STEFANOS_TSITSIPAS,
                    PABLO_CUEVAS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.36,
                    PABLO_CUEVAS: 3.15
                }
            }

        ]
    },

    {
        'name': 'Mutua Madrid Open',
        'date': '2019-05-05',
        'location': 'Madrid, Spain',
        'matches': [

            # 2019-05-04
            {
                'round': 512,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    TARO_DANIEL
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.35,
                    TARO_DANIEL: 2.98
                }
            },
            {
                'round': 512,
                'players': [
                    MARIUS_COPIL,
                    NICOLAS_JARRY
                ],
                'score': [(5, 7), (6, 4), (7, 6)],
                'odds': {
                    MARIUS_COPIL: 2.95,
                    NICOLAS_JARRY: 1.33
                }
            },
            {
                'round': 512,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    UGO_HUMBERT
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.25,
                    UGO_HUMBERT: 3.75
                }
            },
            {
                'round': 512,
                'players': [
                    ROBIN_HAASE,
                    BERNARD_TOMIC
                ],
                'score': [(6, 7), (6, 2), (7, 5)],
                'odds': {
                    ROBIN_HAASE: 1.32,
                    BERNARD_TOMIC: 3.07
                }
            },
            {
                'round': 512,
                'players': [
                    HUGO_DELLIEN,
                    LEONARDO_MAYER
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    HUGO_DELLIEN: 2.75,
                    LEONARDO_MAYER: 1.31
                }
            },
            {
                'round': 512,
                'players': [
                    MARTIN_KLIZAN,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    MARTIN_KLIZAN: 1.38,
                    ERNESTS_GULBIS: 2.70
                }
            },
            {
                'round': 512,
                'players': [
                    REILLY_OPELKA,
                    MISCHA_ZVEREV
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 1.21,
                    MISCHA_ZVEREV: 3.65
                }
            },
            {
                'round': 512,
                'players': [
                    TAYLOR_FRITZ,
                    NICOLA_KUHN
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    TAYLOR_FRITZ: 1.65,
                    NICOLA_KUHN: 2.05
                }
            },
            {
                'round': 512,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    MACKENZIE_MCDONALD
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.38,
                    MACKENZIE_MCDONALD: 2.80
                }
            },
            {
                'round': 512,
                'players': [
                    ADRIAN_MANNARINO,
                    JORGE_PLANS
                ],
                'score': [(6, 4), (6, 7), (7, 5)],
                'odds': {
                    ADRIAN_MANNARINO: 1.01,
                    JORGE_PLANS: 19.85
                }
            },
            {
                'round': 512,
                'players': [
                    GUIDO_ANDREOZZI,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 3), (1, 6), (6, 3)],
                'odds': {
                    GUIDO_ANDREOZZI: 1.37,
                    DAMIR_DZUMHUR: 2.88
                }
            },
            {
                'round': 512,
                'players': [
                    HUBERT_HURKACZ,
                    MARCEL_GRANOLLERS
                ],
                'score': [(6, 0), (6, 2)],
                'odds': {
                    HUBERT_HURKACZ: 1.48,
                    MARCEL_GRANOLLERS: 2.50
                }
            },
            {
                'round': 512,
                'players': [
                    CASPER_RUUD,
                    BENOIT_PAIRE
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    CASPER_RUUD: 2.04,
                    BENOIT_PAIRE: 1.59
                }
            },
            {
                'round': 512,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    DENIS_KUDLA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.27,
                    DENIS_KUDLA: 3.40
                }
            },

            # 2019-05-05
            {
                'round': 256,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    CASPER_RUUD
                ],
                'score': [(2, 6), (7, 6), (6, 1)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.00,
                    CASPER_RUUD: 1.71
                }
            },
            {
                'round': 256,
                'players': [
                    HUGO_DELLIEN,
                    GUIDO_ANDREOZZI
                ],
                'score': [(3, 6), (6, 4), (6, 2)],
                'odds': {
                    HUGO_DELLIEN: 2.15,
                    GUIDO_ANDREOZZI: 1.63
                }
            },
            {
                'round': 256,
                'players': [
                    REILLY_OPELKA,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(7, 6), (5, 7), (6, 2)],
                'odds': {
                    REILLY_OPELKA: 1.99,
                    JUAN_IGNACIO_LONDERO: 1.61
                }
            },
            {
                'round': 256,
                'players': [
                    TAYLOR_FRITZ,
                    MARIUS_COPIL
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    TAYLOR_FRITZ: 1.41,
                    MARIUS_COPIL: 2.68
                }
            },
            {
                'round': 256,
                'players': [
                    MARTIN_KLIZAN,
                    ANDRIAN_MANNARINO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    MARTIN_KLIZAN: 1.33,
                    ANDRIAN_MANNARINO: 3.00
                }
            },
            {
                'round': 256,
                'players': [
                    HUBERT_HURKACZ,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 1.67,
                    ROBERTO_CARBALLES_BAENA: 2.05
                }
            },
            {
                'round': 256,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    ROBIN_HAASE
                ],
                'score': [(5, 7), (6, 3), (7, 6)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.67,
                    ROBIN_HAASE: 2.10
                }
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    NICK_KYRGIOS
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.99,
                    NICK_KYRGIOS: 1.83
                }
            },
            {
                'round': 64,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    DENIS_SHAPOVALOV
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.69,
                    DENIS_SHAPOVALOV: 2.14
                }
            },

            # 2019-05-06
            {
                'round': 64,
                'players': [
                    FERNANDO_VERDASCO,
                    RADU_ALBOT
                ],
                'score': [(6, 2), (3, 6), (6, 1)],
                'odds': {
                    FERNANDO_VERDASCO: 1.51,
                    RADU_ALBOT: 2.40
                }
            },
            {
                'round': 64,
                'players': [
                    REILLY_OPELKA,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    REILLY_OPELKA: 2.05,
                    PABLO_CARRENO_BUSTA: 1.74
                }
            },
            {
                'round': 64,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.34,
                    MIKHAIL_KUKUSHKIN: 3.18
                }
            },
            {
                'round': 64,
                'players': [
                    RICHARD_GASQUET,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    RICHARD_GASQUET: 2.65,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.36
                }
            },
            {
                'round': 64,
                'players': [
                    TAYLOR_FRITZ,
                    GRIGOR_DIMITROV
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    TAYLOR_FRITZ: 2.70,
                    GRIGOR_DIMITROV: 1.33
                }
            },
            {
                'round': 64,
                'players': [
                    LASLO_DJERE,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    LASLO_DJERE: 2.10,
                    DUSAN_LAJOVIC: 1.67
                }
            },
            {
                'round': 64,
                'players': [
                    GAEL_MONFILS,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    GAEL_MONFILS: 1.28,
                    ANDREAS_SEPPI: 3.80
                }
            },
            {
                'round': 64,
                'players': [
                    FRANCES_TIAFOE,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    FRANCES_TIAFOE: 1.91,
                    NIKOLOZ_BASILASHVILI: 1.80
                }
            },
            {
                'round': 64,
                'players': [
                    KAREN_KHACHANOV,
                    JAUME_MUNAR
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 1.98,
                    JAUME_MUNAR: 1.80
                }
            },
            {
                'round': 64,
                'players': [
                    MARIN_CILIC,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 4), (2, 6), (7, 6)],
                'odds': {
                    MARIN_CILIC: 1.53,
                    MARTIN_KLIZAN: 2.40
                }
            },

            # 2019-05-07
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    STAN_WAWRINKA: 1.44,
                    PIERRE_HUGUES_HERBERT: 2.66
                }
            },
            {
                'round': 64,
                'players': [
                    JOHN_MILLMAN,
                    STEVE_JOHNSON
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JOHN_MILLMAN: 1.69,
                    STEVE_JOHNSON: 2.12
                }
            },
            {
                'round': 64,
                'players': [
                    ADRIAN_MANNARINO,
                    JOAO_SOUSA
                ],
                'score': [(7, 5), (5, 7), (6, 1)],
                'odds': {
                    ADRIAN_MANNARINO: 2.72,
                    JOAO_SOUSA: 1.45
                }
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    ALEX_DE_MINAUR
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 1.35,
                    ALEX_DE_MINAUR: 3.19
                }
            },
            {
                'round': 64,
                'players': [
                    MARTON_FUCSOVICS,
                    DAVID_GOFFIN
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    MARTON_FUCSOVICS: 2.30,
                    DAVID_GOFFIN: 1.59
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_FERRER,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(6, 4), (4, 6), (6, 4)],
                'odds': {
                    DAVID_FERRER: 2.20,
                    ROBERTO_BAUTISTA_AGUT: 1.67
                }
            },
            {
                'round': 64,
                'players': [
                    HUGO_DELLIEN,
                    GILLES_SIMON
                ],
                'score': [(4, 6), (6, 1), (7, 6)],
                'odds': {
                    HUGO_DELLIEN: 2.30,
                    GILLES_SIMON: 1.61
                }
            },
            {
                'round': 64,
                'players': [
                    JEREMY_CHARDY,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 2), (4, 6), (7, 5)],
                'odds': {
                    JEREMY_CHARDY: 2.65,
                    ALBERT_RAMOS_VINOLAS: 1.43
                }
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 0), (4, 6), (6, 1)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.93,
                    MARCO_CECCHINATO: 1.84
                }
            },
            {
                'round': 64,
                'players': [
                    LUCAS_POUILLE,
                    BORNA_CORIC
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    LUCAS_POUILLE: 2.85,
                    BORNA_CORIC: 1.42
                }
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    DANILL_MEDVEDEV
                ],
                'score': [(6, 2), (1, 6), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 2.40,
                    DANILL_MEDVEDEV: 1.56
                }
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    KYLE_EDMUND
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    FABIO_FOGNINI: 1.80,
                    KYLE_EDMUND: 1.91
                }
            },
            {
                'round': 32,
                'players': [
                    MARIN_CILIC,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    MARIN_CILIC: 1.87,
                    JAN_LENNARD_STRUFF: 1.83
                }
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    REILLY_OPELKA
                ],
                'score': [(6, 7), (6, 3), (1, 0)],
                'retired': True,
                'odds': {
                    DOMINIC_THIEM: 1.13,
                    REILLY_OPELKA: 5.50
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    RICHARD_GASQUET
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.08,
                    RICHARD_GASQUET: 6.75
                }
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.09,
                    TAYLOR_FRITZ: 6.50
                }
            },

            # 2019-05-08
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    GUIDO_PELLA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STAN_WAWRINKA: 1.65,
                    GUIDO_PELLA: 2.25
                }
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    FRANCES_TIAFOE: 2.60,
                    PHILIPP_KOHLSCHREIBER: 1.50
                }
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    LUCAS_POUILLE
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    HUBERT_HURKACZ: 1.70,
                    LUCAS_POUILLE: 2.10
                }
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    JEREMY_CHARDY: 3.11,
                    DIEGO_SCHWARTZMAN: 1.34
                }
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    MARTON_FUCSOVICS
                ],
                'score': [(1, 6), (6, 4), (6, 2)],
                'odds': {
                    GAEL_MONFILS: 1.53,
                    MARTON_FUCSOVICS: 2.50
                }
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 7), (6, 1), (7, 5)],
                'odds': {
                    FERNANDO_VERDASCO: 2.15,
                    KAREN_KHACHANOV: 1.69
                }
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    JOHN_MILLMAN
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    FABIO_FOGNINI: 1.36,
                    JOHN_MILLMAN: 3.09
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    ANDRIAN_MANNARINO
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.11,
                    ANDRIAN_MANNARINO: 6.00
                }
            },
            {
                'round': 32,
                'players': [
                    LASLO_DJERE,
                    JUAN_MARTIN_DEL_POTRO
                ],
                'score': [(6, 3), (2, 6), (7, 5)],
                'odds': {
                    LASLO_DJERE: 2.00,
                    JUAN_MARTIN_DEL_POTRO: 1.79
                }
            },
            {
                'round': 32,
                'players': [
                    KEI_NISHIKORI,
                    HUGO_DELLIEN
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    KEI_NISHIKORI: 1.14,
                    HUGO_DELLIEN: 5.50
                }
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    DAVID_FERRER
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.33,
                    DAVID_FERRER: 3.43
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.16,
                    FELIX_AUGER_ALIASSIME: 5.25
                }
            },

            # 2019-05-09
            {
                'round': 16,
                'players': [
                    MARIN_CILIC,
                    LASLO_DJERE
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    MARIN_CILIC: 1.63,
                    LASLO_DJERE: 2.15
                }
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.33,
                    FERNANDO_VERDASCO: 3.15
                }
            },
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    KEI_NISHIKORI
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    STAN_WAWRINKA: 1.71,
                    KEI_NISHIKORI: 2.05
                }
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    FABIO_FOGNINI
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    DOMINIC_THIEM: 1.34,
                    FABIO_FOGNINI: 3.22
                }
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    GAEL_MONFILS
                ],
                'score': [(6, 0), (4, 6), (7, 6)],
                'odds': {
                    ROGER_FEDERER: 1.29,
                    GAEL_MONFILS: 3.55
                }
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    HUBERT_HURKACZ
                ],
                'score': [(3, 6), (6, 4), (6, 4)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.44,
                    HUBERT_HURKACZ: 2.95
                }
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.05,
                    FRANCES_TIAFOE: 9.00
                }
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    JEREMY_CHARDY
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.07,
                    JEREMY_CHARDY: 7.00
                }
            },

            # 2019-05-10
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    ROGER_FEDERER
                ],
                'score': [(3, 6), (7, 6), (6, 4)],
                'odds': {
                    DOMINIC_THIEM: 1.43,
                    ROGER_FEDERER: 2.80
                }
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    ALEXANDER_ZVEREV
                ],
                'score': [(7, 5), (3, 6), (6, 2)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.77,
                    ALEXANDER_ZVEREV: 2.10
                }
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    STAN_WAWRINKA
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.20,
                    STAN_WAWRINKA: 4.60
                }
            },
            {
                'round': 8,
                'players': [
                    NOVAK_DJOKOVIC,
                    MARIN_CILIC
                ],
                'score': [],
                'wo': True,
                'odds': {
                    NOVAK_DJOKOVIC: 1.14,
                    MARIN_CILIC: 5.50
                }
            },

            # 2019-05-11
            {
                'round': 4,
                'players': [
                    STEFANOS_TSITSIPAS,
                    RAFAEL_NADAL
                ],
                'score': [(6, 4), (2, 6), (6, 3)],
                'odds': {
                    STEFANOS_TSITSIPAS: 5.50,
                    RAFAEL_NADAL: 1.12
                }
            },
            {
                'round': 4,
                'players': [
                    NOVAK_DJOKOVIC,
                    DOMINIC_THIEM
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.74,
                    DOMINIC_THIEM: 1.95
                }
            },

            # 2019-05-12
            {
                'round': 2,
                'players': [
                    NOVAK_DJOKOVIC,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.43,
                    STEFANOS_TSITSIPAS: 2.80
                }
            }
        ]
    },

    {
        'name': 'Internazionali BNL d\'Italia',
        'date': '2019-05-12',
        'location': 'Rome, Italy',
        'matches': [

            # 2019-05-11
            {
                'round': 512,
                'players': [
                    BERNARD_TOMIC,
                    RICCARDO_BALZERANI
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    BERNARD_TOMIC: 1.19,
                    RICCARDO_BALZERANI: 4.43
                }
            },
            {
                'round': 512,
                'players': [
                    NICOLAS_JARRY,
                    MARIUS_COPIL
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    NICOLAS_JARRY: 1.33,
                    MARIUS_COPIL: 3.20
                }
            },
            {
                'round': 512,
                'players': [
                    CASPER_RUUD,
                    LORENZO_MUSETTI
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    CASPER_RUUD: 1.15,
                    LORENZO_MUSETTI: 5.18
                }
            },
            {
                'round': 512,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    DENIS_KUDLA
                ],
                'score': [(7, 6), (4, 6), (6, 3)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.31,
                    DENIS_KUDLA: 3.35
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_EVANS,
                    ROBIN_HAASE
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    DANIEL_EVANS: 2.63,
                    ROBIN_HAASE: 1.37
                }
            },
            {
                'round': 512,
                'players': [
                    FILLIPPO_BALDI,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    FILLIPPO_BALDI: 3.94,
                    MARTIN_KLIZAN: 1.22
                }
            },
            {
                'round': 512,
                'players': [
                    REILLY_OPELKA,
                    ERNESTS_GULBIS
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    REILLY_OPELKA: 1.71,
                    ERNESTS_GULBIS: 1.90
                }
            },
            {
                'round': 512,
                'players': [
                    TAYLOR_FRITZ,
                    JACOPO_BERRETTINI
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    TAYLOR_FRITZ: 1.09,
                    JACOPO_BERRETTINI: 6.25
                }
            },
            {
                'round': 512,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    JAUME_MUNAR
                ],
                'score': [(6, 7), (6, 3), (7, 6)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.15,
                    JAUME_MUNAR: 1.61
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    TARO_DANIEL
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    DAMIR_DZUMHUR: 2.40,
                    TARO_DANIEL: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    MIOMIR_KECMANOVIC,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 3), (1, 6), (6, 4)],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.70,
                    HUBERT_HURKACZ: 1.43
                }
            },
            {
                'round': 512,
                'players': [
                    CAMERON_NORRIE,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 7), (7, 5), (6, 3)],
                'odds': {
                    CAMERON_NORRIE: 1.51,
                    PETER_GOJOWCZYK: 2.35
                }
            },
            {
                'round': 512,
                'players': [
                    BENOIT_PAIRE,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    BENOIT_PAIRE: 1.15,
                    BRADLEY_KLAHN: 5.20
                }
            },
            {
                'round': 512,
                'players': [
                    DUSAN_LAJOVIC,
                    ALJAZ_BEDENE
                ],
                'score': [(7, 6), (6, 7), (6, 1)],
                'odds': {
                    DUSAN_LAJOVIC: 1.56,
                    ALJAZ_BEDENE: 2.15
                }
            },

            # 2019-05-12
            {
                'round': 256,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    BERNARD_TOMIC
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.25,
                    BERNARD_TOMIC: 3.34
                }
            },
            {
                'round': 256,
                'players': [
                    CASPER_RUUD,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    CASPER_RUUD: 1.36,
                    MIOMIR_KECMANOVIC: 2.52
                }
            },
            {
                'round': 256,
                'players': [
                    TAYLOR_FRITZ,
                    FILLIPPO_BALDI
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    TAYLOR_FRITZ: 1.41,
                    FILLIPPO_BALDI: 2.75
                }
            },
            {
                'round': 256,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 4), (4, 6), (6, 3)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.91,
                    DAMIR_DZUMHUR: 1.71
                }
            },
            {
                'round': 256,
                'players': [
                    CAMERON_NORRIE,
                    NICOLAS_JARRY
                ],
                'score': [(6, 3), (4, 6), (7, 6)],
                'odds': {
                    CAMERON_NORRIE: 2.60,
                    NICOLAS_JARRY: 1.39
                }
            },
            {
                'round': 256,
                'players': [
                    BENOIT_PAIRE,
                    REILLY_OPELKA
                ],
                'score': [(5, 7), (6, 2), (7, 6)],
                'odds': {
                    BENOIT_PAIRE: 1.54,
                    REILLY_OPELKA: 2.29
                }
            },
            {
                'round': 256,
                'players': [
                    DANIEL_EVANS,
                    DUSAN_LAJOVIC
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    DANIEL_EVANS: 2.90,
                    DUSAN_LAJOVIC: 1.27
                }
            },
            {
                'round': 64,
                'players': [
                    JANNIK_SINNER,
                    STEVE_JOHNSON
                ],
                'score': [(1, 6), (6, 1), (7, 5)],
                'odds': {
                    JANNIK_SINNER: 2.30,
                    STEVE_JOHNSON: 1.65
                }
            },
            {
                'round': 64,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    GILLES_SIMON
                ],
                'score': [(6, 2), (3, 6), (6, 3)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.33,
                    GILLES_SIMON: 3.26
                }
            },
            {
                'round': 64,
                'players': [
                    MATTEO_BERRETTINI,
                    LUCAS_POUILLE
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 1.38,
                    LUCAS_POUILLE: 3.15
                }
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 1), (3, 6), (6, 1)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.23,
                    ANDREAS_SEPPI: 4.17
                }
            },
            {
                'round': 64,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.60,
                    MARTON_FUCSOVICS: 1.52
                }
            },

            # 2019-05-13
            {
                'round': 64,
                'players': [
                    FERNANDO_VERDASCO,
                    KYLE_EDMUND
                ],
                'score': [(4, 6), (6, 4), (6, 2)],
                'odds': {
                    FERNANDO_VERDASCO: 2.20,
                    KYLE_EDMUND: 1.67
                }
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.67,
                    PABLO_CARRENO_BUSTA: 2.19
                }
            },
            {
                'round': 64,
                'players': [
                    CASPER_RUUD,
                    DANIEL_EVANS
                ],
                'score': [(7, 5), (0, 6), (6, 3)],
                'odds': {
                    CASPER_RUUD: 1.42,
                    DANIEL_EVANS: 2.88
                }
            },
            {
                'round': 64,
                'players': [
                    CAMERON_NORRIE,
                    JOHN_MILLMAN
                ],
                'score': [(3, 6), (6, 3), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 1.87,
                    JOHN_MILLMAN: 1.89
                }
            },
            {
                'round': 64,
                'players': [
                    LASLO_DJERE,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    LASLO_DJERE: 1.37,
                    MIKHAIL_KUKUSHKIN: 2.90
                }
            },
            {
                'round': 64,
                'players': [
                    MARCO_CECCHINATO,
                    ALEX_DE_MINAUR
                ],
                'score': [(4, 6), (6, 3), (6, 1)],
                'odds': {
                    MARCO_CECCHINATO: 1.25,
                    ALEX_DE_MINAUR: 4.04
                }
            },
            {
                'round': 64,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    GAEL_MONFILS
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 3.30,
                    GAEL_MONFILS: 1.36
                }
            },
            {
                'round': 64,
                'players': [
                    BORNA_CORIC,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    BORNA_CORIC: 2.00,
                    FELIX_AUGER_ALIASSIME: 1.80
                }
            },
            {
                'round': 64,
                'players': [
                    KAREN_KHACHANOV,
                    LORENZO_SONEGO
                ],
                'score': [(6, 3), (6, 7), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 1.83,
                    LORENZO_SONEGO: 2.00
                }
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.36,
                    JO_WILFRIED_TSONGA: 3.35
                }
            },

            # 2019-05-14
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    GRIGOR_DIMITROV
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.14,
                    GRIGOR_DIMITROV: 1.71
                }
            },
            {
                'round': 64,
                'players': [
                    JOAO_SOUSA,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 3), (6, 7), (7, 6)],
                'odds': {
                    JOAO_SOUSA: 2.70,
                    FRANCES_TIAFOE: 1.45
                }
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.43,
                    YOSHIHITO_NISHIOKA: 2.84
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    STAN_WAWRINKA
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 2.60,
                    STAN_WAWRINKA: 1.49
                }
            },
            {
                'round': 64,
                'players': [
                    TAYLOR_FRITZ,
                    GUIDO_PELLA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 3.15,
                    GUIDO_PELLA: 1.38
                }
            },
            {
                'round': 64,
                'players': [
                    JEREMY_CHARDY,
                    RICHARD_GASQUET
                ],
                'score': [(6, 1), (4, 6), (6, 3)],
                # no odds
            },
            {
                'round': 64,
                'players': [
                    RADU_ALBOT,
                    BENOIT_PAIRE
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    RADU_ALBOT: 2.79,
                    BENOIT_PAIRE: 1.44
                }
            },
            {
                'round': 64,
                'players': [
                    NICK_KYRGIOS,
                    DANILL_MEDVEDEV
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    NICK_KYRGIOS: 2.99,
                    DANILL_MEDVEDEV: 1.39
                }
            },
            {
                'round': 64,
                'players': [
                    MARIN_CILIC,
                    ANDREA_BASSO
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    MARIN_CILIC: 1.07,
                    ANDREA_BASSO: 7.79
                }
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    LASLO_DJERE
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.26,
                    LASLO_DJERE: 1.61
                }
            },
            {
                'round': 32,
                'players': [
                    BORNA_CORIC,
                    CAMERON_NORRIE
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    BORNA_CORIC: 1.20,
                    CAMERON_NORRIE: 4.40
                }
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(5, 7), (6, 4), (6, 2)],
                'odds': {
                    KAREN_KHACHANOV: 2.20,
                    ROBERTO_BAUTISTA_AGUT: 1.65
                }
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    ALEXANDER_ZVEREV
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    MATTEO_BERRETTINI: 2.31,
                    ALEXANDER_ZVEREV: 1.61
                }
            },

            # 2019-05-16
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.44,
                    ALBERT_RAMOS_VINOLAS: 2.80
                }
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    NICK_KYRGIOS
                ],
                'score': [(6, 3), (6, 7), (2, 1)],
                'def': True,
                'odds': {
                    CASPER_RUUD: 3.10,
                    NICK_KYRGIOS: 1.36,
                }
            },
            {
                'round': 32,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 2.17,
                    MARCO_CECCHINATO: 1.69
                }
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    RADU_ALBOT
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    FABIO_FOGNINI: 1.25,
                    RADU_ALBOT: 3.70
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    MARIN_CILIC
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.40,
                    MARIN_CILIC: 1.57
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    JANNIK_SINNER
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.13,
                    JANNIK_SINNER: 5.50
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_MARTIN_DEL_POTRO,
                    DAVID_GOFFIN
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JUAN_MARTIN_DEL_POTRO: 2.35,
                    DAVID_GOFFIN: 1.56
                }
            },
            {
                'round': 32,
                'players': [
                    KEI_NISHIKORI,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    KEI_NISHIKORI: 1.31,
                    TAYLOR_FRITZ: 3.45
                }
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    DOMINIC_THIEM
                ],
                'score': [(4, 6), (6, 4), (7, 5)],
                'odds': {
                    FERNANDO_VERDASCO: 4.90,
                    DOMINIC_THIEM: 1.16
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    JOAO_SOUSA
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.07,
                    JOAO_SOUSA: 8.50
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    JEREMY_CHARDY
                ],
                'score': [(6, 0), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.03,
                    JEREMY_CHARDY: 11.00
                }
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    DENIS_SHAPOVALOV
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.10,
                    DENIS_SHAPOVALOV: 7.00
                }
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MATTEO_BERRETTINI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 2.37,
                    MATTEO_BERRETTINI: 1.54
                }
            },
            {
                'round': 16,
                'players': [
                    FERNANDO_VERDASCO,
                    KAREN_KHACHANOV
                ],
                'score': [(7, 5), (3, 6), (6, 3)],
                'odds': {
                    FERNANDO_VERDASCO: 2.60,
                    KAREN_KHACHANOV: 2.60
                }
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    FABIO_FOGNINI
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.43,
                    FABIO_FOGNINI: 2.45
                }
            },
            {
                'round': 16,
                'players': [
                    JUAN_MARTIN_DEL_POTRO,
                    CASPER_RUUD
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JUAN_MARTIN_DEL_POTRO: 1.36,
                    CASPER_RUUD: 3.10
                }
            },
            {
                'round': 16,
                'players': [
                    KEI_NISHIKORI,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(3, 6), (7, 6), (6, 3)],
                'odds': {
                    KEI_NISHIKORI: 1.50,
                    JAN_LENNARD_STRUFF: 2.65
                }
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    BORNA_CORIC
                ],
                'score': [(2, 6), (6, 4), (7, 6)],
                'odds': {
                    ROGER_FEDERER: 1.50,
                    BORNA_CORIC: 2.45
                }
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(6, 1), (6, 0)],
                'odds': {
                    RAFAEL_NADAL: 1.02,
                    NIKOLOZ_BASILASHVILI: 11.00
                }
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.08,
                    PHILIPP_KOHLSCHREIBER: 7.00
                }
            },

            # 2019-05-17
            {
                'round': 8,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    KEI_NISHIKORI
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 2.30,
                    KEI_NISHIKORI: 1.57
                }
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    ROGER_FEDERER
                ],
                'score': [],
                'wo': True,
                'odds': {
                    STEFANOS_TSITSIPAS: 1.69,
                    ROGER_FEDERER: 2.15
                }
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    RAFAEL_NADAL: 1.03,
                    FERNANDO_VERDASCO: 12.00
                }
            },
            {
                'round': 8,
                'players': [
                    NOVAK_DJOKOVIC,
                    JUAN_MARTIN_DEL_POTRO
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.12,
                    JUAN_MARTIN_DEL_POTRO: 6.62
                }
            },

            # 2019-05-18
            {
                'round': 4,
                'players': [
                    RAFAEL_NADAL,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.21,
                    STEFANOS_TSITSIPAS: 4.00
                }
            },
            {
                'round': 4,
                'players': [
                    NOVAK_DJOKOVIC,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 3), (6, 7), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.12,
                    DIEGO_SCHWARTZMAN: 6.50
                }
            },

            # 2019-05-19
            {
                'round': 2,
                'players': [
                    RAFAEL_NADAL,
                    NOVAK_DJOKOVIC
                ],
                'score': [(6, 0), (4, 6), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.47,
                    NOVAK_DJOKOVIC: 2.62
                }
            }
        ]
    },

    {
        'name': 'Banque Eric Sturdza Geneva Open',
        'date': '2019-05-19',
        'location': 'Geneva, Switzerland',
        'matches': [

            # 2019-05-18
            {
                'round': 512,
                'players': [
                    BERNABE_ZAPATA_MIRALLES,
                    BRADLEY_KLAHN
                ],
                'score': [(5, 7), (6, 4), (6, 2)],
                'odds': {
                    BERNABE_ZAPATA_MIRALLES: 1.40,
                    BRADLEY_KLAHN: 2.75
                }
            },
            {
                'round': 512,
                'players': [
                    KAICHI_UCHIDA,
                    RICARDAS_BERANKIS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    KAICHI_UCHIDA: 3.78,
                    RICARDAS_BERANKIS: 1.25
                }
            },
            {
                'round': 512,
                'players': [
                    LORENZO_SONEGO,
                    DANIEL_MASUR
                ],
                'score': [(4, 6), (6, 2), (6, 3)],
                'odds': {
                    LORENZO_SONEGO: 1.20,
                    DANIEL_MASUR: 3.99
                }
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    STEPHANE_ROBERT
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    TOMMY_PAUL: 1.18,
                    STEPHANE_ROBERT: 4.65
                }
            },
            {
                'round': 512,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ULISES_BLANCH
                ],
                'score': [(4, 6), (6, 1), (6, 4)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.21,
                    ULISES_BLANCH: 3.60
                }
            },
            {
                'round': 512,
                'players': [
                    THOMAS_FABBIANO,
                    MARKO_MILADINOVIC
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    THOMAS_FABBIANO: 1.10,
                    MARKO_MILADINOVIC: 6.25
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    JC_ARAGONE
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DAMIR_DZUMHUR: 1.10,
                    JC_ARAGONE: 6.35
                }
            },
            {
                'round': 512,
                'players': [
                    GRIGOR_DIMITROV,
                    MARC_ANDREA_HUESLER
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    GRIGOR_DIMITROV: 1.08,
                    MARC_ANDREA_HUESLER: 6.50
                }
            },

            # 2019-05-19
            {
                'round': 256,
                'players': [
                    BERNABE_ZAPATA_MIRALLES,
                    KAICHI_UCHIDA
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    BERNABE_ZAPATA_MIRALLES: 1.26,
                    KAICHI_UCHIDA: 3.47
                }
            },
            {
                'round': 256,
                'players': [
                    LORENZO_SONEGO,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    LORENZO_SONEGO: 1.47,
                    MIOMIR_KECMANOVIC: 2.63
                }
            },
            {
                'round': 256,
                'players': [
                    DAMIR_DZUMHUR,
                    TOMMY_PAUL
                ],
                'score': [(6, 2), (4, 6), (6, 3)],
                'odds': {
                    DAMIR_DZUMHUR: 1.65,
                    TOMMY_PAUL: 2.15
                }
            },
            {
                'round': 256,
                'players': [
                    GRIGOR_DIMITROV,
                    THOMAS_FABBIANO
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    GRIGOR_DIMITROV: 1.18,
                    THOMAS_FABBIANO: 4.65
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.25,
                    MISCHA_ZVEREV: 4.05
                }
            },
            {
                'round': 32,
                'players': [
                    ERNESTS_GULBIS,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    ERNESTS_GULBIS: 2.51,
                    YOSHIHITO_NISHIOKA: 1.53
                }
            },

            # 2019-05-20
            {
                'round': 32,
                'players': [
                    JANKO_TIPSAREVIC,
                    PETER_GOJOWCZYK
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    JANKO_TIPSAREVIC: 2.30,
                    PETER_GOJOWCZYK: 1.56
                }
            },
            {
                'round': 32,
                'players': [
                    DENIS_KUDLA,
                    JORDAN_THOMPSON
                ],
                'score': [(5, 7), (6, 2), (6, 4)],
                'odds': {
                    DENIS_KUDLA: 2.30,
                    JORDAN_THOMPSON: 1.65
                }
            },
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    BERNABE_ZAPATA_MIRALLES
                ],
                'score': [(6, 4), (4, 6), (6, 3)],
                'odds': {
                    TARO_DANIEL: 1.61,
                    BERNABE_ZAPATA_MIRALLES: 2.25
                }
            },
            {
                'round': 32,
                'players': [
                    HUGO_DELLIEN,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 1), (3, 6), (6, 4)],
                'odds': {
                    HUGO_DELLIEN: 1.79,
                    ANDREAS_SEPPI: 1.95
                }
            },
            {
                'round': 32,
                'players': [
                    NICOLAS_JARRY,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    NICOLAS_JARRY: 1.12,
                    MATTHEW_EBDEN: 6.25
                }
            },
            {
                'round': 32,
                'players': [
                    RADU_ALBOT,
                    LORENZO_SONEGO
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    RADU_ALBOT: 2.40,
                    LORENZO_SONEGO: 1.56
                }
            },

            # 2019-05-21
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    LEONARDO_MAYER
                ],
                'score': [(6, 2), (6, 7), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 1.98,
                    LEONARDO_MAYER: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    DAMIR_DZUMHUR,
                    FELICIANO_LOPEZ
                ],
                'score': [(6, 7), (6, 4), (7, 5)],
                'odds': {
                    DAMIR_DZUMHUR: 1.49,
                    FELICIANO_LOPEZ: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    FEDERICO_DELBONIS,
                    GRIGOR_DIMITROV
                ],
                'score': [(6, 7), (6, 3), (6, 2)],
                'odds': {
                    FEDERICO_DELBONIS: 2.70,
                    GRIGOR_DIMITROV: 1.44
                }
            },
            {
                'round': 16,
                'players': [
                    HUGO_DELLIEN,
                    JANKO_TIPSAREVIC
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    HUGO_DELLIEN: 1.44,
                    JANKO_TIPSAREVIC: 2.75
                }
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    ERNESTS_GULBIS
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.15,
                    ERNESTS_GULBIS: 5.50
                }
            },

            # 2019-05-22
            {
                'round': 16,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    JOAO_SOUSA
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.63,
                    JOAO_SOUSA: 2.21
                }
            },
            {
                'round': 16,
                'players': [
                    NICOLAS_JARRY,
                    DENIS_KUDLA
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    NICOLAS_JARRY: 1.40,
                    DENIS_KUDLA: 3.00
                }
            },
            {
                'round': 16,
                'players': [
                    RADU_ALBOT,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 1), (6, 7), (6, 4)],
                'odds': {
                    RADU_ALBOT: 1.79,
                    JUAN_IGNACIO_LONDERO: 1.95
                }
            },
            {
                'round': 16,
                'players': [
                    FEDERICO_DELBONIS,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    FEDERICO_DELBONIS: 1.95,
                    MARTON_FUCSOVICS: 1.80
                }
            },
            {
                'round': 16,
                'players': [
                    TARO_DANIEL,
                    CRISTIAN_GARIN
                ],
                'score': [(6, 2), (4, 6), (6, 4)],
                'odds': {
                    TARO_DANIEL: 3.25,
                    CRISTIAN_GARIN: 1.31
                }
            },

            # 2019-05-23
            {
                'round': 8,
                'players': [
                    NICOLAS_JARRY,
                    TARO_DANIEL
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    NICOLAS_JARRY: 1.46,
                    TARO_DANIEL: 2.87
                }
            },
            {
                'round': 8,
                'players': [
                    FEDERICO_DELBONIS,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    FEDERICO_DELBONIS: 1.67,
                    ALBERT_RAMOS_VINOLAS: 2.20
                }
            },
            {
                'round': 8,
                'players': [
                    RADU_ALBOT,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    RADU_ALBOT: 1.83,
                    DAMIR_DZUMHUR: 1.87
                }
            },
            {
                'round': 8,
                'players': [
                    ALEXANDER_ZVEREV,
                    HUGO_DELLIEN
                ],
                'score': [(7, 5), (3, 6), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.19,
                    HUGO_DELLIEN: 5.37
                }
            },

            # 2019-05-24
            {
                'round': 4,
                'players': [
                    NICOLAS_JARRY,
                    RADU_ALBOT
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    NICOLAS_JARRY: 1.74,
                    RADU_ALBOT: 1.97
                }
            },
            {
                'round': 4,
                'players': [
                    ALEXANDER_ZVEREV,
                    FEDERICO_DELBONIS
                ],
                'score': [(7, 5), (6, 7), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.45,
                    FEDERICO_DELBONIS: 2.86
                }
            },

            # 2019-05-25
            {
                'round': 2,
                'players': [
                    ALEXANDER_ZVEREV,
                    NICOLAS_JARRY
                ],
                'score': [(6, 3), (3, 6), (7, 6)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.47,
                    NICOLAS_JARRY: 2.82
                }
            }
        ]
    },

    {
        'name': 'Open Parc Auvergne-Rhone-Alpes Lyon',
        'date': '2019-05-19',
        'location': 'Lyon, France',
        'matches': [

            # 2019-05-18
            {
                'round': 512,
                'players': [
                    MAXIME_JANVIER,
                    GUILHERME_CLEZAR
                ],
                'score': [(7, 5), (4, 6), (6, 4)],
                'odds': {
                    MAXIME_JANVIER: 1.48,
                    GUILHERME_CLEZAR: 2.60
                }
            },
            {
                'round': 512,
                'players': [
                    QUENTIN_HALYS,
                    MARIO_VILELLA_MARTINEZ
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    QUENTIN_HALYS: 1.34,
                    MARIO_VILELLA_MARTINEZ: 2.90
                }
            },
            {
                'round': 512,
                'players': [
                    JANNIK_SINNER,
                    ANTOINE_HOANG
                ],
                'score': [(6, 4), (5, 7), (6, 1)],
                'odds': {
                    JANNIK_SINNER: 1.74,
                    ANTOINE_HOANG: 1.95
                }
            },
            {
                'round': 512,
                'players': [
                    GREGOIRE_BARRERE,
                    HUGO_GRENIER
                ],
                'score': [(6, 7), (6, 4), (7, 6)],
                'odds': {
                    GREGOIRE_BARRERE: 1.17,
                    HUGO_GRENIER: 5.00
                }
            },
            {
                'round': 512,
                'players': [
                    STEVEN_DIEZ,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 4), (3, 6), (7, 5)],
                'odds': {
                    STEVEN_DIEZ: 2.40,
                    ALEXEI_POPYRIN: 1.48
                }
            },
            {
                'round': 512,
                'players': [
                    JIRI_VESELY,
                    NICOLA_KUHN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JIRI_VESELY: 1.65,
                    NICOLA_KUHN: 2.13
                }
            },
            {
                'round': 512,
                'players': [
                    TRISTAN_LAMASINE,
                    ALEXANDER_BUBLIK
                ],
                'score': [(6, 2), (2, 6), (7, 5)],
                'odds': {
                    TRISTAN_LAMASINE: 1.78,
                    ALEXANDER_BUBLIK: 1.74
                }
            },
            {
                'round': 512,
                'players': [
                    LLOYD_HARRIS,
                    KENNY_DE_SCHEPPER
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    LLOYD_HARRIS: 1.19,
                    KENNY_DE_SCHEPPER: 4.40
                }
            },

            # 2019-05-19
            {
                'round': 256,
                'players': [
                    JANNIK_SINNER,
                    TRISTAN_LAMASINE
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    JANNIK_SINNER: 1.48,
                    TRISTAN_LAMASINE: 2.45
                }
            },
            {
                'round': 256,
                'players': [
                    STEVEN_DIEZ,
                    QUENTIN_HALYS
                ],
                'score': [(6, 2), (3, 6), (6, 3)],
                'odds': {
                    STEVEN_DIEZ: 2.90,
                    QUENTIN_HALYS: 1.33
                }
            },
            {
                'round': 256,
                'players': [
                    JIRI_VESELY,
                    GREGOIRE_BARRERE
                ],
                'score': [(3, 6), (6, 3), (6, 2)],
                'odds': {
                    JIRI_VESELY: 1.48,
                    GREGOIRE_BARRERE: 2.50
                }
            },
            {
                'round': 256,
                'players': [
                    MAXIME_JANVIER,
                    LLOYD_HARRIS
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    MAXIME_JANVIER: 2.05,
                    LLOYD_HARRIS: 1.69
                }
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    PABLO_ANDUJAR
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    JOHN_MILLMAN: 2.04,
                    PABLO_ANDUJAR: 1.72
                }
            },
            {
                'round': 32,
                'players': [
                    JO_WILFRIED_TSONGA,
                    DUSAN_LAJOVIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.60,
                    DUSAN_LAJOVIC: 2.30
                }
            },

            # 2019-05-20
            {
                'round': 32,
                'players': [
                    TRISTAN_LAMASINE,
                    JANNIK_SINNER
                ],
                'score': [(6, 0), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    STEVE_JOHNSON,
                    LLOYD_HARRIS
                ],
                'score': [(6, 2), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    CAMERON_NORRIE
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    UGO_HUMBERT: 2.50,
                    CAMERON_NORRIE: 1.49
                }
            },
            {
                'round': 32,
                'players': [
                    TAYLOR_FRITZ,
                    JIRI_VESELY
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    TAYLOR_FRITZ: 1.67,
                    JIRI_VESELY: 2.15
                }
            },
            {
                'round': 32,
                'players': [
                    STEVEN_DIEZ,
                    BERNARD_TOMIC
                ],
                'score': [(6, 4), (4, 1)],
                'retired': True,
                'odds': {
                    STEVEN_DIEZ: 1.74,
                    BERNARD_TOMIC: 2.00
                }
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    JEREMY_CHARDY
                ],
                'score': [(6, 7), (6, 2), (7, 6)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 2.05,
                    JEREMY_CHARDY: 1.71
                }
            },

            # 2019-05-21
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    MACKENZIE_MCDONALD
                ],
                'score': [(3, 6), (7, 6), (6, 1)],
                'odds': {
                    BENOIT_PAIRE: 1.33,
                    MACKENZIE_MCDONALD: 3.09
                }
            },
            {
                'round': 32,
                'players': [
                    CORENTIN_MOUTET,
                    REILLY_OPELKA
                ],
                'score': [(6, 3), (2, 6), (7, 6)],
                'odds': {
                    CORENTIN_MOUTET: 2.51,
                    REILLY_OPELKA: 1.50
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_CUEVAS,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    PABLO_CUEVAS: 1.71,
                    HUBERT_HURKACZ: 2.05
                }
            },
            {
                'round': 16,
                'players': [
                    STEVE_JOHNSON,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(7, 6), (5, 7), (6, 1)],
                'odds': {
                    STEVE_JOHNSON: 2.55,
                    PIERRE_HUGUES_HERBERT: 1.51
                }
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    JOHN_MILLMAN
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.43,
                    JOHN_MILLMAN: 2.55
                }
            },

            # 2019-05-22
            {
                'round': 16,
                'players': [
                    JO_WILFRIED_TSONGA,
                    STEVEN_DIEZ
                ],
                'score': [(3, 6), (7, 6), (6, 3)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.20,
                    STEVEN_DIEZ: 4.50
                }
            },
            {
                'round': 16,
                'players': [
                    BENOIT_PAIRE,
                    PABLO_CUEVAS
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 2.65,
                    PABLO_CUEVAS: 1.48
                }
            },
            {
                'round': 16,
                'players': [
                    TAYLOR_FRITZ,
                    RICHARD_GASQUET
                ],
                'score': [],
                'wo': True,
                'odds': {
                    TAYLOR_FRITZ: 1.54,
                    RICHARD_GASQUET: 2.30
                }
            },
            {
                'round': 16,
                'players': [
                    DENIS_SHAPOVALOV,
                    UGO_HUMBERT
                ],
                'score': [(2, 6), (7, 6), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.47,
                    UGO_HUMBERT: 2.60
                }
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    CORENTIN_MOUTET
                ],
                'score': [(4, 6), (6, 4), (6, 3)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.22,
                    CORENTIN_MOUTET: 4.15
                }
            },
            {
                'round': 16,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    TRISTAN_LAMASINE
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.25,
                    TRISTAN_LAMASINE: 3.85
                }
            },

            # 2019-05-23
            {
                'round': 8,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    STEVE_JOHNSON
                ],
                'score': [(6, 4), (2, 6), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.33,
                    STEVE_JOHNSON: 3.30
                }
            },
            {
                'round': 8,
                'players': [
                    BENOIT_PAIRE,
                    DENIS_SHAPOVALOV
                ],
                'score': [(6, 3), (4, 6), (7, 6)],
                'odds': {
                    BENOIT_PAIRE: 1.80,
                    DENIS_SHAPOVALOV: 2.00
                }
            },
            {
                'round': 8,
                'players': [
                    TAYLOR_FRITZ,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 2.40,
                    ROBERTO_BAUTISTA_AGUT: 1.56
                }
            },
            {
                'round': 8,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.22,
                    JO_WILFRIED_TSONGA: 1.65
                }
            },

            # 2019-05-24
            {
                'round': 4,
                'players': [
                    BENOIT_PAIRE,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    BENOIT_PAIRE: 2.04,
                    TAYLOR_FRITZ: 1.71
                }
            },
            {
                'round': 4,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(2, 6), (7, 6), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.64,
                    NIKOLOZ_BASILASHVILI: 2.15
                }
            },

            # 2019-05-25
            {
                'round': 2,
                'players': [
                    BENOIT_PAIRE,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 1.95,
                    FELIX_AUGER_ALIASSIME: 1.80
                }
            }
        ]
    },

    {
        'name': 'Roland Garros',
        'date': '2019-05-26',
        'location': 'Paris, France',
        'matches': [
            {
                'round': 128,
                'players': [
                    CASPER_RUUD,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 2), (7, 6), (6, 0)],
                'odds': {
                    CASPER_RUUD: 1.26,
                    ERNESTS_GULBIS: 3.80
                }
            },
            {
                'round': 128,
                'players': [
                    ALEXEI_POPYRIN,
                    UGO_HUMBERT
                ],
                'score': [(3, 6), (6, 3), (7, 6), (6, 3)],
                'odds': {
                    ALEXEI_POPYRIN: 2.00,
                    UGO_HUMBERT: 1.77
                }
            },
            {
                'round': 128,
                'players': [
                    OSCAR_OTTE,
                    MALEK_JAZIRI,
                ],
                'score': [(6, 3), (6, 1), (4, 6), (6, 0)],
                'odds': {
                    OSCAR_OTTE: 1.75,
                    MALEK_JAZIRI: 2.00
                }
            },
            {
                'round': 128,
                'players': [
                    LEONARDO_MAYER,
                    JIRI_VESELY
                ],
                'score': [(7, 6), (6, 3), (6, 0)],
                'odds': {
                    LEONARDO_MAYER: 1.63,
                    JIRI_VESELY: 2.33
                }
            },
            {
                'round': 128,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    ROBIN_HAASE,
                ],
                'score': [(6, 4), (6, 4), (6, 7), (6, 1)],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.22,
                    ROBIN_HAASE: 4.25
                }
            },
            {
                'round': 128,
                'players': [
                    GRIGOR_DIMITROV,
                    JANKO_TIPSAREVIC,
                ],
                'score': [(6, 3), (6, 0), (3, 6), (6, 7), (6, 4)],
                'odds': {
                    GRIGOR_DIMITROV: 1.17,
                    JANKO_TIPSAREVIC: 5.21
                }
            },
            {
                'round': 128,
                'players': [
                    HUGO_DELLIEN,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(6, 1), (6, 3), (6, 1)],
                'odds': {
                    HUGO_DELLIEN: 1.20,
                    PRAJNESH_GUNNESWARAN: 4.57
                }
            },
            {
                'round': 128,
                'players': [
                    LASLO_DJERE,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 3), (6, 2), (7, 6)],
                'odds': {
                    LASLO_DJERE: 1.74,
                    ALBERT_RAMOS_VINOLAS: 2.13
                }
            },
            {
                'round': 128,
                'players': [
                    MATTEO_BERRETTINI,
                    PABLO_ANDUJAR
                ],
                'score': [(6, 7), (6, 4), (6, 4), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 1.19,
                    PABLO_ANDUJAR: 5.00
                }
            },
            {
                'round': 128,
                'players': [
                    DAVID_GOFFIN,
                    RICARDAS_BERANKIS
                ],
                'score': [(6, 0), (6, 2), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.07,
                    RICARDAS_BERANKIS: 9.37
                }
            },
            {
                'round': 128,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 3), (3, 6), (7, 6), (2, 6), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.31,
                    MARTON_FUCSOVICS: 3.30
                }
            },
            {
                'round': 128,
                'players': [
                    NICOLAS_MAHUT,
                    MARCO_CECCHINATO
                ],
                'score': [(2, 6), (6, 7), (6, 4), (6, 2), (6, 4)],
                'odds': {
                    NICOLAS_MAHUT: 8.00,
                    MARCO_CECCHINATO: 1.09
                }
            },
            {
                'round': 128,
                'players': [
                    MARIN_CILIC,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 3), (7, 5), (6, 1)],
                'odds': {
                    MARIN_CILIC: 1.08,
                    THOMAS_FABBIANO: 8.11
                }
            },
            {
                'round': 128,
                'players': [
                    KEI_NISHIKORI,
                    QUENTIN_HALYS
                ],
                'score': [(6, 2), (6, 3), (6, 4)],
                'odds': {
                    KEI_NISHIKORI: 1.15,
                    QUENTIN_HALYS: 5.65
                }
            },
            {
                'round': 128,
                'players': [
                    STEFANOS_TSITSIPAS,
                    MAXIMILIAN_MARTERER,
                ],
                'score': [(6, 2), (6, 2), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.02,
                    MAXIMILIAN_MARTERER: 17.73
                }
            },
            {
                'round': 128,
                'players': [
                    ROGER_FEDERER,
                    LORENZO_SONEGO
                ],
                'score': [(6, 2), (6, 4), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.10,
                    LORENZO_SONEGO: 7.00
                }
            },

            {
                'round': 128,
                'players': [
                    JO_WILFRIED_TSONGA,
                    PETER_GOJOWCZYK
                ],
                'score': [(7, 6), (6, 1), (4, 6), (6, 3)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.22,
                    PETER_GOJOWCZYK: 4.70
                }
            },
            {
                'round': 128,
                'players': [
                    BENOIT_PAIRE,
                    MARIUS_COPIL
                ],
                'score': [(6, 4), (6, 7), (6, 0), (6, 1)],
                'odds': {
                    BENOIT_PAIRE: 1.18,
                    MARIUS_COPIL: 5.01
                }
            },
            {
                'round': 128,
                'players': [
                    CORENTIN_MOUTET,
                    ALEXEY_VATUTIN,
                ],
                'score': [(6, 4), (7, 6), (6, 4)],
                'odds': {
                    CORENTIN_MOUTET: 1.51,
                    ALEXEY_VATUTIN: 2.65
                }
            },
            {
                'round': 128,
                'players': [
                    YANNICK_MADEN,
                    KIMMER_COPPEJANS,
                ],
                'score': [(7, 6), (7, 5), (6, 3)],
                'odds': {
                    YANNICK_MADEN: 1.45,
                    KIMMER_COPPEJANS: 2.75
                }
            },
            {
                'round': 128,
                'players': [
                    HENRI_LAAKSONEN,
                    PEDRO_MARTINEZ
                ],
                'score': [(6, 1), (6, 0), (7, 6)],
                'odds': {
                    HENRI_LAAKSONEN: 1.83,
                    PEDRO_MARTINEZ: 1.91
                }
            },
            {
                'round': 128,
                'players': [
                    MIOMIR_KECMANOVIC,
                    DENIS_KUDLA
                ],
                'score': [(6, 0), (6, 7), (5, 7), (6, 3), (6, 4)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.44,
                    DENIS_KUDLA: 2.80
                }
            },
            {
                'round': 128,
                'players': [
                    LLOYD_HARRIS,
                    LUKAS_ROSOL
                ],
                'score': [(6, 1), (4, 6), (2, 6), (6, 1), (6, 2)],
                'odds': {
                    LLOYD_HARRIS: 1.61,
                    LUKAS_ROSOL: 2.41
                }
            },
            {
                'round': 128,
                'players': [
                    RICHARD_GASQUET,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 3), (6, 4), (6, 3)],
                'odds': {
                    RICHARD_GASQUET: 1.11,
                    MISCHA_ZVEREV: 6.27
                }
            },
            {
                'round': 128,
                'players': [
                    CRISTIAN_GARIN,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (7, 5), (7, 6)],
                'odds': {
                    CRISTIAN_GARIN: 1.37,
                    REILLY_OPELKA: 3.20
                }
            },
            {
                'round': 128,
                'players': [
                    PABLO_CUEVAS,
                    MAXIME_JANVIER
                ],
                'score': [(6, 4), (6, 4), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 1.17,
                    MAXIME_JANVIER: 5.47
                }
            },
            {
                'round': 128,
                'players': [
                    SALVATORE_CARUSO,
                    JAUME_MUNAR
                ],
                'score': [(7, 5), (4, 6), (6, 3), (6, 3)],
                'odds': {
                    SALVATORE_CARUSO: 4.00,
                    JAUME_MUNAR: 1.25
                }
            },
            {
                'round': 128,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JOAO_SOUSA
                ],
                'score': [(6, 3), (6, 1), (6, 2)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.78,
                    JOAO_SOUSA: 1.91
                }
            },
            {
                'round': 128,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    ALEXANDRE_MULLER
                ],
                'score': [(6, 4), (6, 4), (6, 2)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.18,
                    ALEXANDRE_MULLER: 5.15
                }
            },
            {
                'round': 128,
                'players': [
                    ALEXANDER_BUBLIK,
                    RUDOLF_MOLLEKER
                ],
                'score': [(7, 5), (6, 7), (6, 1), (7, 6)],
                'odds': {
                    ALEXANDER_BUBLIK: 3.18,
                    RUDOLF_MOLLEKER: 1.38
                }
            },
            {
                'round': 128,
                'players': [
                    RADU_ALBOT,
                    TENNYS_SANDGREN
                ],
                'score': [(7, 6), (7, 6), (3, 6), (6, 1)],
                'odds': {
                    RADU_ALBOT: 1.31,
                    TENNYS_SANDGREN: 3.32
                }
            },
            {
                'round': 128,
                'players': [
                    FILIP_KRAJINOVIC,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 2), (4, 6), (6, 3), (3, 6), (6, 0)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.42,
                    FRANCES_TIAFOE: 2.88
                }
            },
            {
                'round': 128,
                'players': [
                    GILLES_SIMON,
                    SERGIY_STAKHOVSKY
                ],
                'score': [(6, 3), (6, 3), (6, 4)],
                'odds': {
                    GILLES_SIMON: 1.14,
                    SERGIY_STAKHOVSKY: 6.06
                }
            },
            {
                'round': 128,
                'players': [
                    STAN_WAWRINKA,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 1), (6, 7), (6, 2), (6, 3)],
                'odds': {
                    STAN_WAWRINKA: 1.09,
                    JOZEF_KOVALIK: 7.14
                }
            },
            {
                'round': 128,
                'players': [
                    ALEX_DE_MINAUR,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 1), (6, 4), (6, 4)],
                'odds': {
                    ALEX_DE_MINAUR: 1.17,
                    BRADLEY_KLAHN: 5.47
                }
            },
            {
                'round': 128,
                'players': [
                    JAN_LENNARD_STRUFF,
                    DENIS_SHAPOVALOV
                ],
                'score': [(7, 6), (6, 3), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.50,
                    DENIS_SHAPOVALOV: 2.68
                }
            },
            {
                'round': 128,
                'players': [
                    GUIDO_PELLA,
                    GUIDO_ANDREOZZI
                ],
                'score': [(7, 6), (6, 4), (1, 6), (6, 1)],
                'odds': {
                    GUIDO_PELLA: 1.24,
                    GUIDO_ANDREOZZI: 4.25
                }
            },
            {
                'round': 128,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(6, 4), (6, 1), (6, 3)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 2.52,
                    NIKOLOZ_BASILASHVILI: 1.48
                }
            },
            {
                'round': 128,
                'players': [
                    BORNA_CORIC,
                    ALJAZ_BEDENE
                ],
                'score': [(6, 1), (6, 7), (6, 4), (6, 4)],
                'odds': {
                    BORNA_CORIC: 1.18,
                    ALJAZ_BEDENE: 4.67
                }
            },
            {
                'round': 128,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    DANILL_MEDVEDEV
                ],
                'score': [(4, 6), (4, 6), (6, 3), (6, 2), (7, 5)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 3.43,
                    DANILL_MEDVEDEV: 1.33
                }
            },
            {
                'round': 128,
                'players': [
                    DOMINIC_THIEM,
                    TOMMY_PAUL
                ],
                'score': [(6, 4), (4, 6), (7, 6), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.02,
                    TOMMY_PAUL: 18.13
                }
            },
            {
                'round': 128,
                'players': [
                    RAFAEL_NADAL,
                    YANNICK_HANFMANN
                ],
                'score': [(6, 2), (6, 1), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.00,
                    YANNICK_HANFMANN: 22.23
                }
            },
            {
                'round': 128,
                'players': [
                    NOVAK_DJOKOVIC,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 4), (6, 2), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.03,
                    HUBERT_HURKACZ: 13.84
                }
            },

            {
                'round': 128,
                'players': [
                    MIKAEL_YMER,
                    BLAZ_ROLA
                ],
                'score': [(6, 0), (6, 3), (7, 6)],
                'odds': {
                    MIKAEL_YMER: 1.65,
                    BLAZ_ROLA: 2.20
                }
            },
            {
                'round': 128,
                'players': [
                    JORDAN_THOMPSON,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(6, 3), (6, 2), (7, 6)],
                'odds': {
                    JORDAN_THOMPSON: 2.75,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.48
                }
            },
            {
                'round': 128,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    MACKENZIE_MCDONALD
                ],
                'score': [(6, 7), (6, 0), (4, 6), (6, 2), (6, 3)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.32,
                    MACKENZIE_MCDONALD: 2.95
                }
            },
            {
                'round': 128,
                'players': [
                    ADRIAN_MANNARINO,
                    STEFANO_TRAVAGLIA
                ],
                'score': [(6, 7), (6, 3), (3, 6), (6, 2), (6, 2)],
                'odds': {
                    ADRIAN_MANNARINO: 2.70,
                    STEFANO_TRAVAGLIA: 1.46
                }
            },
            {
                'round': 128,
                'players': [
                    MARTIN_KLIZAN,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(3, 6), (5, 7), (6, 4), (6, 2), (6, 3)],
                'odds': {
                    MARTIN_KLIZAN: 1.56,
                    MIKHAIL_KUKUSHKIN: 2.45
                }
            },
            {
                'round': 128,
                'players': [
                    IVO_KARLOVIC,
                    FELICIANO_LOPEZ
                ],
                'score': [(7, 6), (7, 5), (6, 7), (7, 5)],
                'odds': {
                    IVO_KARLOVIC: 2.63,
                    FELICIANO_LOPEZ: 1.45
                }
            },
            {
                'round': 128,
                'players': [
                    ANTOINE_HOANG,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 4), (0, 6), (7, 6), (6, 3)],
                'odds': {
                    ANTOINE_HOANG: 3.45,
                    DAMIR_DZUMHUR: 1.32
                }
            },
            {
                'round': 128,
                'players': [
                    TAYLOR_FRITZ,
                    BERNARD_TOMIC
                ],
                'score': [(6, 1), (6, 4), (6, 1)],
                'odds': {
                    TAYLOR_FRITZ: 1.12,
                    BERNARD_TOMIC: 5.77
                }
            },
            {
                'round': 128,
                'players': [
                    FEDERICO_DELBONIS,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(6, 1), (3, 6), (6, 3), (6, 2)],
                'odds': {
                    FEDERICO_DELBONIS: 1.30,
                    GUILLERMO_GARCIA_LOPEZ: 3.45
                }
            },
            {
                'round': 128,
                'players': [
                    ELLIOT_BENCHETRIT,
                    CAMERON_NORRIE
                ],
                'score': [(6, 3), (6, 0), (6, 2)],
                'odds': {
                    ELLIOT_BENCHETRIT: 2.24,
                    CAMERON_NORRIE: 1.61
                }
            },
            {
                'round': 128,
                'players': [
                    GREGOIRE_BARRERE,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 3), (5, 7), (7, 5), (6, 1)],
                'odds': {
                    GREGOIRE_BARRERE: 1.24,
                    MATTHEW_EBDEN: 4.00
                }
            },
            {
                'round': 128,
                'players': [
                    DUSAN_LAJOVIC,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 3), (6, 4), (6, 4)],
                'odds': {
                    DUSAN_LAJOVIC: 1.45,
                    THIAGO_MONTEIRO: 2.63
                }
            },
            {
                'round': 128,
                'players': [
                    KYLE_EDMUND,
                    JEREMY_CHARDY
                ],
                'score': [(7, 6), (5, 7), (6, 4), (4, 6), (7, 5)]
            },
            {
                'round': 128,
                'players': [
                    FERNANDO_VERDASCO,
                    DANIEL_EVANS
                ],
                'score': [(6, 3), (6, 7), (6, 3), (6, 2)],
                'odds': {
                    FERNANDO_VERDASCO: 1.22,
                    DANIEL_EVANS: 3.34
                }
            },
            {
                'round': 128,
                'players': [
                    LUCAS_POUILLE,
                    SIMONE_BOLELLI
                ],
                'score': [(6, 3), (6, 4), (7, 5)],
                'odds': {
                    LUCAS_POUILLE: 1.43,
                    SIMONE_BOLELLI: 2.95
                }
            },
            {
                'round': 128,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    STEVE_JOHNSON
                ],
                'score': [(6, 3), (6, 4), (6, 2)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.19,
                    STEVE_JOHNSON: 4.60
                }
            },
            {
                'round': 128,
                'players': [
                    GAEL_MONFILS,
                    TARO_DANIEL
                ],
                'score': [(6, 0), (6, 4), (6, 1)],
                'odds': {
                    GAEL_MONFILS: 1.11,
                    TARO_DANIEL: 6.00
                }
            },
            {
                'round': 128,
                'players': [
                    KAREN_KHACHANOV,
                    CEDRIC_MARCEL_STEBE
                ],
                'score': [(6, 1), (6, 1), (6, 4)],
                'odds': {
                    KAREN_KHACHANOV: 1.02,
                    CEDRIC_MARCEL_STEBE: 13.00
                }
            },
            {
                'round': 128,
                'players': [
                    FABIO_FOGNINI,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 3), (6, 0), (3, 6), (6, 3)],
                'odds': {
                    FABIO_FOGNINI: 1.14,
                    ANDREAS_SEPPI: 5.50
                }
            },
            {
                'round': 128,
                'players': [
                    JUAN_MARTIN_DEL_POTRO,
                    NICOLAS_JARRY
                ],
                'score': [(3, 6), (6, 2), (6, 1), (6, 4)],
                'odds': {
                    JUAN_MARTIN_DEL_POTRO: 1.25,
                    NICOLAS_JARRY: 4.10
                }
            },
            {
                'round': 128,
                'players': [
                    ALEXANDER_ZVEREV,
                    JOHN_MILLMAN
                ],
                'score': [(7, 6), (6, 3), (2, 6), (6, 7), (6, 3)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.11,
                    JOHN_MILLMAN: 7.01
                }
            },

            {
                'round': 64,
                'players': [
                    BENOIT_PAIRE,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 2), (6, 2), (5, 7), (6, 7), (11, 9)],
                'odds': {
                    BENOIT_PAIRE: 1.42,
                    PIERRE_HUGUES_HERBERT: 2.73
                }
            },
            {
                'round': 64,
                'players': [
                    NICOLAS_MAHUT,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 3), (6, 3), (6, 3)],
                'odds': {
                    NICOLAS_MAHUT: 6.62,
                    PHILIPP_KOHLSCHREIBER: 1.10
                }
            },
            {
                'round': 64,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    RICHARD_GASQUET
                ],
                'score': [(6, 2), (3, 6), (6, 3), (6, 4)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.91,
                    RICHARD_GASQUET: 1.87
                }
            },
            {
                'round': 64,
                'players': [
                    FILIP_KRAJINOVIC,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 4), (6, 4), (6, 7), (3, 6), (8, 6)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.44,
                    ROBERTO_CARBALLES_BAENA: 2.85
                }
            },
            {
                'round': 64,
                'players': [
                    LASLO_DJERE,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 4), (7, 6), (6, 4)],
                'odds': {
                    LASLO_DJERE: 1.24,
                    ALEXEI_POPYRIN: 4.00
                }
            },
            {
                'round': 64,
                'players': [
                    CASPER_RUUD,
                    MATTEO_BERRETTINI
                ],
                'score': [(6, 4), (7, 5), (6, 3)],
                'odds': {
                    CASPER_RUUD: 2.55,
                    MATTEO_BERRETTINI: 1.51
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 2), (6, 4), (6, 3)],
                'odds': {
                    DAVID_GOFFIN: 1.11,
                    MIOMIR_KECMANOVIC: 6.25
                }
            },
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    CRISTIAN_GARIN
                ],
                'score': [(6, 1), (6, 4), (6, 0)],
                'odds': {
                    STAN_WAWRINKA: 1.53,
                    CRISTIAN_GARIN: 2.50
                }
            },
            {
                'round': 64,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    ALEX_DE_MINAUR
                ],
                'score': [(6, 3), (6, 1), (6, 1)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.43,
                    ALEX_DE_MINAUR: 2.84
                }
            },
            {
                'round': 64,
                'players': [
                    CORENTIN_MOUTET,
                    GUIDO_PELLA
                ],
                'score': [(6, 3), (6, 1), (2, 6), (7, 5)],
                'odds': {
                    CORENTIN_MOUTET: 4.05,
                    GUIDO_PELLA: 1.22
                }
            },
            {
                'round': 64,
                'players': [
                    GRIGOR_DIMITROV,
                    MARIN_CILIC
                ],
                'score': [(6, 7), (6, 4), (4, 6), (7, 6), (6, 3)],
                'odds': {
                    GRIGOR_DIMITROV: 2.45,
                    MARIN_CILIC: 1.54
                }
            },
            {
                'round': 64,
                'players': [
                    KEI_NISHIKORI,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(4, 6), (6, 4), (6, 4), (6, 4)],
                'odds': {
                    KEI_NISHIKORI: 1.32,
                    JO_WILFRIED_TSONGA: 3.25
                }
            },
            {
                'round': 64,
                'players': [
                    STEFANOS_TSITSIPAS,
                    HUGO_DELLIEN
                ],
                'score': [(4, 6), (6, 0), (6, 3), (7, 5)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.07,
                    HUGO_DELLIEN: 7.50
                }
            },
            {
                'round': 64,
                'players': [
                    ROGER_FEDERER,
                    OSCAR_OTTE
                ],
                'score': [(6, 4), (6, 3), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.02,
                    OSCAR_OTTE: 16.78
                }
            },
            {
                'round': 64,
                'players': [
                    RAFAEL_NADAL,
                    YANNICK_MADEN
                ],
                'score': [(6, 1), (6, 2), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    YANNICK_MADEN: 22.00
                }
            },

            # 2019-05-30
            {
                'round': 64,
                'players': [
                    JORDAN_THOMPSON,
                    IVO_KARLOVIC
                ],
                'score': [(6, 3), (6, 4), (6, 7), (6, 3)],
                'odds': {
                    JORDAN_THOMPSON: 1.47,
                    IVO_KARLOVIC: 2.73
                }
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    RADU_ALBOT
                ],
                'score': [(7, 6), (7, 6), (6, 7), (6, 2)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.37,
                    RADU_ALBOT: 3.09
                }
            },
            {
                'round': 64,
                'players': [
                    DUSAN_LAJOVIC,
                    ELLIOT_BENCHETRIT
                ],
                'score': [(6, 3), (6, 3), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 1.31,
                    ELLIOT_BENCHETRIT: 3.55
                }
            },
            {
                'round': 64,
                'players': [
                    PABLO_CUEVAS,
                    KYLE_EDMUND
                ],
                'score': [(7, 6), (6, 3), (2, 1)],
                'retired': True,
                'odds': {
                    PABLO_CUEVAS: 1.61,
                    KYLE_EDMUND: 2.20
                }
            },
            {
                'round': 64,
                'players': [
                    SALVATORE_CARUSO,
                    GILLES_SIMON
                ],
                'score': [(6, 1), (6, 2), (6, 4)],
                'odds': {
                    SALVATORE_CARUSO: 3.24,
                    GILLES_SIMON: 1.33
                }
            },
            {
                'round': 64,
                'players': [
                    ANTOINE_HOANG,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 4), (3, 6), (7, 6), (7, 5)],
                'odds': {
                    ANTOINE_HOANG: 5.75,
                    FERNANDO_VERDASCO: 1.13
                }
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 2), (6, 3), (6, 2)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.44,
                    TAYLOR_FRITZ: 2.68
                }
            },
            {
                'round': 64,
                'players': [
                    LEONARDO_MAYER,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(4, 6), (6, 3), (6, 4), (7, 5)]
            },
            {
                'round': 64,
                'players': [
                    GAEL_MONFILS,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 3), (6, 4), (6, 4)],
                'odds': {
                    GAEL_MONFILS: 1.09,
                    ADRIAN_MANNARINO: 7.00
                }
            },
            {
                'round': 64,
                'players': [
                    BORNA_CORIC,
                    LLOYD_HARRIS
                ],
                'score': [(6, 2), (6, 3), (7, 6)],
                'odds': {
                    BORNA_CORIC: 1.06,
                    LLOYD_HARRIS: 9.50
                }
            },
            {
                'round': 64,
                'players': [
                    KAREN_KHACHANOV,
                    GREGOIRE_BARRERE
                ],
                'score': [(6, 3), (7, 6), (0, 6), (7, 5)],
                'odds': {
                    KAREN_KHACHANOV: 1.10,
                    GREGOIRE_BARRERE: 6.75
                }
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 4), (3, 6), (6, 3), (6, 3)],
                'odds': {
                    FABIO_FOGNINI: 1.45,
                    FEDERICO_DELBONIS: 2.70
                }
            },
            {
                'round': 64,
                'players': [
                    JUAN_MARTIN_DEL_POTRO,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(5, 7), (6, 4), (6, 2), (6, 7), (6, 2)],
                'odds': {
                    JUAN_MARTIN_DEL_POTRO: 1.07,
                    YOSHIHITO_NISHIOKA: 7.50
                }
            },
            {
                'round': 64,
                'players': [
                    ALEXANDER_ZVEREV,
                    MIKAEL_YMER
                ],
                'score': [(6, 1), (6, 3), (7, 6)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.13,
                    MIKAEL_YMER: 6.50
                }
            },
            {
                'round': 64,
                'players': [
                    DOMINIC_THIEM,
                    ALEXANDER_BUBLIK
                ],
                'score': [(6, 3), (6, 7), (6, 3), (7, 5)],
                'odds': {
                    DOMINIC_THIEM: 1.01,
                    ALEXANDER_BUBLIK: 19.00
                }
            },
            {
                'round': 64,
                'players': [
                    NOVAK_DJOKOVIC,
                    HENRI_LAAKSONEN
                ],
                'score': [(6, 1), (6, 4), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    HENRI_LAAKSONEN: 22.74
                }
            },

            # 2019-05-31
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(6, 2), (4, 6), (7, 6)],
                'retired': True,
                'odds': {
                    BENOIT_PAIRE: 2.22,
                    PABLO_CARRENO_BUSTA: 1.56
                }
            },
            {
                'round': 32,
                'players': [
                    LEONARDO_MAYER,
                    NICOLAS_MAHUT
                ],
                'score': [(3, 6), (7, 6), (6, 4), (7, 6)],
                'odds': {
                    LEONARDO_MAYER: 1.24,
                    NICOLAS_MAHUT: 3.75
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    CORENTIN_MOUTET
                ],
                'score': [(2, 6), (6, 3), (6, 4), (5, 7), (6, 4)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.56,
                    CORENTIN_MOUTET: 2.36
                }
            },
            {
                'round': 32,
                'players': [
                    KEI_NISHIKORI,
                    LASLO_DJERE
                ],
                'score': [(6, 4), (6, 7), (6, 3), (4, 6), (8, 6)],
                'odds': {
                    KEI_NISHIKORI: 1.31,
                    LASLO_DJERE: 3.63
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    CASPER_RUUD
                ],
                'score': [(6, 3), (6, 1), 7, 6],
                'odds': {
                    ROGER_FEDERER: 1.12,
                    CASPER_RUUD: 6.00
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    DAVID_GOFFIN
                ],
                'score': [(6, 1), (6, 3), (4, 6), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.02,
                    DAVID_GOFFIN: 13.32
                }
            },

            # 2019-06-01
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    GRIGOR_DIMITROV
                ],
                'score': [(7, 6), (7, 6), (7, 6)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    ANTOINE_HOANG
                ],
                'score': [(6, 3), (6, 2), (6, 3)],
                'odds': {
                    GAEL_MONFILS: 1.07,
                    ANTOINE_HOANG: 7.50
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    BORNA_CORIC
                ],
                'score': [(4, 6), (6, 1), (4, 6), (7, 6), (11, 9)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.92,
                    BORNA_CORIC: 1.40
                }
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 1), (6, 4), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 1.28,
                    MARTIN_KLIZAN: 3.60
                }
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(7, 6), (6, 4), (4, 6), (6, 1)],
                'odds': {
                    FABIO_FOGNINI: 1.67,
                    ROBERTO_BAUTISTA_AGUT: 2.19
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_MARTIN_DEL_POTRO,
                    JORDAN_THOMPSON
                ],
                'score': [(6, 4), (6, 4), (6, 0)],
                'odds': {
                    JUAN_MARTIN_DEL_POTRO: 1.27,
                    JORDAN_THOMPSON: 3.75
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    FILIP_KRAJINOVIC
                ],
                'score': [(7, 5), (6, 3), (6, 7), (7, 6)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 4), (6, 2), (4, 6), (1, 6), (6, 2)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.31,
                    DUSAN_LAJOVIC: 3.63
                }
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    PABLO_CUEVAS
                ],
                'score': [(6, 3), (4, 6), (6, 2), (7, 5)],
                'odds': {
                    DOMINIC_THIEM: 1.21,
                    PABLO_CUEVAS: 4.20
                }
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    SALVATORE_CARUSO
                ],
                'score': [(6, 3), (6, 3), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    SALVATORE_CARUSO: 20.86
                }
            },

            # 2019-06-02
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(7, 6), (5, 7), (6, 4), (3, 6), (8, 6)],
                'odds': {
                    STAN_WAWRINKA: 2.10,
                    STEFANOS_TSITSIPAS: 1.71
                }
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    LEONARDO_MAYER
                ],
                'score': [(6, 2), (6, 3), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.07,
                    LEONARDO_MAYER: 8.00
                }
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 2), (6, 3), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    JUAN_IGNACIO_LONDERO: 23.00
                }
            },

            # 2019-06-03
            {
                'round': 16,
                'players': [
                    KAREN_KHACHANOV,
                    JUAN_MARTIN_DEL_POTRO
                ],
                'score': [(7, 5), (6, 3), (3, 6), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 2.75,
                    JUAN_MARTIN_DEL_POTRO: 1.41
                }
            },
            {
                'round': 16,
                'players': [
                    KEI_NISHIKORI,
                    BENOIT_PAIRE
                ],
                'score': [(6, 2), (6, 7), (6, 2), (6, 7), (6, 2)],
                # no odds
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    FABIO_FOGNINI
                ],
                'score': [(3, 6), (6, 2), (6, 2), (7, 6)],
                'odds': {
                    ALEXANDER_ZVEREV: 2.06,
                    FABIO_FOGNINI: 1.74
                }
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    GAEL_MONFILS
                ],
                'score': [(6, 4), (6, 4), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.36,
                    GAEL_MONFILS: 3.15
                }
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 3), (6, 2), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.04,
                    JAN_LENNARD_STRUFF: 13.00
                }
            },

            # 2019-06-04
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    STAN_WAWRINKA
                ],
                'score': [(7, 6), (4, 6), (7, 6), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.22,
                    STAN_WAWRINKA: 3.05
                }
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    KEI_NISHIKORI
                ],
                'score': [(6, 1), (6, 1), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.02,
                    KEI_NISHIKORI: 14.75
                }
            },

            # 2019-06-06
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 2), (6, 4), (6, 2)],
                'odds': {
                    DOMINIC_THIEM: 1.27,
                    KAREN_KHACHANOV: 3.75
                }
            },
            {
                'round': 8,
                'players': [
                    NOVAK_DJOKOVIC,
                    ALEXANDER_ZVEREV
                ],
                'score': [(7, 5), (6, 2), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.13,
                    ALEXANDER_ZVEREV: 7.07
                }
            },

            # 2019-06-07
            {
                'round': 4,
                'players': [
                    RAFAEL_NADAL,
                    ROGER_FEDERER
                ],
                'score': [(6, 3), (6, 4), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.13,
                    ROGER_FEDERER: 6.00
                }
            },

            # 2019-06-08
            {
                'round': 4,
                'players': [
                    DOMINIC_THIEM,
                    NOVAK_DJOKOVIC
                ],
                'score': [(6, 2), (3, 6), (7, 5), (5, 7), (7, 5)],
                'odds': {
                    DOMINIC_THIEM: 1.20,
                    NOVAK_DJOKOVIC: 2.05
                }
            },

            # 2019-06-09
            {
                'round': 2,
                'players': [
                    RAFAEL_NADAL,
                    DOMINIC_THIEM
                ],
                'score': [(6, 3), (5, 7), (6, 1), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.19,
                    DOMINIC_THIEM: 4.75
                }
            }
        ]
    },

    {
        'name': 'MercedesCup',
        'date': '2019-06-10',
        'location': 'Stuttgart, Germany',
        'matches': [
            {
                'round': 512,
                'players': [
                    GREGOIRE_BARRERE,
                    SASI_KUMAR_MUKUND,
                ],
                'score': [
                    (6, 3), (6, 4)
                ],
                'odds': {
                    GREGOIRE_BARRERE: 1.22,
                    SASI_KUMAR_MUKUND: 3.90
                }
            },
            {
                'round': 512,
                'players': [
                    SERGIY_STAKHOVSKY,
                    ADRIAN_MENENDEZ_MACEIRAS,
                ],
                'score': [
                    (6, 3), (6, 4)
                ],
                'odds': {
                    SERGIY_STAKHOVSKY: 1.39,
                    ADRIAN_MENENDEZ_MACEIRAS: 2.75
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    MAVERICK_BANES,
                ],
                'score': [
                    (4, 6), (6, 3), (7, 6)
                ],
                'odds': {
                    ALEXEI_POPYRIN: 1.18,
                    MAVERICK_BANES: 4.65
                }
            },
            {
                'round': 512,
                'players': [
                    FELICIANO_LOPEZ,
                    TIM_PUETZ,
                ],
                'score': [
                    (7, 6), (7, 5)
                ],
                'odds': {
                    FELICIANO_LOPEZ: 1.22,
                    TIM_PUETZ: 4.00
                }
            },
            {
                'round': 512,
                'players': [
                    VIKTOR_GALOVIC,
                    BRAYDEN_SCHNUR,
                ],
                'score': [
                    (4, 6), (6, 3), (6, 4)
                ],
                'odds': {
                    VIKTOR_GALOVIC: 2.75,
                    BRAYDEN_SCHNUR: 1.40
                }
            },
            {
                'round': 512,
                'players': [
                    DUSTIN_BROWN,
                    DENIS_ISTOMIN,
                ],
                'score': [
                    (7, 5), (6, 4)
                ],
                'odds': {
                    DUSTIN_BROWN: 1.77,
                    DENIS_ISTOMIN: 1.91
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXANDER_BUBLIK,
                    HIROKI_MORIYA,
                ],
                'score': [
                    (6, 0), (6, 3)
                ],
                'odds': {
                    ALEXANDER_BUBLIK: 1.27,
                    HIROKI_MORIYA: 3.55
                }
            },
            {
                'round': 512,
                'players': [
                    MATTEO_VIOLA,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [
                    (6, 7), (7, 6), (2, 1)
                ],
                'retired': True,
                'odds': {
                    MATTEO_VIOLA: 3.55,
                    PRAJNESH_GUNNESWARAN: 1.27
                }
            },

            {
                'round': 256,
                'players': [
                    DUSTIN_BROWN,
                    GREGOIRE_BARRERE
                ],
                'score': [
                    (6, 2), (7, 6)
                ],
                'odds': {
                    DUSTIN_BROWN: 1.71,
                    GREGOIRE_BARRERE: 1.95
                }
            },
            {
                'round': 256,
                'players': [
                    VIKTOR_GALOVIC,
                    SERGIY_STAKHOVSKY
                ],
                'score': [
                    (6, 4), (2, 6), (6, 4)
                ],
                'odds': {
                    VIKTOR_GALOVIC: 3.16,
                    SERGIY_STAKHOVSKY: 1.32
                }
            },
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    MATTEO_VIOLA
                ],
                'score': [
                    (6, 3), (7, 5)
                ],
                'odds': {
                    ALEXEI_POPYRIN: 1.30,
                    MATTEO_VIOLA: 3.45
                }
            },
            {
                'round': 256,
                'players': [
                    FELICIANO_LOPEZ,
                    ALEXANDER_BUBLIK
                ],
                'score': [
                    (7, 5), (6, 4)
                ],
                'odds': {
                    FELICIANO_LOPEZ: 1.61,
                    ALEXANDER_BUBLIK: 2.20
                }
            },

            {
                'round': 32,
                'players': [
                    JO_WILFRIED_TSONGA,
                    MISCHA_ZVEREV,
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.24,
                    MISCHA_ZVEREV: 4.22
                }
            },
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    PETER_GOJOWCZYK
                ],
                'score': [(4, 6), (6, 2), (6, 3)],
                'odds': {
                    GILLES_SIMON: 1.67,
                    PETER_GOJOWCZYK: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    LUCAS_POUILLE,
                    FELICIANO_LOPEZ
                ],
                'score': [(6, 3), (3, 6), (7, 6)],
                'odds': {
                    LUCAS_POUILLE: 1.87,
                    FELICIANO_LOPEZ: 1.91
                }
            },
            {
                'round': 32,
                'players': [
                    DENIS_KUDLA,
                    VIKTOR_GALOVIC
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    DENIS_KUDLA: 1.26,
                    VIKTOR_GALOVIC: 4.02
                }
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(4, 6), (7, 5), (6, 3)],
                'odds': {
                    MIOMIR_KECMANOVIC: 5.32,
                    PHILIPP_KOHLSCHREIBER: 1.17
                }
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    JAUME_MUNAR
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    MARTON_FUCSOVICS: 1.32,
                    JAUME_MUNAR: 3.55
                }
            },
            {
                'round': 32,
                'players': [
                    DUSTIN_BROWN,
                    JOHN_MILLMAN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DUSTIN_BROWN: 2.05,
                    JOHN_MILLMAN: 1.77
                }
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    NICK_KYRGIOS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 2.77,
                    NICK_KYRGIOS: 1.45
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    DENIS_SHAPOVALOV
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.13,
                    DENIS_SHAPOVALOV: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    ERNESTS_GULBIS
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.64,
                    ERNESTS_GULBIS: 2.25
                }
            },
            {
                'round': 32,
                'players': [
                    MILOS_RAONIC,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 7), (6, 4), (7, 6)],
                'odds': {
                    MILOS_RAONIC: 1.28,
                    ALEXEI_POPYRIN: 3.80
                }
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    STEVE_JOHNSON
                ],
                'score': [(7, 5), (5, 7), (7, 6)],
                'odds': {
                    GAEL_MONFILS: 1.42,
                    STEVE_JOHNSON: 2.90
                }
            },

            {
                'round': 16,
                'players': [
                    JAN_LENNARD_STRUFF,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.28,
                    MIOMIR_KECMANOVIC: 3.60
                }
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    GILLES_SIMON
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.48,
                    GILLES_SIMON: 2.60
                }
            },
            {
                'round': 16,
                'players': [
                    MILOS_RAONIC,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    MILOS_RAONIC: 2.15,
                    JO_WILFRIED_TSONGA: 1.71
                }
            },
            {
                'round': 16,
                'players': [
                    DENIS_KUDLA,
                    GAEL_MONFILS
                ],
                'score': [(7, 5), (6, 7), (7, 6)],
                'odds': {
                    DENIS_KUDLA: 2.81,
                    GAEL_MONFILS: 1.43
                }
            },
            {
                'round': 16,
                'players': [
                    MARTON_FUCSOVICS,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(6, 7), (6, 2), (7, 5)],
                'odds': {
                    MARTON_FUCSOVICS: 1.54,
                    NIKOLOZ_BASILASHVILI: 2.54
                }
            },
            {
                'round': 16,
                'players': [
                    LUCAS_POUILLE,
                    DANILL_MEDVEDEV
                ],
                'score': [(7, 6), (4, 6), (6, 2)],
                'odds': {
                    LUCAS_POUILLE: 2.66,
                    DANILL_MEDVEDEV: 1.48
                }
            },
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 1.95,
                    KAREN_KHACHANOV: 1.74
                }
            },
            {
                'round': 16,
                'players': [
                    DUSTIN_BROWN,
                    ALEXANDER_ZVEREV
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    DUSTIN_BROWN: 4.02,
                    ALEXANDER_ZVEREV: 1.24
                }
            },

            {
                'round': 8,
                'players': [
                    JAN_LENNARD_STRUFF,
                    LUCAS_POUILLE
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.80,
                    LUCAS_POUILLE: 2.01
                }
            },
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    DENIS_KUDLA
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.49,
                    DENIS_KUDLA: 2.61
                }
            },
            {
                'round': 8,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    DUSTIN_BROWN
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.60,
                    DUSTIN_BROWN: 2.44
                }
            },
            {
                'round': 8,
                'players': [
                    MILOS_RAONIC,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MILOS_RAONIC: 1.36,
                    MARTON_FUCSOVICS: 3.07
                }
            },

            {
                'round': 4,
                'players': [
                    MATTEO_BERRETTINI,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    MATTEO_BERRETTINI: 1.76,
                    JAN_LENNARD_STRUFF: 2.10
                }
            },
            {
                'round': 4,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    MILOS_RAONIC
                ],
                'score': [],
                'wo': True,
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.84,
                    MILOS_RAONIC: 1.44
                }
            },

            {
                'round': 2,
                'players': [
                    MATTEO_BERRETTINI,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 1.47,
                    FELIX_AUGER_ALIASSIME: 2.70
                }
            }
        ]
    }
]
