# myanimelist-scraper-py
Unofficial myanimelist scraper

## List of functions
- animesearch
- animeinfo
- mangasearch
- mangainfo

## Usage
### animesearch

```python

#syntax
#animesearch(searchQuery,searchresult=3,page=0)
#searchresult is the number of searchresults returned (max 50)
#page is the page number of search result by default it is 0 (page 1)

#returns {'One Piece Movie 1': 'https://myanimelist.net/anime/459/One_Piece_Movie_1', 'One Piece Film: Z': 'https://myanimelist.net/anime/12859/One_Piece_Film__Z', 'One Piece Film: Gold': 'https://myanimelist.net/anime/31490/One_Piece_Film__Gold'}
animesearch("One piece")
```

### animeinfo

```python
#syntax
#animeinfo(animeLink)
#animeLink is link to the anime on myanimelist

#returns {'Japanese:': 'ヴィンランド・サガ', 'Type:': 'TV', 'Episodes:': '24', 'Status:': 'Finished Airing', 'Aired:': 'Jul 8, 2019 to Dec 30, 2019', 'Premiered:': 'Summer 2019', 'Broadcast:': 'Mondays at 00:10 (JST)', 'Producers:': 'Production I.G,       Dentsu,       Kodansha,       Twin Engine', 'Licensors:': 'Sentai Filmworks', 'Studios:': 'Wit Studio', 'Source:': 'Manga', 'Genres:': 'Action, Adventure, Drama, Historical, Seinen', 'Theme:': 'HistoricalHistorical', 'Demographic:': 'SeinenSeinen', 'Duration:': '24 min. per ep.', 'Rating:': 'R - 17+ (violence & profanity)', 'Score:': '8.731', 'Ranked:': "#4022    based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.", 'Popularity:': '#104', 'Members:': '1,056,583', 'Favorites:': '30,895', 'synopsis': "Young Thorfinn grew up listening to the stories of old sailors that had traveled the ocean and reached the place of legend, Vinland. It's said to be warm and fertile, a place where there would be no need for fighting—not at all like the frozen village in Iceland where he was born, and certainly not like his current life as a mercenary. War is his home now. Though his father once told him, You have no enemies, nobody does. There is nobody who it's okay to hurt, as he grew, Thorfinn knew that nothing was further from the truth.The war between England and the Danes grows worse with each passing year. Death has become commonplace, and the viking mercenaries are loving every moment of it. Allying with either side will cause a massive swing in the balance of power, and the vikings are happy to make names for themselves and take any spoils they earn along the way. Among the chaos, Thorfinn must take his revenge and kill Askeladd, the man who murdered his father. The only paradise for the vikings, it seems, is the era of war and death that rages on.", 'image': 'https://cdn.myanimelist.net/images/anime/1500/103005.jpg'}
animeinfo('https://myanimelist.net/anime/37521/Vinland_Saga')
```

### mangasearch

```python
#syntax
#mangasearch(searchQuery,searchresult=3,page=0)
#searchresult is the number of searchresults returned (max 50)
#page is the page number of search result by default it is 0 (page 1)

#returns {'Jujutsu Kaisen': 'https://myanimelist.net/manga/113138/Jujutsu_Kaisen', 'Jujutsu Kaisen 0: Tokyo Toritsu Jujutsu Koutou Senmon Gakkou': 'https://myanimelist.net/manga/115710/Jujutsu_Kaisen_0__Tokyo_Toritsu_Jujutsu_Koutou_Senmon_Gakkou', 'Jujutsu Kaisen: Yoake no Ibara Michi': 'https://myanimelist.net/manga/133048/Jujutsu_Kaisen__Yoake_no_Ibara_Michi'}
mangasearch("Jujutsu kaisen")
```

### mangainfo

```python
#syntax
#mangainfo(mangaLink)
#mangaLink is link to the manga on myanimelist

#returns {'Synonyms:': 'Blade of Demon Destruction', 'Japanese:': '鬼滅の刃', 'English:': 'Demon Slayer: Kimetsu no Yaiba', 'German:': 'Demon Slayer - Kimetsu no Yaiba', 'Spanish:': 'Guardianes de la noche', 'French:': 'Demon Slayer', 'Type:': 'Manga', 'Volumes:': '23', 'Chapters:': '207', 'Status:': 'Finished', 'Published:': 'Feb  15, 2016 to May  18, 2020', 'Genres:': 'Action, Fantasy, Historical, Shounen', 'Theme:': 'Historical                Historical', 'Demographic:': 'Shounen                Shounen', 'Serialization:': 'Shounen Jump (Weekly)', 'Authors:': 'Gotouge, Koyoharu (Story & Art)', 'Score:': '8.301', 'Ranked:': "#2722 2 based on the top manga page. Please note that 'R18+' titles are excluded.", 'Popularity:': '#12', 'Members:': '327,696', 'Favorites:': '24,743'}
animeinfo('https://myanimelist.net/manga/96792/Kimetsu_no_Yaiba')
```


