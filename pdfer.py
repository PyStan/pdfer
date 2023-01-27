import streamlit as st
import fillpdf
from fillpdf import fillpdfs
import pandas as pd
import math

st.title("Fill out PDF with data from CSV file")
col1, col2, col3 = st.columns(3)

csv_file = st.file_uploader(label="Choose CSV File")
pdf_file = st.file_uploader(label="Choose a PDF")
if csv_file is not None:
    df = pd.read_csv(csv_file)
    old_values = list(df.values)
    # values = old_values[0].tolist()

def process():
    if rows > 1:
        for row in range(rows):
            values = old_values[row].tolist()
            pdf_output = f"PDF{row}"
            map_dict = dict(zip(mapped_keys, values))
            fillpdfs.write_fillable_pdf("../test.pdf", f"{pdf_output}.pdf",
                                        map_dict)

    map_dict = dict(zip(mapped_keys, values))
    fillpdfs.write_fillable_pdf("../test.pdf", f"{pdf_output}.pdf", map_dict)

while csv_file and pdf_file:
    dict1 = list(fillpdfs.get_form_fields(pdf_file))
    dict1.insert(0, "")
    # df = pd.read_csv(csv_file)
    keys = list(df.columns)
    # old_values = list(df.values)
    mapped_keys = []
    num = math.floor(len(keys) / 2)

    with col1:
        for item in keys[:num + 1]:
            df_column = st.selectbox(label=f"CSV Column '{item}' Map to PDF Field:", key=item,
                                     options=dict1)
            mapped_keys.append(df_column)
    with col2:
        for item in keys[num + 1:]:
            df_column = st.selectbox(label=f"CSV Column '{item}' Map to Pdf Field:", key=item,
                                    options=dict1)
            mapped_keys.append(df_column)
    with col3:
        rows = st.number_input("How many rows, excluding header?", min_value=1, value=1)
        values = old_values[0].tolist()
        pdf_output = st.text_input("Name PDF file", key="OG")
        st.button("Process", on_click=process, args=())




