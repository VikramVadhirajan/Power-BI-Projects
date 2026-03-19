import streamlit as st
import streamlit.components.v1 as components

# ... other streamlit code ...
# st.set_page_config(layout="wide")
st.title("Warranty Analysis Power BI Dashboard")

# Paste the iframe code here
power_bi_embed_code = """
<iframe title="Warranty_Analysis_Report" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNTk1N2RjYjAtNjVkZi00YWRkLWIxY2YtZDQ1OGE2NGVkYjM4IiwidCI6IjQwYTk3NzkxLTgyYjAtNDhiYy05ZWM1LWViMjVjYjQyYTIzYSJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
# Embed the HTML content
components.html(power_bi_embed_code, width=800, height=600)

