import lxml
from bs4 import BeautifulSoup
import requests

class Anime:

    def __init__(self):
        self.dict = "Use info method to get info on an anime"
    
    def __str__(self):
        return self.dict
        
    def search(self,query,searchresult=3,page=1):
        self.searchResult = animesearch(query,searchresult,page)
        return self.searchResult

    def info(self,query):
        self.dict = animeinfo(query)
        try:self.synonyms = self.dict["Synonyms"]
        except:pass
        try:self.title = self.dict['title']
        except:pass
        try:self.titleJa = self.dict['Japanese']
        except:pass
        try:self.titleEn = self.dict['English']
        except:pass
        try:self.type = self.dict['Type']
        except:pass
        try:self.episodes = self.dict['Episodes']
        except:pass
        try:self.status = self.dict['Status']
        except:pass
        try:self.aired = self.dict['Aired']
        except:pass
        try:self.producers = self.dict['Producers']
        except:pass
        try:self.licensors = self.dict['Licensors']
        except:pass
        try:self.studio = self.dict['Studios']
        except:pass
        try:self.source = self.dict['Source']
        except:pass
        try:self.genre = self.dict['Genres']
        except:pass
        try:self.duration = self.dict['Duration']
        except:pass
        try:self.rating = self.dict['Rating']
        except:pass
        try:self.score = self.dict['Score'][:5]
        except:pass
        try:self.rank = self.dict['Ranked'][:-97]
        except:pass
        try:self.popularity = self.dict['Popularity']
        except:pass
        try:self.members = self.dict["Members"]
        except:pass
        try:self.favorites = self.dict['Favorites']
        except:pass
        try:self.synopsis = self.dict['synopsis']
        except:pass
        try:self.imageurl = self.dict['image']
        except:pass

    def infoByID(self,query):
        self.dict = animeinfoID(query)
        try:self.synonyms = self.dict["Synonyms"]
        except:pass
        try:self.title = self.dict['title']
        except:pass
        try:self.titleJa = self.dict['Japanese']
        except:pass
        try:self.titleEn = self.dict['English']
        except:pass
        try:self.type = self.dict['Type']
        except:pass
        try:self.episodes = self.dict['Episodes']
        except:pass
        try:self.status = self.dict['Status']
        except:pass
        try:self.aired = self.dict['Aired']
        except:pass
        try:self.producers = self.dict['Producers']
        except:pass
        try:self.licensors = self.dict['Licensors']
        except:pass
        try:self.studio = self.dict['Studios']
        except:pass
        try:self.source = self.dict['Source']
        except:pass
        try:self.genre = self.dict['Genres']
        except:pass
        try:self.duration = self.dict['Duration']
        except:pass
        try:self.rating = self.dict['Rating']
        except:pass
        try:self.score = self.dict['Score'][:5]
        except:pass
        try:self.rank = self.dict['Ranked'][:-97]
        except:pass
        try:self.popularity = self.dict['Popularity']
        except:pass
        try:self.members = self.dict["Members"]
        except:pass
        try:self.favorites = self.dict['Favorites']
        except:pass
        try:self.synopsis = self.dict['synopsis']
        except:pass
        try:self.imageurl = self.dict['image']
        except:pass
