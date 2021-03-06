from men import *
from location import *

DATA_2020_01 = [
    {
        'location': ATP_CUP,
        'date': '2020-01-12',
        'matches': [

            # 2020-01-03
            {
                'round': 512,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    MICHAIL_PERVOLARAKIS,
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.05,
                    MICHAIL_PERVOLARAKIS: 9.00,
                },
            },
            {
                'round': 512,
                'players': [
                    DENIS_SHAPOVALOV,
                    STEFANOS_TSITSIPAS,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    DENIS_SHAPOVALOV: 2.10,
                    STEFANOS_TSITSIPAS: 1.70,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 7,
            },
            {
                'round': 512,
                'players': [
                    STEVE_DARCIS,
                    ALEXANDER_COZBINOV,
                ],
                'score': [(6, 4), (6, 7), (7, 5)],
                'odds': {
                    STEVE_DARCIS: 1.02,
                    ALEXANDER_COZBINOV: 12.00,
                },
                'prediction': STEVE_DARCIS,
                'bet': 1,
            },
            {
                'round': 512,
                'players': [
                    DAVID_GOFFIN,
                    RADU_ALBOT,
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    DAVID_GOFFIN: 1.52,
                    RADU_ALBOT: 2.50,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    ALEX_DE_MINAUR,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(4, 6), (7, 6), (6, 2)],
                'odds': {
                    ALEX_DE_MINAUR: 2.15,
                    ALEXANDER_ZVEREV: 1.68,
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    NICK_KYRGIOS,
                    JAN_LENNARD_STRUFF,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 1.48,
                    JAN_LENNARD_STRUFF: 2.60,
                },
            },
            {
                'round': 512,
                'players': [
                    GRIGOR_DIMITROV,
                    DANIEL_EVANS,
                ],
                'score': [(2, 6), (6, 4), (6, 1)],
                'odds': {
                    GRIGOR_DIMITROV: 1.68,
                    DANIEL_EVANS: 2.15,
                },
            },
            {
                'round': 512,
                'players': [
                    CAMERON_NORRIE,
                    DIMITAR_KUZMANOV,
                ],
                'score': [(6, 2), (3, 6), (6, 2)],
                'odds': {
                    CAMERON_NORRIE: 1.14,
                    DIMITAR_KUZMANOV: 5.50,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    TAYLOR_FRITZ,
                    VIKTOR_DURASOVIC,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    TAYLOR_FRITZ: 1.09,
                    VIKTOR_DURASOVIC: 7.00,
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    CASPER_RUUD,
                    JOHN_ISNER,
                ],
                'score': [(6, 7), (7, 6), (7, 5)],
                'odds': {
                    CASPER_RUUD: 2.50,
                    JOHN_ISNER: 1.52,
                },
                'prediction': JOHN_ISNER,
                'bet': 5,
            },
            {
                'round': 512,
                'players': [
                    KAREN_KHACHANOV,
                    STEFANO_TRAVAGLIA,
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    KAREN_KHACHANOV: 1.16,
                    STEFANO_TRAVAGLIA: 5.00,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 6,
            },
            {
                'round': 512,
                'players': [
                    DANIIL_MEDVEDEV,
                    FABIO_FOGNINI,
                ],
                'score': [(1, 6), (6, 1), (6, 3)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.32,
                    FABIO_FOGNINI: 3.30,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 5,
            },

            # 2020-01-04
            {
                'round': 256,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    ALEKSANDRE_METREVELI,
                ],
                'score': [(6, 0), (6, 0)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.01,
                    ALEKSANDRE_METREVELI: 26.00,
                },
            },
            {
                'round': 256,
                'players': [
                    RAFAEL_NADAL,
                    NIKOLOZ_BASILASHVILI,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    RAFAEL_NADAL: 1.06,
                    NIKOLOZ_BASILASHVILI: 8.50,
                },
                'prediction': RAFAEL_NADAL,
                'bet': 5,
            },
            {
                'round': 256,
                'players': [
                    MARIN_CILIC,
                    DENNIS_NOVAK,
                ],
                'score': [(6, 7), (6, 4), (6, 4)],
                'odds': {
                    MARIN_CILIC: 1.36,
                    DENNIS_NOVAK: 3.10,
                },
                'prediction': MARIN_CILIC,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    BORNA_CORIC,
                    DOMINIC_THIEM,
                ],
                'score': [(7, 6), (2, 6), (6, 3)],
                'odds': {
                    BORNA_CORIC: 2.90,
                    DOMINIC_THIEM: 1.40,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    NOVAK_DJOKOVIC,
                    KEVIN_ANDERSON,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.09,
                    KEVIN_ANDERSON: 7.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 4,
            },
            {
                'round': 256,
                'players': [
                    DUSAN_LAJOVIC,
                    LLOYD_HARRIS,
                ],
                'score': [(3, 6), (7, 6), (6, 3)],
                'odds': {
                    DUSAN_LAJOVIC: 2.00,
                    LLOYD_HARRIS: 1.80,
                },
                'prediction': LLOYD_HARRIS,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    HUBERT_HURKACZ,
                    DIEGO_SCHWARTZMAN,
                ],
                'score': [(4, 6), (6, 2), (6, 3)],
                'odds': {
                    HUBERT_HURKACZ: 2.05,
                    DIEGO_SCHWARTZMAN: 1.75,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 8,
            },
            {
                'round': 256,
                'players': [
                    GUIDO_PELLA,
                    KAMIL_MAJCHRZAK,
                ],
                'score': [(6, 2), (2, 6), (6, 2)],
                'odds': {
                    GUIDO_PELLA: 1.52,
                    KAMIL_MAJCHRZAK: 2.50,
                },
                'prediction': GUIDO_PELLA,
                'bet': 7,
            },
            {
                'round': 256,
                'players': [
                    GAEL_MONFILS,
                    CHRISTIAN_GARIN,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    GAEL_MONFILS: 1.45,
                    CHRISTIAN_GARIN: 2.70,
                },
                'prediction': GAEL_MONFILS,
                'bet': 6,
            },
            {
                'round': 256,
                'players': [
                    BENOIT_PAIRE,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 7), (6, 3), (6, 3)],
                'odds': {
                    BENOIT_PAIRE: 1.52,
                    NICOLAS_JARRY: 2.50,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 6,
            },
            {
                'round': 256,
                'players': [
                    YOSHIHITO_NISHIOKA,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 0), (6, 1)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 1.52,
                    PABLO_CUEVAS: 2.50,
                },
                'prediction': YOSHIHITO_NISHIOKA,
                'bet': 8,
            },
            {
                'round': 256,
                'players': [
                    GO_SOEDA,
                    MARTIN_CUEVAS,
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    GO_SOEDA: 1.16,
                    MARTIN_CUEVAS: 5.00,
                },
            },

            # 2020-01-05
            {
                'round': 256,
                'players': [
                    STEVE_DARCIS,
                    CAMERON_NORRIE,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    STEVE_DARCIS: 3.40,
                    CAMERON_NORRIE: 1.30,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 1,
            },
            {
                'round': 256,
                'players': [
                    DANIEL_EVANS,
                    DAVID_GOFFIN,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DANIEL_EVANS: 3.30,
                    DAVID_GOFFIN: 1.32,
                },
                'prediction': DAVID_GOFFIN,
                'bet': 3,
            },
            {
                'round': 256,
                'players': [
                    ALEX_DE_MINAUR,
                    DENIS_SHAPOVALOV,
                ],
                'score': [(6, 7), (6, 4), (6, 2)],
                'odds': {
                    ALEX_DE_MINAUR: 1.85,
                    DENIS_SHAPOVALOV: 1.42,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    JOHN_MILLMAN,
                    FELIX_AUGER_ALIASSIME,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JOHN_MILLMAN: 1.55,
                    FELIX_AUGER_ALIASSIME: 2.40,
                },
                'prediction': NICK_KYRGIOS,
                'bet': 0,  # refunded 1,
            },
            {
                'round': 256,
                'players': [
                    GRIGOR_DIMITROV,
                    RADU_ALBOT,
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    GRIGOR_DIMITROV: 1.42,
                    RADU_ALBOT: 2.80,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 6,
            },
            {
                'round': 256,
                'players': [
                    DIMITAR_KUZMANOV,
                    ALEXANDER_COZBINOV,
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    DIMITAR_KUZMANOV: 1.10,
                    ALEXANDER_COZBINOV: 6.50,
                },
                'prediction': DIMITAR_KUZMANOV,
                'bet': 2,
            },
            {
                'round': 256,
                'players': [
                    KAREN_KHACHANOV,
                    TAYLOR_FRITZ,
                ],
                'score': [(3, 6), (7, 5), (6, 1)],
                'odds': {
                    KAREN_KHACHANOV: 1.45,
                    TAYLOR_FRITZ: 2.70,
                },
                'prediction': KAREN_KHACHANOV,
                'bet': 9,
            },
            {
                'round': 256,
                'players': [
                    DANIIL_MEDVEDEV,
                    JOHN_ISNER,
                ],
                'score': [(6, 3), (6, 1)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.28,
                    JOHN_ISNER: 3.60,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 5,
            },
            {
                'round': 256,
                'players': [
                    CASPER_RUUD,
                    FABIO_FOGNINI,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    CASPER_RUUD: 2.15,
                    FABIO_FOGNINI: 1.68,
                },
                'prediction': FABIO_FOGNINI,
                'bet': 5,
            },
            {
                'round': 256,
                'players': [
                    STEFANO_TRAVAGLIA,
                    VIKTOR_DURASOVIC,
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    STEFANO_TRAVAGLIA: 1.42,
                    VIKTOR_DURASOVIC: 2.80,
                },
                'prediction': STEFANO_TRAVAGLIA,
                'bet': 6,
            },
            {
                'round': 256,
                'players': [
                    JAN_LENNARD_STRUFF,
                    MICHAIL_PERVOLARAKIS,
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.01,
                    MICHAIL_PERVOLARAKIS: 17.00,
                },
            },
            {
                'round': 256,
                'players': [
                    STEFANOS_TSITSIPAS,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.42,
                    ALEXANDER_ZVEREV: 2.80,
                },
                'prediction': STEFANOS_TSITSIPAS,
                'bet': 1,
            },

            # 2020-01-06
            {
                'round': 128,
                'players': [
                    RAFAEL_NADAL,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    PABLO_CUEVAS: 17.00,
                },
            },
            {
                'round': 128,
                'players': [
                    NOVAK_DJOKOVIC,
                    GAEL_MONFILS,
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.14,
                    GAEL_MONFILS: 5.50,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    MARTIN_CUEVAS,
                ],
                'score': [(6, 1), (6, 2)],
            },
            {
                'round': 128,
                'players': [
                    DOMINIC_THIEM,
                    DIEGO_SCHWARTZMAN,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DOMINIC_THIEM: 1.48,
                    DIEGO_SCHWARTZMAN: 2.60,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 4,
            },
            {
                'round': 128,
                'players': [
                    MARIN_CILIC,
                    KAMIL_MAJCHRZAK,
                ],
                'score': [(7, 6), (6, 4)],
            },
            {
                'round': 128,
                'players': [
                    LLOYD_HARRIS,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    LLOYD_HARRIS: 1.60,
                    NICOLAS_JARRY: 2.30,
                },
                'prediction': LLOYD_HARRIS,
                'bet': 5,
            },
            {
                'round': 128,
                'players': [
                    HUBERT_HURKACZ,
                    BORNA_CORIC,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    HUBERT_HURKACZ: 2.15,
                    BORNA_CORIC: 1.68,
                },
                'prediction': BORNA_CORIC,
                'bet': 8,
            },
            {
                'round': 128,
                'players': [
                    KEVIN_ANDERSON,
                    CHRISTIAN_GARIN,
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    KEVIN_ANDERSON: 1.45,
                    CHRISTIAN_GARIN: 2.70,
                },
                'prediction': KEVIN_ANDERSON,
                'bet': 3,
            },
            {
                'round': 128,
                'players': [
                    GO_SOEDA,
                    ALEKSANDRE_METREVELI,
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    GO_SOEDA: 1.01,
                    ALEKSANDRE_METREVELI: 17.00,
                },
            },
            {
                'round': 128,
                'players': {
                    YOSHIHITO_NISHIOKA,
                    NIKOLOZ_BASILASHVILI,
                },
                'score': [(6, 2), (6, 3)],
                'odds': {
                    YOSHIHITO_NISHIOKA: 2.00,
                    NIKOLOZ_BASILASHVILI: 1.80,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 8,
            },
            {
                'round': 128,
                'players': [
                    DENNIS_NOVAK,
                    GUIDO_PELLA,
                ],
                'score': [(0, 6), (6, 4), (6, 4)],
                'odds': {
                    DENNIS_NOVAK: 2.25,
                    GUIDO_PELLA: 1.62,
                },
                'prediction': GUIDO_PELLA,
                'bet': 2,
            },
            {
                'round': 128,
                'players': [
                    BENOIT_PAIRE,
                    DUSAN_LAJOVIC,
                ],
                'score': [(6, 2), (6, 7), (6, 4)],
                'odds': {
                    BENOIT_PAIRE: 1.55,
                    DUSAN_LAJOVIC: 2.40,
                },
                'prediction': BENOIT_PAIRE,
                'bet': 2,
            },

            # 2020-01-07
            {
                'round': 64,
                'players': [
                    DANIEL_EVANS,
                    RADU_ALBOT,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DANIEL_EVANS: 1.40,
                    RADU_ALBOT: 2.90,
                },
                'prediction': DANIEL_EVANS,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    CAMERON_NORRIE,
                    ALEXANDER_COZBINOV,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    CAMERON_NORRIE: 1.03,
                    ALEXANDER_COZBINOV: 11.00,
                },
                'prediction': CAMERON_NORRIE,
                'bet': 9,
            },
            {
                'round': 64,
                'players': [
                    FABIO_FOGNINI,
                    JOHN_ISNER,
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    FABIO_FOGNINI: 1.95,
                    JOHN_ISNER: 1.85,
                },
                'prediction': JOHN_ISNER,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    STEFANO_TRAVAGLIA,
                    TAYLOR_FRITZ,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    STEFANO_TRAVAGLIA: 2.90,
                    TAYLOR_FRITZ: 1.40,
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    DAVID_GOFFIN,
                    GRIGOR_DIMITROV,
                ],
                'score': [(4, 6), (6, 2), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 2.20,
                    GRIGOR_DIMITROV: 1.65,
                },
                'prediction': GRIGOR_DIMITROV,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    DIMITAR_KUZMANOV,
                    STEVE_DARCIS,
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    DIMITAR_KUZMANOV: 2.70,
                    STEVE_DARCIS: 1.45,
                },
                'prediction': STEVE_DARCIS,
                'bet': 2,
            },
            {
                'round': 64,
                'players': [
                    DANIIL_MEDVEDEV,
                    CASPER_RUUD,
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    DANIIL_MEDVEDEV: 1.09,
                    CASPER_RUUD: 7.00,
                },
                'prediction': DANIIL_MEDVEDEV,
                'bet': 5,
            },
            {
                'round': 64,
                'players': [
                    NICK_KYRGIOS,
                    MICHAIL_PERVOLARAKIS,
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    NICK_KYRGIOS: 1.01,
                    MICHAIL_PERVOLARAKIS: 26.00,
                },
            },
            {
                'round': 64,
                'players': [
                    DENIS_SHAPOVALOV,
                    ALEXANDER_ZVEREV,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DENIS_SHAPOVALOV: 1.62,
                    ALEXANDER_ZVEREV: 2.25,
                },
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    JAN_LENNARD_STRUFF,
                    FELIX_AUGER_ALIASSIME,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.90,
                    FELIX_AUGER_ALIASSIME: 1.90,
                },
            },

            # 2020-01-08
            {
                'round': 32,
                'players': [
                    KEVIN_ANDERSON,
                    BENOIT_PAIRE,
                ],
                'score': [(2, 6), (7, 6), (7, 6)],
            },
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    LLOYD_HARRIS,
                ],
                'score': [(2, 6), (6, 2), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    NIKOLOZ_BASILASHVILI,
                    PABLO_CUEVAS,
                ],
                'score': [(6, 4), (1, 6), (6, 4)],
                'odds': {
                    NIKOLOZ_BASILASHVILI: 1.30,
                    PABLO_CUEVAS: 3.40,
                },
                'prediction': NIKOLOZ_BASILASHVILI,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    ALEKSANDRE_METREVELI,
                    FRANCO_RONCADELLI,
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    ALEKSANDRE_METREVELI: 1.06,
                    FRANCO_RONCADELLI: 8.50,
                },
                'prediction': ALEKSANDRE_METREVELI,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    GO_SOEDA,
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.06,
                    GO_SOEDA: 8.50,
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 11,
            },
            {
                'round': 32,
                'players': [
                    RAFAEL_NADAL,
                    YOSHIHITO_NISHIOKA,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    RAFAEL_NADAL: 1.01,
                    YOSHIHITO_NISHIOKA: 17.00,
                },
            },
            {
                'round': 32,
                'players': [
                    NOVAK_DJOKOVIC,
                    CHRISTIAN_GARIN,
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    NOVAK_DJOKOVIC: 1.01,
                    CHRISTIAN_GARIN: 14.00,
                },
                'prediction': NOVAK_DJOKOVIC,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    DUSAN_LAJOVIC,
                    NICOLAS_JARRY,
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    DUSAN_LAJOVIC: 1.75,
                    NICOLAS_JARRY: 2.05,
                },
                'prediction': DUSAN_LAJOVIC,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    DOMINIC_THIEM,
                ],
                'score': [(3, 6), (6, 4), (7, 6)],
                'odds': {
                    HUBERT_HURKACZ: 2.25,
                    DOMINIC_THIEM: 1.62,
                },
                'prediction': DOMINIC_THIEM,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    KACPER_ZUK,
                    DENNIS_NOVAK,
                ],
                'score': [(5, 7), (7, 6), (6, 3)],
                'odds': {
                    KACPER_ZUK: 3.60,
                    DENNIS_NOVAK: 1.28,
                },
                'prediction': DENNIS_NOVAK,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    GUIDO_PELLA,
                    MARIN_CILIC,
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    GUIDO_PELLA: 2.80,
                    MARIN_CILIC: 1.42,
                },
                'prediction': MARIN_CILIC,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    BORNA_CORIC,
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 1.68,
                    BORNA_CORIC: 2.15,
                },
                'prediction': DIEGO_SCHWARTZMAN,
                'bet': 2,
            },
        ]
    },

    {
        'location': DOHA,
        'date': '2020-01-11',
        'matches': [

            # 2020-01-06
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    JORDAN_THOMPSON,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.65,
                    JORDAN_THOMPSON: 2.20,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_BUBLIK,
                    ADRIAN_MANNARINO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    ALEXANDER_BUBLIK: 2.15,
                    ADRIAN_MANNARINO: 1.68,
                },
                'prediction': ADRIAN_MANNARINO,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    MIKAEL_YMER,
                ],
                'score': [(3, 6), (6, 4), (6, 3)],
                'odds': {
                    ALJAZ_BEDENE: 1.95,
                    MIKAEL_YMER: 1.85,
                },
                'prediction': MIKAEL_YMER,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    GREGOIRE_BARRERE,
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    JEREMY_CHARDY: 1.48,
                    GREGOIRE_BARRERE: 2.60,
                },
                'prediction': JEREMY_CHARDY,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    CORENTIN_MOUTET,
                    TENNYS_SANDGREN,
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    CORENTIN_MOUTET: 1.55,
                    TENNYS_SANDGREN: 2.40,
                },
                'prediction': CORENTIN_MOUTET,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    PABLO_ANDUJAR,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    FERNANDO_VERDASCO: 1.28,
                    PABLO_ANDUJAR: 2.40,
                },
                'prediction': FERNANDO_VERDASCO,
                'bet': 12,
            },
            {
                'round': 32,
                'players': [
                    FILIP_KRAJINOVIC,
                    KYLE_EDMUND,
                ],
                'score': [(4, 6), (6, 3), (6, 3)],
                'odds': {
                    FILIP_KRAJINOVIC: 2.20,
                    KYLE_EDMUND: 1.65,
                },
                'prediction': KYLE_EDMUND,
                'bet': 8,
            },

            # 2020-01-07
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    MALEK_JAZIRI,
                ],
                'score': [(6, 0), (6, 3)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.20,
                    MALEK_JAZIRI: 4.40,
                },
            },
            {
                'round': 32,
                'players': [
                    CEM_ILKEL,
                    RICARDAS_BERANKIS,
                ],
                'score': [(6, 2), (4, 6), (6, 2)],
                'odds': {
                    CEM_ILKEL: 4.20,
                    RICARDAS_BERANKIS: 1.22,
                },
            },
            {
                'round': 32,
                'players': [
                    MARTON_FUCSOVICS,
                    FRANCES_TIAFOE,
                ],
                'score': [(6, 4), (4, 6), (6, 4)],
                'odds': {
                    MARTON_FUCSOVICS: 2.00,
                    FRANCES_TIAFOE: 1.80,
                },
                'prediction': FRANCES_TIAFOE,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    LASLO_DJERE,
                    LORENZO_SONEGO,
                ],
                'score': [(6, 1), (3, 6), (6, 2)],
                'odds': {
                    LASLO_DJERE: 3.10,
                    LORENZO_SONEGO: 1.36,
                },
                'prediction': LORENZO_SONEGO,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    ALJAZ_BEDENE,
                    ALEXANDER_BUBLIK,
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    ALJAZ_BEDENE: 1.70,
                    ALEXANDER_BUBLIK: 2.10,
                },
                'prediction': ALJAZ_BEDENE,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    STAN_WAWRINKA,
                    JEREMY_CHARDY,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STAN_WAWRINKA: 1.28,
                    JEREMY_CHARDY: 3.60,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    MARCO_CECCHINATO,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.48,
                    MARCO_CECCHINATO: 2.60,
                },
                'prediction': PIERRE_HUGUES_HERBERT,
                'bet': 2,
            },

            # 2020-01-08
            {
                'round': 16,
                'players': [
                    MIOMIR_KECMANOVIC,
                    JO_WILFRIED_TSONGA,
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.70,
                    JO_WILFRIED_TSONGA: 1.45,
                },
                'prediction': JO_WILFRIED_TSONGA,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    MIKHAIL_KUKUSHKIN,
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    ANDREY_RUBLEV: 1.26,
                    MIKHAIL_KUKUSHKIN: 3.80,
                },
            },
            {
                'round': 16,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    LASLO_DJERE,
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.34,
                    LASLO_DJERE: 3.20,
                },
                'prediction': PIERRE_HUGUES_HERBERT,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    FERNANDO_VERDASCO,
                    FILIP_KRAJINOVIC,
                ],
                'score': [(7, 5), (4, 6), (6, 0)],
                'odds': {
                    FERNANDO_VERDASCO: 2.40,
                    FILIP_KRAJINOVIC: 1.55,
                },
            },
            {
                'round': 16,
                'players': [
                    MARTON_FUCSOVICS,
                    CEM_ILKEL,
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    MARTON_FUCSOVICS: 1.18,
                    CEM_ILKEL: 4.60,
                },
                'prediction': MARTON_FUCSOVICS,
                'bet': 7,
            },
            {
                'round': 16,
                'players': [
                    CORENTIN_MOUTET,
                    MILOS_RAONIC,
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    CORENTIN_MOUTET: 3.80,
                    MILOS_RAONIC: 1.26,
                },
                'prediction': MILOS_RAONIC,
                'bet': 7,
            },

            # 2020-01-09
            {
                'round': 8,
                'players': [
                    MIOMIR_KECMANOVIC,
                    MARTON_FUCSOVICS,
                ],
                'score': [(6, 2), (6, 0)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.65,
                    MARTON_FUCSOVICS: 2.20,
                },
                'prediction': MIOMIR_KECMANOVIC,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    ANDREY_RUBLEV,
                    PIERRE_HUGUES_HERBERT,
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 1.22,
                    PIERRE_HUGUES_HERBERT: 4.20,
                },
            },
            {
                'round': 8,
                'players': [
                    STAN_WAWRINKA,
                    ALJAZ_BEDENE,
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STAN_WAWRINKA: 1.28,
                    ALJAZ_BEDENE: 3.60,
                },
                'prediction': STAN_WAWRINKA,
                'bet': 9,
            },
            {
                'round': 8,
                'players': [
                    CORENTIN_MOUTET,
                    FERNANDO_VERDASCO,
                ],
                'odds': {
                    CORENTIN_MOUTET: 2.35,
                    FERNANDO_VERDASCO: 1.58,
                },
                'score': [(6, 4), (4, 6), (6, 4)],
                'prediction': FERNANDO_VERDASCO,
                'bet': 2,
            },

            # 2020-10-11
            {
                'round': 2,
                'players': [
                    ANDREY_RUBLEV,
                    CORENTIN_MOUTET,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.20,
                    CORENTIN_MOUTET: 4.40,
                },
                'score': [(6, 2), (7, 6)],
            }
        ]
    },

    {
        'location': ADELAIDE,
        'date': '2020-01-18',
        'matches': [

            # 2020-01-11
            {
                'round': 64,
                'players': [
                    NICOLAS_JARRY,
                    JOHN_PATRICK_SMITH,
                ],
                'odds': {
                    NICOLAS_JARRY: 1.55,
                    JOHN_PATRICK_SMITH: 2.40,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': NICOLAS_JARRY,
                'bet': 4,
            },
            {
                'round': 64,
                'players': [
                    TOMMY_PAUL,
                    MATTHEW_CHRISTOPHER_ROMIOS,
                ],
                'odds': {
                    TOMMY_PAUL: 1.02,
                    MATTHEW_CHRISTOPHER_ROMIOS: 12.00,
                },
                'score': [(6, 2), (6, 2)],
            },

            # 2020-01-12
            {
                'round': 64,
                'players': [
                    ANDREW_HARRIS,
                    STEPHANE_ROBERT,
                ],
                'odds': {
                    ANDREW_HARRIS: 1.10,
                    STEPHANE_ROBERT: 6.50,
                },
                'score': [(7, 5), (6, 4)],
            },
            {
                'round': 64,
                'players': [
                    FEDERICO_DELBONIS,
                    SALVATORE_CARUSO,
                ],
                'odds': {
                    FEDERICO_DELBONIS: 2.05,
                    SALVATORE_CARUSO: 1.75,
                },
                'score': [(7, 6), (7, 6)],
            },
            {
                'round': 64,
                'players': [
                    GREGOIRE_BARRERE,
                    JAUME_MUNAR,
                ],
                'odds': {
                    GREGOIRE_BARRERE: 1.62,
                    JAUME_MUNAR: 2.25,
                },
                'score': [(6, 7), (6, 4), (6, 4)],
                'prediction': GREGOIRE_BARRERE,
                'bet': 7,
            },
            {
                'round': 64,
                'players': [
                    ALEXANDER_BUBLIK,
                    TAYLOR_FRITZ,
                ],
                'odds': {
                    ALEXANDER_BUBLIK: 2.50,
                    TAYLOR_FRITZ: 1.52,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': TAYLOR_FRITZ,
                'bet': 3,
            },
            {
                'round': 64,
                'players': [
                    TOMMY_PAUL,
                    NICOLAS_JARRY,
                ],
                'odds': {
                    TOMMY_PAUL: 1.55,
                    NICOLAS_JARRY: 2.40,
                },
                'score': [(6, 3), (6, 2)],
            },
            {
                'round': 64,
                'players': [
                    PABLO_CUEVAS,
                    REILLY_OPELKA,
                ],
                'odds': {
                    PABLO_CUEVAS: 3.40,
                    REILLY_OPELKA: 1.30,
                },
                'score': [(5, 7), (7, 6), (7, 6)],
                'prediction': REILLY_OPELKA,
                'bet': 1,
            },
            {
                'round': 64,
                'players': [
                    LASLO_DJERE,
                    ALEXEI_POPYRIN,
                ],
                'odds': {
                    LASLO_DJERE: 3.10,
                    ALEXEI_POPYRIN: 1.36,
                },
                'score': [(7, 6), (3, 6), (6, 4)],
                'prediction': ALEXEI_POPYRIN,
                'bet': 7,
            },

            # 2020-01-13
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    GILLES_SIMON,
                ],
                'odds': {
                    JEREMY_CHARDY: 1.70,
                    GILLES_SIMON: 2.10,
                },
                'score': [(6, 3), (7, 5)],
                'prediction': JEREMY_CHARDY,
                'bet': 3,
            },
            {
                'round': 32,
                'players': [
                    DANIEL_EVANS,
                    JUAN_IGNACIO_LONDERO,
                ],
                'odds': {
                    DANIEL_EVANS: 1.30,
                    JUAN_IGNACIO_LONDERO: 3.40,
                },
                'score': [(6, 2), (6, 4)],
                'prediction': DANIEL_EVANS,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    LLOYD_HARRIS,
                    CHRISTIAN_GARIN,
                ],
                'odds': {
                    LLOYD_HARRIS: 1.85,
                    CHRISTIAN_GARIN: 1.95,
                },
                'score': [(7, 6), (3, 6), (6, 4)],
                'prediction': LLOYD_HARRIS,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    GREGOIRE_BARRERE,
                ],
                'odds': {
                    SAM_QUERREY: 1.65,
                    GREGOIRE_BARRERE: 2.20,
                },
                'score': [(6, 7), (6, 2), (7, 5)],
                'prediction': SAM_QUERREY,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    JAMES_DUCKWORTH,
                    FEDERICO_DELBONIS,
                ],
                'odds': {
                    JAMES_DUCKWORTH: 1.85,
                    FEDERICO_DELBONIS: 1.95,
                },
                'score': [(6, 4), (6, 4)],
            },

            # 2020-01-14
            {
                'round': 32,
                'players': [
                    TOMMY_PAUL,
                    ALJAZ_BEDENE,
                ],
                'odds': {
                    TOMMY_PAUL: 1.95,
                    ALJAZ_BEDENE: 1.85,
                },
                'score': [(6, 4), (6, 4)],
                'prediction': ALJAZ_BEDENE,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    DANIEL_EVANS,
                    ALEXANDER_BUBLIK,
                ],
                'odds': {
                    DANIEL_EVANS: 1.80,
                    ALEXANDER_BUBLIK: 2.00,
                },
                'score': [(7, 5), (6, 2)],
                'prediction': DANIEL_EVANS,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    JORDAN_THOMPSON,
                ],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 2.40,
                    JORDAN_THOMPSON: 1.55,
                },
                'score': [(6, 4), (6, 7), (6, 3)],
                'prediction': JORDAN_THOMPSON,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    ALEX_BOLT,
                    STEPHANE_ROBERT,
                ],
                'odds': {
                    ALEX_BOLT: 2.30,
                    STEPHANE_ROBERT: 1.60,
                },
                'score': [(6, 4), (2, 6), (6, 0)],
                'prediction': STEPHANE_ROBERT,
                'bet': 0,  # refunded 1,
            },

            # 2020-01-15
            {
                'round': 16,
                'players': [
                    LLOYD_HARRIS,
                    LASLO_DJERE,
                ],
                'odds': {
                    LLOYD_HARRIS: 1.60,
                    LASLO_DJERE: 2.30,
                },
                'score': [(7, 6), (6, 3)],
                'prediction': LLOYD_HARRIS,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    ANDREY_RUBLEV,
                    SAM_QUERREY,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.62,
                    SAM_QUERREY: 2.25,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': ANDREY_RUBLEV,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    JEREMY_CHARDY,
                ],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.90,
                    JEREMY_CHARDY: 1.90,
                },
                'score': [(6, 3), (6, 2)],
            },
            {
                'round': 16,
                'players': [
                    TOMMY_PAUL,
                    PABLO_CUEVAS,
                ],
                'odds': {
                    TOMMY_PAUL: 1.48,
                    PABLO_CUEVAS: 2.60,
                },
                'score': [(6, 1), (6, 2)],
                'prediction': TOMMY_PAUL,
                'bet': 7,
            },
            {
                'round': 16,
                'players': [
                    ALBERT_RAMOS_VINOLAS,
                    JAUME_MUNAR,
                ],
                'odds': {
                    ALBERT_RAMOS_VINOLAS: 1.55,
                    JAUME_MUNAR: 2.40,
                },
                'score': [(7, 6), (6, 3)],
                'prediction': ALBERT_RAMOS_VINOLAS,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    JAMES_DUCKWORTH,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.62,
                    JAMES_DUCKWORTH: 2.25,
                },
                'score': [(6, 3), (7, 6)],
            },

            # 2020-01-16
            {
                'round': 8,
                'players': [
                    LLOYD_HARRIS,
                    PABLO_CARRENO_BUSTA,
                ],
                'odds': {
                    LLOYD_HARRIS: 2.60,
                    PABLO_CARRENO_BUSTA: 1.48,
                },
                'score': [(6, 3), (6, 3)],
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 6,
            },
            {
                'round': 8,
                'players': [
                    TOMMY_PAUL,
                    ALBERT_RAMOS_VINOLAS,
                ],
                'odds': {
                    TOMMY_PAUL: 1.58,
                    ALBERT_RAMOS_VINOLAS: 2.35,
                },
                'score': [(6, 3), (6, 4)],
            },
            {
                'round': 8,
                'players': [
                    ANDREY_RUBLEV,
                    DANIEL_EVANS,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.48,
                    DANIEL_EVANS: 2.60,
                },
                'score': [(6, 4), (3, 6), (6, 3)],
                'prediction': ANDREY_RUBLEV,
                'bet': 1,
            },
            {
                'round': 8,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    ALEX_BOLT,
                ],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.52,
                    ALEX_BOLT: 2.50,
                },
                'score': [(6, 3), (6, 0)],
            },

            # 2020-01-17
            {
                'round': 4,
                'players': [
                    LLOYD_HARRIS,
                    TOMMY_PAUL,
                ],
                'odds': {
                    LLOYD_HARRIS: 2.15,
                    TOMMY_PAUL: 1.68,
                },
                'score': [(6, 4), (6, 7), (6, 3)],
                'prediction': TOMMY_PAUL,
                'bet': 2,
            },
            {
                'round': 4,
                'players': [
                    ANDREY_RUBLEV,
                    FELIX_AUGER_ALIASSIME,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.52,
                    FELIX_AUGER_ALIASSIME: 2.50,
                },
                'score': [(7, 6), (6, 7), (6, 4)],
                'prediction': ANDREY_RUBLEV,
                'bet': 6,
            },

            # 2020-01-18
            {
                'round': 2,
                'players': [
                    ANDREY_RUBLEV,
                    LLOYD_HARRIS,
                ],
                'odds': {
                    ANDREY_RUBLEV: 1.28,
                    LLOYD_HARRIS: 3.60,
                },
                'score': [(6, 3), (6, 0)],
            }
        ]
    },

    {
        'location': AUCKLAND,
        'date': '2020-01-18',
        'matches': [

            # 2020-01-12
            {
                'round': 64,
                'players': [
                    MIKAEL_YMER,
                    MACKENZIE_MCDONALD,
                ],
                'odds': {
                    MIKAEL_YMER: 1.36,
                    MACKENZIE_MCDONALD: 3.00,
                },
                'score': [(6, 4), (6, 3)],
                'prediction': MIKAEL_YMER,
                'bet': 6,
            },
            {
                'round': 64,
                'players': [
                    VASEK_POSPISIL,
                    HOLGER_VITUS_NODSKOV_RUNE,
                ],
                'odds': {
                    VASEK_POSPISIL: 1.07,
                    HOLGER_VITUS_NODSKOV_RUNE: 7.50,
                },
                'score': [(7, 5), (6, 1)],
                'prediction': VASEK_POSPISIL,
                'bet': 1,
            },

            # 2020-01-13
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    LORENZO_SONEGO,
                ],
                'odds': {
                    HUBERT_HURKACZ: 1.34,
                    LORENZO_SONEGO: 3.20,
                },
                'score': [(7, 5), (6, 3)],
                'prediction': HUBERT_HURKACZ,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    TENNYS_SANDGREN,
                    MICHAEL_VENUS,
                ],
                'odds': {
                    TENNYS_SANDGREN: 1.22,
                    MICHAEL_VENUS: 4.20,
                },
                'score': [(6, 4), (6, 3)],
                'prediction': TENNYS_SANDGREN,
                'bet': 5,
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    CASPER_RUUD,
                ],
                'odds': {
                    UGO_HUMBERT: 2.00,
                    CASPER_RUUD: 1.80,
                },
                'score': [(7, 6), (2, 6), (6, 3)],
                'prediction': CASPER_RUUD,
                'bet': 4,
            },
            {
                'round': 32,
                'players': [
                    THIAGO_MONTEIRO,
                    CAMERON_NORRIE,
                ],
                'odds': {
                    THIAGO_MONTEIRO: 1.85,
                    CAMERON_NORRIE: 1.95,
                },
                'score': [(7, 6), (6, 2)],
                'prediction': THIAGO_MONTEIRO,
                'bet': 2,
            },
            {
                'round': 32,
                'players': [
                    BENOIT_PAIRE,
                    JANNIK_SINNER,
                ],
                'odds': {
                    BENOIT_PAIRE: 2.20,
                    JANNIK_SINNER: 1.65,
                },
                'score': [(6, 4), (2, 6), (6, 4)],
                'prediction': JANNIK_SINNER,
                'bet': 6,
            },
            {
                'round': 32,
                'players': [
                    MIKAEL_YMER,
                    FRANCES_TIAFOE,
                ],
                'odds': {
                    MIKAEL_YMER: 2.10,
                    FRANCES_TIAFOE: 1.70,
                },
                'score': [(6, 4), (5, 7), (6, 1)],
                'prediction': FRANCES_TIAFOE,
                'bet': 2,
            },

            # 2020-01-14
            {
                'round': 32,
                'players': [
                    KYLE_EDMUND,
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                ],
                'odds': {
                    KYLE_EDMUND: 1.48,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.60,
                },
                'score': [(6, 2), (4, 6), (6, 3)],
                'prediction': KYLE_EDMUND,
                'bet': 1,
            },
            {
                'round': 32,
                'players': [
                    VASEK_POSPISIL,
                    JOAO_SOUSA,
                ],
                'odds': {
                    VASEK_POSPISIL: 1.38,
                    JOAO_SOUSA: 3.00,
                },
                'score': [(6, 4), (6, 2)],
            },
            {
                'round': 32,
                'players': [
                    JOHN_MILLMAN,
                    MICHAEL_MMOH,
                ],
                'odds': {
                    JOHN_MILLMAN: 1.60,
                    MICHAEL_MMOH: 2.30,
                },
                'score': [(7, 6), (6, 4)],
                'prediction': JOHN_MILLMAN,
                'bet': 2,
            },

            # 2020-01-15
            {
                'round': 32,
                'players': [
                    ANDREAS_SEPPI,
                    ADRIAN_MANNARINO,
                ],
                'odds': {
                    ANDREAS_SEPPI: 2.40,
                    ADRIAN_MANNARINO: 1.55,
                },
                'score': [(3, 6), (6, 4), (6, 4)],
                'prediction': ADRIAN_MANNARINO,
                'bet': 7,
            },
            {
                'round': 32,
                'players': [
                    FELICIANO_LOPEZ,
                    PABLO_ANDUJAR,
                ],
                'odds': {
                    FELICIANO_LOPEZ: 1.95,
                    PABLO_ANDUJAR: 1.85,
                },
                'score': [(3, 6), (7, 6), (6, 4)],
            },
            {
                'round': 16,
                'players': [
                    JOHN_ISNER,
                    TENNYS_SANDGREN,
                ],
                'odds': {
                    JOHN_ISNER: 1.62,
                    TENNYS_SANDGREN: 2.25,
                },
                'score': [(7, 6), (6, 7), (6, 3)],
                'prediction': JOHN_ISNER,
                'bet': 3,
            },
            {
                'round': 16,
                'players': [
                    HUBERT_HURKACZ,
                    MIKAEL_YMER,
                ],
                'odds': {
                    HUBERT_HURKACZ: 1.42,
                    MIKAEL_YMER: 2.80,
                },
                'score': [(6, 2), (7, 6)],
                'prediction': HUBERT_HURKACZ,
                'bet': 2,
            },
            {
                'round': 16,
                'players': [
                    BENOIT_PAIRE,
                    THIAGO_MONTEIRO,
                ],
                'odds': {
                    BENOIT_PAIRE: 1.48,
                    THIAGO_MONTEIRO: 2.60,
                },
                'score': [(4, 6), (6, 4), (6, 3)],
                'prediction': BENOIT_PAIRE,
                'bet': 1,
            },
            {
                'round': 16,
                'players': [
                    DENIS_SHAPOVALOV,
                    VASEK_POSPISIL,
                ],
                'odds': {
                    DENIS_SHAPOVALOV: 1.58,
                    VASEK_POSPISIL: 2.35,
                },
                'score': [(6, 4), (7, 6)],
                'prediction': DENIS_SHAPOVALOV,
                'bet': 1,
            },

            # 2020-01-16
            {
                'round': 8,
                'players': [
                    JOHN_ISNER,
                    KYLE_EDMUND,
                ],
                'odds': {
                    JOHN_ISNER: 1.85,
                    KYLE_EDMUND: 1.95,
                },
                'score': [(7, 6), (7, 6)],
                'prediction': JOHN_ISNER,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    UGO_HUMBERT,
                    DENIS_SHAPOVALOV,
                ],
                'odds': {
                    UGO_HUMBERT: 3.10,
                    DENIS_SHAPOVALOV: 1.36,
                },
                'score': [(7, 5), (6, 4)],
            },
            {
                'round': 8,
                'players': [
                    BENOIT_PAIRE,
                    JOHN_MILLMAN,
                ],
                'odds': {
                    BENOIT_PAIRE: 2.00,
                    JOHN_MILLMAN: 1.80,
                },
                'score': [(3, 6), (6, 1), (6, 4)],
                'prediction': JOHN_MILLMAN,
                'bet': 4,
            },
            {
                'round': 8,
                'players': [
                    HUBERT_HURKACZ,
                    FELICIANO_LOPEZ,
                ],
                'odds': {
                    HUBERT_HURKACZ: 1.30,
                    FELICIANO_LOPEZ: 3.40,
                },
                'score': [(6, 4), (6, 7), (6, 4)],
            },

            # 2020-01-17
            {
                'round': 4,
                'players': [
                    UGO_HUMBERT,
                    JOHN_ISNER,
                ],
                'odds': {
                    UGO_HUMBERT: 1.90,
                    JOHN_ISNER: 1.90,
                },
                'score': [(7, 6), (6, 4)],
            },
            {
                'round': 4,
                'players': [
                    BENOIT_PAIRE,
                    HUBERT_HURKACZ,
                ],
                'odds': {
                    BENOIT_PAIRE: 2.35,
                    HUBERT_HURKACZ: 1.58,
                },
                'score': [(6, 4), (6, 7), (6, 2)],
                'prediction': HUBERT_HURKACZ,
                'bet': 4,
            },

            # 2020-01-18
            {
                'round': 2,
                'players': [
                    UGO_HUMBERT,
                    BENOIT_PAIRE,
                ],
                'odds': {
                    UGO_HUMBERT: 1.80,
                    BENOIT_PAIRE: 2.00,
                },
                'score': [(7, 6), (3, 6), (7, 6)],
                'prediction': UGO_HUMBERT,
                'bet': 1,
            }
        ]
    },

]
