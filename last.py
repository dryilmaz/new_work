from bs4 import BeautifulSoup
import html
import urllib
import urllib.error
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import sys

###########################################
# Open file
###########################################

file = open("source/deneme/22.txt","r")

###########################################
# For loop over file
###########################################
for line in file:
###########################################
# Get url from file
###########################################
    fields = line.split(";")
    links = fields[0]
    url = links
###########################################
# http and server Error
###########################################
    try:
        url_oku = urllib.request.urlopen(links)
    except(HTTPError) as e:
        print(e)
    except URLError:
        print("server down")
    except(ConnectionError):
        print(url_oku+ "time out")
############################################
# code working
############################################
    else:
        #soup = BeautifulSoup(response.read().decode('utf-8'))
        #soup = BeautifulSoup(url_oku,'html.parser')

        soup = BeautifulSoup(url_oku,"lxml")
        try:
            #######################################
            # Name of book
            #######################################

            bName = soup.find('div' ,attrs={'class':'padding'}).find('h1').text
        except:
            bName="Kitap adi belirtilmemis"
        print(bName)

        try:
            #######################################
            # Photo of book
            #######################################
            bPhoto = soup.find('div',attrs={'class':'image-container'}).find('a')
        except:
            bPhoto="noPic"
        print(bPhoto['href'])

        try:
            ######################################
            # publication date
            ######################################
            pubDate = soup.find_all('td',attrs={'itemprop':'datePublished'})[0].get_text()
        except:
            pubDate="Yayınlanma tarihi belirtilmemiş"
        print(pubDate)

        try:
            ######################################
            # price of book
            ######################################
            bPrice = soup.find_all('div',attrs={'class':'middle'})[0].get_text()
        except:
            bPrice="Kitabin fiyati belirtilmemis"
        print(bPrice)

        #try:
            ######################################
            # description
            ######################################
            #descOfBook = soup.find_all('span',attrs={'itemprop':'description'})[0].get_text()
        #except:
            #descOfBook="Kitabin tanimi belirtilmemis"
        #print(descOfBook)
        try:
            descOfBook=soup.find_all('span',attrs={'itemprop':'description'})[0].get_text()
        except(TypeError,IndexError):
            descOfBook=soup.find('span',attrs={'itemprop':'description'}).contents[0].strip()
        if not descOfBook:
            descOfBook="tanim yok"
            print(descOfBook)
        else:
            print(descOfBook)

        try:
            ######################################
            # Number of page
            ######################################
            nPage = soup.find_all('span',attrs={'itemprop':'numberOfPages'})[0].get_text()
        except(IndexError):
            nPage = "Sayfa Sayisi belirtilmemis"
        print(nPage)
        try:
            ###############################333
            #yazar
            ##########################
            wRiter=soup.find_all('span',attrs={'itemprop':'name'})[0].get_text()
        except(IndexError):
            wRiter="yazar belirtilmemis"
        print(wRiter)
        try:
            ######################################
            ##isbn
            ######################################
            isbn=soup.find_all('span',attrs={'itemprop':'isbn'})[0].get_text()
        except(IndexError):
            isbn="isbn belirtilmemiş"
        print(isbn)
        try:
            #####################################
            ##book bookEdition
            #####################################
            bookEdition=soup.find_all('span',attrs={'itemprop':'bookEdition'})[0].get_text()
        except(IndexError):
            bookEdition="basim sayisi belirtilmemiş"
        print(bookEdition)

file.close()
