from men import *

# 68  -1.0  2019-02-17 Argentina Open
# 67  -2.6  2019-02-24 Rio Open presented by Claro
# 67  0.41  skipping bets based on pred (none excluded)
# 67  0.30  estimators to 100 and no betting on qualifiers
# 59  -2.84  2019-02-24 Open 13 Provence
# 57  -10.3  2019-07-21 Swedish Open
# 53  -8.45  Plava Laguna Croatia Open Umag
# 53  -9.73  2019-07-21 Hall of Fame Open
# 55  -9.7  2019-07-14 Wimbledon
# 67  9.1  retireds added

# 65  -0.0  hamburg updated
# 63  -1.5  added multi bet and changed to roi
# 61  -24  diff set to absolute
# 60  5.31  2019-06-29 Nature Valley International
# 62  2.51  2019-06-29 Turkish Airlines Open Antalya
# 64  2.23  2019-06-23 Fever-Tree Championships

# 62  1.96  2019-02-24 Delray Beach Open by VITACOST.com
# 53 1.68 <- bet multiplier added
# 65 -0.80 <- 2019-04-14 Fayez Sarofim & Co US Mens Clay Court Championship
# 68 -0.57 <- 2019-04-22 Hungarian Open
# 52 -2.88 <- added round as variable


DATA = [
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
    },

    {
        'name': 'Libema Open',
        'category': 'ATP250',
        'date': '2019-06-16',
        'location': 's-Hertogenbosch, Netherlands',
        'matches': [

            # 2019-06-08
            {
                'round': 512,
                'players': [
                    SALVATORE_CARUSO,
                    FILIP_HORANSKY
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    SALVATORE_CARUSO: 1.43,
                    FILIP_HORANSKY: 2.65
                }
            },
            {
                'round': 512,
                'players': [
                    JANNIK_SINNER,
                    LUKAS_LACKO
                ],
                'score': [(6, 7), (7, 6), (6, 2)],
                'odds': {
                    JANNIK_SINNER: 3.30,
                    LUKAS_LACKO: 1.27
                }
            },
            {
                'round': 512,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    NICOLAS_MAHUT
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.35,
                    NICOLAS_MAHUT: 1.56
                }
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    EGOR_GERASIMOV
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    TOMMY_PAUL: 1.36,
                    EGOR_GERASIMOV: 2.73
                }
            },
            {
                'round': 512,
                'players': [
                    DANIEL_BRANDS,
                    ALEX_BOLT
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    DANIEL_BRANDS: 2.50,
                    ALEX_BOLT: 1.51
                }
            },
            {
                'round': 512,
                'players': [
                    MARCOS_GIRON,
                    JASON_JUNG
                ],
                'score': [(6, 2), (5, 7), (6, 2)],
                'odds': {
                    MARCOS_GIRON: 2.19,
                    JASON_JUNG: 1.57
                }
            },
            {
                'round': 512,
                'players': [
                    THOMAS_FABBIANO,
                    EMIL_RUUSUVUORI
                ],
                'score': [(4, 6), (6, 3), (6, 1)],
                'odds': {
                    THOMAS_FABBIANO: 1.19,
                    EMIL_RUUSUVUORI: 4.20
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREA_ARNABOLDI,
                    BRADLEY_KLAHN
                ],
                'score': [(4, 6), (6, 4), (6, 2)],
                'odds': {
                    ANDREA_ARNABOLDI: 2.65,
                    BRADLEY_KLAHN: 1.42
                }
            },

            # 2019-06-09
            {
                'round': 256,
                'players': [
                    SALVATORE_CARUSO,
                    MARCOS_GIRON
                ],
                'score': [(6, 3), (3, 6), (6, 3)],
                'odds': {
                    SALVATORE_CARUSO: 1.63,
                    MARCOS_GIRON: 2.05
                }
            },
            {
                'round': 256,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    ANDREA_ARNABOLDI
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.18,
                    ANDREA_ARNABOLDI: 4.56
                }
            },
            {
                'round': 256,
                'players': [
                    TOMMY_PAUL,
                    DANIEL_BRANDS
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    TOMMY_PAUL: 1.42,
                    DANIEL_BRANDS: 2.70
                }
            },
            {
                'round': 256,
                'players': [
                    JANNIK_SINNER,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    JANNIK_SINNER: 2.05,
                    THOMAS_FABBIANO: 1.61
                }
            },

            # 2019-06-10
            {
                'round': 32,
                'players': [
                    JORDAN_THOMPSON,
                    TOMMY_PAUL
                ],
                'score': [(3, 6), (6, 1), (6, 4)],
                'odds': {
                    JORDAN_THOMPSON: 1.83,
                    TOMMY_PAUL: 1.92
                }
            },
            {
                'round': 32,
                'players': [
                    ROBIN_HAASE,
                    UGO_HUMBERT
                ],
                'score': [(5, 7), (7, 6), (7, 6)],
                'odds': {
                    ROBIN_HAASE: 1.65,
                    UGO_HUMBERT: 2.20
                }
            },
            {
                'round': 32,
                'players': [
                    TAYLOR_FRITZ,
                    JURIJ_RODIONOV
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 1.22,
                    JURIJ_RODIONOV: 4.35
                }
            },
            {
                'round': 32,
                'players': [
                    CRISTIAN_GARIN,
                    SALVATORE_CARUSO
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    CRISTIAN_GARIN: 1.59,
                    SALVATORE_CARUSO: 2.47
                }
            },
            {
                'round': 32,
                'players': [
                    FRANCES_TIAFOE,
                    JOAO_SOUSA
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    FRANCES_TIAFOE: 1.41,
                    JOAO_SOUSA: 3.03
                }
            },

            # 2019-06-11
            {
                'round': 32,
                'players': [
                    ANDREAS_SEPPI,
                    THOMAS_FABBIANO
                ],
                'score': [(7, 6), (7, 5)],
                'odds': {
                    ANDREAS_SEPPI: 1.45,
                    THOMAS_FABBIANO: 2.80
                }
            },
            {
                'round': 32,
                'players': [
                    ADRIAN_MANNARINO,
                    THIEMO_DE_BAKKER
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    ADRIAN_MANNARINO: 1.20,
                    THIEMO_DE_BAKKER: 4.60
                }
            },
            {
                'round': 32,
                'players': [
                    MIKHAIL_KUKUSHKIN,
                    LORENZO_SONEGO
                ],
                'score': [(5, 7), (6, 4), (6, 4)],
                'odds': {
                    MIKHAIL_KUKUSHKIN: 1.59,
                    LORENZO_SONEGO: 2.35
                }
            },
            {
                'round': 32,
                'players': [
                    NICOLAS_JARRY,
                    JANNIK_SINNER
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    NICOLAS_JARRY: 1.80,
                    JANNIK_SINNER: 2.03
                }
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 2.05,
                    MATTHEW_EBDEN: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    ALJAZ_BEDENE
                ],
                'score': [(6, 7), (7, 6), (6, 4)],
                'odds': {
                    RICHARD_GASQUET: 1.35,
                    ALJAZ_BEDENE: 3.20
                }
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(6, 0), (6, 2)],
                'odds': {
                    DAVID_GOFFIN: 1.35,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 3.22
                }
            },

            # 2019-06-12
            {
                'round': 16,
                'players': [
                    JORDAN_THOMPSON,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JORDAN_THOMPSON: 2.41,
                    FRANCES_TIAFOE: 1.59
                }
            },
            {
                'round': 16,
                'players': [
                    ALEX_DE_MINAUR,
                    ANDREAS_SEPPI
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    ALEX_DE_MINAUR: 1.59,
                    ANDREAS_SEPPI: 2.40
                }
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    TAYLOR_FRITZ
                ],
                'score': [(4, 6), (6, 3), (6, 3)],
                'odds': {
                    BORNA_CORIC: 1.61,
                    TAYLOR_FRITZ: 2.36
                }
            },

            # 2019-06-13
            {
                'round': 16,
                'players': [
                    CRISTIAN_GARIN,
                    ROBIN_HAASE
                ],
                'score': [(7, 5), (7, 5)],
                # no odds
            },
            {
                'round': 16,
                'players': [
                    DAVID_GOFFIN,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    DAVID_GOFFIN: 1.38,
                    PIERRE_HUGUES_HERBERT: 3.07
                }
            },
            {
                'round': 16,
                'players': [
                    ADRIAN_MANNARINO,
                    FERNANDO_VERDASCO
                ],
                'score': [(1, 6), (6, 3), (6, 4)],
                'odds': {
                    ADRIAN_MANNARINO: 1.69,
                    FERNANDO_VERDASCO: 2.24
                }
            },
            {
                'round': 16,
                'players': [
                    NICOLAS_JARRY,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(6, 4), (3, 6), (6, 4)],
                'odds': {
                    NICOLAS_JARRY: 4.45,
                    STEFANOS_TSITSIPAS: 1.18
                }
            },

            # 2019-06-14
            {
                'round': 16,
                'players': [
                    RICHARD_GASQUET,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(7, 6), (6, 4)],
                # no odds
            },
            {
                'round': 8,
                'players': [
                    RICHARD_GASQUET,
                    NICOLAS_JARRY
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    RICHARD_GASQUET: 1.76,
                    NICOLAS_JARRY: 2.19
                }
            },
            {
                'round': 8,
                'players': [
                    ADRIAN_MANNARINO,
                    DAVID_GOFFIN
                ],
                'score': [(4, 6), (7, 5), (6, 3)],
                'odds': {
                    ADRIAN_MANNARINO: 3.59,
                    DAVID_GOFFIN: 1.29
                }
            },
            {
                'round': 8,
                'players': [
                    JORDAN_THOMPSON,
                    ALEX_DE_MINAUR
                ],
                'score': [(4, 6), (6, 2), (6, 3)],
                'odds': {
                    JORDAN_THOMPSON: 2.60,
                    ALEX_DE_MINAUR: 1.54
                }
            },
            {
                'round': 8,
                'players': [
                    BORNA_CORIC,
                    CRISTIAN_GARIN
                ],
                'score': [(6, 7), (6, 3), (7, 6)],
                'odds': {
                    BORNA_CORIC: 1.41,
                    CRISTIAN_GARIN: 2.95
                }
            },

            # 2019-06-16
            {
                'round': 4,
                'players': [
                    JORDAN_THOMPSON,
                    RICHARD_GASQUET
                ],
                'score': [(7, 5), (6, 3)]
            },
            {
                'round': 4,
                'players': [
                    ADRIAN_MANNARINO,
                    BORNA_CORIC
                ],
                'score': [(4, 6), (6, 3), (7, 6)]
            },
            {
                'round': 2,
                'players': [
                    ADRIAN_MANNARINO,
                    JORDAN_THOMPSON
                ],
                'score': [(7, 6), (6, 3)]
            }
        ]
    },

    {
        'name': 'Fever-Tree Championships',
        'category': 'ATP500',
        'date': '2019-06-23',
        'location': 'London, Great Britain',
        'matches': [

            # 2019-06-15
            {
                'round': 512,
                'players': [
                    ALJAZ_BEDENE,
                    JURGEN_ZOPP
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    ALJAZ_BEDENE: 1.21,
                    JURGEN_ZOPP: 4.25
                }
            },
            {
                'round': 512,
                'players': [
                    JAMES_WARD,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    JAMES_WARD: 1.67,
                    PRAJNESH_GUNNESWARAN: 2.05
                }
            },
            {
                'round': 512,
                'players': [
                    TOMMY_PAUL,
                    BRADLEY_KLAHN
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    TOMMY_PAUL: 1.46,
                    BRADLEY_KLAHN: 2.60
                }
            },
            {
                'round': 512,
                'players': [
                    ALEJANDRO_DAVIDOVICH_FOKINA,
                    BERNARD_TOMIC
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ALEJANDRO_DAVIDOVICH_FOKINA: 2.00,
                    BERNARD_TOMIC: 1.71
                }
            },
            {
                'round': 512,
                'players': [
                    IVO_KARLOVIC,
                    PETER_POLANSKY
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    IVO_KARLOVIC: 1.34,
                    PETER_POLANSKY: 3.04
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXANDER_BUBLIK,
                    JACK_DRAPER
                ],
                'score': [(6, 2), (1, 6), (6, 3)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.26,
                    JACK_DRAPER: 3.41
                }
            },
            {
                'round': 512,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    ALEXEI_POPYRIN
                ],
                'score': [(6, 2), (5, 7), (6, 4)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 3.60,
                    ALEXEI_POPYRIN: 1.23
                }
            },
            {
                'round': 512,
                'players': [
                    NICOLAS_MAHUT,
                    NICOLAS_JARRY
                ],
                'score': [(6, 3), (6, 7), (7, 6)],
                'odds': {
                    NICOLAS_MAHUT: 1.83,
                    NICOLAS_JARRY: 1.83
                }
            },

            # 2019-06-16
            {
                'round': 256,
                'players': [
                    NICOLAS_MAHUT,
                    ALEJANDRO_DAVIDOVICH_FOKINA
                ],
                'score': [(7, 5), (4, 6), (6, 3)],
                'odds': {
                    NICOLAS_MAHUT: 1.74,
                    ALEJANDRO_DAVIDOVICH_FOKINA: 1.79
                }
            },
            {
                'round': 256,
                'players': [
                    JAMES_WARD,
                    IVO_KARLOVIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    JAMES_WARD: 2.84,
                    IVO_KARLOVIC: 1.36
                }
            },
            {
                'round': 256,
                'players': [
                    ALEXANDER_BUBLIK,
                    TOMMY_PAUL
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.95,
                    TOMMY_PAUL: 1.71
                }
            },
            {
                'round': 256,
                'players': [
                    ALJAZ_BEDENE,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(7, 6), (3, 6), (6, 1)],
                'odds': {
                    ALJAZ_BEDENE: 1.24,
                    ROBERTO_CARBALLES_BAENA: 3.90
                }
            },

            # 2019-06-17
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    JAMES_WARD
                ],
                'score': [(3, 6), (6, 3), (7, 6)],
                'odds': {
                    GILLES_SIMON: 1.44,
                    JAMES_WARD: 2.70
                }
            },
            {
                'round': 32,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    ALEXANDER_BUBLIK
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 2.25,
                    ALEXANDER_BUBLIK: 1.62
                }
            },
            {
                'round': 32,
                'players': [
                    NICOLAS_MAHUT,
                    FRANCES_TIAFOE
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    NICOLAS_MAHUT: 2.08,
                    FRANCES_TIAFOE: 1.69
                }
            },
            {
                'round': 32,
                'players': [
                    MARIN_CILIC,
                    CRISTIAN_GARIN
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    MARIN_CILIC: 1.29,
                    CRISTIAN_GARIN: 3.50
                }
            },
            {
                'round': 32,
                'players': [
                    DANILL_MEDVEDEV,
                    FERNANDO_VERDASCO
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    DANILL_MEDVEDEV: 1.40,
                    FERNANDO_VERDASCO: 2.95
                }
            },
            {
                'round': 32,
                'players': [
                    KEVIN_ANDERSON,
                    CAMERON_NORRIE
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    KEVIN_ANDERSON: 1.35,
                    CAMERON_NORRIE: 3.25
                }
            },

            # 2019-06-19
            {
                'round': 32,
                'players': [
                    LUCAS_POUILLE,
                    JAY_CLARKE
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    LUCAS_POUILLE: 1.14,
                    JAY_CLARKE: 5.25
                }
            },
            {
                'round': 32,
                'players': [
                    FELICIANO_LOPEZ,
                    MARTON_FUCSOVICS
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 1.63,
                    MARTON_FUCSOVICS: 2.23
                }
            },
            {
                'round': 32,
                'players': [
                    JEREMY_CHARDY,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 1), (6, 3)],
                'odds': {
                    JEREMY_CHARDY: 1.61,
                    MIKHAIL_KUKUSHKIN: 2.30
                }
            },
            {
                'round': 32,
                'players': [
                    ALJAZ_BEDENE,
                    ALEX_DE_MINAUR
                ],
                'score': [(3, 6), (6, 4), (6, 4)],
                'odds': {
                    ALJAZ_BEDENE: 2.45,
                    ALEX_DE_MINAUR: 1.56
                }
            },
            {
                'round': 32,
                'players': [
                    STAN_WAWRINKA,
                    DANIEL_EVANS
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    STAN_WAWRINKA: 1.69,
                    DANIEL_EVANS: 2.15
                }
            },
            {
                'round': 32,
                'players': [
                    MILOS_RAONIC,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    MILOS_RAONIC: 1.17,
                    MARCO_CECCHINATO: 5.15
                }
            },
            {
                'round': 32,
                'players': [
                    JUAN_MARTIN_DEL_POTRO,
                    DENIS_SHAPOVALOV
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    JUAN_MARTIN_DEL_POTRO: 1.38,
                    DENIS_SHAPOVALOV: 2.85
                }
            },
            {
                'round': 16,
                'players': [
                    FELICIANO_LOPEZ,
                    JUAN_MARTIN_DEL_POTRO
                ],
                'score': [],
                'wo': True,
                'odds': {
                    FELICIANO_LOPEZ: 2.85,
                    JUAN_MARTIN_DEL_POTRO: 1.38
                }
            },

            # 2019-06-20
            {
                'round': 32,
                'players': [
                    NICK_KYRGIOS,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    NICK_KYRGIOS: 1.21,
                    ROBERTO_CARBALLES_BAENA: 4.74
                }
            },
            {
                'round': 32,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    GRIGOR_DIMITROV
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.35,
                    GRIGOR_DIMITROV: 1.57
                }
            },
            {
                'round': 32,
                'players': [
                    STEFANOS_TSITSIPAS,
                    KYLE_EDMUND
                ],
                'score': [(6, 3), (7, 5)],
                # no odds
            },
            {
                'round': 16,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    NICK_KYRGIOS
                ],
                'score': [(6, 7), (7, 6), (7, 5)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 1.78,
                    NICK_KYRGIOS: 2.00
                }
            },
            {
                'round': 16,
                'players': [
                    NICOLAS_MAHUT,
                    STAN_WAWRINKA
                ],
                'score': [(3, 6), (7, 5), (7, 6)],
                'odds': {
                    NICOLAS_MAHUT: 2.85,
                    STAN_WAWRINKA: 1.38
                }
            },
            {
                'round': 16,
                'players': [
                    MILOS_RAONIC,
                    ALJAZ_BEDENE
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    MILOS_RAONIC: 1.17,
                    ALJAZ_BEDENE: 5.00
                }
            },
            {
                'round': 16,
                'players': [
                    DIEGO_SCHWARTZMAN,
                    MARIN_CILIC
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    DIEGO_SCHWARTZMAN: 4.45,
                    MARIN_CILIC: 1.18
                }
            },
            {
                'round': 16,
                'players': [
                    DANILL_MEDVEDEV,
                    LUCAS_POUILLE
                ],
                'score': [(7, 6), (6, 7), (6, 4)],
                'odds': {
                    DANILL_MEDVEDEV: 1.48,
                    LUCAS_POUILLE: 2.60
                }
            },
            {
                'round': 16,
                'players': [
                    GILLES_SIMON,
                    KEVIN_ANDERSON
                ],
                'score': [(6, 1), (4, 6), (6, 4)],
                'odds': {
                    GILLES_SIMON: 3.10,
                    KEVIN_ANDERSON: 1.33
                }
            },
            {
                'round': 16,
                'players': [
                    STEFANOS_TSITSIPAS,
                    JEREMY_CHARDY
                ],
                'score': [(4, 6), (7, 6), (7, 6)],
                'odds': {
                    STEFANOS_TSITSIPAS: 1.25,
                    JEREMY_CHARDY: 3.60
                }
            },

            # 2019-06-21
            {
                'round': 8,
                'players': [
                    GILLES_SIMON,
                    NICOLAS_MAHUT
                ],
                'score': [(7, 6), (5, 7), (7, 6)],
                'odds': {
                    GILLES_SIMON: 1.65,
                    NICOLAS_MAHUT: 2.20
                }
            },
            {
                'round': 8,
                'players': [
                    FELICIANO_LOPEZ,
                    MILOS_RAONIC
                ],
                'score': [(4, 6), (6, 4), (7, 6)],
                'odds': {
                    FELICIANO_LOPEZ: 3.25,
                    MILOS_RAONIC: 1.33
                }
            },
            {
                'round': 8,
                'players': [
                    DANILL_MEDVEDEV,
                    DIEGO_SCHWARTZMAN
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    DANILL_MEDVEDEV: 1.27,
                    DIEGO_SCHWARTZMAN: 3.85
                }
            },
            {
                'round': 8,
                'players': [
                    FELIX_AUGER_ALIASSIME,
                    STEFANOS_TSITSIPAS
                ],
                'score': [(7, 5), (6, 2)],
                'odds': {
                    FELIX_AUGER_ALIASSIME: 2.30,
                    STEFANOS_TSITSIPAS: 1.59
                }
            },

            # 2019-06-22
            {
                'round': 4,
                'players': [
                    FELICIANO_LOPEZ,
                    FELIX_AUGER_ALIASSIME
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    FELICIANO_LOPEZ: 2.70,
                    FELIX_AUGER_ALIASSIME: 1.47
                }
            },
            {
                'round': 4,
                'players': [
                    GILLES_SIMON,
                    DANILL_MEDVEDEV
                ],
                'score': [(6, 7), (6, 4), (6, 3)],
                'odds': {
                    GILLES_SIMON: 4.50,
                    DANILL_MEDVEDEV: 1.18
                }
            },

            # 2019-06-23
            {
                'round': 2,
                'players': [
                    FELICIANO_LOPEZ,
                    GILLES_SIMON
                ],
                'score': [(6, 2), (6, 7), (7, 6)],
                'odds': {
                    FELICIANO_LOPEZ: 1.53,
                    GILLES_SIMON: 2.44
                }
            }
        ]
    },

    {
        'name': 'Noventi Open',
        'category': 'ATP500',
        'date': '2019-06-23',
        'location': 'Halle, Germany',
        'matches': [

            # 2019-06-15
            {
                'round': 512,
                'players': [
                    SERGIY_STAKHOVSKY,
                    ERNESTS_GULBIS
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    SERGIY_STAKHOVSKY: 1.91,
                    ERNESTS_GULBIS: 1.71
                }
            },
            {
                'round': 512,
                'players': [
                    MISCHA_ZVEREV,
                    LLOYD_HARRIS
                ],
                'score': [(6, 3), (5, 7), (6, 4)],
                'odds': {
                    MISCHA_ZVEREV: 1.74,
                    LLOYD_HARRIS: 1.80
                }
            },
            {
                'round': 512,
                'players': [
                    DENIS_KUDLA,
                    THOMAS_FABBIANO
                ],
                'score': [(4, 6), (6, 0), (6, 4)],
                'odds': {
                    DENIS_KUDLA: 1.35,
                    THOMAS_FABBIANO: 2.87
                }
            },
            {
                'round': 512,
                'players': [
                    MIOMIR_KECMANOVIC,
                    LOUIS_WESSELS
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.06,
                    LOUIS_WESSELS: 8.02
                }
            },
            {
                'round': 512,
                'players': [
                    MATS_MORAING,
                    ANDREY_RUBLEV
                ],
                'score': [(6, 3), (5, 7), (7, 6)],
                'odds': {
                    MATS_MORAING: 2.09,
                    ANDREY_RUBLEV: 1.61
                }
            },
            {
                'round': 512,
                'players': [
                    MATTHIAS_BACHINGER,
                    LORENZO_SONEGO
                ],
                'score': [(6, 4), (6, 2)],
                'odds': {
                    MATTHIAS_BACHINGER: 1.80,
                    LORENZO_SONEGO: 1.77
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREAS_SEPPI,
                    BRAYDEN_SCHNUR
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    ANDREAS_SEPPI: 1.33,
                    BRAYDEN_SCHNUR: 3.20
                }
            },
            {
                'round': 512,
                'players': [
                    JOAO_SOUSA,
                    JANNIK_SINNER
                ],
                'score': [(6, 7), (6, 3), (6, 4)],
                'odds': {
                    JOAO_SOUSA: 2.00,
                    JANNIK_SINNER: 1.70
                }
            },

            # 2019-06-16
            {
                'round': 256,
                'players': [
                    SERGIY_STAKHOVSKY,
                    MATTHIAS_BACHINGER
                ],
                'score': [(6, 4), (6, 7), (6, 2)],
                'odds': {
                    SERGIY_STAKHOVSKY: 1.95,
                    MATTHIAS_BACHINGER: 1.74
                }
            },
            {
                'round': 256,
                'players': [
                    MATS_MORAING,
                    DENIS_KUDLA
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    MATS_MORAING: 4.90,
                    DENIS_KUDLA: 1.16
                }
            },
            {
                'round': 256,
                'players': [
                    ANDREAS_SEPPI,
                    MISCHA_ZVEREV
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    ANDREAS_SEPPI: 1.34,
                    MISCHA_ZVEREV: 3.02
                }
            },
            {
                'round': 256,
                'players': [
                    JOAO_SOUSA,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 7), (6, 4), (6, 1)],
                'odds': {
                    JOAO_SOUSA: 2.05,
                    MIOMIR_KECMANOVIC: 1.62
                }
            },

            # 2019-06-17
            {
                'round': 32,
                'players': [
                    JOAO_SOUSA,
                    HUBERT_HURKACZ
                ],
                'score': [(7, 6), (6, 1)],
                'odds': {
                    JOAO_SOUSA: 2.10,
                    HUBERT_HURKACZ: 1.74
                }
            },
            {
                'round': 32,
                'players': [
                    STEVE_JOHNSON,
                    PHILIPP_KOHLSCHREIBER
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    STEVE_JOHNSON: 2.22,
                    PHILIPP_KOHLSCHREIBER: 1.63
                }
            },
            {
                'round': 32,
                'players': [
                    RADU_ALBOT,
                    MATTHEW_EBDEN
                ],
                'score': [(5, 7), (6, 1), (6, 4)],
                'odds': {
                    RADU_ALBOT: 2.10,
                    MATTHEW_EBDEN: 1.71
                }
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    GAEL_MONFILS
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 2.60,
                    GAEL_MONFILS: 1.50
                }
            },
            {
                'round': 32,
                'players': [
                    KAREN_KHACHANOV,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    KAREN_KHACHANOV: 3.72,
                    MIOMIR_KECMANOVIC: 1.31
                }
            },
            {
                'round': 32,
                'players': [
                    ALEXANDER_ZVEREV,
                    ROBIN_HAASE
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.16,
                    ROBIN_HAASE: 5.70
                }
            },

            # 2019-06-18
            {
                'round': 32,
                'players': [
                    JO_WILFRIED_TSONGA,
                    BENOIT_PAIRE
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    JO_WILFRIED_TSONGA: 1.38,
                    BENOIT_PAIRE: 3.05
                }
            },
            {
                'round': 32,
                'players': [
                    JAN_LENNARD_STRUFF,
                    LASLO_DJERE
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JAN_LENNARD_STRUFF: 1.17,
                    LASLO_DJERE: 5.00
                }
            },
            {
                'round': 32,
                'players': [
                    SERGIY_STAKHOVSKY,
                    RUDOLF_MOLLEKER
                ],
                'score': [(3, 6), (7, 6), (6, 2)],
                'odds': {
                    SERGIY_STAKHOVSKY: 1.54,
                    RUDOLF_MOLLEKER: 2.45
                }
            },
            {
                'round': 32,
                'players': [
                    ANDREAS_SEPPI,
                    MATS_MORAING
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ANDREAS_SEPPI: 1.36,
                    MATS_MORAING: 3.07
                }
            },
            {
                'round': 32,
                'players': [
                    RICHARD_GASQUET,
                    PETER_GOJOWCZYK
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    RICHARD_GASQUET: 1.38,
                    PETER_GOJOWCZYK: 2.95
                }
            },
            {
                'round': 32,
                'players': [
                    DAVID_GOFFIN,
                    GUIDO_PELLA
                ],
                'score': [(6, 1), (6, 1)],
                'odds': {
                    DAVID_GOFFIN: 1.24,
                    GUIDO_PELLA: 3.85
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    TAYLOR_FRITZ
                ],
                'score': [(7, 6), (6, 0)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.56,
                    TAYLOR_FRITZ: 2.35
                }
            },
            {
                'round': 32,
                'players': [
                    MATTEO_BERRETTINI,
                    NIKOLOZ_BASILASHVILI
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    MATTEO_BERRETTINI: 1.28,
                    NIKOLOZ_BASILASHVILI: 3.60
                }
            },
            {
                'round': 32,
                'players': [
                    BORNA_CORIC,
                    JAUME_MUNAR
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    BORNA_CORIC: 1.18,
                    JAUME_MUNAR: 4.55
                }
            },
            {
                'round': 32,
                'players': [
                    ROGER_FEDERER,
                    JOHN_MILLMAN
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.05,
                    JOHN_MILLMAN: 8.00
                }
            },

            # 2019-06-19
            {
                'round': 16,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    SERGIY_STAKHOVSKY
                ],
                'score': [(2, 6), (7, 6), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.36,
                    SERGIY_STAKHOVSKY: 3.15
                }
            },
            {
                'round': 16,
                'players': [
                    DAVID_GOFFIN,
                    RADU_ALBOT
                ],
                'score': [(4, 6), (6, 4), (6, 3)],
                'odds': {
                    DAVID_GOFFIN: 1.21,
                    RADU_ALBOT: 4.30
                }
            },
            {
                'round': 16,
                'players': [
                    BORNA_CORIC,
                    JOAO_SOUSA
                ],
                'score': [(7, 6), (5, 7), (7, 6)],
                'odds': {
                    BORNA_CORIC: 1.21,
                    JOAO_SOUSA: 4.25
                }
            },
            {
                'round': 16,
                'players': [
                    KAREN_KHACHANOV,
                    JAN_LENNARD_STRUFF
                ],
                'score': [(6, 3), (3, 6), (6, 4)],
                'odds': {
                    KAREN_KHACHANOV: 1.91,
                    JAN_LENNARD_STRUFF: 1.87
                }
            },

            # 2019-06-20
            {
                'round': 16,
                'players': [
                    MATTEO_BERRETTINI,
                    ANDREAS_SEPPI
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    MATTEO_BERRETTINI: 1.25,
                    ANDREAS_SEPPI: 3.60
                }
            },
            {
                'round': 16,
                'players': [
                    ROBERTO_BAUTISTA_AGUT,
                    RICHARD_GASQUET
                ],
                'score': [(6, 1), (6, 4)],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.56,
                    RICHARD_GASQUET: 2.40
                }
            },
            {
                'round': 16,
                'players': [
                    ALEXANDER_ZVEREV,
                    STEVE_JOHNSON
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    ALEXANDER_ZVEREV: 1.47,
                    STEVE_JOHNSON: 2.69
                }
            },
            {
                'round': 16,
                'players': [
                    ROGER_FEDERER,
                    JO_WILFRIED_TSONGA
                ],
                'score': [(7, 6), (4, 6), (7, 5)],
                'odds': {
                    ROGER_FEDERER: 1.17,
                    JO_WILFRIED_TSONGA: 5.00
                }
            },

            # 2019-06-21
            {
                'round': 8,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    BORNA_CORIC
                ],
                'score': [(7, 5), (0, 0)],
                'retired': True,
                'odds': {
                    PIERRE_HUGUES_HERBERT: 2.30,
                    BORNA_CORIC: 1.51
                }
            },
            {
                'round': 8,
                'players': [
                    MATTEO_BERRETTINI,
                    KAREN_KHACHANOV
                ],
                'score': [(6, 2), (7, 6)],
                'odds': {
                    MATTEO_BERRETTINI: 1.67,
                    KAREN_KHACHANOV: 2.20
                }
            },
            {
                'round': 8,
                'players': [
                    DAVID_GOFFIN,
                    ALEXANDER_ZVEREV
                ],
                'score': [(3, 6), (6, 1), (7, 6)],
                'odds': {
                    DAVID_GOFFIN: 2.27,
                    ALEXANDER_ZVEREV: 1.63
                }
            },
            {
                'round': 8,
                'players': [
                    ROGER_FEDERER,
                    ROBERTO_BAUTISTA_AGUT
                ],
                'score': [(6, 3), (4, 6), (6, 4)],
                'odds': {
                    ROGER_FEDERER: 1.15,
                    ROBERTO_BAUTISTA_AGUT: 5.00
                }
            },

            # 2019-06-22
            {
                'round': 4,
                'players': [
                    DAVID_GOFFIN,
                    MATTEO_BERRETTINI
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    DAVID_GOFFIN: 2.25,
                    MATTEO_BERRETTINI: 1.63
                }
            },
            {
                'round': 4,
                'players': [
                    ROGER_FEDERER,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 3), (6, 3)],
                'odds': {
                    ROGER_FEDERER: 1.06,
                    PIERRE_HUGUES_HERBERT: 8.50
                }
            },

            # 2019-06-23
            {
                'round': 2,
                'players': [
                    ROGER_FEDERER,
                    DAVID_GOFFIN
                ],
                'score': [(7, 6), (6, 1)]
            }
        ]
    },

    {
        'name': 'Turkish Airlines Open Antalya',
        'category': 'ATP250',
        'date': '2019-06-29',
        'location': 'Antalya, Turkey',
        'matches': [

            # 2019-06-22
            {
                'round': 512,
                'players': [
                    ROBERTO_ORTEGA_OLMEDO,
                    SASI_KUMAR_MUKUND
                ],
                'score': [(6, 2), (6, 1)],
                'odds': {
                    ROBERTO_ORTEGA_OLMEDO: 1.74,
                    SASI_KUMAR_MUKUND: 1.95
                }
            },
            {
                'round': 512,
                'players': [
                    CARLOS_GOMEZ_HERRERA,
                    MARCELO_TOMAS_BARRIOS_VERA
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    CARLOS_GOMEZ_HERRERA: 1.91,
                    MARCELO_TOMAS_BARRIOS_VERA: 1.77
                }
            },
            {
                'round': 512,
                'players': [
                    KEVIN_KRAWIETZ,
                    ALDIN_SETKIC
                ],
                'score': [(7, 5), (6, 3)],
                'odds': {
                    KEVIN_KRAWIETZ: 1.61,
                    ALDIN_SETKIC: 2.25
                }
            },
            {
                'round': 512,
                'players': [
                    MARC_ANDREA_HUESLER,
                    ANTE_PAVIC
                ],
                'score': [(7, 6), (6, 7), (7, 6)],
                'odds': {
                    MARC_ANDREA_HUESLER: 1.91,
                    ANTE_PAVIC: 1.74
                }
            },
            {
                'round': 512,
                'players': [
                    JC_ARAGONE,
                    TIM_PUETZ
                ],
                'score': [(6, 1), (6, 4)],
                # no odds
            },
            {
                'round': 512,
                'players': [
                    GONCALO_OLIVEIRA,
                    LUKE_SAVILLE
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    GONCALO_OLIVEIRA: 3.70,
                    LUKE_SAVILLE: 1.25
                }
            },
            {
                'round': 512,
                'players': [
                    STEVE_DARCIS,
                    SARP_AGABIGUN
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    STEVE_DARCIS: 1.01,
                    SARP_AGABIGUN: 13.21
                }
            },
            {
                'round': 512,
                'players': [
                    VIKTOR_TROICKI,
                    YANKI_EREL
                ],
                'score': [(6, 1), (7, 5)],
                'odds': {
                    VIKTOR_TROICKI: 1.05,
                    YANKI_EREL: 9.80
                }
            },

            # 2019-06-23
            {
                'round': 256,
                'players': [
                    JC_ARAGONE,
                    MARC_ANDREA_HUESLER
                ],
                'score': [(6, 1), (6, 4)]
            },
            {
                'round': 256,
                'players': [
                    KEVIN_KRAWIETZ,
                    GONCALO_OLIVEIRA
                ],
                'score': [(6, 4), (3, 6), (7, 6)]
            },
            {
                'round': 256,
                'players': [
                    STEVE_DARCIS,
                    CARLOS_GOMEZ_HERRERA
                ],
                'score': [(6, 3), (6, 3)]
            },
            {
                'round': 256,
                'players': [
                    VIKTOR_TROICKI,
                    ROBERTO_ORTEGA_OLMEDO
                ],
                'score': [(3, 6), (7, 6), (6, 2)]
            },
            {
                'round': 32,
                'players': [
                    MIOMIR_KECMANOVIC,
                    JAUME_MUNAR
                ],
                'score': [(6, 4), (6, 3)]
            },
            {
                'round': 32,
                'players': [
                    LORENZO_SONEGO,
                    JOAO_SOUSA
                ],
                'score': [(6, 3), (7, 6)]
            },

            # 2019-06-24
            {
                'round': 32,
                'players': [
                    VIKTOR_TROICKI,
                    JOZEF_KOVALIK
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    VIKTOR_TROICKI: 1.31,
                    JOZEF_KOVALIK: 3.50
                }
            },
            {
                'round': 32,
                'players': [
                    BRADLEY_KLAHN,
                    STEVE_DARCIS
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    BRADLEY_KLAHN: 2.55,
                    STEVE_DARCIS: 1.45
                }
            },
            {
                'round': 32,
                'players': [
                    PRAJNESH_GUNNESWARAN,
                    JANKO_TIPSAREVIC
                ],
                'score': [(6, 0), (7, 6)],
                'odds': {
                    PRAJNESH_GUNNESWARAN: 2.30,
                    JANKO_TIPSAREVIC: 1.61
                }
            },
            {
                'round': 32,
                'players': [
                    PETER_GOJOWCZYK,
                    ERGI_KIRKIN
                ],
                'score': [(6, 3), (6, 7), (6, 2)],
                'odds': {
                    PETER_GOJOWCZYK: 1.15,
                    ERGI_KIRKIN: 5.13
                }
            },
            {
                'round': 32,
                'players': [
                    ALTUG_CELIKBILEK,
                    ERNESTS_GULBIS
                ],
                'score': [(6, 3), (4, 6), (6, 4)],
                'odds': {
                    ALTUG_CELIKBILEK: 5.00,
                    ERNESTS_GULBIS: 1.15
                }
            },
            {
                'round': 32,
                'players': [
                    ROBERTO_CARBALLES_BAENA,
                    JC_ARAGONE
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 1.63,
                    JC_ARAGONE: 2.36
                }
            },
            {
                'round': 32,
                'players': [
                    BERNARD_TOMIC,
                    ANDREAS_SEPPI
                ],
                'score': [(4, 6), (6, 4), (6, 4)],
                'odds': {
                    BERNARD_TOMIC: 2.40,
                    ANDREAS_SEPPI: 1.57
                }
            },
            {
                'round': 32,
                'players': [
                    UGO_HUMBERT,
                    FEDERICO_DELBONIS
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    UGO_HUMBERT: 1.38,
                    FEDERICO_DELBONIS: 2.95
                }
            },
            {
                'round': 32,
                'players': [
                    DAMIR_DZUMHUR,
                    MATTHEW_EBDEN
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    DAMIR_DZUMHUR: 2.35,
                    MATTHEW_EBDEN: 1.56
                }
            },

            # 2019-06-25
            {
                'round': 32,
                'players': [
                    KEVIN_KRAWIETZ,
                    CEM_ILKEL
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    KEVIN_KRAWIETZ: 1.85,
                    CEM_ILKEL: 1.93
                }
            },
            {
                'round': 16,
                'players': [
                    LORENZO_SONEGO,
                    PRAJNESH_GUNNESWARAN
                ],
                'score': [(6, 7), (6, 0), (7, 5)],
                'odds': {
                    LORENZO_SONEGO: 1.48,
                    PRAJNESH_GUNNESWARAN: 2.55
                }
            },
            {
                'round': 16,
                'players': [
                    DAMIR_DZUMHUR,
                    ALTUG_CELIKBILEK
                ],
                'score': [(6, 3), (4, 6), (6, 3)],
                'odds': {
                    DAMIR_DZUMHUR: 1.13,
                    ALTUG_CELIKBILEK: 5.50
                }
            },
            {
                'round': 16,
                'players': [
                    JORDAN_THOMPSON,
                    BRADLEY_KLAHN
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    JORDAN_THOMPSON: 1.30,
                    BRADLEY_KLAHN: 3.70
                }
            },
            {
                'round': 16,
                'players': [
                    ADRIAN_MANNARINO,
                    ROBERTO_CARBALLES_BAENA
                ],
                'score': [(3, 6), (6, 1), (7, 5)],
                'odds': {
                    ADRIAN_MANNARINO: 1.33,
                    ROBERTO_CARBALLES_BAENA: 3.45
                }
            },

            # 2019-06-26
            {
                'round': 16,
                'players': [
                    BERNARD_TOMIC,
                    PETER_GOJOWCZYK
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    BERNARD_TOMIC: 1.59,
                    PETER_GOJOWCZYK: 2.12
                }
            },
            {
                'round': 16,
                'players': [
                    MIOMIR_KECMANOVIC,
                    UGO_HUMBERT
                ],
                'score': [(6, 4), (7, 5)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.77,
                    UGO_HUMBERT: 1.95
                }
            },
            {
                'round': 16,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    KEVIN_KRAWIETZ
                ],
                'score': [(7, 6), (6, 4)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 1.51,
                    KEVIN_KRAWIETZ: 2.55
                }
            },
            {
                'round': 16,
                'players': [
                    VIKTOR_TROICKI,
                    BENOIT_PAIRE
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    VIKTOR_TROICKI: 2.02,
                    BENOIT_PAIRE: 1.64
                }
            },

            # 2019-06-27
            {
                'round': 8,
                'players': [
                    MIOMIR_KECMANOVIC,
                    VIKTOR_TROICKI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    MIOMIR_KECMANOVIC: 1.65,
                    VIKTOR_TROICKI: 2.20
                }
            },
            {
                'round': 8,
                'players': [
                    PABLO_CARRENO_BUSTA,
                    BERNARD_TOMIC
                ],
                'score': [(6, 7), (6, 4), (6, 4)],
                'odds': {
                    PABLO_CARRENO_BUSTA: 2.40,
                    BERNARD_TOMIC: 1.56
                }
            },
            {
                'round': 8,
                'players': [
                    JORDAN_THOMPSON,
                    DAMIR_DZUMHUR
                ],
                'score': [(7, 5), (1, 0)],
                'retired': True,
                'odds': {
                    JORDAN_THOMPSON: 1.40,
                    DAMIR_DZUMHUR: 3.02
                }
            },
            {
                'round': 8,
                'players': [
                    LORENZO_SONEGO,
                    ADRIAN_MANNARINO
                ],
                'score': [(3, 6), (7, 6), (6, 3)],
                'odds': {
                    LORENZO_SONEGO: 2.68,
                    ADRIAN_MANNARINO: 1.47
                }
            },

            # 2019-06-28
            {
                'round': 4,
                'players': [
                    MIOMIR_KECMANOVIC,
                    JORDAN_THOMPSON
                ],
                'score': [(6, 7), (7, 6), (7, 6)],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.41,
                    JORDAN_THOMPSON: 1.62
                }
            },

            # 2019-06-29
            {
                'round': 4,
                'players': [
                    LORENZO_SONEGO,
                    PABLO_CARRENO_BUSTA
                ],
                'score': [(6, 3), (7, 6)],
                # no odds
            },
            {
                'round': 2,
                'players': [
                    LORENZO_SONEGO,
                    MIOMIR_KECMANOVIC
                ],
                'score': [(6, 7), (7, 6), (6, 1)],
                'odds': {
                    LORENZO_SONEGO: 1.77,
                    MIOMIR_KECMANOVIC: 2.02
                }
            }
        ]
    },

    {
        'name': 'Nature Valley International',
        'category': 'ATP250',
        'date': '2019-06-29',
        'location': 'Eastbourne, Great Britain',
        'matches': [

            # 2019-06-22
            {
                'round': 512,
                'players': [
                    PAUL_JUBB,
                    DENIS_ISTOMIN
                ],
                'score': [(6, 2), (5, 7), (7, 6)],
                'odds': {
                    PAUL_JUBB: 2.95,
                    DENIS_ISTOMIN: 1.34
                }
            },
            {
                'round': 512,
                'players': [
                    THOMAS_FABBIANO,
                    KENNY_DE_SCHEPPER
                ],
                'score': [(2, 6), (6, 3), (7, 6)],
                'odds': {
                    THOMAS_FABBIANO: 3.45,
                    KENNY_DE_SCHEPPER: 3.45
                }
            },
            {
                'round': 512,
                'players': [
                    TENNYS_SANDGREN,
                    THAI_SON_KWIATKOWSKI
                ],
                'score': [(6, 4), (6, 1)],
                'odds': {
                    TENNYS_SANDGREN: 1.65,
                    THAI_SON_KWIATKOWSKI: 2.07
                }
            },
            {
                'round': 512,
                'players': [
                    JAMES_WARD,
                    LLOYD_HARRIS
                ],
                'score': [(4, 6), (7, 6), (6, 4)],
                'odds': {
                    JAMES_WARD: 1.67,
                    LLOYD_HARRIS: 2.10
                }
            },
            {
                'round': 512,
                'players': [
                    ALEXANDER_BUBLIK,
                    STEVEN_DIEZ
                ],
                'score': [(4, 6), (6, 0), (6, 3)],
                'odds': {
                    ALEXANDER_BUBLIK: 1.22,
                    STEVEN_DIEZ: 4.19
                }
            },
            {
                'round': 512,
                'players': [
                    ANDREY_RUBLEV,
                    MAX_PURCELL
                ],
                'score': [(7, 5), (6, 7), (6, 3)],
                'odds': {
                    ANDREY_RUBLEV: 1.30,
                    MAX_PURCELL: 3.20
                }
            },
            {
                'round': 512,
                'players': [
                    DENIS_KUDLA,
                    DANIEL_MASUR
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    DENIS_KUDLA: 1.13,
                    DANIEL_MASUR: 5.20
                }
            },
            {
                'round': 512,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    GUIDO_ANDREOZZI
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    JUAN_IGNACIO_LONDERO: 1.94,
                    GUIDO_ANDREOZZI: 1.69
                }
            },

            # 2019-06-23
            {
                'round': 256,
                'players': [
                    TENNYS_SANDGREN,
                    ALEXANDER_BUBLIK
                ],
                'score': [(4, 6), (6, 4), (6, 3)],
                'odds': {
                    TENNYS_SANDGREN: 2.05,
                    ALEXANDER_BUBLIK: 1.59
                }
            },
            {
                'round': 256,
                'players': [
                    PAUL_JUBB,
                    ANDREY_RUBLEV
                ],
                'score': [(4, 6), (6, 3), (6, 2)],
                'odds': {
                    PAUL_JUBB: 3.00,
                    ANDREY_RUBLEV: 1.28
                }
            },
            {
                'round': 256,
                'players': [
                    JAMES_WARD,
                    DENIS_KUDLA
                ],
                'score': [(6, 3), (6, 2)],
                'odds': {
                    JAMES_WARD: 2.90,
                    DENIS_KUDLA: 1.32
                }
            },
            {
                'round': 256,
                'players': [
                    THOMAS_FABBIANO,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(7, 5), (6, 4)],
                'odds': {
                    THOMAS_FABBIANO: 1.53,
                    JUAN_IGNACIO_LONDERO: 2.35
                }
            },

            # 2019-06-24
            {
                'round': 32,
                'players': [
                    SAM_QUERREY,
                    MIKHAIL_KUKUSHKIN
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    SAM_QUERREY: 1.71,
                    MIKHAIL_KUKUSHKIN: 2.10
                }
            },
            {
                'round': 32,
                'players': [
                    STEVE_JOHNSON,
                    REILLY_OPELKA
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    STEVE_JOHNSON: 1.53,
                    REILLY_OPELKA: 2.55
                }
            },
            {
                'round': 32,
                'players': [
                    TAYLOR_FRITZ,
                    PAUL_JUBB
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    TAYLOR_FRITZ: 1.32,
                    PAUL_JUBB: 3.40
                }
            },
            {
                'round': 32,
                'players': [
                    HUBERT_HURKACZ,
                    MARCO_CECCHINATO
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    HUBERT_HURKACZ: 1.48,
                    MARCO_CECCHINATO: 2.75
                }
            },
            {
                'round': 32,
                'players': [
                    FERNANDO_VERDASCO,
                    JOHN_MILLMAN
                ],
                'score': [(6, 7), (6, 4), (6, 1)],
                'odds': {
                    FERNANDO_VERDASCO: 1.95,
                    JOHN_MILLMAN: 1.77
                }
            },

            # 2019-06-25
            {
                'round': 32,
                'players': [
                    CAMERON_NORRIE,
                    JEREMY_CHARDY
                ],
                'score': [(6, 3), (7, 6)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    JUAN_IGNACIO_LONDERO,
                    JAY_CLARKE
                ],
                'score': [(6, 7), (6, 1), (6, 3)],
                # no odds
            },
            {
                'round': 32,
                'players': [
                    NICOLAS_JARRY,
                    PABLO_CUEVAS
                ],
                'score': [(6, 1), (7, 6)],
                'odds': {
                    NICOLAS_JARRY: 1.54,
                    PABLO_CUEVAS: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    PIERRE_HUGUES_HERBERT,
                    DENIS_KUDLA
                ],
                'score': [(5, 7), (7, 6), (6, 4)],
                'odds': {
                    PIERRE_HUGUES_HERBERT: 1.53,
                    DENIS_KUDLA: 2.45
                }
            },
            {
                'round': 32,
                'players': [
                    THOMAS_FABBIANO,
                    JAMES_WARD
                ],
                'score': [(2, 6), (6, 3), (6, 1)],
                'odds': {
                    THOMAS_FABBIANO: 2.12,
                    JAMES_WARD: 1.63
                }
            },
            {
                'round': 32,
                'players': [
                    DANIEL_EVANS,
                    RADU_ALBOT
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    DANIEL_EVANS: 1.50,
                    RADU_ALBOT: 2.60
                }
            },
            {
                'round': 32,
                'players': [
                    GILLES_SIMON,
                    TENNYS_SANDGREN
                ],
                'score': [(7, 5), (6, 1)],
                'odds': {
                    GILLES_SIMON: 1.59,
                    TENNYS_SANDGREN: 2.30
                }
            },

            # 2019-06-26
            {
                'round': 16,
                'players': [
                    HUBERT_HURKACZ,
                    STEVE_JOHNSON
                ],
                'score': [(6, 3), (7, 6)],
                'odds': {
                    HUBERT_HURKACZ: 2.30,
                    STEVE_JOHNSON: 1.53
                }
            },
            {
                'round': 16,
                'players': [
                    DANIEL_EVANS,
                    PIERRE_HUGUES_HERBERT
                ],
                'score': [(6, 3), (7, 5)],
                'odds': {
                    DANIEL_EVANS: 1.63,
                    PIERRE_HUGUES_HERBERT: 2.23
                }
            },
            {
                'round': 16,
                'players': [
                    GILLES_SIMON,
                    NICOLAS_JARRY
                ],
                'score': [(6, 2), (6, 4)],
                'odds': {
                    GILLES_SIMON: 1.75,
                    NICOLAS_JARRY: 2.09
                }
            },
            {
                'round': 16,
                'players': [
                    FERNANDO_VERDASCO,
                    JUAN_IGNACIO_LONDERO
                ],
                'score': [(6, 7), (6, 3), (7, 6)],
                'odds': {
                    FERNANDO_VERDASCO: 1.28,
                    JUAN_IGNACIO_LONDERO: 3.75
                }
            },
            {
                'round': 16,
                'players': [
                    SAM_QUERREY,
                    DUSAN_LAJOVIC
                ],
                'score': [(6, 2), (6, 3)],
                'odds': {
                    SAM_QUERREY: 1.29,
                    DUSAN_LAJOVIC: 3.40
                }
            },
            {
                'round': 16,
                'players': [
                    KYLE_EDMUND,
                    CAMERON_NORRIE
                ],
                'score': [(6, 2), (6, 2)],
                'odds': {
                    KYLE_EDMUND: 1.59,
                    CAMERON_NORRIE: 2.35
                }
            },
            {
                'round': 16,
                'players': [
                    THOMAS_FABBIANO,
                    LASLO_DJERE
                ],
                'score': [(7, 6), (7, 6)],
                'odds': {
                    THOMAS_FABBIANO: 1.63,
                    LASLO_DJERE: 2.19
                }
            },
            {
                'round': 16,
                'players': [
                    TAYLOR_FRITZ,
                    GUIDO_PELLA
                ],
                'score': [(6, 4), (3, 6), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 1.31,
                    GUIDO_PELLA: 3.15
                }
            },

            # 2019-06-27
            {
                'round': 8,
                'players': [
                    TAYLOR_FRITZ,
                    HUBERT_HURKACZ
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    TAYLOR_FRITZ: 1.67,
                    HUBERT_HURKACZ: 2.20
                }
            },
            {
                'round': 8,
                'players': [
                    THOMAS_FABBIANO,
                    GILLES_SIMON
                ],
                'score': [(6, 4), (6, 3)],
                'odds': {
                    THOMAS_FABBIANO: 4.28,
                    GILLES_SIMON: 1.19
                }
            },
            {
                'round': 8,
                'players': [
                    SAM_QUERREY,
                    FERNANDO_VERDASCO
                ],
                'score': [(7, 6), (6, 2)],
                'odds': {
                    SAM_QUERREY: 1.43,
                    FERNANDO_VERDASCO: 2.74
                }
            },
            {
                'round': 8,
                'players': [
                    KYLE_EDMUND,
                    DANIEL_EVANS
                ],
                'score': [(1, 6), (6, 3), (6, 4)],
                'odds': {
                    KYLE_EDMUND: 1.80,
                    DANIEL_EVANS: 2.00
                }
            },

            # 2019-06-28
            {
                'round': 4,
                'players': [
                    SAM_QUERREY,
                    THOMAS_FABBIANO
                ],
                'score': [(6, 3), (6, 7), (6, 3)],
                'odds': {
                    SAM_QUERREY: 1.21,
                    THOMAS_FABBIANO: 4.10
                }
            },
            {
                'round': 4,
                'players': [
                    TAYLOR_FRITZ,
                    KYLE_EDMUND
                ],
                'score': [(7, 6), (6, 3)],
                'odds': {
                    TAYLOR_FRITZ: 2.60,
                    KYLE_EDMUND: 1.51
                }
            },

            # 2019-06-29
            {
                'round': 2,
                'players': [
                    TAYLOR_FRITZ,
                    SAM_QUERREY
                ],
                'score': [(6, 3), (6, 4)],
                'odds': {
                    TAYLOR_FRITZ: 2.35,
                    SAM_QUERREY: 1.61
                }
            }
        ]
    },

    {
        'name': 'Wimbledon',
        'category': 'ATP2000',
        'date': '2019-07-14',
        'location': 'London, Great Britian',
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
                    CRISTIAN_GARIN
                ],
                'score': [(4, 6), (6, 4), (7, 5), (6, 4)],
                'odds': {
                    ANDREY_RUBLEV: 2.55,
                    CRISTIAN_GARIN: 1.53
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
        'name': 'Hall of Fame Open',
        'category': 'ATP250',
        'date': '2019-07-21',
        'location': 'Newport, United States',
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
        'name': 'Plava Laguna Croatia Open Umag',
        'category': 'ATP250',
        'date': '2019-07-21',
        'location': 'Umag, Croatia',
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
        'name': 'Swedish Open',
        'category': 'ATP250',
        'date': '2019-07-21',
        'location': 'Bastad, Sweden',
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
                    CRISTIAN_GARIN
                ],
                'score': [(6, 4), (6, 4)],
                'odds': {
                    JEREMY_CHARDY: 2.40,
                    CRISTIAN_GARIN: 1.57
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

    ###############################################################################
    # Active
    ###############################################################################

    {
        'name': 'BB&T Atlanta Open',
        'date': '2019-07-28',
        'location': 'Atlanta, United States',
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
                'score': [(7, 5), 6, 4],
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

            # 2016-09-26
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
            {
                'round': 8,
                'players': [
                    ALEX_DE_MINAUR,
                    BERNARD_TOMIC
                ],
                'odds': {
                    ALEX_DE_MINAUR: 1.34,
                    BERNARD_TOMIC: 3.20
                },
                'prediction': BERNARD_TOMIC,
                'bet': 20,
            },
            {
                'round': 8,
                'players': [
                    REILLY_OPELKA,
                    DANIEL_EVANS
                ],
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
                    MIOMIR_KECMANOVIC,
                    TAYLOR_FRITZ
                ],
                'odds': {
                    MIOMIR_KECMANOVIC: 2.70,
                    TAYLOR_FRITZ: 1.45
                },
                'prediction': TAYLOR_FRITZ,
                'bet': 10,
            }
        ]
    },

    {
        'name': 'J Safra Sarasin Swiss Open Gstaad',
        'date': '2019-07-28',
        'location': 'Gstaad, Switzerland',
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
                    CEDRIC_MARCEL_STEBE: 2.70,
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
                    ROBERTO_CARBALLES_BAENA: 1.55,
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
                    JOAO_SOUSA: 1.48,
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
                    ROBERTO_CARBALLES_BAENA,
                    ALBERT_RAMOS_VINOLAS
                ],
                'odds': {
                    ROBERTO_CARBALLES_BAENA: 2.30,
                    ALBERT_RAMOS_VINOLAS: 1.60
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
                    ROBERTO_BAUTISTA_AGUT,
                    JOAO_SOUSA
                ],
                'odds': {
                    ROBERTO_BAUTISTA_AGUT: 1.24,
                    JOAO_SOUSA: 4.00
                },
                'prediction': ROBERTO_BAUTISTA_AGUT,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    THOMAS_FABBIANO,
                    CEDRIC_MARCEL_STEBE
                ],
                'odds': {
                    THOMAS_FABBIANO: 1.90,
                    CEDRIC_MARCEL_STEBE: 1.90
                },
                'prediction': CEDRIC_MARCEL_STEBE,
                'bet': 10,
            }
        ]
    },

    {
        'name': 'Hamburg European Open',
        'date': '2019-07-28',
        'location': 'Hamburg, Germany',
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
                    CRISTIAN_GARIN
                ],
                'score': [(6, 4), (7, 6)],
                'odds': {
                    ANDREY_RUBLEV: 2.13,
                    CRISTIAN_GARIN: 1.67
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
                    JEREMY_CHARDY,
                    NIKOLOZ_BASILASHVILI
                ],
                'odds': {
                    JEREMY_CHARDY: 2.00,
                    NIKOLOZ_BASILASHVILI: 1.80
                },
                'prediction': JEREMY_CHARDY,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    DOMINIC_THIEM,
                    ANDREY_RUBLEV
                ],
                'odds': {
                    DOMINIC_THIEM: 1.14,
                    ANDREY_RUBLEV: 5.50
                },
                'prediction': DOMINIC_THIEM,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    FILIP_KRAJINOVIC,
                    ALEXANDER_ZVEREV
                ],
                'odds': {
                    FILIP_KRAJINOVIC: 3.10,
                    ALEXANDER_ZVEREV: 1.36
                },
                'prediction': ALEXANDER_ZVEREV,
                'bet': 10,
            },
            {
                'round': 8,
                'players': [
                    FABIO_FOGNINI,
                    PABLO_CARRENO_BUSTA
                ],
                'odds': {
                    FABIO_FOGNINI: 2.00,
                    PABLO_CARRENO_BUSTA: 1.80
                },
                'prediction': PABLO_CARRENO_BUSTA,
                'bet': 10,
            }
        ]
    }
]
