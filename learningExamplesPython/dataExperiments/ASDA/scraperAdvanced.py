import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.firefox.options import Options

# on this file commented out are ways to scrape asda involving both a normal webdriver (gecko or something ) and the headless one (which is phantomjs and also when the normal ones options is set to headless)
# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options)
driver = webdriver.PhantomJS()
# specify the url
urlpage = 'https://groceries.asda.com/search/yogurt'
# run firefox webdriver from executable path of your choice
# driver = webdriver.Firefox()
# get web page
driver.get(urlpage)
# execute script to scroll down the page
# driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# # sleep for 30s


# find elements by xpath
# at time of publication, Nov 2018:
# results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
# updated Nov 2019:
results = driver.find_elements_by_class_name(
    "co-product__anchor")
# print('Number of results', len(results))


data = []

# loop over results
for result in results:
    product_link = result.get_attribute("href")
    product_name = result.get_attribute('innerHTML')
    data.append({"product": product_name, "link": product_link})

driver.quit()


# driver = webdriver.Firefox()

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

for item in data:
    driver = webdriver.Firefox()
    url = item["link"]
    driver.get(url)
    time.sleep(5)
    try:
        nutritionResults = driver.find_elements_by_xpath(
            "//div[@class='asda-nutrition-light__text-indicator']")
        item["Fat"] = nutritionResults[1].get_attribute('innerHTML')
        item["Saturates"] = nutritionResults[2].get_attribute('innerHTML')
        item["Sugar"] = nutritionResults[3].get_attribute('innerHTML')
        item["Salt"] = nutritionResults[4].get_attribute('innerHTML')
    except:
        nutritionResults = driver.find_elements_by_xpath(
            "pdp-description-reviews__nutrition-cell pdp-description-reviews__nutrition-cell--details")
        print("LENGTH", len(nutritionResults))
        item["Fat"] = "NA"
        item["Saturates"] = "NA"
        item["Sugar"] = "NA"
        item["Salt"] = "NA"
    print(item)
    driver.quit()

    # html body div  # root div.layout section#main-content.layout__section.product-layout__section main.product-detail-page.layout__main div.product-detail-page__main-cntr div.product-detail-page__main-detail-cntr div.pdp-main-details div div div.pdp-description-reviews__product-details-cntr div.pdp-description-reviews__product-details-content div.pdp-description-reviews__nutrition-table-cntr div.pdp-description-reviews__nutrition-row.pdp-description-reviews__nutrition-row--details div.pdp-description-reviews__nutrition-cell.pdp-description-reviews__nutrition-cell--details
    # html body div  # root div.layout section#main-content.layout__section.product-layout__section main.product-detail-page.layout__main div.product-detail-page__main-cntr div.product-detail-page__main-detail-cntr div.pdp-main-details div div div.pdp-description-reviews__product-details-cntr div.pdp-description-reviews__product-details-content div.pdp-description-reviews__nutrition-table-cntr div.pdp-description-reviews__nutrition-row.pdp-description-reviews__nutrition-row--details div.pdp-description-reviews__nutrition-cell.pdp-description-reviews__nutrition-cell--details

    html body div  # root div.layout section#main-content.layout__section.product-layout__section main.product-detail-page.layout__main div.product-detail-page__main-cntr div.product-detail-page__main-detail-cntr div.pdp-main-details div div div.pdp-description-reviews__product-details-cntr div.pdp-description-reviews__product-details-content div.pdp-description-reviews__nutrition-table-cntr div.pdp-description-reviews__nutrition-row.pdp-description-reviews__nutrition-row--details div.pdp-description-reviews__nutrition-cell.pdp-description-reviews__nutrition-cell--details

    # div.pdp-description-reviews__nutrition-row: nth-child(2)


# nutDiv = soup.find(
#     "div", attrs={"class": "pdp-nutrition__nutrition-panel-container"})

# print(soup)
# print(url)
# print(nutDiv)

# for entry in data:
#     url = entry["link"]
#     page = urllib.request.urlopen(url)
#     soup = BeautifulSoup(page, 'html.parser')
#     print(soup)
#     # nutDivs = soup.findAll(
#     "div", {"class": "asda-nutrition-light pdp-nutrition__nutrition-panel"})

# print("nut divs", nutDivs)


# print(product_name)
# print(product_link)

#     print(site)
# url = product_link
# driver.get(urlpage)
# time.sleep(10)
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)


df.to_csv('asdaYoghurtLink.csv')
