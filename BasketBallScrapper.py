#Function for scrapping data from BasketBall Reference.com
from bs4 import BeautifulSoup
import requests
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def basketball_scrapper(title_sheet, url ,title_xlsxfile):
    """Function that creates an excel (xlsx) spreadsheet based off data collected off a BasketBall Reference URL
    The stats include-Rebounds,Assists,Points,Opposing Team, three point info ,Field Goal info"""
    e="oops, that URL isn't from BBall Reference or is wrong"
    #Initialize excel file
    excel = openpyxl.Workbook()

    sheet = excel.active
    sheet.title = title_sheet

    sheet.append(['Date', 'Opp' , 'MP','FG','FGA','3P','3PA','3P%','TRB','AST','STL','BLK','TOV','PTS'])

    #Start extracting these data from website

    #Create try and except block
    try:
        #Get Raw HTML file
        source = requests.get(url)
        #Call error is URl doesnt exist
        source.raise_for_status()

        #Create HTML parser
        soup = BeautifulSoup(source.text , 'html.parser')

        #Create a variable that represents all values in div
        stats = soup.find('div',{'id':"all_pgl_basic"} , class_ = "table_wrapper").find('tbody').find_all('tr',class_=None)
    
    

        #Loop trough the parsed HTML to extract statisics
        for stat in stats:

            #Extract Date
            date = stat.find('td' , class_ = 'left').a.text
        
        
            #Extract Opp
            opp = stat.find('td' , {"data-stat":"opp_id"}, class_ = 'left').a.text
        
       
        
            #Extract MP
            mp = stat.find('td',{"data-stat":["mp",'reason']},class_ = ['right iz','center','right']).text
        
            #Extract FG 
            fg = stat.find('td',{"data-stat":["fg",'reason']},class_ = ['right iz','center','right']).text
        
            # Extract'FGA'
            fga = stat.find('td',{"data-stat":["fga",'reason']},class_ = ['right iz','center','right']).text
        
            # Extract'3P'
            threep = stat.find('td',{"data-stat":["fg3",'reason']},class_ = ['right iz','center','right']).text
        
            # Extract '3PA'
            threepA = stat.find('td',{"data-stat":["fg3a",'reason']},class_ = ['right iz','center','right']).text
       
            # Extract '3P%'
            threepP = stat.find('td',{"data-stat":["fg3_pct",'reason']},class_ = ['right iz','center','right']).text
       
            # Extract 'TRB'
            trb = stat.find('td',{"data-stat":["trb",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'AST'
            ast = stat.find('td',{"data-stat":["ast",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'STL'
            stl = stat.find('td',{"data-stat":["stl",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'BLK'
            blk = stat.find('td',{"data-stat":["blk",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'TOV'
            tov = stat.find('td',{"data-stat":["tov",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'PTS'
            pts = stat.find('td',{"data-stat":["pts",'reason']},class_ = ['right iz','center','right']).text

        
            print(date,opp,mp,fg,fga,threep,threepA,threepP,trb,ast,stl,blk,tov,pts)

            #Add to excel file
            sheet.append([date,opp,mp,fg,fga,threep,threepA,threepP,trb,ast,stl,blk,tov,pts])
        
##############################################################################################################################   
    
    #We need to extract the playoff data seperatly since its a dynamic data set
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)

        time.sleep(5) 

        html = driver.page_source

        soup = BeautifulSoup(html , 'html.parser')



        stats = soup.find('div',{'id':"all_pgl_basic_playoffs"} , class_ = "table_wrapper").find('tbody').find_all('tr',class_=None)
    
    

        #Loop trough the parsed HTML to extract statisics
        for stat in stats:

            #Extract Date
            date = stat.find('td' , class_ = 'left').a.text
        
        
            #Extract Opp
            opp = stat.find('td' , {"data-stat":"opp_id"}, class_ = 'left').a.text
        
       
        
            #Extract MP
            mp = stat.find('td',{"data-stat":["mp",'reason']},class_ = ['right iz','center','right']).text
        
            #Extract FG 
            fg = stat.find('td',{"data-stat":["fg",'reason']},class_ = ['right iz','center','right']).text
        
            # Extract'FGA'
            fga = stat.find('td',{"data-stat":["fga",'reason']},class_ = ['right iz','center','right']).text
        
            # Extract'3P'
            threep = stat.find('td',{"data-stat":["fg3",'reason']},class_ = ['right iz','center','right']).text
        
            # Extract '3PA'
            threepA = stat.find('td',{"data-stat":["fg3a",'reason']},class_ = ['right iz','center','right']).text
       
            # Extract '3P%'
            threepP = stat.find('td',{"data-stat":["fg3_pct",'reason']},class_ = ['right iz','center','right']).text
       
            # Extract 'TRB'
            trb = stat.find('td',{"data-stat":["trb",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'AST'
            ast = stat.find('td',{"data-stat":["ast",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'STL'
            stl = stat.find('td',{"data-stat":["stl",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'BLK'
            blk = stat.find('td',{"data-stat":["blk",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'TOV'
            tov = stat.find('td',{"data-stat":["tov",'reason']},class_ = ['right iz','center','right']).text
            # Extract 'PTS'
            pts = stat.find('td',{"data-stat":["pts",'reason']},class_ = ['right iz','center','right']).text

        
            print(date,opp,mp,fg,fga,threep,threepA,threepP,trb,ast,stl,blk,tov,pts)
            sheet.append([date,opp,mp,fg,fga,threep,threepA,threepP,trb,ast,stl,blk,tov,pts])

        excel.save(title_xlsxfile)


    
    except Exception as e:
        print(e)
