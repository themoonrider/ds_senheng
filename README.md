# Commercial Insights from Scraping and Analyzing Product listings on Senheng.com.my

*   Scraped the entire Computers& Laptops section on senheng.com.my for Product Name, Product Brand, Product SKU, Product Price and Distributor. 
*   Engineered features from the text of product names to categorise into 8 categories.
*   Visualised number of product listings and average price per product category for each brand. 

## The following recommendations were suggested for Product Manager based on the data:

*   Product to increase more listings: Huawei Laptops
*   Rationale: Laptop listing in terms of Brands is well-distributed with 1 high-end Brand, 1 low-end Brand and mostly 4 medium-ranged Brands. However, in terms of the number of listings per brand, Huawei is a medium-ranged Brand but has much fewer products listed compared to other medium-ranged Brands. MSI Laptops are more expensive than Huawei but its listing almost doubles that of Huawei. HP Laptops are as similarly priced as Huawei but has more than 1.5 times higher listings than Huawei. 
*   Benefit: Increasing Huawei listings might be an option to cater for more interests in middle-ranged Laptops.  

## Code and Resources Used

* **Rstudio Version:** 1.4.1106
* **Python Version:** 3.7.3
* **Spyder Version:** 3.3.3
* **Data source:** https://www.senheng.com.my/all-products/computers-laptops.html?p=1
* **Web scraping:** https://medium.com/analytics-vidhya/web-scraping-e-commerce-sites-using-selenium-python-55fd980fe2fc
* **Markdown cheatsheet:** https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet#images

## What I've done:
1. Scraped Product information from senheng.com.my
+  Scraped for Product Name, Product Brand, Product SKU, Product Price and Distributor

2. Examined SH_raw:
+ Checked for missing values, duplicated entries and re-format character data
+ Added extra feature including Category based on keywords from Name

3. Analyzed SH_cleaned: 
+ Explored which Brands and Categories have the highest number of products listed 
+ Explored which Laptop and PC Accessories Brands have the highest average Price

## Insights:
1. Number of product listed:
*  Brands with the highest number of products listed are TP-Link, Microsoft, MSI, Apple and HP
*  The majority of products listed are PC Accessories, followed by Laptops
*  Most of Laptops are Microsoft, followed by Acer, MSI, HP, ASUS, Apple and lastly Huawei
*  Most of PC Accessories are TP-Link, followed by Apple, MSI, Microsoft, Rapoo, Logitech and Samsung.
![alt text](https://github.com/themoonrider/ds_senheng/blob/master/brand_category_distribution.png)

2. Average Laptop and PC Accessories Price:
*  Within Laptops: higher end - Apple (~6500)
                   medium range - MSI (~4800),HP (~4500), Huawei (~4500), Acer (~4300)
                   lower end - ASUS (~3500)
                  *Microsoft and Promate Laptop price are too low for a laptop, probably a misclassification error (Ideally will need to run the Scraping again to extract this information, will omit from analysis now on)*
*  Within PC Accessories: higher end - Apple, TP-Link 
                          medium range - MSI. 
                          lower end - Samsung, Rapoo, Logitech
* *PC Accessories include many different products, hence further classification is required with more specific scraping.* 
![alt text](https://github.com/themoonrider/ds_senheng/blob/master/avgprice_laptop_accessories.png)

## Limitations:
*   Categories were based on Keywords extracted from Product Name, therefore affecting the robustness of analysis. 
*   Re-do scraping for precise Category and more insights on PC Accessories. 
