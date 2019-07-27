from fighters import *

DATA_2016 = [
    {
        'date': '2016-12-30',
        'name': 'UFC 207: Nunes vs Rousey',
        'location': 'Las Vegas, Nevada',
        'venue': 'T-Mobile Arena',
        'fights': [
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': ALEX_OLIVEIRA,
                        'stats': '19-6-1',
                    },
                    {
                        'name': TIM_MEANS,
                        'stats': '28-11-1',
                    },
                ],
                'winner': {
                    'fighter': None,
                    'by': 'cnc',
                    'round': 1,
                    'time': '3:33',
                },
                'time': '19:35',
                'odds': {
                    TIM_MEANS: 2.10,
                    ALEX_OLIVEIRA: 1.68
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
                        'name': BRANDON_THATCH,
                        'stats': '11-5-0',
                    },
                ],
                'winner': {
                    'fighter': NIKO_PRICE,
                    'by': 'submission',
                    'round': 1,
                    'time': '4:30',
                },
                'time': '20:05',
                'odds': {
                    NIKO_PRICE: 2.30,
                    BRANDON_THATCH: 1.63
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': MIKE_PYLE,
                        'stats': '27-14-1',
                    },
                    {
                        'name': ALEX_GARCIA,
                        'stats': '15-5-0',
                    },
                ],
                'winner': {
                    'fighter': ALEX_GARCIA,
                    'by': 'ko/tko',
                    'round': 1,
                    'time': '3:34',
                },
                'time': '20:30',
                'odds': {
                    ALEX_GARCIA: 1.48,
                    MIKE_PYLE: 2.65
                },
            },
            {
                'weight_class': MENS_MIDDLEWEIGHT,
                'fighters': [
                    {
                        'name': MARVIN_VETTORI,
                        'stats': '12-4-1',
                    },
                    {
                        'name': ANTONIO_CARLOS_JUNIOR,
                        'stats': '11-2-0',
                    },
                ],
                'winner': {
                    'fighter': ANTONIO_CARLOS_JUNIOR,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:05',
                'odds': {
                    ANTONIO_CARLOS_JUNIOR: 1.83,
                    MARVIN_VETTORI: 1.91
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': NEIL_MAGNY,
                        'stats': '21-8-0',
                    },
                    {
                        'name': JOHNY_HENDRICKS,
                        'stats': '18-8-0',
                    },
                ],
                'winner': {
                    'fighter': NEIL_MAGNY,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '21:35',
                'odds': {
                    NEIL_MAGNY: 1.49,
                    JOHNY_HENDRICKS: 2.60
                },
            },
            {
                'weight_class': MENS_FLYWEIGHT,
                'fighters': [
                    {
                        'name': RAY_BORG,
                        'stats': '11-4-0',
                    },
                    {
                        'name': LOUIS_SMOLKA,
                        'stats': '15-6-0',
                    },
                ],
                'winner': {
                    'fighter': RAY_BORG,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:15',
                'odds': {
                    RAY_BORG: 1.71,
                    LOUIS_SMOLKA: 1.95
                },
            },
            {
                'weight_class': MENS_WELTERWEIGHT,
                'fighters': [
                    {
                        'name': TAREC_SAFFIEDINE,
                        'stats': '16-7-0',
                    },
                    {
                        'name': DONG_HYUN_KIM,
                        'stats': '22-4-1',
                    },
                ],
                'winner': {
                    'fighter': DONG_HYUN_KIM,
                    'by': 's.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '22:30',
                'odds': {
                    DONG_HYUN_KIM: 1.67,
                    TAREC_SAFFIEDINE: 2.15
                },
            },
            {
                'weight_class': MENS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': JOHN_LINEKER,
                        'stats': '31-8-0',
                    },
                    {
                        'name': TJ_DILLASHAW,
                        'stats': '17-4-0',
                    },
                ],
                'winner': {
                    'fighter': TJ_DILLASHAW,
                    'by': 'u.dec',
                    'round': 3,
                    'time': '5:00',
                },
                'time': '23:15',
                'odds': {
                    TJ_DILLASHAW: 1.44,
                    JOHN_LINEKER: 2.75
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
                        'name': DOMINICK_CRUZ,
                        'stats': '22-2-0',
                    },
                ],
                'winner': {
                    'fighter': CODY_GARBRANDT,
                    'by': 'u.dec',
                    'round': 5,
                    'time': '5:00',
                },
                'time': '23:30',
                'odds': {
                    CODY_GARBRANDT: 2.85,
                    DOMINICK_CRUZ: 1.43
                },
            },
            {
                'weight_class': WOMANS_BANTAMWEIGHT,
                'fighters': [
                    {
                        'name': RONDA_ROUSEY,
                        'stats': '12-2-0',
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
                    'time': '0:48',
                },
                'time': '23:59',
                'odds': {
                    AMANDA_NUNES: 2.50,
                    RONDA_ROUSEY: 1.53
                }
            }
        ]
    }
]
