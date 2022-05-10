# myanimelist-scraper-py
Unofficial myanimelist scraper
 
  
## Anime

### Example
```python
anime = Anime()

anime.search("Demon slayer")
#creates and returns a new atrribute searchResult = [Kimetsu no Yaiba, Kimetsu no Yaiba Movie: Mugen Ressha-hen, Kimetsu no Yaiba: Mugen Ressha-hen]
#each element in the list has 3 attributes, title, id and link
#search method has 2 optional parameters anime.search(searchQuery,searchresult=3,page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)

anime.info(anime.searchResult[0].link)
#OR
anime.infoByID(anime.searchResult[0].id)
#This creates 20 attributes (aired, episodes, imageurl, members, rank, status, titleEn, favorites, popularity, rating, studio, titleJa, duration, genre, licensors, producers, score, source, synopsis, type)
#And a dictionary attribute called dict = {'Synonyms': 'Blade of Demon Destruction', 'Japanese': '鬼滅の刃', 'English': 'Demon Slayer: Kimetsu no Yaiba', 'German': 'Demon Slayer', 'Spanish': 'Guardianes De La Noche: Kimetsu no Yaiba', 'French': 'Demon Slayer', 'Type': 'TV', 'Episodes': '26', 'Status': 'Finished Airing', 'Aired': 'Apr 6, 2019 to Sep 28, 2019', 'Premiered': 'Spring 2019', 'Broadcast': 'Saturdays at 23:30 (JST)', 'Producers': 'Aniplex,       Shueisha', 'Licensors': 'Aniplex of America', 'Studios': 'ufotable', 'Source': 'Manga', 'Genres': 'Action, Fantasy, Historical, Shounen', 'Theme': 'HistoricalHistorical', 'Demographic': 'ShounenShounen', 'Duration': '23 min. per ep.', 'Rating': 'R - 17+ (violence & profanity)', 'Score': '8.551 (scored by 16671281,667,128 users)      1          indicates a weighted score.', 'Ranked': "#9022    based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.", 'Popularity': '#9', 'Members': '2,403,420', 'Favorites': '79,305', 'synopsis': "Ever since the death of his father, the burden of supporting the family has fallen upon Tanjirou Kamado's shoulders. Though living impoverished on a remote mountain, the Kamado family are able to enjoy a relatively peaceful and happy life. One day, Tanjirou decides to go down to the local village to make a little money selling charcoal. On his way back, night falls, forcing Tanjirou to take shelter in the house of a strange man, who warns him of the existence of flesh-eating demons that lurk in the woods at night.When he finally arrives back home the next day, he is met with a horrifying sight—his whole family has been slaughtered. Worse still, the sole survivor is his sister Nezuko, who has been turned into a bloodthirsty demon. Consumed by rage and hatred, Tanjirou swears to avenge his family and stay by his only remaining sibling. Alongside the mysterious group calling themselves the Demon Slayer Corps, Tanjirou will do whatever it takes to slay the demons and protect the remnants of his beloved sister's humanity.", 'image': 'https://cdn.myanimelist.net/images/anime/1286/99889.jpg'}

print(anime.episodes) #prints '26'

```


## List of functions
- animesearch
- animeinfo
- animeinfoID
- mangasearch
- mangainfo
- topanime
- topmanga

## Usage
### animesearch

```python

#syntax
#animesearch(searchQuery,searchresult=3,page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)

#returns [One Piece Movie 01, One Piece Film: Gold, One Piece Film: Z]
#each element in the list has 3 attributes, title, id and link
```
```python
animesearch("One piece")
```

### animeinfo

