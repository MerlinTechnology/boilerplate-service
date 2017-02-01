from __future__ import print_function
import os
import sys

# get this file's directory independent of where it's run from
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(file_path, "./"))
sys.path.append(os.path.join(file_path, "./vendored"))

import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info(event)
    logger.info(context)
    return True


