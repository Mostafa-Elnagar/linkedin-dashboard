
import dash_mantine_components as dmc
import pandas as pd

SHADOW = "xs"
RADIUS = "md"
THEME = "light"

def render_header():
    return header_layout

linked_in_logo = dmc.Col(
    span=1,
    children=[
        dmc.Center(
            children=[
                dmc.Paper(
                    children=[
                        dmc.Image(
                            src="assets/logo.png",
                            fit="cover",
                            radius=RADIUS,
                        ),  # Image
                    ],
                    shadow=SHADOW,
                    radius=RADIUS,
                    withBorder=True,
                    ml=2,
                    p=0
                ),  # Paper
            ]
        ), # Center
    ]
)

header_layout = (
    dmc.Grid(
        grow=False,
        columns=10,
        gutter="lg",
        justify="center",
        children=[
            dmc.Col(
                span=2,
                children=[
                    dmc.Grid(
                        grow=True,
                        columns=1,
                        children=[
                            dmc.Col(
                                children=[
                                    dmc.Grid(
                                        columns=2,
                                        gutter="xs",
                                        align="center",
                                        grow=False,
                                        children=[
                                            dmc.Col(
                                                span=1,
                                                children=[
                                                    dmc.Center(
                                                        children=[
                                                            dmc.Paper(
                                                                children=[
                                                                    dmc.Image(
                                                                        src="assets/me.jpeg",
                                                                        fit="cover",
                                                                        radius="xl",
                                                                    ), # Image
                                                                ],
                                                                shadow=SHADOW,
                                                                radius="xl",
                                                                withBorder=True,
                                                                style={"width": "100px"},
                                                                p=5
                                                            ),  # Paper
                                                        ]
                                                    ),  # Center
                                                ]
                                            ),  # Col 
                                            linked_in_logo
                                        ]
                                    ), # Grid
                                ]
                            ),  # Col
                            dmc.Col(
                                children=[
                                    dmc.Paper(
                                        children=[
                                            dmc.Anchor(
                                                children=[
                                                    dmc.Text(
                                                        "MOSTAFA ELNAGAR",
                                                        style={'font-family': 'IntegralCF-Regular'},
                                                        size="xl",
                                                        color="dark",
                                                        underline=False
                                                    ), # Text
                                                ],
                                                align="center",
                                                underline=False,
                                                href="https://www.linkedin.com/in/mostafa-ds/",
                                                target="_blank",
                                            ), # Anchor
                                        ],
                                        shadow=SHADOW,
                                        radius=RADIUS,
                                        withBorder=True,
                                        p='sm',
                                    ),  # Paper
                                ]
                            ),  # Col
                        ]
                    ),  # Grid
                ]      
            ),  # Col
            dmc.Col(
                span=7,
                offset=1,
                gutter="xl",
                children=[
                    dmc.Group(
                        direction = 'row',
                        grow = True,
                        style={"margin-top": "10px"},
                        children = [
                            dmc.Paper(
                                radius=RADIUS, 
                                withBorder=True,
                                shadow=SHADOW,
                                p='sm',
                                style={'height': '165px'},
                                children=[
                                    dmc.Group(
                                        direction='column',
                                        position='center',
                                        spacing='xs',
                                        style={'margin-top':15},
                                        children=[
                                            dmc.Text(
                                                children='Select Start Date', 
                                                size='xs', 
                                                color='dimmed', 
                                                style={'font-family':'IntegralCF-RegularOblique'}
                                            ),  # Text
                                            dmc.DatePicker(
                                                id="date-picker-start",
                                                value=pd.to_datetime("2022-01-01", format="%Y-%m-%d"),
                                                size="lg"
                                            ),  # DatePicker
                                        ]
                                    ),  # Group
                                ],
                            ),  # Group
                            dmc.Paper(
                                radius=RADIUS,
                                withBorder=True,
                                shadow=SHADOW,
                                p='sm',
                                style={'height':'165px'},
                                children=[
                                    dmc.Group(
                                        direction='column',
                                        position='center',
                                        spacing='xs',
                                        style={'margin-top':15},
                                        children=[
                                            dmc.Text(
                                                children='Select End Date', 
                                                size='xs', 
                                                color='dimmed', 
                                                style={'font-family':'IntegralCF-RegularOblique'}
                                            ),  # Text
                                            dmc.DatePicker(
                                                id="date-picker-end",
                                                value=pd.Timestamp.today(),
                                                size="lg"
                                            ),  # DatePicker
                                        ]
                                    ),  # Group
                                ],
                            ),  # Paper
                        ]
                    ),  # Group
                ]
            )
        ]
    )
)