```python
#syntax
#animeinfo(animeLink)
#animeLink is link to the anime on myanimelist

#returns {'Japanese': 'ヴィンランド・サガ', 'Type': 'TV', 'Episodes': '24', 'Status': 'Finished Airing', 'Aired': 'Jul 8, 2019 to Dec 30, 2019', 'Premiered': 'Summer 2019', 'Broadcast': 'Mondays at 00:10 (JST)', 'Producers': 'Production I.G,       Dentsu,       Kodansha,       Twin Engine', 'Licensors': 'Sentai Filmworks', 'Studios': 'Wit Studio', 'Source': 'Manga', 'Genres': 'Action, Adventure, Drama, Historical, Seinen', 'Theme': 'HistoricalHistorical', 'Demographic': 'SeinenSeinen', 'Duration': '24 min. per ep.', 'Rating': 'R - 17+ (violence & profanity)', 'Score': '8.731 (scored by 588785588,785 users)      1          indicates a weighted score.', 'Ranked': "#4322    based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.", 'Popularity': '#102', 'Members': '1,082,740', 'Favorites': '31,939', 'synopsis': "Young Thorfinn grew up listening to the stories of old sailors that had traveled the ocean and reached the place of legend, Vinland. It's said to be warm and fertile, a place where there would be no need for fighting—not at all like the frozen village in Iceland where he was born, and certainly not like his current life as a mercenary. War is his home now. Though his father once told him, You have no enemies, nobody does. There is nobody who it's okay to hurt, as he grew, Thorfinn knew that nothing was further from the truth.The war between England and the Danes grows worse with each passing year. Death has become commonplace, and the viking mercenaries are loving every moment of it. Allying with either side will cause a massive swing in the balance of power, and the vikings are happy to make names for themselves and take any spoils they earn along the way. Among the chaos, Thorfinn must take his revenge and kill Askeladd, the man who murdered his father. The only paradise for the vikings, it seems, is the era of war and death that rages on.", 'image': 'https://cdn.myanimelist.net/images/anime/1500/103005.jpg'}
```
```python
animeinfo('https://myanimelist.net/anime/37521/Vinland_Saga')
```

### animeinfoID

```python
#syntax
#animeinfoID(animeID)
#animeID is ID of anime on myanimelist

#returns {'Japanese': 'ヴィンランド・サガ', 'Type': 'TV', 'Episodes': '24', 'Status': 'Finished Airing', 'Aired': 'Jul 8, 2019 to Dec 30, 2019', 'Premiered': 'Summer 2019', 'Broadcast': 'Mondays at 00:10 (JST)', 'Producers': 'Production I.G,       Dentsu,       Kodansha,       Twin Engine', 'Licensors': 'Sentai Filmworks', 'Studios': 'Wit Studio', 'Source': 'Manga', 'Genres': 'Action, Adventure, Drama, Historical, Seinen', 'Theme': 'HistoricalHistorical', 'Demographic': 'SeinenSeinen', 'Duration': '24 min. per ep.', 'Rating': 'R - 17+ (violence & profanity)', 'Score': '8.731 (scored by 588785588,785 users)      1          indicates a weighted score.', 'Ranked': "#4322    based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.", 'Popularity': '#102', 'Members': '1,082,740', 'Favorites': '31,939', 'synopsis': "Young Thorfinn grew up listening to the stories of old sailors that had traveled the ocean and reached the place of legend, Vinland. It's said to be warm and fertile, a place where there would be no need for fighting—not at all like the frozen village in Iceland where he was born, and certainly not like his current life as a mercenary. War is his home now. Though his father once told him, You have no enemies, nobody does. There is nobody who it's okay to hurt, as he grew, Thorfinn knew that nothing was further from the truth.The war between England and the Danes grows worse with each passing year. Death has become commonplace, and the viking mercenaries are loving every moment of it. Allying with either side will cause a massive swing in the balance of power, and the vikings are happy to make names for themselves and take any spoils they earn along the way. Among the chaos, Thorfinn must take his revenge and kill Askeladd, the man who murdered his father. The only paradise for the vikings, it seems, is the era of war and death that rages on.", 'image': 'https://cdn.myanimelist.net/images/anime/1500/103005.jpg'}
```
```python
animeinfoID(37521)
```

### mangasearch

```python
#syntax
#mangasearch(searchQuery,searchresult=3,page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)

#returns {'Jujutsu Kaisen': 'https://myanimelist.net/manga/113138/Jujutsu_Kaisen', 'Jujutsu Kaisen 0: Tokyo Toritsu Jujutsu Koutou Senmon Gakkou': 'https://myanimelist.net/manga/115710/Jujutsu_Kaisen_0__Tokyo_Toritsu_Jujutsu_Koutou_Senmon_Gakkou', 'Jujutsu Kaisen: Yoake no Ibara Michi': 'https://myanimelist.net/manga/133048/Jujutsu_Kaisen__Yoake_no_Ibara_Michi'}
```
```python
mangasearch("Jujutsu kaisen")
```

