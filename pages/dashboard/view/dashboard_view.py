
import dash_mantine_components as dmc

from app import app
from .sections.header import render_header
from .sections.overview import render_overview
from .sections.viz import render_viz

SHADOW = "xs"
RADIUS = "md"
THEME = "light"

def render_dashboard():
    return layout

layout = dmc.MantineProvider(
    theme={
        'colorScheme': THEME
    },
    children=[
        dmc.Container(
            fluid=True,
            # style={
            #     "align": "center",
            #     "marginTop": "10px",
            #     "marginBottom": "10px",
            #     "marginRight": "20px",
            #     "marginLeft": "20px",
            # },
            children=[
                dmc.Stack(
                    align="stretch",
                    justify="center",
                    children=[
                        render_header(),
                        dmc.Divider(label="Overview", labelPosition='center', size='xs', variant="solid", color="gray"),
                        render_overview(),
                        dmc.Divider(label="Visualizations", labelPosition='center', size='xs', variant="solid", color="gray"),
                        render_viz()
                    ]
                ),  # Grid
            ]
        ),  # Div
    ]
)

