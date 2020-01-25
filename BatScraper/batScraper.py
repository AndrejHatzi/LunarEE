from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.firefox.options import Options;

options = Options();
options.headless = False;
driver = webdriver.Firefox(options=options);


companies = ['http://www.baseballbats.net/bat-brands/baum-bats/', 'http://baseballbats.net/bat-brands/anderson-bat-company/', 'http://www.baseballbats.net/bat-brands/axe-bat/', 'http://baseballbats.net/bat-brands/viper-bats/', 'http://baseballbats.net/bat-brands/demarini/', 'http://baseballbats.net/bat-brands/rawlings/', 'http://baseballbats.net/bat-brands/combat/', 'http://www.baseballbats.net/bat-brands/easton/', 'http://baseballbats.net/bat-brands/akadema/', 'http://baseballbats.net/bat-brands/worth/', 'http://baseballbats.net/bat-brands/mizuno/', 'http://baseballbats.net/bat-brands/brett-brothers/', 'http://www.baseballbats.net/bat-brands/ruth-baseball-bats/', 'http://baseballbats.net/bat-brands/mattingly/', 'http://www.baseballbats.net/bat-brands/miken/', 'http://baseballbats.net/bat-brands/x-bat/', 'http://www.baseballbats.net/bat-brands/old-hickory/', 'http://www.baseballbats.net/bat-brands/marucci-baseball-bats/', 'http://baseballbats.net/bat-brands/sam-bat/', 'http://baseballbats.net/bat-brands/phoenix-bats/', 'http://baseballbats.net/bat-brands/max-bat/', 'http://baseballbats.net/bat-brands/bwp/', 'http://baseballbats.net/bat-brands/striker-bat-company/', 'http://baseballbats.net/bat-brands/mpowered/', 'http://www.baseballbats.net/bat-brands/louisville-slugger/', 'http://baseballbats.net/bat-brands/superior-bat/', 'http://baseballbats.net/bat-brands/rockbats/', 'http://baseballbats.net/bat-brands/d-bat/', 'http://baseballbats.net/bat-brands/pro-bats/', 'http://baseballbats.net/bat-brands/back-yard-bat-co/', 'http://www.baseballbats.net/bat-brands/glomar-pro-bats/', 'http://www.baseballbats.net/bat-brands/bamboobat-company/', 'http://www.baseballbats.net/bat-brands/kr3/', 'http://www.baseballbats.net/bat-brands/trinity-bat-company/', 'http://www.baseballbats.net/bat-brands/dinger-bats/', 'http://www.baseballbats.net/bat-brands/annex-baseball/', 'http://www.baseballbats.net/bat-brands/chameleon-bats/', 'http://www.baseballbats.net/bat-brands/ssk/', 'http://www.baseballbats.net/bat-brands/dove-tail-bats/', 'http://www.baseballbats.net/bat-brands/zinger-bat-co/', 'http://www.baseballbats.net/bat-brands/chandler-bats/', 'http://www.baseballbats.net/bat-brands/victus-sports/', 'http://www.baseballbats.net/bat-brands/tucci-lumber-company/', 'http://www.baseballbats.net/bat-brands/outlaw-bats/', 'http://www.baseballbats.net/bat-brands/natural-bat-company/', 'http://www.baseballbats.net/bat-brands/macdougall-batmakers/', 'http://www.baseballbats.net/bat-brands/texas-timber-bat-co/', 'http://www.baseballbats.net/bat-brands/jaw-bats/', 'http://www.baseballbats.net/bat-brands/game-1-sports/', 'http://www.baseballbats.net/bat-brands/mine-wood-bats/', 'http://www.baseballbats.net/bat-brands/warstic-wood-bat-co/', 'http://www.baseballbats.net/bat-brands/east-coast-bat-company/', 'http://www.baseballbats.net/bat-brands/smacker-bat-co/', 'http://www.baseballbats.net/bat-brands/ds-wood-bats/', 'http://www.baseballbats.net/bat-brands/proxr-bats/', 'http://www.baseballbats.net/bat-brands/dream-bat-company/', 'http://www.baseballbats.net/bat-brands/clutch-stick-baseball-bats/', 'http://www.baseballbats.net/bat-brands/kren-bat-company/', 'http://www.baseballbats.net/bat-brands/southbat/', 'http://www.baseballbats.net/bat-brands/madden-bats/', 'http://www.baseballbats.net/bat-brands/americas-bat-company/', 'http://www.baseballbats.net/bat-brands/rip-it/', 'http://www.baseballbats.net/bat-brands/rude-american-bat-company/', 'http://www.baseballbats.net/bat-brands/atomic-bat-company/', 'http://www.baseballbats.net/valor-bat-company/', 'http://www.baseballbats.net/bat-brands/dirty-south-bats/', 'http://www.baseballbats.net/sabrecat-bats/', 'http://www.baseballbats.net/bat-brands/carolina-clubs/', 'http://www.baseballbats.net/bat-brands/b45/', 'http://www.baseballbats.net/bat-brands/caliburn-bat-company/', 'http://www.baseballbats.net/bat-brands/tater-bats/', 'http://www.baseballbats.net/bat-brands/birchbats/', 'http://www.baseballbats.net/bat-brands/aul-bat-company/', 'http://www.baseballbats.net/bat-brands/black-widow-bats/', 'http://www.baseballbats.net/bat-brands/3031-2/', 'http://www.baseballbats.net/bat-brands/anchor-bat-company/', 'http://www.baseballbats.net/bat-brands/zorian-bat-company/', 'http://www.baseballbats.net/bat-brands/prairie-sticks-bat-company/', 'http://www.baseballbats.net/bat-brands/bear-valley-bats/', 'http://www.baseballbats.net/bat-brands/3074-2/', 'http://www.baseballbats.net/bat-brands/thorium-bat-company/', 'http://www.baseballbats.net/bat-brands/homewood-bat-company/', 'http://www.baseballbats.net/bat-brands/otw-bat-company/', 'http://www.baseballbats.net/bat-brands/yaya-baseball/', 'http://www.baseballbats.net/bat-brands/mad-dog-bats/', 'http://www.baseballbats.net/bat-brands/beaver-bat-company/', 'http://www.baseballbats.net/bat-brands/hendrix-bats/', 'http://www.baseballbats.net/bat-brands/zero-k-bats/', 'http://www.baseballbats.net/bat-brands/pillbox-bat-company/', 'http://www.baseballbats.net/bat-brands/hoosier-bat-company-2/', 'http://www.baseballbats.net/bat-brands/vullo-bat-company/', 'http://www.baseballbats.net/bat-brands/meridian-baseball-company/', 'http://www.baseballbats.net/bat-brands/phenom-bat-company/', 'http://www.baseballbats.net/bat-brands/bonsall-bat-company/']
def ScrapeCompany(url:str):
    current_company = [];
    driver.get(url);
    CompanyName:str = driver.find_element_by_class_name("entry-title").text;
    CompanyOverView:str = driver.find_element_by_class_name("wp-caption-text").text;
    try:
        CompanyOverView = CompanyOverView.replace("\n", "|");
    except:
        pass;
    try:
        CL:str = driver.find_element_by_xpath("//div[@class='entry-content']/div/img").get_attribute("src");
    except:
        CL = 0;    
    print(current_company);
    with open("bats.txt", "a") as f:
        f.write("{},{}\n".format(CompanyName, CompanyOverView));
    with open("batslinks.txt", "a") as f:
        f.write("{}\n".format(CL));
    
errs = [];
for i in range(len(companies)):
    try:
        ScrapeCompany(companies[i]);
    except:
        errs.append(i);
        print(i);
driver.close();
driver.quit();
