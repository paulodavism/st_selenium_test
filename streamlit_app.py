import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import platform

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

Este é um exemplo de como fazer web scraping usando SeleniumBase com Chrome/Chromium no Streamlit.
"""

@st.cache_resource
def get_driver():
    if platform.system() == "Linux":
        # Configuração para usar o Selenium Grid ou um driver remoto
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:chromeOptions'] = {
            'args': ['--headless', '--no-sandbox', '--disable-dev-shm-usage']
        }
        return webdriver.Remote(command_executor='http://<remote-url>:<port>/wd/hub', desired_capabilities=capabilities)
    return webdriver.Chrome()

try:
    driver = get_driver()
    driver.get("https://app.mercos.com/login")
    st.code(driver.page_source)
except Exception as e:
    st.error(f"Erro ao acessar a página: {str(e)}")
finally:
    if 'driver' in locals():
        driver.quit()
