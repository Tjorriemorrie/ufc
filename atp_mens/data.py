from men import *
from location import *

# score mat roi acc profit  desc
# 19.8  70  28  79  5650    2020-02 NEW YORK        (1, 695), (2, 613), (3, 362), (9, 361), (4, 305)
# 20.0  78  26  75  5680    2020-02 ROTTERDAM       (1, 746), (2, 704), (3, 446), (4, 321), (10, 309)
# 19.4  71  27  78  5460    2020-02 CORDOBA         (2, 639), (3, 532), (1, 510), (4, 331), (9, 316)
# 19.4  71  27  78  5400    2020-02 MONTPELLIER     (2, 576), (1, 552), (3, 534), (4, 375), (8, 318)
# 22.8  68  34  83  4660    2020-02 PUNE            (1, 690), (2, 576), (3, 544), (4, 500), (5, 476)

# 22.9  67  34  84  4640    2020-02 AUSTRALIAN OPEN (1, 676), (2, 562), (3, 546), (4, 514), (5, 473)
# 22.8  67  34  84  4740    2020-01 ADELAIDE        (1, 644), (4, 596), (5, 521), (3, 506), (2, 449)
# 22.3  79  28  75  4100    2020 atp cup
# 79.5  26.7    2820    2019 basel                  (1, 688), (2, 627), (3, 449), (4, 408), (5, 346)

# 93.6  38.8    3474    2019 antwerp                (4, 335), (2, 323), (3, 268), (7, 251), (1, 247)
# 75.4  29.3    2619    2019 moscow                         (1, 992), (2, 428), (5, 214), (6, 206)
# 78.7  26.3    2111    2019 beijing                        (1, 1098), (3, 658), (4, 648), (2, 646)

# 79.1  24.2    1431    2018 umag                           (1, 1143), (2, 758), (3, 445), (4, 264)
# 72.1  10.0    1191    2018 washington                     (3, 1187), (4, 538), (6, 337), (1, 283)

# 72.9  7.9     349     2019-08-31                          (1, 1534), (2, 974), (0, 819), (3, 160)

