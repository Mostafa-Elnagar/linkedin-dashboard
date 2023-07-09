
import plotly.express as px
from dash import Input, Output
from app import app, repo
from plotly.io import templates



def get_data_between(df, start_date, end_date):
    df_cnt_masked = df[
        (df['DATE'] >= start_date) & (df['DATE'] <= end_date)
    ]
    return df_cnt_masked

# Line Chart 
@app.callback(
    Output("line-chart", "figure"),
    Input("date-picker-start", "value"),
    Input("date-picker-end", "value")
)
def update_line(start_date, end_date):
    cnt_by_month = repo.get_connections_by_month(start_date, end_date)
    fig = px.line(
        cnt_by_month,
        template=templates["simple_white"],
        title="Total Connections by Month Name"
    )
    fig.update_traces(mode="lines+markers",line={'color':'blue'})
    fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        showlegend=False, 
        yaxis_title=""
    )
    
    return fig

# Bar Chart 
@app.callback(
    Output("bar-chart", "figure"),
    Input("date-picker-start", "value"),
    Input("date-picker-end", "value")
)
def update_bar(start_date, end_date):
    most_companies = repo.get_most_companies(start_date, end_date, limit=10)
    fig = px.bar(
        most_companies,
        template=templates["simple_white"],
        orientation='h',
        title="",
        text_auto="d",
        
    )
    fig.update_yaxes(tickangle=-20)
    fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        showlegend=False,
        uniformtext_minsize=14,
        uniformtext_mode='hide',
        yaxis_title=""
    )
    fig.update_traces(
        marker_color='blue',
        textposition="outside",
        textfont={
            "family": "Courier New, monospace",
            "color": "MidnightBlue"
        }
    )
    fig.update_xaxes(visible=False)
    
    return fig

# Pie Chart 
@app.callback(
    Output("pie-chart", "figure"),
    Input("date-picker-start", "value"),
    Input("date-picker-end", "value")
)
def update_pie(start_date, end_date):
    data, non_data = repo.get_num_positions(start_date, end_date)

    fig = px.pie(
        names=["Data Related", "Other"],
        values=[data, non_data],
        template=templates["simple_white"],
        title="",
        hole=0.5
    )
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig.update_traces(marker_colors=['RoyalBlue','LightSalmon'])
    
    return fig
    
@app.callback(
    Output("wordcloud", "figure"),
    Input("date-picker-start", "value"),
    Input("date-picker-end", "value")
)
def update_wordcloud(start_date, end_date):
    
    my_wordcloud = repo.get_wordcloud_data(start_date, end_date)
    
    fig = px.imshow(
        my_wordcloud,
        template=templates["simple_white"],
        title="",
    )
    fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    
    return fig


