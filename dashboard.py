import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Data
total_izin = 597
average_izin = 712.1
selesai_diproses = 433
ditolak_dibatalkan = 163
masih_diproses = 1

# percentage
selesai_perc = selesai_diproses / total_izin * 100
ditolak_perc = ditolak_dibatalkan / total_izin * 100
masih_perc = masih_diproses / total_izin * 100


# Set page config
st.set_page_config(page_title = "DPMPTSP Dashboard", layout="wide")


# Header
t1, t2 = st.columns((0.07,1))

t1.image('images/dpmptsp_logo2.jpeg', width = 100)
t2.title('Dashboard Tipologi DPMPTSP Jakarta')
t2.markdown("**tel :** 1500164 / (021)1500164 **| website :** https://pelayanan.jakarta.go.id/ **")


with st.spinner('Updating Report .... ') : 

    # Metrics setting and rendering

    sp_izin_df = pd.read_excel('ct_izin.xlsx',sheet_name = 'service_point')
    sp = st.selectbox('Choose Service Point', sp_izin_df, help = 'Filter report to show only one service point of penanaman modal')

    # label logic : determine if kecamatan, kelurahan or kota

    if sp.startswith('Kantor Camat') : 
        level = 'kecamatan' 
    elif sp.startswith('Kantor Lurah') : 
        level = 'kelurahan'
    else :
        level = 'kota / kabupaten'

# Define layout using column in streamlit
m1, m2, m3  = st.columns((1,1,1))
m1.write('')
m2.metric(label = "Total Izin yang diajukan", value = total_izin)
m3.metric(label = f"**In Average**<br> <sub> izin per {level.capitalize()}</sub>", value = '', delta = average_izin)
m1.write('')

c3, c4, c5 = st.columns(3)
c3.metric(label = "Selesai diproses", value = selesai_diproses, delta=f"{round(selesai_perc, 1)}%")
c4.metric(label = "Masih diproses", value = masih_diproses, delta=f"{round(masih_perc, 1)}%")
c5.metric(label = "Ditolak & dibatalkan", value = ditolak_dibatalkan, delta=f"{round(ditolak_perc, 1)}%")


fig = go.Figure(go.Bar(
    x = ['Selesai','Masih Diproses', 'Ditolak & Dibatalkan']
    , y = [selesai_diproses, masih_diproses, ditolak_dibatalkan]
    , marker_color = ['green', 'orange', 'red']
))

fig.update_layout(title_text = "Distribution of Process Status", title_x = 0.5)

st.plotly_chart(fig, use_container_width = True)