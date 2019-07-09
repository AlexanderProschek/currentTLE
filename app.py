#!/usr/bin/python3

from spacetrack import SpaceTrackClient
from dotenv import load_dotenv
import os

load_dotenv('./.env')

st = SpaceTrackClient(os.getenv('EMAIL'), os.getenv('PASSWD'))

print(st.tle_latest(norad_cat_id=[25544, 41335], ordinal=1, format='tle'))