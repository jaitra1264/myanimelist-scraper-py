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
#This creates 21 attributes (aired, episodes, imageurl, members, rank, status, titleEn, favorites, popularity, rating, studio, titleJa, duration, genre, licensors, producers, score, source, synopsis, type)
#And a dictionary attribute called dict = {'Synonyms': 'Blade of Demon Destruction', 'Japanese': '鬼滅の刃', 'English': 'Demon Slayer: Kimetsu no Yaiba', 'German': 'Demon Slayer', 'Spanish': 'Guardianes De La Noche: Kimetsu no Yaiba', 'French': 'Demon Slayer', 'Type': 'TV', 'Episodes': '26', 'Status': 'Finished Airing', 'Aired': 'Apr 6, 2019 to Sep 28, 2019', 'Premiered': 'Spring 2019', 'Broadcast': 'Saturdays at 23:30 (JST)', 'Producers': 'Aniplex,       Shueisha', 'Licensors': 'Aniplex of America', 'Studios': 'ufotable', 'Source': 'Manga', 'Genres': 'Action, Fantasy, Historical, Shounen', 'Theme': 'HistoricalHistorical', 'Demographic': 'ShounenShounen', 'Duration': '23 min. per ep.', 'Rating': 'R - 17+ (violence & profanity)', 'Score': '8.551 (scored by 16679771,667,977 users)      1          indicates a weighted score.', 'Ranked': "#9022    based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.", 'Popularity': '#9', 'Members': '2,404,709', 'Favorites': '79,354', 'synopsis': "Ever since the death of his father, the burden of supporting the family has fallen upon Tanjirou Kamado's shoulders. Though living impoverished on a remote mountain, the Kamado family are able to enjoy a relatively peaceful and happy life. One day, Tanjirou decides to go down to the local village to make a little money selling charcoal. On his way back, night falls, forcing Tanjirou to take shelter in the house of a strange man, who warns him of the existence of flesh-eating demons that lurk in the woods at night.When he finally arrives back home the next day, he is met with a horrifying sight—his whole family has been slaughtered. Worse still, the sole survivor is his sister Nezuko, who has been turned into a bloodthirsty demon. Consumed by rage and hatred, Tanjirou swears to avenge his family and stay by his only remaining sibling. Alongside the mysterious group calling themselves the Demon Slayer Corps, Tanjirou will do whatever it takes to slay the demons and protect the remnants of his beloved sister's humanity.", 'title': 'Kimetsu no Yaiba', 'image': 'https://cdn.myanimelist.net/images/anime/1286/99889.jpg'}


print(anime.episodes) #prints '26'
```
## Manga
### Example
```python
manga = Manga()

manga.search('fullmetal alchemist')
#creates and returns a new atrribute searchResult = [Fullmetal Alchemist, Fullmetal Alchemist, Full Metal Alchemist: Prototype]
#each element in the list has 3 attributes, title, id and link
#search method has 2 optional parameters manga.search(searchQuery,searchresult=3,page=1)
#searchresult is the number of search results returned (max 49)
#page is the page number of search result by default it is 1 (page 1)

manga.info(manga.searchResult[0].link)
#OR
manga.infoByID(manga.searchResult[0].link)
#This creates 19 attributes (author, chapters, favorites, genre, imageurl, members, popularity, published, rank, score, serialization, status, synonyms, synopsis, title, titleEn, titleJa, type, volumes)
#And a dictionary attribute called dict = {'Synonyms': 'Full Metal Alchemist, Hagane no Renkinjutsushi, FMA, HagaRen, Fullmetal Alchemist Gaiden', 'Japanese': '鋼の錬金術師', 'English': 'Fullmetal Alchemist', 'Type': 'Manga', 'Volumes': '27', 'Chapters': '116', 'Status': 'Finished', 'Published': 'Jul  12, 2001 to Sep  11, 2010', 'Genres': 'Action, Adventure, Award Winning, Drama, Fantasy, Military, Shounen', 'Theme': 'Military                Military', 'Demographic': 'Shounen                Shounen', 'Serialization': 'Shounen Gangan', 'Authors': 'Arakawa, Hiromu (Story & Art)', 'Score': '9.061 (scored by 141168141,168 users)1 indicates a weighted score.', 'Ranked': "#62 2 based on the top manga page. Please note that 'R18+' titles are excluded.", 'Popularity': '#18', 'Members': '259,424', 'Favorites': '28,244', 'synopsis': "Alchemists are knowledgeable and naturally talented individuals who can manipulate and modify matter due to their art. Yet despite the wide range of possibilities, alchemy is not as all-powerful as most would believe. Human transmutation is strictly forbidden, and whoever attempts it risks severe consequences. Even so, siblings Edward and Alphonse Elric decide to ignore this great taboo and bring their mother back to life. Unfortunately, not only do they fail in resurrecting her, they also pay an extremely high price for their arrogance: Edward loses his left leg and Alphonse his entire body. Furthermore, Edward also gives up his right arm in order to seal his brother's soul into a suit of armor.Years later, the young alchemists travel across the country looking for the Philosopher's Stone, in the hopes of recovering their old bodies with its power. However, their quest for the fated stone also leads them to unravel far darker secrets than they could ever imagine.", 'title': 'Fullmetal Alchemist', 'image': 'https://cdn.myanimelist.net/images/manga/3/243675.jpg'}


