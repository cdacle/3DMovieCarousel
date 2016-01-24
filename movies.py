""" 
This defines helper functions that will dynamically generate html file.
It requires a full path to a json file that defines the set of movies and their metadata.

Example json input:

{
  "movies": [
    {
      "title": "Top Gun",
      "description": "Adrenaline in the sky",
      "poster": "https://howtoexperience.files.wordpress.com/2012/10/topgun.png",
      "trailer": "https://youtu.be/iCrUqt9Uf3E",
      "imdb_rating":  "6.9",
      "release": "1986",
      "mpaa_rating": "PG",
      "director": "Tony Scott",
      "stars": "Tom Cruise, Kelly McGillis, Val Kilmer, Tom Skerritt"
    },
    ...

"""
import json
import os
import media
import re

def render_movie_html(movies_datafile_path):
    """ Given the full path to a json file, generate an html file and return the filename

        Args:
        movies_datafile_path: full path to json file defining the set of movies and their metadata

        Returns:
        full path to output html file, otherwise None

    """

    rendered_content = get_html_rendered_content(movies_datafile_path)

    html_output_filename_url = None
    if (rendered_content is not None):
        html_output_filename_url = get_html_output_filepath(movies_datafile_path)
        with open(html_output_filename_url, "w") as output_file:
            output_file.write(rendered_content)

    return html_output_filename_url


def get_html_output_filepath(input_filepath):
    """ Given a file path, return the same file path but with the "html" file extension

        Args:
        input_filepath: full path to a file 

        Returns:
        full path to corresponding ".html" file

    """

    input_filename = os.path.basename(input_filepath)
    base_input_filename = os.path.splitext(input_filename)[0]
    html_output_filename = base_input_filename + ".html"
    html_output_filename_url = os.path.abspath(html_output_filename)

    return html_output_filename_url


def get_html_rendered_content(movies_datafile_path):
    """ Given the movie input file path, return the html content as a string

        Args:
        movies_datafile_path: full path to input file 

        Returns:
        the final html content, otherwise None

    """

    movie_entry_template = """
    <div class="movie_entry" data-trailer-youtube-id="{youtube_id}" data-toggle="modal" data-target="#trailer" movie="{title}" release="{release}" rating="{mpaa_rating}" director="{director}" stars="{stars}">
      <img src="{poster}" width="220" height="342">
    </div>
    """

    rendered_content = None
    
    movies_data = get_movie_data(movies_datafile_path)
    if movies_data is not None:
        movie_entries = ""

        total_movies = len(movies_data)

        for movie_data in movies_data:
            
            movie = media.Movie(movie_data)
            movie.pretty_print()

            movie_entries += movie_entry_template.format(
                youtube_id = get_youtube_id(movie.trailer),
                title = movie.title,
                release = movie.release,
                mpaa_rating = movie.mpaa_rating,
                director = movie.director,
                stars = movie.stars,
                poster = movie.poster)

        rendered_content = get_rendered_content_with_filled_template(total_movies, movie_entries)

    return rendered_content


def get_youtube_id(trailer):
    """ Given a trailer url, return the youtube id 

        Args:
        trailer: youtube url

        Returns:
        the youtube id

    """

    # Extract the youtube ID from the url
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', trailer)

    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', trailer)

    trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                            else None)

    return trailer_youtube_id


def get_movie_data(movies_datafile_path):
    """ Given a trailer url, return the youtube id 

        Args:
        movies_datafile_path: full path to input file

        Returns:
        the movies data represented as a dictionary, otherwise None

    """

    movies = None
    with open(movies_datafile_path, "r") as movie_data_file:
        try:
            movie_data = json.load(movie_data_file)
        except:
            print("Error: Unable to parse json input file")
        else:
            if ("movies" in movie_data):
                movies = movie_data["movies"]

    return movies


def get_rendered_content_with_filled_template(total_movies, movie_entries):
    """ Given data extracted from input file, fill in the html template

        Args:
        total_movies: total # of movies
        movie_entries: the html content representing the individual movies

        Returns:
        the final rendered html content

    """

    content = None
    with open("movie_html_template.html", "r") as template_file:
        template = template_file.read()
        content = template.format(
            _MOVIE_COUNT = total_movies,
            _MOVIE_ENTRIES = movie_entries)

    return content