from men import *
from location import *

# acc   roi     profit  desc
# 67.7  17.8    244     opt speed       0:100%
# 67.7  19.4    288     opt step/subsample/scale
# 67.8  20.0    283     opt surface     0:100%
# 68.0  17.0    393     opt gamma/mdepth/mchildw            (2, 689), (3, 80), (6, 60), (5, 56)
# 67.8  14.7    341     2019-08-20
# 69.5  22.8    554     opt doors   0:740 1:148
# 69.8  19.7    452     opt estimators and learning rate           (2, 673), (3, 90), (6, 62), (5, 51)

# 69.4  17.0  389    opt win and loss ('bet_wnl_multi-2', 110)  (2, 675), (3, 87), (6, 61), (5, 52)
# 69.9  14.9  550    opt upsets                             (2, 446), (5, 197), (4, 107), (6, 71)
# 68.6  17.9  590    added tie-breaker                      (2, 373), (5, 195), (4, 85), (6, 65)
# 69.9  17.5  743    added games param
# 67.5  14.1  555    removed whitewashes 1% useful

# 71.8  23.2  865    2019-08-16
# 68.4  7.6   228    added drs_bet, drs_cutoff              (1, 368), (3, 108), (7, 108), (4, 95)
# 68.9  4.7   45     opt learning_rate, gamma, max_depth, min_child_weight  (1, 784)
# 66.2  6.1   59     merged params

# 66.2  -1.2  -19    hyper updated and cutoffs moved to bet params, bounds within 50
# 67.4  1.1   15     optimized

# 68.1  7.4   105    optimized
# 68.8  6.2   75     optimized                              (1, 480), (2, 184), (3, 120)

# 65.7  9.7   335    upsets bet param added


