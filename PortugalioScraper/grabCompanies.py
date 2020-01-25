from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.firefox.options import Options;
from typing import List, Tuple, Dict;
from time import sleep;

'''
<?
    -> https://www.portugalio.com/bares/torres-novas/
    
    ** restaurantes **
    ** bares **
?>
'''

    




#link: str = "https://www.portugalio.com/bares/torres-novas/";

driver=webdriver.Firefox();
#driver.get(link);
def Grab()->str:
    
    nome: str = driver.find_elements_by_class_name("list-item-title");
    morada : str = driver.find_elements_by_class_name("list-item-address");
    cpostal: str = driver.find_elements_by_class_name("pc");
    telefone: str = driver.find_elements_by_class_name("list-item-phones-block");

    i:int;
    for i in range(len(telefone)):
        with open("contactos.txt", "a") as f:
            f.write("{},{},{},{}\n".format(nome[i].text, morada[i].text,cpostal[i].text,telefone[i].text));
    '''
    try:
        btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/ul/li[4]/a").get_attribute("href");
        driver.get(btn);
        Grab();
    except:
       print("Fim.\n");
    '''
for i in range(1, 4):
    driver.get("https://www.portugalio.com/restaurantes/torres-novas/{}.html".format(i));
    Grab();

#/html/body/div[1]/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div/ul/li[4]/a
Grab();
