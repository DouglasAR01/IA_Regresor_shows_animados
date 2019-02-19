# Estimador de popularidad de shows animados
**Presentado por:**
- Douglas Andrés Ramírez Brujes
- Marianne Solangel Rojas Robles

**Universidad Industrial de Santander**

**2019**

<p align="center"><img src="http://garza.uis.edu.co/idayregreso/images/logoUIS.jpg" width="342" heigth="166"></p>

## ¿En qué consiste el proyecto?
El proyecto aprovecha el poder del machine learning para la estimación de la popularidad de un show animado 2d,
a través de un regresor.
Para esto se usan varios parámetros, entre los cuales se encuentran los siguientes:
- Número de personas interesadas en ver el show.
- Número de persosas que marcaron el show como favorito.
- Número de episodios que tiene cada show.
- Puntaje dado por las personas que vieron el show.
- Géneros del show animado.

## ¿Qué generos tomamos?
Dado que existen en el mundo de la animación oriental 2d demasiados géneros, el cómputo necesario es increíblemente alto,
por lo tanto, decidimos reducir la complejidad de los géneros mediante el agrupamiento de géneros.

La tupla que compone los géneros de un show animado se construye a partir de grupos definidos de géneros que tienen algún
tipo de relación.

<p align="center"><img src="https://i.imgur.com/n4tOUP6.png" /></p>

Los grupos de géneros fueron planteados a partir del dendrograma siguiente:

<p align="center"><img src="https://raw.githubusercontent.com/racinmat/mal-analysis/master/genres-hierarchical.png" /></p>

Autor: <a href="https://github.com/racinmat/mal-analysis">Racinmat</a>

Finalmente, los grupos de géneros resultantes son los mostrados a continuación:
- Romance
- Ecchi
- Shounen
- Fantasy
- Comedy
- Sports
- Hentai
- Historical
- Mistery
- Thriller
- Supernatural
- Gore
- Sci-Fi
- Action
- Otro

## Objetivo
El objetivo del proyecto es, al pasarse una tupla de datos que contenga los géneros del show,
el número estimado de episodios y la fuente (manga, novela, etc.), el regresor retorne una aproximación de su popularidad.

## Referencias
Los datos usados para el dataset provienen de MyAnimeList
- https://www.kaggle.com/azathoth42/myanimelist#anime_filtered.csv
- https://www.kaggle.com/azathoth42/myanimelist#anime_cleaned.csv
- https://www.kaggle.com/CooperUnion/anime-recommendations-database
- https://raw.githubusercontent.com/racinmat/mal-analysis/master/genres-hierarchical.png
- https://myanimelist.net/

<p align="center"><img src="https://image4.owler.com/logo/myanimelist_owler_20160226_213523_original.png" width="342" heigth="166"></p>
