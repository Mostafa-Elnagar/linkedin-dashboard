
import dash_mantine_components as dmc
from dash import dcc

SHADOW = "xs"
RADIUS = "md"
THEME = "light"

def render_viz():
    return viz_layout


viz_layout = (
    dmc.Container(
        fluid=True,
        children=[
            dmc.Grid(
                columns=10,
                grow=True,
                children=[
                    dmc.Col(
                        span=7,
                        children=[
                            dmc.Group(
                                direction="column",
                                grow=True,
                                children=[
                                    dmc.Title(
                                        children="New Connections",
                                        order=2,
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center',
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                            'margin-top':15, 
                                        }
                                    ),  # Title
                                    dmc.Paper(
                                        radius="md", # or p=10 for border-radius of 10px
                                        withBorder=True,
                                        shadow='xs',
                                        p=0,
                                        style={"height": "600px"},
                                        children=[
                                            dcc.Graph(id='line-chart', style={"width": "100%", "height": "100%", "display": "flex"}),
                                        ]
                                    ),
                                ]
                            ),
                        ]
                    ),  # Col
                    dmc.Col(
                        span=7,
                        children=[
                            dmc.Group(
                                direction="column",
                                grow=True,
                                children=[
                                    dmc.Title(
                                        children="Most Common Companies", 
                                        order=2, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                            'margin-top':15, 
                                        }
                                    ),  # Title
                                    dmc.Paper(
                                        radius="md", # or p=10 for border-radius of 10px
                                        withBorder=True,
                                        shadow='xs',
                                        p=0,
                                        style={"height": "865px"},
                                        children=[
                                            dcc.Graph(id='bar-chart', style={"width": "100%", "height": "100%", "display": "flex"}),
                                        ]
                                    ),
                                ]
                            ),
                        ]
                    ),  # Col
                    dmc.Col(
                        span=3,
                        children=[
                            dmc.Group(
                                direction="column",
                                grow=True,
                                children = [
                                    dmc.Title(
                                        children="Connections Positions", 
                                        order=2, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                            'margin-top':15, 
                                        }
                                    ),  # Title
                                    dmc.Paper(
                                        radius="md", # or p=10 for border-radius of 10px
                                        withBorder=True,
                                        shadow='xs',
                                        p='sm',
                                        style={"height": "400px"},
                                        children=[
                                            dcc.Graph(id='pie-chart', style={"width": "100%", "height": "100%", "display": "flex"}),
                                        ]
                                    ),  # Paper
                                ]
                            ),
                            dmc.Group(
                                direction="column",
                                grow=True,
                                children = [
                                    dmc.Title(
                                        children="Positions WordCloud", 
                                        order=2, 
                                        style={
                                            'font-family':'IntegralCF-Regular',
                                            'text-align':'center', 
                                            "color": "grey",
                                            'letter-spacing':'1px',
                                            'margin-top':15, 
                                        }
                                    ),  # Title
                                    dmc.Paper(
                                        radius="md", # or p=10 for border-radius of 10px
                                        withBorder=True,
                                        shadow='xs',
                                        p='sm',
                                        style={"height": "400px"},
                                        children=[
                                            dcc.Graph(id='wordcloud', style={"width": "100%", "height": "100%", "display": "flex"}),
                                        ]
                                    ),  # Paper
                                ]
                            ),
                        ]
                    ),  # Col
                ]
            )
        ]
    )
    
)