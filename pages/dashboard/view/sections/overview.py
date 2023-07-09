
import dash_mantine_components as dmc

from dash_extensions import Lottie

from assets import lottie_urls

SHADOW = "xs"
RADIUS = "md"
THEME = "light"

def render_overview():
    return overview_layout

overview_layout = (
    dmc.Grid(
        columns=10,
        align="stretch",
        grow=True,
        gutter="lg",
        justify="center",
        children=[
            dmc.Col(
                span=2,
                children=[
                    dmc.Paper(
                        children=[
                            dmc.Group(
                                direction="column",
                                position='center',
                                style={'margin-top':15, "height": "200px"},
                                spacing='xs',
                                grow=True,
                                children=[
                                    dmc.Header(
                                        height=100,
                                        children=[
                                            Lottie(options=lottie_urls.options, width="40%", height="40%", url=lottie_urls.connections)
                                        ]
                                    ),  # Header
                                    dmc.Title(
                                        children='Connections', 
                                        order=6, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                    dmc.Title(
                                        children="0000",
                                        id="connections-tracker",
                                        order=2, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "dark",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                ]
                            ),  # Group
                        ],
                        shadow=SHADOW,
                        radius=RADIUS,
                        p='sm',
                    ),  # Paper
                ]
            ),  # Col
            dmc.Col(
                span=2,
                children=[
                    dmc.Paper(
                        children=[
                            dmc.Group(
                                direction="column",
                                position='center',
                                style={'margin-top':15, "height": "200px"},
                                spacing='xs',
                                grow=True,
                                children=[
                                    dmc.Header(
                                        height=100,
                                        children=[
                                            Lottie(options=lottie_urls.options, width="32%", height="32%", url=lottie_urls.companies)
                                        ]
                                    ),  # Header
                                    dmc.Title(
                                        children='companies', 
                                        order=6, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                    dmc.Title(
                                        children="0000",
                                        id="companies-tracker",
                                        order=2, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "dark",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                ]
                            ),  # Group
                        ],
                        shadow=SHADOW,
                        radius=RADIUS,
                        p='sm',
                    )
                ]
            ),
            dmc.Col(
                span=2,
                children=[
                    dmc.Paper(
                        children=[
                            dmc.Group(
                                direction="column",
                                position='center',
                                style={'margin-top':15, "height": "200px"},
                                spacing='xs',
                                grow=True,
                                children=[
                                    dmc.Header(
                                        height=100,
                                        children=[
                                            Lottie(options=lottie_urls.options, width="32%", height="32%", url=lottie_urls.invites_received)
                                        ]
                                    ),  # Header
                                    dmc.Title(
                                        children='invites received', 
                                        order=6, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                    dmc.Title(
                                        children="0000",
                                        id="invites-received-tracker",
                                        order=2, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "dark",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                ]
                            ),  # Group
                        ],
                        shadow=SHADOW,
                        radius=RADIUS,
                        p='sm',
                    )
                ]
            ),
            dmc.Col(
                span=2,
                children=[
                    dmc.Paper(
                        children=[
                            dmc.Group(
                                direction="column",
                                position='center',
                                style={'margin-top':15, "height": "200px"},
                                spacing='xs',
                                grow=True,
                                children=[
                                    dmc.Header(
                                        height=100,
                                        children=[
                                            Lottie(options=lottie_urls.options, width="40%", height="40%", url=lottie_urls.invites_sent)
                                        ]
                                    ),  # Header
                                    dmc.Title(
                                        children='invites sent', 
                                        order=6, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                    dmc.Title(
                                        children="0000",
                                        id="invites-sent-tracker",
                                        order=2, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "dark",
                                            'letter-spacing':'1px',
                                        }
                                    ),  # Title
                                ]
                            ),  # Group
                        ],
                        shadow=SHADOW,
                        radius=RADIUS,
                        p='sm',
                    )
                ]
            ),
            # dmc.Col(
            #     span=2,
            #     children=[
            #         dmc.Paper(
            #             children=[
            #                 dmc.Group(
            #                     direction="column",
            #                     position='center',
            #                     style={'margin-top':15, "height": "200px"},
            #                     spacing='xs',
            #                     grow=True,
            #                     children=[
            #                         dmc.Header(
            #                             height=100,
            #                             children=[
            #                                 Lottie(options=lottie_urls.options, width="32%", height="32%", url=lottie_urls.reactions)
            #                             ]
            #                         ),  # Header
            #                         dmc.Title(
            #                             children='reactions', 
            #                             order=6, 
            #                             style={
            #                                 'font-family':'IntegralCF-Regular',
            #                                 'text-align':'center', 
            #                                 "color": "grey",
            #                                 'letter-spacing':'1px',
            #                             }
            #                         ),  # Title
            #                         dmc.Title(
            #                             children="0000",
            #                             id="reactions-tracker",
            #                             order=2, 
            #                             style={
            #                                 'font-family':'IntegralCF-Regular',
            #                                 'text-align':'center', 
            #                                 "color": "dark",
            #                                 'letter-spacing':'1px',
            #                             }
            #                         ),  # Title
            #                     ]
            #                 ),  # Group
            #             ],
            #             shadow=SHADOW,
            #             radius=RADIUS,
            #             p='sm',
            #         )
            #     ]
            # )
        ]
    )
)