class Manga():
    
    def __init__(self):
        self.dict = "Use info method to get info on an manga"

    def __str__(self):
        return self.dict

    def search(self,query,searchresult=3,page=1):
        self.searchResult = mangasearch(query,searchresult,page)
        return self.searchResult

    def info(self,query):
        self.dict = mangainfo(query)
        try:self.synonyms = self.dict["Synonyms"]
        except:pass
        try:self.title = self.dict["title"]
        except:pass
        try:self.titleJa = self.dict['Japanese']
        except:pass
        try:self.titleEn = self.dict['English']
        except:pass
        try:self.chapters = self.dict["Chapters"]
        except:pass
        try:self.type = self.dict['Type']
        except:pass
        try:self.chapters = self.dict['Chapters']
        except:pass
        try:self.status = self.dict['Status']
        except:pass
        try:self.published = self.dict['Published']
        except:pass
        try:self.genre = self.dict['Genres']
        except:pass
        try:self.serialization = self.dict["Serialization"]
        except:pass
        try:self.score = self.dict['Score'][:5]
        except:pass
        try:self.rank = self.dict['Ranked'][:-76]
        except:pass
        try:self.popularity = self.dict['Popularity']
        except:pass
        try:self.members = self.dict["Members"]
        except:pass
        try:self.favorites = self.dict['Favorites']
        except:pass
        try:self.synopsis = self.dict['synopsis']
        except:pass
        try:self.imageurl = self.dict['image']
        except:pass
        try:self.author = self.dict["Authors"]
        except:pass

    def infoByID(self,query):
        self.dict = mangainfoID(query)
        try:self.synonyms = self.dict["Synonyms"]
        except:pass
        try:self.title = self.dict["title"]
        except:pass
        try:self.titleJa = self.dict['Japanese']
        except:pass
        try:self.titleEn = self.dict['English']
        except:pass
        try:self.chapters = self.dict["Chapters"]
        except:pass
        try:self.type = self.dict['Type']
        except:pass
        try:self.chapters = self.dict['Chapters']
        except:pass
        try:self.status = self.dict['Status']
        except:pass
        try:self.published = self.dict['Published']
        except:pass
        try:self.genre = self.dict['Genres']
        except:pass
        try:self.serialization = self.dict["Serialization"]
        except:pass
        try:self.score = self.dict['Score'][:5]
        except:pass
        try:self.rank = self.dict['Ranked'][:-76]
        except:pass
        try:self.popularity = self.dict['Popularity']
        except:pass
        try:self.members = self.dict["Members"]
        except:pass
        try:self.favorites = self.dict['Favorites']
        except:pass
        try:self.synopsis = self.dict['synopsis']
        except:pass
        try:self.imageurl = self.dict['image']
        except:pass
        try:self.author = self.dict["Authors"]
        except:pass

class SearchResult:

    def __init__(self,title,link,id):
        self.title = title
        self.link = link
        self.id = id
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title

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
    anime_lst = []
    for title in soup.find_all('div',class_='title')[:searchresult]:
        anime_lst.append(SearchResult(title.a.text,title.a['href'],title.a['href'].split('/')[-2]))

    return anime_lst
#returns a dictionary in this form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}


#scraping anime info from particular anime page
#pass myanimelist anime link to scrape info
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
    title = soup.find('h1',class_='title-name h1_bold_none')
    for info in anime:
        try:
            anime_dict[info.span.text.replace(':','')] = info.text.replace('\n','').replace(info.span.text,'').strip()
            if info.span.text == 'Genres:':
                genre = ''
                for i in soup.find_all('span',attrs={"itemprop":'genre'}):
                    genre += i.text.strip()+', '
                anime_dict['Genres'] = genre[:-2]
            if info.span.text == 'Score:':
                anime_dict[info.span.text.replace(':','')] = anime_dict[info.span.text][:5] 
        except:
            pass

    try:
        anime_dict['synopsis'] = soup.find('p',attrs={"itemprop":'description'}).text.replace('\n','').replace('\r','').replace('[Written by MAL Rewrite]','').replace('"','').replace('\\','')
    except:
        pass

    try:anime_dict['title'] = title.text
    except:pass

    try:
        anime_dict['image'] = image.a.contents[1]['data-src']
    except:
        pass
    return anime_dict
#returns a dictionary with all the available info about the anime

