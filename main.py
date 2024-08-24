from helper import get_id, get_secret, get_auth

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
import random
# add random songs to queue
#  pause play playback



SPOTIFY_REDIRECT_URL = "http://localhost:4269"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=get_id(),
                                               client_secret=get_secret(),
                                               redirect_uri=SPOTIFY_REDIRECT_URL,
                                               scope="user-library-read user-read-playback-state user-modify-playback-state"))



h = get_auth()
payload = f"""GET /deep HTTP/1.1
Host: kb.quoccabank.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://haas.quoccabank.com/
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Origin: http://haas.quoccabank.com
Connection: keep-alive
{h}

"""
# print(payload)

r = requests.get("https://api.spotify.com/v1/me/player", headers={h})

# print(r.text)


# curl --request GET \
#   --url https://api.spotify.com/v1/me/player \
#   --header 'Authorization: Bearer 1POdFZRZbvb...qqillRxMr2z'
