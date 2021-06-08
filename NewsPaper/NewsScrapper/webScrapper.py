import os
import sys
from selenium import webdriver
import json
import json
from selenium.webdriver.firefox.options import Options
def get_data():
    options=Options()
    options.headless=True
    driver= webdriver.Firefox(options=options,executable_path='D:\geckodriver.exe')
    list_website=["https://www.ndtv.com/latest?pfrom=home-ndtv_mainnavgation"]
    driver.get(list_website[0])
    #driver.close()
    
    news_list=driver.find_elements_by_class_name('news_Itm')

    obj=[]
    for news in news_list:
        
        if "adBg" not in news.get_attribute("class"):
            #print(news.get_attribute("class"))
            #print(news.find_elements_by_class_name('news_Itm-img')[0].find_element_by_tag_name('a').get_attribute("href"))
            obj.append({
                    'heading':news.find_elements_by_class_name('newsHdng')[0].find_element_by_tag_name('a').get_attribute("innerText"),
                    'source':news.find_elements_by_class_name('newsHdng')[0].find_element_by_tag_name('a').get_attribute("href"),
                    'img':{'source':news.find_elements_by_class_name('news_Itm-img')[0].find_element_by_tag_name('img').get_attribute("src"),
                            'alt':news.find_elements_by_class_name('news_Itm-img')[0].find_element_by_tag_name('img').get_attribute("alt")},
                    'description':news.find_elements_by_class_name('newsCont')[0].get_attribute("innerText")
                })
    print(obj)
    driver.close()
    #return(obj)
    #driver.close()
    f=open(os.path.join(sys.path[0],"testData.txt"),"w",encoding="utf-8")
    f.write(json.dumps(obj))
    f.close()
    print('Suceess')
    #return "Success"
