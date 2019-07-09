#!/usr/bin/python3

from spacetrack import SpaceTrackClient
from dotenv import load_dotenv
import os

load_dotenv('./.env')

st = SpaceTrackClient(os.getenv('EMAIL'), os.getenv('PASSWD'))

satelites = os.getenv('SATS').split(' ')

output = st.tle_latest(norad_cat_id=satelites, ordinal=1, format='tle')

file = open('output.tle', 'w')
file.write(output)
file.close()
