import webbrowser

# Search for keyword: "unfinished" to find unifinished sections


class Video():
    """ This class is the parent from which other media classes inherit"""

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def display_info(self):
        print(self.title)
        print(self.duration)


class Movie(Video):
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    def __init__(
            self,
            title,
            duration,
            movie_director,
            movie_storyline,
            poster_image,
            trailer_youtube):
        Video.__init__(self, title, duration)
        self.director = movie_director
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# -- unfinished
# class TvShow(Video):
#    """ This class provides a way to store TV program related information"""
#    def __init__(self, title, duration, season, episode, tv_station):
#        Video.__init__(self, title, duration)

#    def get_local_listing():
