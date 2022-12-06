from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

url = "https://www.zillow.com/homes/for_sale/131678830_zpid/"


# Initialise the webdriver
safari_options = Options()
safari_options.headless = False
driver = webdriver.Firefox(options=safari_options)
driver.get(url)
time.sleep(5)  # ensure the page is fully loaded
#xpath = '//*[@id="details-page-container"]/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div/ul/li[10]/div/div[2]/div/div/h4'
#neigh = driver.find_element(By.XPATH, xpath)
# button_one = driver.find_element(By.XPATH,'//*[@id="details-page-container"]/div/div/div[1]/div[2]/div[2]/div[3]/div/div/div/div/div/nav/ul/li[3]/a')
button = driver.find_element(By.XPATH, '//*[@id="ds-home-values"]/div/div[1]/div/div/div[3]/div/button/p')
button.click()
# Render the dynamic content to static HTML
html = driver.page_source
n = html.find('neighborhoodRegion')
neigh = html[n:]
neigh = list(neigh.split("\\"))
neigh = neigh[4][1:]
# Parse the static HTML
soup = BeautifulSoup(html, "html.parser")
# <h4 class="Text-c11n-8-73-0__sc-aiai24-0 hdp__sc-vwszk-0 bKDNyY fHJlku hdp__sc-1j01zad-5 bOGcXJ">Neighborhood: Highland</h4>
divs = soup.find_all("span", {"class": "Text-c11n-8-73-0__sc-aiai24-0 kHeRng"})

my_string = ""
for i in divs:
    tmp = str(i)
    if "Subdivision" in tmp:
        my_string = tmp[64:]
        my_string = my_string[:-7]
        break

stuff = []
for i in range(1, len(di)):
    tmp = di[i][58:]
    tmp = list(tmp.split('</td>'))
    stuff.append(tmp[0])

historical_data = {'2010':{},'2011':{},'2012':{},'2013':{},
                   '2014':{},'2015':{},'2016':{},'2017':{},
                   '2018':{},'2019':{},'2020':{},'2021':{},
                   '2022':{}}
for i in range(0, len(stuff), 4):
    x = i
    tmp = stuff[x:x+2]
    tmp_dates = tmp[0].split(" ")
    tmp_dates.reverse()
    tmp_dates.append(tmp[1])
    if len(tmp_dates) == 3:
        year = tmp_dates[0]
        month = tmp_dates[1]
        value = tmp_dates[2]
        historical_data[year][month] = value

print(historical_data)

# Close the webdriver
driver.close()