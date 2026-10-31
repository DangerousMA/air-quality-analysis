from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Beijing Air Quality | PM2.5", page_icon="🌿", layout="wide")
st.markdown("""<style>.block-container {padding-top: 1.6rem;} [data-testid="stMetricValue"] {font-size: 1.85rem;} </style>""", unsafe_allow_html=True)

@st.cache_data(show_spinner="Memuat data PM2.5...")
def load_data():
    p = Path(__file__).parent / "main_data.csv"
    df = pd.read_csv(p, parse_dates=["timestamp"])
    assert {"timestamp", "station", "pm25"}.issubset(df.columns)
    df = df.dropna(subset=["timestamp", "station", "pm25"])
    df = df.loc[df["pm25"] >= 0].copy()
    df["date"] = df["timestamp"].dt.date
    df["month"] = df["timestamp"].dt.month
    return df

data = load_data()
MONTH = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"Mei",6:"Jun",7:"Jul",8:"Agu",9:"Sep",10:"Okt",11:"Nov",12:"Des"}
st.title("🌿 Beijing Air Quality Dashboard")
st.caption("PM2.5 | 12 stasiun | Dataset PRSA Beijing • Mar 2013–Feb 2017 | Data historis (bukan kondisi real-time)")
st.sidebar.header("Filter pengamatan")
all_stations = sorted(data["station"].unique())
selected_stations = st.sidebar.multiselect("Stasiun", all_stations, default=all_stations)
date_min, date_max = data["date"].min(), data["date"].max()
period = st.sidebar.date_input("Rentang tanggal", value=(date_min, date_max), min_value=date_min, max_value=date_max)
st.sidebar.caption("Rata-rata dihitung dari observasi PM2.5 per jam yang tersedia. Missing tidak diimputasi.")
if not selected_stations:
    st.warning("Pilih setidaknya satu stasiun."); st.stop()
if not isinstance(period, (tuple, list)) or len(period) != 2:
    st.info("Tentukan tanggal awal dan akhir."); st.stop()
start, end = period
if start > end:
    st.error("Tanggal awal harus lebih kecil atau sama dengan tanggal akhir."); st.stop()
filtered = data.loc[data["station"].isin(selected_stations) & data["date"].between(start, end)].copy()
if filtered.empty:
    st.warning("Tidak ada pengamatan pada kombinasi filter ini."); st.stop()
station_mean = filtered.groupby("station")["pm25"].mean().sort_values(ascending=False)
month_mean = filtered.groupby("month")["pm25"].mean().reindex(range(1,13))
col1, col2, col3, col4 = st.columns(4)
col1.metric("PM2.5 rata-rata", f"{filtered['pm25'].mean():,.1f} µg/m³")
col2.metric("Jumlah pengamatan valid", f"{len(filtered):,}")
col3.metric("Stasiun tertinggi", station_mean.index[0])
col4.metric("Bulan rerata tertinggi", MONTH[int(month_mean.idxmax())])

st.subheader("1. Perbandingan rata-rata PM2.5 antarlokasi")
fig, ax = plt.subplots(figsize=(10,5))
r = station_mean.sort_values()
colors = ["#0F766E" if s == station_mean.index[0] else "#94A3B8" for s in r.index]
ax.barh(r.index, r.values, color=colors)
ax.set_xlabel("PM2.5 rata-rata (µg/m³)")
ax.set_ylabel("Stasiun")
ax.set_xlim(0, max(r.values)*1.18)
for i,v in enumerate(r.values): ax.text(v+.5,i,f"{v:.1f}",va="center",fontsize=9)
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout(); st.pyplot(fig); plt.close(fig)
st.caption("Perbandingan hanya berlaku untuk stasiun dan rentang tanggal yang dipilih; bar dimulai dari nol.")

st.subheader("2. Pola PM2.5 menurut bulan kalender")
fig2, ax2 = plt.subplots(figsize=(10,3.7))
valid_months = month_mean.dropna()
ax2.plot(valid_months.index, valid_months.values, marker="o", color="#0F766E", linewidth=2.2)
ax2.set_xticks(range(1,13), [MONTH[x] for x in range(1,13)])
ax2.set_xlabel("Bulan kalender")
ax2.set_ylabel("PM2.5 rata-rata (µg/m³)")
ax2.set_ylim(bottom=0)
ax2.grid(axis="y",alpha=.25); ax2.spines[["top","right"]].set_visible(False)
fig2.tight_layout(); st.pyplot(fig2); plt.close(fig2)
st.caption("Bulan kalender digabungkan dalam rentang filter. Bila rentang tidak memuat siklus penuh, interpretasi pola musiman harus hati-hati.")

st.subheader("3. Tren harian pada periode terpilih")
daily = filtered.groupby("date")["pm25"].mean().reset_index()
fig3,ax3=plt.subplots(figsize=(11,3.2))
ax3.plot(daily["date"],daily["pm25"],color="#0F766E",linewidth=.8)
ax3.set(xlabel="Tanggal", ylabel="PM2.5 rata-rata (µg/m³)")
ax3.set_ylim(bottom=0); ax3.grid(axis="y",alpha=.2); ax3.spines[["top","right"]].set_visible(False)
fig3.tight_layout(); st.pyplot(fig3); plt.close(fig3)

st.subheader("4. Analisis lanjutan: proporsi kuartil relatif")
q1,q2,q3=data["pm25"].quantile([.25,.5,.75])
category_bins=[-np.inf,q1,q2,q3,np.inf]
category_labels=["Q1", "Q2", "Q3", "Q4"]
filtered["kelompok"] = pd.cut(filtered["pm25"], bins=category_bins, labels=category_labels, include_lowest=True)
share = (pd.crosstab(filtered["station"], filtered["kelompok"], normalize="index")*100).reindex(columns=category_labels,fill_value=0)
share=share.sort_values("Q4",ascending=False)
fig4,ax4=plt.subplots(figsize=(10,5))
left = np.zeros(len(share))
for label,color in zip(category_labels,["#CCFBF1","#5EEAD4","#0D9488","#115E59"]):
    vals=share[label].to_numpy(); ax4.barh(share.index,vals,left=left,label=label,color=color);left+=vals
ax4.set_xlim(0,100);ax4.set(xlabel="Proporsi pengamatan valid (%)",ylabel="Stasiun")
ax4.legend(title="Kuartil relatif",bbox_to_anchor=(1.02,1),loc="upper left")
ax4.spines[["top","right"]].set_visible(False)
fig4.tight_layout();st.pyplot(fig4);plt.close(fig4)
st.caption(f"Batas Q1={q1:.0f}, median={q2:.0f}, Q3={q3:.0f} µg/m³ dihitung dari seluruh data bersih. Q4 berarti >{q3:.0f} µg/m³. **Bukan** kategori resmi AQI atau ambang kesehatan.")
with st.expander("Tabel ringkasan dan unduh data"):
    st.dataframe(filtered.groupby("station")["pm25"].agg(["count","mean","median"]).round(2),use_container_width=True)
    st.download_button("Unduh data terfilter (CSV)", data=filtered[["timestamp","station","pm25"]].to_csv(index=False).encode("utf-8"),file_name="pm25_filtered.csv",mime="text/csv")
st.divider()
st.info("Analisis deskriptif pada data historis 2013–2017. Tidak menunjukkan penyebab polusi, kondisi udara saat ini, atau rekomendasi medis. Missing pada PM2.5 dikeluarkan dan nilai ekstrim valid dipertahankan.")
