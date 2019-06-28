from fighters import *

DATA = [
    {
        'date': '2019-05-04',
        'name': 'UFC Fight Night',
        'location': 'Ottawa, Ontario',
        'venue': 'Canadian Tire Centre',
        'fights': [
            {
                'time': '18:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': COLE_SMITH,
                        'stats': '6-0-0',
                    },
                    {
                        'name': MITCH_GAGNON,
                        'stats': '12-4-0',
                    },
                ],
                'winner': {
                    'fighter': COLE_SMITH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    COLE_SMITH: 115,
                    MITCH_GAGNON: -129,
                },
            },
            {
                'time': '18:05',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NORDINE_TALEB,
                        'stats': '14-6-0',
                    },
                    {
                        'name': KYLE_PREPOLEC,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': NORDINE_TALEB,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    NORDINE_TALEB: -519,
                    KYLE_PREPOLEC: 400,
                },
            },
            {
                'time': '18:40',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': JUAN_ADAMS,
                        'stats': '5-0-0',
                    },
                    {
                        'name': ARJAN_BHULLAR,
                        'stats': '8-1-0',
                    },
                ],
                'winner': {
                    'fighter': ARJAN_BHULLAR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ARJAN_BHULLAR: 120,
                    JUAN_ADAMS: -135,
                },
            },
            {
                'time': '19:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': MATT_SAYLES,
                        'stats': '6-2-0',
                    },
                    {
                        'name': KYLE_NELSON,
                        'stats': '12-2-0',
                    },
                ],
                'winner': {
                    'fighter': MATT_SAYLES,
                    'by': 'submission',
                    'round': 3,
                    'time': '3:16',
                },
                'odds': {
                    MATT_SAYLES: -187,
                    KYLE_NELSON: 165,
                },
            },
            {
                'time': '20:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': VINCE_MORALES,
                        'stats': '0-0-0',
                    },
                    {
                        'name': AIEMANN_ZAHABI,
                        'stats': '7-1-0',
                    },
                ],
                'winner': {
                    'fighter': VINCE_MORALES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    VINCE_MORALES: 160,
                    AIEMANN_ZAHABI: -181,
                },
            },
            {
                'time': '21:05',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANDREW_SANCHEZ,
                        'stats': '11-4-0',
                    },
                    {
                        'name': MARC_ANDRE_BARRIAULT,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter':ANDREW_SANCHEZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANDREW_SANCHEZ: -153,
                    MARC_ANDRE_BARRIAULT: 136,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': SERGEY_SPIVAK,
                        'stats': '9-0-0',
                    },
                    {
                        'name': WALT_HARRIS,
                        'stats': '11-7-0',
                    },
                ],
                'winner': {
                    'fighter': WALT_HARRIS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:50',
                },
                'odds': {
                    WALT_HARRIS: -170,
                    SERGEY_SPIVAK: 150,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SHANE_BURGOS,
                        'stats': '11-1-0',
                    },
                    {
                        'name': CUB_SWANSON,
                        'stats': '25-10-0',
                    },
                ],
                'winner': {
                    'fighter': SHANE_BURGOS,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SHANE_BURGOS: -181,
                    CUB_SWANSON: 160,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': MERAB_DVALISHVILI,
                        'stats': '8-4-0',
                    },
                    {
                        'name': BRAD_KATONA,
                        'stats': '9-0-0',
                    },
                ],
                'winner': {
                    'fighter': MERAB_DVALISHVILI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MERAB_DVALISHVILI: -152,
                    BRAD_KATONA: 135,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
                    },
                    {
                        'name': AL_IAQUINTA,
                        'stats': '14-4-1',
                    },
                ],
                'winner': {
                    'fighter': DONALD_CERRONE,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'odds': {
                    DONALD_CERRONE: 115,
                    AL_IAQUINTA: -129,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ELIAS_THEODOROU,
                        'stats': '17-2-0',
                    },
                    {
                        'name': DEREK_BRUNSON,
                        'stats': '18-7-0',
                    },
                ],
                'winner': {
                    'fighter': DEREK_BRUNSON,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DEREK_BRUNSON: 102,
                    ELIAS_THEODOROU: -115,
                },
            },
        ]
    },

    {
        'date': '2019-05-11',
        'name': 'UFC 237',
        'location': 'Rio de Janeiro, Brazil',
        'venue': 'Jeunesse Arena',
        'fights': [
            {
                'time': '19:00',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RAONI_BARCELOS,
                        'stats': '13-1-0',
                    },
                    {
                        'name': CARLOS_HUACHIN_QUIROZ,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': RAONI_BARCELOS,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:49',
                },
                'odds': {
                    CARLOS_HUACHIN_QUIROZ: 721,
                    RAONI_BARCELOS: -1099,
                },
            },
            {
                'time': '19:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': LUANA_CAROLINA,
                        'stats': '5-1-0',
                    },
                    {
                        'name': PRISCILA_CACHOEIRA,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': LUANA_CAROLINA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    PRISCILA_CACHOEIRA: 155,
                    LUANA_CAROLINA: -176,
                },
            },
            {
                'time': '20:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CLAY_GUIDA,
                        'stats': '34-15-0',
                    },
                    {
                        'name': BJ_PENN,
                        'stats': '16-13-2'
                    },
                ],
                'winner': {
                    'fighter': CLAY_GUIDA,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CLAY_GUIDA: -697,
                    BJ_PENN: 510,
                },
            },
            {
                'time': '20:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SERGIO_MORAES,
                        'stats': '14-5-1',
                    },
                    {
                        'name': WARLLEY_ALVES,
                        'stats': '13-3-0',
                    },
                ],
                'winner': {
                    'fighter': WARLLEY_ALVES,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:13',
                },
                'odds': {
                    SERGIO_MORAES: 118,
                    WARLLEY_ALVES: -133,
                },
            },
            {
                'time': '21:00',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': KURT_HOLOBAUGH,
                        'stats': '17-6-0',
                    },
                    {
                        'name': THIAGO_MOISES,
                        'stats': '11-3-0',
                    }
                ],
                'winner': {
                    'fighter': THIAGO_MOISES,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    KURT_HOLOBAUGH: 115,
                    THIAGO_MOISES: -129,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': RYAN_SPANN,
                        'stats': '15-5-0',
                    },
                    {
                        'name': ANTONIO_ROGERIO_NOGUEIRA,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': RYAN_SPANN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:07',
                },
                'odds': {
                    RYAN_SPANN: -135,
                    ANTONIO_ROGERIO_NOGUEIRA: 120,
                },
            },
            {
                'time': '22:00',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': BETHE_CORREIA,
                        'stats': '10-3-1',
                    },
                    {
                        'name': IRENE_ALDANA,
                        'stats': '9-4-0',
                    },
                ],
                'winner': {
                    'fighter': IRENE_ALDANA,
                    'by': 'submission',
                    'round': 3,
                    'time': '3:24',
                },
                'odds': {
                    BETHE_CORREIA: 310,
                    IRENE_ALDANA: -387,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': LAUREANO_STAROPOLI,
                        'stats': '8-1-0',
                    },
                    {
                        'name': THIAGO_ALVES,
                        'stats': '28-13-0',
                    },
                ],
                'winner': {
                    'fighter': LAUREANO_STAROPOLI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LAUREANO_STAROPOLI: 110,
                    THIAGO_ALVES: -124,
                },
            },
            {
                'time': '23:00',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': ALEXANDER_VOLKANOVSKI,
                        'stats': '19-1-0',
                    },
                    {
                        'name': JOSE_ALDO,
                        'stats': '28-4-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXANDER_VOLKANOVSKI,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEXANDER_VOLKANOVSKI: 114,
                    JOSE_ALDO: -128,
                },
            },
            {
                'time': '23:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': ANDERSON_SILVA,
                        'stats': '34-9-0',
                    },
                    {
                        'name': JARED_CANNONIER,
                        'stats': '11-4-0',
                    },
                ],
                'winner': {
                    'fighter': JARED_CANNONIER,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:47',
                },
                'odds': {
                    JARED_CANNONIER: -124,
                    ANDERSON_SILVA: 110,
                },
            },
            {
                'time': '23:59',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ROSE_NAMAJUNAS,
                        'stats': '9-3-0',
                    },
                    {
                        'name': JESSICA_ANDRADE,
                        'stats': '19-6-0',
                    },
                ],
                'winner': {
                    'fighter': JESSICA_ANDRADE,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:58',
                },
                'odds': {
                    ROSE_NAMAJUNAS: 134,
                    JESSICA_ANDRADE: -151,
                },
            },
        ]
    },

    {
        'date': '2019-05-18',
        'name': 'UFC Fight Night',
        'location': 'Rochester, Michigan',
        'venue': 'Blue Cross Arena',
        'fights': [
            {
                'time': '17:35',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': TREVIN_GILES,
                        'stats': '11-0-0',
                    },
                    {
                        'name': ZAK_CUMMINGS,
                        'stats': '22-6-0',
                    },
                ],
                'winner': {
                    'fighter': ZAK_CUMMINGS,
                    'by': 'submission',
                    'round': 3,
                    'time': '4:01',
                },
                'odds': {
                    TREVIN_GILES: -193,
                    ZAK_CUMMINGS: 170,
                },
            },
            {
                'time': '18:05',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ED_HERMAN,
                        'stats': '24-14-0',
                    },
                    {
                        'name': PATRICK_CUMMINS,
                        'stats': '10-6-0',
                    },
                ],
                'winner': {
                    'fighter': ED_HERMAN,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:39',
                },
                'odds': {
                    ED_HERMAN: 230,
                    PATRICK_CUMMINS: -265,
                },
            },
            {
                'time': '18:05',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': JULIAN_EROSA,
                        'stats': '22-8-0',
                    },
                    {
                        'name': JULIO_ACRE,
                        'stats': '15-3-0',
                    },
                ],
                'winner': {
                    'fighter': JULIO_ACRE,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:49',
                },
                'odds': {
                    JULIAN_EROSA: 560,
                    JULIO_ACRE: -822,
                },
            },
            {
                'time': '18:24',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': GRANT_DAWSON,
                        'stats': '13-1-0',
                    },
                    {
                        'name': MICHAEL_TRIZANO,
                        'stats': '9-0-0',
                    },
                ],
                'winner': {
                    'fighter': GRANT_DAWSON,
                    'by': 'submission',
                    'round': 2,
                    'time': '2:27',
                },
                'odds': {
                    GRANT_DAWSON: -158,
                    MICHAEL_TRIZANO: 140,
                },
            },
            {
                'time': '18:45',
                'gender': 'mens',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MICHEL_PEREIRA,
                        'stats': '22-9-0',
                    },
                    {
                        'name': DANNY_ROBERTS,
                        'stats': '16-4-0',
                    },
                ],
                'winner': {
                    'fighter': MICHEL_PEREIRA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '1:47',
                },
                'odds': {
                    MICHEL_PEREIRA: 200,
                    DANNY_ROBERTS: -229,
                },
            },
            {
                'time': '19:12',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHARLES_JOURDAIN,
                        'stats': '0-0-0',
                    },
                    {
                        'name': DESMOND_GREEN,
                        'stats': '22-8-0',
                    },
                ],
                'winner': {
                    'fighter': DESMOND_GREEN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CHARLES_JOURDAIN: 550,
                    DESMOND_GREEN: -803,
                },
            },
            {
                'time': '19:45',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': SIJARA_EUBANKS,
                        'stats': '5-2-0',
                    },
                    {
                        'name': ASPEN_LADD,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': ASPEN_LADD,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SIJARA_EUBANKS: 220,
                    ASPEN_LADD: -253,
                },
            },
            {
                'time': '20:45',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': NIK_LENTZ,
                        'stats': '30-9-2',
                    },
                    {
                        'name': CHARLES_OLIVEIRA,
                        'stats': '26-8-0',
                    },
                ],
                'winner': {
                    'fighter': CHARLES_OLIVEIRA,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:11',
                },
                'odds': {
                    NIK_LENTZ: 320,
                    CHARLES_OLIVEIRA: -401,
                },
            },
            {
                'time': '21:35',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': AUSTIN_HUBBARD,
                        'stats': '10-2-0',
                    },
                    {
                        'name': DAVI_RAMOS,
                        'stats': '9-2-0',
                    },
                ],
                'winner': {
                    'fighter': DAVI_RAMOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    AUSTIN_HUBBARD: 390,
                    DAVI_RAMOS: -504,
                },
            },
            {
                'time': '21:35',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': DERRICK_KRANTZ,
                        'stats': '0-0-0',
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
                'odds': {
                    DERRICK_KRANTZ: 700,
                    VICENTE_LUQUE: -1120,
                },
            },
            {
                'time': '21:59',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': IAN_HEINISCH,
                        'stats': '12-1-0',
                    },
                    {
                        'name': ANTONIO_CARLOS_JUNIOR,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': IAN_HEINISCH,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    IAN_HEINISCH: 145,
                    ANTONIO_CARLOS_JUNIOR: -164,
                },
            },
            {
                'time': '22:15',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_LEE,
                        'stats': '17-4-0',
                    },
                    {
                        'name': RAFAEL_DOS_ANJOS,
                        'stats': '28-11-0',
                    },
                ],
                'winner': {
                    'fighter': RAFAEL_DOS_ANJOS,
                    'by': 'submission',
                    'round': 4,
                    'time': '3;47',
                },
                'odds': {
                    KEVIN_LEE: -144,
                    RAFAEL_DOS_ANJOS: 128,
                },
            },
            {
                'time': '23:05',
                'weight_class': WOMANS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': FELICIA_SPENCER,
                        'stats': '6-0-0',
                    },
                    {
                        'name': MEGAN_ANDERSON,
                        'stats': '9-3-0',
                    },
                ],
                'winner': {
                    'fighter': FELICIA_SPENCER,
                    'by': 'submission',
                    'round': 1,
                    'time': '3:24',
                },
                'odds': {
                    FELICIA_SPENCER: 180,
                    MEGAN_ANDERSON: -205,
                },
            },
        ]
    },

    {
        'date': '2019-06-01',
        'name': 'UFC Fight Night',
        'location': 'Stockholm, Sweden',
        'venue': 'Ericsson Globe',
        'fights': [
            {
                'time': '10:10',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DANILO_BELLUARDO,
                        'stats': '12-3-0',
                    },
                    {
                        'name': JOEL_ALVAREZ,
                        'stats': '15-2-0',
                    },
                ],
                'winner': {
                    'fighter': JOEL_ALVAREZ,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '2:22',
                },
                'odds': {
                    DANILO_BELLUARDO: -103,
                    JOEL_ALVAREZ: -109,
                },
            },
            {
                'time': '10:35',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': DEVIN_CLARK,
                        'stats': '9-3-0',
                    },
                    {
                        'name': DARKO_STOSIC,
                        'surname': 'STOSIC',
                        'stats': '13-1-0',
                    },
                ],
                'winner': {
                    'fighter': DEVIN_CLARK,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DEVIN_CLARK: -115,
                    DARKO_STOSIC: 102,
                },
            },
            {
                'time': '11:05',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': EDUARDA_SANTANA,
                        'stats': '0-0-0',
                    },
                    {
                        'name': BEA_MALECKI,
                        'stats': '2-0-0',
                    },
                ],
                'winner': {
                    'fighter': BEA_MALECKI,
                    'by': 'submission',
                    'round': 2,
                    'time': '1:59',
                },
                'odds': {
                    EDUARDA_SANTANA: 108,
                    BEA_MALECKI: -121,
                },
            },
            {
                'time': '11:35',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': FRANK_CAMACHO,
                        'stats': '21-7-0',
                    },
                    {
                        'name': NICK_HEIN,
                        'stats': '14-4-0',
                    },
                ],
                'winner': {
                    'fighter': FRANK_CAMACHO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:56',
                },
                'odds': {
                    FRANK_CAMACHO: -138,
                    NICK_HEIN: 123,
                },
            },
            {
                'time': '12:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': LEONARDO_SANTOS,
                        'stats': '16-4-1',
                    },
                    {
                        'name': STEVIE_RAY,
                        'stats': '22-7-0',
                    },
                ],
                'winner': {
                    'fighter': LEONARDO_SANTOS,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '2:17',
                },
                'odds': {
                    LEONARDO_SANTOS: -150,
                    STEVIE_RAY: 133,
                },
            },
            {
                'time': '12:35',
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': LINA_LANSBERG,
                        'stats': '8-4-0',
                    },
                    {
                        'name': TONYA_EVINGER,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': LINA_LANSBERG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    LINA_LANSBERG: 323,
                    TONYA_EVINGER: -382,
                },
            },
            {
                'time': '13:05',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': SERGEY_KHANDOZHKO,
                        'stats': '25-5-0',
                    },
                    {
                        'name': ROSTEM_AKMAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': SERGEY_KHANDOZHKO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SERGEY_KHANDOZHKO: -155,
                    ROSTEM_AKMAN: 137,
                },
            },
            {
                'time': '13:35',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': SUNG_BIN_JO,
                        'stats': '0-0-0',
                    },
                    {
                        'name': DANIEL_TEYMUR,
                        'stats': '6-3-0',
                    },
                ],
                'winner': {
                    'fighter': DANIEL_TEYMUR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SUNG_BIN_JO: -118,
                    DANIEL_TEYMUR: 105,
                },
            },
            {
                'time': '14:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CHRISTOS_GIAGOS,
                        'stats': '16-7-0',
                    },
                    {
                        'name': DAMIR_HADZOVIC,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': CHRISTOS_GIAGOS,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    CHRISTOS_GIAGOS: 133,
                    DAMIR_HADZOVIC: -150,
                },
            },
            {
                'time': '14:35',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': CHRIS_FISHGOLD,
                        'stats': '18-2-1',
                    },
                    {
                        'name': MAKWAN_AMIRKHANI,
                        'stats': '14-3-0',
                    },
                ],
                'winner': {
                    'fighter': MAKWAN_AMIRKHANI,
                    'by': 'submission',
                    'round': 2,
                    'time': '4:25',
                },
                'odds': {
                    CHRIS_FISHGOLD: 112,
                    MAKWAN_AMIRKHANI: -126,
                },
            },
            {
                'time': '15:05',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALEKSANDAR_RAKIC,
                        'surname': 'RAKIC',
                        'stats': '1-1-0',
                    },
                    {
                        'name': JIMI_MANUWA,
                        'stats': '17-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEKSANDAR_RAKIC,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:42',
                },
                'odds': {
                    ALEKSANDAR_RAKIC: -270,
                    JIMI_MANUWA: 234,
                },
            },
            {
                'time': '15:35',
                'weight_class': MENS_LIGHT_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ANTHONY_SMITH,
                        'stats': '31-14-0',
                    },
                    {
                        'name': ALEXANDER_GUSTAFSSON,
                        'stats': '18-5-0',
                    },
                ],
                'winner': {
                    'fighter': ANTHONY_SMITH,
                    'by': 'submission',
                    'round': 4,
                    'time': '2:38',
                },
                'odds': {
                    ANTHONY_SMITH: 277,
                    ALEXANDER_GUSTAFSSON: -324,
                },
            },
        ],
    },

    {
        'date': '2019-06-08',
        'name': 'UFC 238',
        'location': 'Chicago, Illinois',
        'venue': 'United Center',
        'fights': [
            {
                'time': '18:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JOANNE_CALDERWOOD,
                        'stats': '13-3-0',
                    },
                    {
                        'name': KATLYN_CHOOKAGIAN,
                        'stats': '11-2-0',
                    }
                ],
                'winner': {
                    'fighter': KATLYN_CHOOKAGIAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    JOANNE_CALDERWOOD: -102,
                    KATLYN_CHOOKAGIAN: -110,
                },
            },
            {
                'time': '18:48',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': GRIGORY_POPOV,
                        'stats': '0-0-0',
                    },
                    {
                        'name': EDDIE_WINELAND,
                        'stats': '23-13-1',
                    },
                ],
                'winner': {
                    'fighter': EDDIE_WINELAND,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '4:47',
                },
                'odds': {
                    GRIGORY_POPOV: 142,
                    EDDIE_WINELAND: -160,
                },
            },
            {
                'time': '19:15',
                'class_weight': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DARREN_STEWART,
                        'stats': '9-4-0',
                    },
                    {
                        'name': BEVON_LEWIS,
                        'stats': '5-1-0',
                    },
                ],
                'winner': {
                    'fighter': DARREN_STEWART,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DARREN_STEWART: 158,
                    BEVON_LEWIS: -179,
                },
            },
            {
                'time': '19:35',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ANGELA_HILL,
                        'stats': '8-6-0',
                    },
                    {
                        'name': XIAONAN_YAN,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': XIAONAN_YAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANGELA_HILL: 205,
                    XIAONAN_YAN: -235,
                },
            },
            {
                'time': '20:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': CALVIN_KATTAR,
                        'stats': '19-3-0',
                    },
                    {
                        'name': RICARDO_LAMAS,
                        'stats': '19-7-0',
                    },
                ],
                'winner': {
                    'fighter': CALVIN_KATTAR,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '4:06',
                },
                'odds': {
                    CALVIN_KATTAR: -164,
                    RICARDO_LAMAS: 145,
                },
            },
            {
                'time': '20:30',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ALEXA_GRASSO,
                        'stats': '10-2-0',
                    },
                    {
                        'name': KAROLINA_KOWALKIEWICZ,
                        'stats': '13-4-0',
                    },
                ],
                'winner': {
                    'fighter': ALEXA_GRASSO,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALEXA_GRASSO: -121,
                    KAROLINA_KOWALKIEWICZ: 108,
                },
            },
            {
                'time': '21:12',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PEDRO_MUNHOZ,
                        'stats': '18-3-0',
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
                'odds': {
                    PEDRO_MUNHOZ: 145,
                    ALJAMAIN_STERLING: -164,
                },
            },
            {
                'time': '21:30',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': NINA_ANSAROFF,
                        'stats': '10-5-0',
                    },
                    {
                        'name': TATIANA_SUAREZ,
                        'stats': '7-0-0',
                    },
                ],
                'winner': {
                    'fighter': TATIANA_SUAREZ,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    NINA_ANSAROFF: 525,
                    TATIANA_SUAREZ: -755,
                },
            },
            {
                'time': '22:05',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': BLAGOY_IVANOV,
                        'stats': '17-2-0',
                    },
                    {
                        'name': TAI_TUIVASA,
                        'stats': '10-1-0',
                    },
                ],
                'winner': {
                    'fighter': BLAGOY_IVANOV,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    BLAGOY_IVANOV: 140,
                    TAI_TUIVASA: -158,
                },
            },
            {
                'time': '22:30',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': PETR_YAN,
                        'stats': '12-1-0',
                    },
                    {
                        'name': JIMMIE_RIVERA,
                        'stats': '22-3-0',
                    },
                ],
                'winner': {
                    'fighter': PETR_YAN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    PETR_YAN: -334,
                    JIMMIE_RIVERA: 285,
                },
            },
            {
                'time': '23:05',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': DONALD_CERRONE,
                        'stats': '35-11-0',
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
                'odds': {
                    DONALD_CERRONE: 193,
                    TONY_FERGUSON: -220,
                },
            },
            {
                'time': '23:30',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': JESSICA_EYE,
                        'stats': '14-6-0',
                    },
                    {
                        'name': VALENTINA_SHEVCHENKO,
                        'stats': '16-3-0',
                    },
                ],
                'winner': {
                    'fighter': VALENTINA_SHEVCHENKO,
                    'by': 'ko/tko',
                    'round': 2,
                    'time': '0:26',
                },
                'odds': {
                    JESSICA_EYE: 775,
                    VALENTINA_SHEVCHENKO: -1305,
                },
            },
            {
                'time': '23:57',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': HENRY_CEJUDO,
                        'stats': '14-2-0',
                    },
                    {
                        'name': MARLON_MORAES,
                        'stats': '22-5-1',
                    },
                ],
                'winner': {
                    'fighter': HENRY_CEJUDO,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '4:51',
                },
                'odds': {
                    HENRY_CEJUDO: 137,
                    MARLON_MORAES: -155,
                },
            },
        ]
    },

    {
        'date': '2019-06-22',
        'name': 'UFC Fight Night',
        'location': 'Greenville, South Carolina',
        'venue': 'Bon Secours Wellness Arena',
        'fights': [
            {
                'time': '16:05',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': DERON_WINN,
                        'stats': '7-1-0',
                    },
                    {
                        'name': ERIC_SPICELY,
                        'stats': '10-5-0',
                    },
                ],
                'winner': {
                    'fighter': DERON_WINN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ERIC_SPICELY: 290,
                    DERON_WINN: -340,
                }
            },
            {
                'time': '16:35',
                'weight_class': MENS_LIGHTWEIGHT,
                'fighters': [
                    {
                        'name': MATT_WIMAN,
                        'stats': '16-7-0',
                    },
                    {
                        'name': LUIS_PENA,
                        'stats': '6-1-0',
                    },
                ],
                'winner': {
                    'fighter': LUIS_PENA,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '1:14',
                },
                'odds': {
                    MATT_WIMAN: 285,
                    LUIS_PENA: -352,
                }
            },
            {
                'time': '17:35',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': DAN_IGE,
                        'stats': '11-2-0',
                    },
                    {
                        'name': KEVIN_AGUILAR,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': DAN_IGE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    DAN_IGE: 121,
                    KEVIN_AGUILAR: -136,
                }
            },
            {
                'time': '18:35',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ARIANE_LIPSKI,
                        'stats': '11-4-0',
                    },
                    {
                        'name': MOLLY_MCCANN,
                        'stats': '8-2-0',
                    },
                ],
                'winner': {
                    'fighter': MOLLY_MCCANN,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MOLLY_MCCANN: 205,
                    ARIANE_LIPSKI: -235,
                },
            },
            {
                'time': '20:00',
                'weight_class': WOMANS_STRAWWEIGHT,
                'fighters': [
                    {
                        'name': ASHLEY_YODER,
                        'stats': '6-4-0',
                    },
                    {
                        'name': SYURI_KONDO,
                        'stats': '6-2-0',
                    },
                ],
                'winner': {
                    'fighter': ASHLEY_YODER,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    SYURI_KONDO: 120,
                    ASHLEY_YODER: -135,
                }
            },
            {
                'time': '20:22',
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': ANDRE_EWELL,
                        'stats': '13-5-0',
                    },
                    {
                        'name': ANDERSON_BERLINGERI_DOS_SANTOS,
                        'stats': '0-0-0',
                    },
                ],
                'winner': {
                    'fighter': ANDRE_EWELL,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ANDERSON_BERLINGERI_DOS_SANTOS: 120,
                    ANDRE_EWELL: -135,
                }
            },
            {
                'time': '20:30',
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': KEVIN_HOLLAND,
                        'stats': '15-4-0',
                    },
                    {
                        'name': ALESSIO_DI_CHRICO,
                        'stats': '12-2-0',
                    },
                ],
                'winner': {
                    'fighter': KEVIN_HOLLAND,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    ALESSIO_DI_CHRICO: 186,
                    KEVIN_HOLLAND: -212,
                },
            },
            {
                'time': '20:45',
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': BRYAN_BARBERENA,
                        'stats': '14-6-0',
                    },
                    {
                        'name': RANDY_BROWN,
                        'stats': '10-3-0',
                    },
                ],
                'winner': {
                    'fighter': RANDY_BROWN,
                    'by': 'ko/tko',
                    'round': 3,
                    'time': '2:54',
                },
                'odds': {
                    RANDY_BROWN: 198,
                    BRYAN_BARBERENA: -237,
                },
            },
            {
                'time': '21:10',
                'weight_class': MENS_FEATHERWEIGHT,
                'fighters': [
                    {
                        'name': RENATO_MOICANO,
                        'stats': '13-2-1',
                    },
                    {
                        'name': CHAN_SUNG_JUNG,
                        'stats': '14-5-0',
                    },
                ],
                'winner': {
                    'fighter': CHAN_SUNG_JUNG,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:58'
                },
                'odds': {
                    CHAN_SUNG_JUNG: 187,
                    RENATO_MOICANO: -213,
                },
            },
            {
                'time': '21:30',
                'weight_class': MENS_HEAVYWEIGHT,
                'fighters': [
                    {
                        'name': ALLEN_CROWDER,
                        'stats': '10-3-0',
                    },
                    {
                        'name': JAIRZINHO_ROZENSTRUIK,
                        'stats': '6-0-0',
                    },
                ],
                'winner': {
                    'fighter': JAIRZINHO_ROZENSTRUIK,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '0:09',
                },
                'odds': {
                    JAIRZINHO_ROZENSTRUIK: -223,
                    ALLEN_CROWDER: 195,
                },
            },
            {
                'time': '22:00',
                'weight_class': WOMANS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': ANDREA_LEE,
                        'stats': '10-2-0',
                    },
                    {
                        'name': MONTANA_DE_LA_ROSA,
                        'stats': '10-4-0',
                    },
                ],
                'winner': {
                    'fighter': ANDREA_LEE,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'odds': {
                    MONTANA_DE_LA_ROSA: 150,
                    ANDREA_LEE: -170,
                },
            },
        ]
    }
]
