#!/usr/bin/env python3

import os
import shutil
import logging
import nose
import OpenMovie


class Test_OpenMovie:
    """
        Author: Winnie Wei Jeng
        Assignment: Week 5
        Professor: Phil Tracton
        Date: 10/28/2018
        Test_OpenMovie class demonstrates nosetests on OpenMovie class
    """


    def __init__(self):
        '''
        constructor
        '''
        # capture stdouts and log statements
        self.capture = nose.plugins.capture.Capture()
        self.logcapture = nose.plugins.logcapture.LogCapture()
        self.logcapture.start()
        logging.basicConfig(filename="testlog.log",
                            level=logging.info,
                            format='%(asctime)s,%(levelname)s,%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        pass

    def setup(self):
        '''
        setup begins capturing the stdout and log statements
        '''
        self.capture.begin()
        self.logcapture.begin()
        self.empty_movie = OpenMovie.OpenMovie()

        # assert self.empty_movie.path is "Posters"

        # if Posters directory already exists, delete it
        if os.path.isdir(self.empty_movie.path):
            shutil.rmtree(self.empty_movie.path)
        else:
            pass

    def teardown(self):
        '''
        teardown
        '''
        self.capture.end()
        self.logcapture.end()
        del (self.empty_movie)
        print("capture: %s" % (self.capture.buffer))
        print("logcapture: %s " % (self.logcapture.formatLogRecords()))

    def test_ctor(self):
        '''
        Test constructor method
        '''
        self.capture.begin()
        self.logcapture.begin()
        assert self.empty_movie.title is None
        assert self.empty_movie.posterURL is None
        assert self.empty_movie.posterFileName is None
        assert self.empty_movie.path is 'Posters'
        # if Posters directory already exists assert its existence
        if os.path.isdir(self.empty_movie.path):
            assert os.path.isdir(self.empty_movie.path)
        # else create the Posters directory and then assert its existence
        else:
            os.mkdir(self.empty_movie.path)
            assert os.path.isdir(self.empty_movie.path)
        self.capture.finalize(result="None")

    def test_getPoster(self):
        '''
        Test getPoster method
        '''
        self.capture.begin()
        self.logcapture.begin()
        # test a functioning poster title and url to create a file in Posters
        self.gladiator_movie = OpenMovie.OpenMovie("Gladiator", "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS00MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg")
        self.gladiator_movie.getPoster()
        # test another functioning poster title and url to create a file in Posters
        self.ironman_movie = OpenMovie.OpenMovie("Iron Man", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX300.jpg")
        self.ironman_movie.getPoster()
        # test an incorrect url to default to exception
        self.faulty_movie = OpenMovie.OpenMovie("Dummy", "https://images.jpg")
        self.faulty_movie.getPoster()

        self.capture.finalize(result="None")
