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



holidays_dates = ["2022-03-18", "2022-01-26"]


current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
timetrack = current_time.hour

if timetrack <= 20:
  tday = date.today() - datetime.timedelta(days=1)
else:
  tday = date.today()

#tday = date.today()


#tday = st.sidebar.date_input('Date Input')
previous_Date = tday - timedelta(days = 180)

lc, mc, rc = st.columns(3)


with st.sidebar:
  selected_option = option_menu(
    "TraDatAnalytix",
    ['Global Markets','Derivatives Data','Open Interest Data', 'FII/DII Data','Pick Outperformers' ,'Trading Strategy'],
    icons = ['globe','body-text','bar-chart-fill', 'gear', 'currency-exchange' ,'option'],
    menu_icon = "cast",
    default_index = 0
  )


if selected_option == "Global Markets":

    

    tab1, tab2, tab3 = st.tabs(["Dashboard", "Comparison Charts", "Candlesticks"])




    # Get CMPS

    with tab1:
      
      lc, mc, rc = st.columns(3)

      #NIFTY 50
      dftrynifty = fetch_investingcom('Nifty 50', 'india')
      niftycmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      niftychangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      niftychangepc = "{:.2%}".format(niftychangepc)

      # DOW 30
      dftrynifty = fetch_investingcom('Dow 30', 'united states')
      dowcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      dowchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      dowchangepc = "{:.2%}".format(dowchangepc)


      # DAX
      dftrynifty = fetch_investingcom('DAX', 'germany')
      daxcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      daxchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      daxchangepc = "{:.2%}".format(daxchangepc)


      # CAC
      dftrynifty = fetch_investingcom('CAC 40', 'france')
      caccmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      cacchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      cacchangepc = "{:.2%}".format(cacchangepc)


      # Nikkei 225
      dftrynifty = fetch_investingcom('Nikkei 225', 'Japan')
      nikcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      nikchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      nikchangepc = "{:.2%}".format(nikchangepc)

      # Hang Sang
      dftrynifty = fetch_investingcom('Hang Seng', 'Hong Kong')
      hancmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      hanchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      hanchangepc = "{:.2%}".format(hanchangepc)



      # FTSE

      ftse_index = globaldashboard_metric('FTSE 100', 'united kingdom')
      #strait_index = globaldashboard_metric('STI', 'singapore')
      kospi_index = globaldashboard_metric('KOSPI', 'south korea')
      nasdaq_index = globaldashboard_metric('NASDAQ', 'united states')





      # Metrics
      lc.metric(label="Nifty 50 - India", value=niftycmp, delta=niftychangepc)
      mc.metric(label="DAX - Germany", value=daxcmp, delta=daxchangepc)
      rc.metric(label="DOW 30 - USA", value=dowcmp, delta=dowchangepc)
      lc.metric(label="CAC 40 - France", value=caccmp, delta=cacchangepc)
      mc.metric(label="Nikkei 225 - Japan", value=nikcmp, delta=nikchangepc)
      rc.metric(label="Hang Sang - Hong Kong", value=hancmp, delta=hanchangepc)
      lc.metric(label="FTSE - UK", value=ftse_index[0], delta=ftse_index[1])
      mc.metric(label="NASDAQ - US", value=nasdaq_index[0], delta=nasdaq_index[1])
      rc.metric(label="KOSPI - South Korea", value=kospi_index[0], delta=kospi_index[1])


      
    
    with tab2:

        # Summary Chart -- Global

        indialist = globallist_get("Nifty 50",'india')
        uklist = globallist_get("FTSE 100",'united kingdom')
        uslist = globallist_get("NASDAQ",'united states')
        japanlist = globallist_get("Nikkei 225",'Japan')
        hongkonglist = globallist_get("Hang Seng",'Hong Kong')
        francelist = globallist_get("CAC 40",'france')
        #sglist = globallist_get("STI",'singapore')
        southkorlist = globallist_get("KOSPI",'south korea')
        germanylist = globallist_get("DAX",'germany')
        datelist = datelistget("DAX",'germany')





        # linechartplot = linechart_js(datelist, indialist)


        # st_echarts(
        #     options = linechartplot, height=400,
        # )


        #st.write((indialist))
        # st.write((uslist))
        # st.write((gerlist))
        # st.write((frlist))
        # st.write((korlist))
        # st.write((hklist))
        # st.write((jplist))
        # st.write((uklist))
        #st.write((datelist))

        plot_global = global_graph(datelist, indialist, uklist, uslist, southkorlist, japanlist, hongkonglist, francelist, germanylist)


        st_echarts(
            options = plot_global, height=400,
        )




    with tab3:    
  
	      st.write("View Global Indices Candle Chart")
	      df = pd.read_csv("./globalindices_sym.csv")
	      
	      select_option = st.selectbox(
	                            'Choose Global Index',
	                            ('Nifty 50', 'Dow 30', 'FTSE 100' , 'CAC 40', 'DAX' ,'Nikkei 225', 'Hang Seng'))
	      
	      sb1 = st.button("See Chart")
	      

	      if sb1:

				  df = df.loc[(df['symbol'] == select_option)]
				  country = df.iloc[0]['country']
			      sym_yahoo = df.iloc[0]['yahoofin']

				  dftrynifty = fetch_investingcom(select_option, country)
				  
				  dateobj22 = list(dftrynifty.index.values)
				
				    
				  datelist = [str(x) for x in dateobj22]

				  dfohlc = dftrynifty[["Close", "Open", "Low", "High"]]
				    
				  ohlclist = dfohlc.to_numpy().tolist()
				    
				  printcandlechart = candlestick_chart_display(datelist, ohlclist)

				  st_echarts(
				                options=printcandlechart, height = "400px"
				             )
		         


          

  ###################################################################

