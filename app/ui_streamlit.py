from __future__ import annotations

import streamlit as st
from src.graph import run_graph

st.set_page_config(page_title="AI Agent App Template")
st.title("AI Agent App Template")

question = st.text_input("Ask a question")
if st.button("Run") and question:
    result = run_graph(question)
    st.write(result.answer)
    if result.sources:
        st.subheader("Sources")
        st.write(result.sources)
