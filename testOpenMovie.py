import OpenMovie
import configparser
import logging
import sys

if __name__ == "__main__":
    try:
        config = configparser.RawConfigParser()
        # read in the "movie.cfg" file
        config.read("movies.cfg")
    except:
        print("Config fail")
        logging.error("Config fail")
        sys.exit()

        # if the configuration has a section named ”LOGGING”,
        # read the LOG_FILE field of it and store the name in log_file_name
        # else set log file name to ”default.log”
    if config.has_section('LOGGING'):
        log_file_name = config.get('LOGGING', 'log_file')

    else:
        log_file_name = "default.log"

    # create a logging basiConfig
    logging.basicConfig(filename=log_file_name, level=logging.INFO,
                        format='%(asctime)s,%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    # create a logging instance using log_file_name
    logging.info(" %s opens. Program starts." % log_file_name)

openMovie = OpenMovie.OpenMovie()
print(openMovie.getCrew())