#/usr/bin/python

import os
import os.path
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('initilisation en cours ')

filename = "caca"

def creation_pipeline_logstash(f):
    import os.path
    file_exists = os.path.isfile(f) 

    if file_exists:
        # do something
        logging.info('le fichier %s exite deja', filename)
    else:
        # do something else
        f = open(filename, "w+")
        logging.info('creation du fichier %s', filename)
        f.close()

creation_pipeline_logstash(filename)