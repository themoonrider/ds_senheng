# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#Phuong Tran
import selenium
from selenium import webdriver
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException

# Calling Chrome Webdriver
driver=webdriver.Chrome('/Users/ccmb_hd/Downloads/chromedriver_2')

# Open webpage
driver.get('https://www.senheng.com.my/all-products/computers-laptops.html?p=1')

# Running loop to store the product links in a list

listOfLinks=[]
condition=True
while condition:
    time.sleep(3)
    productInfoList=driver.find_elements_by_class_name('product-item-name')
    for e in productInfoList:
        pp=e.find_element_by_tag_name('a')
        listOfLinks.append(pp.get_property('href'))
    try:
        next_page=driver.find_element_by_class_name('pages').find_element_by_xpath("//li[@class='item pages-item-next']/a").get_property('href')
        driver.get(next_page)
    except:
        condition=False

#scraping individual product details
from tqdm import tqdm 
import re
alldetails=[]
brand=""
sku=""
distributor=""


for i in tqdm(listOfLinks):
    driver.get(i)
    time.sleep(3)
#product name
    name=driver.find_element_by_xpath("//h1[@class='page-title']/span").text

#product price
    try:
        price=driver.find_element_by_xpath("//*[@class='price-box price-final_price']").text
    except:
        price=""
        
#access product attribute description (brand, sku, distributor)
    try:
        innerHTML=driver.find_element_by_xpath("//*[@id='description']/script[1]").get_property("innerHTML")
       
#product brand
        brand=re.search('var product_brand = (.*)',innerHTML).group(1)

#brand distributor
        distributor=re.search('var distributor = (.*)',innerHTML).group(1)

#product_sku
        
        sku=re.search('var product_sku = (.*)',innerHTML).group(1)
    except:
        brand=""
        distributor=""
        sku=""
        
    temp={
            'SKU':sku,
            'Brand':brand,
            'Name':name,
            'Price':price,
            'Distributor':distributor,
            'LinkofProduct':i}
    alldetails.append(temp)

# Save result as csv
data=pd.DataFrame.from_dict(alldetails)
data.to_csv('Senheng_compt.csv')