#scraping anime info from particular anime page
#pass myanimelist anime ID to scrape info
def animeinfoID(query):
    try:
        req = requests.get("https://myanimelist.net/anime/"+str(query))
    except Exception as e:
        print("Invalid request")
        print(e)
        return

    soup = BeautifulSoup(req.text,'lxml')
    anime = soup.find_all('div',class_='spaceit_pad')
    anime_dict = {}
    image = soup.find('div',class_='leftside')
    title = soup.find('h1',class_='title-name h1_bold_none')

    for info in anime:
        try:
            anime_dict[info.span.text.replace(':','')] = info.text.replace('\n','').replace(info.span.text,'').strip()
            if info.span.text == 'Genres:':
                genre = ''
                for i in soup.find_all('span',attrs={"itemprop":'genre'}):
                    genre += i.text.strip()+', '
                anime_dict['Genres'] = genre[:-2]
            if info.span.text == 'Score:':
                anime_dict[info.span.text.replace(':','')] = anime_dict[info.span.text][:5]
        except:
            pass

    try:
        anime_dict['synopsis'] = soup.find('p',attrs={"itemprop":'description'}).text.replace('\n','').replace('\r','').replace('[Written by MAL Rewrite]','').replace('"','').replace('\\','')
    except:
        pass

    try:anime_dict['title'] = title.text
    except:pass

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
    manga_lst = []
    for manga in soup.find_all('a',class_="hoverinfo_trigger fw-b")[:searchresult]:
        manga_lst.append(SearchResult(manga.text,manga["href"],manga["href"].split('/')[-2]))
    return manga_lst
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
    title = soup.find('span',class_='h1-title')

    manga_dict = {}
    for info in manga:
        try:
            manga_dict[info.span.text.replace(":","")] = info.text.replace('\n','').replace(info.span.text,'').strip()
            if info.span.text == 'Genres:':
                genre = ''
                for i in soup.find_all('span',attrs={"itemprop":'genre'}):
                    genre += i.text.strip()+', '
                manga_dict['Genres'] = genre[:-2]
            if info.span.text == 'Score:':
                manga_dict[info.span.text] = manga_dict[info.span.text][:5] 
        except:
            pass
    
    try:
        manga_dict['synopsis'] = soup.find('span',attrs={"itemprop":'description'}).text.replace('\n','').replace('\r','').replace('[Written by MAL Rewrite]','').replace('"','').replace('\\','')
    except:
        pass

    try:manga_dict['title'] = title.text
    except:pass
    
    try:
        manga_dict['image'] = image.a.contents[0]["data-src"]
    except:
        pass
    return manga_dict
#returns a dictionary with all the available info about the manga

#scraping manga info from particular manga page
#pass myanimelist manga ID to scrape info
def mangainfoID(query):
    try:
        req = requests.get("https://myanimelist.net/manga/"+query)
    except Exception as e:
        print("Invalid request")
        print(e)
        return
    soup = BeautifulSoup(req.text,'lxml')
    manga = soup.find_all("div",class_="spaceit_pad")
    image = soup.find('div',class_='leftside')
    title = soup.find('span',class_='h1-title')

    manga_dict = {}
    for info in manga:
        try:
            manga_dict[info.span.text.replace(":","")] = info.text.replace('\n','').replace(info.span.text,'').strip()
            if info.span.text == 'Genres:':
                genre = ''
                for i in soup.find_all('span',attrs={"itemprop":'genre'}):
                    genre += i.text.strip()+', '
                manga_dict['Genres'] = genre[:-2]
            if info.span.text == 'Score:':
                manga_dict[info.span.text] = manga_dict[info.span.text][:5]
        except:
            pass

    try:
        manga_dict['synopsis'] = soup.find('span',attrs={"itemprop":'description'}).text.replace('\n','').replace('\r','').replace('[Written by MAL Rewrite]','').replace('"','').replace('\\','')
    except:
        pass

    try:manga_dict['title'] = title.text
    except:pass

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
    top_lst = []
    for j  in details_div:
        i = j.find('a')
        top_lst.append(SearchResult(i.text,i['href'],i['href'].split('/')[-2]))
    return top_lst
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
    top_lst = []
    for j  in details_div:
        i = j.find('a')
        top_lst.append(SearchResult(i.text,i['href'],i['href'].split('/')[-2]))
    return top_lst
#returns a dictionary in form {"title 1":"link 1","title 2":"link 2","title 3":"link 3"....}
