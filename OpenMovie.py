#!/usr/bin/env python3

import logging
import os
import re
import sys
import traceback
import urllib.request
import sqlalchemy
# import sqlalchemy.orm
# import sqlalchemy.ext.declarative
import json
import ORM

"""
File: Jeng_Winnie_Lab6.py
Author: Winnie Wei Jeng
Assignment: Lab 7
Professor: Phil Tracton
Date: 11/8/2018
Description: This simple GUI pulls up movie poster's image upon entering in the movie title

"""
class OpenMovie:
    """
        Author: Winnie Wei Jeng
        Assignment: Week 6
        Professor: Phil Tracton
        Date: 11/3/2018
        OpenMovie class takes in a string title and a string url and return an image
    """

    # constructor:
    def __init__(self, title=None, posterURL=None):
        '''
        constructor
        '''
        self.title = title
        self.posterURL = posterURL
        self.posterFileName = None
        self.path = "Posters"
        if os.path.isdir(self.path):
            pass
        else:
            os.mkdir(self.path)
            logging.info(" Successfully created the directory %s " % self.path)

    def getPoster(self):
        # log the event of calling getPoster() method
        logging.info(" getPoster() method is called")
        logging.info(" Poster's name: %s" % self.title)
        logging.info(" Poster's URL %s" % self.posterURL)

        # substitute every symbol and spaces in title with underline
        re.sub(r"[^a-zA-Z0-9]", "_", self.title)
        self.posterFileName = "Posters/%s.jpg" % self.title
        try:
            urllib.request.urlretrieve(self.posterURL, self.posterFileName)
            return True
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            logging.error("*** tb_lineno: {}".format(exc_traceback.tb_lineno))
            return False

    # user enters movie title in GUI, fxn gets the row from the instance's movie title
    def getMovieTitleData(self):

        # query the ORM session for the ORM Movies

        # self.title = "Avatar"  # testing purpose
        result = ORM.session.query(ORM.Movies.title)
        for x in result:
            # print(x)
            x = re.sub(r'[\W_]+', '', str(x))
            # if query works and ORM Movies title is equal to this class title, return resultx
            if x == self.title:
                logging.info("  movie title {} is queried from the db".format(self.title))
                result = x
                return result
            else:
                logging.error(" movie title {} is not found in the db".format(self.title))
                return False

    # get the cast information from this movie’s credits table
    def getCast(self):

        # query the ORM session for the ORM Credits table
        # filter it on the ORM Credits title matching this class’s title
        # store the results in movieCreditsQuery

        # self.title = "Iron Man"  # testing purpose
        moviesCreditsQuery = ORM.session.query(ORM.Credits.title, ORM.Credits.cast)
        for x in moviesCreditsQuery:
            if x[0] == self.title:
                logging.info(" movie credits title {} is queried from the db".format(self.title))
                # print(x[1])
                try:
                    # json loads the cast from 0th element of movieCreditsQuery and store result in cast
                    cast_info = json.loads(x[1])
                    cast = cast_info[0]['name']
                    return cast
                except:
                    logging.error(" could not load the cast info from the db".format(self.title))
                    return False
            else:
                logging.error(" movie credits title {} is not found in the db".format(self.title))
                return False


    # get the crew information from this movie’s Credits table
    def getCrew(self):
        print("get crew!")
        # query the ORM session for this ORM Credits and filter
        # where the ORM Credits title is the movie’s title and
        # store this in movieCreditsQuery
        moviesCreditsQuery = ORM.session.query(ORM.Credits.title).filter(ORM.Credits.title == self.title)
        if self.title is moviesCreditsQuery:
            logging.info(" movie credits title {} is queried from the db".format(self.title))
        else:
            return False, False
        try:
            crew = json.load(moviesCreditsQuery[0].crew)
        except:
            logging.error(" could not load the crew info from the db".format(self.title))
            return False, False

        try:
            for key, value in crew.iteritems():
                if "Director" is value:
                    # return crew[value+1]
                    return value+1, crew  # return the director's name and crew
        except:
            logging.error(" cannot query the director's info")
            return False, False