DATA = [
    {
        'location': WIMBLEDON,
        'date': '2019-07-14',
        'matches': [

            # 2019-07-01
            {
                'round': 128,
                'players': [
                    FERNANDO_VERDASCO,
                    KAMIL_MAJCHRZAK
                ],
                'score': [(6, 4), (6, 4), (6, 4)],
                'odds': {
                    FERNANDO_VERDASCO: 1.95,
                    KAMIL_MAJCHRZAK: 1.87
                }
            },
            {
                'round': 128,
                'players': [
                    JANKO_TIPSAREVIC,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 4), (6, 7), (6, 2), (5, 7), (6, 2)],
                'odds': {
                    JANKO_TIPSAREVIC: 2.10,
                    YOSHIHITO_NISHIOKA: 1.29
                }
            },
            {
                'round': 128,
                'players': [
                    ANDREAS_SEPPI,
                    NICOLAS_JARRY
                ],
                'score': [(6, 3), (6, 7), (6, 1), (6, 2)],
                'odds': {
                    ANDREAS_SEPPI: 1.91,
                    NICOLAS_JARRY: 1.85
                }
            },
            {
                'round': 128,
                'players': [
                    ALEXEI_POPYRIN,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(7, 6), (7, 5), (6, 2)],
                'odds': {
                    ALEXEI_POPYRIN: 1.61,
                    PABLO_CARRENO_BUSTA: 2.30
                }
            },
            {
                'round': 128,
                'players': [
                    REILLY_OPELKA,
                    CEDRIC_MARCEL_STEBE
                ],
                'score': [(7, 6), (7, 5), (6, 2)],
                'odds': {
                    REILLY_OPELKA: 1.12,
                    CEDRIC_MARCEL_STEBE: 3.10
                }
            },
            {
                'round': 128,
                'players': [
                    CORENTIN_MOUTET,
                    GRIGOR_DIMITROV
                ],
                'score': [(2, 6), (3, 6), (7, 6), (6, 3), (6, 1)],
                'odds': {
                    CORENTIN_MOUTET: 4.70,
                    GRIGOR_DIMITROV: 1.19
                }
            },
            {
                'round': 128,
                'players': [
                    LEONARDO_MAYER,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 1), (7, 6), (6, 2)],
                'odds': {
                    LEONARDO_MAYER: 1.89,
                    ERNESTS_GULBIS: 1.87
                }
            },
            {
                'round': 128,
                'players': [
                    FELICIANO_LOPEZ,
                    MARCOS_GIRON
                ],
                'score': [(6, 4), (6, 2), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 1.25,
                    MARCOS_GIRON: 4.00
                }
            },
            {
                'round': 128,
                'players': [
                    DENIS_KUDLA,
                    MALEK_JAZIRI
                ],
                'score': [(6, 4), (6, 1), (6, 3)],
                'odds': {
                    DENIS_KUDLA: 1.13,
                    MALEK_JAZIRI: 5.50
                }
            },
            {
                'round': 128,
                'players': [
                    MIOMIR_KECMANOVIC,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(2, 6), (6, 3), (6, 3), (6, 1)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.43,
                    ROBERTO_CARBALLES_BAENA: 2.95
                }
            },
            {
                'round': 128,
                'players': [
                    IVO_KARLOVIC,
                    ANDREA_ARNABOLDI
                ],
                'score': [(6, 4), (6, 4), (7, 6)],
                'odds': {
                    IVO_KARLOVIC: 1.25,
                    ANDREA_ARNABOLDI: 3.87
                }
            },
            {
                'round': 128,
                'players': [
                    ROBIN_HAASE,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 1), (6, 3), (6, 1)],
                'odds': {
                    ROBIN_HAASE: 1.27,
                    JOZEF_KOVALIK: 3.90
                }
            },
            {
                'round': 128,
                'players': [
                    MARCEL_GRANOLLERS,
                    LORENZO_SONEGO
                ],
                'score': [(7, 6), (6, 4), (6, 4)],
                'odds': {
                    MARCEL_GRANOLLERS: 2.20,
                    LORENZO_SONEGO: 1.67
                }
            },
            {
                'round': 128,
                'players': [
                    STEVE_DARCIS,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 2), (6, 4), (6, 4)],
                'odds': {
                    STEVE_DARCIS: 1.67,
                    MISCHA_ZVEREV: 2.22
                }
            },
            {
                'round': 128,
                'players': [
                    PABLO_CUEVAS,
                    DAMIR_DZUMHUR
                ],
                'score': [(4, 6), (7, 6), (2, 6), (6, 4), (6, 2)],
                'odds': {
                    PABLO_CUEVAS: 1.83,
                    DAMIR_DZUMHUR: 1.92
                }
            },
            {
                'round': 128,
                'players': [
                    JEREMY_CHARDY,
                    MARTIN_KLIZAN
                ],
                'score': [(3, 6), (6, 0), (6, 3), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 1.26,
                    MARTIN_KLIZAN: 3.90
                }
            },
            {
                'round': 128,
                'players': [
                    HUBERT_HURKACZ,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 3), (4, 6), (6, 4), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 1.32,
                    DUSAN_LAJOVIC: 3.31
                }
            },
            {
                'round': 128,
                'players': [
                    KYLE_EDMUND,
                    JAUME_MUNAR
                ],
                'score': [(6, 4), (6, 4), (6, 4)],
                'odds': {
                    KYLE_EDMUND: 1.11,
                    JAUME_MUNAR: 6.50
                }
            },
            {
                'round': 128,
                'players': [
                    BENOIT_PAIRE,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(4, 6), (6, 4), (6, 4), (7, 6)],
                'odds': {
                    BENOIT_PAIRE: 1.26,
                    JUAN_IGNACIO_LONDERO: 3.55
                }
            },
            {
                'round': 128,
                'players': [
                    GUIDO_PELLA,
                    MARIUS_COPIL
                ],
                'score': [(7, 6), (5, 7), (6, 3), (6, 4)],
                'odds': {
                    GUIDO_PELLA: 1.91,
                    MARIUS_COPIL: 1.83
                }
            },
            {
                'round': 128,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 3), (6, 2), (6, 3)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.04,
                    PETER_GOJOWCZYK: 11.00
                }
            },
            {
                'round': 128,
                'players': [
                    STAN_WAWRINKA,
                    RUBEN_BEMELMANS
                ],
                'score': [(6, 3), (6, 2), (6, 2)],
                'odds': {
                    STAN_WAWRINKA: 1.14,
                    RUBEN_BEMELMANS: 5.50
                }
            },
            {
                'round': 128,
                'players': [
                    DAVID_GOFFIN,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 4), (6, 4), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 1.02,
                    BRADLEY_KLAHN: 13.00
                }
            },
            {
                'round': 128,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    VASEK_POSPISIL
                ],
                'score': [(5, 7), (6, 2), (6, 4), (6, 3)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.06,
                    VASEK_POSPISIL: 10.50
                }
            },
            {
                'round': 128,
                'players': [
                    UGO_HUMBERT,
                    GAEL_MONFILS
                ],
                'score': [(6, 7), (3, 6), (6, 4), (7, 5), (3, 0)],
                'odds': {
                    UGO_HUMBERT: 3.40,
                    GAEL_MONFILS: 1.30
                }
            },
            {
                'round': 128,
                'players': [
                    MILOS_RAONIC,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(7, 6), (6, 4), (6, 2)],
                'odds': {
                    MILOS_RAONIC: 1.04,
                    PRAJNESH_GUNNESWARAN: 14.30
                }
            },
            {
                'round': 128,
                'players': [
                    DANILL_MEDVEDEV,
                    PAOLO_LORENZI
                ],
                'score': [(6, 3), (7, 6), (7, 6)],
                'odds': {
                    DANILL_MEDVEDEV: 1.01,
                    PAOLO_LORENZI: 33.64
                }
            },
            {
                'round': 128,
                'players': [
                    KAREN_KHACHANOV,
                    SOONWOO_KWON
                ],
                'score': [(7, 6), (6, 4), (4, 6), (7, 5)],
                'odds': {
                    KAREN_KHACHANOV: 1.27,
                    SOONWOO_KWON: 3.55
                }
            },
            {
                'round': 128,
                'players': [
                    THOMAS_FABBIANO,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 4), (3, 6), (6, 4), (6, 7), (6, 3)],
                'odds': {
                    THOMAS_FABBIANO: 7.50,
                    STEFANOS_TSITSIPAS: 1.10
                }
            },
            {
                'round': 128,
                'players': [
                    JIRI_VESELY,
                    ALEXANDER_ZVEREV
                ],
                'score': [(4, 6), (6, 3), (6, 2), (7, 5)],
                'odds': {
                    JIRI_VESELY: 4.45,
                    ALEXANDER_ZVEREV: 1.21
                }
            },
            {
                'round': 128,
                'players': [
                    KEVIN_ANDERSON,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 3), (6, 4), (6, 2)],
                'odds': {
                    KEVIN_ANDERSON: 1.34,
                    PIERRE_HUGUES_HERBERT: 3.20
                }
            },
            {
                'round': 128,
                'players': [
                    NOVAK_DJOKOVIC,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 3), (7, 5), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.02,
                    PHILIPP_KOHLSCHREIBER: 22.59
                }
            },

            # 2019-07-02
            {
                'round': 128,
                'players': [
                    JO_WILFRIED_TSONGA,
                    BERNARD_TOMIC
                ],
                'score': [(6, 2), (6, 1), (6, 4)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.17,
                    BERNARD_TOMIC: 4.85
                }
            },
            {
                'round': 128,
                'players': [
                    JOAO_SOUSA,
                    PAUL_JUBB
                ],
                'score': [(6, 0), (6, 3), (6, 7), (6, 1)],
                'odds': {
                    JOAO_SOUSA: 1.22,
                    PAUL_JUBB: 4.15
                }
            },
            {
                'round': 128,
                'players': [
                    TENNYS_SANDGREN,
                    YASUTAKA_UCHIYAMA
                ],
                'score': [(3, 6), (6, 2), (6, 4), (6, 3)],
                'odds': {
                    TENNYS_SANDGREN: 1.71,
                    YASUTAKA_UCHIYAMA: 2.10
                }
            },
            {
                'round': 128,
                'players': [
                    ANDREY_RUBLEV,
                    CHRISTIAN_GARIN
                ],
                'score': [(4, 6), (6, 4), (7, 5), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 2.55,
                    CHRISTIAN_GARIN: 1.53
                }
            },
            {
                'round': 128,
                'players': [
                    CAMERON_NORRIE,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 2), (6, 4), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 1.51,
                    DENIS_ISTOMIN: 2.55
                }
            },
            {
                'round': 128,
                'players': [
                    JOHN_MILLMAN,
                    HUGO_DELLIEN
                ],
                'score': [(6, 2), (6, 3), (6, 4)],
                'odds': {
                    JOHN_MILLMAN: 1.06,
                    HUGO_DELLIEN: 8.50
                }
            },
            {
                'round': 128,
                'players': [
                    NICK_KYRGIOS,
                    JORDAN_THOMPSON
                ],
                'odds': {
                    NICK_KYRGIOS: 1.40,
                    JORDAN_THOMPSON: 3.04
                },
                'score': [(7, 6), (3, 6), (7, 6), (0, 6), (6, 1)]
            },
            {
                'round': 128,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    PABLO_ANDUJAR
                ],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.17,
                    PABLO_ANDUJAR: 4.55
                },
                'score': [(6, 3), (6, 2), (6, 4)]
            },
            {
                'round': 128,
                'players': [
                    DOMINIK_KOEPFER,
                    FILIP_KRAJINOVIC
                ],
                'odds': {
                    DOMINIK_KOEPFER: 1.69,
                    FILIP_KRAJINOVIC: 1.69
                },
                'score': [(6, 3), (4, 6), (7, 6), (6, 1)]
            },
            {
                'round': 128,
                'players': [
                    STEVE_JOHNSON,
                    ALBERT_RAMOS_VINOLAS
                ],
                'odds': {
                    STEVE_JOHNSON: 1.14,
                    ALBERT_RAMOS_VINOLAS: 5.33
                },
                'score': [(6, 4), (6, 2), (6, 3)]
            },
            {
                'round': 128,
                'players': [
                    MARTON_FUCSOVICS,
                    DENNIS_NOVAK
                ],
                'odds': {
                    MARTON_FUCSOVICS: 1.79,
                    DENNIS_NOVAK: 2.05
                },
                'score': [(3, 6), (6, 4), (7, 6), (6, 2)]
            },
            {
                'round': 128,
                'players': [
                    TAYLOR_FRITZ,
                    TOMAS_BERDYCH
                ],
                'odds': {
                    TAYLOR_FRITZ: 1.39,
                    TOMAS_BERDYCH: 2.95
                },
                'score': [(6, 4), (6, 4), (6, 3)]
            },
            {
                'round': 128,
                'players': [
                    DANIEL_EVANS,
                    FEDERICO_DELBONIS
                ],
                'odds': {
                    DANIEL_EVANS: 1.06,
                    FEDERICO_DELBONIS: 9.50
                },
                'score': [(6, 3), (7, 6), (6, 3)]
            },
            {
                'round': 128,
                'players': [
                    JAY_CLARKE,
                    NOAH_RUBIN
                ],
                'odds': {
                    JAY_CLARKE: 2.50,
                    NOAH_RUBIN: 1.53
                },
                'score': [(4, 6), (7, 5), (6, 4), (6, 4)]
            },
            {
                'round': 128,
                'players': [
                    GREGOIRE_BARRERE,
                    ALEXANDER_BUBLIK
                ],
                'odds': {
                    GREGOIRE_BARRERE: 2.10,
                    ALEXANDER_BUBLIK: 1.74
                },
                'score': [(3, 6), (6, 4), (6, 3), (6, 3)]
            },
            {
                'round': 128,
                'players': [
                    MARCOS_BAGHDATIS,
                    BRAYDEN_SCHNUR
                ],
                'odds': {
                    MARCOS_BAGHDATIS: 1.67,
                    BRAYDEN_SCHNUR: 2.15
                },
                'score': [(6, 2), (6, 4), (6, 4)]
            },
            {
                'round': 128,
                'players': [
                    JAN_LENNARD_STRUFF,
                    RADU_ALBOT
                ],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.28,
                    RADU_ALBOT: 3.65
                },
                'score': [(6, 4), (6, 3), (6, 2)]
            },
            {
                'round': 128,
                'players': [
                    LASLO_DJERE,
                    GUIDO_ANDREOZZI
                ],
                'score': [(3, 6), (7, 6), (7, 6), (6, 3)],
                'odds': {
                    LASLO_DJERE: 1.31,
                    GUIDO_ANDREOZZI: 3.40
                },
            },
            {
                'round': 128,
                'players': [
                    RICARDAS_BERANKIS,
                    DENIS_SHAPOVALOV
                ],
                'score': [(7, 6), (6, 4), (6, 3)],
                'odds': {
                    RICARDAS_BERANKIS: 6.75,
                    DENIS_SHAPOVALOV: 1.11
                },
            },
            {
                'round': 128,
                'players': [
                    LUCAS_POUILLE,
                    RICHARD_GASQUET
                ],
                'score': [(7, 6), (6, 4), (6, 3)],
                'odds': {
                    LUCAS_POUILLE: 1.63,
                    RICHARD_GASQUET: 2.24
                }
            },
            {
                'round': 128,
                'players': [
                    ALEX_DE_MINAUR,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 0), (6, 4), (7, 6)],
                'odds': {
                    ALEX_DE_MINAUR: 1.16,
                    MARCO_CECCHINATO: 5.11
                }
            },
            {
                'round': 128,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 4), (3, 6), (6, 3), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.45,
                    MATTHEW_EBDEN: 2.61
                }
            },
            {
                'round': 128,
                'players': [
                    GILLES_SIMON,
                    SALVATORE_CARUSO
                ],
                'score': [(7, 6), (6, 3), (6, 2)],
                'odds': {
                    GILLES_SIMON: 1.25,
                    SALVATORE_CARUSO: 4.25
                }
            },
            {
                'round': 128,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JAMES_WARD
                ],
                'score': [(2, 6), (4, 6), (6, 4), (6, 4), (8, 6)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.59,
                    JAMES_WARD: 2.30
                }
            },
            {
                'round': 128,
                'players': [
                    MATTEO_BERRETTINI,
                    ALJAZ_BEDENE
                ],
                'score': [(3, 6), (6, 3), (6, 2), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 1.15,
                    ALJAZ_BEDENE: 5.00
                }
            },
            {
                'round': 128,
                'players': [
                    MARIN_CILIC,
                    ADRIAN_MANNARINO
                ],
                'score': [(7, 6), (7, 6), (6, 3)],
                'odds': {
                    MARIN_CILIC: 1.30,
                    ADRIAN_MANNARINO: 3.55
                }
            },
            {
                'round': 128,
                'players': [
                    FABIO_FOGNINI,
                    FRANCES_TIAFOE
                ],
                'score': [(5, 7), (6, 4), (6, 3), (4, 6), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.71,
                    FRANCES_TIAFOE: 2.04
                }
            },
            {
                'round': 128,
                'players': [
                    JOHN_ISNER,
                    CASPER_RUUD
                ],
                'score': [(6, 3), (6, 4), (7, 6)],
                'odds': {
                    JOHN_ISNER: 1.24,
                    CASPER_RUUD: 3.85
                }
            },
            {
                'round': 128,
                'players': [
                    KEI_NISHIKORI,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 4), (7, 6), (6, 4)],
                'odds': {
                    KEI_NISHIKORI: 1.05,
                    THIAGO_MONTEIRO: 10.50
                }
            },
            {
                'round': 128,
                'players': [
                    SAM_QUERREY,
                    DOMINIC_THIEM
                ],
                'score': [(6, 7), (7, 6), (6, 3), (6, 0)],
                'odds': {
                    SAM_QUERREY: 2.15,
                    DOMINIC_THIEM: 1.65
                }
            },
            {
                'round': 128,
                'players': [
                    RAFAEL_NADAL,
                    YUICHI_SUGITA
                ],
                'score': [(6, 3), (6, 1), (6, 3)],
                'odds': {
                    RAFAEL_NADAL: 1.03,
                    YUICHI_SUGITA: 17.65
                }
            },
            {
                'round': 128,
                'players': [
                    ROGER_FEDERER,
                    LLOYD_HARRIS
                ],
                'score': [(3, 6), (6, 1), (6, 2), (6, 2)],
                'odds': {
                    ROGER_FEDERER: 1.01,
                    LLOYD_HARRIS: 20.00
                }
            },

            # 2019-07-03
            {
                'round': 64,
                'players': [
                    JIRI_VESELY,
                    PABLO_CUEVAS
                ],
                'score': [(4, 6), (7, 6), (6, 4), (6, 4)],
                'odds': {
                    JIRI_VESELY: 1.28,
                    PABLO_CUEVAS: 3.58
                }
            },
            {
                'round': 64,
                'players': [
                    HUBERT_HURKACZ,
                    LEONARDO_MAYER
                ],
                'score': [(6, 7), (6, 1), (7, 6), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 1.43,
                    LEONARDO_MAYER: 2.80
                }
            },
            {
                'round': 64,
                'players': [
                    UGO_HUMBERT,
                    MARCEL_GRANOLLERS
                ],
                'score': [(6, 4), (7, 6), (7, 5)],
                'odds': {
                    UGO_HUMBERT: 2.22,
                    MARCEL_GRANOLLERS: 1.65
                }
            },
            {
                'round': 64,
                'players': [
                    THOMAS_FABBIANO,
                    IVO_KARLOVIC
                ],
                'score': [(6, 3), (6, 7), (6, 3), (6, 7), (6, 4)],
                'odds': {
                    THOMAS_FABBIANO: 1.91,
                    IVO_KARLOVIC: 1.87
                }
            },
            {
                'round': 64,
                'players': [
                    FERNANDO_VERDASCO,
                    KYLE_EDMUND
                ],
                'score': [(4, 6), (4, 6), (7, 6), (6, 3), (6, 4)],
                'oods': {
                    FERNANDO_VERDASCO: 2.50,
                    KYLE_EDMUND: 1.53
                }
            },
            {
                'round': 64,
                'players': [
                    BENOIT_PAIRE,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(7, 6), (6, 4)],
                'retired': True,
                'odds': {
                    BENOIT_PAIRE: 1.67,
                    MIOMIR_KECMANOVIC: 2.15
                }
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    ANDREAS_SEPPI
                ],
                'score': [(6, 4), (4, 6), (4, 6), (7, 5), (6, 1)],
                'odds': {
                    GUIDO_PELLA: 2.55,
                    ANDREAS_SEPPI: 1.50
                }
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    STEVE_DARCIS
                ],
                'score': [(6, 3), (6, 2), (4, 2)],
                'retired': True,
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.04,
                    STEVE_DARCIS: 10.50
                }
            },
            {
                'round': 64,
                'players': [
                    REILLY_OPELKA,
                    STAN_WAWRINKA
                ],
                'score': [(7, 5), (3, 6), (4, 6), (6, 4), (8, 6)],
                'odds': {
                    REILLY_OPELKA: 4.15,
                    STAN_WAWRINKA: 1.21
                }
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    JEREMY_CHARDY
                ],
                'score': [(6, 2), (6, 4), (6, 3)],
                'odds': {
                    DAVID_GOFFIN: 1.31,
                    JEREMY_CHARDY: 3.50
                }
            },
            {
                'round': 64,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    CORENTIN_MOUTET
                ],
                'score': [(6, 3), (4, 6), (6, 4), (6, 2)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.15,
                    CORENTIN_MOUTET: 5.00
                }
            },
            {
                'round': 64,
                'players': [
                    MILOS_RAONIC,
                    ROBIN_HAASE
                ],
                'score': [(7, 6), (7, 5), (7, 6)],
                'odds': {
                    MILOS_RAONIC: 1.08,
                    ROBIN_HAASE: 7.50
                }
            },
            {
                'round': 64,
                'players': [
                    DANILL_MEDVEDEV,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 7), (6, 1), (6, 4), (6, 4)],
                'odds': {
                    DANILL_MEDVEDEV: 1.21,
                    ALEXEI_POPYRIN: 4.30
                }
            },
            {
                'round': 64,
                'players': [
                    KAREN_KHACHANOV,
                    FELICIANO_LOPEZ
                ],
                'score': [(4, 6), (6, 4), (7, 5), (6, 4)],
                'odds': {
                    KAREN_KHACHANOV: 1.77,
                    FELICIANO_LOPEZ: 2.05
                }
            },
            {
                'round': 64,
                'players': [
                    KEVIN_ANDERSON,
                    JANKO_TIPSAREVIC
                ],
                'score': [(6, 4), (6, 7), (6, 1), (6, 4)],
                'odds': {
                    KEVIN_ANDERSON: 1.06,
                    JANKO_TIPSAREVIC: 9.00
                }
            },
            {
                'round': 64,
                'players': [
                    NOVAK_DJOKOVIC,
                    DENIS_KUDLA
                ],
                'score': [(6, 3), (6, 2), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    DENIS_KUDLA: 21.00
                }
            },

            # 2019-07-04
            {
                'round': 64,
                'players': [
                    JO_WILFRIED_TSONGA,
                    RICARDAS_BERANKIS
                ],
                'score': [(7, 6), (6, 3), (6, 3)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.08,
                    RICARDAS_BERANKIS: 7.50
                }
            },
            {
                'round': 64,
                'players': [
                    SAM_QUERREY,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 3), (6, 2), (6, 3)],
                'odds': {
                    SAM_QUERREY: 1.17,
                    ANDREY_RUBLEV: 5.00
                }
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 4), (6, 3), (5, 7), (7, 6)],
                'odds': {
                    JAN_LENNARD_STRUFF: 2.12,
                    TAYLOR_FRITZ: 1.63
                }
            },
            {
                'round': 64,
                'players': [
                    JOHN_MILLMAN,
                    LASLO_DJERE
                ],
                'score': [(6, 3), (6, 2), (6, 1)],
                'odds': {
                    JOHN_MILLMAN: 1.29,
                    LASLO_DJERE: 3.60
                }
            },
            {
                'round': 64,
                'players': [
                    LUCAS_POUILLE,
                    GREGOIRE_BARRERE
                ],
                'score': [(6, 1), (7, 6), (6, 4)],
                'odds': {
                    LUCAS_POUILLE: 1.15,
                    GREGOIRE_BARRERE: 4.50
                }
            },
            {
                'round': 64,
                'players': [
                    STEVE_JOHNSON,
                    ALEX_DE_MINAUR
                ],
                'score': [(3, 6), (7, 6), (6, 3), (3, 6), (6, 3)],
                'odds': {
                    STEVE_JOHNSON: 2.29,
                    ALEX_DE_MINAUR: 1.56
                }
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    DOMINIK_KOEPFER
                ],
                'score': [(6, 0), (6, 3), (7, 5)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.39,
                    DOMINIK_KOEPFER: 2.95
                }
            },
            {
                'round': 64,
                'players': [
                    TENNYS_SANDGREN,
                    GILLES_SIMON
                ],
                'score': [(6, 2), (6, 3), (4, 6), (3, 6), (8, 6)],
                'odds': {
                    TENNYS_SANDGREN: 4.29,
                    GILLES_SIMON: 1.21
                }
            },
            {
                'round': 64,
                'players': [
                    DANIEL_EVANS,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(6, 3), (6, 2), (7, 6)],
                'odds': {
                    DANIEL_EVANS: 1.24,
                    NIKOLOZ_BASILASHVILI: 3.70
                }
            },
            {
                'round': 64,
                'players': [
                    MATTEO_BERRETTINI,
                    MARCOS_BAGHDATIS
                ],
                'score': [(6, 1), (7, 6), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.13,
                    MARCOS_BAGHDATIS: 6.00
                }
            },
            {
                'round': 64,
                'players': [
                    JOAO_SOUSA,
                    MARIN_CILIC
                ],
                'score': [(6, 4), (6, 4), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 7.00,
                    MARIN_CILIC: 1.10
                }
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 7), (6, 4), (7, 6), (2, 6), (6, 3)],
                'odds': {
                    FABIO_FOGNINI: 1.71,
                    MARTON_FUCSOVICS: 2.10
                }
            },
            {
                'round': 64,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    JOHN_ISNER
                ],
                'score': [(6, 4), (6, 7), (4, 6), (6, 1), (6, 4)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 4.00,
                    JOHN_ISNER: 1.21
                }
            },
            {
                'round': 64,
                'players': [
                    KEI_NISHIKORI,
                    CAMERON_NORRIE
                ],
                'score': [(6, 4), (6, 4), (6, 0)],
                'odds': {
                    KEI_NISHIKORI: 1.13,
                    CAMERON_NORRIE: 5.50
                }
            },
            {
                'round': 64,
                'players': [
                    RAFAEL_NADAL,
                    NICK_KYRGIOS
                ],
                'score': [(6, 3), (3, 6), (7, 6), (7, 6)],
                'odds': {
                    RAFAEL_NADAL: 1.25,
                    NICK_KYRGIOS: 4.00
                }
            },
            {
                'round': 64,
                'players': [
                    ROGER_FEDERER,
                    JAY_CLARKE
                ],
                'score': [(6, 1), (7, 6), (6, 2)],
                'odds': {
                    ROGER_FEDERER: 1.10,
                    JAY_CLARKE: 26.00
                }
            },

            # 2019-07-05
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 4), (7, 6), (6, 4)],
                'odds': {
                    FERNANDO_VERDASCO: 1.58,
                    THOMAS_FABBIANO: 2.40
                }
            },
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    JIRI_VESELY
                ],
                'score': [(5, 7), (7, 6), (6, 3), (7, 6)],
                'odds': {
                    BENOIT_PAIRE: 1.80,
                    JIRI_VESELY: 1.94
                }
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 4), (7, 5), (6, 3)],
                'odds': {
                    UGO_HUMBERT: 4.10,
                    FELIX_AUGER_ALIASSIME: 1.22
                }
            },
            {
                'round': 32,
                'players': [
                    MILOS_RAONIC,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (6, 2), (6, 1)],
                'odds': {
                    MILOS_RAONIC: 1.34,
                    REILLY_OPELKA: 3.20
                }
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    DANILL_MEDVEDEV
                ],
                'score': [(4, 6), (6, 2), (3, 6), (6, 3), (7, 5)],
                'odds': {
                    DAVID_GOFFIN: 1.91,
                    DANILL_MEDVEDEV: 1.91
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 3), (7, 6), (6, 1)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.50,
                    KAREN_KHACHANOV: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    KEVIN_ANDERSON
                ],
                'score': [(6, 4), (6, 3), (7, 6)],
                'odds': {
                    GUIDO_PELLA: 5.75,
                    KEVIN_ANDERSON: 1.14
                }
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    HUBERT_HURKACZ
                ],
                'score': [(7, 5), (6, 7), (6, 1), (6, 4)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.02,
                    HUBERT_HURKACZ: 23.00
                }
            },

            # 2019-07-06
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    DANIEL_EVANS
                ],
                'score': [(4, 6), (6, 4), (7, 5), (4, 6), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 2.95,
                    DANIEL_EVANS: 1.36
                }
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    JOHN_MILLMAN
                ],
                'score': [(7, 6), (7, 6), (6, 3)],
                'odds': {
                    SAM_QUERREY: 1.25,
                    JOHN_MILLMAN: 3.80
                }
            },
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 3), (7, 6), (4, 6), (7, 5)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 3.90,
                    JAN_LENNARD_STRUFF: 1.24
                }
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 7), (7, 6), (4, 6), (7, 6), (6, 3)],
                'odds': {
                    MATTEO_BERRETTINI: 1.32,
                    DIEGO_SCHWARTZMAN: 3.44
                }
            },
            {
                'round': 32,
                'players': [
                    TENNYS_SANDGREN,
                    FABIO_FOGNINI
                ],
                'score': [(6, 3), (7, 6), (6, 3)],
                'odds': {
                    TENNYS_SANDGREN: 3.45,
                    FABIO_FOGNINI: 1.31
                }
            },
            {
                'round': 32,
                'players': [
                    KEI_NISHIKORI,
                    STEVE_JOHNSON
                ],
                'score': [(6, 4), (6, 3), (6, 2)],
                'odds': {
                    KEI_NISHIKORI: 1.20,
                    STEVE_JOHNSON: 4.46
                }
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(6, 2), (6, 3), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.18,
                    JO_WILFRIED_TSONGA: 4.90
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    LUCAS_POUILLE
                ],
                'score': [(7, 5), (6, 2), (7, 6)],
                'odds': {
                    ROGER_FEDERER: 1.06,
                    LUCAS_POUILLE: 8.00
                }
            },

            # 2019-07-08
            {
                'round': 16,
                'players': [
                    SAM_QUERREY,
                    TENNYS_SANDGREN
                ],
                'score': [(6, 4), (6, 7), (7, 6), (7, 6)],
                'odds': {
                    SAM_QUERREY: 1.16,
                    TENNYS_SANDGREN: 5.00
                }
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    BENOIT_PAIRE
                ],
                'score': [(6, 3), (7, 5), (6, 2)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.20,
                    BENOIT_PAIRE: 4.35
                }
            },
            {
                'round': 16,
                'players': [
                    DAVID_GOFFIN,
                    FERNANDO_VERDASCO
                ],
                'score': [(7, 6), (2, 6), (6, 3), (6, 4)],
                'odds': {
                    DAVID_GOFFIN: 1.31,
                    FERNANDO_VERDASCO: 3.40
                }
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    MILOS_RAONIC
                ],
                'score': [(3, 6), (4, 6), (6, 3), (7, 6), (8, 6)],
                'odds': {
                    GUIDO_PELLA: 4.75,
                    MILOS_RAONIC: 1.17
                }
            },
            {
                'round': 16,
                'players': [
                    KEI_NISHIKORI,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 3), (3, 6), (6, 3), (6, 4)],
                'odds': {
                    KEI_NISHIKORI: 1.11,
                    MIKHAIL_KUKUSHKIN: 6.50
                }
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    JOAO_SOUSA
                ],
                'score': [(6, 2), (6, 2), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.02,
                    JOAO_SOUSA: 14.22
                }
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    UGO_HUMBERT
                ],
                'score': [(6, 3), (6, 2), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    UGO_HUMBERT: 17.00
                }
            },

            # 2019-07-10
            {
                'round': 8,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    GUIDO_PELLA
                ],
                'score': [(7, 5), (6, 4), (3, 6), (6, 3)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.18,
                    GUIDO_PELLA: 4.50
                }
            },
            {
                'round': 8,
                'players': [
                    RAFAEL_NADAL,
                    SAM_QUERREY
                ],
                'score': [(7, 5), (6, 2), (6, 2)],
                'odds': {
                    RAFAEL_NADAL: 1.13,
                    SAM_QUERREY: 6.00
                }
            },
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    KEI_NISHIKORI
                ],
                'score': [(4, 6), (6, 1), (6, 4), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.12,
                    KEI_NISHIKORI: 6.50
                }
            },
            {
                'round': 8,
                'players': [
                    NOVAK_DJOKOVIC,
                    DAVID_GOFFIN
                ],
                'score': [(6, 4), (6, 0), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.05,
                    DAVID_GOFFIN: 9.00
                }
            },

            # 2019-07-12
            {
                'round': 4,
                'players': [
                    ROGER_FEDERER,
                    RAFAEL_NADAL
                ],
                'score': [(7, 6), (1, 6), (6, 3), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 2.22,
                    RAFAEL_NADAL: 1.67
                }
            },
            {
                'round': 4,
                'players': [
                    NOVAK_DJOKOVIC,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(6, 2), (4, 6), (6, 3), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.07,
                    ROBERTO_BAUTISTA_AGUT: 8.00
                }
            },

            # 2019-07-14
            {
                'round': 2,
                'players': [
                    NOVAK_DJOKOVIC,
                    ROGER_FEDERER
                ],
                'score': [(7, 6), (1, 6), (7, 6), (4, 6), (13, 12)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.51,
                    ROGER_FEDERER: 2.55
                }
            }
        ]
    },

    {
        'location': NEWPORT,
        'date': '2019-07-21',
        'matches': [

            # 2019-07-14
            {
                'round': 512,
                'players': [
                    TIM_SMYCZEK,
                    MITCHELL_KRUEGER
                ],
                'score': [(6, 3), (6, 1)]
            },
            {
                'round': 512,
                'players': [
                    NOAH_RUBIN,
                    AMIR_WEINTRAUB
                ],
                'score': [(6, 1), (6, 1)]
            },
            {
                'round': 512,
                'players': [
                    VIKTOR_TROICKI,
                    KARL_POLING
                ],
                'score': [(6, 1), (6, 4)]
            },
            {
                'round': 512,
                'players': [
                    YUICHI_SUGITA,
                    QUENTIN_HALYS
                ],
                'score': [(7, 5), (6, 4)]
            },
            {
                'round': 512,
                'players': [
                    JOHN_PATRICK_SMITH,
                    TATSUMA_ITO
                ],
                'score': [(6, 2), (3, 6), (6, 3)]
            },
            {
                'round': 512,
                'players': [
                    RAMKUMAR_RAMANATHAN,
                    MAXIME_CRESSY
                ],
                'score': [(7, 6), (6, 3)]
            },
            {
                'round': 512,
                'players': [
                    ALEX_BOLT,
                    EVGENY_KARLOVSKIY
                ],
                'score': [(6, 2), (6, 2)]
            },
            {
                'round': 512,
                'players': [
                    BJORN_FRATANGELO,
                    THAI_SON_KWIATKOWSKI
                ],
                'score': [(6, 1), (6, 4)]
            },

            # 2019-07-15
            {
                'round': 256,
                'players': [
                    TIM_SMYCZEK,
                    JOHN_PATRICK_SMITH
                ],
                'score': [(6, 4), (3, 6), (6, 2)],
                'odds': {
                    TIM_SMYCZEK: 1.77,
                    JOHN_PATRICK_SMITH: 1.87
                }
            },
            {
                'round': 256,
                'players': [
                    RAMKUMAR_RAMANATHAN,
                    YUICHI_SUGITA
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    RAMKUMAR_RAMANATHAN: 2.05,
                    YUICHI_SUGITA: 1.69
                }
            },
            {
                'round': 256,
                'players': [
                    ALEX_BOLT,
                    NOAH_RUBIN
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ALEX_BOLT: 2.05,
                    NOAH_RUBIN: 1.69
                }
            },
            {
                'round': 256,
                'players': [
                    VIKTOR_TROICKI,
                    BJORN_FRATANGELO
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    VIKTOR_TROICKI: 1.63,
                    BJORN_FRATANGELO: 2.06
                }
            },
            {
                'round': 32,
                'players': [
                    TENNYS_SANDGREN,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 4), (5, 7), (6, 4)],
                'odds': {
                    TENNYS_SANDGREN: 1.41,
                    DENIS_ISTOMIN: 2.85
                }
            },
            {
                'round': 32,
                'players': [
                    KAMIL_MAJCHRZAK,
                    ALASTAIR_GRAY
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.06,
                    ALASTAIR_GRAY: 8.50
                }
            },
            {
                'round': 32,
                'players': [
                    ILYA_IVASHKA,
                    BERNARD_TOMIC
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    ILYA_IVASHKA: 2.85,
                    BERNARD_TOMIC: 1.40
                }
            },
            {
                'round': 32,
                'players': [
                    MARCEL_GRANOLLERS,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    MARCEL_GRANOLLERS: 1.33,
                    PRAJNESH_GUNNESWARAN: 3.25
                }
            },
            {
                'round': 32,
                'players': [
                    GUIDO_ANDREOZZI,
                    IVO_KARLOVIC
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    GUIDO_ANDREOZZI: 3.80,
                    IVO_KARLOVIC: 1.23
                }
            },

            # 2019-07-16
            {
                'round': 32,
                'players': [
                    MISCHA_ZVEREV,
                    TIM_SMYCZEK
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    MISCHA_ZVEREV: 2.34,
                    TIM_SMYCZEK: 1.59
                }
            },
            {
                'round': 32,
                'players': [
                    VIKTOR_TROICKI,
                    JASON_JUNG
                ],
                'score': [(3, 6), (7, 5), (7, 5)],
                'odds': {
                    VIKTOR_TROICKI: 1.44,
                    JASON_JUNG: 2.80
                }
            },
            {
                'round': 32,
                'players': [
                    RAMKUMAR_RAMANATHAN,
                    SERGIY_STAKHOVSKY
                ],
                'score': [(5, 7), (7, 6), (6, 2)],
                'odds': {
                    RAMKUMAR_RAMANATHAN: 1.87,
                    SERGIY_STAKHOVSKY: 1.87
                }
            },
            {
                'round': 32,
                'players': [
                    MATTHEW_EBDEN,
                    BRAYDEN_SCHNUR
                ],
                'score': [(6, 1), (2, 6), (6, 3)],
                'odds': {
                    MATTHEW_EBDEN: 1.63,
                    BRAYDEN_SCHNUR: 2.10
                }
            },
            {
                'round': 32,
                'players': [
                    DENIS_KUDLA,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DENIS_KUDLA: 1.50,
                    BRADLEY_KLAHN: 2.48
                }
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_BUBLIK,
                    ALEX_BOLT
                ],
                'score': [(6, 4), (2, 6), (7, 6)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.91,
                    ALEX_BOLT: 1.83
                }
            },
            {
                'round': 32,
                'players': [
                    CHRISTOPHER_EUBANKS,
                    STEVE_JOHNSON
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    CHRISTOPHER_EUBANKS: 4.33,
                    STEVE_JOHNSON: 1.20
                }
            },

            # 2019-07-17
            {
                'round': 16,
                'players': [
                    MISCHA_ZVEREV,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MISCHA_ZVEREV: 1.82,
                    GUIDO_ANDREOZZI: 1.99
                }
            },
            {
                'round': 16,
                'players': [
                    ILYA_IVASHKA,
                    CHRISTOPHER_EUBANKS
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    ILYA_IVASHKA: 2.05,
                    CHRISTOPHER_EUBANKS: 1.74
                }
            },
            {
                'round': 16,
                'players': [
                    MATTHEW_EBDEN,
                    DENIS_KUDLA
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    MATTHEW_EBDEN: 2.25,
                    DENIS_KUDLA: 1.65
                }
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_BUBLIK,
                    VIKTOR_TROICKI
                ],
                'score': [(3, 6), (6, 3), (6, 3)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.30,
                    VIKTOR_TROICKI: 1.63
                }
            },
            {
                'round': 16,
                'players': [
                    UGO_HUMBERT,
                    RAMKUMAR_RAMANATHAN
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    UGO_HUMBERT: 1.54,
                    RAMKUMAR_RAMANATHAN: 2.45
                }
            },
            {
                'round': 16,
                'players': [
                    MARCEL_GRANOLLERS,
                    JORDAN_THOMPSON
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    MARCEL_GRANOLLERS: 2.12,
                    JORDAN_THOMPSON: 1.74
                }
            },
            {
                'round': 16,
                'players': [
                    TENNYS_SANDGREN,
                    ADRIAN_MANNARINO
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    TENNYS_SANDGREN: 2.10,
                    ADRIAN_MANNARINO: 1.65
                }
            },
            {
                'round': 16,
                'players': [
                    JOHN_ISNER,
                    KAMIL_MAJCHRZAK
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    JOHN_ISNER: 1.36,
                    KAMIL_MAJCHRZAK: 3.10
                }
            },

            # 2019-07-19
            {
                'round': 8,
                'players': [
                    MARCEL_GRANOLLERS,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 3), (6, 0)],
                # no odds
            },
            {
                'round': 8,
                'players': [
                    ALEXANDER_BUBLIK,
                    TENNYS_SANDGREN
                ],
                'score': [(0, 6), (6, 3), (6, 0)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.39,
                    TENNYS_SANDGREN: 1.56
                }
            },
            {
                'round': 8,
                'players': [
                    UGO_HUMBERT,
                    ILYA_IVASHKA
                ],
                'score': [(7, 5), (3, 6), (6, 2)],
                'odds': {
                    UGO_HUMBERT: 1.37,
                    ILYA_IVASHKA: 3.00
                }
            },
            {
                'round': 8,
                'players': [
                    JOHN_ISNER,
                    MATTHEW_EBDEN
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    JOHN_ISNER: 1.32,
                    MATTHEW_EBDEN: 3.30
                }
            },

            # 2019-07-20
            {
                'round': 4,
                'players': [
                    ALEXANDER_BUBLIK,
                    MARCEL_GRANOLLERS
                ],
                'score': [(7, 6), (3, 6), (6, 4)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.60,
                    MARCEL_GRANOLLERS: 1.44
                }
            },
            {
                'round': 4,
                'players': [
                    JOHN_ISNER,
                    UGO_HUMBERT
                ],
                'score': [(6, 7), (7, 6), (6, 3)],
                'odds': {
                    JOHN_ISNER: 1.47,
                    UGO_HUMBERT: 2.59
                }
            },

            # 2019-07-21
            {
                'round': 2,
                'players': [
                    JOHN_ISNER,
                    ALEXANDER_BUBLIK
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    JOHN_ISNER: 1.30,
                    ALEXANDER_BUBLIK: 3.40
                }
            }
        ]
    },

    {
        'location': UMAG,
        'date': '2019-07-21',
        'matches': [

            # 2019-07-14
            {
                'round': 512,
                'players': [
                    ATTILA_BALAZS,
                    ADMIR_KALENDER
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    ATTILA_BALAZS: 1.02,
                    ADMIR_KALENDER: 13.73
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_ALTMAIER,
                    CARLOS_BERLOCQ
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    DANIEL_ALTMAIER: 1.59,
                    CARLOS_BERLOCQ: 2.26
                }
            },
            {
                'round': 512,
                'players': [
                    STEFANO_NAPOLITANO,
                    JAVIER_BARRANCO_COSANO
                ],
                'score': [(7, 6), (3, 6), (6, 2)],
                'odds': {
                    STEFANO_NAPOLITANO: 1.37,
                    JAVIER_BARRANCO_COSANO: 2.75
                }
            },
            {
                'round': 512,
                'players': [
                    TOMMY_ROBREDO,
                    MILJAN_ZEKIC
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    TOMMY_ROBREDO: 1.09,
                    MILJAN_ZEKIC: 5.85
                }
            },
            {
                'round': 512,
                'players': [
                    MARCO_TRUNGELLITI,
                    ALEXANDER_ZHURBIN
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    MARCO_TRUNGELLITI: 1.19,
                    ALEXANDER_ZHURBIN: 4.37
                }
            },
            {
                'round': 512,
                'players': [
                    PETER_TOREBKO,
                    FILLIPPO_BALDI
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    PETER_TOREBKO: 2.54,
                    FILLIPPO_BALDI: 1.38
                }
            },
            {
                'round': 512,
                'players': [
                    RUDOLF_MOLLEKER,
                    FABRIZIO_ORNAGO
                ],
                'score': [(6, 7), (7, 5), (6, 2)],
                'odds': {
                    RUDOLF_MOLLEKER: 1.13,
                    FABRIZIO_ORNAGO: 5.41
                }
            },
            {
                'round': 512,
                'players': [
                    SALVATORE_CARUSO,
                    NIK_RAZBORSEK
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    SALVATORE_CARUSO: 1.05,
                    NIK_RAZBORSEK: 8.39
                }
            },

            # 2019-07-15
            {
                'round': 256,
                'players': [
                    PETER_TOREBKO,
                    DANIEL_ALTMAIER
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    PETER_TOREBKO: 3.00,
                    DANIEL_ALTMAIER: 1.32
                }
            },
            {
                'round': 256,
                'players': [
                    MARCO_TRUNGELLITI,
                    STEFANO_NAPOLITANO
                ],
                'score': [(6, 7), (6, 2), (6, 3)],
                'odds': {
                    MARCO_TRUNGELLITI: 2.25,
                    STEFANO_NAPOLITANO: 1.59
                }
            },
            {
                'round': 256,
                'players': [
                    ATTILA_BALAZS,
                    RUDOLF_MOLLEKER
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ATTILA_BALAZS: 1.37,
                    RUDOLF_MOLLEKER: 2.70
                }
            },
            {
                'round': 256,
                'players': [
                    SALVATORE_CARUSO,
                    TOMMY_ROBREDO
                ],
                'score': [(5, 7), (6, 4), (6, 3)],
                'odds': {
                    SALVATORE_CARUSO: 1.95,
                    TOMMY_ROBREDO: 1.71
                }
            },
            {
                'round': 32,
                'players': [
                    JIRI_VESELY,
                    CEDRIC_MARCEL_STEBE
                ],
                'score': [(7, 6), (3, 6), (7, 6)],
                'odds': {
                    JIRI_VESELY: 1.25,
                    CEDRIC_MARCEL_STEBE: 3.80
                }
            },
            {
                'round': 32,
                'players': [
                    JANNIK_SINNER,
                    PEDRO_SOUSA
                ],
                'score': [(1, 6), (6, 3), (6, 4)],
                'odds': {
                    JANNIK_SINNER: 1.93,
                    PEDRO_SOUSA: 1.80
                }
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ALJAZ_BEDENE: 1.84,
                    MARCO_CECCHINATO: 1.95
                }
            },

            # 2019-07-16
            {
                'round': 32,
                'players': [
                    STEFANO_TRAVAGLIA,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    STEFANO_TRAVAGLIA: 1.54,
                    THOMAS_FABBIANO: 2.51
                }
            },
            {
                'round': 32,
                'players': [
                    NINO_SERDARUSIC,
                    MARCO_TRUNGELLITI
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    NINO_SERDARUSIC: 2.55,
                    MARCO_TRUNGELLITI: 1.51
                }
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    ROBIN_HAASE
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ANDREY_RUBLEV: 1.67,
                    ROBIN_HAASE: 2.12
                }
            },
            {
                'round': 32,
                'players': [
                    PAOLO_LORENZI,
                    PETER_TOREBKO
                ],
                'score': [(5, 7), (6, 4), (7, 6)],
                'odds': {
                    PAOLO_LORENZI: 1.43,
                    PETER_TOREBKO: 2.80
                }
            },
            {
                'round': 32,
                'players': [
                    SALVATORE_CARUSO,
                    CORENTIN_MOUTET
                ],
                'score': [(7, 5), (6, 0)],
                'odds': {
                    SALVATORE_CARUSO: 2.20,
                    CORENTIN_MOUTET: 1.59
                }
            },
            {
                'round': 32,
                'players': [
                    ATTILA_BALAZS,
                    VIKTOR_GALOVIC
                ],
                'score': [(6, 0), (6, 7), (7, 6)],
                'odds': {
                    ATTILA_BALAZS: 1.29,
                    VIKTOR_GALOVIC: 3.45
                }
            },
            {
                'round': 32,
                'players': [
                    LEONARDO_MAYER,
                    PABLO_ANDUJAR
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    LEONARDO_MAYER: 1.80,
                    PABLO_ANDUJAR: 1.92
                }
            },
            {
                'round': 32,
                'players': [
                    FACUNDO_BAGNIS,
                    MARTIN_KLIZAN
                ],
                'score': [(4, 6), (6, 3), (7, 5)],
                'odds': {
                    FACUNDO_BAGNIS: 2.45,
                    MARTIN_KLIZAN: 1.56
                }
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    TARO_DANIEL
                ],
                'score': [(7, 5), (7, 6)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.15,
                    TARO_DANIEL: 5.00
                }
            },

            # 2019-07-17
            {
                'round': 16,
                'players': [
                    LEONARDO_MAYER,
                    JIRI_VESELY
                ],
                'score': [(3, 6), (6, 4), (6, 4)],
                'odds': {
                    LEONARDO_MAYER: 1.48,
                    JIRI_VESELY: 2.60
                }
            },
            {
                'round': 16,
                'players': [
                    ATTILA_BALAZS,
                    FILIP_KRAJINOVIC
                ],
                'score': [(6, 3), (6, 7), (7, 6)],
                'odds': {
                    ATTILA_BALAZS: 3.30,
                    FILIP_KRAJINOVIC: 1.33
                }
            },
            {
                'round': 16,
                'players': [
                    LASLO_DJERE,
                    PAOLO_LORENZI
                ],
                'score': [(6, 3), (6, 7), (6, 4)],
                'odds': {
                    LASLO_DJERE: 1.24,
                    PAOLO_LORENZI: 3.75
                }
            },
            {
                'round': 16,
                'players': [
                    STEFANO_TRAVAGLIA,
                    FABIO_FOGNINI
                ],
                'score': [(6, 1), (2, 1)],
                'retired': True,
                'odds': {
                    STEFANO_TRAVAGLIA: 3.07,
                    FABIO_FOGNINI: 1.38
                }
            },

            # 2019-07-18
            {
                'round': 16,
                'players': [
                    ALJAZ_BEDENE,
                    JANNIK_SINNER
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALJAZ_BEDENE: 1.32,
                    JANNIK_SINNER: 3.26
                }
            },
            {
                'round': 16,
                'players': [
                    FACUNDO_BAGNIS,
                    NINO_SERDARUSIC
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    FACUNDO_BAGNIS: 1.41,
                    NINO_SERDARUSIC: 2.85
                }
            },
            {
                'round': 16,
                'players': [
                    DUSAN_LAJOVIC,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 1.96,
                    ANDREY_RUBLEV: 1.83
                }
            },
            {
                'round': 16,
                'players': [
                    SALVATORE_CARUSO,
                    BORNA_CORIC
                ],
                'score': [(6, 2), (3, 6), (6, 1)],
                'odds': {
                    SALVATORE_CARUSO: 3.20,
                    BORNA_CORIC: 1.36
                }
            },

            # 2019-07-19
            {
                'round': 8,
                'players': [
                    SALVATORE_CARUSO,
                    FACUNDO_BAGNIS
                ],
                'score': [(6, 4), (6, 0)],
                'odds': {
                    SALVATORE_CARUSO: 1.61,
                    FACUNDO_BAGNIS: 2.28
                }
            },
            {
                'round': 8,
                'players': [
                    ATTILA_BALAZS,
                    STEFANO_TRAVAGLIA
                ],
                'score': [(3, 6), (7, 6), (6, 3)],
                'odds': {
                    ATTILA_BALAZS: 2.00,
                    STEFANO_TRAVAGLIA: 1.79
                }
            },
            {
                'round': 8,
                'players': [
                    DUSAN_LAJOVIC,
                    ALJAZ_BEDENE
                ],
                'score': [(5, 7), (6, 3), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 1.71,
                    ALJAZ_BEDENE: 2.10
                }
            },
            {
                'round': 8,
                'players': [
                    LASLO_DJERE,
                    LEONARDO_MAYER
                ],
                'score': [(6, 4), (6, 7), (6, 3)],
                'odds': {
                    LASLO_DJERE: 1.83,
                    LEONARDO_MAYER: 1.91
                }
            },

            # 2019-07-20
            {
                'round': 4,
                'players': [
                    DUSAN_LAJOVIC,
                    SALVATORE_CARUSO
                ],
                'score': [(7, 5), (0, 0)],
                'retired': True,
                'odds': {
                    DUSAN_LAJOVIC: 1.50,
                    SALVATORE_CARUSO: 2.58
                }
            },
            {
                'round': 4,
                'players': [
                    ATTILA_BALAZS,
                    LASLO_DJERE
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ATTILA_BALAZS: 2.50,
                    LASLO_DJERE: 1.50
                }
            },

            # 2019-07-21
            {
                'round': 2,
                'players': [
                    DUSAN_LAJOVIC,
                    ATTILA_BALAZS
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    DUSAN_LAJOVIC: 1.50,
                    ATTILA_BALAZS: 2.60
                }
            }
        ]
    },

    {
        'location': BASTAD,
        'date': '2019-07-21',
        'matches': [

            # 2019-07-14
            {
                'round': 512,
                'players': [
                    ROBERTO_QUIROZ,
                    YANNICK_MERTENS
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    ROBERTO_QUIROZ: 1.20,
                    YANNICK_MERTENS: 4.16
                }
            },
            {
                'round': 512,
                'players': [
                    STEVEN_DIEZ,
                    MARC_ANDREA_HUESLER
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    STEVEN_DIEZ: 1.33,
                    MARC_ANDREA_HUESLER: 2.97
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEY_VATUTIN,
                    JULIAN_OCLEPPO
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    ALEXEY_VATUTIN: 1.19,
                    JULIAN_OCLEPPO: 4.28
                }
            },
            {
                'round': 512,
                'players': [
                    CONSTANT_LESTIENNE,
                    JOHN_HALLQUIST_LITHEN
                ],
                'score': [(6, 0), (7, 6)],
                'odds': {
                    CONSTANT_LESTIENNE: 1.02,
                    JOHN_HALLQUIST_LITHEN: 13.78
                }
            },
            {
                'round': 512,
                'players': [
                    BERNABE_ZAPATA_MIRALLES,
                    FILIP_HORANSKY
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    BERNABE_ZAPATA_MIRALLES: 1.67,
                    FILIP_HORANSKY: 1.99
                }
            },
            {
                'round': 512,
                'players': [
                    FACUNDO_ARGUELLO,
                    MARKUS_ERIKSSON
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    FACUNDO_ARGUELLO: 1.33,
                    MARKUS_ERIKSSON: 2.94
                }
            },
            {
                'round': 512,
                'players': [
                    LAURYNAS_GRIGELIS,
                    JOAO_DOMINGUES
                ],
                'score': [(7, 6), (2, 6), (6, 2)],
                'odds': {
                    LAURYNAS_GRIGELIS: 3.42,
                    JOAO_DOMINGUES: 1.26
                }
            },
            {
                'round': 512,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    CARL_SODERLUND
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.05,
                    CARL_SODERLUND: 10.15
                }
            },

            # 2019-07-15
            {
                'round': 256,
                'players': [
                    BERNABE_ZAPATA_MIRALLES,
                    ALEXEY_VATUTIN
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    BERNABE_ZAPATA_MIRALLES: 1.87,
                    ALEXEY_VATUTIN: 1.74
                }
            },
            {
                'round': 256,
                'players': [
                    CONSTANT_LESTIENNE,
                    LAURYNAS_GRIGELIS
                ],
                'score': [(1, 6), (6, 2), (6, 1)],
                'odds': {
                    CONSTANT_LESTIENNE: 1.33,
                    LAURYNAS_GRIGELIS: 3.05
                }
            },
            {
                'round': 256,
                'players': [
                    FACUNDO_ARGUELLO,
                    STEVEN_DIEZ
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    FACUNDO_ARGUELLO: 1.77,
                    STEVEN_DIEZ: 1.83
                }
            },
            {
                'round': 256,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    ROBERTO_QUIROZ
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.17,
                    ROBERTO_QUIROZ: 4.80
                }
            },
            {
                'round': 32,
                'players': [
                    MIKAEL_YMER,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(4, 6), (7, 5), (6, 0)],
                'odds': {
                    MIKAEL_YMER: 1.61,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.27
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    JAUME_MUNAR
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.80,
                    JAUME_MUNAR: 1.97
                }
            },

            # 2019-07-16
            {
                'round': 32,
                'players': [
                    ELIAS_YMER,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 3), (2, 6), (7, 5)],
                'odds': {
                    ELIAS_YMER: 2.10,
                    THIAGO_MONTEIRO: 1.65
                }
            },
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    CONSTANT_LESTIENNE
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.33,
                    CONSTANT_LESTIENNE: 3.20
                }
            },
            {
                'round': 32,
                'players': [
                    DENNIS_NOVAK,
                    STEVE_DARCIS
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    DENNIS_NOVAK: 1.60,
                    STEVE_DARCIS: 2.25
                }
            },
            {
                'round': 32,
                'players': [
                    HUGO_DELLIEN,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 2), (2, 1)],
                'retired': True,
                'odds': {
                    HUGO_DELLIEN: 1.43,
                    ERNESTS_GULBIS: 2.80
                }
            },
            {
                'round': 32,
                'players': [
                    FEDERICO_DELBONIS,
                    BERNABE_ZAPATA_MIRALLES
                ],
                'score': [(7, 5), (3, 6), (6, 2)],
                'odds': {
                    FEDERICO_DELBONIS: 1.25,
                    BERNABE_ZAPATA_MIRALLES: 3.70
                }
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(6, 4), (4, 6), (7, 5)],
                'odds': {
                    JEREMY_CHARDY: 2.25,
                    PABLO_CARRENO_BUSTA: 1.66
                }
            },
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    JOZEF_KOVALIK
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 1.56,
                    JOZEF_KOVALIK: 2.32
                }
            },
            {
                'round': 32,
                'players': [
                    DAMIR_DZUMHUR,
                    CASPER_RUUD
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    DAMIR_DZUMHUR: 3.10,
                    CASPER_RUUD: 1.34
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    FACUNDO_ARGUELLO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.40,
                    FACUNDO_ARGUELLO: 3.00
                }
            },
            {
                'round': 32,
                'players': [
                    NICOLAS_JARRY,
                    HENRI_LAAKSONEN
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    NICOLAS_JARRY: 1.56,
                    HENRI_LAAKSONEN: 2.54
                }
            },

            # 2019-07-17
            {
                'round': 16,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    DAMIR_DZUMHUR
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.63,
                    DAMIR_DZUMHUR: 2.35
                }
            },
            {
                'round': 16,
                'players': [
                    NICOLAS_JARRY,
                    MIKAEL_YMER
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    NICOLAS_JARRY: 1.69,
                    MIKAEL_YMER: 2.24
                }
            },
            {
                'round': 16,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.50,
                    FERNANDO_VERDASCO: 1.54
                }
            },
            {
                'round': 16,
                'players': [
                    JEREMY_CHARDY,
                    CHRISTIAN_GARIN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 2.40,
                    CHRISTIAN_GARIN: 1.57
                }
            },

            # 2019-07-18
            {
                'round': 16,
                'players': [
                    JOAO_SOUSA,
                    ELIAS_YMER
                ],
                'score': [(4, 6), (6, 4), (6, 2)],
                'odds': {
                    JOAO_SOUSA: 1.61,
                    ELIAS_YMER: 2.17
                }
            },
            {
                'round': 16,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    HUGO_DELLIEN
                ],
                'score': [(4, 6), (7, 5), (6, 3)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.59,
                    HUGO_DELLIEN: 2.29
                }
            },
            {
                'round': 16,
                'players': [
                    RICHARD_GASQUET,
                    DENNIS_NOVAK
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    RICHARD_GASQUET: 1.53,
                    DENNIS_NOVAK: 2.50
                }
            },
            {
                'round': 16,
                'players': [
                    FEDERICO_DELBONIS,
                    PABLO_CUEVAS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    FEDERICO_DELBONIS: 2.27,
                    PABLO_CUEVAS: 1.65
                }
            },

            # 2019-07-19
            {
                'round': 8,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(4, 6), (6, 1), (6, 1)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.99,
                    ROBERTO_CARBALLES_BAENA: 1.83
                }
            },
            {
                'round': 8,
                'players': [
                    FEDERICO_DELBONIS,
                    JOAO_SOUSA
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    FEDERICO_DELBONIS: 1.58,
                    JOAO_SOUSA: 2.30
                }
            },
            {
                'round': 8,
                'players': [
                    NICOLAS_JARRY,
                    JEREMY_CHARDY
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    NICOLAS_JARRY: 1.99,
                    JEREMY_CHARDY: 1.80
                }
            },
            {
                'round': 8,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    RICHARD_GASQUET
                ],
                'score': [(7, 6), (4, 6), (6, 3)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.67,
                    RICHARD_GASQUET: 2.10
                }
            },

            # 2019-07-20
            {
                'round': 4,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    ALBERT_RAMOS_VINOLAS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 2.10,
                    ALBERT_RAMOS_VINOLAS: 1.67
                }
            },
            {
                'round': 4,
                'players': [
                    NICOLAS_JARRY,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    NICOLAS_JARRY: 2.17,
                    FEDERICO_DELBONIS: 1.71
                }
            },

            # 2019-07-21
            {
                'round': 2,
                'players': [
                    NICOLAS_JARRY,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    NICOLAS_JARRY: 1.67,
                    JUAN_IGNACIO_LONDERO: 2.25
                }
            }
        ]
    },

    {
        'location': ATLANTA,
        'date': '2019-07-28',
        'matches': [

            # 2019-07-20
            {
                'round': 512,
                'players': [
                    JASON_JUNG,
                    ALEX_BOLT
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    JASON_JUNG: 1.91,
                    ALEX_BOLT: 1.74
                }
            },
            {
                'round': 512,
                'players': [
                    DONALD_YOUNG,
                    DOMINIK_KOEPFER
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    DONALD_YOUNG: 1.95,
                    DOMINIK_KOEPFER: 1.74
                }
            },
            {
                'round': 512,
                'players': [
                    KEVIN_KING,
                    GUIDO_ANDREOZZI
                ],
                'score': [(7, 5), (4, 6), (7, 6)],
                'odds': {
                    KEVIN_KING: 3.10,
                    GUIDO_ANDREOZZI: 1.33
                }
            },

            # 2019-07-21
            {
                'round': 512,
                'players': [
                    RYAN_HARRISON,
                    VIKTOR_TROICKI
                ],
                'score': [(4, 6), (7, 5), (7, 6)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    MICHAEL_MMOH
                ],
                'score': [(5, 7), (7, 6), (7, 6)],
                'odds': {
                    TOMMY_PAUL: 1.47,
                    MICHAEL_MMOH: 2.55
                }
            },
            {
                'round': 512,
                'players': [
                    PETER_GOJOWCZYK,
                    MIKAEL_TORPEGAARD
                ],
                'score': [(6, 4), (3, 6), (7, 6)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    SOONWOO_KWON,
                    ILYA_IVASHKA
                ],
                'score': [(6, 2), (6, 3)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    KAMIL_MAJCHRZAK,
                    TRENT_BRYDE
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.04,
                    TRENT_BRYDE: 7.82
                }
            },
            {
                'round': 256,
                'players': [
                    KEVIN_KING,
                    RYAN_HARRISON
                ],
                'score': [(6, 7), (7, 5), (3, 1)],
                'retired': True,
                # no odds
            },
            {
                'round': 256,
                'players': [
                    JASON_JUNG,
                    DONALD_YOUNG
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    JASON_JUNG: 1.75,
                    DONALD_YOUNG: 1.91
                }
            },
            {
                'round': 256,
                'players': [
                    SOONWOO_KWON,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 2), (6, 2)],
                # no odds
            },
            {
                'round': 256,
                'players': [
                    KAMIL_MAJCHRZAK,
                    TOMMY_PAUL
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    KAMIL_MAJCHRZAK: 2.55,
                    TOMMY_PAUL: 1.47
                }
            },

            # 2019-07-22
            {
                'round': 32,
                'players': [
                    ALEXEI_POPYRIN,
                    DENIS_KUDLA
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ALEXEI_POPYRIN: 1.67,
                    DENIS_KUDLA: 2.18
                }
            },
            {
                'round': 32,
                'players': [
                    BRADLEY_KLAHN,
                    MARIUS_COPIL
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    BRADLEY_KLAHN: 1.53,
                    MARIUS_COPIL: 2.45
                }
            },
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    JORDAN_THOMPSON
                ],
                'score': [(7, 6), (4, 6), (6, 3)],
                'odds': {
                    CAMERON_NORRIE: 1.95,
                    JORDAN_THOMPSON: 1.80
                }
            },

            # 2019-07-23
            {
                'round': 32,
                'players': [
                    REILLY_OPELKA,
                    ALEXANDER_BUBLIK
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 1.35,
                    ALEXANDER_BUBLIK: 3.13
                }
            },
            {
                'round': 32,
                'players': [
                    SOONWOO_KWON,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(6, 7), (7, 5), (6, 0)],
                'odds': {
                    SOONWOO_KWON: 1.31,
                    PRAJNESH_GUNNESWARAN: 3.30
                }
            },
            {
                'round': 32,
                'players': [
                    KEVIN_KING,
                    GRIGOR_DIMITROV
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    KEVIN_KING: 5.50,
                    GRIGOR_DIMITROV: 1.13
                }
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    JACK_SOCK
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.34,
                    JACK_SOCK: 3.11
                }
            },
            {
                'round': 32,
                'players': [
                    DANIEL_EVANS,
                    JASON_JUNG
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    DANIEL_EVANS: 1.36,
                    JASON_JUNG: 3.11
                }
            },
            {
                'round': 32,
                'players': [
                    MATTHEW_EBDEN,
                    KAMIL_MAJCHRZAK
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    MATTHEW_EBDEN: 2.60,
                    KAMIL_MAJCHRZAK: 1.43
                }
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    COLE_GROMLEY
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    UGO_HUMBERT: 1.04,
                    COLE_GROMLEY: 9.50
                }
            },
            {
                'round': 32,
                'players': [
                    RADU_ALBOT,
                    TENNYS_SANDGREN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    RADU_ALBOT: 1.77,
                    TENNYS_SANDGREN: 1.95
                }
            },
            {
                'round': 32,
                'players': [
                    BERNARD_TOMIC,
                    FRANCES_TIAFOE
                ],
                'score': [(4, 6), (6, 3), (7, 6)],
                'odds': {
                    BERNARD_TOMIC: 3.40,
                    FRANCES_TIAFOE: 1.30
                }
            },

            # 2019-07-24
            {
                'round': 16,
                'players': [
                    CAMERON_NORRIE,
                    SOONWOO_KWON
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 1.85,
                    SOONWOO_KWON: 1.95
                },
                'prediction': CAMERON_NORRIE,
                'bet': 20
            },
            {
                'round': 16,
                'players': [
                    DANIEL_EVANS,
                    RADU_ALBOT
                ],
                'score': [(7, 6), (5, 7), (6, 2)],
                'odds': {
                    DANIEL_EVANS: 1.48,
                    RADU_ALBOT: 2.60
                },
                'prediction': DANIEL_EVANS,
                'bet': 20
            },
            {
                'round': 16,
                'players': [
                    ALEXEI_POPYRIN,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    ALEXEI_POPYRIN: 1.90,
                    PIERRE_HUGUES_HERBERT: 1.90
                },
                'prediction': ALEXEI_POPYRIN,
                'bet': 5
            },
            {
                'round': 16,
                'players': [
                    REILLY_OPELKA,
                    JOHN_ISNER
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    REILLY_OPELKA: 2.30,
                    JOHN_ISNER: 1.60
                },
                'prediction': JOHN_ISNER,
                'bet': 5
            },

            # 2019-07-25
            {
                'round': 16,
                'players': [
                    BERNARD_TOMIC,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    BERNARD_TOMIC: 1.80,
                    MATTHEW_EBDEN: 2.00
                },
                'prediction': MATTHEW_EBDEN,
                'bet': 20
            },
            {
                'round': 16,
                'players': [
                    ALEX_DE_MINAUR,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    ALEX_DE_MINAUR: 1.42,
                    BRADLEY_KLAHN: 2.80
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 20
            },
            {
                'round': 16,
                'players': [
                    TAYLOR_FRITZ,
                    KEVIN_KING
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    TAYLOR_FRITZ: 1.16,
                    KEVIN_KING: 5.00
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 5
            },
            {
                'round': 16,
                'players': [
                    MIOMIR_KECMANOVIC,
                    UGO_HUMBERT
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.95,
                    UGO_HUMBERT: 1.85
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 5
            },

            # 2016-09-26
            {
                'round': 8,
                'players': [
                    ALEX_DE_MINAUR,
                    BERNARD_TOMIC
                ],
                'score': [(6, 2), (3, 0)],
                'retired': True,
                'odds': {
                    ALEX_DE_MINAUR: 1.34,
                    BERNARD_TOMIC: 3.20
                },
            },
            {
                'round': 8,
                'players': [
                    REILLY_OPELKA,
                    DANIEL_EVANS
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    REILLY_OPELKA: 1.80,
                    DANIEL_EVANS: 2.00
                },
                'prediction': DANIEL_EVANS,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    CAMERON_NORRIE,
                    ALEXEI_POPYRIN
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 1.80,
                    ALEXEI_POPYRIN: 2.00
                },
                'prediction': CAMERON_NORRIE,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    TAYLOR_FRITZ,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    TAYLOR_FRITZ: 1.45,
                    MIOMIR_KECMANOVIC: 2.70
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 10,
            },

            # 2019-07-27
            {
                'round': 4,
                'players': [
                    ALEX_DE_MINAUR,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (6, 7), (6, 3)],
                'odds': {
                    ALEX_DE_MINAUR: 1.91,
                    REILLY_OPELKA: 1.88
                }
            },
            {
                'round': 4,
                'players': [
                    TAYLOR_FRITZ,
                    CAMERON_NORRIE
                ],
                'score': [(6, 1), (3, 6), (6, 3)],
                'odds': {
                    TAYLOR_FRITZ: 1.37,
                    CAMERON_NORRIE: 2.90
                }
            },

            # 2019-07-28
            {
                'round': 2,
                'players': [
                    ALEX_DE_MINAUR,
                    TAYLOR_FRITZ
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    ALEX_DE_MINAUR: 1.90,
                    TAYLOR_FRITZ: 1.90
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 15,
            }
        ]
    },

    {
        'location': GSTAAD,
        'date': '2019-07-28',
        'matches': [

            # 2019-07-20
            {
                'round': 512,
                'players': [
                    GIAN_MARCO_MORONI,
                    LUCA_MARGAROLI
                ],
                'score': [(6, 3), (6, 4)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    VIKTOR_GALOVIC,
                    STEFANO_NAPOLITANO
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    VIKTOR_GALOVIC: 2.30,
                    STEFANO_NAPOLITANO: 1.53
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_ELAHI_GALAN,
                    ELLIOT_BENCHETRIT
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    DANIEL_ELAHI_GALAN: 1.63,
                    ELLIOT_BENCHETRIT: 2.20
                }
            },
            {
                'round': 512,
                'players': [
                    GUILLERMO_GARCIA_LOPEZ,
                    GONZALO_ESCOBAR
                ],
                'score': [(6, 1), (6, 2)],
                'odds': {
                    GUILLERMO_GARCIA_LOPEZ: 1.21,
                    GONZALO_ESCOBAR: 4.25
                }
            },
            {
                'round': 512,
                'players': [
                    MARCO_TRUNGELLITI,
                    RAPHAEL_BALTENSPERGER
                ],
                'score': [(4, 6), (6, 3), (7, 5)],
                'odds': {
                    MARCO_TRUNGELLITI: 1.09,
                    RAPHAEL_BALTENSPERGER: 6.55
                }
            },
            {
                'round': 512,
                'players': [
                    FILLIPPO_BALDI,
                    JOHAN_NIKLES
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    FILLIPPO_BALDI: 1.23,
                    JOHAN_NIKLES: 3.90
                }
            },
            {
                'round': 512,
                'players': [
                    DENNIS_NOVAK,
                    STEPHANE_ROBERT
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    DENNIS_NOVAK: 1.06,
                    STEPHANE_ROBERT: 8.07
                }
            },

            # 2019-07-21
            {
                'round': 256,
                'players': [
                    DANIEL_ELAHI_GALAN,
                    JAKUB_PAUL
                ],
                'score': [(6, 1), (2, 6), (7, 6)],
                'odds': {
                    DANIEL_ELAHI_GALAN: 1.07,
                    JAKUB_PAUL: 6.02
                }
            },
            {
                'round': 256,
                'players': [
                    GIAN_MARCO_MORONI,
                    MARCO_TRUNGELLITI
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    GIAN_MARCO_MORONI: 1.59,
                    MARCO_TRUNGELLITI: 2.22
                }
            },
            {
                'round': 256,
                'players': [
                    FILLIPPO_BALDI,
                    GUILLERMO_GARCIA_LOPEZ
                ],
                'score': [(4, 6), (7, 6), (6, 2)],
                'odds': {
                    FILLIPPO_BALDI: 2.95,
                    GUILLERMO_GARCIA_LOPEZ: 1.34
                }
            },
            {
                'round': 256,
                'players': [
                    DENNIS_NOVAK,
                    VIKTOR_GALOVIC
                ],
                'score': [(6, 1), (2, 6), (7, 6)],
                'odds': {
                    DENNIS_NOVAK: 1.36,
                    VIKTOR_GALOVIC: 2.67
                }
            },

            # 2019-07-22
            {
                'round': 32,
                'players': [
                    JIRI_VESELY,
                    ERNESTS_GULBIS
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    JIRI_VESELY: 1.49,
                    ERNESTS_GULBIS: 2.45
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANO_TRAVAGLIA,
                    DANIEL_ELAHI_GALAN
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    STEFANO_TRAVAGLIA: 1.50,
                    DANIEL_ELAHI_GALAN: 2.65
                }
            },
            {
                'round': 32,
                'players': [
                    THOMAS_FABBIANO,
                    SANDRO_EHRAT
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    THOMAS_FABBIANO: 1.68,
                    SANDRO_EHRAT: 2.00
                }
            },
            {
                'round': 32,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    CORENTIN_MOUTET
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 2.75,
                    CORENTIN_MOUTET: 1.40
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_ANDUJAR,
                    DENNIS_NOVAK
                ],
                'score': [(6, 1), (3, 6), (6, 3)],
                'odds': {
                    PABLO_ANDUJAR: 1.77,
                    DENNIS_NOVAK: 1.96
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    PAOLO_LORENZI
                ],
                'score': [(6, 7), (6, 3), (6, 2)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.32,
                    PAOLO_LORENZI: 3.34
                }
            },

            # 2019-07-23
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    HENRI_LAAKSONEN
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.67,
                    HENRI_LAAKSONEN: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    MALEK_JAZIRI
                ],
                'score': [(5, 7), (6, 3), (6, 4)],
                'odds': {
                    JAUME_MUNAR: 1.29,
                    MALEK_JAZIRI: 3.45
                }
            },
            {
                'round': 32,
                'players': [
                    GIAN_MARCO_MORONI,
                    TOMMY_ROBREDO
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    GIAN_MARCO_MORONI: 2.00,
                    TOMMY_ROBREDO: 1.77
                }
            },
            {
                'round': 32,
                'players': [
                    DENIS_ISTOMIN,
                    MARC_ANDREA_HUESLER
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DENIS_ISTOMIN: 1.74,
                    MARC_ANDREA_HUESLER: 1.95
                }
            },
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    FILLIPPO_BALDI
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    TARO_DANIEL: 1.88,
                    FILLIPPO_BALDI: 1.87
                }
            },
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    STEVE_DARCIS
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 1.36,
                    STEVE_DARCIS: 2.90
                }
            },

            # 2019-07-24
            {
                'round': 16,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    JIRI_VESELY
                ],
                'score': [(7, 6), (4, 6), (6, 3)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 2.60,
                    JIRI_VESELY: 1.45
                },
                'prediction': CEDRIC_MARCEL_STEBE,
                'bet': 5
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    STEFANO_TRAVAGLIA
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.58,
                    STEFANO_TRAVAGLIA: 2.40
                },
                'prediction': ROBERTO_CARBALLES_BAENA,
                'bet': 20
            },
            {
                'round': 16,
                'players': [
                    THOMAS_FABBIANO,
                    LORENZO_SONEGO
                ],
                'score': [(7, 6), (3, 6), (6, 1)],
                'odds': {
                    THOMAS_FABBIANO: 2.90,
                    LORENZO_SONEGO: 1.40
                },
                'prediction': LORENZO_SONEGO,
                'bet': 20
            },
            {
                'round': 16,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.95,
                    FERNANDO_VERDASCO: 1.85
                },
                'prediction': ALBERT_RAMOS_VINOLAS,
                'bet': 5
            },

            # 2019-07-25
            {
                'round': 16,
                'players': [
                    PABLO_ANDUJAR,
                    TARO_DANIEL
                ],
                'score': [(6, 1), (3, 6), (7, 6)],
                'odds': {
                    PABLO_ANDUJAR: 1.48,
                    TARO_DANIEL: 2.60
                },
                'prediction': PABLO_ANDUJAR,
                'bet': 20,
            },
            {
                'round': 16,
                'players': [
                    DUSAN_LAJOVIC,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 4), (6, 7), (7, 6)],
                'odds': {
                    DUSAN_LAJOVIC: 1.24,
                    DENIS_ISTOMIN: 4.00
                },
                'prediction': DUSAN_LAJOVIC,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    JOAO_SOUSA,
                    GIAN_MARCO_MORONI
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 1.50,
                    GIAN_MARCO_MORONI: 2.60
                },
                'prediction': JOAO_SOUSA,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    JAUME_MUNAR
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.28,
                    JAUME_MUNAR: 3.60
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 20,
            },

            # 2019-07-26
            {
                'round': 8,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.60,
                    ROBERTO_CARBALLES_BAENA: 2.30
                },
                'prediction': ALBERT_RAMOS_VINOLAS,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    PABLO_ANDUJAR,
                    DUSAN_LAJOVIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PABLO_ANDUJAR: 2.00,
                    DUSAN_LAJOVIC: 1.80
                },
                'prediction': DUSAN_LAJOVIC,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    JOAO_SOUSA,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(4, 6), (6, 3), (7, 5)],
                'odds': {
                    JOAO_SOUSA: 4.00,
                    ROBERTO_BAUTISTA_AGUT: 1.24
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 4), (2, 6), (6, 4)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 1.90,
                    THOMAS_FABBIANO: 1.90
                },
                'prediction': CEDRIC_MARCEL_STEBE,
                'bet': 10,
            },

            # 2019-07-27
            {
                'round': 4,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    PABLO_ANDUJAR
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.63,
                    PABLO_ANDUJAR: 2.23
                }
            },
            {
                'round': 4,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    JOAO_SOUSA
                ],
                'score': [(3, 6), (6, 1), (6, 2)],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 3.51,
                    JOAO_SOUSA: 1.31
                }
            },

            # 2019-07-28
            {
                'round': 2,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    CEDRIC_MARCEL_STEBE,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.22,
                    CEDRIC_MARCEL_STEBE: 4.20,
                },
                'prediction': ALBERT_RAMOS_VINOLAS,
                'bet': 15,
            }
        ]
    },

    {
        'location': HAMBURG,
        'date': '2019-07-28',
        'matches': [

            # 2019-07-20
            {
                'round': 512,
                'players': [
                    CARLOS_BERLOCQ,
                    JOZEF_KOVALIK
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    CARLOS_BERLOCQ: 3.92,
                    JOZEF_KOVALIK: 1.22
                }
            },
            {
                'round': 512,
                'players': [
                    JULIAN_LENZ,
                    JOAO_DOMINGUES
                ],
                'score': [(6, 3), (4, 6), (7, 6)],
                'odds': {
                    JULIAN_LENZ: 2.25,
                    JOAO_DOMINGUES: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEY_VATUTIN,
                    PEDRO_MARTINEZ
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ALEXEY_VATUTIN: 1.83,
                    PEDRO_MARTINEZ: 1.71
                }
            },
            {
                'round': 512,
                'players': [
                    SUMIT_NAGAL,
                    SEBASTIAN_OFNER
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    SUMIT_NAGAL: 1.45,
                    SEBASTIAN_OFNER: 2.35
                }
            },
            {
                'round': 512,
                'players': [
                    GIANLUCA_MAGER,
                    TOBIAS_KAMKE
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    GIANLUCA_MAGER: 1.49,
                    TOBIAS_KAMKE: 2.24
                }
            },
            {
                'round': 512,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    JOHANNES_HAERTEIS
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.19,
                    JOHANNES_HAERTEIS: 4.30
                }
            },
            {
                'round': 512,
                'players': [
                    HUGO_DELLIEN,
                    DANIEL_MASUR
                ],
                'score': [(4, 6), (6, 2), (7, 5)],
                'odds': {
                    HUGO_DELLIEN: 1.26,
                    DANIEL_MASUR: 3.15
                }
            },

            # 2019-07-21
            {
                'round': 256,
                'players': [
                    JULIAN_LENZ,
                    GIANLUCA_MAGER
                ],
                'score': [(6, 2), (6, 7), (7, 5)],
                'odds': {
                    JULIAN_LENZ: 2.45,
                    GIANLUCA_MAGER: 1.48
                }
            },
            {
                'round': 256,
                'players': [
                    SUMIT_NAGAL,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    SUMIT_NAGAL: 2.35,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.47
                }
            },
            {
                'round': 256,
                'players': [
                    HUGO_DELLIEN,
                    ALEXEY_VATUTIN
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    HUGO_DELLIEN: 1.42,
                    ALEXEY_VATUTIN: 2.67
                }
            },
            {
                'round': 256,
                'players': [
                    THIAGO_MONTEIRO,
                    CARLOS_BERLOCQ
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    THIAGO_MONTEIRO: 1.17,
                    CARLOS_BERLOCQ: 4.35
                }
            },

            # 2019-07-22
            {
                'round': 32,
                'players': [
                    RUDOLF_MOLLEKER,
                    LEONARDO_MAYER
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    RUDOLF_MOLLEKER: 3.38,
                    LEONARDO_MAYER: 1.30
                }
            },
            {
                'round': 32,
                'players': [
                    MARTIN_KLIZAN,
                    DANIEL_ALTMAIER
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    MARTIN_KLIZAN: 1.42,
                    DANIEL_ALTMAIER: 2.90
                }
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    MARTON_FUCSOVICS: 2.25,
                    PHILIPP_KOHLSCHREIBER: 1.63
                }
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    CHRISTIAN_GARIN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ANDREY_RUBLEV: 2.13,
                    CHRISTIAN_GARIN: 1.67
                }
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    BENOIT_PAIRE
                ],
                'score': [(6, 7), (7, 5), (6, 3)],
                'odds': {
                    JEREMY_CHARDY: 1.96,
                    BENOIT_PAIRE: 1.77
                }
            },

            # 2019-07-23
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    ROBIN_HAASE
                ],
                'score': [(6, 3), (3, 6), (6, 1)],
                'odds': {
                    CASPER_RUUD: 1.43,
                    ROBIN_HAASE: 2.65
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.44,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.76
                }
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    SUMIT_NAGAL
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    RICHARD_GASQUET: 1.40,
                    SUMIT_NAGAL: 2.70
                }
            },
            {
                'round': 32,
                'players': [
                    FEDERICO_DELBONIS,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 7), (7, 6), (6, 2)],
                'odds': {
                    FEDERICO_DELBONIS: 1.45,
                    MARCO_CECCHINATO: 2.68
                }
            },
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    YANNICK_HANFMANN
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.74,
                    YANNICK_HANFMANN: 2.00
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    THIAGO_MONTEIRO
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.63,
                    THIAGO_MONTEIRO: 2.25
                }
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    LASLO_DJERE
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.58,
                    LASLO_DJERE: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    HUGO_DELLIEN
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.77,
                    HUGO_DELLIEN: 1.95
                }
            },
            {
                'round': 32,
                'players': [
                    FABIO_FOGNINI,
                    JULIAN_LENZ
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.24,
                    JULIAN_LENZ: 4.20
                }
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    NICOLAS_JARRY
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.42,
                    NICOLAS_JARRY: 2.87
                }
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    PABLO_CUEVAS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DOMINIC_THIEM: 1.25,
                    PABLO_CUEVAS: 3.85
                }
            },

            # 2019-07-24
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    CASPER_RUUD
                ],
                'score': [(3, 6), (7, 5), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 1.90,
                    CASPER_RUUD: 1.90
                },
                'prediction': CASPER_RUUD,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    JEREMY_CHARDY,
                    RICHARD_GASQUET
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    JEREMY_CHARDY: 1.80,
                    RICHARD_GASQUET: 2.00
                },
                'prediction': JEREMY_CHARDY,
                'bet': 5
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    MARTON_FUCSOVICS
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    DOMINIC_THIEM: 1.18,
                    MARTON_FUCSOVICS: 4.60
                },
                'prediction': DOMINIC_THIEM,
                'bet': 20
            },
            {
                'round': 16,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 4), (3, 6), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.05,
                    JUAN_IGNACIO_LONDERO: 1.75
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 5
            },

            # 2019-07-25
            {
                'round': 16,
                'players': [
                    FILIP_KRAJINOVIC,
                    MARTIN_KLIZAN
                ],
                'score': [(6, 7), (7, 5), (6, 1)],
                'odds': {
                    FILIP_KRAJINOVIC: 1.45,
                    MARTIN_KLIZAN: 2.70
                },
                'prediction': FILIP_KRAJINOVIC,
                'bet': 20,
            },
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 2.50,
                    JAN_LENNARD_STRUFF: 1.52
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 20,
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.26,
                    FEDERICO_DELBONIS: 3.80
                },
                'prediction': FEDERICO_DELBONIS,
                'bet': 20,
            },
            {
                'round': 16,
                'players': [
                    FABIO_FOGNINI,
                    RUDOLF_MOLLEKER
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    FABIO_FOGNINI: 1.30,
                    RUDOLF_MOLLEKER: 3.40
                },
                'prediction': FABIO_FOGNINI,
                'bet': 20,
            },

            # 2019-07-26
            {
                'round': 8,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    JEREMY_CHARDY
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.80,
                    JEREMY_CHARDY: 2.00
                },
                'prediction': JEREMY_CHARDY,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    ANDREY_RUBLEV,
                    DOMINIC_THIEM
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    ANDREY_RUBLEV: 5.50,
                    DOMINIC_THIEM: 1.14
                },
                'prediction': DOMINIC_THIEM,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    ALEXANDER_ZVEREV,
                    FILIP_KRAJINOVIC
                ],
                'score': [(2, 6), (7, 5), (6, 2)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.36,
                    FILIP_KRAJINOVIC: 3.10
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    FABIO_FOGNINI
                ],
                'score': [(3, 6), (6, 2), (7, 6)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.80,
                    FABIO_FOGNINI: 2.00
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 10,
            },

            # 2019-07-27
            {
                'round': 4,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    ALEXANDER_ZVEREV
                ],
                'score': [(6, 4), (4, 6), (7, 6)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 3.07,
                    ALEXANDER_ZVEREV: 1.35
                }
            },
            {
                'round': 4,
                'players': [
                    ANDREY_RUBLEV,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(4, 6), (7, 5), (6, 1)],
                'odds': {
                    ANDREY_RUBLEV: 1.71,
                    PABLO_CARRENO_BUSTA: 2.00
                }
            },

            # 2019-07-28
            {
                'round': 2,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    ANDREY_RUBLEV,
                ],
                'score': [(7, 5), (4, 6), (6, 3)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 2.05,
                    ANDREY_RUBLEV: 1.75,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 15,
            }
        ]
    },

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
                    DANILL_MEDVEDEV,
                    BJORN_FRATANGELO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    DANILL_MEDVEDEV: 1.22,
                    BJORN_FRATANGELO: 4.20,
                },
                'prediction': DANILL_MEDVEDEV,
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
                    DANILL_MEDVEDEV,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    DANILL_MEDVEDEV: 1.45,
                    FRANCES_TIAFOE: 2.70,
                },
                'prediction': DANILL_MEDVEDEV,
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
                    DANILL_MEDVEDEV,
                    MARIN_CILIC,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DANILL_MEDVEDEV: 1.68,
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
                    DANILL_MEDVEDEV,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DANILL_MEDVEDEV: 1.16,
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
                    DANILL_MEDVEDEV
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 2.10,
                    DANILL_MEDVEDEV: 1.65,
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
                    DANILL_MEDVEDEV,
                    KYLE_EDMUND
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    DANILL_MEDVEDEV: 1.48,
                    KYLE_EDMUND: 2.50,
                },
                'prediction': DANILL_MEDVEDEV,
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
                    DANILL_MEDVEDEV,
                    CHRISTIAN_GARIN
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    DANILL_MEDVEDEV: 1.16,
                    CHRISTIAN_GARIN: 5.00,
                },
                'prediction': DANILL_MEDVEDEV,
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
                    DANILL_MEDVEDEV,
                    DOMINIC_THIEM
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DANILL_MEDVEDEV: 1.60,
                    DOMINIC_THIEM: 2.30,
                },
                'prediction': DANILL_MEDVEDEV,
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
                    DANILL_MEDVEDEV,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    DANILL_MEDVEDEV: 1.49,
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
                    DANILL_MEDVEDEV,
                ],
                'score': [(6, 3), (6, 0)],
                'odds': {
                    RAFAEL_NADAL: 1.40,
                    DANILL_MEDVEDEV: 2.90,
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
                    DANILL_MEDVEDEV,
                    KYLE_EDMUND,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    DANILL_MEDVEDEV: 1.42,
                    KYLE_EDMUND: 2.80,
                },
                'prediction': DANILL_MEDVEDEV,
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
                    DANILL_MEDVEDEV,
                    BENOIT_PAIRE
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    DANILL_MEDVEDEV: 1.25,
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
                    DANILL_MEDVEDEV,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    DANILL_MEDVEDEV: 1.40,
                    JAN_LENNARD_STRUFF: 2.80,
                },
                'prediction': DANILL_MEDVEDEV,
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
                    DANILL_MEDVEDEV,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    DANILL_MEDVEDEV: 1.30,
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
                    DANILL_MEDVEDEV,
                    NOVAK_DJOKOVIC,
                ],
                'score': [(3, 6), (6, 3), (6, 3)],
                'odds': {
                    DANILL_MEDVEDEV: 3.40,
                    NOVAK_DJOKOVIC: 1.30,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 4,
            },

            # 2019-08-18
            {
                'round': 2,
                'players': [
                    DANILL_MEDVEDEV,
                    DAVID_GOFFIN,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    DANILL_MEDVEDEV: 1.40,
                    DAVID_GOFFIN: 2.90,
                },
                'prediction': DANILL_MEDVEDEV,
                'bet': 4,
            }
        ]
    },

    ###############################################################################
    # Active
    ###############################################################################

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
                'round': 32,
                'players': [
                    ROBIN_HAASE,
                    JOHN_MILLMAN,
                ],
                'odds': {
                    ROBIN_HAASE: 2.50,
                    JOHN_MILLMAN: 1.52,
                },
                'prediction': ROBIN_HAASE,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    UGO_HUMBERT,
                ],
                'odds': {
                    BENOIT_PAIRE: 1.90,
                    UGO_HUMBERT: 1.90,
                },
                'prediction': UGO_HUMBERT,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    STEVE_JOHNSON,
                ],
                'odds': {
                    CASPER_RUUD: 2.80,
                    STEVE_JOHNSON: 1.42,
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
                    MIOMIR_KECMANOVIC,
                    DENIS_SHAPOVALOV,
                ],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.10,
                    DENIS_SHAPOVALOV: 1.70,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    FELICIANO_LOPEZ,
                    HUBERT_HURKACZ,
                ],
                'odds': {
                    FELICIANO_LOPEZ: 2.80,
                    HUBERT_HURKACZ: 1.42,
                },
                'prediction': HUBERT_HURKACZ,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    FRANCES_TIAFOE,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 2.20,
                    FRANCES_TIAFOE: 1.65,
                },
                'prediction': FRANCES_TIAFOE,
                'bet': 8,
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    ANDREY_RUBLEV,
                ],
                'odds': {
                    SAM_QUERREY: 1.70,
                    ANDREY_RUBLEV: 2.10,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 2,
            },

            #
        ]
    },
]