if selected_option == "Derivatives Data":
    
    if tday.weekday() == 5:
      tday = tday - timedelta(days=1)
    elif tday.weekday() == 6:
      tday = tday - timedelta(days=2)
    elif tday.strftime("%Y-%m-%d") in holidays_dates:
      tday = tday - timedelta(days=1)
      if tday.weekday() == 0:
        tday = tday - timedelta(days=3)  
    
    df = fnodata(tday)



    selected4 = option_menu("", ["Option OI", "Future OI", "PCR", "Max Pain"], 
    icons=['collection', 'activity', 'speedometer', 'chevron-bar-contract'], 
    menu_icon="graph-up-arrow", default_index=1, orientation = "horizontal")



    if selected4 == "Option OI":
      #df = fnodata(tday)
      st.write(tday)
      left, right = st.columns(2)
      option = left.selectbox(
              'Symbol',
              df['SYMBOL'].unique())

      option_exp = right.selectbox(
              'Expiry DATE',
              df['EXPIRY_DT'].unique())

      option_inst = "OPTIDX"

      #Getting CMP
      gcmp = get_cmp(df, option)

      # Graph data as per user choice    
      filterdata = filtered_data(df, option, option_exp, option_inst, gcmp)

          
          #md_results = f"**{option}** Futures LTP **{gcmp}**"
          #st.markdown(md_results)
          #lc.markdown(f"<h4 style='text-align: center; color: white; background-color:SlateBlue'>{md_results}</h4>", unsafe_allow_html=True)
          #st.write("Current Future Price" + gcmp)

      
      bb1 = st.button("Generate OI Graphs")

      if bb1:
          gcmp = round(gcmp/50)*50
          #st.write(gcmp)
          dfce = filterdata[filterdata['OPTION_TYP']=="CE"]
          dfpe = filterdata[filterdata['OPTION_TYP']=="PE"]
          #st.write(dfce)
          #st.write(dfpe)
          strikelist = dfpe['STRIKE_PR'].tolist()
          pelist_oi = dfpe['OPEN_INT'].tolist()
          celist_oi = dfce["OPEN_INT"].tolist()
          
          oic_chart_js = oi_premium_bar_js(strikelist, celist_oi, pelist_oi, gcmp, titlegraph = "Open Interest")

          st_echarts(
                        options=oic_chart_js, height="400px",
                    )


          pelist_coi = dfpe['CHG_IN_OI'].tolist()
          celist_coi = dfce["CHG_IN_OI"].tolist()
          oicoi_chart_js = oi_premium_bar_js(strikelist, celist_coi, pelist_coi, gcmp, titlegraph = "Change in OI")

          st_echarts(
                        options=oicoi_chart_js, height="400px",
                    )
                    
          #oi_chart = oi_chart_graph(filterdata)

          #coi_chart = coi_chart_graph(filterdata)

          pcr = pcr_cal(df, option, option_exp, option_inst)
          pcrgraph = pcr_gauge_graph(pcr/2*100)

          # Plotting OI Graph
          
          #st.plotly_chart(oi_chart)

          # Plotting OI Change Graph
          
          #st.plotly_chart(coi_chart)
          md_results = f"**PCR for {option} **{round(pcr, 2)}"
          st.markdown(md_results)

          st_echarts(
                        options=pcrgraph, height="400px",
                    )
          
          #st.markdown(f"<h4 style='text-align: center; color: white; background-color:SlateBlue'>{pcr}</h4>", unsafe_allow_html=True)
        #st.write(pcr)

    if selected4 == "Max Pain":
        max_pain_graph = maxxpain (strikelist, celist_oi, pelist_oi)


        st_echarts(
                      options=max_pain_graph, height="400px",
                  )

    if selected4 == "Future OI": 
        
                      
        data1 = fnodata(tday)
        option = st.selectbox(
              'Symbol',
              df['SYMBOL'].unique())

        st.write(tday)      

        left, right = st.columns(2)
        #dftrynifty = fetch_investingcom('Nifty 50', 'india')
        #niftycmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']        

        filterdata = filtered_data_future(data1, option, "FUTIDX")

        # Hang Sang
        
        futoi_current = filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']
        fut_oi_current_pc_1 = (filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])
        fut_oi_current_pc = "{:.2%}".format(fut_oi_current_pc_1)


        futoi_next = filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']
        fut_oi_next_pc_1 = (filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])
        fut_oi_next_pc = "{:.2%}".format(fut_oi_next_pc_1)



        # Metrics
        left.metric(label="Futures (Current Month) OI Change", value=futoi_current, delta=fut_oi_current_pc)
        right.metric(label="Futures (Next Month) OI Change", value=futoi_next, delta=fut_oi_next_pc)

        if (fut_oi_current_pc_1 > 0.1):
          st.markdown(f'<h1 style="color:#04ba65;font-size:24px;">{"Market is Bullish"}</h1>', unsafe_allow_html=True)
        elif (fut_oi_current_pc_1 < -0.1):
          st.markdown(f'<h1 style="color:#ba0419;font-size:24px;">{"Market is Bearish"}</h1>', unsafe_allow_html=True)
        else:
          st.markdown(f'<h1 style="color:#d1c300;font-size:24px;">{"Market is Sideways"}</h1>', unsafe_allow_html=True)


        # start_date = date(2022, 2, 10)
        # end_date = date(2022, 2, 18)

        #holidays_dates = ["2022-03-18", "2022-01-26"]

        start_date = tday - timedelta(days=10)
        end_date = tday
        delta = timedelta(days=1)
        rowsdata = []

        while start_date <= end_date:
            if (start_date.weekday() >= 0 and start_date.weekday() <= 4) and (start_date.strftime("%Y-%m-%d") not in holidays_dates):
              data2 = fnodata(start_date)
              filterdata = filtered_data_future(data2, option, "FUTIDX")
              futoi_current = filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']
              fut_oi_current_pc_1 = (filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])*100
              futoi_next = filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']
              fut_oi_next_pc_1 = (filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])*100
              rowsdata.append([start_date, fut_oi_current_pc_1, fut_oi_next_pc_1])
            start_date += delta    
              #print(start_date)

        
        df = pd.DataFrame(rowsdata, columns=["Date", "Change in Current Month Future OI (%)", "Change in Next Month Future OI (%)"])
        # plot1 = df.plot()
        # fig = px.line(        
        #               df, #Data Frame
        #               x = "Date", #Columns from the data frame
        #               y = "Change in Current Month Future OI (%)",
        #               title = "Percentage Change in Future OI"
        #           )
        # fig.update_traces(line_color = "maroon")
        # st.plotly_chart(fig) 


        datelist1 = df["Date"].tolist()
        datelist = [date_obj.strftime('%Y%m%d') for date_obj in datelist1]
        currlist = df["Change in Current Month Future OI (%)"].tolist()
        nextlist = df["Change in Next Month Future OI (%)"].tolist()
          
        futurechart_js = futureoigraph_hist(datelist, currlist, nextlist)

        st_echarts(
                      options=futurechart_js, height="400px",
                  )
        
        #st.write(df) 
        
        #st.write(filterdata)




    if selected4 == "PCR":            
          data2 = fnodata(tday)
          left, right = st.columns(2)
          option = left.selectbox(
                  'Symbol',
                  df['SYMBOL'].unique())

          option_exp = right.selectbox(
                  'Expiry DATE',
                  df['EXPIRY_DT'].unique())

          option_inst = "OPTIDX"

          #Getting CMP
          gcmp = get_cmp(df, option)

          # Graph data as per user choice    
          filterdata = filtered_data(df, option, option_exp, option_inst, gcmp)     

          #left, right = st.columns(2)
          #dftrynifty = fetch_investingcom('Nifty 50', 'india')
          #niftycmp = dftrynifty.iloc[len(dftrynifty)-1]['Close'] 
          
          start_date = tday - timedelta(days=10)
          end_date = tday
          delta = timedelta(days=1)
          rowsdata = []

          while start_date <= end_date:
              if start_date.weekday() >= 0 and start_date.weekday() <= 4 and (start_date.strftime("%Y-%m-%d") not in holidays_dates):
                df = fnodata(start_date)
                gcmp = get_cmp(df, option)
                filterdata = filtered_data(df, option, option_exp, option_inst, gcmp)
                pcr = pcr_cal(df, option, option_exp, option_inst)
                rowsdata.append([start_date, pcr])    
                #print(start_date)
              start_date += delta
          
          df = pd.DataFrame(rowsdata, columns=["Date", "PCR"])
          #st.write(df)
          # plot1 = df.plot()
          # fig = px.line(        
          #               df, #Data Frame
          #               x = "Date", #Columns from the data frame
          #               y = "Change in Current Month Future OI (%)",
          #               title = "Percentage Change in Future OI"
          #           )
          # fig.update_traces(line_color = "maroon")
          # st.plotly_chart(fig) 


          datelist1 = df["Date"].tolist()
          datelist = [date_obj.strftime('%Y%m%d') for date_obj in datelist1]
          pcrlist = df["PCR"].tolist()
          # nextlist = df["Change in Next Month Future OI (%)"].tolist()

          pcrchartjs = pcrchart_hist(datelist, pcrlist)
            
          # futurechart_js = futureoigraph_hist(datelist, currlist, nextlist)

          st_echarts(
                        options=pcrchartjs, height="400px",
                    )
          
          if (df.iloc[len(df)-1]['PCR'] > df.iloc[len(df)-2]['PCR']):
            st.markdown(f'<h1 style="color:#04ba65;font-size:24px;">{"Market is Bullish"}</h1>', unsafe_allow_html=True)
          elif (df.iloc[len(df)-1]['PCR'] < df.iloc[len(df)-2]['PCR']):
            st.markdown(f'<h1 style="color:#ba0419;font-size:24px;">{"Market is Bearish"}</h1>', unsafe_allow_html=True)
          else:
            st.markdown(f'<h1 style="color:#d1c300;font-size:24px;">{"Market is Sideways"}</h1>', unsafe_allow_html=True)

          
      


#####################################################################################################3
