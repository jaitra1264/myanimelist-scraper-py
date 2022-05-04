from re import search
import lxml
from bs4 import BeautifulSoup
import requests

#scraping anime search results
def animesearch(query,searchresult=3,page=1):
    if searchresult >= 49:
        searchresult = 49
    try:
        req = requests.get('https://myanimelist.net/anime.php?cat=anime&q='+query+'&show='+str((page-1)*50))
    except Exception as e:
        print("Invalid request")
        print(e)
        return

    soup = BeautifulSoup(req.text,'lxml')
    anime_dict = {}
    for title in soup.find_all('div',class_='title')[:searchresult]:
        anime_dict[title.a.text] = title.a['href']
    return anime_dict
#returns a dictionary in this form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}


#scraping anime info from particular anime page
def animeinfo(query):
    try:
        req = requests.get(query)
    except Exception as e:
        print("Invalid request")
        print(e)
        return

    soup = BeautifulSoup(req.text,'lxml')
    anime = soup.find_all('div',class_='spaceit_pad')
    anime_dict = {}
    image = soup.find('div',class_='leftside')
    
    for info in anime:
        try:
            anime_dict[info.span.text] = info.text.replace('\n','').replace(info.span.text,'').strip()
            if info.span.text == 'Genres:':
                genre = ''
                for i in soup.find_all('span',attrs={"itemprop":'genre'}):
                    genre += i.text.strip()+', '
                anime_dict['Genres:'] = genre[:-2]
            if info.span.text == 'Score:':
                anime_dict[info.span.text] = anime_dict[info.span.text][:5] 
        except:
            pass

    try:
        anime_dict['synopsis'] = soup.find('p',attrs={"itemprop":'description'}).text.replace('\n','').replace('\r','').replace('[Written by MAL Rewrite]','').replace('"','').replace('\\','')
    except:
        pass

    try:
        anime_dict['image'] = image.a.contents[1]['data-src']
    except:
        pass
    return anime_dict
#returns a dictionary with all the available info about the anime

#scraping manga search results
def mangasearch(query,searchresult=3,page=1):
    if searchresult >= 49:
        searchresult = 49
    try:
        req = requests.get('https://myanimelist.net/manga.php?cat=manga&q='+query+'&show='+str((page-1)*50))
    except Exception as e:
        print("Invalid request")
        print(e)
        return

    soup = BeautifulSoup(req.text,'lxml')
    manga_dict = {}
    for i in soup.find_all('a',class_="hoverinfo_trigger fw-b")[:searchresult]:
        manga_dict[i.text] = i["href"]
    return manga_dict
#returns a dictionary in this form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}


#scraping manga info from particular manga page
def mangainfo(query):
    try:
        req = requests.get(query)
    except Exception as e:
        print("Invalid request")
        print(e)
        return
    soup = BeautifulSoup(req.text,'lxml')
    manga = soup.find_all("div",class_="spaceit_pad")
    image = soup.find('div',class_='leftside')

    manga_dict = {}
    for info in manga:
        try:
            manga_dict[info.span.text] = info.text.replace('\n','').replace(info.span.text,'').strip()
            if info.span.text == 'Genres:':
                genre = ''
                for i in soup.find_all('span',attrs={"itemprop":'genre'}):
                    genre += i.text.strip()+', '
                manga_dict['Genres:'] = genre[:-2]
            if info.span.text == 'Score:':
                manga_dict[info.span.text] = manga_dict[info.span.text][:5] 
        except:
            pass
    
    try:
        manga_dict['synopsis'] = soup.find('span',attrs={"itemprop":'description'}).text.replace('\n','').replace('\r','').replace('[Written by MAL Rewrite]','').replace('"','').replace('\\','')
    except:
        pass
    
    try:
        manga_dict['image'] = image.a.contents[0]["data-src"]
    except:
        pass
    return manga_dict
#returns a dictionary with all the available info about the manga


#scraping top anime list
#search result maximum value 49
#possible values for type: airing, upcoming, tv, movie, ova, ona, special, bypopularity, favorite or an empty string for overall top
def topanime(searchresult=3,type='',page=1):
    if searchresult >= 49:
        searchresult = 49
    try:
        req = requests.get("https://myanimelist.net/topanime.php?type="+ type + '&limit='+str((page-1)*50))
    except Exception as e:
        print("Invalid request")
        print(e)
    soup = BeautifulSoup(req.text,'lxml')
    details_div = soup.find_all('div',class_='detail')[:searchresult]
    top_dict = {}
    for j  in details_div:
        i = j.find('a')
        top_dict[i.text] = i['href']
    return top_dict
#returns a dictionary in form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}

#scraping top manga list
#search result maximum value 49
#possible values for type: manga, oneshots, doujin, lightnovels, novels, manhwa, manhua, bypopularity, favorite or an empty string for overall top
def topmanga(searchresult=3,type='',page=1):
    if searchresult >= 49:
        searchresult = 49
    try:
        req = requests.get("https://myanimelist.net/topmanga.php?type="+ type + '&limit='+str((page-1)*50))
    except Exception as e:
        print("Invalid request")
        print(e)
    soup = BeautifulSoup(req.text,'lxml')
    details_div = soup.find_all('div',class_='detail')[:searchresult]
    top_dict = {}
    for j  in details_div:
        i = j.find('a')
        top_dict[i.text] = i['href']
    return top_dict
#returns a dictionary in form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}