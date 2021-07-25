#!/usr/bin/env python
# coding: utf-8

# In[84]:


##Write a python program to scrape a data for all available Hostels from 
##https://www.hostelworld.com/ in “London” location. You have to scrape hostel name, 
##distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms 
##from price, facilities and property description.


# In[19]:


get_ipython().system('pip install selenium')


# In[20]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import selenium
from PIL import Image
import pandas as pd
import urllib
from selenium import webdriver


# In[148]:


driver=webdriver.Chrome('chromedriver.exe')


# In[ ]:


##Q10. Write a python program to scrape a data for all available Hostels from 
#https://www.hostelworld.com/ in “London” location. You have to scrape hostel name, 
#distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms 
#from price, facilities and property description.


# In[104]:


url='https://www.hostelworld.com//'


# In[147]:


driver.get(url)


# In[106]:


search_loc=driver.find_element_by_id('location-text-input-field')


# In[107]:


search_loc


# In[108]:


search_loc.send_keys('London')


# In[122]:


search_btn=driver.find_element_by_xpath("//div[@class='search-button']")


# In[123]:


search_btn.click()


# In[124]:


search_btn1=driver.find_element_by_id("search-button")


# In[125]:


search_btn1.click()


# In[ ]:


## When i click button website not working


# In[ ]:


##Write a program to extract at least 500 Comments, Comment upvote and time when comment 
##was posted from any YouTube Video?


# In[104]:


URL=('https://www.youtube.com/watch?v=Hr6SAJ5CfYc')


# In[105]:


driver.get(URL)


# In[106]:


##YTC= Youtube
YTC=driver.find_elements_by_xpath("//span[@class='style-scope yt-formatted-string']")


# In[128]:


#YTC


# In[109]:


CommentsList=[]
for z in YTC:
    CommentsList.append(z.text)
CommentsList


# In[110]:


len(CommentsList)


# In[111]:


ToC=driver.find_elements_by_xpath("//a[@class='yt-simple-endpoint style-scope yt-formatted-string']")


# In[127]:


#ToC


# In[113]:


TimeComments=[]
for i in ToC:
    TimeComments.append(i.text)
TimeComments


# In[114]:


len(TimeComments)


# In[115]:


YTU= driver.find_elements_by_class_name('style-scope ytd-toggle-button-renderer')


# In[126]:


#YTU


# In[123]:


UpvotesY=[]
for c in YTU:
    UpvotesY.append(c.text)
UpvotesY


# In[118]:


len(UpvotesY)


# In[120]:


YoutubeData=pd.DataFrame({'Upvotes':UpvotesY[0:370],'Time':TimeComments[0:370],'Comments':CommentsList[0:370]})


# In[121]:


YoutubeData


# In[125]:


##Write a python program to scrape the details for all billionaires from www.forbes.com. 
#Details to be scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, 
#“Industry”.


# In[135]:


url2=('https://www.forbes.com/')


# In[137]:


driver.get(url2)


# In[138]:


BN=driver.find_elements_by_xpath("//div[@class='personName']")


# In[168]:


#BN


# In[140]:


PersonName=[]
for k in BN:
    PersonName.append(k.text)
PersonName


# In[141]:


len(BN)


# In[142]:


Age=driver.find_elements_by_xpath("//div[@class='age']")


# In[167]:


#Age


# In[144]:


AgeList=[]
for j in Age:
    AgeList.append(j.text)
AgeList


# In[145]:


len(AgeList)


# In[146]:


NW=driver.find_elements_by_xpath("//div[@class='netWorth']")


# In[166]:


#NW


# In[148]:


NetWorthList=[]
for m in NW:
    NetWorthList.append(m.text)
NetWorthList


# In[159]:


State=driver.find_elements_by_xpath("//div[@class='state']")


# In[165]:


#State


# In[161]:


StateList=[]
for z in State:
    StateList.append(z.text)
StateList


# In[162]:


Source=driver.find_elements_by_xpath("//div[@class='source']")


