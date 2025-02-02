import os
from dotenv import load_dotenv
import traceback
import re
import json
import pandas as pd
from langchain.callbacks import get_openai_callback
import streamlit as st
from src.mcqgenerator.mcqgenerator import final_chain
from src.mcqgenerator.utils import read_file, get_table
from src.mcqgenerator.logger import logging

#loading Json file
with open('Response.json', 'r') as file:
    RESPONSEJSON = json.load(file)

st.title("MCQ Generator App using Langchain")

with st.form('user_input'):
    uploaded_file = st.file_uploader("Upload a PDF or txt file")
    mcq_count = st.number_input("Enter no of mcqs", min_value=3, max_value=10)
    subject = st.text_input("Enter Subject", max_chars=20)
    tone = st.text_input("Enter complexity level", max_chars=20, placeholder="Simple")
    button = st.form_submit_button("Create MCQs")
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading...."):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:  # Fixed: Added parentheses
                    response = final_chain({
                    'text': text,
                    'number': mcq_count,
                    'subject': subject,
                    'tone': tone,
                    'responsejson': json.dumps(RESPONSEJSON)  # Fixed: dumps instead of dump
                })
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error(f"Error: {str(e)}")
            else:

            # Process the response
                if isinstance(response, dict):
                    # print("Response is: ", response["quiz"])
                    match = re.search(r'### RESPONSE\s*(.*)', response["quiz"], re.DOTALL)

                    

    # Parse the extracted JSON string
                    match = match.group(1).strip()
                    match2 = re.search(r'### RESPONSE\s*({.*})', match, re.DOTALL)
                    quiz = match2.group(1)
                    # print(quiz)

                    
                    if quiz:
                        try:
                            table_data = get_table(quiz)
                            if table_data:
                                df = pd.DataFrame(table_data)
                                df.index = df.index + 1
                                st.dataframe(df)
                            else:
                                st.error("No data available to create table")
                        except Exception as table_error:
                            st.error(f"Error processing table data: {str(table_error)}")
                    else:
                        st.warning("No quiz data found in the response")
                else:
                    st.write("Response:", response)
