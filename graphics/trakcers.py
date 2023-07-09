from dash import Input, Output
from app import app, repo

# Updating the five trackers
@app.callback(
    Output("connections-tracker", "children"),
    Output("companies-tracker", "children"),
    Output("invites-received-tracker", "children"),
    Output("invites-sent-tracker", "children"),
    Input("date-picker-start", "value"),
    Input("date-picker-end", "value")
)
def update_tracker(start_date, end_date):
    # Connections and Companies
    connections_count = repo.get_num_connections(start_date, end_date)
    companies_count = repo.get_num_companies(start_date, end_date)
    # Invitations
    in_invites, out_invites = repo.get_inv_nums(start_date, end_date)

    return connections_count, companies_count, in_invites, out_invites