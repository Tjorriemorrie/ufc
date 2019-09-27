from men import *
from location import *

# acc   roi     profit  desc
# 71.4  19.9    1435    2019 metz                           (1, 1672), (4, 872), (3, 412), (2, 154)
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

            # 2019-09-20
            {
                'round': 8,
                'players': [
                    ALJAZ_BEDENE,
                    PABLO_CARRENO_BUSTA,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    ALJAZ_BEDENE: 2.70,
                    PABLO_CARRENO_BUSTA: 1.45,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    BENOIT_PAIRE,
                    GREGOIRE_BARRERE,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    BENOIT_PAIRE: 1.48,
                    GREGOIRE_BARRERE: 2.60,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    LUCAS_POUILLE,
                    FILIP_KRAJINOVIC,
                ],
                'score': [(4, 6), (7, 5), (6, 2)],
                'odds': {
                    LUCAS_POUILLE: 1.65,
                    FILIP_KRAJINOVIC: 2.20,
                },
                'prediction': LUCAS_POUILLE,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    JO_WILFRIED_TSONGA,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(5, 7), (6, 3), (4, 1)],
                'retired': True,
                'odds': {
                    JO_WILFRIED_TSONGA: 1.45,
                    NIKOLOZ_BASILASHVILI: 2.70,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 0,  # refunded 3,
            },

            # 2019-09-21
            {
                'round': 4,
                'players': [
                    ALJAZ_BEDENE,
                    BENOIT_PAIRE,
                ],
                'score': [(4, 6), (6, 1), (6, 2)],
                'odds': {
                    ALJAZ_BEDENE: 1.80,
                    BENOIT_PAIRE: 2.00,
                },
                'prediction': ALJAZ_BEDENE,
                'bet': 4,
            },
            {
                'round': 4,
                'players': [
                    JO_WILFRIED_TSONGA,
                    LUCAS_POUILLE,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.70,
                    LUCAS_POUILLE: 2.10,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 3,
            },

            # 2019-09-22
            {
                'round': 2,
                'players': [
                    JO_WILFRIED_TSONGA,
                    ALJAZ_BEDENE,
                ],
                'score': [(6, 7), (7, 6), (6, 3)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.36,
                    ALJAZ_BEDENE: 3.10,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 1,
            }
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

            # 2019-09-20
            {
                'round': 8,
                'players': [
                    BORNA_CORIC,
                    CASPER_RUUD,
                ],
                'score': [(3, 6), (7, 5), (6, 3)],
                'odds': {
                    BORNA_CORIC: 1.58,
                    CASPER_RUUD: 2.35,
                },
            },
            {
                'round': 8,
                'players': [
                    JOAO_SOUSA,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    JOAO_SOUSA: 1.85,
                    MIKHAIL_KUKUSHKIN: 1.95,
                },
                'prediction': JOAO_SOUSA,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    EGOR_GERASIMOV,
                    MATTEO_BERRETTINI,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    EGOR_GERASIMOV: 3.60,
                    MATTEO_BERRETTINI: 1.28,
                },
                'prediction': MATTEO_BERRETTINI,
                'bet': 2,
            },
            {
                'round': 8,
                'players': [
                    DANIIL_MEDVEDEV,
                    ANDREY_RUBLEV,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.24,
                    ANDREY_RUBLEV: 4.00,
                },
            },

            # 2019-09-21
            {
                'round': 4,
                'players': [
                    BORNA_CORIC,
                    JOAO_SOUSA,
                ],
                'score': [(3, 6), (7, 6), (6, 1)],
                'odds': {
                    BORNA_CORIC: 1.70,
                    JOAO_SOUSA: 2.10,
                },
            },
            {
                'round': 4,
                'players': [
                    DANIIL_MEDVEDEV,
                    EGOR_GERASIMOV,
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.14,
                    EGOR_GERASIMOV: 5.50,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 2,
            },

            # 2019-09-22
            {
                'round': 2,
                'players': [
                    DANIIL_MEDVEDEV,
                    BORNA_CORIC,
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.22,
                    BORNA_CORIC: 4.20,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 2,
            }
        ]
    },

    ###############################################################################
    # Active
    ###############################################################################

    {
        'location': CHENGDU,
        'date': '2019-09-29',
        'matches': [
            # 2019-09-23
            {
                'round': 512,
                'players': [
                    LUKE_SAVILLE,
                    ANDREW_HARRIS,
                ],
                'score': [(6, 4), (7, 5)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    JAMES_DUCKWORTH,
                    HARRY_BOURCHIER,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JAMES_DUCKWORTH: 1.12,
                    HARRY_BOURCHIER: 5.95
                }
            },
            {
                'round': 512,
                'players': [
                    JASON_JUNG,
                    AKIRA_SANTILLAN
                ],
                'score': [(7, 5), (3, 6), (7, 6)],
                'odds': {
                    JASON_JUNG: 1.77,
                    AKIRA_SANTILLAN: 1.80,
                }
            },
            {
                'round': 512,
                'players': [
                    LLOYD_HARRIS,
                    JIE_CUI
                ],
                'score': [(6, 7), (6, 3), (6, 0)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    DENIS_ISTOMIN,
                    BERNARD_TOMIC
                ],
                'score': [(6, 1), (3, 1)],
                'retired': True,
                'odds': {
                    DENIS_ISTOMIN: 1.80,
                    BERNARD_TOMIC: 1.87
                }
            },
            {
                'round': 512,
                'players': [
                    BRADLEY_KLAHN,
                    HIROKI_MORIYA
                ],
                'score': [(4, 6), (6, 3), (6, 4)],
                'odds': {
                    BRADLEY_KLAHN: 1.28,
                    HIROKI_MORIYA: 3.30,
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXEI_POPYRIN,
                    XIN_GAO
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    ALEXEI_POPYRIN: 1.02,
                    XIN_GAO: 12.50
                }
            },
            {
                'round': 512,
                'players': [
                    KAMIL_MAJCHRZAK,
                    MAX_PURCELL
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.30,
                    MAX_PURCELL: 3.45
                }
            },

            # 2019-09-24
            {
                'round': 256,
                'players': [
                    JASON_JUNG,
                    LUKE_SAVILLE
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JASON_JUNG: 1.29,
                    LUKE_SAVILLE: 3.20
                }
            },
            {
                'round': 256,
                'players': [
                    BRADLEY_KLAHN,
                    LLOYD_HARRIS
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    BRADLEY_KLAHN: 1.70,
                    LLOYD_HARRIS: 1.86
                }
            },
            {
                'round': 256,
                'players': [
                    ALEXEI_POPYRIN,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 3), (3, 6), (7, 5)],
                'odds': {
                    ALEXEI_POPYRIN: 1.63,
                    DENIS_ISTOMIN: 2.10,
                }
            },
            {
                'round': 256,
                'players': [
                    KAMIL_MAJCHRZAK,
                    JAMES_DUCKWORTH
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.71,
                    JAMES_DUCKWORTH: 1.91
                }
            },

            # 2019-09-25
            {
                'round': 32,
                'players': [
                    CHRISTIAN_GARIN,
                    KYLE_EDMUND,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    CHRISTIAN_GARIN: 2.90,
                    KYLE_EDMUND: 1.40,
                },
            },
            {
                'round': 32,
                'players': [
                    BRADLEY_KLAHN,
                    JASON_JUNG,
                ],
                'score': [(4, 6), (6, 3), (7, 6)],
                'odds': {
                    BRADLEY_KLAHN: 1.60,
                    JASON_JUNG: 2.25,
                },
            },
            {
                'round': 32,
                'players': [
                    DANIEL_EVANS,
                    Y_BAI,
                ],
                'score': [(6, 3), (4, 6), (7, 6)],
                'odds': {
                    DANIEL_EVANS: 1.16,
                    Y_BAI: 5.00,
                },
                'prediction': DANIEL_EVANS,
                'bet': 1,
            },

            # 2019-09-24
            {
                'round': 32,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    RADU_ALBOT,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.55,
                    RADU_ALBOT: 2.40,
                },
            },
            {
                'round': 32,
                'players': [
                    DUSAN_LAJOVIC,
                    JUAN_IGNACIO_LONDERO,
                ],
                'score': [(6, 2), (4, 6), (6, 4)],
                'odds': {
                    DUSAN_LAJOVIC: 1.70,
                    JUAN_IGNACIO_LONDERO: 2.10,
                },
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    ALEXEI_POPYRIN,
                ],
                'score': [(6, 2), (7, 5)],
                'odds': {
                    FERNANDO_VERDASCO: 1.70,
                    ALEXEI_POPYRIN: 2.10,
                },
            },
            {
                'round': 32,
                'players': [
                    KAMIL_MAJCHRZAK,
                    MARTON_FUCSOVICS,
                ],
                'score': [(4, 6), (6, 4), (6, 2)],
                'odds': {
                    KAMIL_MAJCHRZAK: 1.75,
                    MARTON_FUCSOVICS: 2.05,
                },
            },
            {
                'round': 32,
                'players': [
                    EGOR_GERASIMOV,
                    ZHE_LI,
                ],
                'score': [(4, 6), (6, 2), (6, 3)],
                'odds': {
                    EGOR_GERASIMOV: 1.32,
                    ZHE_LI: 3.30,
                },
                'prediction': EGOR_GERASIMOV,
                'bet': 4,
            },

            # 2019-09-25
            {
                'round': 32,
                'players': [
                    DENIS_SHAPOVALOV,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.42,
                    RICARDAS_BERANKIS: 2.80,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    HYEON_CHUNG,
                ],
                'score': [(1, 6), (6, 3), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 2.70,
                    HYEON_CHUNG: 1.45,
                },
                'prediction': HYEON_CHUNG,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    JORDAN_THOMPSON,
                    VASEK_POSPISIL,
                ],
                'score': [(6, 3), (3, 6), (7, 5)],
                'odds': {
                    JORDAN_THOMPSON: 1.75,
                    VASEK_POSPISIL: 2.05,
                },
                'prediction': JORDAN_THOMPSON,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_BUBLIK,
                    TAYLOR_FRITZ
                ],
                'score': [(4, 6), (7, 5), (7, 5)],
                'odds': {
                    ALEXANDER_BUBLIK: 3.10,
                    TAYLOR_FRITZ: 1.30
                }
            },

            # 2019-09-26
            {
                'round': 16,
                'players': [
                    GRIGOR_DIMITROV,
                    DANIEL_EVANS,
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    GRIGOR_DIMITROV: 1.48,
                    DANIEL_EVANS: 2.60,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    BENOIT_PAIRE,
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.45,
                    BENOIT_PAIRE: 2.70,
                },
            },
            {
                'round': 16,
                'players': [
                    CHRISTIAN_GARIN,
                    FERNANDO_VERDASCO,
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    CHRISTIAN_GARIN: 2.30,
                    FERNANDO_VERDASCO: 1.60,
                },
                'prediction': FERNANDO_VERDASCO,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_BUBLIK,
                    JORDAN_THOMPSON,
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.40,
                    JORDAN_THOMPSON: 1.55,
                },
                'prediction': JORDAN_THOMPSON,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    DENIS_SHAPOVALOV,
                    BRADLEY_KLAHN,
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.24,
                    BRADLEY_KLAHN: 4.00,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    JOAO_SOUSA,
                    FELIX_AUGER_ALIASSIME,
                ],
                'score': [(6, 4), (6, 7), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 1.95,
                    FELIX_AUGER_ALIASSIME: 1.85,
                },
            },
            {
                'round': 16,
                'players': [
                    EGOR_GERASIMOV,
                    JOHN_ISNER,
                ],
                'score': [(6, 7), (7, 6), (7, 6)],
                'odds': {
                    EGOR_GERASIMOV: 2.50,
                    JOHN_ISNER: 1.52,
                },
                'prediction': JOHN_ISNER,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    LLOYD_HARRIS,
                    DUSAN_LAJOVIC,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    LLOYD_HARRIS: 2.30,
                    DUSAN_LAJOVIC: 1.60,
                },
                'prediction': DUSAN_LAJOVIC,
                'bet': 6,
            },

            #
            {
                'round': 8,
                'players': [
                    ALEXANDER_BUBLIK,
                    GRIGOR_DIMITROV,
                ],
                'odds': {
                    ALEXANDER_BUBLIK: 3.60,
                    GRIGOR_DIMITROV: 1.28,
                },
            },
            {
                'round': 8,
                'players': [
                    LLOYD_HARRIS,
                    JOAO_SOUSA,
                ],
                'odds': {
                    LLOYD_HARRIS: 2.60,
                    JOAO_SOUSA: 1.48,
                },
            },
            {
                'round': 8,
                'players': [
                    EGOR_GERASIMOV,
                    DENIS_SHAPOVALOV,
                ],
                'odds': {
                    EGOR_GERASIMOV: 2.60,
                    DENIS_SHAPOVALOV: 1.48,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    CHRISTIAN_GARIN,
                ],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.42,
                    CHRISTIAN_GARIN: 2.80,
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 1,
            },

            #
        ]
    },

    {
        'location': ZHUHAI,
        'date': '2019-09-29',
        'matches': [

            # 2019-09-23
            {
                'round': 512,
                'players': [
                    JIRI_VESELY,
                    YASUTAKA_UCHIYAMA,
                ],
                'score': [(6, 7), (7, 6), (7, 6)],
                'odds': {
                    JIRI_VESELY: 1.56,
                    YASUTAKA_UCHIYAMA: 2.20,
                }
            },
            {
                'round': 512,
                'players': [
                    YUICHI_SUGITA,
                    ZHAO_ZHAO
                ],
                'score': [(6, 0), (6, 0)],
                'odds': {
                    YUICHI_SUGITA: 1.01,
                    ZHAO_ZHAO: 11.00
                }
            },
            {
                'round': 512,
                'players': [
                    HENRI_LAAKSONEN,
                    RUNHAO_HUA,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    HENRI_LAAKSONEN: 1.12,
                    RUNHAO_HUA: 4.50
                }
            },
            {
                'round': 512,
                'players': [
                    BRAYDEN_SCHNUR,
                    GONCALO_OLIVEIRA,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    BRAYDEN_SCHNUR: 1.30,
                    GONCALO_OLIVEIRA: 3.20
                }
            },
            {
                'round': 512,
                'players': [
                    TATSUMA_ITO,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    TATSUMA_ITO: 2.00,
                    THOMAS_FABBIANO: 1.62
                }
            },
            {
                'round': 512,
                'players': [
                    DAMIR_DZUMHUR,
                    ALEX_BOLT
                ],
                'score': [(6, 4), (2, 6), (6, 4)],
                'odds': {
                    DAMIR_DZUMHUR: 1.33,
                    ALEX_BOLT: 3.00
                }
            },
            {
                'round': 512,
                'players': [
                    DOMINIK_KOEPFER,
                    YECONG_HE
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    DOMINIK_KOEPFER: 1.03,
                    YECONG_HE: 10.00
                }
            },
            {
                'round': 512,
                'players': [
                    SOONWOO_KWON,
                    MILIAAN_NIESTEN
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    SOONWOO_KWON: 1.03,
                    MILIAAN_NIESTEN: 9.00
                }
            },

            # 2019-09-24
            {
                'round': 256,
                'players': [
                    TATSUMA_ITO,
                    JIRI_VESELY
                ],
                'score': [(6, 4), (0, 0)],
                'retired': True,
                'odds': {
                    TATSUMA_ITO: 2.40,
                    JIRI_VESELY: 1.45
                }
            },
            {
                'round': 256,
                'players': [
                    DAMIR_DZUMHUR,
                    BRAYDEN_SCHNUR
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DAMIR_DZUMHUR: 1.40,
                    BRAYDEN_SCHNUR: 2.60
                }
            },
            {
                'round': 256,
                'players': [
                    DOMINIK_KOEPFER,
                    YUICHI_SUGITA
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    DOMINIK_KOEPFER: 1.45,
                    YUICHI_SUGITA: 2.35
                }
            },
            {
                'round': 256,
                'players': [
                    SOONWOO_KWON,
                    HENRI_LAAKSONEN
                ],
                'score': [(6, 2), (5, 7), (6, 4)],
                'odds': {
                    SOONWOO_KWON: 1.33,
                    HENRI_LAAKSONEN: 3.10
                }
            },

            # 2019-09-25
            {
                'round': 32,
                'players': [
                    DI_WU,
                    TATSUMA_ITO,
                ],
                'score': [(3, 6), (6, 3), (7, 5)],
                'odds': {
                    DI_WU: 2.25,
                    TATSUMA_ITO: 1.54
                }
            },
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    CAMERON_NORRIE: 1.50,
                    PETER_GOJOWCZYK: 2.40
                }
            },
            {
                'round': 32,
                'players': [
                    ADRIAN_MANNARINO,
                    ZE_ZHANG
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    ADRIAN_MANNARINO: 1.29,
                    ZE_ZHANG: 3.29
                }
            },
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    YOSHIHITO_NISHIOKA
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.35,
                    YOSHIHITO_NISHIOKA: 1.53
                }
            },

            # 2019-09-24
            {
                'round': 32,
                'players': [
                    PABLO_ANDUJAR,
                    STEVE_JOHNSON,
                ],
                'score': [(2, 6), (6, 2), (6, 1)],
                'odds': {
                    PABLO_ANDUJAR: 2.25,
                    STEVE_JOHNSON: 1.62,
                },
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    CASPER_RUUD,
                ],
                'score': [(6, 2), (0, 0)],
                'retired': True,
                'odds': {
                    MIOMIR_KECMANOVIC: 1.68,
                    CASPER_RUUD: 2.15,
                },
            },
            {
                'round': 32,
                'players': [
                    DAMIR_DZUMHUR,
                    MARCO_CECCHINATO,
                ],
                'score': [(5, 7), (6, 4), (6, 2)],
                'odds': {
                    DAMIR_DZUMHUR: 1.38,
                    MARCO_CECCHINATO: 3.00,
                },
            },
            {
                'round': 32,
                'players': [
                    ZHIZHEN_ZHANG,
                    DOMINIK_KOEPFER,
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    ZHIZHEN_ZHANG: 3.30,
                    DOMINIK_KOEPFER: 1.32,
                },
                'prediction': DOMINIK_KOEPFER,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    ALEX_DE_MINAUR,
                    JOHN_MILLMAN,
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    ALEX_DE_MINAUR: 1.48,
                    JOHN_MILLMAN: 2.60,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    ANDY_MURRAY,
                    TENNYS_SANDGREN,
                ],
                'score': [(6, 3), (6, 7), (6, 1)],
                'odds': {
                    ANDY_MURRAY: 1.75,
                    TENNYS_SANDGREN: 2.05,
                },
            },

            # 2019-09-25
            {
                'round': 32,
                'players': [
                    ANDREAS_SEPPI,
                    NICK_KYRGIOS
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    ANDREAS_SEPPI: 2.40,
                    NICK_KYRGIOS: 1.50
                }
            },
            {
                'round': 16,
                'players': [
                    SOONWOO_KWON,
                    LUCAS_POUILLE,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    SOONWOO_KWON: 2.15,
                    LUCAS_POUILLE: 1.68,
                },
                'prediction': LUCAS_POUILLE,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    MIOMIR_KECMANOVIC,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.15,
                    MIOMIR_KECMANOVIC: 1.68,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    GAEL_MONFILS,
                    CAMERON_NORRIE,
                ],
                'score': [(5, 7), (6, 3), (6, 4)],
                'odds': {
                    GAEL_MONFILS: 1.26,
                    CAMERON_NORRIE: 3.80,
                },
                'prediction': GAEL_MONFILS,
                'bet': 2,
            },

            # 2019-09-26
            {
                'round': 16,
                'players': [
                    ANDREAS_SEPPI,
                    ZHIZHEN_ZHANG,
                ],
                'score': [(7, 6), (4, 6), (7, 6)],
                'odds': {
                    ANDREAS_SEPPI: 1.38,
                    ZHIZHEN_ZHANG: 3.00,
                },
                'prediction': ANDREAS_SEPPI,
                'bet': 5,
            },
            {
                'round': 16,
                'players': [
                    DAMIR_DZUMHUR,
                    SOONWOO_KWON,
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    DAMIR_DZUMHUR: 2.30,
                    SOONWOO_KWON: 1.60,
                },
            },
            {
                'round': 16,
                'players': [
                    ADRIAN_MANNARINO,
                    STEFANOS_TSITSIPAS,
                ],
                'score': [(3, 6), (7, 5), (0, 0)],
                'retired': True,
                'odds': {
                    ADRIAN_MANNARINO: 3.60,
                    STEFANOS_TSITSIPAS: 1.28,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 0,  # refunded7,
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    PABLO_ANDUJAR,
                ],
                'score': [(7, 5), (7, 5)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.22,
                    PABLO_ANDUJAR: 4.20,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    DI_WU,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    BORNA_CORIC: 1.16,
                    DI_WU: 5.00,
                },
                'prediction': BORNA_CORIC,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    ALEX_DE_MINAUR,
                    ANDY_MURRAY,
                ],
                'score': [(4, 6), (6, 2), (6, 4)],
                'odds': {
                    ALEX_DE_MINAUR: 1.38,
                    ANDY_MURRAY: 3.00,
                },
                'prediction': ALEX_DE_MINAUR,
                'bet': 4,
            },

            #
            {
                'round': 8,
                'players': [
                    GAEL_MONFILS,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'odds': {
                    GAEL_MONFILS: 1.34,
                    ALBERT_RAMOS_VINOLAS: 3.20,
                },
            },
            {
                'round': 8,
                'players': [
                    ADRIAN_MANNARINO,
                    DAMIR_DZUMHUR,
                ],
                'odds': {
                    ADRIAN_MANNARINO: 1.80,
                    DAMIR_DZUMHUR: 2.00,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    ANDREAS_SEPPI,
                    ROBERTO_BAUTISTA_AGUT,
                ],
                'odds': {
                    ANDREAS_SEPPI: 4.00,
                    ROBERTO_BAUTISTA_AGUT: 1.24,
                },
            },

            #
        ]
    }
]