print(manga.chapters) #prints '116'
```


## List of functions
- animesearch
- animeinfo
- animeinfoID
- mangasearch
- mangainfo
- mangainfoID
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

#returns {'Japanese': 'ヴィンランド・サガ', 'Type': 'TV', 'Episodes': '24', 'Status': 'Finished Airing', 'Aired': 'Jul 8, 2019 to Dec 30, 2019', 'Premiered': 'Summer 2019', 'Broadcast': 'Mondays at 00:10 (JST)', 'Producers': 'Production I.G,       Dentsu,       Kodansha,       Twin Engine', 'Licensors': 'Sentai Filmworks', 'Studios': 'Wit Studio', 'Source': 'Manga', 'Genres': 'Action, Adventure, Drama, Historical, Seinen', 'Theme': 'HistoricalHistorical', 'Demographic': 'SeinenSeinen', 'Duration': '24 min. per ep.', 'Rating': 'R - 17+ (violence & profanity)', 'Score': '8.731 (scored by 588785588,785 users)      1          indicates a weighted score.', 'Ranked': "#4322    based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.", 'Popularity': '#102', 'Members': '1,082,740', 'Favorites': '31,941', 'synopsis': "Young Thorfinn grew up listening to the stories of old sailors that had traveled the ocean and reached the place of legend, Vinland. It's said to be warm and fertile, a place where there would be no need for fighting—not at all like the frozen village in Iceland where he was born, and certainly not like his current life as a mercenary. War is his home now. Though his father once told him, You have no enemies, nobody does. There is nobody who it's okay to hurt, as he grew, Thorfinn knew that nothing was further from the truth.The war between England and the Danes grows worse with each passing year. Death has become commonplace, and the viking mercenaries are loving every moment of it. Allying with either side will cause a massive swing in the balance of power, and the vikings are happy to make names for themselves and take any spoils they earn along the way. Among the chaos, Thorfinn must take his revenge and kill Askeladd, the man who murdered his father. The only paradise for the vikings, it seems, is the era of war and death that rages on.", 'title': 'Vinland Saga', 'image': 'https://cdn.myanimelist.net/images/anime/1500/103005.jpg'}
```

```python
animeinfo('https://myanimelist.net/anime/37521/Vinland_Saga')
```

### animeinfoID

```python
#syntax
#animeinfoID(animeID)
#animeID is ID of anime on myanimelist

#returns {'Japanese': 'ヴィンランド・サガ', 'Type': 'TV', 'Episodes': '24', 'Status': 'Finished Airing', 'Aired': 'Jul 8, 2019 to Dec 30, 2019', 'Premiered': 'Summer 2019', 'Broadcast': 'Mondays at 00:10 (JST)', 'Producers': 'Production I.G,       Dentsu,       Kodansha,       Twin Engine', 'Licensors': 'Sentai Filmworks', 'Studios': 'Wit Studio', 'Source': 'Manga', 'Genres': 'Action, Adventure, Drama, Historical, Seinen', 'Theme': 'HistoricalHistorical', 'Demographic': 'SeinenSeinen', 'Duration': '24 min. per ep.', 'Rating': 'R - 17+ (violence & profanity)', 'Score': '8.731 (scored by 588785588,785 users)      1          indicates a weighted score.', 'Ranked': "#4322    based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.", 'Popularity': '#102', 'Members': '1,082,740', 'Favorites': '31,941', 'synopsis': "Young Thorfinn grew up listening to the stories of old sailors that had traveled the ocean and reached the place of legend, Vinland. It's said to be warm and fertile, a place where there would be no need for fighting—not at all like the frozen village in Iceland where he was born, and certainly not like his current life as a mercenary. War is his home now. Though his father once told him, You have no enemies, nobody does. There is nobody who it's okay to hurt, as he grew, Thorfinn knew that nothing was further from the truth.The war between England and the Danes grows worse with each passing year. Death has become commonplace, and the viking mercenaries are loving every moment of it. Allying with either side will cause a massive swing in the balance of power, and the vikings are happy to make names for themselves and take any spoils they earn along the way. Among the chaos, Thorfinn must take his revenge and kill Askeladd, the man who murdered his father. The only paradise for the vikings, it seems, is the era of war and death that rages on.", 'title': 'Vinland Saga', 'image': 'https://cdn.myanimelist.net/images/anime/1500/103005.jpg'}
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

#returns [Jujutsu Kaisen, Jujutsu Kaisen 0: Tokyo Toritsu Jujutsu Koutou Senmon Gakkou, Jujutsu Kaisen: Yoake no Ibara Michi]
#each element in the list has 3 attributes, title, id and link
```
```python
mangasearch("Jujutsu kaisen")
```

### mangainfo

