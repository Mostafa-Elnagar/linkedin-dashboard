import dash
from utils.data_preperation import DataRepo
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
repo = DataRepo()
repo.wrangle()

app = dash.Dash(
    __name__, 
    suppress_callback_exceptions = True, 
    title='LinkedIn Dashboard', 
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)
