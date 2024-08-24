from helper import get_id, get_secret
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import random


MAX_VOL = 100
SPOTIFY_REDIRECT_URL = "http://localhost:1234"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=get_id(),
                                               client_secret=get_secret(),
                                               redirect_uri=SPOTIFY_REDIRECT_URL,
                                               scope="user-library-read user-read-playback-state user-modify-playback-state"))

def keep_volume_high():
    try:
        playback_state = sp.current_playback()
        if playback_state and playback_state.get('device'):
            volume_percent = playback_state.get('device', {}).get('volume_percent', 0)
            print(f"Current volume: {volume_percent}%")
            
            if volume_percent < 70:
                print("Volume TOO LOW, Maxing it out")
                # random chance for it to wait abit before adjusting volume
                if (random.randint(1,2) == 1):
                    print("waiting abit before maxing out")
                    time.sleep(3)
                    


                sp.volume(100)
            else:
                print("Volume is GOOD! No adjustment needed.")
        else:
            print("No active playback or device found.")
    except spotipy.SpotifyException as e:
        print(f"Error: {e}")


def do_stop_start():
    try:
        playback_state = sp.current_playback()

        if playback_state:
            # if its not playing yet play if not pause
            if not is_playing():
                sp.start_playback()

            action = random.choice(['stop_start', 'skip'])
            interval = random.randint(1,6)
            sp.pause_playback()
            print("Playback stopped.")
            
            time.sleep(interval)  
            # Start the playback
            sp.start_playback()
            print("Playback started.")
        else:
            print("No active playback found.")
    except spotipy.SpotifyException as e:
        print(f"Error: {e}")

    keep_volume_high()
    


def do_random_skip_or_back():
    try:
        playback_state = sp.current_playback()

        if playback_state:
            action = random.choice(['skip', 'back'])

            if action == 'skip':
                sp.next_track()
                print("Skipped to the next track.")
            elif action == 'back':
                sp.previous_track()
                print("Went back to the previous track.")
        else:
            print("No active playback found.")
    except spotipy.SpotifyException as e:
        print(f"Error: {e}")

    keep_volume_high()
    


def is_playing():
    try:
        playback_state = sp.current_playback()
        
        if playback_state:
            if playback_state.get('is_playing'):
                return True
            else:
                return False
        else:
            return False
    except spotipy.SpotifyException as e:
        print(f"Error: {e}")
    return False


if __name__ == "__main__":
    sp.volume(MAX_VOL)
    player = sp.current_playback
    while True:
        if not is_playing():
            print("You tried to pause... UNPAUSING :D")
            sp.start_playback()
        keep_volume_high()

        # do random stuff
        rand = random.randint(1,5)
        if rand == 1:
            user_changed = False
            do_random_skip_or_back()
        elif rand == 2:
            do_stop_start()
        else:
            # keep the song playing
            print("sleeping for abit")

        # sp.volume(random.randint(0,100) )
        time.sleep(5)