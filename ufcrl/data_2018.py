from fighters import *

DATA_2018 = [
    {
        'date': '2018-01-14',
        'name': 'UFC Fight Night: Stephens vs Choi',
        'location': 'St. Louis, Missouri',
        'venue': 'Scottrade Center',
        'fights': [
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_SANTIAGO,
                        'stats': '21-12-0',
                    },
                    {
                        'name': MADS_BURNELL,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': MADS_BURNELL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    MADS_BURNELL: 2.50,
                    MIKE_SANTIAGO: 1.49,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JJ_ALDRICH,
                        'stats': '7-3-0',
                    },
                    {
                        'name': DANIELLE_TAYLOR,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': JJ_ALDRICH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    JJ_ALDRICH: 1.74,
                    DANIELLE_TAYLOR: 2.05,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KALINDRA_FARIA,
                        'stats': '18-8-1',
                    },
                    {
                        'name': JESSICA_EYE,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_EYE,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    JESSICA_EYE: 1.71,
                    KALINDRA_FARIA: 2.10,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GUIDO_CANNETTI,
                        'stats': '8-5-0',
                    },
                    {
                        'name': KYUNG_HO_KANG,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': KYUNG_HO_KANG,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:53',
                },
                'time': '20:00',
                'odds': {
                    KYUNG_HO_KANG: 1.32,
                    GUIDO_CANNETTI: 3.40,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': TALITA_BERNARDO,
                        'stats': '6-3-0',
                    },
                    {
                        'name': IRENE_ALDANA,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': IRENE_ALDANA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    IRENE_ALDANA: 1.67,
                    TALITA_BERNARDO: 2.20,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MATT_FREVOLA,
                        'stats': '6-1-1',
                    },
                    {
                        'name': MARC_POLO_REYES,
                        'stats': '8-5-0',
                    },
                ],
                'winner': {
                    'fighter': MARC_POLO_REYES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:00',
                },
                'time': '21:00',
                'odds': {
                    MARC_POLO_REYES: 2.70,
                    MATT_FREVOLA: 1.48,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_JOHNSON,
                        'stats': '20-14-0',
                    },
                    {
                        'name': DARREN_ELKINS,
                        'stats': '25-7-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_ELKINS,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:22',
                },
                'time': '22:00',
                'odds': {
                    DARREN_ELKINS: 2.65,
                    MICHAEL_JOHNSON: 1.48,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': EMIL_MEEK,
                        'stats': '9-4-1',
                    },
                    {
                        'name': KAMARU_USMAN,
                        'stats': '15-1-0',
                    },
                ],
                'winner': {
                    'fighter': KAMARU_USMAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    KAMARU_USMAN: 1.13,
                    EMIL_MEEK: 5.25,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JESSICA_ROSE_CLARK,
                        'stats': '9-5-0',
                    },
                    {
                        'name': PAIGE_VANZANT,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ROSE_CLARK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    JESSICA_ROSE_CLARK: 1.91,
                    PAIGE_VANZANT: 1.74,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': DOOHO_CHOI,
                        'stats': '14-3-0',
                    },
                    {
                        'name': JEREMY_STEPHENS,
                        'stats': '28-16-0',
                    },
                ],
                'winner': {
                    'fighter': JEREMY_STEPHENS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:36',
                },
                'time': '23:30',
                'odds': {
                    JEREMY_STEPHENS: 2.35,
                    DOOHO_CHOI: 1.59,
                },
            },
        ]
    },

    {
        'date': '2018-01-20',
        'name': 'UFC 220: Miocic vs Ngannou',
        'location': 'Boston, Massachusetts',
        'venue': 'TD Garden',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ISLAM_MAKHACHEV,
                        'stats': '16-1-0',
                    },
                    {
                        'name': GLEISON_TIBAU,
                        'stats': '40-14-0',
                    },
                ],
                'winner': {
                    'fighter': ISLAM_MAKHACHEV,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:57',
                },
                'time': '18:30',
                'odds': {
                    ISLAM_MAKHACHEV: 1.33,
                    GLEISON_TIBAU: 3.35,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MATT_BESSETTE,
                        'stats': '22-9-0',
                    },
                    {
                        'name': ENRIQUE_BARZOLA,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': ENRIQUE_BARZOLA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ENRIQUE_BARZOLA: 1.35,
                    MATT_BESSETTE: 3.25,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JULIO_ACRE,
                        'stats': '15-3-0',
                    },
                    {
                        'name': DAN_IGE,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': JULIO_ACRE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    JULIO_ACRE: 1.67,
                    DAN_IGE: 2.20,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDRE_PANTOJA,
                        'stats': '20-3-0',
                    },
                    {
                        'name': DUSTIN_ORTIZ,
                        'stats': '19-8-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_ORTIZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    DUSTIN_ORTIZ: 1.77,
                    ALEXANDRE_PANTOJA: 2.00,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ABDUL_RAZAK_ALHASSAN,
                        'stats': '21-3-0',
                    },
                    {
                        'name': SABAH_HOMASI,
                        'stats': '11-8-0',
                    },
                ],
                'winner': {
                    'fighter': ABDUL_RAZAK_ALHASSAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:47',
                },
                'time': '21:00',
                'odds': {
                    ABDUL_RAZAK_ALHASSAN: 1.44,
                    SABAH_HOMASI: 2.71,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BRANDON_DAVIS,
                        'stats': '9-5-0',
                    },
                    {
                        'name': KYLE_BOCHNIAK,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': KYLE_BOCHNIAK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    KYLE_BOCHNIAK: 2.18,
                    BRANDON_DAVIS: 1.65,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': THOMAS_ALMEIDA,
                        'stats': '21-3-0',
                    },
                    {
                        'name': ROB_FONT,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': ROB_FONT,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:24',
                },
                'time': '22:00',
                'odds': {
                    ROB_FONT: 2.15,
                    THOMAS_ALMEIDA: 1.67,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GIAN_VILLANTE,
                        'stats': '17-11-0',
                    },
                    {
                        'name': FRANCIMAR_BARROSO,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': GIAN_VILLANTE,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    GIAN_VILLANTE: 1.59,
                    FRANCIMAR_BARROSO: 2.29,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CALVIN_KATTAR,
                        'stats': '19-3-0',
                    },
                    {
                        'name': SHANE_BURGOS,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': CALVIN_KATTAR,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:32',
                },
                'time': '23:00',
                'odds': {
                    CALVIN_KATTAR: 2.90,
                    SHANE_BURGOS: 1.40,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': VOLKAN_OEZDEMIR,
                        'stats': '15-4-0',
                    },
                    {
                        'name': DANIEL_CORMIER,
                        'stats': '22-1-0',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_CORMIER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:00',
                },
                'time': '23:30',
                'odds': {
                    DANIEL_CORMIER: 1.26,
                    VOLKAN_OEZDEMIR: 3.60,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': FRANCIS_NGANNOU,
                        'stats': '13-3-0',
                    },
                    {
                        'name': STIPE_MIOCIC,
                        'stats': '18-3-0',
                    },
                ],
                'winner': {
                    'fighter': STIPE_MIOCIC,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    STIPE_MIOCIC: 2.43,
                    FRANCIS_NGANNOU: 1.57,
                },
            },
        ]
    },

    {
        'date': '2018-01-27',
        'name': 'UFC Fight Night: Jacare vs Brunson 2',
        'location': 'Charlotte, North Carolina',
        'venue': 'Spectrum Center',
        'fights': [
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CORY_SANDHAGEN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': AUSTIN_ARNETT,
                        'stats': '16-6-0',
                    },
                ],
                'winner': {
                    'fighter': CORY_SANDHAGEN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:48',
                },
                'time': '16:00',
                'odds': {
                    CORY_SANDHAGEN: 1.48,
                    AUSTIN_ARNETT: 2.66,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NIKO_PRICE,
                        'stats': '13-2-0',
                    },
                    {
                        'name': GEORGE_SULLIVAN,
                        'stats': '17-7-0',
                    },
                ],
                'winner': {
                    'fighter': NIKO_PRICE,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:21',
                },
                'time': '16:30',
                'odds': {
                    NIKO_PRICE: 1.26,
                    GEORGE_SULLIVAN: 3.86,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOAQUIM_SILVA,
                        'stats': '11-1-0',
                    },
                    {
                        'name': VINC_PICHEL,
                        'stats': '16-6-0',
                    },
                ],
                'winner': {
                    'fighter': VINC_PICHEL,
                    'by': '11-2-0',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:00',
                'odds': {
                    VINC_PICHEL: 2.01,
                    JOAQUIM_SILVA: 1.69,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JI_YEON_KIM,
                        'stats': '7-2-2',
                    },
                    {
                        'name': JUSTINE_KISH,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': JI_YEON_KIM,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:30',
                'odds': {
                    JI_YEON_KIM: 2.40,
                    JUSTINE_KISH: 1.57,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': RANDA_MARKOS,
                        'stats': '9-7-1',
                    },
                    {
                        'name': JULIANA_LIMA,
                        'stats': '9-5-0',
                    },
                ],
                'winner': {
                    'fighter': RANDA_MARKOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:00',
                'odds': {
                    RANDA_MARKOS: 1.63,
                    JULIANA_LIMA: 2.30,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MARA_ROMERO_BORELLA,
                        'stats': '13-5-0',
                    },
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': KATLYN_CHOOKAGIAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    KATLYN_CHOOKAGIAN: 1.50,
                    MARA_ROMERO_BORELLA: 2.45,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MIRSAD_BEKTIC,
                        'stats': '13-1-0',
                    },
                    {
                        'name': GODOFREDO_PEPEY,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': MIRSAD_BEKTIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:47',
                },
                'time': '19:00',
                'odds': {
                    MIRSAD_BEKTIC: 1.15,
                    GODOFREDO_PEPEY: 5.10,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ERIK_KOCH,
                        'stats': '15-6-0',
                    },
                    {
                        'name': BOBBY_GREEN,
                        'stats': '24-9-1',
                    },
                ],
                'winner': {
                    'fighter': BOBBY_GREEN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    BOBBY_GREEN: 1.50,
                    ERIK_KOCH: 2.45,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': FRANK_CAMACHO,
                        'stats': '21-7-0',
                    },
                    {
                        'name': DREW_DOBER,
                        'stats': '20-9-0',
                    },
                ],
                'winner': {
                    'fighter': DREW_DOBER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    DREW_DOBER: 1.64,
                    FRANK_CAMACHO: 2.20,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GREGOR_GILLESPIE,
                        'stats': '13-0-0',
                    },
                    {
                        'name': JORDAN_RINALDI,
                        'stats': '14-7-0',
                    },
                ],
                'winner': {
                    'fighter': GREGOR_GILLESPIE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:46'','
                },
                'time': '21:00',
                'odds': {
                    GREGOR_GILLESPIE: 1.17,
                    JORDAN_RINALDI: 5.00,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_FILI,
                        'stats': '19-6-0',
                    },
                    {
                        'name': DENNIS_BERMUDEZ,
                        'stats': '18-9-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_FILI,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    ANDRE_FILI: 2.31,
                    DENNIS_BERMUDEZ: 1.54,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACARE_SOUZA,
                        'stats': '26-6-0',
                    },
                    {
                        'name': DEREK_BRUNSON,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': JACARE_SOUZA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:50',
                },
                'time': '22:00',
                'odds': {
                    JACARE_SOUZA: 2.15,
                    DEREK_BRUNSON: 1.68,
                },
            },
        ]
    },

    {
        'date': '2018-02-03',
        'name': 'UFC Fight Night: Machida vs Anders',
        'location': 'Belem, Brazil',
        'venue': 'Arena Guilherme Paraense (Mangueirinho)',
        'fights': [
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOSEPH_MORALES,
                        'stats': '9-2-0',
                    },
                    {
                        'name': DEIVESON_FIGUEIREDO,
                        'stats': '15-1-0',
                    },
                ],
                'winner': {
                    'fighter': DEIVESON_FIGUEIREDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:34',
                },
                'time': '19:30',
                'odds': {
                    DEIVESON_FIGUEIREDO: 1.94,
                    JOSEPH_MORALES: 1.74,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JOE_SOTO,
                        'stats': '18-7-0',
                    },
                    {
                        'name': IURI_ALCANTARA,
                        'stats': '35-10-0',
                    },
                ],
                'winner': {
                    'fighter': IURI_ALCANTARA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:06',
                },
                'time': '21:00',
                'odds': {
                    IURI_ALCANTARA: 1.74,
                    JOE_SOTO: 1.97,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': POLYANA_VIANA,
                        'stats': '10-3-0',
                    },
                    {
                        'name': MAIA_STEVENSON,
                        'stats': '6-5-0',
                    },
                ],
                'winner': {
                    'fighter': POLYANA_VIANA,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:50',
                },
                'time': '20:30',
                'odds': {
                    POLYANA_VIANA: 1.20,
                    MAIA_STEVENSON: 4.45,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAMIR_HADZOVIC,
                        'stats': '13-4-0',
                    },
                    {
                        'name': ALAN_PATRICK,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': ALAN_PATRICK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    ALAN_PATRICK: 1.38,
                    DAMIR_HADZOVIC: 3.05,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                    {
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                ],
                'winner': {
                    'fighter': SERGIO_MORAES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    SERGIO_MORAES: 2.65,
                    TIM_MEANS: 1.44,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:03',
                },
                'time': '22:00',
                'odds': {
                    THIAGO_SANTOS: 1.38,
                    ANTHONY_SMITH: 2.95,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                    {
                        'name': DOUGLAS_SILVA_DE_ANDRADE,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': DOUGLAS_SILVA_DE_ANDRADE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    DOUGLAS_SILVA_DE_ANDRADE: 2.65,
                    MARLON_VERA: 1.48,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCELO_GOLM,
                        'stats': '6-2-0',
                    },
                    {
                        'name': TIM_JOHNSON,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': TIM_JOHNSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    TIM_JOHNSON: 2.47,
                    MARCELO_GOLM: 1.54,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DESMOND_GREEN,
                        'stats': '22-8-0',
                    },
                    {
                        'name': MICHEL_PRAZERES,
                        'stats': '26-3-0',
                    },
                ],
                'winner': {
                    'fighter': MICHEL_PRAZERES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    MICHEL_PRAZERES: 1.74,
                    DESMOND_GREEN: 2.05,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': PRISCILA_CACHOEIRA,
                        'stats': '8-2-0',
                    },
                    {
                        'name': VALENTINA_SHEVCHENKO,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': VALENTINA_SHEVCHENKO,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:25',
                },
                'time': '23:59',
                'odds': {
                    VALENTINA_SHEVCHENKO: 1.08,
                    PRISCILA_CACHOEIRA: 7.50,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                    {
                        'name': LYOTO_MACHIDA,
                        'stats': '24-8-0',
                    },
                ],
                'winner': {
                    'fighter': LYOTO_MACHIDA,
                    'by': 's.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    LYOTO_MACHIDA: 2.95,
                    ERYK_ANDERS: 1.38,
                },
            },
        ]
    },

    {
        'date': '2018-02-10',
        'name': 'UFC 221: Romero vs Rockhold',
        'location': 'Perth Australia',
        'venue': 'Perth Arena',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAICHI_ABE,
                        'stats': '6-2-0',
                    },
                    {
                        'name': LUKE_JUMEAU,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': LUKE_JUMEAU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    LUKE_JUMEAU: 2.22,
                    DAICHI_ABE: 1.63,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': TERUTO_ISHIHARA,
                        'stats': '11-6-2',
                    },
                    {
                        'name': JOSE_QUINONEZ,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': JOSE_QUINONEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    JOSE_QUINONEZ: 1.59,
                    TERUTO_ISHIHARA: 2.30,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MIZUTO_HIROTA,
                        'stats': '19-10-2',
                    },
                    {
                        'name': ROSS_PEARSON,
                        'stats': '22-16-0',
                    },
                ],
                'winner': {
                    'fighter': ROSS_PEARSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ROSS_PEARSON: 1.61,
                    MIZUTO_HIROTA: 2.29,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': BEN_NGUYEN,
                        'stats': '17-8-0',
                    },
                    {
                        'name': JUSSIER_FORMIGA,
                        'stats': '23-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUSSIER_FORMIGA,
                    'by': 'submission',
                    'round': 3,
                    'time': '1:43',
                },
                'time': '20:00',
                'odds': {
                    JUSSIER_FORMIGA: 1.89,
                    BEN_NGUYEN: 1.83,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': JEREMY_KENNEDY,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:57',
                },
                'time': '20:30',
                'odds': {
                    ALEXANDER_VOLKANOVSKI: 1.44,
                    JEREMY_KENNEDY: 2.66,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ISRAEL_ADESANYA,
                        'stats': '16-0-0',
                    },
                    {
                        'name': ROB_WILKINSON,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': ISRAEL_ADESANYA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:37',
                },
                'time': '21:00',
                'odds': {
                    ISRAEL_ADESANYA: 1.25,
                    ROB_WILKINSON: 3.85,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAMIEN_BROWN,
                        'stats': '17-12-0',
                    },
                    {
                        'name': DONG_HYUN_KIM,
                        'stats': '16-8-3',
                    },
                ],
                'winner': {
                    'fighter': DONG_HYUN_KIM,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    DONG_HYUN_KIM: 1.71,
                    DAMIEN_BROWN: 1.99,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SAPARBEG_SAFAROV,
                        'stats': '8-2-0',
                    },
                    {
                        'name': TYSON_PEDRO,
                        'stats': '7-2-0',
                    },
                ],
                'winner': {
                    'fighter': TYSON_PEDRO,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:54',
                },
                'time': '22:00',
                'odds': {
                    TYSON_PEDRO: 1.32,
                    SAPARBEG_SAFAROV: 3.40,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JAKE_MATTHEWS,
                        'stats': '13-4-0',
                    },
                    {
                        'name': LI_JINGLIANG,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': JAKE_MATTHEWS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    JAKE_MATTHEWS: 2.25,
                    LI_JINGLIANG: 1.61,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TAI_TUIVASA,
                        'stats': '10-1-0',
                    },
                    {
                        'name': CYRIL_ASKER,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': TAI_TUIVASA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:18',
                },
                'time': '23:00',
                'odds': {
                    TAI_TUIVASA: 1.33,
                    CYRIL_ASKER: 3.25,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_BLAYDES,
                        'stats': '11-2-0',
                    },
                    {
                        'name': MARK_HUNT,
                        'stats': '13-14-1',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_BLAYDES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    CURTIS_BLAYDES: 1.50,
                    MARK_HUNT: 2.55,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': YOEL_ROMERO,
                        'stats': '13-3-0',
                    },
                    {
                        'name': LUKE_ROCKHOLD,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': YOEL_ROMERO,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:48',
                },
                'time': '23:55',
                'odds': {
                    YOEL_ROMERO: 2.50,
                    LUKE_ROCKHOLD: 1.50,
                },
            },
        ]
    },

    {
        'date': '2018-02-18',
        'name': 'UFC Fight Night: Cerrone vs Medeiros',
        'location': 'Austin, Texas',
        'venue': 'Frank Erwin Center',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TIM_WILLIAMS,
                        'stats': '15-5-0',
                    },
                    {
                        'name': OSKAR_PIECHOTA,
                        'stats': '11-1-1',
                    },
                ],
                'winner': {
                    'fighter': OSKAR_PIECHOTA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:54',
                },
                'time': '18:00',
                'odds': {
                    TIM_WILLIAMS: 3.60,
                    OSKAR_PIECHOTA: 1.29,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_MORONO,
                        'stats': '16-5-0',
                    },
                    {
                        'name': JOSHUA_BURKMAN,
                        'stats': '29-17-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_MORONO,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:12',
                },
                'time': '18:30',
                'odds': {
                    ALEX_MORONO: 1.27,
                    JOSHUA_BURKMAN: 3.85,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUCIE_PUDILOVA,
                        'stats': '8-4-0',
                    },
                    {
                        'name': SARAH_MORAS,
                        'stats': '5-5-0',
                    },
                ],
                'winner': {
                    'fighter': LUCIE_PUDILOVA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    LUCIE_PUDILOVA: 1.65,
                    SARAH_MORAS: 2.25,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ROBERTO_SANCHEZ,
                        'stats': '8-2-0',
                    },
                    {
                        'name': JOBY_SANCHEZ,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': ROBERTO_SANCHEZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:50',
                },
                'time': '19:30',
                'odds': {
                    ROBERTO_SANCHEZ: 2.25,
                    JOBY_SANCHEZ: 1.61,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GEOFF_NEAL,
                        'stats': '11-2-0',
                    },
                    {
                        'name': BRIAN_CAMOZZI,
                        'stats': '7-5-0',
                    },
                ],
                'winner': {
                    'fighter': GEOFF_NEAL,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:48',
                },
                'time': '20:00',
                'odds': {
                    GEOFF_NEAL: 1.44,
                    BRIAN_CAMOZZI: 2.75,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JARED_GORDON,
                        'stats': '14-3-0',
                    },
                    {
                        'name': DIEGO_FERREIRA,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': DIEGO_FERREIRA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:58',
                },
                'time': '20:30',
                'odds': {
                    DIEGO_FERREIRA: 2.55,
                    JARED_GORDON: 1.51,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': THIBAULT_GOUTI,
                        'stats': '11-2-0',
                    },
                    {
                        'name': SAGE_NORTHCUTT,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': SAGE_NORTHCUTT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    SAGE_NORTHCUTT: 1.25,
                    THIBAULT_GOUTI: 4.00,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': STEVEN_PETERSON,
                        'stats': '17-8-0',
                    },
                    {
                        'name': BRANDON_DAVIS,
                        'stats': '9-5-0',
                    },
                ],
                'winner': {
                    'fighter': BRANDON_DAVIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    BRANDON_DAVIS: 1.63,
                    STEVEN_PETERSON: 2.30,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_MILLENDER,
                        'stats': '17-4-0',
                    },
                    {
                        'name': THIAGO_ALVES,
                        'stats': '28-13-0',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_MILLENDER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:17',
                },
                'time': '22:00',
                'odds': {
                    CURTIS_MILLENDER: 2.25,
                    THIAGO_ALVES: 1.65,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JAMES_VICK,
                        'stats': '13-3-0',
                    },
                    {
                        'name': FRANCISCO_TRINALDO,
                        'stats': '23-6-0',
                    },
                ],
                'winner': {
                    'fighter': JAMES_VICK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    JAMES_VICK: 1.47,
                    FRANCISCO_TRINALDO: 2.70,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCIN_TYBURA,
                        'stats': '17-4-0',
                    },
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': DERRICK_LEWIS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:48',
                },
                'time': '23:00',
                'odds': {
                    DERRICK_LEWIS: 1.83,
                    MARCIN_TYBURA: 1.91,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                    {
                        'name': YANCY_MEDEIROS,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': DONALD_CERRONE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:58',
                },
                'time': '23:30',
                'odds': {
                    DONALD_CERRONE: 1.95,
                    YANCY_MEDEIROS: 1.78,
                },
            },
        ]
    },

    {
        'date': '2018-02-24',
        'name': 'UFC Fight Night: Emmett vs Stephens',
        'location': 'Orlando, Florida',
        'venue': 'Amway Center',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MANNY_BERMUDEZ,
                        'stats': '14-0-0',
                    },
                    {
                        'name': ALBERT_MORALES,
                        'stats': '7-4-1',
                    },
                ],
                'winner': {
                    'fighter': MANNY_BERMUDEZ,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:33',
                },
                'time': '16:20',
                'odds': {
                    MANNY_BERMUDEZ: 1.54,
                    ALBERT_MORALES: 2.46,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_PEREZ,
                        'stats': '22-5-0',
                    },
                    {
                        'name': ERIC_SHELTON,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_PEREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:45',
                'odds': {
                    ALEX_PEREZ: 1.99,
                    ERIC_SHELTON: 1.69,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RANI_YAHYA,
                        'stats': '26-10-0',
                    },
                    {
                        'name': RUSSEL_DOANE,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': RANI_YAHYA,
                    'by': 'submission',
                    'round': 3,
                    'time': '2:32',
                },
                'time': '17:10',
                'odds': {
                    RANI_YAHYA: 1.44,
                    RUSSEL_DOANE: 2.72,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCIN_PRACHNIO,
                        'stats': '13-4-0',
                    },
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': SAM_ALVEY,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:23',
                },
                'time': '17:30',
                'odds': {
                    SAM_ALVEY: 2.62,
                    MARCIN_PRACHNIO: 1.44,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALAN_JOUBAN,
                        'stats': '16-6-0',
                    },
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                ],
                'winner': {
                    'fighter': ALAN_JOUBAN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:38',
                },
                'time': '18:05',
                'odds': {
                    ALAN_JOUBAN: 1.38,
                    BEN_SAUNDERS: 3.00,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MARYNA_MOROZ,
                        'stats': '9-3-0',
                    },
                    {
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                ],
                'winner': {
                    'fighter': ANGELA_HILL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:35',
                'odds': {
                    ANGELA_HILL: 1.63,
                    MARYNA_MOROZ: 2.22,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARION_RENEAU,
                        'stats': '9-5-1',
                    },
                    {
                        'name': SARA_MCMANN,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': MARION_RENEAU,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:40',
                },
                'time': '19:05',
                'odds': {
                    MARION_RENEAU: 2.55,
                    SARA_MCMANN: 1.48,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRIAN_KELLEHER,
                        'stats': '19-10-0',
                    },
                    {
                        'name': RENAN_BARAO,
                        'stats': '36-8-0',
                    },
                ],
                'winner': {
                    'fighter': BRIAN_KELLEHER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    BRIAN_KELLEHER: 2.32,
                    RENAN_BARAO: 1.57,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_PERRY,
                        'stats': '12-4-0',
                    },
                    {
                        'name': MAX_GRIFFIN,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': MAX_GRIFFIN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:05',
                'odds': {
                    MAX_GRIFFIN: 3.60,
                    MIKE_PERRY: 1.29,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '23-12-0',
                    },
                    {
                        'name': ILIR_LATIFI,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': ILIR_LATIFI,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:48,'
                },
                'time': '20:35',
                'odds': {
                    ILIR_LATIFI: 2.37,
                    OVINCE_SAINT_PREUX: 1.59,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': TECIA_TORRES,
                        'stats': '10-4-0',
                    },
                    {
                        'name': JESSICA_ANDRADE,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ANDRADE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:05',
                'odds': {
                    JESSICA_ANDRADE: 1.42,
                    TECIA_TORRES: 2.88,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JOSH_EMMETT,
                        'stats': '14-2-0',
                    },
                    {
                        'name': JEREMY_STEPHENS,
                        'stats': '28-16-0',
                    },
                ],
                'winner': {
                    'fighter': JEREMY_STEPHENS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:35',
                },
                'time': '21:45',
                'odds': {
                    JEREMY_STEPHENS: 1.74,
                    JOSH_EMMETT: 2.01,
                },
            },
        ]
    },

    {
        'date': '2018-03-03',
        'name': 'UFC 222: Cyborg vs Kunitskaya',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {

                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_JOHNSON,
                        'stats': '10-0-0',
                    },
                    {
                        'name': ADAM_MILSTEAD,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_JOHNSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    JORDAN_JOHNSON: 1.38,
                    ADAM_MILSTEAD: 2.85,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CODY_STAMANN,
                        'stats': '18-2-0',
                    },
                    {
                        'name': BRYAN_CARAWAY,
                        'stats': '21-10-0',
                    },
                ],
                'winner': {
                    'fighter': CODY_STAMANN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    CODY_STAMANN: 1.82,
                    BRYAN_CARAWAY: 1.91,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ZAK_OTTOW,
                        'stats': '17-7-0',
                    },
                    {
                        'name': MIKE_PYLE,
                        'stats': '27-14-1',
                    },
                ],
                'winner': {
                    'fighter': ZAK_OTTOW,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:34',
                },
                'time': '19:30',
                'odds': {
                    ZAK_OTTOW: 1.29,
                    MIKE_PYLE: 3.65,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': HECTOR_LOMBARD,
                        'stats': '34-9-1',
                    },
                    {
                        'name': CB_DOLLAWAY,
                        'stats': '18-10-0',
                    },
                ],
                'winner': {
                    'fighter': CB_DOLLAWAY,
                    'by': 'dq',
                    'round': 1,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    CB_DOLLAWAY: 1.95,
                    HECTOR_LOMBARD: 1.80,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                    {
                        'name': JOHN_DODSON,
                        'stats': '21-11-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_DODSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    JOHN_DODSON: 1.59,
                    PEDRO_MUNHOZ: 2.40,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_HERNANDEZ,
                        'stats': '10-2-0',
                    },
                    {
                        'name': BENEIL_DARIUSH,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_HERNANDEZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:42',
                },
                'time': '21:00',
                'odds': {
                    ALEXANDER_HERNANDEZ: 4.25,
                    BENEIL_DARIUSH: 1.22,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MACKENZIE_DERN,
                        'stats': '7-0-0',
                    },
                    {
                        'name': ASHLEY_YODER,
                        'stats': '6-4-0',
                    },
                ],
                'winner': {
                    'fighter': MACKENZIE_DERN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    MACKENZIE_DERN: 1.18,
                    ASHLEY_YODER: 4.70,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': KETLEN_VIEIRA,
                        'stats': '10-0-0',
                    },
                    {
                        'name': CAT_ZINGANO,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': KETLEN_VIEIRA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    KETLEN_VIEIRA: 1.48,
                    CAT_ZINGANO: 2.69,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                    {
                        'name': STEFAN_STRUVE,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': ANDREI_ARLOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ANDREI_ARLOVSKI: 2.45,
                    STEFAN_STRUVE: 1.55,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': SEAN_O_MALLEY,
                        'stats': '10-0-0',
                    },
                    {
                        'name': ANDRE_SOUKHAMTHATH,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': SEAN_O_MALLEY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    SEAN_O_MALLEY: 1.64,
                    ANDRE_SOUKHAMTHATH: 2.20,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BRIAN_ORTEGA,
                        'stats': '4-1-0',
                    },
                    {
                        'name': FRANKIE_EDGAR,
                        'stats': '22-6-1',
                    },
                ],
                'winner': {
                    'fighter': BRIAN_ORTEGA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:44',
                },
                'time': '23:30',
                'odds': {
                    BRIAN_ORTEGA: 2.25,
                    FRANKIE_EDGAR: 1.63,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': YANA_KUNITSKAYA,
                        'stats': '12-4-0',
                    },
                    {
                        'name': CRIS_CYBORG,
                        'stats': '20-2-0',
                    },
                ],
                'winner': {
                    'fighter': CRIS_CYBORG,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:25',
                },
                'time': '23:59',
                'odds': {
                    CRIS_CYBORG: 1.09,
                    YANA_KUNITSKAYA: 6.50,
                },
            },
        ]
    },

    {
        'date': '2018-03-17',
        'name': 'UFC Fight Night: Werdum vs Volkov',
        'location': 'London, UK',
        'venue': 'The O2 Arena',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DMITRY_SOSNOVSKIY,
                        'stats': '10-0-0',
                    },
                    {
                        'name': MARK_GODBEER,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': DMITRY_SOSNOVSKIY,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:29',
                },
                'time': '14:15',
                'odds': {
                    DMITRY_SOSNOVSKIY: 1.36,
                    MARK_GODBEER: 3.20,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': STEVIE_RAY,
                        'stats': '22-7-0',
                    },
                    {
                        'name': KAJAN_JOHNSON,
                        'stats': '23-14-1',
                    },
                ],
                'winner': {
                    'fighter': KAJAN_JOHNSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:45',
                'odds': {
                    KAJAN_JOHNSON: 2.80,
                    STEVIE_RAY: 1.43,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MAGOMED_ANKALAEV,
                        'stats': '11-1-0',
                    },
                    {
                        'name': PAUL_CRAIG,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': PAUL_CRAIG,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:59',
                },
                'time': '15:30',
                'odds': {
                    PAUL_CRAIG: 6.00,
                    MAGOMED_ANKALAEV: 1.13,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HAKEEM_DAWODU,
                        'stats': '9-0-1',
                    },
                    {
                        'name': DANNY_HENRY,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': DANNY_HENRY,
                    'by': 'submission',
                    'round': 1,
                    'time': '0:39',
                },
                'time': '16:00',
                'odds': {
                    DANNY_HENRY: 3.05,
                    HAKEEM_DAWODU: 1.35,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': OLIVER_ENKAMP,
                        'stats': '7-2-0',
                    },
                    {
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': DANNY_ROBERTS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:12',
                },
                'time': '16:06',
                'odds': {
                    DANNY_ROBERTS: 1.71,
                    OLIVER_ENKAMP: 2.08,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_BYRD,
                        'stats': '10-6-0',
                    },
                    {
                        'name': JOHN_PHILLIPS,
                        'stats': '21-9-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_BYRD,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:58',
                },
                'time': '16:25',
                'odds': {
                    CHARLES_BYRD: 1.91,
                    JOHN_PHILLIPS: 1.81,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LEON_EDWARDS,
                        'stats': '17-3-0',
                    },
                    {
                        'name': PETER_SOBOTTA,
                        'stats': '17-6-1',
                    },
                ],
                'winner': {
                    'fighter': LEON_EDWARDS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:59',
                },
                'time': '16:55',
                'odds': {
                    LEON_EDWARDS: 1.50,
                    PETER_SOBOTTA: 2.60,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': TERRION_WARE,
                        'stats': '17-8-0',
                    },
                    {
                        'name': TOM_DUQUESNOY,
                        'stats': '16-2-0',
                    },
                ],
                'winner': {
                    'fighter': TOM_DUQUESNOY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:45',
                'odds': {
                    TOM_DUQUESNOY: 1.22,
                    TERRION_WARE: 4.15,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JAN_BLACHOWICZ,
                        'stats': '23-8-0',
                    },
                    {
                        'name': JIMI_MANUWA,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': JAN_BLACHOWICZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:15',
                'odds': {
                    JAN_BLACHOWICZ: 2.25,
                    JIMI_MANUWA: 1.61,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKOV,
                        'stats': '30-7-0',
                    },
                    {
                        'name': FABRICIO_WERDUM,
                        'stats': '23-8-1',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKOV,
                    'by': 'ko/tko',
                    'round': 4,
                    'time': '1:38',
                },
                'time': '18:45',
                'odds': {
                    ALEXANDER_VOLKOV: 2.70,
                    FABRICIO_WERDUM: 1.47,
                },
            },
        ]
    },

    {
        'date': '2018-04-07',
        'name': 'UFC 223: Khabib vs Iaquinta',
        'location': 'Brooklyn, New York',
        'venue': 'Barclays Center',
        'fights': [
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_RODRIGUEZ,
                        'stats': '10-3-0',
                    },
                    {
                        'name': DEVIN_CLARK,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': DEVIN_CLARK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    DEVIN_CLARK: 1.89,
                    MIKE_RODRIGUEZ: 1.77,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': BEC_RAWLINGS,
                        'stats': '7-8-0',
                    },
                    {
                        'name': ASHLEE_EVANS_SMITH,
                        'stats': '6-4-0',
                    },
                ],
                'winner': {
                    'fighter': ASHLEE_EVANS_SMITH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': OLIVIER_AUBIN_MERCIER,
                        'stats': '12-4-0',
                    },
                    {
                        'name': EVAN_DUNHAM,
                        'stats': '18-7-1',
                    },
                ],
                'winner': {
                    'fighter': OLIVIER_AUBIN_MERCIER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:53',
                },
                'time': '20:30',
                'odds': {
                    OLIVIER_AUBIN_MERCIER: 2.10,
                    EVAN_DUNHAM: 1.62,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': KAROLINA_KOWALKIEWICZ,
                        'stats': '13-4-0',
                    },
                    {
                        'name': FELICE_HERRIG,
                        'stats': '14-8-0',
                    },
                ],
                'winner': {
                    'fighter': KAROLINA_KOWALKIEWICZ,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    KAROLINA_KOWALKIEWICZ: 1.48,
                    FELICE_HERRIG: 2.57,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_GRUETZEMACHER,
                        'stats': '14-4-0',
                    },
                    {
                        'name': JOE_LAUZON,
                        'stats': '18-7-1',
                    },
                ],
                'winner': {
                    'fighter': CHRIS_GRUETZEMACHER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    CHRIS_GRUETZEMACHER: 2.19,
                    JOE_LAUZON: 1.61,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ZABIT_MAGOMEDSHARIPOV,
                        'stats': '17-1-0',
                    },
                    {
                        'name': KYLE_BOCHNIAK,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': ZABIT_MAGOMEDSHARIPOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ZABIT_MAGOMEDSHARIPOV: 1.14,
                    KYLE_BOCHNIAK: 5.25,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CALVIN_KATTAR,
                        'stats': '19-3-0',
                    },
                    {
                        'name': RENATO_MOICANO,
                        'stats': '13-2-1',
                    },
                ],
                'winner': {
                    'fighter': RENATO_MOICANO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    RENATO_MOICANO: 1.81,
                    CALVIN_KATTAR: 1.91,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ROSE_NAMAJUNAS,
                        'stats': '9-3-0',
                    },
                    {
                        'name': JOANNA_JEDRZEJCZYK,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': ROSE_NAMAJUNAS,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    ROSE_NAMAJUNAS: 1.88,
                    JOANNA_JEDRZEJCZYK: 1.77,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KHABIB_NURMAGOMEDIV,
                        'stats': '27-0-0',
                    },
                    {
                        'name': AL_IAQUINTA,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': KHABIB_NURMAGOMEDIV,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:55',
                'odds': {
                    KHABIB_NURMAGOMEDIV: 1.11,
                    AL_IAQUINTA: 5.00,
                },
            },
        ]
    },

    {
        'date': '2018-04-14',
        'name': 'UFC Fight Night: Poirier vs Gaethje',
        'location': 'Glendale, Arizona',
        'venue': 'Gila River Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PATRICK_WILLIAMS,
                        'stats': '8-6-0',
                    },
                    {
                        'name': LUKE_SANDERS,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': LUKE_SANDERS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:30',
                'odds': {
                    LUKE_SANDERS: 1.21,
                    PATRICK_WILLIAMS: 4.25,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MATTHEW_LOPEZ,
                        'stats': '10-5-0',
                    },
                    {
                        'name': ALEJANDRO_PEREZ,
                        'stats': '22-7-1',
                    },
                ],
                'winner': {
                    'fighter': ALEJANDRO_PEREZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:42',
                },
                'time': '16:05',
                'odds': {
                    ALEJANDRO_PEREZ: 1.87,
                    MATTHEW_LOPEZ: 1.80,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ARJAN_BHULLAR,
                        'stats': '8-1-0',
                    },
                    {
                        'name': ADAM_WIECZOREK,
                        'stats': '10-2-0',
                    },
                ],
                'winner': {
                    'fighter': ADAM_WIECZOREK,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:59',
                },
                'time': '16:25',
                'odds': {
                    ADAM_WIECZOREK: 3.69,
                    ARJAN_BHULLAR: 1.28,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DHIEGO_LIMA,
                        'stats': '15-7-0',
                    },
                    {
                        'name': YUSHIN_OKAMI,
                        'stats': '34-13-0',
                    },
                ],
                'winner': {
                    'fighter': YUSHIN_OKAMI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:45',
                'odds': {
                    YUSHIN_OKAMI: 1.79,
                    DHIEGO_LIMA: 1.95,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SHANA_DOBSON,
                        'stats': '3-2-0',
                    },
                    {
                        'name': LAUREN_MUELLER,
                        'stats': '5-1-0',
                    },
                ],
                'winner': {
                    'fighter': LAUREN_MUELLER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:01',
                'odds': {
                    LAUREN_MUELLER: 1.61,
                    SHANA_DOBSON: 2.30,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_MORET,
                        'stats': '13-5-0',
                    },
                    {
                        'name': GILBERT_BURNS,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': GILBERT_BURNS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:59',
                },
                'time': '17:30',
                'odds': {
                    GILBERT_BURNS: 1.16,
                    DAN_MORET: 5.00,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': BRAD_TAVARES,
                        'stats': '17-5-0',
                    },
                    {
                        'name': KRZYSZTOF_JOTKO,
                        'stats': '19-4-0',
                    },
                ],
                'winner': {
                    'fighter': BRAD_TAVARES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:16',
                },
                'time': '19:01',
                'odds': {
                    BRAD_TAVARES: 1.83,
                    KRZYSZTOF_JOTKO: 1.76,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': WILSON_REIS,
                        'stats': '23-9-0',
                    },
                    {
                        'name': JOHN_MORAGA,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_MORAGA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:31',
                'odds': {
                    JOHN_MORAGA: 2.00,
                    WILSON_REIS: 1.77,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': RICKEY_RAINEY,
                        'stats': '13-6-0',
                    },
                    {
                        'name': MUSLIM_SALIKHOV,
                        'stats': '14-2-0',
                    },
                ],
                'winner': {
                    'fighter': MUSLIM_SALIKHOV,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:12',
                },
                'time': '19:00',
                'odds': {
                    MUSLIM_SALIKHOV: 1.49,
                    RICKEY_RAINEY: 2.60,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANTONIO_CARLOS_JUNIOR,
                        'stats': '11-2-0',
                    },
                    {
                        'name': TIM_BOETSCH,
                        'stats': '21-13-0',
                    },
                ],
                'winner': {
                    'fighter': ANTONIO_CARLOS_JUNIOR,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:28',
                },
                'time': '19:40',
                'odds': {
                    TIM_BOETSCH: 2.90,
                    ANTONIO_CARLOS_JUNIOR: 1.40,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CORTNEY_CASEY_SANCHEZ,
                        'stats': '8-6-0',
                    },
                    {
                        'name': MICHELLE_WATERSON,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': MICHELLE_WATERSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:15',
                'odds': {
                    MICHELLE_WATERSON: 2.25,
                    CORTNEY_CASEY_SANCHEZ: 1.59,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ISRAEL_ADESANYA,
                        'stats': '16-0-0',
                    },
                    {
                        'name': MARVIN_VETTORI,
                        'stats': '12-4-1',
                    },
                ],
                'winner': {
                    'fighter': ISRAEL_ADESANYA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    ISRAEL_ADESANYA: 1.40,
                    MARVIN_VETTORI: 2.95,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_OLIVEIRA,
                        'stats': '19-6-1',
                    },
                    {
                        'name': CARLOS_CONDIT,
                        'stats': '30-13-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_OLIVEIRA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:17',
                },
                'time': '21:15',
                'odds': {
                    ALEX_OLIVEIRA: 1.49,
                    CARLOS_CONDIT: 2.55,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_GAETHJE,
                        'stats': '20-2-0',
                    },
                    {
                        'name': DUSTIN_POIRIER,
                        'stats': '24-5-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_POIRIER,
                    'by': 'ko/tko',
                    'round': 4,
                    'time': '0:33',
                },
                'time': '21:40',
                'odds': {
                    DUSTIN_POIRIER: 1.80,
                    JUSTIN_GAETHJE: 1.91,
                },
            },
        ]
    },

    {
        'date': '2018-04-21',
        'name': 'UFC Fight Night: Barboza vs Lee',
        'location': 'Atlantic City, New Jersey',
        'venue': 'Boardwalk Hall',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KEITA_NAKAMURA,
                        'stats': '34-9-2',
                    },
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_ROCCO_MARTIN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ANTHONY_ROCCO_MARTIN: 1.44,
                    KEITA_NAKAMURA: 2.75,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': COREY_ANDERSON,
                        'stats': '13-4-0',
                    },
                    {
                        'name': PATRICK_CUMMINS,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': COREY_ANDERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    COREY_ANDERSON: 1.57,
                    PATRICK_CUMMINS: 2.30,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LUAN_CHAGAS,
                        'stats': '15-3-1',
                    },
                    {
                        'name': SIYAR_BAHADURZADA,
                        'stats': '24-7-1',
                    },
                ],
                'winner': {
                    'fighter': SIYAR_BAHADURZADA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:40',
                },
                'time': '20:30',
                'odds': {
                    SIYAR_BAHADURZADA: 2.50,
                    LUAN_CHAGAS: 1.54,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MERAB_DVALISHVILI,
                        'stats': '8-4-0',
                    },
                    {
                        'name': RICKY_SIMON,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': RICKY_SIMON,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    RICKY_SIMON: 1.87,
                    MERAB_DVALISHVILI: 1.87,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_LAFLARE,
                        'stats': '13-3-0',
                    },
                    {
                        'name': ALEX_GARCIA,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_LAFLARE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    RYAN_LAFLARE: 1.63,
                    ALEX_GARCIA: 2.30,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_HOOKER,
                        'stats': '18-8-0',
                    },
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_HOOKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:00',
                },
                'time': '22:00',
                'odds': {
                    DAN_HOOKER: 1.33,
                    JIM_MILLER: 3.30,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRETT_JOHNS,
                        'stats': '15-2-0',
                    },
                    {
                        'name': ALJAMAIN_STERLING,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALJAMAIN_STERLING,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ALJAMAIN_STERLING: 1.87,
                    BRETT_JOHNS: 1.87,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_BRANCH,
                        'stats': '22-6-0',
                    },
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': DAVID_BRANCH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:30',
                },
                'time': '23:00',
                'odds': {
                    DAVID_BRANCH: 2.35,
                    THIAGO_SANTOS: 1.59,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_WILLIS,
                        'stats': '8-2-0',
                    },
                    {
                        'name': CHASE_SHERMAN,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_WILLIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    JUSTIN_WILLIS: 1.33,
                    CHASE_SHERMAN: 3.30,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CUB_SWANSON,
                        'stats': '25-10-0',
                    },
                    {
                        'name': FRANKIE_EDGAR,
                        'stats': '22-6-1',
                    },
                ],
                'winner': {
                    'fighter': FRANKIE_EDGAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:58',
                'odds': {
                    FRANKIE_EDGAR: 1.32,
                    CUB_SWANSON: 3.25,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                    {
                        'name': EDSON_BARBOZA,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_LEE,
                    'by': 'tko',
                    'round': 5,
                    'time': '2:18',
                },
                'time': '23:59',
                'odds': {
                    KEVIN_LEE: 1.54,
                    EDSON_BARBOZA: 2.41,
                },
            },
        ]
    },

    {
        'date': '2018-05-12',
        'name': 'UFC 224',
        'location': 'Rio de Janeiro, Brazil',
        'venue': 'Jeunesse Arena',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': MARKUS_PEREZ,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JAMES_BOCHNOVIC,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': MARKUS_PEREZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:28',
                },
                'time': '18:00',
                'odds': {
                    MARKUS_PEREZ: 1.31,
                    JAMES_BOCHNOVIC: 3.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': RAMAZAN_EMEEV,
                        'stats': '18-3-0',
                    },
                    {
                        'name': ALBERTO_MINA,
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': RAMAZAN_EMEEV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    RAMAZAN_EMEEV: 1.55,
                    ALBERTO_MINA: 2.40,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACK_HERMANSSON,
                        'stats': '19-4-0',
                    },
                    {
                        'name': THALES_LEITES,
                        'stats': '28-9-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_HERMANSSON,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:10',
                },
                'time': '19:00',
                'odds': {
                    JACK_HERMANSSON: 1.71,
                    THALES_LEITES: 2.10,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SULTAN_ALIEV,
                        'stats': '14-3-0',
                    },
                    {
                        'name': WARLLEY_ALVES,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': WARLLEY_ALVES,
                    'by': 'tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    WARLLEY_ALVES: 1.32,
                    SULTAN_ALIEV: 3.30,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ELIZEU_DOS_SANTOS,
                        'stats': '20-5-0',
                    },
                    {
                        'name': SEAN_STRICKLAND,
                        'stats': '20-3-0',
                    },
                ],
                'winner': {
                    'fighter': ELIZEU_DOS_SANTOS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:12',
                },
                'time': '20:00',
                'odds': {
                    ELIZEU_DOS_SANTOS: 1.95,
                    SEAN_STRICKLAND: 1.80,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAVI_RAMOS,
                        'stats': '9-2-0',
                    },
                    {
                        'name': NICK_HEIN,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': DAVI_RAMOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:15',
                },
                'time': '20:30',
                'odds': {
                    DAVI_RAMOS: 1.50,
                    NICK_HEIN: 2.52,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUNIOR_ALBINI,
                        'stats': '14-5-0',
                    },
                    {
                        'name': ALEKSEI_OLEINIK,
                        'stats': '57-11-1',
                    },
                ],
                'winner': {
                    'fighter': ALEKSEI_OLEINIK,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:45',
                },
                'time': '21:00',
                'odds': {
                    ALEKSEI_OLEINIK: 2.23,
                    JUNIOR_ALBINI: 1.62,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KARL_ROBERSON,
                        'stats': '7-2-0',
                    },
                    {
                        'name': CEZAR_FERREIRA,
                        'stats': '14-7-0',
                    },
                ],
                'winner': {
                    'fighter': CEZAR_FERREIRA,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:45',
                },
                'time': '21:30',
                'odds': {
                    CEZAR_FERREIRA: 1.63,
                    KARL_ROBERSON: 2.25,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': LYOTO_MACHIDA,
                        'stats': '24-8-0',
                    },
                    {
                        'name': VITOR_BELFORT,
                        'stats': '26-14-0',
                    },
                ],
                'winner': {
                    'fighter': LYOTO_MACHIDA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:00',
                },
                'time': '22:00',
                'odds': {
                    LYOTO_MACHIDA: 1.48,
                    VITOR_BELFORT: 2.60,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRIAN_KELLEHER,
                        'stats': '19-10-0',
                    },
                    {
                        'name': JOHN_LINEKER,
                        'stats': '31-8-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_LINEKER,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:43',
                },
                'time': '22:30',
                'odds': {
                    JOHN_LINEKER: 1.36,
                    BRIAN_KELLEHER: 3.20,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MACKENZIE_DERN,
                        'stats': '7-0-0',
                    },
                    {
                        'name': AMANDA_COOPER,
                        'stats': '4-5-0',
                    }
                ],
                'winner': {
                    'fighter': MACKENZIE_DERN,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:27',
                },
                'time': '23:00',
                'odds': {
                    MACKENZIE_DERN: 1.38,
                    AMANDA_COOPER: 3.00,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JACARE_SOUZA,
                        'stats': '26-6-0',
                    },
                    {
                        'name': KELVIN_GASTELUM,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': KELVIN_GASTELUM,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    KELVIN_GASTELUM: 1.95,
                    JACARE_SOUZA: 1.80,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RAQUEL_PENNINGTON,
                        'stats': '9-8-0',
                    },
                    {
                        'name': AMANDA_NUNES,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': AMANDA_NUNES,
                    'by': 'ko/tko',
                    'round': 5,
                    'time': '2:36',
                },
                'time': '23:59',
                'odds': {
                    AMANDA_NUNES: 1.11,
                    RAQUEL_PENNINGTON: 5.50,
                },
            },
        ]
    },

    {
        'date': '2018-05-19',
        'name': 'UFC Fight Night: Maia vs Usman',
        'location': 'Santiago, Chile',
        'venue': 'Movistar Arena',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CLAUDIO_PUELLES,
                        'stats': '9-2-0',
                    },
                    {
                        'name': FELIPE_SILVA,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': CLAUDIO_PUELLES,
                    'by': 'submission',
                    'round': 3,
                    'time': '2:23',
                },
                'time': '18:30',
                'odds': {
                    CLAUDIO_PUELLES: 3.45,
                    FELIPE_SILVA: 1.32,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': HENRY_BRIONES,
                        'stats': '19-8-1',
                    },
                    {
                        'name': FRANKIE_SAENZ,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': FRANKIE_SAENZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    FRANKIE_SAENZ: 1.29,
                    HENRY_BRIONES: 3.65,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BRANDON_DAVIS,
                        'stats': '9-5-0',
                    },
                    {
                        'name': ENRIQUE_BARZOLA,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': ENRIQUE_BARZOLA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'round': {
                    ENRIQUE_BARZOLA: 1.40,
                    BRANDON_DAVIS: 2.90,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HUMBERTO_BANDENAY,
                        'stats': '14-6-0',
                    },
                    {
                        'name': GABRIEL_BENITEZ,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': GABRIEL_BENITEZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:39',
                },
                'time': '20:00',
                'odds': {
                    GABRIEL_BENITEZ: 1.61,
                    HUMBERTO_BANDENAY: 2.35,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': SYURI_KONDO,
                        'stats': '6-2-0',
                    },
                    {
                        'name': POLIANA_BOTELHO,
                        'stats': '7-2-0',
                    },
                ],
                'winner': {
                    'fighter': POLIANA_BOTELHO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:33',
                },
                'time': '20:30',
                'odds': {
                    POLIANA_BOTELHO: 1.53,
                    SYURI_KONDO: 2.50,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDRE_PANTOJA,
                        'stats': '20-3-0',
                    },
                    {
                        'name': BRANDON_MORENO,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDRE_PANTOJA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    ALEXANDRE_PANTOJA: 1.87,
                    BRANDON_MORENO: 1.87,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICHEL_PRAZERES,
                        'stats': '26-3-0',
                    },
                    {
                        'name': ZAK_CUMMINGS,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': MICHEL_PRAZERES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    MICHEL_PRAZERES: 2.55,
                    ZAK_CUMMINGS: 1.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': VICENTE_LUQUE,
                        'stats': '15-6-1',
                    },
                    {
                        'name': CHAD_LAPRISE,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': VICENTE_LUQUE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:16',
                },
                'time': '22:00',
                'odds': {
                    VICENTE_LUQUE: 1.43,
                    CHAD_LAPRISE: 2.85,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANDREA_LEE,
                        'stats': '10-2-0',
                    },
                    {
                        'name': VERONICA_MACEDO,
                        'stats': '5-3-1',
                    },
                ],
                'winner': {
                    'fighter': ANDREA_LEE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    ANDREA_LEE: 1.27,
                    VERONICA_MACEDO: 3.59,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GUIDO_CANNETTI,
                        'stats': '8-5-0',
                    },
                    {
                        'name': DIEGO_RIVAS,
                        'stats': '7-2-0',
                    },
                ],
                'winner': {
                    'fighter': GUIDO_CANNETTI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    GUIDO_CANNETTI: 2.50,
                    DIEGO_RIVAS: 1.54,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DOMINICK_REYES,
                        'stats': '11-0-0',
                    },
                    {
                        'name': JARED_CANNONIER,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': DOMINICK_REYES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:55',
                },
                'time': '23:30',
                'odds': {
                    DOMINICK_REYES: 1.44,
                    JARED_CANNONIER: 2.70,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ALEXA_GRASSO,
                        'stats': '10-2-0',
                    },
                    {
                        'name': TATIANA_SUAREZ,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': TATIANA_SUAREZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:44',
                },
                'time': '23:59',
                'odds': {
                    TATIANA_SUAREZ: 1.17,
                    ALEXA_GRASSO: 4.75,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KAMARU_USMAN,
                        'stats': '15-1-0',
                    },
                    {
                        'name': DEMIAN_MAIA,
                        'stats': '26-9-0',
                    },
                ],
                'winner': {
                    'fighter': KAMARU_USMAN,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    KAMARU_USMAN: 1.19,
                    DEMIAN_MAIA: 4.50,
                },
            },
        ]
    },

    {
        'date': '2018-05-27',
        'name': 'UFC Fight Night',
        'location': 'Liverpool, United Kingdom',
        'venue': 'Echo Arena',
        'fights': [
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ELIAS_THEODOROU,
                        'stats': '17-2-0',
                    },
                    {
                        'name': TREVOR_SMITH,
                        'stats': '15-9-0',
                    },
                ],
                'winner': {
                    'fighter': ELIAS_THEODOROU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '11:00',
                'odds': {
                    ELIAS_THEODOROU: 1.25,
                    TREVOR_SMITH: 4.00,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MOLLY_MCCANN,
                        'stats': '8-2-0',
                    },
                    {
                        'name': GILLIAN_ROBERTSON,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': GILLIAN_ROBERTSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:05',
                },
                'time': '13:00',
                'odds': {
                    GILLIAN_ROBERTSON: 2.25,
                    MOLLY_MCCANN: 1.64,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CARLO_PEDERSOLI_JR,
                        'stats': '11-2-0',
                    },
                    {
                        'name': BRADLEY_SCOTT,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': CARLO_PEDERSOLI_JR,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '13:30',
                'odds': {
                    CARLO_PEDERSOLI_JR: 1.63,
                    BRADLEY_SCOTT: 2.21,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GINA_MAZANY,
                        'stats': '5-3-0',
                    },
                    {
                        'name': LINA_LANSBERG,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': LINA_LANSBERG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:00',
                'odds': {
                    LINA_LANSBERG: 2.15,
                    GINA_MAZANY: 1.61,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TOM_BREESE,
                        'stats': '11-1-0',
                    },
                    {
                        'name': DANIEL_KELLY,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': TOM_BREESE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:33',
                },
                'time': '14:30',
                'odds': {
                    TOM_BREESE: 1.25,
                    DANIEL_KELLY: 3.70,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                    {
                        'name': ERIC_SPICELY,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_STEWART,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:47',
                },
                'time': '15:00',
                'odds': {
                    DARREN_STEWART: 2.35,
                    ERIC_SPICELY: 1.61,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NORDINE_TALEB,
                        'stats': '14-6-0',
                    },
                    {
                        'name': CLAUDIO_DA_SILVA,
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': CLAUDIO_DA_SILVA,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:31',
                },
                'time': '15:30',
                'odds': {
                    CLAUDIO_DA_SILVA: 3.70,
                    NORDINE_TALEB: 1.26,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JASON_KNIGHT,
                        'stats': '20-6-0',
                    },
                    {
                        'name': MAKWAN_AMIRKHANI,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAKWAN_AMIRKHANI,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:00',
                'odds': {
                    MAKWAN_AMIRKHANI: 2.40,
                    JASON_KNIGHT: 1.56,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MADS_BURNELL,
                        'stats': '9-3-0',
                    },
                    {
                        'name': ARNOLD_ALLEN,
                        'stats': '14-1-0',
                    },
                ],
                'winner': {
                    'fighter': ARNOLD_ALLEN,
                    'by': 'submission',
                    'round': 3,
                    'time': '2:41',
                },
                'time': '16:30',
                'odds': {
                    ARNOLD_ALLEN: 1.39,
                    MADS_BURNELL: 2.85,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CRAIG_WHITE,
                        'stats': '14-9-0',
                    },
                    {
                        'name': NEIL_MAGNY,
                        'stats': '21-8-0',
                    },
                ],
                'winner': {
                    'fighter': NEIL_MAGNY,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:32',
                },
                'time': '17:00',
                'odds': {
                    NEIL_MAGNY: 1.13,
                    CRAIG_WHITE: 5.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_TILL,
                        'stats': '17-2-1',
                    },
                    {
                        'name': STEPHEN_THOMPSON,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': DARREN_TILL,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '17:30',
                'odds': {
                    DARREN_TILL: 2.20,
                    STEPHEN_THOMPSON: 1.67,
                },
            },
        ]
    },

    {
        'date': '2018-06-01',
        'name': 'UFC Fight Night',
        'location': 'Utica, New York',
        'venue': 'Adirondack Bank Center',
        'fights': [
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOSE_TORRES,
                        'stats': '8-1-0',
                    },
                    {
                        'name': JARRED_BROOKS,
                        'stats': '14-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOSE_TORRES,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:55',
                },
                'time': '18:30',
                'odds': {
                    JOSE_TORRES: 1.67,
                    JARRED_BROOKS: 2.15,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': NATHANIEL_WOOD,
                        'stats': '16-3-0',
                    },
                    {
                        'name': JOHNNY_EDUARDO,
                        'stats': '28-12-0',
                    },
                ],
                'winner': {
                    'fighter': NATHANIEL_WOOD,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:18',
                },
                'time': '19:00',
                'odds': {
                    NATHANIEL_WOOD: 1.38,
                    JOHNNY_EDUARDO: 2.95,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_TEYMUR,
                        'stats': '8-2-0',
                    },
                    {
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                ],
                'winner': {
                    'fighter': DAVID_TEYMUR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:05',
                'odds': {
                    DAVID_TEYMUR: 1.33,
                    NIK_LENTZ: 3.30,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SIJARA_EUBANKS,
                        'stats': '5-2-0',
                    },
                    {
                        'name': LAUREN_MURPHY,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': SIJARA_EUBANKS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    SIJARA_EUBANKS: 1.43,
                    LAUREN_MURPHY: 2.67,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
                    },
                    {
                        'name': GIAN_VILLANTE,
                        'stats': '17-11-0',
                    },
                ],
                'winner': {
                    'fighter': SAM_ALVEY,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    SAM_ALVEY: 1.63,
                    GIAN_VILLANTE: 2.20,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JULIO_ACRE,
                        'stats': '15-3-0',
                    },
                    {
                        'name': DANIEL_TEYMUR,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': JULIO_ACRE,
                    'by': 'submission',
                    'round': 3,
                    'time': '2:55',
                },
                'time': '22:30',
                'odds': {
                    JULIO_ACRE: 1.50,
                    DANIEL_TEYMUR: 2.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                    {
                        'name': JAKE_ELLENBERGER,
                        'stats': '31-15-0',
                    },
                ],
                'winner': {
                    'fighter': BEN_SAUNDERS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:56',
                },
                'time': '23:00',
                'odds': {
                    BEN_SAUNDERS: 2.40,
                    JAKE_ELLENBERGER: 1.59,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DANIEL_SPITZ,
                        'stats': '6-2-0',
                    },
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': WALT_HARRIS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:59',
                },
                'time': '23:30',
                'odds': {
                    WALT_HARRIS: 1.45,
                    DANIEL_SPITZ: 2.70,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GREGOR_GILLESPIE,
                        'stats': '13-0-0',
                    },
                    {
                        'name': VINC_PICHEL,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': GREGOR_GILLESPIE,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:06',
                },
                'time': '23:59',
                'odds': {
                    GREGOR_GILLESPIE: 1.25,
                    VINC_PICHEL: 4.00,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARLON_MORAES,
                        'stats': '22-5-1',
                    },
                    {
                        'name': JIMMIE_RIVERA,
                        'stats': '22-3-0',
                    },
                ],
                'winner': {
                    'fighter': MARLON_MORAES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:33',
                },
                'time': '23:59',
                'odds': {
                    MARLON_MORAES: 1.98,
                    JIMMIE_RIVERA: 1.77,
                },
            },
        ]
    },

    {
        'date': '2018-06-09',
        'name': 'UFC 225',
        'location': 'Chicago, Illinois',
        'venue': 'United Center',
        'fights': [
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_SANTIAGO,
                        'stats': '21-12-0',
                    },
                    {
                        'name': DAN_IGE,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_IGE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:50',
                },
                'time': '18:15',
                'odds': {
                    MIKE_SANTIAGO: 1.91,
                    DAN_IGE: 1.80,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                    {
                        'name': CLAY_GUIDA,
                        'stats': '34-15-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:18',
                },
                'time': '18:45',
                'odds': {
                    CHARLES_OLIVEIRA: 1.67,
                    CLAY_GUIDA: 2.20,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SERGIO_PETTIS,
                        'stats': '17-5-0',
                    },
                    {
                        'name': JOSEPH_BENAVIDEZ,
                        'stats': '27-5-0',
                    },
                ],
                'winner': {
                    'fighter': SERGIO_PETTIS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:15',
                'odds': {
                    SERGIO_PETTIS: 2.56,
                    JOSEPH_BENAVIDEZ: 1.44,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': RASHAD_EVANS,
                        'stats': '24-8-1',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_SMITH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:53',
                },
                'time': '19:45',
                'odds': {
                    ANTHONY_SMITH: 1.44,
                    RASHAD_EVANS: 2.65,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': RASHAD_COULTER,
                        'stats': '9-4-0',
                    },
                    {
                        'name': CHRIS_DE_LA_ROCHA,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': CHRIS_DE_LA_ROCHA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:53',
                },
                'time': '20:00',
                'odds': {
                    CHRIS_DE_LA_ROCHA: 1.95,
                    RASHAD_COULTER: 1.80,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MIRSAD_BEKTIC,
                        'stats': '13-1-0',
                    },
                    {
                        'name': RICARDO_LAMAS,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': MIRSAD_BEKTIC,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    MIRSAD_BEKTIC: 1.38,
                    RICARDO_LAMAS: 2.95,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CARLA_ESPARZA,
                        'stats': '14-6-0',
                    },
                    {
                        'name': CLAUDIA_GADELHA,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': CLAUDIA_GADELHA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    CLAUDIA_GADELHA: 1.37,
                    CARLA_ESPARZA: 3.10,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_BLAYDES,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ALISTAIR_OVEREEM,
                        'stats': '44-17-0',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_BLAYDES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:56',
                },
                'time': '21:30',
                'odds': {
                    CURTIS_BLAYDES: 1.44,
                    ALISTAIR_OVEREEM: 2.65,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CM_PUNK,
                        'stats': '0-2-0',
                    },
                    {
                        'name': MIKE_JACKSON,
                        'stats': '1-1-0',
                    },
                ],
                'winner': {
                    'fighter': MIKE_JACKSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    MIKE_JACKSON: 1.50,
                    CM_PUNK: 2.60,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TAI_TUIVASA,
                        'stats': '10-1-0',
                    },
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                ],
                'winner': {
                    'fighter': TAI_TUIVASA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    TAI_TUIVASA: 1.42,
                    ANDREI_ARLOVSKI: 2.80,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MEGAN_ANDERSON,
                        'stats': '9-3-0',
                    },
                    {
                        'name': HOLLY_HOLM,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': HOLLY_HOLM,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    HOLLY_HOLM: 1.59,
                    MEGAN_ANDERSON: 2.30,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': COLBY_COVINGTON,
                        'stats': '14-1-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': COLBY_COVINGTON,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    COLBY_COVINGTON: 1.67,
                    RAFAEL_DOS_ANJOS: 2.20,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ROBERT_WHITTAKER,
                        'stats': '21-4-0',
                    },
                    {
                        'name': YOEL_ROMERO,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': ROBERT_WHITTAKER,
                    'by': 's.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    ROBERT_WHITTAKER: 1.33,
                    YOEL_ROMERO: 3.35,
                },
            },
        ]
    },

    {
        'date': '2018-06-23',
        'name': 'UFC Fight Night',
        'location': 'Kallang, Singapore',
        'venue': 'Singapore Indoor Stadium',
        'fights': [
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MELINDA_FABIAN,
                        'stats': '4-4-2',
                    },
                    {
                        'name': JI_YEON_KIM,
                        'stats': '7-2-2',
                    },
                ],
                'winner': {
                    'fighter': JI_YEON_KIM,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JENEL_LAUSA,
                        'stats': '7-5-0',
                    },
                    {
                        'name': ULKA_SASAKI,
                        'stats': '21-6-2',
                    },
                ],
                'winner': {
                    'fighter': ULKA_SASAKI,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:04',
                },
                'time': '16:00',
                'odds': {
                    ULKA_SASAKI: 1.38,
                    JENEL_LAUSA: 2.95,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': NAOKI_INOUE,
                        'stats': '11-1-0',
                    },
                    {
                        'name': MATT_SCHNELL,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': MATT_SCHNELL,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:30',
                'odds': {
                    MATT_SCHNELL: 2.60,
                    NAOKI_INOUE: 1.50,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': YAN_XIAONAN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': VIVIANE_PEREIRA,
                        'stats': '13-2-0',
                    },
                ],
                'winner': {
                    'fighter': YAN_XIAONAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SHINSHO_ANZAI,
                        'stats': '10-3-0',
                    },
                    {
                        'name': JAKE_MATTHEWS,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': JAKE_MATTHEWS,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:44',
                },
                'time': '17:30',
                'odds': {
                    JAKE_MATTHEWS: 1.17,
                    SHINSHO_ANZAI: 5.00,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': HECTOR_ALDANA,
                        'stats': '4-3-0',
                    },
                    {
                        'name': SONG_KENAN,
                        'stats': '13-5-0',
                    },
                ],
                'winner': {
                    'fighter': SONG_KENAN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:45',
                },
                'time': '18:00',
                'odds': {
                    SONG_KENAN: 1.33,
                    HECTOR_ALDANA: 3.35,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHANE_YOUNG,
                        'stats': '12-4-0',
                    },
                    {
                        'name': ROLANDO_DY,
                        'stats': '9-7-1',
                    },
                ],
                'winner': {
                    'fighter': SHANE_YOUNG,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:40',
                },
                'time': '18:30',
                'odds': {
                    SHANE_YOUNG: 1.57,
                    ROLANDO_DY: 2.40,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': SONG_YADONG,
                        'stats': '13-3-0',
                    },
                    {
                        'name': FELIPE_ARANTES,
                        'stats': '18-10-1',
                    },
                ],
                'winner': {
                    'fighter': SONG_YADONG,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:59',
                },
                'time': '19:00',
                'odds': {
                    SONG_YADONG: 1.77,
                    FELIPE_ARANTES: 2.00,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PETR_YAN,
                        'stats': '12-1-0',
                    },
                    {
                        'name': TERUTO_ISHIHARA,
                        'stats': '11-6-2',
                    },
                ],
                'winner': {
                    'fighter': PETR_YAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:28',
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAICHI_ABE,
                        'stats': '6-2-0',
                    },
                    {
                        'name': LI_JINGLIANG,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': LI_JINGLIANG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    LI_JINGLIANG: 1.40,
                    DAICHI_ABE: 2.80,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JESSICA_ROSE_CLARK,
                        'stats': '9-5-0',
                    },
                    {
                        'name': JESSICA_EYE,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_EYE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    JESSICA_EYE: 2.37,
                    JESSICA_ROSE_CLARK: 1.56,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TYSON_PEDRO,
                        'stats': '7-2-0',
                    },
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '23-12-0',
                    },
                ],
                'winner': {
                    'fighter': OVINCE_SAINT_PREUX,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:54',
                },
                'time': '21:00',
                'odds': {
                    OVINCE_SAINT_PREUX: 2.18,
                    TYSON_PEDRO: 1.65,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LEON_EDWARDS,
                        'stats': '17-3-0',
                    },
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                ],
                'winner': {
                    'fighter': LEON_EDWARDS,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    LEON_EDWARDS: 1.38,
                    DONALD_CERRONE: 2.95,
                },
            },
        ]
    },

    {
        'date': '2018-07-07',
        'name': 'UFC 226',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': EMILY_WHITMIRE,
                        'stats': '4-2-0',
                    },
                    {
                        'name': JAMIE_MOYLE,
                        'stats': '4-3-0',
                    },
                ],
                'winner': {
                    'fighter': EMILY_WHITMIRE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:30',
                'odds': {
                    EMILY_WHITMIRE: 2.64,
                    JAMIE_MOYLE: 1.49,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GILBERT_BURNS,
                        'stats': '14-3-0',
                    },
                    {
                        'name': DAN_HOOKER,
                        'stats': '18-8-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_HOOKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:28',
                },
                'time': '19:30',
                'odds': {
                    DAN_HOOKER: 1.80,
                    GILBERT_BURNS: 1.93,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_MILLENDER,
                        'stats': '17-4-0',
                    },
                    {
                        'name': MAX_GRIFFIN,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_MILLENDER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    CURTIS_MILLENDER: 1.54,
                    MAX_GRIFFIN: 2.40,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DRAKKAR_KLOSE,
                        'stats': '14-3-0',
                    },
                    {
                        'name': LANDO_VANNATA,
                        'stats': '10-3-2',
                    },
                ],
                'winner': {
                    'fighter': DRAKKAR_KLOSE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:40',
                'odds': {
                    DRAKKAR_KLOSE: 2.60,
                    LANDO_VANNATA: 1.50,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ROB_FONT,
                        'stats': '16-4-0',
                    },
                    {
                        'name': RAPHAEL_ASSUNCAO,
                        'stats': '27-6-0',
                    },
                ],
                'winner': {
                    'fighter': RAPHAEL_ASSUNCAO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:10',
                'odds': {
                    RAPHAEL_ASSUNCAO: 1.67,
                    ROB_FONT: 2.16,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': PAULO_COSTA,
                        'stats': '12-0-0',
                    },
                    {
                        'name': URIAH_HALL,
                        'stats': '15-9-0',
                    },
                ],
                'winner': {
                    'fighter': PAULO_COSTA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:38',
                },
                'time': '21:30',
                'odds': {
                    PAULO_COSTA: 1.30,
                    URIAH_HALL: 3.35,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GOKHAN_SAKI,
                        'stats': '1-2-0',
                    },
                    {
                        'name': KHALIL_ROUNTREE,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': KHALIL_ROUNTREE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:36',
                },
                'time': '22:00',
                'odds': {
                    KHALIL_ROUNTREE: 2.41,
                    GOKHAN_SAKI: 1.54,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_PETTIS,
                        'stats': '22-8-0',
                    },
                    {
                        'name': MICHAEL_CHIESA,
                        'stats': '15-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_PETTIS,
                    'by': 'submission',
                    'round': 2,
                    'time': '0:52',
                },
                'time': '22:30',
                'odds': {
                    ANTHONY_PETTIS: 2.44,
                    MICHAEL_CHIESA: 1.57,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_PERRY,
                        'stats': '12-4-0',
                    },
                    {
                        'name': PAUL_FELDER,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': MIKE_PERRY,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    MIKE_PERRY: 2.41,
                    PAUL_FELDER: 1.57,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': FRANCIS_NGANNOU,
                        'stats': '13-3-0',
                    },
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': DERRICK_LEWIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:40',
                'odds': {
                    DERRICK_LEWIS: 3.55,
                    FRANCIS_NGANNOU: 1.29,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': STIPE_MIOCIC,
                        'stats': '18-3-0',
                    },
                    {
                        'name': DANIEL_CORMIER,
                        'stats': '22-1-0',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_CORMIER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:33',
                },
            },
        ]
    },

    {
        'date': '2018-07-14',
        'name': 'UFC Fight Night',
        'location': 'Boise, Idaho',
        'venue': 'CenturyLink Arena',
        'fights': [
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': JODIE_ESQUIBEL,
                        'stats': '6-4-0',
                    },
                    {
                        'name': JESSICA_AGUILAR,
                        'stats': '20-8-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_AGUILAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:40',
                'odds': {
                    JESSICA_AGUILAR: 2.31,
                    JODIE_ESQUIBEL: 1.57,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ELIAS_GARCIA,
                        'stats': '6-2-0',
                    },
                    {
                        'name': MARK_DE_LA_ROSA,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': MARK_DE_LA_ROSA,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:00',
                },
                'time': '17:00',
                'odds': {
                    MARK_DE_LA_ROSA: 2.14,
                    ELIAS_GARCIA: 1.67,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JENNIFER_MAIA,
                        'stats': '16-5-1',
                    },
                    {
                        'name': LIZ_CARMOUCHE,
                        'stats': '13-6-0',
                    },
                ],
                'winner': {
                    'fighter': LIZ_CARMOUCHE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:10',
                'odds': {
                    LIZ_CARMOUCHE: 1.80,
                    JENNIFER_MAIA: 1.95,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RAONI_BARCELOS,
                        'stats': '13-1-0',
                    },
                    {
                        'name': KURT_HOLOBAUGH,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': RAONI_BARCELOS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:29',
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SAID_NURMAGOMEDOV,
                        'stats': '13-1-0',
                    },
                    {
                        'name': JUSTIN_SCOGGINS,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': SAID_NURMAGOMEDOV,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    SAID_NURMAGOMEDOV: 1.77,
                    JUSTIN_SCOGGINS: 1.98,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': DARREN_ELKINS,
                        'stats': '25-7-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    ALEXANDER_VOLKANOVSKI: 1.43,
                    DARREN_ELKINS: 2.80,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ALEJANDRO_PEREZ,
                        'stats': '22-7-1',
                    },
                    {
                        'name': EDDIE_WINELAND,
                        'stats': '23-13-1',
                    },
                ],
                'winner': {
                    'fighter': ALEJANDRO_PEREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    ALEJANDRO_PEREZ: 1.54,
                    EDDIE_WINELAND: 2.47,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARION_RENEAU,
                        'stats': '9-5-1',
                    },
                    {
                        'name': CAT_ZINGANO,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': CAT_ZINGANO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    CAT_ZINGANO: 1.91,
                    MARION_RENEAU: 1.83,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CHAD_MENDES,
                        'stats': '18-5-0',
                    },
                    {
                        'name': MYLES_JURY,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': CHAD_MENDES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:52',
                },
                'time': '23:00',
                'odds': {
                    CHAD_MENDES: 1.48,
                    MYLES_JURY: 1.98,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NIKO_PRICE,
                        'stats': '13-2-0',
                    },
                    {
                        'name': RANDY_BROWN,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': NIKO_PRICE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:09',
                },
                'time': '20:35',
                'odds': {
                    NIKO_PRICE: 2.05,
                    RANDY_BROWN: 1.74,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RICK_GLENN,
                        'stats': '21-6-1',
                    },
                    {
                        'name': DENNIS_BERMUDEZ,
                        'stats': '18-9-0',
                    },
                ],
                'winner': {
                    'fighter': RICK_GLENN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:00',
                'odds': {
                    RICK_GLENN: 2.46,
                    DENNIS_BERMUDEZ: 1.53,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ZAK_OTTOW,
                        'stats': '17-7-0',
                    },
                    {
                        'name': SAGE_NORTHCUTT,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': SAGE_NORTHCUTT,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:13',
                },
                'time': '23:30',
                'odds': {
                    SAGE_NORTHCUTT: 1.67,
                    ZAK_OTTOW: 2.07,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': BLAGOY_IVANOV,
                        'stats': '17-2-0',
                    },
                    {
                        'name': JUNIOR_DOS_SANTOS,
                        'stats': '21-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUNIOR_DOS_SANTOS,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '12:30',
                'odds': {
                    JUNIOR_DOS_SANTOS: 1.50,
                    BLAGOY_IVANOV: 2.55,
                },
            },
        ]
    },

    {
        'date': '2018-07-22',
        'name': 'UFC Fight Night',
        'location': 'Hamburg, Germany',
        'venue': 'Barclaycard Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LIU_PINGYUAN,
                        'stats': '13-5-0',
                    },
                    {
                        'name': DAMIAN_STASIAK,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': LIU_PINGYUAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '10:30',
                'odds': {
                    LIU_PINGYUAN: 1.91,
                    DAMIAN_STASIAK: 1.74,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DARKO_STOSIC,
                        'stats': '13-1-0',
                    },
                    {
                        'name': JEREMY_KIMBALL,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': DARKO_STOSIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:13',
                },
                'time': '11:00',
                'odds': {
                    DARKO_STOSIC: 1.36,
                    JEREMY_KIMBALL: 3.00,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MANNY_BERMUDEZ,
                        'stats': '14-0-0',
                    },
                    {
                        'name': DAVEY_GRANT,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': MANNY_BERMUDEZ,
                    'by': 'submission',
                    'round': 1,
                    'time': '0:59',
                },
                'time': '11:30',
                'odds': {
                    MANNY_BERMUDEZ: 1.29,
                    DAVEY_GRANT: 3.60,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSANDAR_RAKIC,
                        'stats': '1-1-0',
                    },
                    {
                        'name': JUSTIN_LEDET,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSANDAR_RAKIC,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:00',
                'odds': {
                    ALEKSANDAR_RAKIC: 1.83,
                    JUSTIN_LEDET: 1.84,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': KHALID_TAHA,
                        'stats': '12-2-0',
                    },
                    {
                        'name': NAD_NARIMANI,
                        'stats': '12-3-0',
                    },
                ],
                'winner': {
                    'fighter': NAD_NARIMANI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '12:30',
                'odds': {
                    NAD_NARIMANI: 1.43,
                    KHALID_TAHA: 2.72,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': EMIL_MEEK,
                        'stats': '9-4-1',
                    },
                    {
                        'name': BARTOSZ_FABINSKI,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': BARTOSZ_FABINSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '1:00',
                'odds': {
                    BARTOSZ_FABINSKI: 2.15,
                    EMIL_MEEK: 1.67,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAMIR_HADZOVIC,
                        'stats': '13-4-0',
                    },
                    {
                        'name': NICK_HEIN,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIR_HADZOVIC,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '1:30',
                'odds': {
                    DAMIR_HADZOVIC: 2.27,
                    NICK_HEIN: 1.61,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': NASRAT_HAQPARAST,
                        'stats': '10-2-0',
                    },
                    {
                        'name': MARC_DIAKIESE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': NASRAT_HAQPARAST,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:00',
                'odds': {
                    NASRAT_HAQPARAST: 2.32,
                    MARC_DIAKIESE: 1.57,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_ZAWADA,
                        'stats': '16-5-0',
                    },
                    {
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': DANNY_ROBERTS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '14:30',
                'odds': {
                    DANNY_ROBERTS: 1.43,
                    DAVID_ZAWADA: 2.75,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MARCIN_TYBURA,
                        'stats': '17-4-0',
                    },
                    {
                        'name': STEFAN_STRUVE,
                        'stats': '33-11-0',
                    },
                ],
                'winner': {
                    'fighter': MARCIN_TYBURA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:00',
                'odds': {
                    MARCIN_TYBURA: 1.49,
                    STEFAN_STRUVE: 2.60,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ABU_AZAITAR,
                        'stats': '14-1-1',
                    },
                    {
                        'name': VITOR_MIRANDA,
                        'stats': '13-7-0',
                    },
                ],
                'winner': {
                    'fighter': ABU_AZAITAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '15:30',
                'odds': {
                    ABU_AZAITAR: 1.43,
                    VITOR_MIRANDA: 2.70,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': COREY_ANDERSON,
                        'stats': '13-4-0',
                    },
                    {
                        'name': GLOVER_TEIXEIRA,
                        'stats': '28-7-0',
                    },
                ],
                'winner': {
                    'fighter': COREY_ANDERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:00',
                'odds': {
                    COREY_ANDERSON: 2.02,
                    GLOVER_TEIXEIRA: 1.74,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': MAURICIO_RUA,
                        'stats': '26-11-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_SMITH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:29',
                },
                'time': '16:30',
                'odds': {
                    ANTHONY_SMITH: 1.63,
                    MAURICIO_RUA: 2.22,
                },
            },
        ]
    },

    {
        'date': '2018-07-28',
        'name': 'UFC Fight Night',
        'location': 'Calgary, Alberta',
        'venue': 'Scotiabank Saddledome',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DEVIN_POWELL,
                        'stats': '9-4-0',
                    },
                    {
                        'name': ALVARO_HERRERA,
                        'stats': '9-6-0',
                    },
                ],
                'winner': {
                    'fighter': DEVIN_POWELL,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:52',
                },
                'time': '16:00',
                'odds': {
                    DEVIN_POWELL: 1.91,
                    ALVARO_HERRERA: 1.83,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': RANDA_MARKOS,
                        'stats': '9-7-1',
                    },
                    {
                        'name': NINA_ANSAROFF,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': NINA_ANSAROFF,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '16:30',
                'odds': {
                    NINA_ANSAROFF: 1.67,
                    RANDA_MARKOS: 2.16,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MATHEUS_NICOLAU,
                        'stats': '13-3-1',
                    },
                    {
                        'name': DUSTIN_ORTIZ,
                        'stats': '19-8-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_ORTIZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:49',
                },
                'time': '17:00',
                'odds': {
                    DUSTIN_ORTIZ: 2.62,
                    MATHEUS_NICOLAU: 1.49,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ALEXIS_DAVIS,
                        'stats': '19-9-0',
                    },
                ],
                'winner': {
                    'fighter': KATLYN_CHOOKAGIAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:30',
                'odds': {
                    KATLYN_CHOOKAGIAN: 1.59,
                    ALEXIS_DAVIS: 2.35,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ROSS_PEARSON,
                        'stats': '22-16-0',
                    },
                    {
                        'name': JOHN_MAKDESSI,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': JOHN_MAKDESSI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '17:30',
                'odds': {
                    JOHN_MAKDESSI: 1.43,
                    ROSS_PEARSON: 2.80,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': GADZHIMURAD_ANTIGULOV,
                        'stats': '20-5-0',
                    },
                    {
                        'name': ION_CUTELABA,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': ION_CUTELABA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:25',
                },
                'time': '18:00',
                'odds': {
                    ION_CUTELABA: 1.72,
                    GADZHIMURAD_ANTIGULOV: 2.05,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ISLAM_MAKHACHEV,
                        'stats': '16-1-0',
                    },
                    {
                        'name': KAJAN_JOHNSON,
                        'stats': '23-14-1',
                    },
                ],
                'winner': {
                    'fighter': ISLAM_MAKHACHEV,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:43',
                },
                'time': '18:30',
                'odds': {
                    ISLAM_MAKHACHEV: 1.17,
                    KAJAN_JOHNSON: 5.00,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HAKEEM_DAWODU,
                        'stats': '9-0-1',
                    },
                    {
                        'name': AUSTIN_ARNETT,
                        'stats': '16-6-0',
                    },
                ],
                'winner': {
                    'fighter': HAKEEM_DAWODU,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    HAKEEM_DAWODU: 1.20,
                    AUSTIN_ARNETT: 4.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_MORONO,
                        'stats': '16-5-0',
                    },
                    {
                        'name': JORDAN_MEIN,
                        'stats': '31-12-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_MEIN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    JORDAN_MEIN: 1.65,
                    ALEX_MORONO: 2.25,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_HERNANDEZ,
                        'stats': '10-2-0',
                    },
                    {
                        'name': OLIVIER_AUBIN_MERCIER,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_HERNANDEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    ALEXANDER_HERNANDEZ: 1.91,
                    OLIVIER_AUBIN_MERCIER: 1.83,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': TECIA_TORRES,
                        'stats': '10-4-0',
                    },
                    {
                        'name': JOANNA_JEDRZEJCZYK,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': JOANNA_JEDRZEJCZYK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    JOANNA_JEDRZEJCZYK: 1.31,
                    TECIA_TORRES: 3.30,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JEREMY_STEPHENS,
                        'stats': '28-16-0',
                    },
                    {
                        'name': JOSE_ALDO,
                        'stats': '28-4-0',
                    },
                ],
                'winner': {
                    'fighter': JOSE_ALDO,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:19',
                },
                'time': '21:00',
                'odds': {
                    JOSE_ALDO: 1.97,
                    JEREMY_STEPHENS: 1.77,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': EDDIE_ALVAREZ,
                        'stats': '29-6-0',
                    },
                    {
                        'name': DUSTIN_POIRIER,
                        'stats': '24-5-0',
                    },
                ],
                'winner': {
                    'fighter': DUSTIN_POIRIER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:05',
                },
                'time': '21:30',
                'odds': {
                    DUSTIN_POIRIER: 1.61,
                    EDDIE_ALVAREZ: 2.28,
                },
            },
        ]
    },

    {
        'date': '2018-08-04',
        'name': 'UFC 227',
        'location': 'Los Angeles, California',
        'venue': 'Staples Center',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': WULIJI_BUREN,
                        'stats': '10-7-0',
                    },
                    {
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:53',
                },
                'time': '18:30',
                'odds': {
                    MARLON_VERA: 1.18,
                    WULIJI_BUREN: 4.75,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ZHANG_WEILI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': DANIELLE_TAYLOR,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': ZHANG_WEILI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    ZHANG_WEILI: 1.27,
                    DANIELLE_TAYLOR: 3.70,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOSE_TORRES,
                        'stats': '8-1-0',
                    },
                    {
                        'name': ALEX_PEREZ,
                        'stats': '22-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_PEREZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:36',
                },
                'time': '19:30',
                'odds': {
                    ALEX_PEREZ: 1.67,
                    JOSE_TORRES: 1.94,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MATT_SAYLES,
                        'stats': '6-2-0',
                    },
                    {
                        'name': SHEYMON_DA_SILVA_MORAES,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': SHEYMON_DA_SILVA_MORAES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    SHEYMON_DA_SILVA_MORAES: 2.10,
                    MATT_SAYLES: 1.71,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RICARDO_RAMOS,
                        'stats': '12-1-0',
                    },
                    {
                        'name': KYUNG_HO_KANG,
                        'stats': '15-8-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_RAMOS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    RICARDO_RAMOS: 1.33,
                    KYUNG_HO_KANG: 3.30,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MONTEL_JACKSON,
                        'stats': '7-1-0',
                    },
                    {
                        'name': RICKY_SIMON,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': RICKY_SIMON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    RICKY_SIMON: 2.00,
                    MONTEL_JACKSON: 1.77,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRETT_JOHNS,
                        'stats': '15-2-0',
                    },
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                ],
                'winner': {
                    'fighter': PEDRO_MUNHOZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    PEDRO_MUNHOZ: 1.44,
                    BRETT_JOHNS: 2.68,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_HOLLAND,
                        'stats': '15-4-0',
                    },
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    THIAGO_SANTOS: 1.27,
                    KEVIN_HOLLAND: 3.75,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': POLYANA_VIANA,
                        'stats': '10-3-0',
                    },
                    {
                        'name': JJ_ALDRICH,
                        'stats': '7-3-0',
                    },
                ],
                'winner': {
                    'fighter': JJ_ALDRICH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    JJ_ALDRICH: 2.33,
                    POLYANA_VIANA: 1.59,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RENATO_MOICANO,
                        'stats': '13-2-1',
                    },
                    {
                        'name': CUB_SWANSON,
                        'stats': '25-10-0',
                    },
                ],
                'winner': {
                    'fighter': RENATO_MOICANO,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:15',
                },
                'time': '23:00',
                'odds': {
                    RENATO_MOICANO: 1.31,
                    CUB_SWANSON: 3.45,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': HENRY_CEJUDO,
                        'stats': '14-2-0',
                    },
                    {
                        'name': DEMETRIOUS_JOHNSON,
                        'stats': '27-3-1',
                    },
                ],
                'winner': {
                    'fighter': HENRY_CEJUDO,
                    'by': 's.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    HENRY_CEJUDO: 4.50,
                    DEMETRIOUS_JOHNSON: 1.19,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CODY_GARBRANDT,
                        'stats': '11-3-0',
                    },
                    {
                        'name': TJ_DILLASHAW,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': TJ_DILLASHAW,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:10',
                },
                'time': '23:59',
                'odds': {
                    TJ_DILLASHAW: 1.74,
                    CODY_GARBRANDT: 2.00,
                },
            },
        ]
    },

    {
        'date': '2018-08-25',
        'name': 'UFC Fight Night',
        'location': 'Lincoln, Nebraska',
        'venue': 'Pinnacle Bank Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUKE_SANDERS,
                        'stats': '13-3-0',
                    },
                    {
                        'name': RANI_YAHYA,
                        'stats': '26-10-0',
                    },
                ],
                'winner': {
                    'fighter': RANI_YAHYA,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:31',
                },
                'time': '18:30',
                'odds': {
                    RANI_YAHYA: 1.87,
                    LUKE_SANDERS: 1.87,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JON_TUCK,
                        'stats': '10-5-0',
                    },
                    {
                        'name': DREW_DOBER,
                        'stats': '20-9-0',
                    },
                ],
                'winner': {
                    'fighter': DREW_DOBER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    DREW_DOBER: 1.42,
                    JON_TUCK: 2.90,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KALINDRA_FARIA,
                        'stats': '18-8-1',
                    },
                    {
                        'name': JOANNE_CALDERWOOD,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': JOANNE_CALDERWOOD,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:57',
                },
                'time': '19:30',
                'odds': {
                    JOANNE_CALDERWOOD: 1.53,
                    KALINDRA_FARIA: 2.45,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICKEY_GALL,
                        'stats': '5-2-0',
                    },
                    {
                        'name': GEORGE_SULLIVAN,
                        'stats': '17-7-0',
                    },
                ],
                'winner': {
                    'fighter': MICKEY_GALL,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:09',
                },
                'time': '20:06',
                'odds': {
                    MICKEY_GALL: 1.27,
                    GEORGE_SULLIVAN: 3.70,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': MARKUS_PEREZ,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ANDREW_SANCHEZ,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANDREW_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:35',
                'odds': {
                    ANDREW_SANCHEZ: 1.69,
                    MARKUS_PEREZ: 2.07,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CORY_SANDHAGEN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': IURI_ALCANTARA,
                        'stats': '35-10-0',
                    },
                ],
                'winner': {
                    'fighter': CORY_SANDHAGEN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:01',
                },
                'time': '21:00',
                'odds': {
                    CORY_SANDHAGEN: 1.44,
                    IURI_ALCANTARA: 2.70,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': WARLLEY_ALVES,
                        'stats': '13-3-0',
                    },
                    {
                        'name': JAMES_KRAUSE,
                        'stats': '25-8-0',
                    },
                ],
                'winner': {
                    'fighter': JAMES_KRAUSE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:28',
                },
                'time': '21:30',
                'odds': {
                    JAMES_KRAUSE: 3.65,
                    WARLLEY_ALVES: 1.28,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TIM_WILLIAMS,
                        'stats': '15-5-0',
                    },
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': ERYK_ANDERS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:42',
                },
                'time': '22:00',
                'odds': {
                    ERYK_ANDERS: 1.07,
                    TIM_WILLIAMS: 8.50,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': DEIVESON_FIGUEIREDO,
                        'stats': '15-1-0',
                    },
                    {
                        'name': JOHN_MORAGA,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': DEIVESON_FIGUEIREDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '3:08',
                },
                'time': '22:30',
                'odds': {
                    DEIVESON_FIGUEIREDO: 1.57,
                    JOHN_MORAGA: 2.36,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BRYAN_BARBERENA,
                        'stats': '14-6-0',
                    },
                    {
                        'name': JAKE_ELLENBERGER,
                        'stats': '31-15-0',
                    },
                ],
                'winner': {
                    'fighter': BRYAN_BARBERENA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:26',
                },
                'time': '23:00',
                'odds': {
                    BRYAN_BARBERENA: 1.21,
                    JAKE_ELLENBERGER: 4.25,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CORTNEY_CASEY_SANCHEZ,
                        'stats': '8-6-0',
                    },
                    {
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                ],
                'winner': {
                    'fighter': CORTNEY_CASEY_SANCHEZ,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    CORTNEY_CASEY_SANCHEZ: 2.05,
                    ANGELA_HILL: 1.74,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_JOHNSON,
                        'stats': '20-14-0',
                    },
                    {
                        'name': ANDRE_FILI,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAEL_JOHNSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    MICHAEL_JOHNSON: 1.95,
                    ANDRE_FILI: 1.80,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_GAETHJE,
                        'stats': '20-2-0',
                    },
                    {
                        'name': JAMES_VICK,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_GAETHJE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:27',
                },
                'time': '23:59',
                'odds': {
                    JUSTIN_GAETHJE: 2.21,
                    JAMES_VICK: 1.65,
                },
            },
        ]
    },

    {
        'date': '2018-09-08',
        'name': 'UFC 228',
        'location': 'Dallas, Texas',
        'venue': 'American Airlines Center',
        'fights': [
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ROBERTO_SANCHEZ,
                        'stats': '8-2-0',
                    },
                    {
                        'name': JARRED_BROOKS,
                        'stats': '14-2-0',
                    },
                ],
                'winner': {
                    'fighter': JARRED_BROOKS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:10',
                'odds': {
                    JARRED_BROOKS: 1.33,
                    ROBERTO_SANCHEZ: 3.25,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LUCIE_PUDILOVA,
                        'stats': '8-4-0',
                    },
                    {
                        'name': IRENE_ALDANA,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': IRENE_ALDANA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:40',
                'odds': {
                    IRENE_ALDANA: 1.83,
                    LUCIE_PUDILOVA: 1.91,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_WHITE,
                        'stats': '13-5-0',
                    },
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': JIM_MILLER,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:29',
                },
                'time': '19:20',
                'odds': {
                    JIM_MILLER: 2.50,
                    ALEX_WHITE: 1.54,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CRAIG_WHITE,
                        'stats': '14-9-0',
                    },
                    {
                        'name': DIEGO_SANCHEZ,
                        'stats': '31-11-0',
                    },
                ],
                'winner': {
                    'fighter': DIEGO_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    DIEGO_SANCHEZ: 2.65,
                    CRAIG_WHITE: 1.43,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_BYRD,
                        'stats': '10-6-0',
                    },
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_STEWART,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:17',
                },
                'time': '20:00',
                'odds': {
                    DARREN_STEWART: 2.50,
                    CHARLES_BYRD: 1.53,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': GEOFF_NEAL,
                        'stats': '11-2-0',
                    },
                    {
                        'name': FRANK_CAMACHO,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': GEOFF_NEAL,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:23',
                },
                'time': '20:30',
                'odds': {
                    GEOFF_NEAL: 1.43,
                    FRANK_CAMACHO: 2.75,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CODY_STAMANN,
                        'stats': '18-2-0',
                    },
                    {
                        'name': ALJAMAIN_STERLING,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALJAMAIN_STERLING,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:42',
                },
                'time': '21:00',
                'odds': {
                    ALJAMAIN_STERLING: 1.54,
                    CODY_STAMANN: 2.45,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': TATIANA_SUAREZ,
                        'stats': '7-0-0',
                    },
                    {
                        'name': CARLA_ESPARZA,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': TATIANA_SUAREZ,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:33',
                },
                'time': '21:30',
                'odds': {
                    TATIANA_SUAREZ: 1.22,
                    CARLA_ESPARZA: 4.25,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NIKO_PRICE,
                        'stats': '13-2-0',
                    },
                    {
                        'name': ABDUL_RAZAK_ALHASSAN,
                        'stats': '10-1-0',
                    },
                ],
                'winner': {
                    'fighter': ABDUL_RAZAK_ALHASSAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:43',
                },
                'time': '22:00',
                'odds': {
                    ABDUL_RAZAK_ALHASSAN: 1.87,
                    NIKO_PRICE: 1.83,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JIMMIE_RIVERA,
                        'stats': '22-3-0',
                    },
                    {
                        'name': JOHN_DODSON,
                        'stats': '21-11-0',
                    },
                ],
                'winner': {
                    'fighter': JIMMIE_RIVERA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    JIMMIE_RIVERA: 1.65,
                    JOHN_DODSON: 2.20,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ZABIT_MAGOMEDSHARIPOV,
                        'stats': '17-1-0',
                    },
                    {
                        'name': BRANDON_DAVIS,
                        'stats': '9-5-0',
                    },
                ],
                'winner': {
                    'fighter': ZABIT_MAGOMEDSHARIPOV,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:46',
                },
                'time': '23:00',
                'odds': {
                    ZABIT_MAGOMEDSHARIPOV: 1.07,
                    BRANDON_DAVIS: 8.50,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': KAROLINA_KOWALKIEWICZ,
                        'stats': '13-4-0',
                    },
                    {
                        'name': JESSICA_ANDRADE,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ANDRADE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:58',
                },
                'time': '23:30',
                'odds': {
                    JESSICA_ANDRADE: 1.20,
                    KAROLINA_KOWALKIEWICZ: 4.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_TILL,
                        'stats': '17-2-1',
                    },
                    {
                        'name': TYRON_WOODLEY,
                        'stats': '19-4-1',
                    },
                ],
                'winner': {
                    'fighter': TYRON_WOODLEY,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:19',
                },
                'time': '23:59',
                'odds': {
                    TYRON_WOODLEY: 1.87,
                    DARREN_TILL: 1.83,
                },
            },
        ]
    },

    {
        'date': '2018-09-22',
        'name': 'UFC Fight Night',
        'location': 'Sao Paulo, Brazil',
        'venue': 'Ginasio do Ibirapuera',
        'fights': [
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': LIVINHA_SOUZA,
                        'stats': '12-1-0',
                    },
                    {
                        'name': ALEX_CHAMBERS,
                        'stats': '5-4-0',
                    },
                ],
                'winner': {
                    'fighter': LIVINHA_SOUZA,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:21',
                },
                'time': '18:30',
                'odds': {
                    LIVINHA_SOUZA: 1.05,
                    ALEX_CHAMBERS: 8.86,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LUIGI_VENDRAMINI,
                        'stats': '8-0-0',
                    },
                    {
                        'name': ELIZEU_DOS_SANTOS,
                        'stats': '20-5-0',
                    },
                ],
                'winner': {
                    'fighter': ELIZEU_DOS_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:20',
                },
                'time': '19:00',
                'odds': {
                    ELIZEU_DOS_SANTOS: 1.08,
                    LUIGI_VENDRAMINI: 8.00,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': HECTOR_LOMBARD,
                        'stats': '34-9-1',
                    },
                    {
                        'name': THALES_LEITES,
                        'stats': '28-9-0',
                    },
                ],
                'winner': {
                    'fighter': THALES_LEITES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    THALES_LEITES: 1.61,
                    HECTOR_LOMBARD: 2.31,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': MAYRA_BUENO_SILVA,
                        'stats': '6-0-0',
                    },
                    {
                        'name': GILLIAN_ROBERTSON,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAYRA_BUENO_SILVA,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:55',
                },
                'time': '19:50',
                'odds': {
                    MAYRA_BUENO_SILVA: 2.15,
                    GILLIAN_ROBERTSON: 1.68,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                    {
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                ],
                'winner': {
                    'fighter': SERGIO_MORAES,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:42',
                },
                'time': '20:10',
                'odds': {
                    SERGIO_MORAES: 1.35,
                    BEN_SAUNDERS: 3.15,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': AUGUSTO_SAKAI,
                        'stats': '12-1-1',
                    },
                    {
                        'name': CHASE_SHERMAN,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': AUGUSTO_SAKAI,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:03',
                },
                'time': '20:30',
                'odds': {
                    AUGUSTO_SAKAI: 1.40,
                    CHASE_SHERMAN: 2.65,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_SPANN,
                        'stats': '15-5-0',
                    },
                    {
                        'name': LUIS_HENRIQUE,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_SPANN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    RYAN_SPANN: 1.83,
                    LUIS_HENRIQUE: 1.87,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FRANCISCO_TRINALDO,
                        'stats': '23-6-0',
                    },
                    {
                        'name': EVAN_DUNHAM,
                        'stats': '18-7-1',
                    },
                ],
                'winner': {
                    'fighter': FRANCISCO_TRINALDO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:10',
                },
                'time': '21:30',
                'odds': {
                    FRANCISCO_TRINALDO: 1.53,
                    EVAN_DUNHAM: 2.45,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHRISTOS_GIAGOS,
                        'stats': '16-7-0',
                    },
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'submission',
                    'round': 2,
                    'time': '3:22',
                },
                'time': '22:00',
                'odds': {
                    CHARLES_OLIVEIRA: 1.20,
                    CHRISTOS_GIAGOS: 4.50,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': MARINA_RODRIGUEZ,
                        'stats': '11-0-1',
                    },
                    {
                        'name': RANDA_MARKOS,
                        'stats': '9-7-1',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': 'm.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    RANDA_MARKOS: 2.10,
                    MARINA_RODRIGUEZ: 1.71,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_EWELL,
                        'stats': '13-5-0',
                    },
                    {
                        'name': RENAN_BARAO,
                        'stats': '36-8-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_EWELL,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    ANDRE_EWELL: 2.65,
                    RENAN_BARAO: 1.49,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SAM_ALVEY,
                        'stats': '33-11-0',
                    },
                    {
                        'name': ROGERIO_NOGUEIRA,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': ROGERIO_NOGUEIRA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:00',
                },
                'time': '23:30',
                'odds': {
                    ROGERIO_NOGUEIRA: 3.70,
                    SAM_ALVEY: 1.25,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CARLO_PEDERSOLI_JR,
                        'stats': '11-2-0',
                    },
                    {
                        'name': ALEX_OLIVEIRA,
                        'stats': '19-6-1',
                    },
                ],
                'winner': {
                    'fighter': ALEX_OLIVEIRA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:39',
                },
                'time': '23:59',
                'odds': {
                    ALEX_OLIVEIRA: 1.18,
                    CARLO_PEDERSOLI_JR: 4.75,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    THIAGO_SANTOS: 1.49,
                    ERYK_ANDERS: 2.61,
                },
            },
        ]
    },

    {
        'date': '2018-10-06',
        'name': 'UFC 229',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                    {
                        'name': RYAN_LAFLARE,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_ROCCO_MARTIN,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:00',
                },
                'time': '18:15',
                'odds': {
                    ANTHONY_ROCCO_MARTIN: 2.00,
                    RYAN_LAFLARE: 1.74,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GRAY_MAYNARD,
                        'stats': '14-8-1',
                    },
                    {
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                ],
                'winner': {
                    'fighter': NIK_LENTZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:19',
                },
                'time': '18:45',
                'odds': {
                    NIK_LENTZ: 1.38,
                    GRAY_MAYNARD: 2.90,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': YANA_KUNITSKAYA,
                        'stats': '12-4-0',
                    },
                    {
                        'name': LINA_LANSBERG,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': YANA_KUNITSKAYA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:35',
                'odds': {
                    YANA_KUNITSKAYA: 1.36,
                    LINA_LANSBERG: 3.05,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SCOTT_HOLTZMAN,
                        'stats': '12-3-0',
                    },
                    {
                        'name': ALAN_PATRICK,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': SCOTT_HOLTZMAN,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '3:42',
                },
                'time': '19:15',
                'odds': {
                    SCOTT_HOLTZMAN: 3.60,
                    ALAN_PATRICK: 1.29,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ASPEN_LADD,
                        'stats': '7-0-0',
                    },
                    {
                        'name': TONYA_EVINGER,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': ASPEN_LADD,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:26',
                },
                'time': '20:00',
                'odds': {
                    ASPEN_LADD: 1.50,
                    TONYA_EVINGER: 2.55,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JALIN_TURNER,
                        'stats': '8-4-0',
                    },
                    {
                        'name': VICENTE_LUQUE,
                        'stats': '15-6-1',
                    },
                ],
                'winner': {
                    'fighter': VICENTE_LUQUE,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:52',
                },
                'time': '21:00',
                'odds': {
                    VICENTE_LUQUE: 1.12,
                    JALIN_TURNER: 5.50,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SERGIO_PETTIS,
                        'stats': '17-5-0',
                    },
                    {
                        'name': JUSSIER_FORMIGA,
                        'stats': '23-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUSSIER_FORMIGA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:40',
                'odds': {
                    JUSSIER_FORMIGA: 2.60,
                    SERGIO_PETTIS: 1.49,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': FELICE_HERRIG,
                        'stats': '14-8-0',
                    },
                    {
                        'name': MICHELLE_WATERSON,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': MICHELLE_WATERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:05',
                'odds': {
                    MICHELLE_WATERSON: 2.10,
                    FELICE_HERRIG: 1.71,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKOV,
                        'stats': '30-7-0',
                    },
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                ],
                'winner': {
                    'fighter': DERRICK_LEWIS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:49',
                },
                'time': '22:30',
                'odds': {
                    DERRICK_LEWIS: 2.30,
                    ALEXANDER_VOLKOV: 1.57,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DOMINICK_REYES,
                        'stats': '11-0-0',
                    },
                    {
                        'name': OVINCE_SAINT_PREUX,
                        'stats': '23-12-0',
                    },
                ],
                'winner': {
                    'fighter': DOMINICK_REYES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    DOMINICK_REYES: 1.41,
                    OVINCE_SAINT_PREUX: 2.80,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_PETTIS,
                        'stats': '22-8-0',
                    },
                    {
                        'name': TONY_FERGUSON,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': TONY_FERGUSON,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    TONY_FERGUSON: 1.24,
                    ANTHONY_PETTIS: 3.80,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KHABIB_NURMAGOMEDIV,
                        'stats': '27-0-0',
                    },
                    {
                        'name': CONOR_MCGREGOR,
                        'stats': '21-4-0',
                    },
                ],
                'winner': {
                    'fighter': KHABIB_NURMAGOMEDIV,
                    'by': 'submission',
                    'round': 4,
                    'time': '3:03',
                },
                'time': '23:59',
                'odds': {
                    KHABIB_NURMAGOMEDIV: 1.30,
                    CONOR_MCGREGOR: 2.65,
                },
            },
        ]
    },

    {
        'date': '2018-11-03',
        'name': 'UFC 230',
        'location': 'New York City, New York',
        'venue': 'Madison Square Garden',
        'fights': [
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ADAM_WIECZOREK,
                        'stats': '10-2-0',
                    },
                    {
                        'name': MARCOS_ROGERIO_DE_LIMA,
                        'stats': '16-7-1',
                    },
                ],
                'winner': {
                    'fighter': MARCOS_ROGERIO_DE_LIMA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '18:15',
                'odds': {
                    MARCOS_ROGERIO_DE_LIMA: 2.35,
                    ADAM_WIECZOREK: 1.57,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHANE_BURGOS,
                        'stats': '11-1-0',
                    },
                    {
                        'name': KURT_HOLOBAUGH,
                        'stats': '17-6-0',
                    },
                ],
                'winner': {
                    'fighter': SHANE_BURGOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:11',
                },
                'time': '19:00',
                'odds': {
                    SHANE_BURGOS: 1.22,
                    KURT_HOLOBAUGH: 4.25,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MATT_FREVOLA,
                        'stats': '6-1-1',
                    },
                    {
                        'name': LANDO_VANNATA,
                        'stats': '10-3-2',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': None,
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    LANDO_VANNATA: 1.40,
                    MATT_FREVOLA: 2.85,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LYMAN_GOOD,
                        'stats': '20-5-0',
                    },
                    {
                        'name': BEN_SAUNDERS,
                        'stats': '22-11-2',
                    },
                ],
                'winner': {
                    'fighter': LYMAN_GOOD,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:32',
                },
                'time': '20:00',
                'odds': {
                    LYMAN_GOOD: 1.33,
                    BEN_SAUNDERS: 3.30,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHEYMON_DA_SILVA_MORAES,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JULIO_ACRE,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': SHEYMON_DA_SILVA_MORAES,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    SHEYMON_DA_SILVA_MORAES: 3.15,
                    JULIO_ACRE: 1.36,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': SIJARA_EUBANKS,
                        'stats': '5-2-0',
                    },
                    {
                        'name': ROXANNE_MODAFFERI,
                        'stats': '3-3-0',
                    },
                ],
                'winner': {
                    'fighter': SIJARA_EUBANKS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    SIJARA_EUBANKS: 1.17,
                    ROXANNE_MODAFFERI: 5.00,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_RINALDI,
                        'stats': '14-7-0',
                    },
                    {
                        'name': JASON_KNIGHT,
                        'stats': '20-6-0',
                    },
                ],
                'winner': {
                    'fighter': JORDAN_RINALDI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    JORDAN_RINALDI: 3.40,
                    JASON_KNIGHT: 1.31,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ISRAEL_ADESANYA,
                        'stats': '16-0-0',
                    },
                    {
                        'name': DEREK_BRUNSON,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': ISRAEL_ADESANYA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:51',
                },
                'time': '22:00',
                'odds': {
                    ISRAEL_ADESANYA: 1.35,
                    DEREK_BRUNSON: 3.24,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KARL_ROBERSON,
                        'stats': '7-2-0',
                    },
                    {
                        'name': JACK_MARSHMAN,
                        'stats': '23-8-0',
                    },
                ],
                'winner': {
                    'fighter': KARL_ROBERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    KARL_ROBERSON: 1.29,
                    JACK_MARSHMAN: 3.65,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': JARED_CANNONIER,
                        'stats': '11-4-0',
                    },
                    {
                        'name': DAVID_BRANCH,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': JARED_CANNONIER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:39',
                },
                'time': '23:00',
                'odds': {
                    JARED_CANNONIER: 3.45,
                    DAVID_BRANCH: 1.30,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_WEIDMAN,
                        'stats': '14-4-0',
                    },
                    {
                        'name': JACARE_SOUZA,
                        'stats': '26-6-0',
                    },
                ],
                'winner': {
                    'fighter': JACARE_SOUZA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:46',
                },
                'time': '23:30',
                'odds': {
                    JACARE_SOUZA: 2.43,
                    CHRIS_WEIDMAN: 1.57,
                },
            },
            {
                'weight_class': DERRICK_LEWIS,
                'fighters': [
                    {
                        'name': DERRICK_LEWIS,
                        'stats': '21-7-0',
                    },
                    {
                        'name': DANIEL_CORMIER,
                        'stats': '22-1-0',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_CORMIER,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:14',
                },
                'time': '23:59',
                'odds': {
                    DANIEL_CORMIER: 1.21,
                    DERRICK_LEWIS: 4.00,
                },
            },
        ]
    },

    {
        'date': '2018-11-10',
        'name': 'UFC Fight Night',
        'location': 'Denver, Colorado',
        'venue': 'Pepsi Center',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARK_DE_LA_ROSA,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JOBY_SANCHEZ,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': MARK_DE_LA_ROSA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    MARK_DE_LA_ROSA: 1.36,
                    JOBY_SANCHEZ: 3.00,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOSEPH_MORALES,
                        'stats': '9-2-0',
                    },
                    {
                        'name': ERIC_SHELTON,
                        'stats': '12-6-0',
                    },
                ],
                'winner': {
                    'fighter': ERIC_SHELTON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    ERIC_SHELTON: 1.65,
                    JOSEPH_MORALES: 2.20,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DEVONTE_SMITH,
                        'stats': '10-1-0',
                    },
                    {
                        'name': JULIAN_EROSA,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': DEVONTE_SMITH,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:46',
                },
                'time': '20:00',
                'odds': {
                    DEVONTE_SMITH: 1.41,
                    JULIAN_EROSA: 2.84,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JOHN_GUNTHER,
                        'stats': '7-2-0',
                    },
                    {
                        'name': DAVI_RAMOS,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAVI_RAMOS,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:57',
                },
                'time': '20:30',
                'odds': {
                    DAVI_RAMOS: 1.08,
                    JOHN_GUNTHER: 7.75,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BOBBY_MOFFETT,
                        'stats': '13-4-0',
                    },
                    {
                        'name': CHAS_SKELLY,
                        'stats': '17-3-0',
                    },
                ],
                'winner': {
                    'fighter': BOBBY_MOFFETT,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:43',
                },
                'time': '21:00',
                'odds': {
                    BOBBY_MOFFETT: 1.77,
                    CHAS_SKELLY: 1.91,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ASHLEY_YODER,
                        'stats': '6-4-0',
                    },
                    {
                        'name': AMANDA_COOPER,
                        'stats': '4-5-0',
                    },
                ],
                'winner': {
                    'fighter': ASHLEY_YODER,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    ASHLEY_YODER: 1.67,
                    AMANDA_COOPER: 2.20,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MICHAEL_TRIZANO,
                        'stats': '9-0-0',
                    },
                    {
                        'name': LUIS_PENA,
                        'stats': '6-1-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAEL_TRIZANO,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    MICHAEL_TRIZANO: 2.33,
                    LUIS_PENA: 1.53,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': HANNA_CIFERS,
                        'stats': '9-3-0',
                    },
                    {
                        'name': MAYCEE_BARBER,
                        'stats': '5-0-0',
                    },
                ],
                'winner': {
                    'fighter': MAYCEE_BARBER,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:01',
                },
                'time': '22:30',
                'odds': {
                    MAYCEE_BARBER: 1.18,
                    HANNA_CIFERS: 4.23,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': THIAGO_MOISES,
                        'stats': '11-3-0',
                    },
                    {
                        'name': BENEIL_DARIUSH,
                        'stats': '16-4-1',
                    },
                ],
                'winner': {
                    'fighter': BENEIL_DARIUSH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    BENEIL_DARIUSH: 1.59,
                    THIAGO_MOISES: 2.25,
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RAQUEL_PENNINGTON,
                        'stats': '9-8-0',
                    },
                    {
                        'name': GERMAINE_DE_RANDAMIE,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': GERMAINE_DE_RANDAMIE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    GERMAINE_DE_RANDAMIE: 1.47,
                    RAQUEL_PENNINGTON: 2.60,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_PERRY,
                        'stats': '12-4-0',
                    },
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                ],
                'winner': {
                    'fighter': DONALD_CERRONE,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:46',
                },
                'time': '23:53',
                'odds': {
                    DONALD_CERRONE: 2.65,
                    MIKE_PERRY: 1.45,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': YAIR_RODRIGUEZ,
                        'stats': '12-2-0',
                    },
                    {
                        'name': CHAN_SUNG_JUNG,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': YAIR_RODRIGUEZ,
                    'by': 'ko/tko',
                    'round': 5,
                    'time': '4:59',
                },
                'time': '23:59',
                'odds': {
                    YAIR_RODRIGUEZ: 1.74,
                    CHAN_SUNG_JUNG: 2.05,
                },
            },
        ]
    },

    {
        'date': '2018-11-17',
        'name': 'UFC Fight Night',
        'location': 'Beunos Aires, Argentina',
        'venue': 'Parque Roca Arena',
        'fights': [
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': NAD_NARIMANI,
                        'stats': '12-3-0',
                    },
                    {
                        'name': ANDERSON_DOS_SANTOS,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': NAD_NARIMANI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    NAD_NARIMANI: 1.22,
                    ANDERSON_DOS_SANTOS: 3.97,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JESUS_PINEDO,
                        'stats': '16-5-1',
                    },
                    {
                        'name': DEVIN_POWELL,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': JESUS_PINEDO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:30',
                'odds': {
                    JESUS_PINEDO: 1.37,
                    DEVIN_POWELL: 3.00,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LAUREANO_STAROPOLI,
                        'stats': '8-1-0',
                    },
                    {
                        'name': HECTOR_ALDANA,
                        'stats': '4-3-0',
                    },
                ],
                'winner': {
                    'fighter': LAUREANO_STAROPOLI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    LAUREANO_STAROPOLI: 2.00,
                    HECTOR_ALDANA: 1.74,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': AUSTIN_ARNETT,
                        'stats': '16-6-0',
                    },
                    {
                        'name': HUMBERTO_BANDENAY,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': AUSTIN_ARNETT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    AUSTIN_ARNETT: 2.85,
                    HUMBERTO_BANDENAY: 1.40,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDRE_PANTOJA,
                        'stats': '20-3-0',
                    },
                    {
                        'name': ULKA_SASAKI,
                        'stats': '21-6-2',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDRE_PANTOJA,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:18',
                },
                'time': '20:30',
                'odds': {
                    ALEXANDRE_PANTOJA: 1.30,
                    ULKA_SASAKI: 3.45,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BARTOSZ_FABINSKI,
                        'stats': '14-3-0',
                    },
                    {
                        'name': MICHEL_PRAZERES,
                        'stats': '26-3-0',
                    },
                ],
                'winner': {
                    'fighter': MICHEL_PRAZERES,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:02',
                },
                'time': '21:00',
                'odds': {
                    MICHEL_PRAZERES: 1.61,
                    BARTOSZ_FABINSKI: 2.20,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': CYNTHIA_CALVILLO,
                        'stats': '8-1-0',
                    },
                    {
                        'name': POLIANA_BOTELHO,
                        'stats': '7-2-0',
                    },
                ],
                'winner': {
                    'fighter': CYNTHIA_CALVILLO,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:48',
                },
                'time': '22:00',
                'odds': {
                    CYNTHIA_CALVILLO: 2.50,
                    POLIANA_BOTELHO: 1.51,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MARLON_VERA,
                        'stats': '13-5-1',
                    },
                    {
                        'name': GUIDO_CANNETTI,
                        'stats': '8-5-0',
                    },
                ],
                'winner': {
                    'fighter': MARLON_VERA,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:31',
                },
                'time': '22:30',
                'odds': {
                    MARLON_VERA: 1.31,
                    GUIDO_CANNETTI: 3.45,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': IAN_HEINISCH,
                        'stats': '12-1-0',
                    },
                    {
                        'name': CEZAR_FERREIRA,
                        'stats': '14-7-0',
                    },
                ],
                'winner': {
                    'fighter': IAN_HEINISCH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    IAN_HEINISCH: 2.54,
                    CEZAR_FERREIRA: 1.50,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JOHNNY_WALKER,
                        'stats': '17-3-0',
                    },
                    {
                        'name': KHALIL_ROUNTREE,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOHNNY_WALKER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:57',
                },
                'time': '23:31',
                'odds': {
                    JOHNNY_WALKER: 2.30,
                    KHALIL_ROUNTREE: 1.61,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RICARDO_LAMAS,
                        'stats': '19-7-0',
                    },
                    {
                        'name': DARREN_ELKINS,
                        'stats': '25-7-0',
                    },
                ],
                'winner': {
                    'fighter': RICARDO_LAMAS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:09',
                },
                'time': '23:55',
                'odds': {
                    RICARDO_LAMAS: 1.50,
                    DARREN_ELKINS: 2.57,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SANTIAGO_PONZINIBBIO,
                        'stats': '28-3-0',
                    },
                    {
                        'name': NEIL_MAGNY,
                        'stats': '21-8-0',
                    },
                ],
                'winner': {
                    'fighter': SANTIAGO_PONZINIBBIO,
                    'by': 'ko/tko',
                    'round': 4,
                    'time': '2:36',
                },
                'time': '23:59',
                'odds': {
                    SANTIAGO_PONZINIBBIO: 1.40,
                    NEIL_MAGNY: 2.80,
                },
            },
        ]
    },

    {
        'date': '2018-11-24',
        'name': 'UFC Fight Night',
        'location': 'Beijing, China',
        'venue': 'Cadillac Arena',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LOUIS_SMOLKA,
                        'stats': '15-6-0',
                    },
                    {
                        'name': SU_MUDAERJI,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': LOUIS_SMOLKA,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:07',
                },
                'time': '3:30',
                'odds': {
                    LOUIS_SMOLKA: 1.57,
                    SU_MUDAERJI: 2.40,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_HOLLAND,
                        'stats': '15-4-0',
                    },
                    {
                        'name': JOHN_PHILLIPS,
                        'stats': '21-9-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_HOLLAND,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:05',
                },
                'time': '4:00',
                'odds': {
                    KEVIN_HOLLAND: 1.15,
                    JOHN_PHILLIPS: 5.00,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': YAN_XIAONAN,
                        'stats': '10-1-0',
                    },
                    {
                        'name': SYURI_KONDO,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': YAN_XIAONAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '4:30',
                'odds': {
                    YAN_XIAONAN: 1.22,
                    SYURI_KONDO: 4.10,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LIU_PINGYUAN,
                        'stats': '13-5-0',
                    },
                    {
                        'name': MARTIN_DAY,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': LIU_PINGYUAN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '5:00',
                'odds': {
                    LIU_PINGYUAN: 1.53,
                    MARTIN_DAY: 2.52,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ZHANG_WEILI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': JESSICA_AGUILAR,
                        'stats': '20-8-0',
                    },
                ],
                'winner': {
                    'fighter': ZHANG_WEILI,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:41',
                },
                'time': '5:30',
                'odds': {
                    ZHANG_WEILI: 1.14,
                    JESSICA_AGUILAR: 5.25,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': HU_YAOZONG,
                        'stats': '3-2-0',
                    },
                    {
                        'name': RASHAD_COULTER,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': RASHAD_COULTER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '6:00',
                'odds': {
                    RASHAD_COULTER: 1.95,
                    HU_YAOZONG: 1.77,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': WU_YANAN,
                        'stats': '10-2-0',
                    },
                    {
                        'name': LAUREN_MUELLER,
                        'stats': '5-1-0',
                    },
                ],
                'winner': {
                    'fighter': WU_YANAN,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:00',
                },
                'time': '6:30',
                'odds': {
                    WU_YANAN: 3.75,
                    LAUREN_MUELLER: 1.26,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SONG_KENAN,
                        'stats': '13-5-0',
                    },
                    {
                        'name': ALEX_MORONO,
                        'stats': '16-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_MORONO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    ALEX_MORONO: 2.14,
                    SONG_KENAN: 1.69,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DAVID_ZAWADA,
                        'stats': '16-5-0',
                    },
                    {
                        'name': LI_JINGLIANG,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': LI_JINGLIANG,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:07',
                },
                'time': '19:30',
                'odds': {
                    LI_JINGLIANG: 1.44,
                    DAVID_ZAWADA: 2.70,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': VINCE_MORALES,
                        'stats': '0-0-0',
                    },
                    {
                        'name': SONG_YADONG,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': SONG_YADONG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    SONG_YADONG: 1.17,
                    VINCE_MORALES: 5.00,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SERGEI_PAVLOVICH,
                        'stats': '12-1-0',
                    },
                    {
                        'name': ALISTAIR_OVEREEM,
                        'stats': '44-17-0',
                    },
                ],
                'winner': {
                    'fighter': ALISTAIR_OVEREEM,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:21',
                },
                'time': '20:30',
                'odds': {
                    ALISTAIR_OVEREEM: 2.07,
                    SERGEI_PAVLOVICH: 1.65,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_BLAYDES,
                        'stats': '11-2-0',
                    },
                    {
                        'name': FRANCIS_NGANNOU,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': FRANCIS_NGANNOU,
                    'by': 'kko/tko',
                    'round': 1,
                    'time': '0:45',
                },
                'time': '20:59',
                'odds': {
                    FRANCIS_NGANNOU: 2.85,
                    CURTIS_BLAYDES: 1.41,
                },
            },
        ]
    },

    {
        'date': '2018-11-30',
        'name': 'UFC - TUF 28 Finale',
        'location': 'Las Vegas, Nevada',
        'venue': 'Pearl Concert Theater',
        'fights': [
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_GUTIERREZ,
                        'stats': '12-3-0',
                    },
                    {
                        'name': RAONI_BARCELOS,
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': RAONI_BARCELOS,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:12',
                },
                'time': '20:30',
                'odds': {
                    RAONI_BARCELOS: 1.18,
                    CHRIS_GUTIERREZ: 4.75,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': RICKEY_RAINEY,
                        'stats': '13-6-0',
                    },
                    {
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                ],
                'winner': {
                    'fighter': TIM_MEANS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:18',
                },
                'time': '21:00',
                'odds': {
                    TIM_MEANS: 1.27,
                    RICKEY_RAINEY: 3.55,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': ROOSEVELT_ROBERTS,
                        'stats': '7-0-0',
                    },
                    {
                        'name': DARRELL_HORCHER,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': ROOSEVELT_ROBERTS,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:50',
                },
                'time': '21:30',
                'odds': {
                    ROOSEVELT_ROBERTS: 1.27,
                    DARRELL_HORCHER: 3.55,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': LEAH_LETSON,
                        'stats': '4-2-0',
                    },
                    {
                        'name': JULIJA_STOLIARENKO,
                        'stats': '4-3-1',
                    },
                ],
                'winner': {
                    'fighter': LEAH_LETSON,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MICHEL_BATISTA,
                        'stats': '4-1-0',
                    },
                    {
                        'name': MAURICE_GREEN,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAURICE_GREEN,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:14',
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_PEREZ,
                        'stats': '22-5-0',
                    },
                    {
                        'name': JOSEPH_BENAVIDEZ,
                        'stats': '27-5-0',
                    },
                ],
                'winner': {
                    'fighter': JOSEPH_BENAVIDEZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:19',
                },
                'time': '22:00',
                'odds': {
                    JOSEPH_BENAVIDEZ: 2.00,
                    ALEX_PEREZ: 1.69,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_AGUILAR,
                        'stats': '0-0-0',
                    },
                    {
                        'name': RICK_GLENN,
                        'stats': '21-6-1',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_AGUILAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    KEVIN_AGUILAR: 1.91,
                    RICK_GLENN: 1.75,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANTONINA_SHEVCHENKO,
                        'stats': '7-0-0',
                    },
                    {
                        'name': JI_YEON_KIM,
                        'stats': '7-2-2',
                    },
                ],
                'winner': {
                    'fighter': ANTONINA_SHEVCHENKO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    ANTONINA_SHEVCHENKO: 1.33,
                    JI_YEON_KIM: 3.25,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': EDMEN_SHAHBAZYAN,
                        'stats': '9-0-0',
                    },
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': EDMEN_SHAHBAZYAN,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    EDMEN_SHAHBAZYAN: 1.80,
                    DARREN_STEWART: 1.93,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
                    },
                    {
                        'name': BRYAN_CARAWAY,
                        'stats': '21-10-0',
                    },
                ],
                'winner': {
                    'fighter': PEDRO_MUNHOZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:39',
                },
                'time': '23:50',
                'odds': {
                    PEDRO_MUNHOZ: 1.33,
                    BRYAN_CARAWAY: 3.30,
                },
            },
            {
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MACY_CHIASSON,
                        'stats': '5-0-0',
                    },
                    {
                        'name': PANNIE_KIANZAD,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': MACY_CHIASSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:11',
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_FRAZIER,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JUAN_ESPINO,
                        'stats': '9-1-0',
                    },
                ],
                'winner': {
                    'fighter': JUAN_ESPINO,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:36',
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KAMARU_USMAN,
                        'stats': '15-1-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': KAMARU_USMAN,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    KAMARU_USMAN: 1.30,
                    RAFAEL_DOS_ANJOS: 3.55,
                },
            },
        ]
    },

    {
        'date': '2018-12-01',
        'name': 'UFC Fight Night',
        'location': 'Adelaide, Australia',
        'venue': 'Adelaide Entertainment Centre',
        'fights': [
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAMIR_ISMAGULOV,
                        'stats': '17-2-0',
                    },
                    {
                        'name': ALEX_GORGEES,
                        'stats': '6-0-0',
                    },
                ],
                'winner': {
                    'fighter': DAMIR_ISMAGULOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '19:00',
                'odds': {
                    DAMIR_ISMAGULOV: 1.18,
                    ALEX_GORGEES: 4.50,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHRISTOS_GIAGOS,
                        'stats': '16-7-0',
                    },
                    {
                        'name': MIZUTO_HIROTA,
                        'stats': '19-10-2',
                    },
                ],
                'winner': {
                    'fighter': CHRISTOS_GIAGOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    CHRISTOS_GIAGOS: 1.25,
                    MIZUTO_HIROTA: 3.70,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KAI_KARA_FRANCE,
                        'stats': '19-7-0',
                    },
                    {
                        'name': ELIAS_GARCIA,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': KAI_KARA_FRANCE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    KAI_KARA_FRANCE: 1.24,
                    ELIAS_GARCIA: 4.05,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SALIM_TOUAHRI,
                        'stats': '10-3-0',
                    },
                    {
                        'name': KEITA_NAKAMURA,
                        'stats': '34-9-2',
                    },
                ],
                'winner': {
                    'fighter': KEITA_NAKAMURA,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    KEITA_NAKAMURA: 1.61,
                    SALIM_TOUAHRI: 2.28,
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': BEN_NGUYEN,
                        'stats': '17-8-0',
                    },
                    {
                        'name': WILSON_REIS,
                        'stats': '23-9-0',
                    },
                ],
                'winner': {
                    'fighter': WILSON_REIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    WILSON_REIS: 2.23,
                    BEN_NGUYEN: 1.65,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSEI_KUNCHENKO,
                        'stats': '20-0-0',
                    },
                    {
                        'name': YUSHIN_OKAMI,
                        'stats': '34-13-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSEI_KUNCHENKO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    ALEKSEI_KUNCHENKO: 1.31,
                    YUSHIN_OKAMI: 3.30,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JIMMY_CRUTE,
                        'stats': '10-0-0',
                    },
                    {
                        'name': PAUL_CRAIG,
                        'stats': '11-3-0',
                    },
                ],
                'winner': {
                    'fighter': JIMMY_CRUTE,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:51',
                },
                'time': '22:00',
                'odds': {
                    JIMMY_CRUTE: 1.32,
                    PAUL_CRAIG: 3.45,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SODIQ_YUSUFF,
                        'stats': '9-1-0',
                    },
                    {
                        'name': SUMAN_MOKHTARIAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': SODIQ_YUSUFF,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:14',
                },
                'time': '22:30',
                'odds': {
                    SODIQ_YUSUFF: 1.17,
                    SUMAN_MOKHTARIAN: 4.85,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': JAKE_MATTHEWS,
                        'stats': '13-4-0',
                    },
                    {
                        'name': ANTHONY_ROCCO_MARTIN,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_ROCCO_MARTIN,
                    'by': 'submission',
                    'round': 3,
                    'time': '1:19',
                },
                'time': '23:00',
                'odds': {
                    ANTHONY_ROCCO_MARTIN: 2.30,
                    JAKE_MATTHEWS: 1.63,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUSTIN_WILLIS,
                        'stats': '8-2-0',
                    },
                    {
                        'name': MARK_HUNT,
                        'stats': '13-14-1',
                    },
                ],
                'winner': {
                    'fighter': JUSTIN_WILLIS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    JUSTIN_WILLIS: 1.83,
                    MARK_HUNT: 1.87,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TYSON_PEDRO,
                        'stats': '7-2-0',
                    },
                    {
                        'name': MAURICIO_RUA,
                        'stats': '26-11-0',
                    },
                ],
                'winner': {
                    'fighter': MAURICIO_RUA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:43',
                },
                'time': '23:55',
                'odds': {
                    MAURICIO_RUA: 4.50,
                    TYSON_PEDRO: 1.18,
                },
            },
            {
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': TAI_TUIVASA,
                        'stats': '10-1-0',
                    },
                    {
                        'name': JUNIOR_DOS_SANTOS,
                        'stats': '21-5-0',
                    },
                ],
                'winner': {
                    'fighter': JUNIOR_DOS_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:30',
                },
                'time': '23:59',
                'odds': {
                    JUNIOR_DOS_SANTOS: 1.61,
                    TAI_TUIVASA: 2.27,
                },
            },
        ]
    },

    {
        'date': '2018-12-08',
        'name': 'UFC 231',
        'location': 'Toronto, Ontario',
        'venue': 'Scotiabank Arena',
        'fights': [
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSANDAR_RAKIC,
                        'stats': '1-1-0',
                    },
                    {
                        'name': DEVIN_CLARK,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSANDAR_RAKIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:05',
                },
                'time': '18:30',
                'odds': {
                    ALEKSANDAR_RAKIC: 1.17,
                    DEVIN_CLARK: 4.75,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KYLE_NELSON,
                        'stats': '12-2-0',
                    },
                    {
                        'name': DIEGO_FERREIRA,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': DIEGO_FERREIRA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '1:23',
                },
                'time': '19:00',
                'odds': {
                    DIEGO_FERREIRA: 1.18,
                    KYLE_NELSON: 4.75,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DHIEGO_LIMA,
                        'stats': '15-7-0',
                    },
                    {
                        'name': CHAD_LAPRISE,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': DHIEGO_LIMA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:37',
                },
                'time': '19:30',
                'odds': {
                    DHIEGO_LIMA: 4.00,
                    CHAD_LAPRISE: 1.25,
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BRAD_KATONA,
                        'stats': '9-0-0',
                    },
                    {
                        'name': MATTHEW_LOPEZ,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': BRAD_KATONA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:00',
                'odds': {
                    BRAD_KATONA: 1.61,
                    MATTHEW_LOPEZ: 2.35,
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ERYK_ANDERS,
                        'stats': '11-3-0',
                    },
                    {
                        'name': ELIAS_THEODOROU,
                        'stats': '17-2-0',
                    },
                ],
                'winner': {
                    'fighter': ELIAS_THEODOROU,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '20:30',
                'odds': {
                    ELIAS_THEODOROU: 1.70,
                    ERYK_ANDERS: 2.05,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    },
                    {
                        'name': JESSICA_EYE,
                        'stats': '14-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_EYE,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:00',
                'odds': {
                    JESSICA_EYE: 2.88,
                    KATLYN_CHOOKAGIAN: 1.40,
                },
            },
            {
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': GILBERT_BURNS,
                        'stats': '14-3-0',
                    },
                    {
                        'name': OLIVIER_AUBIN_MERCIER,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': GILBERT_BURNS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:30',
                'odds': {
                    GILBERT_BURNS: 2.09,
                    OLIVIER_AUBIN_MERCIER: 1.69,
                },
            },
            {
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': NINA_ANSAROFF,
                        'stats': '10-5-0',
                    },
                    {
                        'name': CLAUDIA_GADELHA,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': NINA_ANSAROFF,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:00',
                'odds': {
                    NINA_ANSAROFF: 3.40,
                    CLAUDIA_GADELHA: 1.29,
                },
            },
            {
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': THIAGO_SANTOS,
                        'stats': '21-6-0',
                    },
                    {
                        'name': JIMI_MANUWA,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': THIAGO_SANTOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:41',
                },
                'time': '22:30',
                'odds': {
                    THIAGO_SANTOS: 1.50,
                    JIMI_MANUWA: 2.52,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': HAKEEM_DAWODU,
                        'stats': '9-0-1',
                    },
                    {
                        'name': KYLE_BOCHNIAK,
                        'stats': '8-4-0',
                    },
                ],
                'winner': {
                    'fighter': HAKEEM_DAWODU,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:00',
                'odds': {
                    HAKEEM_DAWODU: 1.49,
                    KYLE_BOCHNIAK: 2.50,
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_OLIVEIRA,
                        'stats': '19-6-1',
                    },
                    {
                        'name': GUNNAR_NELSON,
                        'stats': '17-4-1',
                    },
                ],
                'winner': {
                    'fighter': GUNNAR_NELSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:17',
                },
                'time': '23:30',
                'odds': {
                    ALEX_OLIVEIRA: 2.20,
                    GUNNAR_NELSON: 1.63,
                },
            },
            {
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': VALENTINA_SHEVCHENKO,
                        'stats': '16-3-0',
                    },
                    {
                        'name': JOANNA_JEDRZEJCZYK,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': VALENTINA_SHEVCHENKO,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:54',
                'odds': {
                    VALENTINA_SHEVCHENKO: 1.31,
                    JOANNA_JEDRZEJCZYK: 3.30,
                },
            },
            {
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': BRIAN_ORTEGA,
                        'stats': '14-1-0',
                    },
                    {
                        'name': MAX_HOLLOWAY,
                        'stats': '20-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAX_HOLLOWAY,
                    'by': 'tko',
                    'round': 4,
                    'time': '5:00',
                },
                'time': '23:59',
                'odds': {
                    MAX_HOLLOWAY: 1.91,
                    BRIAN_ORTEGA: 1.80,
                },
            },
        ]
    },

    {
        'date': '2018-12-15',
        'name': 'UFC Fight Night',
        'location': 'Milwaukee, Wisconsin',
        'venue': 'Fiserv Forum',
        'fights': [
            {
                'time': '15:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUAN_ADAMS,
                        'stats': '5-0-0',
                    },
                    {
                        'name': CHRIS_DE_LA_ROCHA,
                        'stats': '5-3-0',
                    },
                ],
                'winner': {
                    'fighter': JUAN_ADAMS,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '0:58',
                },
                'odds': {
                    JUAN_ADAMS: 1.18,
                    CHRIS_DE_LA_ROCHA: 4.50,
                },
            },
            {
                'time': '16:00',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TREVOR_SMITH,
                        'stats': '15-9-0',
                    },
                    {
                        'name': ZAK_CUMMINGS,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': ZAK_CUMMINGS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ZAK_CUMMINGS: 1.29,
                    TREVOR_SMITH: 3.45,
                },
            },
            {
                'time': '16:30',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_RODRIGUEZ,
                        'stats': '10-3-0',
                    },
                    {
                        'name': ADAM_MILSTEAD,
                        'stats': '8-3-0',
                    },
                ],
                'winner': {
                    'fighter': MIKE_RODRIGUEZ,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:59',
                },
                'odds': {
                    MIKE_RODRIGUEZ: 1.83,
                    ADAM_MILSTEAD: 1.87,
                },
            },
            {
                'time': '17:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JORDAN_GRIFFIN,
                        'stats': '17-6-0',
                    },
                    {
                        'name': DAN_IGE,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_IGE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DAN_IGE: 1.56,
                    JORDAN_GRIFFIN: 1.77,
                },
            },
            {
                'time': '18:15',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': GERALD_MEERSCHAERT,
                        'stats': '28-11-0',
                    },
                    {
                        'name': JACK_HERMANSSON,
                        'stats': '19-4-0',
                    },
                ],
                'winner': {
                    'fighter': JACK_HERMANSSON,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:25',
                },
                'odds': {
                    JACK_HERMANSSON: 1.61,
                    GERALD_MEERSCHAERT: 2.33,
                },
            },
            {
                'time': '18:45',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': JARED_GORDON,
                        'stats': '14-3-0',
                    },
                    {
                        'name': JOAQUIM_SILVA,
                        'stats': '11-1-0',
                    },
                ],
                'winner': {
                    'fighter': JOAQUIM_SILVA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:39',
                },
                'odds': {
                    JOAQUIM_SILVA: 1.94,
                    JARED_GORDON: 1.77,
                },
            },
            {
                'time': '19:15',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DRAKKAR_KLOSE,
                        'stats': '10-1-1',
                    },
                    {
                        'name': BOBBY_GREEN,
                        'stats': '24-9-1',
                    },
                ],
                'winner': {
                    'fighter': DRAKKAR_KLOSE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DRAKKAR_KLOSE: 1.39,
                    BOBBY_GREEN: 2.90,
                },
            },
            {
                'time': '19:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DWIGHT_GRANT,
                        'stats': '9-2-0',
                    },
                    {
                        'name': ZAK_OTTOW,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': ZAK_OTTOW,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ZAK_OTTOW: 3.25,
                    DWIGHT_GRANT: 1.33,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                    {
                        'name': JIM_MILLER,
                        'stats': '29-13-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:15',
                },
                'odds': {
                    CHARLES_OLIVEIRA: 1.30,
                    JIM_MILLER: 3.35,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ROB_FONT,
                        'stats': '16-4-0',
                    },
                    {
                        'name': SERGIO_PETTIS,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': ROB_FONT,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ROB_FONT: 1.59,
                    SERGIO_PETTIS: 2.40,
                },
            },
            {
                'time': '21:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DAN_HOOKER,
                        'stats': '18-8-0',
                    },
                    {
                        'name': EDSON_BARBOZA,
                        'stats': '20-7-0',
                    },
                ],
                'winner': {
                    'fighter': EDSON_BARBOZA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:19',
                },
                'odds': {
                    EDSON_BARBOZA: 1.91,
                    DAN_HOOKER: 1.83,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                    {
                        'name': AL_IAQUINTA,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': AL_IAQUINTA,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    AL_IAQUINTA: 3.75,
                    KEVIN_LEE: 1.27,
                },
            },
        ]
    },

    {
        'date': '2018-12-29',
        'name': 'UFC 232',
        'location': 'Los Angeles, California',
        'venue': 'The Forum',
        'fights': [
            {
                'time': '18:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MONTEL_JACKSON,
                        'stats': '7-1-0',
                    },
                    {
                        'name': BRIAN_KELLEHER,
                        'stats': '19-10-0',
                    },
                ],
                'winner': {
                    'fighter': MONTEL_JACKSON,
                    'by': 'submission',
                    'round': 1,
                    'time': '1:40',
                },
                'odds': {
                    MONTEL_JACKSON: 1.53,
                    BRIAN_KELLEHER: 2.55,
                },
            },
            {
                'time': '18:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CURTIS_MILLENDER,
                        'stats': '17-4-0',
                    },
                    {
                        'name': SIYAR_BAHADURZADA,
                        'stats': '24-7-1',
                    },
                ],
                'winner': {
                    'fighter': CURTIS_MILLENDER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CURTIS_MILLENDER: 1.63,
                    SIYAR_BAHADURZADA: 2.27,
                },
            },
            {
                'time': '19:12',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': BEVON_LEWIS,
                        'stats': '5-1-0',
                    },
                    {
                        'name': URIAH_HALL,
                        'stats': '19-10-0',
                    },
                ],
                'winner': {
                    'fighter': URIAH_HALL,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:32',
                },
                'odds': {
                    URIAH_HALL: 2.45,
                    BEVON_LEWIS: 1.53,
                },
            },
            {
                'time': '19:39',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_EWELL,
                        'stats': '13-5-0',
                    },
                    {
                        'name': NATHANIEL_WOOD,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': NATHANIEL_WOOD,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:12',
                },
                'odds': {
                    ANDRE_EWELL: 2.00,
                    NATHANIEL_WOOD: 1.74,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_HALL,
                        'stats': '7-1-0',
                    },
                    {
                        'name': BJ_PENN,
                        'stats': '16-13-2',
                    },
                ],
                'winner': {
                    'fighter': RYAN_HALL,
                    'by': 'submission',
                    'round': 1,
                    'time': '2:46',
                },
                'odds': {
                    RYAN_HALL: 1.21,
                    BJ_PENN: 4.10,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PETR_YAN,
                        'stats': '12-1-0',
                    },
                    {
                        'name': DOUGLAS_SILVA_DE_ANDRADE,
                        'stats': '25-3-0',
                    },
                ],
                'winner': {
                    'fighter': PETR_YAN,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '5:00',
                },
                'odds': {
                    PETR_YAN: 1.29,
                    DOUGLAS_SILVA_DE_ANDRADE: 3.65,
                },
            },
            {
                'time': '21:00',
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MEGAN_ANDERSON,
                        'stats': '9-3-0',
                    },
                    {
                        'name': CAT_ZINGANO,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': MEGAN_ANDERSON,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:01',
                },
                'odds': {
                    MEGAN_ANDERSON: 2.06,
                    CAT_ZINGANO: 1.71,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANDREI_ARLOVSKI,
                        'stats': '27-17-0',
                    },
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': WALT_HARRIS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    WALT_HARRIS: 1.47,
                    ANDREI_ARLOVSKI: 2.70,
                },
            },
            {
                'time': '22:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': CHAD_MENDES,
                        'stats': '18-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:14',
                },
                'odds': {
                    ALEXANDER_VOLKANOVSKI: 2.05,
                    CHAD_MENDES: 1.71,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': COREY_ANDERSON,
                        'stats': '13-4-0',
                    },
                    {
                        'name': ILIR_LATIFI,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': COREY_ANDERSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    COREY_ANDERSON: 2.00,
                    ILIR_LATIFI: 1.75,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': CARLOS_CONDIT,
                        'stats': '30-13-0',
                    },
                    {
                        'name': MICHAEL_CHIESA,
                        'stats': '15-4-0',
                    },
                ],
                'winner': {
                    'fighter': MICHAEL_CHIESA,
                    'by': 'submission',
                    'round': 2,
                    'time': '0:56',
                },
                'odds': {
                    MICHAEL_CHIESA: 1.87,
                    CARLOS_CONDIT: 1.83,
                },
            },
            {
                'time': '23:30',
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CRIS_CYBORG,
                        'stats': '20-2-0',
                    },
                    {
                        'name': AMANDA_NUNES,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': AMANDA_NUNES,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:51',
                },
                'odds': {
                    AMANDA_NUNES: 2.60,
                    CRIS_CYBORG: 1.49,
                },
            },
            {
                'time': '23:59',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JON_JONES,
                        'stats': '24-1-0',
                    },
                    {
                        'name': ALEXANDER_GUSTAFSSON,
                        'stats': '18-5-0',
                    },
                ],
                'winner': {
                    'fighter': JON_JONES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:02',
                },
                'odds': {
                    JON_JONES: 1.31,
                    ALEXANDER_GUSTAFSSON: 3.40,
                },
            },
        ]
    }
]
