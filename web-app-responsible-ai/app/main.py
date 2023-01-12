import streamlit as st
import pandas as pd

from datetime import date

#functions
from check_pw import *

#page settings

st.set_page_config(
    page_title="Responsible AI Sandbox",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    #}
)

#if check_password():

def main():
       
        #main
        st.title('Responsible AI sandbox')
       
        #sidebar
        st.sidebar.title("About F.R.A.N.C.K.")
        st.sidebar.info("IT represents today more than 4% of greenhouse gas emissions, which are the main responsibles for global warming. To be able to decrease this impact, we first need to measure it precisely.")
        st.sidebar.button("More on IT carbon impact")
        st.sidebar.info("FRANCK allows you to assess the carbon footprint of your entire IS. By combining measures from workplace (computers, screens, cellphones) and data centers, it will provide an overhaul of carbon emissions from your entire IS.")
        st.sidebar.button("More on FRANCK roadmap and features")
        
        

        uploaded_file = st.file_uploader("Start by importing your IT assets repository here :")
        

        if uploaded_file is not None:

            df = pd.read_excel(uploaded_file)
            st.text('Snapshot of loaded file :')
            st.write(df.head())

            st.markdown("""---""")
            
            tab1, tab2, tab3 = st.tabs(["Columns mapping", "User data mapping with ref data", "Results"])

            with tab1:
                
                st.tex

            with tab2:
                
                s

            with tab3:
                
                df_grouped['gwp_mult'] = df_grouped['volume'] * df_grouped['gwp_total']
                gwp

                ###

if __name__ == "__main__":
        main()