```python
#syntax
#mangainfo(mangaLink)
#mangaLink is link to the manga on myanimelist

#returns {'Synonyms:': 'Blade of Demon Destruction', 'Japanese:': '鬼滅の刃', 'English:': 'Demon Slayer: Kimetsu no Yaiba', 'German:': 'Demon Slayer - Kimetsu no Yaiba', 'Spanish:': 'Guardianes de la noche', 'French:': 'Demon Slayer', 'Type:': 'Manga', 'Volumes:': '23', 'Chapters:': '207', 'Status:': 'Finished', 'Published:': 'Feb  15, 2016 to May  18, 2020', 'Genres:': 'Action, Fantasy, Historical, Shounen', 'Theme:': 'Historical                Historical', 'Demographic:': 'Shounen                Shounen', 'Serialization:': 'Shounen Jump (Weekly)', 'Authors:': 'Gotouge, Koyoharu (Story & Art)', 'Score:': '8.291', 'Ranked:': "#2932 2 based on the top manga page. Please note that 'R18+' titles are excluded.", 'Popularity:': '#12', 'Members:': '338,597', 'Favorites:': '25,359', 'synopsis': "Tanjirou Kamado lives with his impoverished family on a remote mountain. As the oldest sibling, he took upon the responsibility of ensuring his family's livelihood after the death of his father. On a cold winter day, he goes down to the local village in order to sell some charcoal. As dusk falls, he is forced to spend the night in the house of a curious man who cautions him of strange creatures that roam the night: malevolent demons who crave human flesh.When he finally makes his way home, Tanjirou's worst nightmare comes true. His entire family has been brutally slaughtered with the sole exception of his sister Nezuko, who has turned into a flesh-eating demon. Engulfed in hatred and despair, Tanjirou desperately tries to stop Nezuko from attacking other people, setting out on a journey to avenge his family and find a way to turn his beloved sister back into a human.", 'title': 'Kimetsu no YaibaDemon Slayer: Kimetsu no Yaiba', 'image': 'https://cdn.myanimelist.net/images/manga/3/179023.jpg'}
```

```python
mangainfo('https://myanimelist.net/manga/96792/Kimetsu_no_Yaiba')
```

### mangainfoID

```python 
#syntax
#mangainfoID(mangaID)
#mangaID is ID of manga on myanimelist

#returns {'Synonyms': 'High Kyuu!!, HQ!!, Nisekyuu!!', 'Japanese': 'ハイキュー!!', 'English': 'Haikyu!!', 'German': 'Haikyu!!', 'French': 'Haikyu !! - Les As du volley', 'Type': 'Manga', 'Volumes': '45', 'Chapters': '407', 'Status': 'Finished', 'Published': 'Feb  20, 2012 to Jul  20, 2020', 'Genres': 'Award Winning, Sports, School, Team Sports, Shounen', 'Themes': 'School                School,                    Team Sports                Team Sports', 'Demographic': 'Shounen                Shounen', 'Serialization': 'Shounen Jump (Weekly)', 'Authors': 'Furudate, Haruichi (Story & Art)', 'Score': '8.841 (scored by 8648186,481 users)1 indicates a weighted score.', 'Ranked': "#262 2 based on the top manga page. Please note that 'R18+' titles are excluded.", 'Popularity': '#32', 'Members': '182,356', 'Favorites': '16,019', 'synopsis': "The whistle blows. The ball is up. A dig. A set. A spike.Volleyball. A sport where two teams face off, separated by a formidable, wall-like net.The Little Giant, standing at only 170 cm, overcomes the towering net and the wall of blockers. The awe-inspired Shouyou Hinata looks on at the ace's crow-like figure. Determined to reach great heights like the Little Giant, small-statured Hinata finally manages to form a team in his last year of junior high school, and enters his first volleyball tournament. However, his team is utterly defeated in their first game against the powerhouse school Kitagawa Daiichi, led by the genius, but oppressive setter dubbed the King of the Court, Tobio Kageyama.Hinata enrolls into Karasuno High School seeking  to take revenge against Kageyama in an official high school match and to follow in the Little Giant's footsteps—but his plans are ruined when he opens the gymnasium door to find Kageyama as one of his teammates.Now, Hinata must establish himself on the team and work alongside the problematic Kageyama to overcome his shortcomings and to fulfill his dream of making it to the top of the high school volleyball world.Included one-shot:Volume 14: Nisekyuu!!", 'title': 'Haikyuu!!Haikyu!!', 'image': 'https://cdn.myanimelist.net/images/manga/2/258225.jpg'}
```
```python
mangainfoID(35243)
```

### topanime
```python
#syntax
#topanime(searchresult=3,type='',page=1)
#searchresult is the number of searchresults returned (max 49)
#page is the page number of search result by default it is 1 (page 1)
#type is type of top anime list, possible values for type is: airing, upcoming, tv, movie, ova, ona, special, bypopularity, favorite or an empty string for overall top anime list

#returns [Spy x Family, Kaguya-sama wa Kokurasetai: Ultra Romantic, Kingdom 4th Season, One Piece, Paripi Koumei]
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

#returns[Monogatari Series: First Season, Monogatari Series: Second Season, Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e: 2-nensei-hen, Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e, Ookami to Koushinryou]
```
```python
topmanga(5,'lightnovels')

```

