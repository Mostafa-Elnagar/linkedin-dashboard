from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# import pages
from pages.dashboard.view.dashboard_view import render_dashboard
# from pages.dashboard.dashboard_controller import *
from pages.page_not_found import page_not_found
from graphics.plots import *
from graphics.trakcers import *
from app import app


server = app.server

def serve_content():
    return html.Div(
        [
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content')
        ]
    )

app.layout = serve_content()

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname in '/' or pathname in '/dashboard':
        return render_dashboard()
    return page_not_found()

if __name__ == '__main__':
    try:
        from environment.settings import APP_HOST, APP_PORT, APP_DEBUG
        app.run_server(debug=APP_DEBUG, host=APP_HOST, port=APP_PORT)
    except:
        pass
    