import pandas as pd 
import numpy as np 
import calendar
from wordcloud import WordCloud
from PIL import Image

def pad(num):
        """Perform 4-digit-zero-padding"""
        return str(num).zfill(4)

def get_data_between(df, start_date, end_date):
    df_cnt_masked = df[
        (df['DATE'] >= start_date) & (df['DATE'] <= end_date)
    ]
    return df_cnt_masked

class DataRepo:
    def __init__(
            self,
            connections="./data/Connections.csv",
            invitations="./data/Invitations.csv",
            messages="./data/messages.csv"
    ):
        self.connections = connections
        self.invitations = invitations
        self.messages = messages

    def wrangle(
        self,

    ):
        self.df_cnt = pd.read_csv(self.connections)
        self.df_inv = pd.read_csv(self.invitations)
        self.df_msg = pd.read_csv(self.messages)
        # clean connections dataframe
        self.df_cnt["data_position"] = self.df_cnt.Position.str.contains(
            r"(Aritficial Intelligence|Data|Machine Learning|Statistician)", case=False, na=False
        )
        self.df_cnt["DATE"] = pd.to_datetime(self.df_cnt["Connected On"])
        self.df_cnt["month"] = self.df_cnt["DATE"].dt.month
        self.df_cnt['month'] = self.df_cnt['month'].apply(lambda x: calendar.month_abbr[x])
        self.df_cnt.drop("Connected On", axis=1, inplace=True)

        # clean invitations dataframe
        self.df_inv["DATE"] = pd.to_datetime(self.df_inv["Sent At"], format="%m/%d/%y, %I:%M %p")
        self.df_inv.drop(["Sent At"], axis=1, inplace=True)

        # clean messages
        self.df_msg["DATE"] = pd.to_datetime(self.df_msg["DATE"], utc=True).dt.tz_localize(None)
    
    def get_num_connections(self, start_date, end_date):
        # Connections and Companies
        df_cnt_masked = get_data_between(self.df_cnt, start_date, end_date)
        connections_count = pad(len(df_cnt_masked))

        return connections_count
    
    def get_num_companies(self, start_date, end_date):
        df_cnt_masked = get_data_between(self.df_cnt, start_date, end_date)
        companies_count = len(df_cnt_masked["Company"].unique())
        return pad(companies_count)
    
    def get_inv_nums(self, start_date, end_date):
        """Returns a tuple of (invitations in, invitations out)"""
            # Invitations
        df_invite_masked = get_data_between(self.df_inv, start_date, end_date)
        mask_count_in = df_invite_masked["Direction"] == "INCOMING"
        in_invites = mask_count_in.sum()
        out_invites = (~mask_count_in).sum()

        return pad(in_invites), pad(out_invites)
    
    def get_num_positions(self, start_date, end_date):
        """Returns a tuple (data, non-data)"""
        df = get_data_between(self.df_cnt, start_date, end_date)
        data_count = len(df)
        non_data_count = len(self.df_cnt) - data_count
        return data_count, non_data_count
    
    def get_most_companies(self, start_date, end_date, limit=6):
        df = get_data_between(self.df_cnt, start_date, end_date)
        most_common = df["Company"].value_counts().head(limit)
        return most_common
    
    def get_connections_by_month(self, start_date, end_date):
        df = get_data_between(self.df_cnt, start_date, end_date).set_index("DATE")
        df['connection'] = 1
        count_by_month = df.resample("M")["connection"].count()
        return count_by_month
    
    def get_wordcloud_data(self, start_date, end_date):
        position_series = get_data_between(self.df_cnt, start_date, end_date)["Position"].dropna().astype(str)
    
        with Image.open("./assets/1384014.png") as img:
            mask = np.array(img)
        
        my_wordcloud = WordCloud(
            background_color='white',
            height=275,
            mask=mask,
            mode="RGBA",
            collocations=False
        ).generate(' '.join(position_series))

        return my_wordcloud