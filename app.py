import streamlit as st
import numpy as np
import pandas as pd
import sqlite3
import time
import requests
import streamlit.components.v1 as components
import plotly.express as px
from datetime import date, datetime
from Myround import myround
from fetchdata_investingcom import fetch_investingcom
from fnodataupdate import fnodata
#import SessionState
from filterdata_fun import filtered_data
from oichart_fun import oi_chart_graph
from coichart_fun import coi_chart_graph
from fiidiidatanalysis import fiidiidata
from streamlit import caching
from get_cmp_fun import get_cmp
from fii_chart_fun import get_fii_chart
from filterclientdat_fun import filterclientdat
from pcr_fun import pcr_cal
from optionspayoff import ironbutterfly
from call_option import call_payoff
from put_option import put_payoff
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
import plotly.express as px
from chart_studio import plotly as py
from streamlit_option_menu import option_menu
from plotly.offline import plot
import plotly.graph_objects as go
import yfinance as yf
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
import cufflinks as cf
from datetime import date
from datetime import timedelta
from realtime_optionchain import fetch_optionschain
import json
from os import name
from intradaycharts import volume_profile
#from pynse import *
import logging
import mplfinance as mpf
#from alice_blue import *
import dateutil.parser
from streamlit_option_menu import option_menu
#import streamlit_analytics
from auth0_component import login_button
import pyrebase
from PIL import Image
import hydralit_components as hc
from streamlit_echarts import st_echarts
from dispjsbar import oi_premium_bar_js
from gauge_chart import pcr_gauge_graph
from streamlit_autorefresh import st_autorefresh
import investpy
from fetchdata_investingcom import fetch_investingcom
from options_function_cal import OptionStrat
from options_function_cal import Option
from dispjsoptions import optionspayoff_diagram
from maxpaingraph import maxxpain
from filterdatafuture import filtered_data_future
from futureoigraph import futureoigraph_hist
from pcrchart_h import pcrchart_hist
from candlestick_chart import candlestick_chart_display
#from prophetforecastml import prophet_forecast_graph
from supertrend_optimal import suptrend_cal
import datetime
from multistrikeoi import multistrikeoi_graph
from fetchdata_investingcom_hist import fetch_investingcom_hist
import pytz
from sqlalchemy import create_engine
from globaldashboard import globaldashboard_metric
from globaldf import *
from globalcharts_summary import global_graph
from simplelinechart_js import linechart_js
from sectorchart import sector_graph



logo_top = Image.open("./tradatanalytix logo.png")

st.set_page_config(page_title = 'TraDatAnalytix',layout='wide', page_icon=logo_top)

st.title("Hello World")


st.write("Hi")