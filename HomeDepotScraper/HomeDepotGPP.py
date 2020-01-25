#Version 1.1 by LunarEE

#Std Libraries
import time;
import json;
from typing import List, Tuple, Dict;

#Selenium Extensions
#to install selenium => pip install selenium
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.firefox.options import Options;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.common.by import By;
from selenium.common.exceptions import TimeoutException;

#Pandas
import pandas as pd


saved_list = [];
#Functions from previous version
def get_file_length(file_name, column_name):
    try:
        df_fun = pd.read_csv(file_name)
        ss = len(df_fun[column_name].tolist())
    except:
        return 0
    return ss


def append_data(data_dict_arg, file_name, column_name):
    p = get_file_length(file_name, column_name)
    df = pd.DataFrame(data_dict_arg, index=[p])
    if p == 0:
        df.to_csv(file_name, mode='a+', header=True, encoding='utf-8', index=False)
    else:
        df.to_csv(file_name, mode='a+', header=False, encoding='utf-8', index=False)

#Parsing Functions
def ParseData(product_data):
    print(product_data);
    product_dict = dict()
    #print("+++++++++++++++++++++++++++++++++++++++++++++")
    #print(product_data['primaryItemData']['itemExtension']['pricing'])
    #print(product_data['primaryItemData']["shipping"])
    #print("+++++++++++++++++++++++++++++++++++++++++++++")

    product_dict["Store ID"] = product_data['localStore']['storenumber']
    print("@ Store of ID [{}] scraped!".format(product_dict["Store ID"]));
    try:
        product_dict["Original Price"] = product_data['primaryItemData']['itemExtension']['pricing']['originalPrice']
    except:
        product_dict["Original Price"] = ""
    try:
        product_dict["Special Price"] = product_data['primaryItemData']['itemExtension']['pricing']['specialPrice']
    except:
        product_dict["Special Price"] = ""
    try:
        product_dict['Eligible For Free Shipping'] = product_data['primaryItemData']["shipping"]["eligibleForFreeShipping"]
    except:
        product_dict['Eligible For Free Shipping'] = ""
    try:
        product_dict['Free Shipping Threshold'] = product_data['primaryItemData']["shipping"]['freeShippingThreshold']
    except:
        product_dict['Free Shipping Threshold'] = ""
    try:
        product_dict['Free Shipping Message'] = product_data['primaryItemData']["shipping"]['freeShippingMessage']
    except:
        product_dict['Free Shipping Message'] = ""
    try:
        product_dict['Excluded States Shipping'] = product_data['primaryItemData']["shipping"]["excludedShipStates"]
    except:
        product_dict['Excluded States Shipping'] = ""
    append_data(product_dict, "Product_Details.csv", "Store ID")

def loadFromSave(ProductID:str):
    #save stores but in ram instead of physical memory;
    try:
        with open("{}_save.txt".format(ProductID), 'r') as SavedStores:
            saved_list = SavedStores.readlines();
        return saved_list;
        #print(saved_list);
    except:
        with open("{}_save.txt".format(ProductID), 'w') as SavedStores:
            pass;

def ScrapeData(ProductID:str,end:int = 3)->None:
    stop:int = 0;
    #print(saved_list);
    print(".Browser Started");
    with open('Stores.txt', 'r') as homeDepotStoreID:
        for line in homeDepotStoreID:
            try:
                if (line not in saved_list):
                    #
                    
                    driver.get("https://www.homedepot.com{}".format(line));
                    try:
                        shopThisStoreBtn = driver.find_element_by_css_selector("a.bttn--inline");
                        shopThisStoreBtn.click();
                    except:
                        if(driver.find_element_by_css_selector("div.js-localAdChangeStoreButton > a:nth-child(1)")):
                            print("@ Object in Cache");
                        else:
                            print("Error=>{}".format(link));
                    driver.get("https://www.homedepot.com/p/svcs/frontEndModel/{}".format(ProductID));
                    time.sleep(3);
                    rawData = driver.find_element_by_id("rawdata-tab").click();
                    jsonFile = driver.find_element_by_class_name("data");
                    Product_dict = json.loads(jsonFile.text);
                    ParseData(Product_dict);
                    with open("{}_save.txt".format(ProductID), "a") as f:
                        f.write(line);
                    stop += 1;
                    if (stop >= end):
                        break;
                else:
                    print("skipped {}".format(line));

            #print(line);
            except:
                driver.get("https://www.homedepot.com{}".format(line));
                try:
                    shopThisStoreBtn = driver.find_element_by_css_selector("a.bttn--inline");
                    shopThisStoreBtn.click();
                except:
                    if(driver.find_element_by_css_selector("div.js-localAdChangeStoreButton > a:nth-child(1)")):
                        print("@ Object in Cache");
                    else:
                        print("Error=>{}".format(link));
                driver.get("https://www.homedepot.com/p/svcs/frontEndModel/{}".format(ProductID));
                time.sleep(3);
                rawData = driver.find_element_by_id("rawdata-tab").click();
                jsonFile = driver.find_element_by_class_name("data");
                Product_dict = json.loads(jsonFile.text);
                ParseData(Product_dict);
                with open("{}_save.txt".format(ProductID), "a") as f:
                    f.write(line);
                stop += 1;
                if (stop >= end):
                    break;


print("Load Browser Interface {0 - False}, {1 - True}");
visible:int = int(input(">"));
print("Insert id code")
ProductID:str = input(">");
print("Number of Stores to scrape");
nStores:int = int(input(">"));
#"304206790";
saved_list = loadFromSave(ProductID);
options = Options();
if (visible == 0):
    options.headless = True;
else:
    options.headless = False;
print("Loading Browser...");
driver = webdriver.Firefox(options=options);
ScrapeData(ProductID, nStores);


