import streamlit as st
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import layout
from bokeh.models import Div
import sys

total_izin = 597
average_izin = 712.1
selesai_diproses = 433
ditolak_dibatalkan = 163
masih_diproses = 1

# percentage
selesai_perc = selesai_diproses / total_izin * 100
ditolak_perc = ditolak_dibatalkan / total_izin * 100
masih_perc = masih_diproses / total_izin * 100

total_izin_box = Div(text = f"""
    <div style = 'background-color: #f0f0f0; text-align:center; width: 200px; padding:10px;'>
        <p> Total Izin yang diajukan </p>
        <h2>{total_izin}</h2>
    </div>
""")

average_izin_box = Div(text=f"""
    <div style = 'background-color: #f0f0f0; text-align:center; width: 200px; padding:10px;'>
        <p> in average</p>
        <p> total izin yang diajukan per kecamatan </p>
        <h4>{average_izin}</h4>
    </div>
""")

selesai_izin_box = Div(text=f"""
   <div style = 'background-color: #f0f0f0; text-align:center; width:200px; padding:10px;'>
        <p> Selesai diproses </p>
        <h2>{selesai_diproses}</h2> 
        <p> {round(selesai_perc, 1)}%</p>
    </div>
""")

masih_diproses_box = Div(text=f"""
    <div style = 'background-color: #f0f0f0; text-align:center; width:200px; padding:10px;'>
        <p> Masih diproses</p>
        <h2>{masih_diproses}</h2>
        <p>{round(masih_perc, 1)}%</p>
    </div>
""")

ditolak_izin_box = Div(text=f"""
    <div style = 'background-color: #f0f0f0; text-align:center; width:200px; padding:10px;'>
        <p> Ditolak & Dibatalkan</p>
        <h2>{ditolak_dibatalkan}</h2>
        <p>{round(ditolak_perc, 1)}%</p>
    </div>
""")

layout_dashboard = layout([
    [total_izin_box, average_izin_box]
    , [selesai_izin_box, masih_diproses_box, ditolak_izin_box]
])

print(sys.path)
st.bokeh_chart(layout_dashboard)
