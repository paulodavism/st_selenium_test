import streamlit as st
from seleniumbase import Driver

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

Este é um exemplo de como fazer web scraping usando SeleniumBase com Chrome no Streamlit.
"""

@st.cache_resource
def get_driver():
    return Driver(uc=True, headless=True)

try:
    driver = get_driver()
    driver.get("https://app.mercos.com/login")
    st.code(driver.page_source)
except Exception as e:
    st.error(f"Erro ao acessar a página: {str(e)}")
finally:
    if 'driver' in locals():
        driver.quit()