### mangainfo

```python
#syntax
#mangainfo(mangaLink)
#mangaLink is link to the manga on myanimelist

#returns {'Synonyms:': 'Blade of Demon Destruction', 'Japanese:': '鬼滅の刃', 'English:': 'Demon Slayer: Kimetsu no Yaiba', 'German:': 'Demon Slayer - Kimetsu no Yaiba', 'Spanish:': 'Guardianes de la noche', 'French:': 'Demon Slayer', 'Type:': 'Manga', 'Volumes:': '23', 'Chapters:': '207', 'Status:': 'Finished', 'Published:': 'Feb  15, 2016 to May  18, 2020', 'Genres:': 'Action, Fantasy, Historical, Shounen', 'Theme:': 'Historical                Historical', 'Demographic:': 'Shounen                Shounen', 'Serialization:': 'Shounen Jump (Weekly)', 'Authors:': 'Gotouge, Koyoharu (Story & Art)', 'Score:': '8.301', 'Ranked:': "#2812 2 based on the top manga page. Please note that 'R18+' titles are excluded.", 'Popularity:': '#12', 'Members:': '328,103', 'Favorites:': '24,764', 'synopsis': "Tanjirou Kamado lives with his impoverished family on a remote mountain. As the oldest sibling, he took upon the responsibility of ensuring his family's livelihood after the death of his father. On a cold winter day, he goes down to the local village in order to sell some charcoal. As dusk falls, he is forced to spend the night in the house of a curious man who cautions him of strange creatures that roam the night: malevolent demons who crave human flesh.When he finally makes his way home, Tanjirou's worst nightmare comes true. His entire family has been brutally slaughtered with the sole exception of his sister Nezuko, who has turned into a flesh-eating demon. Engulfed in hatred and despair, Tanjirou desperately tries to stop Nezuko from attacking other people, setting out on a journey to avenge his family and find a way to turn his beloved sister back into a human.", 'image': 'https://cdn.myanimelist.net/images/manga/3/179023.jpg'}
```
```python
mangainfo('https://myanimelist.net/manga/96792/Kimetsu_no_Yaiba')
```

### topanime
```python
#syntax
#topanime(searchresult=3,type='',page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)
#type is type of top anime list, possible values for type is: airing, upcoming, tv, movie, ova, ona, special, bypopularity, favorite or an empty string for overall top anime list

#returns {'Spy x Family': 'https://myanimelist.net/anime/50265/Spy_x_Family', 'Kaguya-sama wa Kokurasetai: Ultra Romantic': 'https://myanimelist.net/anime/43608/Kaguya-sama_wa_Kokurasetai__Ultra_Romantic', 'Kingdom 4th Season': 'https://myanimelist.net/anime/50160/Kingdom_4th_Season', 'One Piece': 'https://myanimelist.net/anime/21/One_Piece', 'Paripi Koumei': 'https://myanimelist.net/anime/50380/Paripi_Koumei'}
```
```python
topanime(5,'airing',1)
```

### topmanga
```python
#syntax
#topmanga(searchresult=3,type='',page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)
#type is type of top manga list, possible values for type: manga, oneshots, doujin, lightnovels, novels, manhwa, manhua, bypopularity, favorite or an empty string for overall top

#returns {'Monogatari Series: First Season': 'https://myanimelist.net/manga/14893/Monogatari_Series__First_Season', 'Monogatari Series: Second Season': 'https://myanimelist.net/manga/23751/Monogatari_Series__Second_Season', 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e': 'https://myanimelist.net/manga/89357/Youkoso_Jitsuryoku_Shijou_Shugi_no_Kyoushitsu_e', 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e: 2-nensei-hen': 'https://myanimelist.net/manga/123992/Youkoso_Jitsuryoku_Shijou_Shugi_no_Kyoushitsu_e__2-nensei-hen', 'Ookami to Koushinryou': 'https://myanimelist.net/manga/9115/Ookami_to_Koushinryou'}
```
```python
topmanga(5,'lightnovels')

```