DATA = [
    {
        'location': AUSTRALIAN_OPEN,
        'date': '2020-02-03',
        'matches': [

            # 2020-01-20
            {
                'round': 128,
                'players': [
                    MATTEO_BERRETTINI,
                    ANDREW_HARRIS,
                ],
                'odds': {
                    MATTEO_BERRETTINI: 1.13,
                    ANDREW_HARRIS: 6.00,
                },
                'score': [(6, 3), (6, 1), (6, 3)],
                'prediction': MATTEO_BERRETTINI,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    RICARDAS_BERANKIS,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'odds': {
                    RICARDAS_BERANKIS: 1.65,
                    ROBERTO_CARBALLES_BAENA: 2.25,
                },
                'score': [(6, 4), (6, 2), (6, 2)],
                'prediction': RICARDAS_BERANKIS,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    DANIEL_EVANS,
                    MACKENZIE_MCDONALD,
                ],
                'odds': {
                    DANIEL_EVANS: 1.13,
                    MACKENZIE_MCDONALD: 6.00,
                },
                'score': [(3, 6), (4, 6), (6, 1), (6, 2), (6, 3)],
                'prediction': DANIEL_EVANS,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    LASLO_DJERE,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.42,
                    LASLO_DJERE: 2.90,
                },
                'score': [(6, 4), (3, 6), (6, 2), (7, 6)],
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    GUIDO_PELLA,
                    JOHN_PATRICK_SMITH,
                ],
                'odds': {
                    GUIDO_PELLA: 1.18,
                    JOHN_PATRICK_SMITH: 5.00,
                },
                'score': [(6, 3), (7, 5), (6, 4)],
                'prediction': GUIDO_PELLA,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    SAM_QUERREY,
                    BORNA_CORIC,
                ],
                'odds': {
                    SAM_QUERREY: 2.30,
                    BORNA_CORIC: 1.62,
                },
                'score': [(6, 3), (6, 4), (6, 4)],
                'prediction': BORNA_CORIC,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    GREGOIRE_BARRERE,
                    MOHAMED_SAFWAT,
                ],
                'odds': {
                    GREGOIRE_BARRERE: 1.30,
                    MOHAMED_SAFWAT: 3.60,
                },
                'score': [(6, 7), (7, 6), (6, 4), (7, 6)],
            },
            {
                'round': 128,
                'players': [
                    MARTON_FUCSOVICS,
                    DENIS_SHAPOVALOV,
                ],
                'odds': {
                    MARTON_FUCSOVICS: 5.00,
                    DENIS_SHAPOVALOV: 1.18,
                },
                'score': [(6, 3), (6, 7), (6, 1), (7, 6)],
            },
            {
                'round': 128,
                'players': [
                    ROGER_FEDERER,
                    STEVE_JOHNSON,
                ],
                'odds': {
                    ROGER_FEDERER: 1.04,
                    STEVE_JOHNSON: 11.00,
                },
                'score': [(6, 3), (6, 2), (6, 2)],
            },
            {
                'round': 128,
                'players': [
                    GRIGOR_DIMITROV,
                    JUAN_IGNACIO_LONDERO,
                ],
                'odds': {
                    GRIGOR_DIMITROV: 1.13,
                    JUAN_IGNACIO_LONDERO: 6.00,
                },
                'score': [(4, 6), (6, 2), (6, 0), (6, 4)],
                'prediction': GRIGOR_DIMITROV,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    MARCOS_GIRON,
                ],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.34,
                    MARCOS_GIRON: 3.30,
                },
                'score': [(7, 5), (6, 1), (6, 2)],
                'prediction': PHILIPP_KOHLSCHREIBER,
                'bet': 6,
            },

            # 2020-01-21
            {
                'round': 128,
                'players': [
                    DUSAN_LAJOVIC,
                    KYLE_EDMUND,
                ],
                'odds': {
                    DUSAN_LAJOVIC: 2.70,
                    KYLE_EDMUND: 1.46,
                },
                'score': [(7, 6), (6, 3), (7, 6)],
                'prediction': KYLE_EDMUND,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    FABIO_FOGNINI,
                    REILLY_OPELKA,
                ],
                'odds': {
                    FABIO_FOGNINI: 1.85,
                    REILLY_OPELKA: 1.95,
                },
                'score': [(3, 6), (6, 7), (6, 4), (6, 3), (7, 6)],
            },
            {
                'round': 128,
                'players': [
                    TENNYS_SANDGREN,
                    MARCO_TRUNGELLITI,
                ],
                'odds': {
                    TENNYS_SANDGREN: 1.40,
                    MARCO_TRUNGELLITI: 3.00,
                },
                'score': [(6, 1), (6, 3), (7, 5)],
                'prediction': TENNYS_SANDGREN,
                'bet': 7,
            },
            {
                'round': 128,
                'players': [
                    MARIN_CILIC,
                    CORENTIN_MOUTET,
                ],
                'odds': {
                    MARIN_CILIC: 1.53,
                    CORENTIN_MOUTET: 2.50,
                },
                'score': [(6, 3), (6, 2), (6, 4)],
                'prediction': MARIN_CILIC,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    FILIP_KRAJINOVIC,
                    QUENTIN_HALYS,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 1.25,
                    QUENTIN_HALYS: 4.00,
                },
                'score': [(7, 6), (7, 6), (3, 6), (4, 6), (7, 5)],
                'prediction': FILIP_KRAJINOVIC,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    JORDAN_THOMPSON,
                    ALEXANDER_BUBLIK,
                ],
                'odds': {
                    JORDAN_THOMPSON: 1.90,
                    ALEXANDER_BUBLIK: 1.90,
                },
                'score': [(6, 4), (6, 3), (6, 2)],
            },
            {
                'round': 128,
                'players': [
                    MICHAEL_MMOH,
                    PABLO_ANDUJAR,
                ],
                'odds': {
                    MICHAEL_MMOH: 1.60,
                    PABLO_ANDUJAR: 2.35,
                },
                'score': [(6, 1), (6, 4), (6, 4)],
                'prediction': MICHAEL_MMOH,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    NORBERT_GOMBOS,
                ],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.70,
                    NORBERT_GOMBOS: 2.15,
                },
                'score': [(4, 6), (6, 4), (2, 6), (6, 3), (6, 2)],
                'prediction': ALEJANDRO_DAVIDOVICH_FOKINA,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    HUBERT_HURKACZ,
                    DENNIS_NOVAK,
                ],
                'odds': {
                    HUBERT_HURKACZ: 1.37,
                    DENNIS_NOVAK: 3.10,
                },
                'score': [(6, 7), (1, 6), (6, 2), (6, 3), (6, 4)],
                'prediction': HUBERT_HURKACZ,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    TOMMY_PAUL,
                    LEONARDO_MAYER,
                ],
                'odds': {
                    TOMMY_PAUL: 1.32,
                    LEONARDO_MAYER: 3.40,
                },
                'score': [(4, 6), (6, 4), (6, 4), (6, 4)],
            },
            {
                'round': 128,
                'players': [
                    MARC_POLMANS,
                    MIKHAIL_KUKUSHKIN,
                ],
                'odds': {
                    MARC_POLMANS: 2.90,
                    MIKHAIL_KUKUSHKIN: 1.42,
                },
                'score': [(6, 4), (6, 3), (4, 6), (6, 7), (6, 4)],
                'prediction': MIKHAIL_KUKUSHKIN,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    JOHN_MILLMAN,
                    UGO_HUMBERT,
                ],
                'odds': {
                    JOHN_MILLMAN: 1.90,
                    UGO_HUMBERT: 1.90,
                },
                'score': [(7, 6), (6, 3), (1, 6), (7, 5)],
            },
            {
                'round': 128,
                'players': [
                    BENOIT_PAIRE,
                    CEDRIC_MARCEL_STEBE,
                ],
                'odds': {
                    BENOIT_PAIRE: 1.27,
                    CEDRIC_MARCEL_STEBE: 3.80,
                },
                'score': [(6, 4), (3, 6), (6, 3), (6, 7), (6, 0)],
                'prediction': BENOIT_PAIRE,
                'bet': 7,
            },
            {
                'round': 128,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    LLOYD_HARRIS,
                ],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.25,
                    LLOYD_HARRIS: 4.00,
                },
                'score': [(6, 4), (6, 2), (6, 2)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    TATSUMA_ITO,
                    PRAJNESH_GUNNESWARAN,
                ],
                'odds': {
                    TATSUMA_ITO: 2.45,
                    PRAJNESH_GUNNESWARAN: 1.55,
                },
                'score': [(6, 4), (6, 2), (7, 5)],
                'prediction': PRAJNESH_GUNNESWARAN,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    STEFANOS_TSITSIPAS,
                    MARCOS_GIRON,
                ],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.02,
                    MARCOS_GIRON: 3.30,
                },
                'score': [(6, 0), (6, 2), (6, 3)],
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    NOVAK_DJOKOVIC,
                    JAN_LENNARD_STRUFF,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    JAN_LENNARD_STRUFF: 21.00,
                },
                'score': [(7, 6), (6, 2), (2, 6), (6, 1)],
            },
            {
                'round': 128,
                'players': [
                    CHRISTIAN_GARIN,
                    STEFANO_TRAVAGLIA,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.70,
                    STEFANO_TRAVAGLIA: 2.15,
                },
                'score': [(6, 4), (6, 3), (6, 4)],
                'prediction': CHRISTIAN_GARIN,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    FELICIANO_LOPEZ,
                ],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.13,
                    FELICIANO_LOPEZ: 6.00,
                },
                'score': [(6, 2), (6, 2), (7, 5)],
            },
            {
                'round': 128,
                'players': [
                    JANNIK_SINNER,
                    MAX_PURCELL,
                ],
                'odds': {
                    JANNIK_SINNER: 1.27,
                    MAX_PURCELL: 3.80,
                },
                'score': [(7, 6), (6, 2), (6, 4)],
            },
            {
                'round': 128,
                'players': [
                    ERNESTS_GULBIS,
                    FELIX_AUGER_ALIASSIME,
                ],
                'odds': {
                    ERNESTS_GULBIS: 4.20,
                    FELIX_AUGER_ALIASSIME: 1.23,
                },
                'score': [(7, 5), (4, 6), (7, 6), (6, 4)],
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    DOMINIC_THIEM,
                    ADRIAN_MANNARINO,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.11,
                    ADRIAN_MANNARINO: 6.50,
                },
                'score': [(6, 3), (7, 5), (6, 2)],
            },
            {
                'round': 128,
                'players': [
                    KAREN_KHACHANOV,
                    MARIO_VILELLA_MARTINEZ,
                ],
                'odds': {
                    KAREN_KHACHANOV: 1.02,
                    MARIO_VILELLA_MARTINEZ: 14.00,
                },
                'score': [(4, 6), (6, 4), (7, 6), (6, 3)],
            },
            {
                'round': 128,
                'players': [
                    MIKAEL_YMER,
                    YASUTAKA_UCHIYAMA,
                ],
                'odds': {
                    MIKAEL_YMER: 1.32,
                    YASUTAKA_UCHIYAMA: 3.40,
                },
                'score': [(6, 4), (6, 1), (6, 2)],
            },
            {
                'round': 128,
                'players': [
                    ALJAZ_BEDENE,
                    JAMES_DUCKWORTH,
                ],
                'odds': {
                    ALJAZ_BEDENE: 1.68,
                    JAMES_DUCKWORTH: 2.20,
                },
                'score': [(6, 4), (6, 7), (6, 7), (6, 2), (6, 4)],
            },
            {
                'round': 128,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    SOONWOO_KWON,
                ],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.77,
                    SOONWOO_KWON: 2.05,
                },
                'score': [(6, 7), (6, 4), (7, 5), (3, 6), (6, 3)],
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    STAN_WAWRINKA,
                    DAMIR_DZUMHUR,
                ],
                'odds': {
                    STAN_WAWRINKA: 1.11,
                    DAMIR_DZUMHUR: 6.50,
                },
                'score': [(7, 5), (6, 7), (6, 4), (6, 4)],
                'prediction': STAN_WAWRINKA,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    RAFAEL_NADAL,
                    HUGO_DELLIEN,
                ],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    HUGO_DELLIEN: 15.00,
                },
                'score': [(6, 2), (6, 3), (6, 0)],
                'prediction': RAFAEL_NADAL,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JOZEF_KOVALIK,
                ],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.10,
                    JOZEF_KOVALIK: 7.00,
                },
                'score': [(6, 4), (3, 6), (6, 1), (7, 6)],
            },
            {
                'round': 128,
                'players': [
                    FERNANDO_VERDASCO,
                    EVGENY_DONSKOY,
                ],
                'odds': {
                    FERNANDO_VERDASCO: 1.34,
                    EVGENY_DONSKOY: 3.30,
                },
                'score': [(7, 5), (6, 2), (6, 1)],
                'prediction': FERNANDO_VERDASCO,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    ALEX_BOLT,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'odds': {
                    ALEX_BOLT: 2.40,
                    ALBERT_RAMOS_VINOLAS: 1.58,
                },
                'score': [(7, 6), (1, 6), (6, 7), (6, 1), (6, 4)],
                'prediction': ALBERT_RAMOS_VINOLAS,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    ANDREAS_SEPPI,
                    MIOMIR_KECMANOVIC,
                ],
                'odds': {
                    ANDREAS_SEPPI: 2.80,
                    MIOMIR_KECMANOVIC: 1.44,
                },
                'score': [(6, 4), (6, 4), (7, 6)],
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    CAMERON_NORRIE,
                ],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.62,
                    CAMERON_NORRIE: 2.30,
                },
                'score': [(7, 5), (3, 6), (3, 6), (7, 5), (6, 4)],
                'prediction': PIERRE_HUGUES_HERBERT,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    ALEXEI_POPYRIN,
                    JO_WILFRIED_TSONGA,
                ],
                'odds': {
                    ALEXEI_POPYRIN: 2.70,
                    JO_WILFRIED_TSONGA: 1.46,
                },
                'score': [(6, 7), (6, 2), (6, 1)],
                'retired': True,
            },
            {
                'round': 128,
                'players': [
                    ANDREY_RUBLEV,
                    CHRISTOPHER_O_CONNELL,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.04,
                    CHRISTOPHER_O_CONNELL: 11.00,
                },
                'score': [(6, 3), (0, 6), (6, 4), (7, 6)],
            },
            {
                'round': 128,
                'players': [
                    YUICHI_SUGITA,
                    ELLIOT_BENCHETRIT,
                ],
                'odds': {
                    YUICHI_SUGITA: 1.40,
                    ELLIOT_BENCHETRIT: 3.00,
                },
                'score': [(6, 2), (6, 0), (6, 3)],
                'prediction': YUICHI_SUGITA,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    PETER_GOJOWCZYK,
                    CHRISTOPHER_EUBANKS,
                ],
                'odds': {
                    PETER_GOJOWCZYK: 1.50,
                    CHRISTOPHER_EUBANKS: 2.60,
                },
                'score': [(7, 6), (6, 3), (4, 6), (6, 0)],
                'prediction': PETER_GOJOWCZYK,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    JOHN_ISNER,
                    THIAGO_MONTEIRO,
                ],
                'odds': {
                    JOHN_ISNER: 1.25,
                    THIAGO_MONTEIRO: 4.00,
                },
                'score': [(6, 7), (7, 6), (7, 6), (7, 6)],
                'prediction': JOHN_ISNER,
                'bet': 7,
            },
            {
                'round': 128,
                'players': [
                    IVO_KARLOVIC,
                    VASEK_POSPISIL,
                ],
                'odds': {
                    IVO_KARLOVIC: 4.60,
                    VASEK_POSPISIL: 1.20,
                },
                'score': [(7, 6), (6, 4), (7, 5)],
            },
            {
                'round': 128,
                'players': [
                    FEDERICO_DELBONIS,
                    JOAO_SOUSA,
                ],
                'odds': {
                    FEDERICO_DELBONIS: 1.80,
                    JOAO_SOUSA: 2.00,
                },
                'score': [(6, 3), (6, 4), (7, 6)],
                'prediction': FEDERICO_DELBONIS,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    JAUME_MUNAR,
                    HUGO_GASTON,
                ],
                'odds': {
                    JAUME_MUNAR: 1.27,
                    HUGO_GASTON: 3.80,
                },
                'score': [(7, 5), (5, 7), (6, 0), (6, 3)],
                'prediction': JAUME_MUNAR,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    DAVID_GOFFIN,
                    JEREMY_CHARDY,
                ],
                'odds': {
                    DAVID_GOFFIN: 1.18,
                    JEREMY_CHARDY: 5.00,
                },
                'score': [(6, 4), (6, 3), (6, 1)],
                'prediction': DAVID_GOFFIN,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    GILLES_SIMON,
                    PABLO_CUEVAS,
                ],
                'odds': {
                    GILLES_SIMON: 1.44,
                    PABLO_CUEVAS: 2.80,
                },
                'score': [(6, 1), (6, 3), (6, 3)],
                'prediction': GILLES_SIMON,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    TAYLOR_FRITZ,
                    TALLON_GRIEKSPOOR,
                ],
                'odds': {
                    TAYLOR_FRITZ: 1.20,
                    TALLON_GRIEKSPOOR: 4.60,
                },
                'score': [(6, 3), (6, 3), (6, 3)],
                'prediction': TAYLOR_FRITZ,
                'bet': 6,
            },
            {
                'round': 128,
                'players': [
                    KEVIN_ANDERSON,
                    ILYA_IVASHKA,
                ],
                'odds': {
                    KEVIN_ANDERSON: 1.20,
                    ILYA_IVASHKA: 4.60,
                },
                'score': [(6, 4), (2, 6), (4, 6), (6, 4), (7, 6)],
                'prediction': KEVIN_ANDERSON,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    NICK_KYRGIOS,
                    LORENZO_SONEGO,
                ],
                'odds': {
                    NICK_KYRGIOS: 1.11,
                    LORENZO_SONEGO: 6.50,
                },
                'score': [(6, 2), (7, 6), (7, 6)],
                'prediction': NICK_KYRGIOS,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    DANIIL_MEDVEDEV,
                    FRANCES_TIAFOE,
                ],
                'odds': {
                    DANIIL_MEDVEDEV: 1.04,
                    FRANCES_TIAFOE: 11.00,
                },
                'score': [(6, 3), (4, 6), (6, 4), (6, 2)],
                'prediction': DANIIL_MEDVEDEV,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    ALEJANDRO_TABILO,
                    DANIEL_ELAHI_GALAN,
                ],
                'odds': {
                    ALEJANDRO_TABILO: 2.70,
                    DANIEL_ELAHI_GALAN: 1.46,
                },
                'score': [(4, 6), (6, 3), (6, 4), (6, 7), (6, 4)],
                'prediction': DANIEL_ELAHI_GALAN,
                'bet': 1,
            },
            {
                'round': 128,
                'players': [
                    PEDRO_MARTINEZ,
                    DOMINIK_KOEPFER,
                ],
                'odds': {
                    PEDRO_MARTINEZ: 2.60,
                    DOMINIK_KOEPFER: 1.50,
                },
                'score': [(6, 3), (6, 4), (7, 5)],
                'prediction': DOMINIK_KOEPFER,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    EGOR_GERASIMOV,
                    CASPER_RUUD,
                ],
                'odds': {
                    EGOR_GERASIMOV: 3.30,
                    CASPER_RUUD: 1.34,
                },
                'score': [(6, 3), (7, 6), (1, 6), (4, 6), (7, 6)],
                'prediction': CASPER_RUUD,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    ALEXANDER_ZVEREV,
                    MARCO_CECCHINATO,
                ],
                'odds': {
                    ALEXANDER_ZVEREV: 1.09,
                    MARCO_CECCHINATO: 7.50,
                },
                'score': [(6, 4), (7, 6), (6, 3)],
                'prediction': ALEXANDER_ZVEREV,
                'bet': 2,
            },

            # 2020-01-22
            {
                'round': 64,
                'players': [
                    SAM_QUERREY,
                    RICARDAS_BERANKIS,
                ],
                'odds': {
                    SAM_QUERREY: 1.32,
                    RICARDAS_BERANKIS: 3.40,
                },
                'score': [(7, 6), (4, 6), (6, 4), (6, 4)],
                'prediction': SAM_QUERREY,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    DANIEL_EVANS,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.15,
                    DANIEL_EVANS: 1.70,
                },
                'score': [(6, 4), (6, 3), (6, 4)],
                'prediction': DANIEL_EVANS,
                'bet': 8,
            },
            {
                'round': 64,
                'players': [
                    GUIDO_PELLA,
                    GREGOIRE_BARRERE,
                ],
                'odds': {
                    GUIDO_PELLA: 1.42,
                    GREGOIRE_BARRERE: 2.90,
                },
                'score': [(6, 1), (6, 4), (3, 6), (6, 3)],
                'prediction': GUIDO_PELLA,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    MARTON_FUCSOVICS,
                    JANNIK_SINNER,
                ],
                'odds': {
                    MARTON_FUCSOVICS: 2.10,
                    JANNIK_SINNER: 1.75,
                },
                'score': [(6, 4), (6, 4), (6, 3)],
                'prediction': JANNIK_SINNER,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    TENNYS_SANDGREN,
                    MATTEO_BERRETTINI,
                ],
                'odds': {
                    TENNYS_SANDGREN: 4.00,
                    MATTEO_BERRETTINI: 1.25,
                },
                'score': [(7, 6), (6, 4), (4, 6), (2, 6), (7, 5)],
                'prediction': MATTEO_BERRETTINI,
                'bet': 7,
            },
            {
                'round': 64,
                'players': [
                    NOVAK_DJOKOVIC,
                    TATSUMA_ITO,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    TATSUMA_ITO: 21.00,
                },
                'score': [(6, 1), (6, 4), (6, 2)],
            },
            {
                'round': 64,
                'players': [
                    MARIN_CILIC,
                    BENOIT_PAIRE,
                ],
                'odds': {
                    MARIN_CILIC: 1.35,
                    BENOIT_PAIRE: 3.20,
                },
                'score': [(6, 2), (6, 7), (3, 6), (6, 1), (7, 6)],
                'prediction': MARIN_CILIC,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    TOMMY_PAUL,
                    GRIGOR_DIMITROV,
                ],
                'odds': {
                    TOMMY_PAUL: 3.10,
                    GRIGOR_DIMITROV: 1.37,
                },
                'score': [(6, 4), (7, 6), (3, 6), (6, 7), (7, 6)],
                'prediction': GRIGOR_DIMITROV,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                ],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.18,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 5.00,
                },
                'score': [(6, 1), (6, 4), (6, 2)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    STEFANOS_TSITSIPAS,
                    PHILIPP_KOHLSCHREIBER,
                ],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.13,
                    PHILIPP_KOHLSCHREIBER: 6.00,
                },
                'score': [],
                'retired': True,
            },
            {
                'round': 64,
                'players': [
                    MILOS_RAONIC,
                    CHRISTIAN_GARIN,
                ],
                'odds': {
                    MILOS_RAONIC: 1.32,
                    CHRISTIAN_GARIN: 3.40,
                },
                'score': [(6, 3), (6, 4), (6, 2)],
                'prediction': MILOS_RAONIC,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    JOHN_MILLMAN,
                    HUBERT_HURKACZ,
                ],
                'odds': {
                    JOHN_MILLMAN: 2.00,
                    HUBERT_HURKACZ: 1.80,
                },
                'score': [(6, 4), (7, 5), (6, 3)],
                'prediction': HUBERT_HURKACZ,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    MICHAEL_MMOH,
                ],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.10,
                    MICHAEL_MMOH: 7.00,
                },
                'score': [(5, 7), (6, 2), (6, 4), (6, 1)],
            },
            {
                'round': 64,
                'players': [
                    DUSAN_LAJOVIC,
                    MARC_POLMANS,
                ],
                'odds': {
                    DUSAN_LAJOVIC: 1.23,
                    MARC_POLMANS: 4.20,
                },
                'score': [(6, 2), (6, 4), (6, 3)],
                'prediction': DUSAN_LAJOVIC,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    JORDAN_THOMPSON,
                ],
                'odds': {
                    FABIO_FOGNINI: 1.60,
                    JORDAN_THOMPSON: 2.35,
                },
                'score': [(7, 6), (6, 1), (3, 6), (4, 6), (7, 6)],
                'prediction': FABIO_FOGNINI,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    ROGER_FEDERER,
                    FILIP_KRAJINOVIC,
                ],
                'odds': {
                    ROGER_FEDERER: 1.02,
                    FILIP_KRAJINOVIC: 14.00,
                },
                'score': [(6, 1), (6, 4), (6, 1)],
            },

            # 2020-01-23
            {
                'round': 64,
                'players': [
                    ERNESTS_GULBIS,
                    ALJAZ_BEDENE,
                ],
                'odds': {
                    ERNESTS_GULBIS: 2.35,
                    ALJAZ_BEDENE: 1.60,
                },
                'score': [(7, 5), (6, 3), (6, 2)],
                'prediction': ALJAZ_BEDENE,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    FERNANDO_VERDASCO,
                    NIKOLOZ_BASILASHVILI,
                ],
                'odds': {
                    FERNANDO_VERDASCO: 1.62,
                    NIKOLOZ_BASILASHVILI: 2.30,
                },
                'score': [(4, 6), (7, 6), (6, 4), (6, 4)],
            },
            {
                'round': 64,
                'players': [
                    DANIIL_MEDVEDEV,
                    PEDRO_MARTINEZ,
                ],
                'odds': {
                    DANIIL_MEDVEDEV: 1.01,
                    PEDRO_MARTINEZ: 21.00,
                },
                'score': [(7, 5), (6, 1), (6, 3)],
                'prediction': DANIIL_MEDVEDEV,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    GAEL_MONFILS,
                    IVO_KARLOVIC,
                ],
                'odds': {
                    GAEL_MONFILS: 1.25,
                    IVO_KARLOVIC: 4.00,
                },
                'score': [(4, 6), (7, 6), (6, 4), (7, 5)],
                'prediction': GAEL_MONFILS,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    ANDREY_RUBLEV,
                    YUICHI_SUGITA,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.15,
                    YUICHI_SUGITA: 5.50,
                },
                'score': [(6, 2), (6, 3), (7, 6)],
            },
            {
                'round': 64,
                'players': [
                    ALEXANDER_ZVEREV,
                    EGOR_GERASIMOV,
                ],
                'odds': {
                    ALEXANDER_ZVEREV: 1.18,
                    EGOR_GERASIMOV: 5.00,
                },
                'score': [(7, 6), (6, 4), (7, 5)],
            },
            {
                'round': 64,
                'players': [
                    TAYLOR_FRITZ,
                    KEVIN_ANDERSON,
                ],
                'odds': {
                    TAYLOR_FRITZ: 1.95,
                    KEVIN_ANDERSON: 1.85,
                },
                'score': [(4, 6), (6, 7), (7, 6), (6, 2), (6, 2)],
            },
            {
                'round': 64,
                'players': [
                    DOMINIC_THIEM,
                    ALEX_BOLT,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.08,
                    ALEX_BOLT: 8.00,
                },
                'score': [(6, 2), (5, 7), (6, 7), (6, 1), (6, 2)],
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    PIERRE_HUGUES_HERBERT,
                ],
                'odds': {
                    DAVID_GOFFIN: 1.13,
                    PIERRE_HUGUES_HERBERT: 6.00,
                },
                'score': [(6, 1), (6, 4), (4, 6), (1, 6), (6, 3)],
                'prediction': DAVID_GOFFIN,
                'bet': 7,
            },
            {
                'round': 64,
                'players': [
                    ALEXEI_POPYRIN,
                    JAUME_MUNAR,
                ],
                'odds': {
                    ALEXEI_POPYRIN: 1.40,
                    JAUME_MUNAR: 3.00,
                },
                'score': [(6, 2), (7, 6), (6, 2)],
                'prediction': ALEXEI_POPYRIN,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    PETER_GOJOWCZYK,
                ],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.20,
                    PETER_GOJOWCZYK: 4.60,
                },
                'score': [(6, 4), (6, 1), (1, 6), (6, 4)],
            },
            {
                'round': 64,
                'players': [
                    JOHN_ISNER,
                    ALEJANDRO_TABILO,
                ],
                'odds': {
                    JOHN_ISNER: 1.11,
                    ALEJANDRO_TABILO: 6.50,
                },
                'score': [(6, 4), (6, 3), (6, 3)],
                'prediction': JOHN_ISNER,
                'bet': 8,
            },
            {
                'round': 64,
                'players': [
                    KAREN_KHACHANOV,
                    MIKAEL_YMER,
                ],
                'odds': {
                    KAREN_KHACHANOV: 1.34,
                    MIKAEL_YMER: 3.30,
                },
                'score': [(6, 2), (2, 6), (6, 4), (3, 6), (7, 6)],
                'prediction': KAREN_KHACHANOV,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    NICK_KYRGIOS,
                    GILLES_SIMON,
                ],
                'odds': {
                    NICK_KYRGIOS: 1.18,
                    GILLES_SIMON: 5.00,
                },
                'score': [(6, 2), (6, 4), (4, 6), (7, 5)],
                'prediction': NICK_KYRGIOS,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    STAN_WAWRINKA,
                    ANDREAS_SEPPI,
                ],
                'odds': {
                    STAN_WAWRINKA: 1.23,
                    ANDREAS_SEPPI: 4.20,
                },
                'score': [(4, 6), (7, 5), (6, 3), (3, 6), (6, 4)],
            },
            {
                'round': 64,
                'players': [
                    RAFAEL_NADAL,
                    FEDERICO_DELBONIS,
                ],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    FEDERICO_DELBONIS: 21.00,
                },
                'score': [(6, 3), (7, 6), (6, 1)],
                'prediction': RAFAEL_NADAL,
                'bet': 4,
            },

            # 2020-01-24
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    DUSAN_LAJOVIC,
                ],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.40,
                    DUSAN_LAJOVIC: 3.00,
                },
                'score': [(6, 2), (6, 3), (7, 6)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    TOMMY_PAUL,
                ],
                'odds': {
                    MARTON_FUCSOVICS: 1.70,
                    TOMMY_PAUL: 2.15,
                },
                'score': [(6, 1), (6, 1), (6, 4)],
                'prediction': MARTON_FUCSOVICS,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    YOSHIHITO_NISHIOKA,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    YOSHIHITO_NISHIOKA: 21.00,
                },
                'score': [(6, 3), (6, 2), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    TENNYS_SANDGREN,
                    SAM_QUERREY,
                ],
                'odds': {
                    TENNYS_SANDGREN: 2.15,
                    SAM_QUERREY: 1.70,
                },
                'score': [(6, 4), (6, 4), (6, 4)],
            },

            # 2020-01-25
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    ERNESTS_GULBIS,
                ],
                'odds': {
                    GAEL_MONFILS: 1.53,
                    ERNESTS_GULBIS: 2.50,
                },
                'score': [(7, 6), (6, 4), (6, 3)],
                'prediction': GAEL_MONFILS,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    TAYLOR_FRITZ,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.37,
                    TAYLOR_FRITZ: 3.10,
                },
                'score': [(6, 2), (6, 4), (6, 7), (6, 4)],
                'prediction': DOMINIC_THIEM,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    DAVID_GOFFIN,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.53,
                    DAVID_GOFFIN: 2.50,
                },
                'score': [(2, 6), (7, 6), (6, 4), (7, 6)],
                'prediction': ANDREY_RUBLEV,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    PABLO_CARRENO_BUSTA,
                ],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    PABLO_CARRENO_BUSTA: 21.00,
                },
                'score': [(6, 1), (6, 2), (6, 4)],
                'prediction': RAFAEL_NADAL,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    JOHN_ISNER,
                ],
                'odds': {
                    STAN_WAWRINKA: 1.75,
                    JOHN_ISNER: 2.10,
                },
                'score': [(6, 4), (4, 1)],
                'retired': True,
            },
            {
                'round': 32,
                'players': [
                    NICK_KYRGIOS,
                    KAREN_KHACHANOV,
                ],
                'odds': {
                    NICK_KYRGIOS: 1.40,
                    KAREN_KHACHANOV: 3.00,
                },
                'score': [(6, 2), (7, 6), (6, 7), (6, 7), (7, 6)],
                'prediction': NICK_KYRGIOS,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    FERNANDO_VERDASCO,
                ],
                'odds': {
                    ALEXANDER_ZVEREV: 1.42,
                    FERNANDO_VERDASCO: 2.90,
                },
                'score': [(6, 2), (6, 2), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    DANIIL_MEDVEDEV,
                    ALEXEI_POPYRIN,
                ],
                'odds': {
                    DANIIL_MEDVEDEV: 1.13,
                    ALEXEI_POPYRIN: 6.00,
                },
                'score': [(6, 4), (6, 3), (6, 2)],
                'prediction': DANIIL_MEDVEDEV,
                'bet': 8,
            },

            # 2020-01-26
            {
                'round': 16,
                'players': [
                    MILOS_RAONIC,
                    MARIN_CILIC,
                ],
                'odds': {
                    MILOS_RAONIC: 1.53,
                    MARIN_CILIC: 2.50,
                },
                'score': [(6, 4), (6, 3), (7, 5)],
                'prediction': MILOS_RAONIC,
                'bet': 6,
            },
            {
                'round': 16,
                'players': [
                    NOVAK_DJOKOVIC,
                    DIEGO_SCHWARTZMAN,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.03,
                    DIEGO_SCHWARTZMAN: 13.00,
                },
                'score': [(6, 3), (6, 4), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    TENNYS_SANDGREN,
                    FABIO_FOGNINI,
                ],
                'odds': {
                    TENNYS_SANDGREN: 2.35,
                    FABIO_FOGNINI: 1.60,
                },
                'score': [(7, 6), (7, 5), (6, 7), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    MARTON_FUCSOVICS,
                ],
                'odds': {
                    ROGER_FEDERER: 1.13,
                    MARTON_FUCSOVICS: 6.00,
                },
                'score': [(4, 6), (6, 1), (6, 2), (6, 2)],
            },

            # 2020-01-27
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    GAEL_MONFILS,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.32,
                    GAEL_MONFILS: 3.40,
                },
                'score': [(6, 2), (6, 4), (6, 4)],
                'prediction': DOMINIC_THIEM,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    DANIIL_MEDVEDEV,
                ],
                'odds': {
                    STAN_WAWRINKA: 4.20,
                    DANIIL_MEDVEDEV: 1.23,
                },
                'score': [(6, 2), (2, 6), (4, 6), (7, 6), (6, 2)],
                'prediction': DANIIL_MEDVEDEV,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    RAFAEL_NADAL,
                    NICK_KYRGIOS,
                ],
                'odds': {
                    RAFAEL_NADAL: 1.20,
                    NICK_KYRGIOS: 4.60,
                },
                'score': [(6, 3), (3, 6), (7, 6), (7, 6)],
                'prediction': RAFAEL_NADAL,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    ANDREY_RUBLEV,
                ],
                'odds': {
                    ALEXANDER_ZVEREV: 1.90,
                    ANDREY_RUBLEV: 1.90,
                },
                'score': [(6, 4), (6, 4), (6, 4)],
            },

            # 2020-01-28
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    TENNYS_SANDGREN,
                ],
                'odds': {
                    ROGER_FEDERER: 1.10,
                    TENNYS_SANDGREN: 7.00,
                },
                'score': [(6, 3), (2, 6), (2, 6), (7, 6), (6, 3)],
            },
            {
                'round': 8,
                'players': [
                    NOVAK_DJOKOVIC,
                    MILOS_RAONIC,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.11,
                    MILOS_RAONIC: 6.50,
                },
                'score': [(6, 4), (6, 3), (7, 6)],
            },

            # 2020-01-29
            {
                'round': 8,
                'players': [
                    ALEXANDER_ZVEREV,
                    STAN_WAWRINKA,
                ],
                'odds': {
                    ALEXANDER_ZVEREV: 1.68,
                    STAN_WAWRINKA: 2.20,
                },
                'score': [(1, 6), (6, 3), (6, 4), (6, 2)],
                'prediction': ALEXANDER_ZVEREV,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    RAFAEL_NADAL,
                ],
                'odds': {
                    DOMINIC_THIEM: 3.30,
                    RAFAEL_NADAL: 1.34,
                },
                'score': [(7, 6), (7, 6), (4, 6), (7, 6)],
                'prediction': RAFAEL_NADAL,
                'bet': 5,
            },

            # 2020-01-30
            {
                'round': 4,
                'players': [
                    NOVAK_DJOKOVIC,
                    ROGER_FEDERER,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.13,
                    ROGER_FEDERER: 6.00,
                },
                'score': [(7, 6), (6, 4), (6, 3)],
                'prediction': NOVAK_DJOKOVIC,
                'bet': 1,
            },

            # 2020-01-31
            {
                'round': 4,
                'players': [
                    DOMINIC_THIEM,
                    ALEXANDER_ZVEREV,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.44,
                    ALEXANDER_ZVEREV: 2.80,
                },
                'score': [(3, 6), (6, 4), (7, 6), (7, 6)],
            },

            # 2020-02-01
            {
                'round': 2,
                'players': [
                    NOVAK_DJOKOVIC,
                    DOMINIC_THIEM,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.25,
                    DOMINIC_THIEM: 4.00,
                },
                'score': [(6, 4), (4, 6), (2, 6), (6, 3), (6, 4)],
            },
        ]
    },

    {
        'location': PUNE,
        'date': '2020-02-09',
        'matches': [

            # 2020-02-03
            {
                'round': 32,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    IVO_KARLOVIC,
                ],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 2.10,
                    IVO_KARLOVIC: 1.70,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': IVO_KARLOVIC,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    YUICHI_SUGITA,
                    THOMAS_FABBIANO,
                ],
                'odds': {
                    YUICHI_SUGITA: 1.32,
                    THOMAS_FABBIANO: 3.30,
                },
                'score': [(6, 3), (6, 0)],
                'prediction': YUICHI_SUGITA,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    VIKTOR_TROICKI,
                    SUMIT_NAGAL,
                ],
                'odds': {
                    VIKTOR_TROICKI: 1.45,
                    SUMIT_NAGAL: 2.70,
                },
                'score': [(6, 2), (6, 7), (6, 1)],
                'prediction': VIKTOR_TROICKI,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    SALVATORE_CARUSO,
                    RAMKUMAR_RAMANATHAN,
                ],
                'odds': {
                    SALVATORE_CARUSO: 1.85,
                    RAMKUMAR_RAMANATHAN: 1.95,
                },
                'score': [(3, 6), (6, 4), (7, 5)],
                'prediction': SALVATORE_CARUSO,
                'bet': 8,
            },

            # 2020-02-04
            {
                'round': 32,
                'players': [
                    JAMES_DUCKWORTH,
                    PETER_GOJOWCZYK,
                ],
                'odds': {
                    JAMES_DUCKWORTH: 1.95,
                    PETER_GOJOWCZYK: 1.85,
                },
                'score': [(7, 6), (5, 4)],
                'prediction': PETER_GOJOWCZYK,
                'bet': 12,
            },
            {
                'round': 32,
                'players': [
                    EGOR_GERASIMOV,
                    PAOLO_LORENZI,
                ],
                'odds': {
                    EGOR_GERASIMOV: 1.32,
                    PAOLO_LORENZI: 3.30,
                },
                'score': [(6, 2), (6, 3)],
                'prediction': EGOR_GERASIMOV,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_MARCORA,
                    LUKAS_ROSOL,
                ],
                'odds': {
                    ROBERTO_MARCORA: 2.60,
                    LUKAS_ROSOL: 1.48,
                },
                'score': [(6, 3), (6, 2)],
                'prediction': LUKAS_ROSOL,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    ILYA_IVASHKA,
                    EVGENY_DONSKOY,
                ],
                'odds': {
                    ILYA_IVASHKA: 1.55,
                    EVGENY_DONSKOY: 2.40,
                },
                'score': [(6, 3), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    JIRI_VESELY,
                    ARJUN_KADHE,
                ],
                'odds': {
                    JIRI_VESELY: 1.08,
                    ARJUN_KADHE: 7.50,
                },
                'score': [(6, 2), (6, 4)],
                'prediction': JIRI_VESELY,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    NIKOLA_MILOJEVIC,
                    ANTOINE_HOANG,
                ],
                'odds': {
                    NIKOLA_MILOJEVIC: 1.58,
                    ANTOINE_HOANG: 2.35,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': NIKOLA_MILOJEVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    YANNICK_MADEN,
                ],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 1.60,
                    YANNICK_MADEN: 2.30,
                },
                'score': [(7, 6), (7, 6)],
            },

            # 2020-02-05
            {
                'round': 16,
                'players': [
                    JIRI_VESELY,
                    SALVATORE_CARUSO,
                ],
                'odds': {
                    JIRI_VESELY: 1.75,
                    SALVATORE_CARUSO: 2.05,
                },
                'score': [(7, 6), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    RICARDAS_BERANKIS,
                    CEDRIC_MARCEL_STEBE,
                ],
                'odds': {
                    RICARDAS_BERANKIS: 1.80,
                    CEDRIC_MARCEL_STEBE: 2.00,
                },
                'score': [(7, 6), (6, 1)],
            },
            {
                'round': 32,
                'players': [
                    TARO_DANIEL,
                    SASI_KUMAR_MUKUND,
                ],
                'odds': {
                    TARO_DANIEL: 1.32,
                    SASI_KUMAR_MUKUND: 3.30,
                },
                'score': [(6, 2), (7, 6)],
                'prediction': TARO_DANIEL,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    YUICHI_SUGITA,
                    VIKTOR_TROICKI,
                ],
                'odds': {
                    YUICHI_SUGITA: 1.60,
                    VIKTOR_TROICKI: 2.30,
                },
                'score': [],
                'retired': True,
            },
            {
                'round': 16,
                'players': [
                    ILYA_IVASHKA,
                    STEFANO_TRAVAGLIA,
                ],
                'odds': {
                    ILYA_IVASHKA: 1.68,
                    STEFANO_TRAVAGLIA: 2.15,
                },
                'score': [(7, 6), (7, 6)],
                'prediction': ILYA_IVASHKA,
                'bet': 6,
            },

            # 2020-02-06
            {
                'round': 16,
                'players': [
                    JAMES_DUCKWORTH,
                    TARO_DANIEL,
                ],
                'odds': {
                    JAMES_DUCKWORTH: 1.58,
                    TARO_DANIEL: 2.35,
                },
                'score': [(6, 7), (7, 6), (6, 3)],
            },
            {
                'round': 16,
                'players': [
                    SOONWOO_KWON,
                    PRAJNESH_GUNNESWARAN,
                ],
                'odds': {
                    SOONWOO_KWON: 1.70,
                    PRAJNESH_GUNNESWARAN: 2.10,
                },
                'score': [(6, 3), (7, 6)],
                'prediction': SOONWOO_KWON,
                'bet': 9,
            },
            {
                'round': 16,
                'players': [
                    EGOR_GERASIMOV,
                    NIKOLA_MILOJEVIC,
                ],
                'odds': {
                    EGOR_GERASIMOV: 1.52,
                    NIKOLA_MILOJEVIC: 2.50,
                },
                'score': [(2, 6), (6, 3), (6, 2)],
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_MARCORA,
                    BENOIT_PAIRE,
                ],
                'odds': {
                    ROBERTO_MARCORA: 3.00,
                    BENOIT_PAIRE: 1.38,
                },
                'score': [(6, 4), (6, 4)],
                'prediction': BENOIT_PAIRE,
                'bet': 5,
            },

            # 2020-02-07
            {
                'round': 8,
                'players': [
                    JIRI_VESELY,
                    ILYA_IVASHKA,
                ],
                'odds': {
                    JIRI_VESELY: 2.10,
                    ILYA_IVASHKA: 1.70,
                },
                'score': [(2, 6), (6, 1), (7, 6)],
                'prediction': ILYA_IVASHKA,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    RICARDAS_BERANKIS,
                    YUICHI_SUGITA,
                ],
                'odds': {
                    RICARDAS_BERANKIS: 1.85,
                    YUICHI_SUGITA: 1.95,
                },
                'score': [(4, 6), (7, 6), (6, 2)],
            },
            {
                'round': 8,
                'players': [
                    JAMES_DUCKWORTH,
                    ROBERTO_MARCORA,
                ],
                'odds': {
                    JAMES_DUCKWORTH: 1.48,
                    ROBERTO_MARCORA: 2.60,
                },
                'score': [(6, 3), (7, 6)],
            },
            {
                'round': 8,
                'players': [
                    EGOR_GERASIMOV,
                    SOONWOO_KWON,
                ],
                'odds': {
                    EGOR_GERASIMOV: 1.80,
                    SOONWOO_KWON: 2.00,
                },
                'score': [(4, 6), (7, 6), (6, 4)],
            },

            # 2020-02-08
            {
                'round': 4,
                'players': [
                    JIRI_VESELY,
                    RICARDAS_BERANKIS,
                ],
                'odds': {
                    JIRI_VESELY: 2.00,
                    RICARDAS_BERANKIS: 1.80,
                },
                'score': [(6, 7), (7, 6), (7, 6)],
                'prediction': RICARDAS_BERANKIS,
                'bet': 1,
            },
            {
                'round': 4,
                'players': [
                    EGOR_GERASIMOV,
                    JAMES_DUCKWORTH,
                ],
                'odds': {
                    EGOR_GERASIMOV: 1.70,
                    JAMES_DUCKWORTH: 2.10,
                },
                'score': [(7, 6), (6, 4)],
            },

            # 2020-02-09
            {
                'round': 2,
                'players': [
                    JIRI_VESELY,
                    EGOR_GERASIMOV,
                ],
                'odds': {
                    JIRI_VESELY: 2.40,
                    EGOR_GERASIMOV: 1.55,
                },
                'score': [(7, 6), (5, 7), (6, 3)],
            }
        ]
    },

    {
        'location': MONTPELLIER,
        'date': '2020-02-09',
        'matches': [

            # 2020-02-03
            {
                'round': 32,
                'players': [
                    ENZO_COUACAUD,
                    GUILLERMO_GARCIA_LOPEZ,
                ],
                'odds': {
                    ENZO_COUACAUD: 1.68,
                    GUILLERMO_GARCIA_LOPEZ: 2.15,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': ENZO_COUACAUD,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    EMIL_RUUSUVUORI,
                    NICOLAS_MAHUT,
                ],
                'odds': {
                    EMIL_RUUSUVUORI: 1.28,
                    NICOLAS_MAHUT: 3.60,
                },
                'score': [(6, 3), (3, 6), (7, 6)],
                'prediction': EMIL_RUUSUVUORI,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    DAMIR_DZUMHUR,
                    ELLIOT_BENCHETRIT,
                ],
                'odds': {
                    DAMIR_DZUMHUR: 1.26,
                    ELLIOT_BENCHETRIT: 3.80,
                },
                'score': [(6, 2), (6, 4)],
                'prediction': DAMIR_DZUMHUR,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    SERGIY_STAKHOVSKY,
                    DANILO_PETROVIC,
                ],
                'odds': {
                    SERGIY_STAKHOVSKY: 1.95,
                    DANILO_PETROVIC: 1.85,
                },
                'score': [(6, 2), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    VASEK_POSPISIL,
                    ALJAZ_BEDENE,
                ],
                'odds': {
                    VASEK_POSPISIL: 1.80,
                    ALJAZ_BEDENE: 2.00,
                },
                'score': [(6, 3), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    GREGOIRE_BARRERE,
                    JOAO_SOUSA,
                ],
                'odds': {
                    GREGOIRE_BARRERE: 1.58,
                    JOAO_SOUSA: 2.35,
                },
                'score': [(6, 2), (7, 6)],
                'prediction': GREGOIRE_BARRERE,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    NORBERT_GOMBOS,
                    PABLO_CARRENO_BUSTA,
                ],
                'odds': {
                    NORBERT_GOMBOS: 3.10,
                    PABLO_CARRENO_BUSTA: 1.36,
                },
                'score': [(3, 6), (6, 4), (6, 3)],
            },

            # 2020-02-04
            {
                'round': 32,
                'players': [
                    ALEXANDER_BUBLIK,
                    HENRI_LAAKSONEN,
                ],
                'odds': {
                    ALEXANDER_BUBLIK: 1.36,
                    HENRI_LAAKSONEN: 3.10,
                },
                'score': [(6, 7), (6, 1), (7, 6)],
                'prediction': ALEXANDER_BUBLIK,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    EMIL_RUUSUVUORI,
                    DENNIS_NOVAK,
                ],
                'odds': {
                    EMIL_RUUSUVUORI: 1.68,
                    DENNIS_NOVAK: 2.15,
                },
                'score': [(7, 6), (4, 6), (6, 2)],
                'prediction': EMIL_RUUSUVUORI,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    MIKAEL_YMER,
                    JANNIK_SINNER,
                ],
                'odds': {
                    MIKAEL_YMER: 2.15,
                    JANNIK_SINNER: 1.68,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': JANNIK_SINNER,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    ENZO_COUACAUD,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 1.24,
                    ENZO_COUACAUD: 4.00,
                },
                'score': [(6, 4), (6, 4)],
                'prediction': FILIP_KRAJINOVIC,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    SERGIY_STAKHOVSKY,
                ],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.28,
                    SERGIY_STAKHOVSKY: 3.60,
                },
                'score': [(6, 2), (7, 5)],
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    DAMIR_DZUMHUR,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.55,
                    DAMIR_DZUMHUR: 2.40,
                },
                'score': [(6, 7), (6, 2), (6, 2)],
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 7,
            },

            # 2020-02-05
            {
                'round': 32,
                'players': [
                    ADRIAN_MANNARINO,
                    ALEXEI_POPYRIN,
                ],
                'odds': {
                    ADRIAN_MANNARINO: 1.80,
                    ALEXEI_POPYRIN: 2.00,
                },
                'score': [(6, 0), (6, 7), (6, 0)],
                'prediction': ADRIAN_MANNARINO,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    FELICIANO_LOPEZ,
                    UGO_HUMBERT,
                ],
                'odds': {
                    FELICIANO_LOPEZ: 3.20,
                    UGO_HUMBERT: 1.34,
                },
                'score': [(6, 4), (6, 1)],
                'prediction': UGO_HUMBERT,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    RICHARD_GASQUET,
                    GILLES_SIMON,
                ],
                'odds': {
                    RICHARD_GASQUET: 2.90,
                    GILLES_SIMON: 1.40,
                },
                'score': [(6, 4), (6, 4)],
                'prediction': GILLES_SIMON,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    GREGOIRE_BARRERE,
                    GRIGOR_DIMITROV,
                ],
                'odds': {
                    GREGOIRE_BARRERE: 3.60,
                    GRIGOR_DIMITROV: 1.28,
                },
                'score': [(6, 7), (6, 4), (7, 5)],
                'prediction': GRIGOR_DIMITROV,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    VASEK_POSPISIL,
                    DENIS_SHAPOVALOV,
                ],
                'odds': {
                    VASEK_POSPISIL: 2.80,
                    DENIS_SHAPOVALOV: 1.42,
                },
                'score': [(6, 2), (6, 3)],
            },

            # 2020-02-06
            {
                'round': 16,
                'players': [
                    FILIP_KRAJINOVIC,
                    MIKAEL_YMER,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 1.65,
                    MIKAEL_YMER: 2.20,
                },
                'score': [(6, 1), (6, 1)],
            },
            {
                'round': 16,
                'players': [
                    DAVID_GOFFIN,
                    ALEXANDER_BUBLIK,
                ],
                'odds': {
                    DAVID_GOFFIN: 1.26,
                    ALEXANDER_BUBLIK: 3.80,
                },
                'score': [(6, 3), (7, 6)],
            },
            {
                'round': 16,
                'players': [
                    RICHARD_GASQUET,
                    FELICIANO_LOPEZ,
                ],
                'odds': {
                    RICHARD_GASQUET: 1.95,
                    FELICIANO_LOPEZ: 1.85,
                },
                'score': [(6, 7), (6, 4), (6, 3)],
                'prediction': FELICIANO_LOPEZ,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    NORBERT_GOMBOS,
                    EMIL_RUUSUVUORI,
                ],
                'odds': {
                    NORBERT_GOMBOS: 2.40,
                    EMIL_RUUSUVUORI: 1.55,
                },
                'score': [(7, 5), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    FELIX_AUGER_ALIASSIME,
                ],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 2.20,
                    FELIX_AUGER_ALIASSIME: 1.65,
                },
                'score': [(7, 6), (7, 5)],
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 6,
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    ADRIAN_MANNARINO,
                ],
                'odds': {
                    GAEL_MONFILS: 1.48,
                    ADRIAN_MANNARINO: 2.60,
                },
                'score': [(4, 6), (6, 1), (6, 4)],
                'prediction': GAEL_MONFILS,
                'bet': 1,
            },

            # 2020-02-07
            {
                'round': 8,
                'players': [
                    FILIP_KRAJINOVIC,
                    GREGOIRE_BARRERE,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 1.48,
                    GREGOIRE_BARRERE: 2.60,
                },
                'score': [(6, 2), (7, 5)],
            },
            {
                'round': 8,
                'players': [
                    VASEK_POSPISIL,
                    RICHARD_GASQUET,
                ],
                'odds': {
                    VASEK_POSPISIL: 1.45,
                    RICHARD_GASQUET: 2.70,
                },
                'score': [(6, 1), (1, 0)],
                'retired': True,
                'prediction': VASEK_POSPISIL,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    GAEL_MONFILS,
                    NORBERT_GOMBOS,
                ],
                'odds': {
                    GAEL_MONFILS: 1.30,
                    NORBERT_GOMBOS: 3.40,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': GAEL_MONFILS,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    DAVID_GOFFIN,
                    PIERRE_HUGUES_HERBERT,
                ],
                'odds': {
                    DAVID_GOFFIN: 1.48,
                    PIERRE_HUGUES_HERBERT: 2.60,
                },
                'score': [(6, 4), (7, 6)],
            },

            # 2020-02-08
            {
                'round': 4,
                'players': [
                    GAEL_MONFILS,
                    FILIP_KRAJINOVIC,
                ],
                'odds': {
                    GAEL_MONFILS: 1.65,
                    FILIP_KRAJINOVIC: 2.20,
                },
                'score': [(7, 6), (6, 2)],
                'prediction': GAEL_MONFILS,
                'bet': 5,
            },
            {
                'round': 4,
                'players': [
                    VASEK_POSPISIL,
                    DAVID_GOFFIN,
                ],
                'odds': {
                    VASEK_POSPISIL: 2.50,
                    DAVID_GOFFIN: 1.52,
                },
                'score': [(6, 3), (1, 6), (7, 5)],
            },

            # 2020-02-09
            {
                'round': 2,
                'players': [
                    GAEL_MONFILS,
                    VASEK_POSPISIL,
                ],
                'odds': {
                    GAEL_MONFILS: 1.42,
                    VASEK_POSPISIL: 2.80,
                },
                'score': [(7, 5), (6, 3)],
                'prediction': GAEL_MONFILS,
                'bet': 5,
            }
        ]
    },

    {
        'location': CORDOBA,
        'date': '2020-02-09',
        'matches': [

            # 2020-02-03
            {
                'round': 32,
                'players': [
                    ATTILA_BALAZS,
                    LORENZO_SONEGO,
                ],
                'odds': {
                    ATTILA_BALAZS: 2.25,
                    LORENZO_SONEGO: 1.62,
                },
                'score': [(6, 2), (7, 6)],
                'prediction': LORENZO_SONEGO,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    GIANLUCA_MAGER,
                    JUAN_PABLO_FICOVICH,
                ],
                'odds': {
                    GIANLUCA_MAGER: 1.80,
                    JUAN_PABLO_FICOVICH: 2.00,
                },
                'score': [(6, 2), (3, 6), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    PABLO_CUEVAS,
                    FEDERICO_DELBONIS,
                ],
                'odds': {
                    PABLO_CUEVAS: 2.05,
                    FEDERICO_DELBONIS: 1.75,
                },
                'score': [(7, 5), (6, 2)],
                'prediction': FEDERICO_DELBONIS,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    CARLOS_TABERNER,
                    FERNANDO_VERDASCO,
                ],
                'odds': {
                    CARLOS_TABERNER: 2.90,
                    FERNANDO_VERDASCO: 1.40,
                },
                'score': [(4, 6), (6, 1), (6, 4)],
                'prediction': FERNANDO_VERDASCO,
                'bet': 6,
            },

            # 2020-02-04
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    PEDRO_MARTINEZ,
                ],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.58,
                    PEDRO_MARTINEZ: 2.35,
                },
                'score': [],
                'retired': True,
                'prediction': ROBERTO_CARBALLES_BAENA,
                'bet': 0,  # refunded 9
            },
            {
                'round': 32,
                'players': [
                    ANDREJ_MARTIN,
                    FEDERICO_CORIA,
                ],
                'odds': {
                    ANDREJ_MARTIN: 1.85,
                    FEDERICO_CORIA: 1.95,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': ANDREJ_MARTIN,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    FACUNDO_BAGNIS,
                ],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.34,
                    FACUNDO_BAGNIS: 3.20,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': ALBERT_RAMOS_VINOLAS,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    CORENTIN_MOUTET,
                    THIAGO_MONTEIRO,
                ],
                'odds': {
                    CORENTIN_MOUTET: 1.62,
                    THIAGO_MONTEIRO: 2.25,
                },
                'score': [(6, 4), (6, 3)],
                'prediction': CORENTIN_MOUTET,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    PEDRO_CACHIN,
                    HUGO_DELLIEN,
                ],
                'odds': {
                    PEDRO_CACHIN: 3.40,
                    HUGO_DELLIEN: 1.30,
                },
                'score': [(6, 1), (6, 1)],
                'prediction': HUGO_DELLIEN,
                'bet': 8,
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    MARCO_CECCHINATO,
                ],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.55,
                    MARCO_CECCHINATO: 2.40,
                },
                'score': [(6, 2), (7, 5)],
                'prediction': JUAN_IGNACIO_LONDERO,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    LEONARDO_MAYER,
                ],
                'odds': {
                    JAUME_MUNAR: 1.70,
                    LEONARDO_MAYER: 2.10,
                },
                'score': [(6, 4), (6, 3)],
            },

            # 2020-02-05
            {
                'round': 16,
                'players': [
                    ANDREJ_MARTIN,
                    CARLOS_TABERNER,
                ],
                'odds': {
                    ANDREJ_MARTIN: 1.95,
                    CARLOS_TABERNER: 1.85,
                },
                'score': [(6, 3), (7, 6)],
                'prediction': CARLOS_TABERNER,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    PABLO_CUEVAS,
                    GIANLUCA_MAGER,
                ],
                'odds': {
                    PABLO_CUEVAS: 1.28,
                    GIANLUCA_MAGER: 3.60,
                },
                'score': [(6, 7), (7, 6), (6, 1)],
                'prediction': PABLO_CUEVAS,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    CORENTIN_MOUTET,
                    GUIDO_PELLA,
                ],
                'odds': {
                    CORENTIN_MOUTET: 2.25,
                    GUIDO_PELLA: 1.62,
                },
                'score': [(6, 7), (7, 5), (6, 3)],
            },
            {
                'round': 16,
                'players': [
                    CHRISTIAN_GARIN,
                    ATTILA_BALAZS,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.42,
                    ATTILA_BALAZS: 2.80,
                },
                'score': [(6, 3), (6, 0)],
                'prediction': CHRISTIAN_GARIN,
                'bet': 1,
            },

            # 2020-02-06
            {
                'round': 16,
                'players': [
                    LASLO_DJERE,
                    PEDRO_MARTINEZ
                ],
                'odds': {
                    LASLO_DJERE: 1.52,
                    PEDRO_MARTINEZ: 2.50,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': LASLO_DJERE,
                'bet': 6,
            },
            {
                'round': 16,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    PABLO_ANDUJAR,
                ],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.75,
                    PABLO_ANDUJAR: 2.05,
                },
                'score': [(6, 3), (6, 7), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    PEDRO_CACHIN,
                ],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.24,
                    PEDRO_CACHIN: 4.00,
                },
                'score': [(6, 3), (6, 3)],
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    JAUME_MUNAR,
                ],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.24,
                    JAUME_MUNAR: 4.00,
                },
                'score': [(6, 1), (7, 5)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 4,
            },

            # 2020-02-07
            {
                'round': 8,
                'players': [
                    ANDREJ_MARTIN,
                    CORENTIN_MOUTET,
                ],
                'odds': {
                    ANDREJ_MARTIN: 2.60,
                    CORENTIN_MOUTET: 1.48,
                },
                'score': [(6, 3), (6, 2)],
            },
            {
                'round': 8,
                'players': [
                    CHRISTIAN_GARIN,
                    PABLO_CUEVAS,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.48,
                    PABLO_CUEVAS: 2.60,
                },
                'score': [(1, 6), (6, 3), (6, 4)],
            },

            # 2020-02-08
            {
                'round': 4,
                'players': [
                    CHRISTIAN_GARIN,
                    ANDREJ_MARTIN,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.42,
                    ANDREJ_MARTIN: 2.80,
                },
                'score': [(2, 6), (6, 2), (6, 2)],
                'prediction': CHRISTIAN_GARIN,
                'bet': 5,
            },
            {
                'round': 4,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    LASLO_DJERE,
                ],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.24,
                    LASLO_DJERE: 4.00,
                },
                'score': [(6, 1), (1, 6), (6, 2)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 3,
            },

            # 2020-02-09
            {
                'round': 2,
                'players': [
                    CHRISTIAN_GARIN,
                    DIEGO_SCHWARTZMAN,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 3.20,
                    DIEGO_SCHWARTZMAN: 1.34,
                },
                'score': [(2, 6), (6, 4), (6, 0)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 1,
            }
        ]
    },

    {
        'location': ROTTERDAM,
        'date': '2020-02-16',
        'matches': [

            # 2020-02-10
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    ADRIAN_MANNARINO,
                ],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.80,
                    ADRIAN_MANNARINO: 2.00,
                },
                'score': [(7, 5), (6, 7), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    MARTON_FUCSOVICS,
                ],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.40,
                    MARTON_FUCSOVICS: 2.90,
                },
                'score': [(4, 6), (7, 6), (6, 1)],
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    GRIGOR_DIMITROV,
                    DENIS_SHAPOVALOV,
                ],
                'odds': {
                    GRIGOR_DIMITROV: 1.95,
                    DENIS_SHAPOVALOV: 1.85,
                },
                'score': [(6, 3), (7, 6)],
                'prediction': DENIS_SHAPOVALOV,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    DANIEL_EVANS,
                    PHILIPP_KOHLSCHREIBER,
                ],
                'odds': {
                    DANIEL_EVANS: 2.00,
                    PHILIPP_KOHLSCHREIBER: 1.80,
                },
                'score': [(6, 3), (7, 5)],
            },

            # 2020-02-11
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    JAN_LENNARD_STRUFF,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.15,
                    JAN_LENNARD_STRUFF: 1.68,
                },
                'score': [(6, 3), (1, 6), (6, 3)],
                'prediction': JAN_LENNARD_STRUFF,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_BUBLIK,
                    GREGOIRE_BARRERE,
                ],
                'odds': {
                    ALEXANDER_BUBLIK: 2.10,
                    GREGOIRE_BARRERE: 1.70,
                },
                'score': [(6, 3), (6, 7), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    FABIO_FOGNINI,
                ],
                'odds': {
                    KAREN_KHACHANOV: 1.45,
                    FABIO_FOGNINI: 2.70,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': KAREN_KHACHANOV,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    NIKOLOZ_BASILASHVILI,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.26,
                    NIKOLOZ_BASILASHVILI: 3.80,
                },
                'score': [(6, 2), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    BENOIT_PAIRE,
                ],
                'odds': {
                    ALJAZ_BEDENE: 1.85,
                    BENOIT_PAIRE: 1.95,
                },
                'score': [(6, 2), (6, 4)],
                'prediction': ALJAZ_BEDENE,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    HUBERT_HURKACZ,
                ],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.30,
                    HUBERT_HURKACZ: 3.40,
                },
                'score': [(6, 7), (6, 3), (6, 1)],
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    TALLON_GRIEKSPOOR,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 1.22,
                    TALLON_GRIEKSPOOR: 4.20,
                },
                'score': [(6, 4), (6, 1)],
                'prediction': FILIP_KRAJINOVIC,
                'bet': 2,
            },

            # 2020-02-12
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    MIKHAIL_KUKUSHKIN,
                ],
                'odds': {
                    GILLES_SIMON: 2.05,
                    MIKHAIL_KUKUSHKIN: 1.75,
                },
                'score': [(7, 6), (3, 6), (6, 3)],
                'prediction': MIKHAIL_KUKUSHKIN,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    JANNIK_SINNER,
                    RADU_ALBOT,
                ],
                'odds': {
                    JANNIK_SINNER: 1.34,
                    RADU_ALBOT: 3.20,
                },
                'score': [],
                'retired': True,
                'prediction': JANNIK_SINNER,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    ROBIN_HAASE,
                ],
                'odds': {
                    DAVID_GOFFIN: 1.12,
                    ROBIN_HAASE: 6.00,
                },
                'score': [(3, 6), (7, 6), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    PABLO_CARRENO_BUSTA,
                ],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.34,
                    PABLO_CARRENO_BUSTA: 3.20,
                },
                'score': [(4, 6), (7, 6), (6, 1)],
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    JOAO_SOUSA,
                ],
                'odds': {
                    GAEL_MONFILS: 1.18,
                    JOAO_SOUSA: 4.60,
                },
                'score': [(6, 3), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    DANIEL_EVANS,
                ],
                'odds': {
                    KAREN_KHACHANOV: 1.60,
                    DANIEL_EVANS: 2.30,
                },
                'score': [(6, 3), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    VASEK_POSPISIL,
                    DANIIL_MEDVEDEV,
                ],
                'odds': {
                    VASEK_POSPISIL: 5.00,
                    DANIIL_MEDVEDEV: 1.16,
                },
                'score': [(6, 4), (6, 3)],
                'prediction': DANIIL_MEDVEDEV,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    GRIGOR_DIMITROV,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.40,
                    GRIGOR_DIMITROV: 1.55,
                },
                'score': [(6, 4), (6, 2)],
                'prediction': GRIGOR_DIMITROV,
                'bet': 5,
            },

            # 2020-02-13
            {
                'round': 16,
                'players': [
                    JANNIK_SINNER,
                    DAVID_GOFFIN,
                ],
                'odds': {
                    JANNIK_SINNER: 3.20,
                    DAVID_GOFFIN: 1.34,
                },
                'score': [(7, 6), (7, 5)],
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    ALEXANDER_BUBLIK,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.20,
                    ALEXANDER_BUBLIK: 4.40,
                },
                'score': [(7, 5), (6, 3)],
            },
            {
                'round': 16,
                'players': [
                    ALJAZ_BEDENE,
                    STEFANOS_TSITSIPAS,
                ],
                'odds': {
                    ALJAZ_BEDENE: 4.20,
                    STEFANOS_TSITSIPAS: 1.22,
                },
                'score': [(7, 5), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    GILLES_SIMON,
                ],
                'odds': {
                    GAEL_MONFILS: 1.28,
                    GILLES_SIMON: 3.60,
                },
                'score': [(6, 4), (6, 1)],
                'prediction': GAEL_MONFILS,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    FILIP_KRAJINOVIC,
                    VASEK_POSPISIL,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 2.00,
                    VASEK_POSPISIL: 1.80,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': VASEK_POSPISIL,
                'bet': 3,
            },

            # 2020-02-14
            {
                'round': 8,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JANNIK_SINNER,
                ],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.70,
                    JANNIK_SINNER: 2.10,
                },
                'score': [(7, 5), (3, 6), (7, 6)],
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 5,
            },
            {
                'round': 8,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    ALJAZ_BEDENE,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.52,
                    ALJAZ_BEDENE: 2.50,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 6,
            },
            {
                'round': 8,
                'players': [
                    GAEL_MONFILS,
                    DANIEL_EVANS,
                ],
                'odds': {
                    GAEL_MONFILS: 1.42,
                    DANIEL_EVANS: 2.80,
                },
                'score': [(7, 6), (6, 2)],
                'prediction': GAEL_MONFILS,
                'bet': 3,
            },
            {
                'round': 8,
                'players': [
                    FILIP_KRAJINOVIC,
                    ANDREY_RUBLEV,
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 3.40,
                    ANDREY_RUBLEV: 1.30,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': ANDREY_RUBLEV,
                'bet': 2,
            },

            # 2020-02-15
            {
                'round': 4,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    PABLO_CARRENO_BUSTA,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.55,
                    PABLO_CARRENO_BUSTA: 2.40,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 1,
            },
            {
                'round': 4,
                'players': [
                    GAEL_MONFILS,
                    FILIP_KRAJINOVIC,
                ],
                'odds': {
                    GAEL_MONFILS: 1.60,
                    FILIP_KRAJINOVIC: 2.30,
                },
                'score': [(6, 4), (7, 6)],
            },

            # 2020-02-16
            {
                'round': 2,
                'players': [
                    GAEL_MONFILS,
                    FELIX_AUGER_ALIASSIME,
                ],
                'odds': {
                    GAEL_MONFILS: 1.55,
                    FELIX_AUGER_ALIASSIME: 2.40,
                },
                'score': [(6, 2), (6, 4)],
                'prediction': GAEL_MONFILS,
                'bet': 4,
            }
        ]
    },

    {
        'location': NEW_YORK,
        'date': '2020-02-16',
        'matches': [

            # 2020-02-10
            {
                'round': 256,
                'players': [
                    JASON_JUNG,
                    MITCHELL_KRUEGER,
                ],
                'odds': {
                    JASON_JUNG: 1.65,
                    MITCHELL_KRUEGER: 2.20,
                },
                'score': [(6, 2), (6, 4)],
                'prediction': JASON_JUNG,
                'bet': 6,
            },
            {
                'round': 256,
                'players': [
                    PAOLO_LORENZI,
                    NOAH_RUBIN,
                ],
                'odds': {
                    PAOLO_LORENZI: 2.50,
                    NOAH_RUBIN: 1.52,
                },
                'score': [(6, 3), (6, 1)],
                'prediction': NOAH_RUBIN,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    DANILO_PETROVIC,
                    BRADLEY_KLAHN,
                ],
                'odds': {
                    DANILO_PETROVIC: 2.60,
                    BRADLEY_KLAHN: 1.48,
                },
                'score': [(6, 3), (6, 2)],
                'prediction': BRADLEY_KLAHN,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    GO_SOEDA,
                    BERNARD_TOMIC,
                ],
                'odds': {
                    GO_SOEDA: 1.70,
                    BERNARD_TOMIC: 2.10,
                },
                'score': [(6, 2), (6, 1)],
            },
            {
                'round': 32,
                'players': [
                    ANDREAS_SEPPI,
                    DAMIR_DZUMHUR,
                ],
                'odds': {
                    ANDREAS_SEPPI: 2.20,
                    DAMIR_DZUMHUR: 1.65,
                },
                'score': [(6, 3), (1, 6), (7, 6)],
                'prediction': DAMIR_DZUMHUR,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    TOMMY_PAUL,
                ],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.25,
                    TOMMY_PAUL: 1.62,
                },
                'score': [(6, 4), (6, 2)],
                'prediction': TOMMY_PAUL,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    STEVE_JOHNSON,
                    TENNYS_SANDGREN,
                ],
                'odds': {
                    STEVE_JOHNSON: 2.10,
                    TENNYS_SANDGREN: 1.70,
                },
                'score': [(6, 7), (6, 3), (7, 6)],
                'prediction': TENNYS_SANDGREN,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    MARCOS_GIRON,
                    JACK_SOCK,
                ],
                'odds': {
                    MARCOS_GIRON: 1.60,
                    JACK_SOCK: 2.30,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': MARCOS_GIRON,
                'bet': 1,
            },

            # 2020-02-11
            {
                'round': 32,
                'players': [
                    JORDAN_THOMPSON,
                    IVO_KARLOVIC,
                ],
                'odds': {
                    JORDAN_THOMPSON: 1.62,
                    IVO_KARLOVIC: 2.25,
                },
                'score': [(6, 3), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    SOONWOO_KWON,
                    GO_SOEDA,
                ],
                'odds': {
                    SOONWOO_KWON: 1.52,
                    GO_SOEDA: 2.50,
                },
                'score': [(6, 2), (6, 7), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    KYLE_EDMUND,
                    YASUTAKA_UCHIYAMA,
                ],
                'odds': {
                    KYLE_EDMUND: 1.24,
                    YASUTAKA_UCHIYAMA: 4.00,
                },
                'score': [(7, 5), (6, 4)],
                'prediction': KYLE_EDMUND,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    PAOLO_LORENZI,
                    DANILO_PETROVIC,
                ],
                'odds': {
                    PAOLO_LORENZI: 1.95,
                    DANILO_PETROVIC: 1.85,
                },
                'score': [(4, 6), (6, 4), (6, 0)],
                'prediction': DANILO_PETROVIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    HENRI_LAAKSONEN,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.24,
                    HENRI_LAAKSONEN: 4.00,
                },
                'score': [(6, 3), (0, 6), (6, 2)],
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    DOMINIK_KOEPFER,
                    BRAYDEN_SCHNUR,
                ],
                'odds': {
                    DOMINIK_KOEPFER: 1.48,
                    BRAYDEN_SCHNUR: 2.60,
                },
                'score': [(6, 4), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    BRIAN_SHI,
                ],
                'odds': {
                    CAMERON_NORRIE: 1.01,
                    BRIAN_SHI: 17.00,
                },
                'score': [(7, 5), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    JASON_JUNG,
                    KEVIN_ANDERSON,
                ],
                'odds': {
                    JASON_JUNG: 3.80,
                    KEVIN_ANDERSON: 1.26,
                },
                'score': [(7, 6), (6, 4)],
            },

            # 2020-02-12
            {
                'round': 16,
                'players': [
                    MIOMIR_KECMANOVIC,
                    PAOLO_LORENZI,
                ],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.28,
                    PAOLO_LORENZI: 3.60,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    ANDREAS_SEPPI,
                    STEVE_JOHNSON,
                ],
                'odds': {
                    ANDREAS_SEPPI: 2.50,
                    STEVE_JOHNSON: 1.52,
                },
                'score': [(7, 6), (6, 3)],
                'prediction': STEVE_JOHNSON,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    SOONWOO_KWON,
                    MILOS_RAONIC,
                ],
                'odds': {
                    SOONWOO_KWON: 4.20,
                    MILOS_RAONIC: 1.22,
                },
                'score': [(7, 6), (6, 7), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    UGO_HUMBERT,
                    MARCOS_GIRON,
                ],
                'odds': {
                    UGO_HUMBERT: 1.26,
                    MARCOS_GIRON: 3.80,
                },
                'score': [(6, 1), (6, 0)],
            },

            # 2020-02-13
            {
                'round': 16,
                'players': [
                    KYLE_EDMUND,
                    DOMINIK_KOEPFER,
                ],
                'odds': {
                    KYLE_EDMUND: 1.45,
                    DOMINIK_KOEPFER: 2.70,
                },
                'score': [(6, 2), (6, 4)],
                'prediction': KYLE_EDMUND,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    JASON_JUNG,
                    CAMERON_NORRIE,
                ],
                'odds': {
                    JASON_JUNG: 1.85,
                    CAMERON_NORRIE: 1.95,
                },
                'score': [(6, 4), (6, 4)],
                'prediction': JASON_JUNG,
                'bet': 8,
            },
            {
                'round': 16,
                'players': [
                    REILLY_OPELKA,
                    YOSHIHITO_NISHIOKA,
                ],
                'odds': {
                    REILLY_OPELKA: 1.60,
                    YOSHIHITO_NISHIOKA: 2.30,
                },
                'score': [(6, 4), (6, 4)],
                'prediction': REILLY_OPELKA,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    JORDAN_THOMPSON,
                    JOHN_ISNER,
                ],
                'odds': {
                    JORDAN_THOMPSON: 2.50,
                    JOHN_ISNER: 1.52,
                },
                'score': [(7, 6), (6, 7), (6, 3)],
                'prediction': JOHN_ISNER,
                'bet': 3,
            },

            # 2020-02-14
            {
                'round': 8,
                'players': [
                    MIOMIR_KECMANOVIC,
                    UGO_HUMBERT,
                ],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.15,
                    UGO_HUMBERT: 1.68,
                },
                'score': [(3, 6), (6, 2), (6, 4)],
                'prediction': UGO_HUMBERT,
                'bet': 5,
            },
            {
                'round': 8,
                'players': [
                    KYLE_EDMUND,
                    SOONWOO_KWON,
                ],
                'odds': {
                    KYLE_EDMUND: 1.60,
                    SOONWOO_KWON: 2.30,
                },
                'score': [(3, 6), (6, 2), (7, 6)],
                'prediction': KYLE_EDMUND,
                'bet': 5,
            },
            {
                'round': 8,
                'players': [
                    JASON_JUNG,
                    REILLY_OPELKA,
                ],
                'odds': {
                    JASON_JUNG: 3.10,
                    REILLY_OPELKA: 1.36,
                },
                'score': [(5, 7), (6, 4), (6, 4)],
                'prediction': REILLY_OPELKA,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    ANDREAS_SEPPI,
                    JORDAN_THOMPSON,
                ],
                'odds': {
                    ANDREAS_SEPPI: 2.05,
                    JORDAN_THOMPSON: 1.75,
                },
                'score': [(6, 7), (6, 4), (6, 1)],
                'prediction': JORDAN_THOMPSON,
                'bet': 5,
            },

            # 2020-02-15
            {
                'round': 4,
                'players': [
                    KYLE_EDMUND,
                    MIOMIR_KECMANOVIC,
                ],
                'odds': {
                    KYLE_EDMUND: 1.75,
                    MIOMIR_KECMANOVIC: 2.05,
                },
                'score': [(6, 1), (6, 4)],
                'prediction': KYLE_EDMUND,
                'bet': 1,
            },
            {
                'round': 4,
                'players': [
                    ANDREAS_SEPPI,
                    JASON_JUNG,
                ],
                'odds': {
                    ANDREAS_SEPPI: 1.65,
                    JASON_JUNG: 2.20,
                },
                'score': [(6, 3), (6, 2)],
            },

            # 2020-02-16
            {
                'round': 2,
                'players': [
                    KYLE_EDMUND,
                    ANDREAS_SEPPI,
                ],
                'odds': {
                    KYLE_EDMUND: 1.38,
                    ANDREAS_SEPPI: 3.00,
                },
                'score': [(7, 5), (6, 1)],
            }
        ]
    },

    {
        'location': BUENOS_AIRES,
        'date': '2020-02-10',
        'matches': [

            # 2020-02-10
            {
                'round': 32,
                'players': [
                    THIAGO_MONTEIRO,
                    JAUME_MUNAR,
                ],
                'odds': {
                    THIAGO_MONTEIRO: 2.00,
                    JAUME_MUNAR: 1.80,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': JAUME_MUNAR,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    CASPER_RUUD,
                    PABLO_ANDUJAR,
                ],
                'odds': {
                    CASPER_RUUD: 1.65,
                    PABLO_ANDUJAR: 2.20,
                },
                'score': [(6, 2), (6, 3)],
                'prediction': CASPER_RUUD,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    PABLO_CUEVAS,
                    LORENZO_SONEGO,
                ],
                'odds': {
                    PABLO_CUEVAS: 1.55,
                    LORENZO_SONEGO: 2.40,
                },
                'score': [(6, 4), (6, 4)],
                'prediction': PABLO_CUEVAS,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    FEDERICO_DELBONIS,
                    HUGO_DELLIEN,
                ],
                'odds': {
                    FEDERICO_DELBONIS: 1.26,
                    HUGO_DELLIEN: 3.80,
                },
                'score': [(1, 6), (6, 3), (7, 5)],
                'prediction': FEDERICO_DELBONIS,
                'bet': 5,
            },

            # 2020-02-11
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    MARCO_CECCHINATO,
                ],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 3.20,
                    MARCO_CECCHINATO: 1.34,
                },
                'score': [(6, 4), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    FACUNDO_BAGNIS,
                    ANDREJ_MARTIN,
                ],
                'odds': {
                    FACUNDO_BAGNIS: 2.20,
                    ANDREJ_MARTIN: 1.65,
                },
                'score': [(6, 4), (6, 1)],
                'prediction': ANDREJ_MARTIN,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    JOZEF_KOVALIK,
                    CORENTIN_MOUTET,
                ],
                'odds': {
                    JOZEF_KOVALIK: 2.25,
                    CORENTIN_MOUTET: 1.62,
                },
                'score': [(6, 3), (7, 6)],
                'prediction': CORENTIN_MOUTET,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    PEDRO_MARTINEZ,
                    FERNANDO_VERDASCO,
                ],
                'odds': {
                    PEDRO_MARTINEZ: 2.40,
                    FERNANDO_VERDASCO: 1.55,
                },
                'score': [(7, 6), (7, 5)],
                'prediction': FERNANDO_VERDASCO,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    LASLO_DJERE,
                    FRANCISCO_CERUNDOLO,
                ],
                'odds': {
                    LASLO_DJERE: 1.32,
                    FRANCISCO_CERUNDOLO: 3.30,
                },
                'score': [(6, 2), (2, 6), (6, 4)],
                'prediction': LASLO_DJERE,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    FILIP_HORANSKY,
                ],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.26,
                    FILIP_HORANSKY: 3.80,
                },
                'score': [(6, 4), (4, 6), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    LEONARDO_MAYER,
                ],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.42,
                    LEONARDO_MAYER: 2.80,
                },
                'score': [(4, 6), (6, 3), (7, 5)],
            },

            # 2020-02-12
            {
                'round': 16,
                'players': [
                    PEDRO_SOUSA,
                    JOZEF_KOVALIK,
                ],
                'odds': {
                    PEDRO_SOUSA: 3.20,
                    JOZEF_KOVALIK: 1.34,
                },
                'score': [(7, 6), (7, 6)],
            },
            {
                'round': 16,
                'players': [
                    DUSAN_LAJOVIC,
                    PEDRO_MARTINEZ,
                ],
                'odds': {
                    DUSAN_LAJOVIC: 1.45,
                    PEDRO_MARTINEZ: 2.70,
                },
                'score': [(7, 6), (7, 6)],
            },
            {
                'round': 16,
                'players': [
                    CASPER_RUUD,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'odds': {
                    CASPER_RUUD: 1.38,
                    ROBERTO_CARBALLES_BAENA: 3.00,
                },
                'score': [(6, 1), (6, 0)],
                'prediction': CASPER_RUUD,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    THIAGO_MONTEIRO,
                    BORNA_CORIC,
                ],
                'odds': {
                    THIAGO_MONTEIRO: 1.75,
                    BORNA_CORIC: 2.05,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': THIAGO_MONTEIRO,
                'bet': 2,
            },

            # 2020-02-13
            {
                'round': 16,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    LASLO_DJERE,
                ],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.90,
                    LASLO_DJERE: 1.90,
                },
                'score': [(6, 7), (6, 2), (6, 1)],
            },
            {
                'round': 16,
                'players': [
                    PABLO_CUEVAS,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'odds': {
                    PABLO_CUEVAS: 1.58,
                    ALBERT_RAMOS_VINOLAS: 2.35,
                },
                'score': [(6, 4), (4, 6), (6, 4)],
                'prediction': PABLO_CUEVAS,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    GUIDO_PELLA,
                    FACUNDO_BAGNIS,
                ],
                'odds': {
                    GUIDO_PELLA: 1.34,
                    FACUNDO_BAGNIS: 3.20,
                },
                'score': [(7, 6), (6, 7), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    FEDERICO_DELBONIS,
                ],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.24,
                    FEDERICO_DELBONIS: 4.00,
                },
                'score': [(6, 3), (4, 6), (6, 2)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 5,
            },

            # 2020-02-14
            {
                'round': 8,
                'players': [
                    CASPER_RUUD,
                    DUSAN_LAJOVIC,
                ],
                'odds': {
                    CASPER_RUUD: 1.42,
                    DUSAN_LAJOVIC: 2.80,
                },
                'score': [(7, 5), (6, 1)],
                'prediction': CASPER_RUUD,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    GUIDO_PELLA,
                ],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.95,
                    GUIDO_PELLA: 1.85,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': GUIDO_PELLA,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    PABLO_CUEVAS,
                ],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.28,
                    PABLO_CUEVAS: 3.60,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 5,
            },
            {
                'round': 8,
                'players': [
                    PEDRO_SOUSA,
                    THIAGO_MONTEIRO,
                ],
                'odds': {
                    PEDRO_SOUSA: 3.60,
                    THIAGO_MONTEIRO: 1.28,
                },
                'score': [(7, 6), (6, 4)],
            },

            # 2020-02-15
            {
                'round': 4,
                'players': [
                    CASPER_RUUD,
                    JUAN_IGNACIO_LONDERO,
                ],
                'odds': {
                    CASPER_RUUD: 1.48,
                    JUAN_IGNACIO_LONDERO: 2.60,
                },
                'score': [(4, 6), (7, 5), (6, 1)],
                'prediction': CASPER_RUUD,
                'bet': 6,
            },
            {
                'round': 4,
                'players': [
                    PEDRO_SOUSA,
                    DIEGO_SCHWARTZMAN,
                ],
                'odds': {
                    PEDRO_SOUSA: 3.00,
                    DIEGO_SCHWARTZMAN: 1.38,
                },
                'score': [],
                'retired': True,
            },

            # 2020-02-16
            {
                'round': 2,
                'players': [
                    CASPER_RUUD,
                    PEDRO_SOUSA,
                ],
                'odds': {
                    CASPER_RUUD: 1.14,
                    PEDRO_SOUSA: 5.50,
                },
                'score': [(6, 1), (6, 4)],
            }
        ]
    },

    {
        'location': RIO_DE_JANEIRO,
        'date': '2020-02-23',
        'matches': [

            # 2020-02-16
            {
                'round': 512,
                'players': [
                    ATTILA_BALAZS,
                    GIANLUCA_MAGER,
                ],
                'odds': {
                    ATTILA_BALAZS: 1.80,
                    GIANLUCA_MAGER: 1.95,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': ATTILA_BALAZS,
                'bet': 4,
            },
            {
                'round': 256,
                'players': [
                    FEDERICO_CORIA,
                    JOZEF_KOVALIK,
                ],
                'odds': {
                    FEDERICO_CORIA: 2.50,
                    JOZEF_KOVALIK: 1.50,
                },
                'score': [(6, 2), (6, 4)],
            },
            {
                'round': 256,
                'players': [
                    JOAO_DOMINGUES,
                    FEDERICO_GAIO,
                ],
                'odds': {
                    JOAO_DOMINGUES: 2.25,
                    FEDERICO_GAIO: 1.60,
                },
                'score': [(3, 6), (7, 6), (7, 5)],
                'prediction': FEDERICO_GAIO,
                'bet': 9,
            },
            {
                'round': 256,
                'players': [
                    PEDRO_MARTINEZ,
                    FILIP_HORANSKY,
                ],
                'odds': {
                    PEDRO_MARTINEZ: 1.55,
                    FILIP_HORANSKY: 2.40,
                },
                'score': [(6, 4), (6, 2)],
                'prediction': PEDRO_MARTINEZ,
                'bet': 1,
            },

            # 2020-02-17
            {
                'round': 32,
                'players': [
                    PABLO_ANDUJAR,
                    FERNANDO_VERDASCO,
                ],
                'odds': {
                    PABLO_ANDUJAR: 2.20,
                    FERNANDO_VERDASCO: 1.65,
                },
                'score': [(6, 3), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    FEDERICO_DELBONIS,
                    ROBERTO_CARBALLES_BAENA,
                ],
                'odds': {
                    FEDERICO_DELBONIS: 1.60,
                    ROBERTO_CARBALLES_BAENA: 2.30,
                },
                'score': [(6, 2), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    CHRISTIAN_GARIN,
                    ANDREJ_MARTIN,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.26,
                    ANDREJ_MARTIN: 3.80,
                },
                'score': [(4, 6), (7, 5), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    PEDRO_MARTINEZ,
                    HUGO_DELLIEN,
                ],
                'odds': {
                    PEDRO_MARTINEZ: 1.75,
                    HUGO_DELLIEN: 2.05,
                },
                'score': [(3, 6), (6, 2), (7, 5)],
                'prediction': PEDRO_MARTINEZ,
                'bet': 8,
            },
            {
                'round': 32,
                'players': [
                    FEDERICO_CORIA,
                    CORENTIN_MOUTET,
                ],
                'odds': {
                    FEDERICO_CORIA: 2.50,
                    CORENTIN_MOUTET: 1.52,
                },
                'score': [(1, 6), (7, 6), (7, 6)],
                'prediction': CORENTIN_MOUTET,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    THIAGO_SEYBOTH_WILD,
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                ],
                'odds': {
                    THIAGO_SEYBOTH_WILD: 2.50,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.52,
                },
                'score': [(5, 7), (7, 6), (7, 5)],
                'prediction': ALEJANDRO_DAVIDOVICH_FOKINA,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    CARLOS_ALCARAZ_GARFIA,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'odds': {
                    CARLOS_ALCARAZ_GARFIA: 4.20,
                    ALBERT_RAMOS_VINOLAS: 1.22,
                },
                'score': [(7, 6), (4, 6), (7, 6)],
                'prediction': ALBERT_RAMOS_VINOLAS,
                'bet': 6,
            },

            # 2020-02-18
            {
                'round': 32,
                'players': [
                    ATTILA_BALAZS,
                    PABLO_CUEVAS,
                ],
                'odds': {
                    ATTILA_BALAZS: 4.00,
                    PABLO_CUEVAS: 1.24,
                },
                'score': [(6, 4), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    DUSAN_LAJOVIC,
                    MARCO_CECCHINATO,
                ],
                'odds': {
                    DUSAN_LAJOVIC: 1.58,
                    MARCO_CECCHINATO: 2.35,
                },
                'score': [(6, 4), (6, 7), (6, 1)],
            },
            {
                'round': 32,
                'players': [
                    BORNA_CORIC,
                    JUAN_IGNACIO_LONDERO,
                ],
                'odds': {
                    BORNA_CORIC: 2.00,
                    JUAN_IGNACIO_LONDERO: 1.80,
                },
                'score': [(7, 6), (7, 5)],
                'prediction': JUAN_IGNACIO_LONDERO,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    JAUME_MUNAR,
                    SALVATORE_CARUSO,
                ],
                'odds': {
                    JAUME_MUNAR: 1.52,
                    SALVATORE_CARUSO: 2.50,
                },
                'score': [(7, 5), (6, 4)],
                'prediction': JAUME_MUNAR,
                'bet': 12,
            },
            {
                'round': 32,
                'players': [
                    JOAO_DOMINGUES,
                    FEDERICO_GAIO,
                ],
                'odds': {
                    JOAO_DOMINGUES: 1.55,
                    FEDERICO_GAIO: 2.40,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': JOAO_DOMINGUES,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    GIANLUCA_MAGER,
                    CASPER_RUUD,
                ],
                'odds': {
                    GIANLUCA_MAGER: 5.00,
                    CASPER_RUUD: 1.16,
                },
                'score': [(7, 6), (7, 5)],
            },
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    LEONARDO_MAYER,
                ],
                'odds': {
                    LORENZO_SONEGO: 1.80,
                    LEONARDO_MAYER: 2.00,
                },
                'score': [(6, 1), (5, 7), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    DOMINIC_THIEM,
                    FELIPE_ALVES,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.01,
                    FELIPE_ALVES: 21.00,
                },
                'score': [(6, 2), (4, 6), (6, 1)],
            },
            {
                'round': 32,
                'players': [
                    THIAGO_MONTEIRO,
                    GUIDO_PELLA,
                ],
                'odds': {
                    THIAGO_MONTEIRO: 2.20,
                    GUIDO_PELLA: 1.65,
                },
                'score': [(5, 7), (6, 4), (7, 6)],
                'prediction': GUIDO_PELLA,
                'bet': 5,
            },

            # 2020-02-19
            {
                'round': 16,
                'players': [
                    CHRISTIAN_GARIN,
                    FEDERICO_DELBONIS,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.48,
                    FEDERICO_DELBONIS: 2.60,
                },
                'score': [(6, 4), (6, 3)],
                'prediction': CHRISTIAN_GARIN,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    PEDRO_MARTINEZ,
                    PABLO_ANDUJAR,
                ],
                'odds': {
                    PEDRO_MARTINEZ: 2.40,
                    PABLO_ANDUJAR: 1.55,
                },
                'score': [(6, 1), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    FEDERICO_CORIA,
                    CARLOS_ALCARAZ_GARFIA,
                ],
                'odds': {
                    FEDERICO_CORIA: 1.70,
                    CARLOS_ALCARAZ_GARFIA: 2.10,
                },
                'score': [(6, 4), (4, 6), (6, 4)],
                'prediction': FEDERICO_CORIA,
                'bet': 2,
            },

            # 2020-02-20
            {
                'round': 16,
                'players': [
                    GIANLUCA_MAGER,
                    JOAO_DOMINGUES,
                ],
                'odds': {
                    GIANLUCA_MAGER: 1.45,
                    JOAO_DOMINGUES: 2.70,
                },
                'score': [(6, 3), (7, 6)],
                'prediction': GIANLUCA_MAGER,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    LORENZO_SONEGO,
                    DUSAN_LAJOVIC,
                ],
                'odds': {
                    LORENZO_SONEGO: 2.60,
                    DUSAN_LAJOVIC: 1.48,
                },
                'score': [(7, 6), (7, 6)],
                'prediction': DUSAN_LAJOVIC,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    THIAGO_SEYBOTH_WILD,
                ],
                'odds': {
                    BORNA_CORIC: 1.38,
                    THIAGO_SEYBOTH_WILD: 3.00,
                },
                'score': [(6, 3), (1, 6), (7, 6)],
                'prediction': BORNA_CORIC,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    DOMINIC_THIEM,
                    JAUME_MUNAR,
                ],
                'odds': {
                    DOMINIC_THIEM: 1.16,
                    JAUME_MUNAR: 5.00,
                },
                'score': [(6, 7), (6, 3), (6, 4)],
            },

            # 2020-02-21
            {
                'round': 8,
                'players': [
                    CHRISTIAN_GARIN,
                    FEDERICO_CORIA,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.20,
                    FEDERICO_CORIA: 4.40,
                },
                'score': [(2, 6), (6, 3), (7, 5)],
                'prediction': CHRISTIAN_GARIN,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    BORNA_CORIC,
                    LORENZO_SONEGO,
                ],
                'odds': {
                    BORNA_CORIC: 1.68,
                    LORENZO_SONEGO: 2.15,
                },
                'score': [(7, 6), (6, 3)],
                'prediction': BORNA_CORIC,
                'bet': 7,
            },

            # 2020-02-22
            {
                'round': 8,
                'players': [
                    GIANLUCA_MAGER,
                    DOMINIC_THIEM,
                ],
                'odds': {
                    GIANLUCA_MAGER: 6.50,
                    DOMINIC_THIEM: 1.10,
                },
                'score': [(7, 6), (7, 5)],
                'prediction': DOMINIC_THIEM,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    ATTILA_BALAZS,
                    PEDRO_MARTINEZ,
                ],
                'odds': {
                    ATTILA_BALAZS: 2.25,
                    PEDRO_MARTINEZ: 1.62,
                },
                'score': [(2, 6), (6, 4), (6, 2)],
                'prediction': PEDRO_MARTINEZ,
                'bet': 3,
            },
            {
                'round': 4,
                'players': [
                    CHRISTIAN_GARIN,
                    BORNA_CORIC,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.70,
                    BORNA_CORIC: 2.10,
                },
                'score': [(2, 6), (6, 3), (7, 5)],
                'prediction': CHRISTIAN_GARIN,
                'bet': 3,
            },

            # 2020-02-23
            {
                'round': 2,
                'players': [
                    CHRISTIAN_GARIN,
                    GIANLUCA_MAGER,
                ],
                'odds': {
                    CHRISTIAN_GARIN: 1.26,
                    GIANLUCA_MAGER: 3.80,
                },
                'score': [(7, 6), (7, 5)],
                'prediction': CHRISTIAN_GARIN,
                'bet': 1,
            }
        ]
    },

    {
        'location': MARSEILLE,
        'date': '2020-02-23',
        'matches': [

            # 2020-02-16
            {
                'round': 512,
                'players': [
                    ELLIOT_BENCHETRIT,
                    LLOYD_HARRIS,
                ],
                'odds': {
                    ELLIOT_BENCHETRIT: 3.60,
                    LLOYD_HARRIS: 1.26,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': LLOYD_HARRIS,
                'bet': 2,
            },
            {
                'round': 512,
                'players': [
                    EMIL_RUUSUVUORI,
                    LUKAS_LACKO,
                ],
                'odds': {
                    EMIL_RUUSUVUORI: 1.26,
                    LUKAS_LACKO: 3.60,
                },
                'score': [(6, 4), (6, 4)],
            },
            {
                'round': 512,
                'players': [
                    MATTHIAS_BACHINGER,
                    SERGIY_STAKHOVSKY,
                ],
                'odds': {
                    MATTHIAS_BACHINGER: 2.20,
                    SERGIY_STAKHOVSKY: 1.62,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': SERGIY_STAKHOVSKY,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    DENNIS_NOVAK,
                    ARTHUR_CAZAUX,
                ],
                'odds': {
                    DENNIS_NOVAK: 1.08,
                    ARTHUR_CAZAUX: 7.00,
                },
                'score': [(6, 1), (6, 3)],
                'prediction': DENNIS_NOVAK,
                'bet': 3,
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    STEVEN_DIEZ,
                ],
                'odds': {
                    ALEXEI_POPYRIN: 1.32,
                    STEVEN_DIEZ: 3.20,
                },
                'score': [(7, 6), (6, 3)],
                'prediction': ALEXEI_POPYRIN,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    ILYA_IVASHKA,
                    BERNABE_ZAPATA_MIRALLES,
                ],
                'odds': {
                    ILYA_IVASHKA: 1.26,
                    BERNABE_ZAPATA_MIRALLES: 3.60,
                },
                'score': [(6, 7), (7, 5), (6, 1)],
                'prediction': ILYA_IVASHKA,
                'bet': 1,
            },

            # 2020-02-17
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    KAREN_KHACHANOV,
                ],
                'odds': {
                    ALJAZ_BEDENE: 2.70,
                    KAREN_KHACHANOV: 1.45,
                },
                'score': [(4, 6), (6, 4), (7, 5)],
            },
            {
                'round': 32,
                'players': [
                    NORBERT_GOMBOS,
                    ELLIOT_BENCHETRIT,
                ],
                'odds': {
                    NORBERT_GOMBOS: 1.42,
                    ELLIOT_BENCHETRIT: 2.80,
                },
                'score': [(6, 4), (6, 7), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    EGOR_GERASIMOV,
                    EMIL_RUUSUVUORI,
                ],
                'odds': {
                    EGOR_GERASIMOV: 2.05,
                    EMIL_RUUSUVUORI: 1.75,
                },
                'score': [(4, 6), (7, 6), (7, 6)],
                'prediction': EMIL_RUUSUVUORI,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    DENNIS_NOVAK,
                    MATTHIAS_BACHINGER,
                ],
                'odds': {
                    DENNIS_NOVAK: 1.40,
                    MATTHIAS_BACHINGER: 2.90,
                },
                'score': [(7, 6), (2, 6), (6, 3)],
                'prediction': DENNIS_NOVAK,
                'bet': 12,
            },
            {
                'round': 256,
                'players': [
                    ILYA_IVASHKA,
                    ALEXEI_POPYRIN,
                ],
                'odds': {
                    ILYA_IVASHKA: 1.90,
                    ALEXEI_POPYRIN: 1.90,
                },
                'score': [(6, 1), (3, 6), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    MIKAEL_YMER,
                    RICHARD_GASQUET,
                ],
                'odds': {
                    MIKAEL_YMER: 1.75,
                    RICHARD_GASQUET: 2.05,
                },
                'score': [(6, 3), (3, 6), (7, 5)],
                'prediction': MIKAEL_YMER,
                'bet': 8,
            },
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    GREGOIRE_BARRERE,
                ],
                'odds': {
                    BENOIT_PAIRE: 1.68,
                    GREGOIRE_BARRERE: 2.15,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': BENOIT_PAIRE,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_BUBLIK,
                    MARTON_FUCSOVICS,
                ],
                'odds': {
                    ALEXANDER_BUBLIK: 2.70,
                    MARTON_FUCSOVICS: 1.45,
                },
                'score': [(6, 4), (7, 5)],
                'prediction': MARTON_FUCSOVICS,
                'bet': 1,
            },

            # 2020-02-18
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    ANTOINE_HOANG,
                ],
                'odds': {
                    HUBERT_HURKACZ: 1.24,
                    ANTOINE_HOANG: 4.00,
                },
                'score': [(6, 4), (6, 1)],
            },
            {
                'round': 32,
                'players': [
                    VASEK_POSPISIL,
                    EMIL_RUUSUVUORI,
                ],
                'odds': {
                    VASEK_POSPISIL: 1.38,
                    EMIL_RUUSUVUORI: 3.00,
                },
                'score': [(7, 6), (6, 3)],
            },
            {
                'round': 32,
                'players': [
                    JANNIK_SINNER,
                    NORBERT_GOMBOS,
                ],
                'odds': {
                    JANNIK_SINNER: 1.34,
                    NORBERT_GOMBOS: 3.20,
                },
                'score': [(6, 4), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    MARIN_CILIC,
                    ILYA_IVASHKA,
                ],
                'odds': {
                    MARIN_CILIC: 1.26,
                    ILYA_IVASHKA: 3.80,
                },
                'score': [(3, 6), (7, 6), (6, 4)],
                'prediction': MARIN_CILIC,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    HAROLD_MAYOT,
                ],
                'odds': {
                    GILLES_SIMON: 1.22,
                    HAROLD_MAYOT: 4.20,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': GILLES_SIMON,
                'bet': 8,
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    KAREN_KHACHANOV,
                ],
                'odds': {
                    ALJAZ_BEDENE: 2.60,
                    KAREN_KHACHANOV: 1.48,
                },
                'score': [(4, 6), (6, 4), (7, 5)],
            },

            # 2020-02-19
            {
                'round': 16,
                'players': [
                    EGOR_GERASIMOV,
                    DENNIS_NOVAK,
                ],
                'odds': {
                    EGOR_GERASIMOV: 1.65,
                    DENNIS_NOVAK: 2.20,
                },
                'score': [(7, 6), (6, 3)],
                'prediction': EGOR_GERASIMOV,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    VASEK_POSPISIL,
                    HUBERT_HURKACZ,
                ],
                'odds': {
                    VASEK_POSPISIL: 2.40,
                    HUBERT_HURKACZ: 1.55,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': HUBERT_HURKACZ,
                'bet': 6,
            },
            {
                'round': 16,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    MIKHAIL_KUKUSHKIN,
                ],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.58,
                    MIKHAIL_KUKUSHKIN: 2.35,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': PIERRE_HUGUES_HERBERT,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    STEFANO_TRAVAGLIA,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.26,
                    STEFANO_TRAVAGLIA: 3.80,
                },
                'score': [(6, 7), (7, 6), (6, 3)],
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    MIKAEL_YMER,
                ],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.20,
                    MIKAEL_YMER: 4.40,
                },
                'score': [(6, 1), (6, 3)],
            },
            {
                'round': 16,
                'players': [
                    BENOIT_PAIRE,
                    ALEXANDER_BUBLIK,
                ],
                'odds': {
                    BENOIT_PAIRE: 1.58,
                    ALEXANDER_BUBLIK: 2.35,
                },
                'score': [(6, 4), (7, 6)],
            },

            # 2020-02-20
            {
                'round': 16,
                'players': [
                    GILLES_SIMON,
                    ALJAZ_BEDENE,
                ],
                'odds': {
                    GILLES_SIMON: 2.40,
                    ALJAZ_BEDENE: 1.55,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': ALJAZ_BEDENE,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    DENIS_SHAPOVALOV,
                    MARIN_CILIC,
                ],
                'odds': {
                    DENIS_SHAPOVALOV: 1.80,
                    MARIN_CILIC: 2.00,
                },
                'score': [(6, 4), (4, 6), (6, 2)],
                'prediction': DENIS_SHAPOVALOV,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    DANIIL_MEDVEDEV,
                    JANNIK_SINNER,
                ],
                'odds': {
                    DANIIL_MEDVEDEV: 1.26,
                    JANNIK_SINNER: 3.80,
                },
                'score': [(1, 6), (6, 1), (6, 2)],
                'prediction': DANIIL_MEDVEDEV,
                'bet': 10,
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    PIERRE_HUGUES_HERBERT,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.00,
                    PIERRE_HUGUES_HERBERT: 1.80,
                },
                'score': [(6, 0), (6, 7), (7, 6)],
                'prediction': PIERRE_HUGUES_HERBERT,
                'bet': 4,
            },
            {
                'round': 16,
                'players': [
                    EGOR_GERASIMOV,
                    DAVID_GOFFIN,
                ],
                'odds': {
                    EGOR_GERASIMOV: 2.70,
                    DAVID_GOFFIN: 1.45,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': DAVID_GOFFIN,
                'bet': 5,
            },

            # 2020-02-21
            {
                'round': 8,
                'players': [
                    ALEXANDER_BUBLIK,
                    DENIS_SHAPOVALOV,
                ],
                'odds': {
                    ALEXANDER_BUBLIK: 2.90,
                    DENIS_SHAPOVALOV: 1.40,
                },
                'score': [(7, 5), (4, 6), (6, 3)],
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    STEFANOS_TSITSIPAS,
                    VASEK_POSPISIL,
                ],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.45,
                    VASEK_POSPISIL: 2.70,
                },
                'score': [(7, 5), (6, 3)],
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    GILLES_SIMON,
                    DANIIL_MEDVEDEV,
                ],
                'odds': {
                    GILLES_SIMON: 4.60,
                    DANIIL_MEDVEDEV: 1.18,
                },
                'score': [(6, 4), (6, 0)],
                'prediction': DANIIL_MEDVEDEV,
                'bet': 11,
            },
            {
                'round': 8,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    EGOR_GERASIMOV,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.52,
                    EGOR_GERASIMOV: 2.50,
                },
                'score': [(7, 5), (6, 2)],
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 1,
            },

            # 2020-02-22
            {
                'round': 4,
                'players': [
                    STEFANOS_TSITSIPAS,
                    ALEXANDER_BUBLIK,
                ],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.22,
                    ALEXANDER_BUBLIK: 4.20,
                },
                'score': [(7, 5), (6, 3)],
            },
            {
                'round': 4,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    GILLES_SIMON,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.55,
                    GILLES_SIMON: 2.40,
                },
                'score': [(7, 5), (7, 6)],
                'prediction': FELIX_AUGER_ALIASSIME,
                'bet': 2,
            },

            # 2020-02-23
            {
                'round': 2,
                'players': [
                    STEFANOS_TSITSIPAS,
                    FELIX_AUGER_ALIASSIME,
                ],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.40,
                    FELIX_AUGER_ALIASSIME: 2.90,
                },
                'score': [(6, 3), (6, 4)],
            }
        ]
    },

    {
        'location': DELRAY_BEACH,
        'date': '2020-02-23',
        'matches': [

            # 2020-02-16
            {
                'round': 256,
                'players': [
                    NOAH_RUBIN,
                    DENIS_ISTOMIN,
                ],
                'odds': {
                    NOAH_RUBIN: 2.15,
                    DENIS_ISTOMIN: 1.65,
                },
                'score': [(6, 4), (3, 6), (7, 6)],
            },
            {
                'round': 256,
                'players': [
                    ERNESTS_GULBIS,
                    BERNARD_TOMIC,
                ],
                'odds': {
                    ERNESTS_GULBIS: 1.55,
                    BERNARD_TOMIC: 2.40,
                },
                'score': [(6, 2), (6, 0)],
                'prediction': ERNESTS_GULBIS,
                'bet': 4,
            },
            {
                'round': 512,
                'players': [
                    EMILIO_GOMEZ,
                    STEFAN_KOZLOV,
                ],
                'odds': {
                    EMILIO_GOMEZ: 1.95,
                    STEFAN_KOZLOV: 1.85,
                },
                'score': [(6, 3), (6, 2)],
            },
            {
                'round': 512,
                'players': [
                    CAMERON_NORRIE,
                    MITCHELL_KRUEGER,
                ],
                'odds': {
                    CAMERON_NORRIE: 1.40,
                    MITCHELL_KRUEGER: 2.90,
                },
                'score': [(4, 6), (6, 2), (7, 6)],
                'prediction': CAMERON_NORRIE,
                'bet': 4,
            },

            # 2020-02-17
            {
                'round': 32,
                'players': [
                    MACKENZIE_MCDONALD,
                    YASUTAKA_UCHIYAMA,
                ],
                'odds': {
                    MACKENZIE_MCDONALD: 1.65,
                    YASUTAKA_UCHIYAMA: 2.20,
                },
                'score': [(6, 2), (7, 6)],
                'prediction': MACKENZIE_MCDONALD,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    RYAN_HARRISON,
                    DAMIR_DZUMHUR,
                ],
                'odds': {
                    RYAN_HARRISON: 3.10,
                    DAMIR_DZUMHUR: 1.36,
                },
                'score': [(6, 3), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    SOONWOO_KWON,
                    ADRIAN_MANNARINO,
                ],
                'odds': {
                    SOONWOO_KWON: 1.70,
                    ADRIAN_MANNARINO: 2.10,
                },
                'score': [(1, 6), (6, 3), (6, 2)],
                'prediction': SOONWOO_KWON,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    JOHN_MILLMAN,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.95,
                    JOHN_MILLMAN: 1.85,
                },
                'score': [(3, 6), (6, 4), (6, 2)],
            },

            # 2020-02-18
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    TAYLOR_FRITZ,
                ],
                'odds': {
                    CAMERON_NORRIE: 2.90,
                    TAYLOR_FRITZ: 1.40,
                },
                'score': [(6, 4), (6, 7), (6, 4)],
                'prediction': TAYLOR_FRITZ,
                'bet': 8,
            },
            {
                'round': 32,
                'players': [
                    CEDRIC_MARCEL_STEBE,
                    BERNARD_TOMIC,
                ],
                'odds': {
                    CEDRIC_MARCEL_STEBE: 1.28,
                    BERNARD_TOMIC: 3.60,
                },
                'score': [(6, 2), (3, 6), (6, 2)],
                'prediction': CEDRIC_MARCEL_STEBE,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    MILOS_RAONIC,
                    DENIS_ISTOMIN,
                ],
                'odds': {
                    MILOS_RAONIC: 1.14,
                    DENIS_ISTOMIN: 5.50,
                },
                'score': [(6, 2), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    JORDAN_THOMPSON,
                ],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.45,
                    JORDAN_THOMPSON: 2.70,
                },
                'score': [(6, 2), (0, 0)],
                'retired': True,
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 11,
            },
            {
                'round': 32,
                'players': [
                    STEVE_JOHNSON,
                    HENRI_LAAKSONEN,
                ],
                'odds': {
                    STEVE_JOHNSON: 1.36,
                    HENRI_LAAKSONEN: 3.10,
                },
                'score': [(7, 6), (6, 4)],
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    KYLE_EDMUND,
                ],
                'odds': {
                    UGO_HUMBERT: 2.00,
                    KYLE_EDMUND: 1.80,
                },
                'score': [(6, 7), (6, 3), (6, 1)],
            },
            {
                'round': 32,
                'players': [
                    NOAH_RUBIN,
                    JASON_JUNG,
                ],
                'odds': {
                    NOAH_RUBIN: 2.10,
                    JASON_JUNG: 1.70,
                },
                'score': [(6, 3), (4, 3)],
                'retired': True,
            },
            {
                'round': 32,
                'players': [
                    REILLY_OPELKA,
                    ERNESTS_GULBIS,
                ],
                'odds': {
                    REILLY_OPELKA: 1.60,
                    ERNESTS_GULBIS: 2.30,
                },
                'score': [(6, 7), (6, 4), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    JACK_SOCK,
                    RADU_ALBOT,
                ],
                'odds': {
                    JACK_SOCK: 2.60,
                    RADU_ALBOT: 1.48,
                },
                'score': [(3, 6), (6, 3), (7, 6)],
                'prediction': RADU_ALBOT,
                'bet': 6,
            },

            # 2020-02-19
            {
                'round': 16,
                'players': [
                    SOONWOO_KWON,
                    RYAN_HARRISON,
                ],
                'odds': {
                    SOONWOO_KWON: 1.30,
                    RYAN_HARRISON: 3.40,
                },
                'score': [(6, 4), (3, 6), (7, 6)],
                'prediction': SOONWOO_KWON,
                'bet': 12,
            },
            {
                'round': 16,
                'players': [
                    BRANDON_NAKASHIMA,
                    CAMERON_NORRIE,
                ],
                'odds': {
                    BRANDON_NAKASHIMA: 1.90,
                    CAMERON_NORRIE: 1.90,
                },
                'score': [(7, 5), (6, 2)],
            },
            {
                'round': 16,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    NOAH_RUBIN,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.26,
                    NOAH_RUBIN: 3.80,
                },
                'score': [(6, 1), (6, 2)],
            },
            {
                'round': 16,
                'players': [
                    REILLY_OPELKA,
                    MACKENZIE_MCDONALD,
                ],
                'odds': {
                    REILLY_OPELKA: 1.45,
                    MACKENZIE_MCDONALD: 2.70,
                },
                'score': [(6, 3), (6, 4)],
            },

            # 2020-02-20
            {
                'round': 16,
                'players': [
                    UGO_HUMBERT,
                    MIOMIR_KECMANOVIC,
                ],
                'odds': {
                    UGO_HUMBERT: 2.20,
                    MIOMIR_KECMANOVIC: 1.65,
                },
                'score': [(6, 4), (7, 6)],
            },
            {
                'round': 16,
                'players': [
                    FRANCES_TIAFOE,
                    TOMMY_PAUL,
                ],
                'odds': {
                    FRANCES_TIAFOE: 2.00,
                    TOMMY_PAUL: 1.80,
                },
                'score': [(7, 5), (7, 6)],
                'prediction': TOMMY_PAUL,
                'bet': 9,
            },
            {
                'round': 16,
                'players': [
                    STEVE_JOHNSON,
                    JACK_SOCK,
                ],
                'odds': {
                    STEVE_JOHNSON: 1.45,
                    JACK_SOCK: 2.70,
                },
                'score': [(6, 4), (5, 7), (6, 1)],
            },
            {
                'round': 16,
                'players': [
                    MILOS_RAONIC,
                    CEDRIC_MARCEL_STEBE,
                ],
                'odds': {
                    MILOS_RAONIC: 1.14,
                    CEDRIC_MARCEL_STEBE: 5.50,
                },
                'score': [(7, 5), (6, 3)],
                'prediction': MILOS_RAONIC,
                'bet': 1,
            },

            # 2020-02-21
            {
                'round': 8,
                'players': [
                    UGO_HUMBERT,
                    FRANCES_TIAFOE,
                ],
                'odds': {
                    UGO_HUMBERT: 1.75,
                    FRANCES_TIAFOE: 2.05,
                },
                'score': [(6, 1), (6, 2)],
            },
            {
                'round': 8,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    BRANDON_NAKASHIMA,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.52,
                    BRANDON_NAKASHIMA: 2.50,
                },
                'score': [(3, 6), (7, 6), (6, 4)],
            },
            {
                'round': 8,
                'players': [
                    REILLY_OPELKA,
                    SOONWOO_KWON,
                ],
                'odds': {
                    REILLY_OPELKA: 1.55,
                    SOONWOO_KWON: 2.40,
                },
                'score': [(6, 3), (6, 4)],
                'prediction': REILLY_OPELKA,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    MILOS_RAONIC,
                    STEVE_JOHNSON,
                ],
                'odds': {
                    MILOS_RAONIC: 1.30,
                    STEVE_JOHNSON: 3.40,
                },
                'score': [(7, 6), (6, 3)],
            },

            # 2020-02-22
            {
                'round': 4,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    UGO_HUMBERT,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.25,
                    UGO_HUMBERT: 1.62,
                },
                'score': [(1, 6), (6, 4), (6, 0)],
                'prediction': UGO_HUMBERT,
                'bet': 1,
            },

            # 2020-02-23
            {
                'round': 4,
                'players': [
                    REILLY_OPELKA,
                    MILOS_RAONIC,
                ],
                'odds': {
                    REILLY_OPELKA: 2.70,
                    MILOS_RAONIC: 1.45,
                },
                'score': [(4, 6), (7, 6), (6, 3)],
                'prediction': REILLY_OPELKA,
                'bet': 2,
            },
            {
                'round': 2,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    REILLY_OPELKA,
                ],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.40,
                    REILLY_OPELKA: 1.55,
                },
                'score': [(1, 6), (6, 4), (6, 0)],
                'prediction': REILLY_OPELKA,
                'bet': 1,
            },
        ]
    },

    ###############################################################################
    # Active
    ###############################################################################

    {
        'location': DUBAI,
        'date': '2020-02-29',
        'matches': [

            # 2020-02-24
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    KAREN_KHACHANOV,
                ],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 3.00,
                    KAREN_KHACHANOV: 1.38,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    PHILIPP_KOHLSCHREIBER,
                    MOHAMED_SAFWAT,
                ],
                'odds': {
                    PHILIPP_KOHLSCHREIBER: 1.26,
                    MOHAMED_SAFWAT: 3.80,
                },
                'prediction': PHILIPP_KOHLSCHREIBER,
                'bet': 10,
            },
            {
                'round': 32,
                'players': [
                    ANDREY_RUBLEV,
                    LORENZO_MUSETTI,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.10,
                    LORENZO_MUSETTI: 6.50,
                },
                'prediction': ANDREY_RUBLEV,
                'bet': 9,
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    MALEK_JAZIRI,
                ],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    MALEK_JAZIRI: 21.00,
                },
            },
            {
                'round': 32,
                'players': [
                    LLOYD_HARRIS,
                    RICHARD_GASQUET,
                ],
                'odds': {
                    LLOYD_HARRIS: 2.30,
                    RICHARD_GASQUET: 1.60,
                },
            },
            {
                'round': 32,
                'players': [
                    GAEL_MONFILS,
                    MARTON_FUCSOVICS,
                ],
                'odds': {
                    GAEL_MONFILS: 1.30,
                    MARTON_FUCSOVICS: 3.40,
                },
            },
        ],
    },

    {
        'location': ACAPULCO,
        'date': '2020-02-29',
        'matches': [

            # 2020-02-24
            {
                'round': 512,
                'players': [
                    DANIEL_ALTMAIER,
                    JASON_JUNG,
                ],
                'odds': {
                    DANIEL_ALTMAIER: 2.35,
                    JASON_JUNG: 1.55,
                },
                'score': [(6, 2), (6, 3)],
            },
            {
                'round': 256,
                'players': [
                    DAMIR_DZUMHUR,
                    ALEX_BOLT,
                ],
                'odds': {
                    DAMIR_DZUMHUR: 1.46,
                    ALEX_BOLT: 2.60,
                },
                'score': [(6, 1), (6, 4)],
                'prediction': DAMIR_DZUMHUR,
                'bet': 6,
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    DANIEL_ELAHI_GALAN,
                ],
                'odds': {
                    TOMMY_PAUL: 1.24,
                    DANIEL_ELAHI_GALAN: 3.80,
                },
                'score': [(7, 6), (1, 0)],
                'retired': True,
                'prediction': TOMMY_PAUL,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    TARO_DANIEL,
                    MARCOS_GIRON,
                ],
                'odds': {
                    TARO_DANIEL: 1.40,
                    MARCOS_GIRON: 2.80,
                },
                'score': [(6, 3), (4, 3)],
                'retired': True,
                'prediction': TARO_DANIEL,
                'bet': 2,
            },

            # 2020-02-25
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    ADRIAN_MANNARINO,
                ],
                'odds': {
                    CAMERON_NORRIE: 2.05,
                    ADRIAN_MANNARINO: 1.75,
                },
            },
            {
                'round': 32,
                'players': [
                    ALEX_DE_MINAUR,
                    MIOMIR_KECMANOVIC,
                ],
                'odds': {
                    ALEX_DE_MINAUR: 1.85,
                    MIOMIR_KECMANOVIC: 1.95,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 13,
            },
            {
                'round': 32,
                'players': [
                    TOMMY_PAUL,
                    MACKENZIE_MCDONALD,
                ],
                'odds': {
                    TOMMY_PAUL: 1.40,
                    MACKENZIE_MCDONALD: 2.90,
                },
            },
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    FRANCES_TIAFOE,
                ],
                'odds': {
                    STAN_WAWRINKA: 1.42,
                    FRANCES_TIAFOE: 2.80,
                },
            },
            {
                'round': 32,
                'players': [
                    KYLE_EDMUND,
                    FELICIANO_LOPEZ,
                ],
                'odds': {
                    KYLE_EDMUND: 1.30,
                    FELICIANO_LOPEZ: 3.40,
                },
                'prediction': KYLE_EDMUND,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    MARCOS_GIRON,
                    GERARDO_LOPEZ_VILLASENOR,
                ],
                'odds': {
                    MARCOS_GIRON: 1.10,
                    GERARDO_LOPEZ_VILLASENOR: 6.50,
                },
                'prediction': MARCOS_GIRON,
                'bet': 10,
            },
        ],
    },

    {
        'location': SANTIAGO,
        'date': '2020-02-29',
        'matches': [

            # 2020-02-23
            {
                'round': 256,
                'players': [
                    MARTIN_KLIZAN,
                    ORLANDO_LUZ,
                ],
                'odds': {
                    MARTIN_KLIZAN: 1.40,
                    ORLANDO_LUZ: 2.80,
                },
                'prediction': MARTIN_KLIZAN,
                'bet': 9,
            },
            {
                'round': 256,
                'players': [
                    JUAN_PABLO_VARILLAS,
                    RENZO_OLIVO,
                ],
                'odds': {
                    JUAN_PABLO_VARILLAS: 1.40,
                    RENZO_OLIVO: 2.80,
                },
            },
            {
                'round': 256,
                'players': [
                    FILIP_HORANSKY,
                    PEDRO_SAKAMOTO,
                ],
                'odds': {
                    FILIP_HORANSKY: 1.46,
                    PEDRO_SAKAMOTO: 2.60,
                },
                'prediction': FILIP_HORANSKY,
                'bet': 3,
            },
            {
                'round': 256,
                'players': [
                    CARLOS_TABERNER,
                    ANDREA_COLLARINI,
                ],
                'odds': {
                    CARLOS_TABERNER: 1.44,
                    ANDREA_COLLARINI: 2.70,
                },
            },
        ]
    }

]




