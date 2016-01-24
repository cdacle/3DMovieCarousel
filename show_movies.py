""" 
This takes a command-line argument representing the file path to a json file that contains movie data
and generates the html file, then displays the output html file in a browser
"""
import getopt
import os
import sys
import webbrowser

import movies

def main(argv):
    """ Main function: Takes command-line arguments. """

    if (len(argv) != 1):
        print("Usage: show_movies.py <path_to_json_file>")
        sys.exit(2)

    movies_datafile = argv[0]
    movies_datafile_path = os.path.abspath(movies_datafile)

    if (not os.path.exists(movies_datafile_path)):
        print("Error: Input file does not exist: %s" % (movies_datafile_path))
        sys.exit(1)

    output_file_url = movies.render_movie_html(movies_datafile_path)
    
    if ((output_file_url is None) or (not os.path.exists(output_file_url))):
        print("Error: Failed to find rendered html output file")
        sys.exit(1)

    webbrowser.open('file://' + output_file_url, new = 2)

if (__name__ == "__main__"):
    main(sys.argv[1:])


