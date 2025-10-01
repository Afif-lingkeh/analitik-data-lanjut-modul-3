import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")

    # Tampilkan data di Streamlit
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    #st.set_option('deprecation.showPyplotGlobalUse', False)

    data = pd.read_csv("pddikti_example.csv")
    
    selected_univesity = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data["universitas"] == selected_univesity]

    plt.figure(figsize=(12, 6))
    
    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]
        subset = subset.sort_values(by='id', ascending = False)
        plt.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    plt.title(f'Visualisasi data untuk{selected_univesity}')
    plt.xlabel('Semester')
    plt.xticks(rotation=90)
    plt.ylabel('Jumlah')
    plt.legend()
    plt.show()
    st.pyplot()