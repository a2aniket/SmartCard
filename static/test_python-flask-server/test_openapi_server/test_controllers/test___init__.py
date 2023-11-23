from python-flask-server.openapi_server.controllers.__init__ import *
import os

def count_files(directory):
    """
    This function takes a directory path as input and returns the number of files in that directory.
    """
    count = 0
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            count += 1
    return count