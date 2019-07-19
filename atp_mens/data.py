from men import *

DATA = [
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
                    MATTEO_BARRETTINI,
                    PABLO_ANDUJAR
                ],
                'score': [(6, 7), (6, 4), (6, 4), (6, 2)],
                'odds': {
                    MATTEO_BARRETTINI: 1.19,
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
                    CHRISTIAN_GARIN,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (7, 5), (7, 6)],
                'odds': {
                    CHRISTIAN_GARIN: 1.37,
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
                    MATTEO_BARRETTINI
                ],
                'score': [(6, 4), (7, 5), (6, 3)],
                'odds': {
                    CASPER_RUUD: 2.55,
                    MATTEO_BARRETTINI: 1.51
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
                    CHRISTIAN_GARIN
                ],
                'score': [(6, 1), (6, 4), (6, 0)],
                'odds': {
                    STAN_WAWRINKA: 1.53,
                    CHRISTIAN_GARIN: 2.50
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
                'round': 'Q1',
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
                'round': 'Q1',
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
                'round': 'Q1',
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
                'round': 'Q1',
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
                'round': 'Q1',
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
                'round': 'Q1',
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
                'round': 'Q1',
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
                'round': 'Q1',
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
                'round': 'Q2',
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
                'round': 'Q2',
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
                'round': 'Q2',
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
                'round': 'Q2',
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
                    MATTEO_BARRETTINI,
                    NICK_KYRGIOS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MATTEO_BARRETTINI: 2.77,
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
                    MATTEO_BARRETTINI,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MATTEO_BARRETTINI: 1.95,
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
                    MATTEO_BARRETTINI,
                    DENIS_KUDLA
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    MATTEO_BARRETTINI: 1.49,
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
                    MATTEO_BARRETTINI,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    MATTEO_BARRETTINI: 1.76,
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
                    MATTEO_BARRETTINI,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    MATTEO_BARRETTINI: 1.47,
                    FELIX_AUGER_ALIASSIME: 2.70
                }
            }
        ]
    }
]

PREDICTIONS = []
