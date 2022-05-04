# myanimelist-scraper-py
Unofficial myanimelist scraper

## List of functions
- animesearch
- animeinfo
- mangasearch
- mangainfo
- topanime

## Usage
### animesearch

```python

#syntax
#animesearch(searchQuery,searchresult=3,page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)

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
#mangasearch(searchQuery,searchresult=3,page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)

#returns {'Jujutsu Kaisen': 'https://myanimelist.net/manga/113138/Jujutsu_Kaisen', 'Jujutsu Kaisen 0: Tokyo Toritsu Jujutsu Koutou Senmon Gakkou': 'https://myanimelist.net/manga/115710/Jujutsu_Kaisen_0__Tokyo_Toritsu_Jujutsu_Koutou_Senmon_Gakkou', 'Jujutsu Kaisen: Yoake no Ibara Michi': 'https://myanimelist.net/manga/133048/Jujutsu_Kaisen__Yoake_no_Ibara_Michi'}
mangasearch("Jujutsu kaisen")
```

### mangainfo

```python
#syntax
#mangainfo(mangaLink)
#mangaLink is link to the manga on myanimelist

#returns {'Synonyms:': 'Blade of Demon Destruction', 'Japanese:': '鬼滅の刃', 'English:': 'Demon Slayer: Kimetsu no Yaiba', 'German:': 'Demon Slayer - Kimetsu no Yaiba', 'Spanish:': 'Guardianes de la noche', 'French:': 'Demon Slayer', 'Type:': 'Manga', 'Volumes:': '23', 'Chapters:': '207', 'Status:': 'Finished', 'Published:': 'Feb  15, 2016 to May  18, 2020', 'Genres:': 'Action, Fantasy, Historical, Shounen', 'Theme:': 'Historical                Historical', 'Demographic:': 'Shounen                Shounen', 'Serialization:': 'Shounen Jump (Weekly)', 'Authors:': 'Gotouge, Koyoharu (Story & Art)', 'Score:': '8.301', 'Ranked:': "#2812 2 based on the top manga page. Please note that 'R18+' titles are excluded.", 'Popularity:': '#12', 'Members:': '328,103', 'Favorites:': '24,764', 'synopsis': "Tanjirou Kamado lives with his impoverished family on a remote mountain. As the oldest sibling, he took upon the responsibility of ensuring his family's livelihood after the death of his father. On a cold winter day, he goes down to the local village in order to sell some charcoal. As dusk falls, he is forced to spend the night in the house of a curious man who cautions him of strange creatures that roam the night: malevolent demons who crave human flesh.When he finally makes his way home, Tanjirou's worst nightmare comes true. His entire family has been brutally slaughtered with the sole exception of his sister Nezuko, who has turned into a flesh-eating demon. Engulfed in hatred and despair, Tanjirou desperately tries to stop Nezuko from attacking other people, setting out on a journey to avenge his family and find a way to turn his beloved sister back into a human.", 'image': 'https://cdn.myanimelist.net/images/manga/3/179023.jpg'}

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


topanime(5,'airing',1)
```


