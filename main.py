# -*- coding: utf-8 -*-
import vk_api
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import token, client_id, client_secret, redirect_uri, scope
import time

def main():
    try:
        vk_session = vk_api.VkApi(token=token)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    
    vk = vk_session.get_api()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

    while True:
        ct = sp.current_user_playing_track()
        name, album = ct['item']['name'], ct['item']['album']['name']
        artists = ', '.join([el['name'] for el in ct['item']['artists']])
        if name != None and album != None and artists != None:
            vk.status.set(text=f'✝✡Spotify : {name} - {album} - {artists} ✝')
        time.sleep(2)


def test():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

    ct = sp.current_user_playing_track()
    ct['item']['artists'][0]['name']


if __name__ == '__main__':
    main()