# In[164]:


#Source


# In[169]:


SourceList=[]
for l in Source:
    SourceList.append(l.text)
SourceList


# In[171]:


Rank=driver.find_elements_by_xpath("//div[@class='rank']")
#Rank


# In[172]:


RankList=[]
for u in Rank:
    RankList.append(u.text)
RankList


# In[177]:


ForbesData=pd.DataFrame({'Rank':RankList[0:400], 'Person Names':PersonName,'Net Worth':NetWorthList,'Source':SourceList, 'Age': AgeList,'State':StateList})


# In[175]:


print(len(RankList))
print(len(PersonName))
print(len(NetWorthList))
print(len(StateList))
print(len(AgeList))
print(len(SourceList))


# In[178]:


ForbesData


# In[179]:


##Write a program to scrap all the available details of best gaming laptops from digit.in.


# In[22]:


urly='https://www.digit.in/'


# In[23]:


driver.get(urly)


# In[24]:


search=driver.find_element_by_id("globalPageSearchText")


# In[25]:


search


# In[28]:


search.send_keys('Gaming laptops')


# In[32]:


descrp=driver.find_elements_by_xpath("//div[@class='searchProduct-desc']")


# In[33]:


descrp


# In[34]:


for y in descrp:
    print(y.text)


# In[39]:


price=driver.find_elements_by_xpath("//div[@class='Block-price']")
for z in price:
    print(z.text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on 
#google maps

#Not done


# In[ ]:


#Write a python program to access the search bar and search button on images.google.com and 
#scrape 100 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning


# In[188]:


url3='https://images.google.com//'


# In[189]:


driver.get(url3)


# In[191]:


images=driver.find_elements_by_xpath("//div[@class='bRMDJf islir']")
images


# In[198]:


ImagesList=[]
for g in images:
    ImagesList.append(g.text)
ImagesList


# In[199]:


imgResults = driver.find_elements_by_xpath("//img[contains(@class,'Q4LuWd')]")

totalResults=len(imgResults)


# In[ ]:


#Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on 
#www.flipkart.com and scrape following details for all the search results displayed on 1st page. 
#Details to be scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, 
#“Storage(ROM)”, “Primary Camera”, “Secondary Camera”, “Display Size”, “Display 
#Resolution”, “Processor”, “Processor Cores”, “Battery Capacity”, “Price”, “Product URL”. 
#Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe 
#and CSV


# In[149]:


UrlN='https://www.flipkart.com/'


# In[150]:


driver.get(UrlN)


# In[151]:


search_item=driver.find_element_by_xpath("//input[@class='_3704LK']")


# In[152]:


search_item.send_keys('samsung')


# In[153]:


search_btn1=driver.find_element_by_xpath("//button[@class='L0Z3Pu']")


# In[154]:


search_btn1.click()


# In[155]:


Name=driver.find_element_by_xpath("//div[@class='_4rR01T']")


# In[156]:


Name.click()


# In[157]:


Namephone=[Name.text]
Namephone


# In[158]:


price_and_discount =driver.find_element_by_xpath("//div[@class='_25b18c']")


# In[159]:


price_and_discount


# In[160]:


priceanddiscountlist=[price_and_discount.text]
priceanddiscountlist


# In[180]:


features=driver.find_element_by_xpath("//div[@class='_21Ahn-']")
features

##NOT Extracting


# In[ ]:


#Write a program to scrap details of all the funding deals for second quarter (i.e. July 20 –
#September 20) from trak.in


# In[179]:


features.text


# In[ ]:


##7. Write a program to scrap all the available details of best gaming laptops from digit.in7. Write a program to scrap all the available details of best gaming laptops from digit.in


# In[64]:


url5='https://trak.in/'


# In[65]:


driver.get(url5)


# In[101]:


#july 2020
July=driver.find_elements_by_xpath("//div[@class='tablepress-48_wrapper']/td")


# In[102]:


for i in July:
    print(i.text)


# In[ ]:





# In[ ]:




