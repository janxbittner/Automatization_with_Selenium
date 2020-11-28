
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd


#%% Data load from csv file and processing 
raw_df = pd.read_csv('./shazam_data/shazamlibrary.csv',skiprows =1)
raw_df = raw_df.set_index('TrackKey',drop = True)
raw_df = raw_df[['Title','Artist']]
raw_df = raw_df.drop_duplicates()

#%% Set chrome browser and login and scrabbing function

# Chrome run in background!
#options = webdriver.ChromeOptions()
#options.add_argument("headless")

# Set adblock on when chrome run in private mode
path_to_extension = r'C:\Users\Janek\Desktop\YT_Music\chrome_extension'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

Path = 'C:\webdrivers\chromedriver.exe'
#driver = webdriver.Chrome(executable_path=Path, chrome_options=options)
driver = webdriver.Chrome(executable_path=Path,chrome_options=chrome_options)
driver.create_options()

def LogIn():
    """
    This function allow to login at youtube music
    
    This funciton contain:
        - username,
        - password
        - link to login page.
    """
    
    username = 'YOURADDRESS@gmail.com'
    password = 'YOUR_PASSWORD'
    
    link_to_login_pg = "https://music.youtube.com/"
    driver.get(link_to_login_pg)
    # Freeze program for 4 seconds
    sleep(5)
    
    # Click login button
    driver.find_element_by_xpath('//*[@id="right-content"]/a')\
        .click()

    sleep(5)
    
    # Insert username
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
    sleep(5)
    # Click next button
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')\
        .click()
    sleep(6)
    # Insert password
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password) 
    sleep(5)
    
    # Click login button
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    sleep(10)

def ScrabbingBot():
    '''
    In this loop, for each song in raw dataframe:
        1) Search song,
        2) Open it and like,
        3) Back to you tube music main page.
    '''
    for i in raw_df.index:
        # Click find button
        driver.find_element_by_xpath('//*[@id="icon"]').click()
        sleep(5)
        
        song_name = raw_df.loc[i]['Title'] + ' '+ raw_df.loc[i] ['Artist']
        
        # Enter title and artist name and click enter button
        driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input').send_keys(song_name)
        driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input').send_keys(Keys.ENTER) 
        sleep(5)
        
        try: # Click the best choice button
            driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[2]/ytmusic-responsive-list-item-renderer/div[1]/ytmusic-item-thumbnail-overlay-renderer/div/ytmusic-play-button-renderer').click()
            sleep(5)
            driver.find_element_by_xpath('//*[@id="like-button-renderer"]/paper-icon-button[2]').click()
            sleep(5)
        except:
            sleep(5)
        

         
        # Go back to main page
        driver.get('https://music.youtube.com/')
        sleep(8)
        
        # Printing that song was liked
        print('Liked: ' + raw_df.loc[i]['Title'])

#%% Run program
try:
    LogIn()
    ScrabbingBot()
except:
    print("Something goes wrong")

