import fresh_tomatoes
import media
import people

#TODO: Add director instances
#TODO: Implement VALID_RATINGS

# Movie instances
blues_brothers = media.Movie(
    "The Blues Brothers",
    148,
    "John Landis",
    "Two brothers--one fresh out of prison--work to get their old blues band back together",
    "https://ia.media-imdb.com/images/M/MV5BYTdlMDExOGUtN2I3MS00MjY5LWE1NTAtYzc3MzIxN2M3OWY1XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
    "https://youtu.be/2HCR4c1zPyk")

chef = media.Movie(
    "Chef",
    114,
    "Jon Favreau",
    "A Chef quits his stifling restaurant job, seeking a creative outlet, and to reunite his family",
    "https://ia.media-imdb.com/images/M/MV5BMTY5NTYzNTA1M15BMl5BanBnXkFtZTgwODIwODU1MTE@._V1_SY1000_CR0,0,680,1000_AL_.jpg",
    "https://youtu.be/qK-ZUFX5fnk")

paris_texas = media.Movie(
    "Paris, Texas",
    147,
    "Wim Wenders",
    "A drifter who's been missing for four years, returns and struggles to integrate back into society and his family",#NOQA
    "https://ia.media-imdb.com/images/M/MV5BM2RjMmU3ZWItYzBlMy00ZmJkLWE5YzgtNTVkODdhOWM3NGZhXkEyXkFqcGdeQXVyNDA5Mjg5MjA@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
    "https://youtu.be/-It9uJSPXLw")

shawshank_redemption = media.Movie(
    "The Shawshank Redemption",
    142,
    "Frank Darabont",
    "Two men in a prison run a crooked warden develop a friendship based on respect and kindness",
    "https://ia.media-imdb.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
    "https://youtu.be/6hB3S9bIaco")

dark_knight = media.Movie(
    "The Dark Knight",
    152,
    "Christopher Nolan",
    "A lunatic emerges in Gotham; With no known past, and no motivation for doing the heinous things he does, \"The Joker\" proves to be Batman's most enigmatic, and terrifying foe",
    "https://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://youtu.be/8jqq4j52Fb4")

shining = media.Movie(
    "The Shining",
    144,
    "Stanley Kubrick",
    "A man, his wife, and son stay in a grand, remote hotel during the winter, working as caretakers. The isolation begins to wear on them.",
    "https://ia.media-imdb.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
    "https://youtu.be/i-B_bbkEfS0")


# Movie list for 'open_movies_page' function
movies = [
    blues_brothers,
    chef,
    paris_texas,
    shawshank_redemption,
    dark_knight,
    shining]
fresh_tomatoes.open_movies_page(movies)

# director instances
# john_landis = people.Director("John Landis", "Chicago, IL, USA", "Short, curly, gray hair", "Landis was reprimanded for circumventing the State of California's child labor laws in hiring [two children].(Noe, Denise. \"The Twilight Zone Tragedy\")")#NOQA
