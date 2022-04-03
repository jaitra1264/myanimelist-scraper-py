from bs4 import BeautifulSoup
import requests

#scraping anime search results
def animesearch(query,searchresult=3,page=0):
    req = requests.get('https://myanimelist.net/anime.php?cat=anime&q='+query+'&show='+str(page*50))
    soup = BeautifulSoup(req.text,'lxml')
    anime_dict = {}
    for title in soup.find_all('div',class_='title')[:searchresult]:
        anime_dict[title.a.text] = title.a['href']
    return anime_dict
#returns a dictionary in this form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}


#scraping anime info from particular anime page
def animeinfo(query):
    req = requests.get(query)
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
def mangasearch(query,searchresult=3,page=0):
    req = requests.get('https://myanimelist.net/manga.php?cat=manga&q='+query+'&show='+str(page*50))
    soup = BeautifulSoup(req.text,'lxml')
    manga_dict = {}
    for i in soup.find_all('a',class_="hoverinfo_trigger fw-b")[:searchresult]:
        manga_dict[i.text] = i["href"]
    return manga_dict
#returns a dictionary in this form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}


#scraping manga info from particular manga page
def mangainfo(query):
    req = requests.get(query)
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
