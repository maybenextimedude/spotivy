# -*- coding: utf-8 -*-
import vk_api
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import token, client_id, client_secret, redirect_uri, scope
import time
import random


def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def main():
    try:
        vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    
    vk = vk_session.get_api()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

    name, artists = None, None
    emoji = ['✝', '⚡', '✔', '❤', '⭐', '🆗',
             '🈳', '🈵' '🈶', '🌈', '🍒', '🎄',
              '👽', '💉', '💊', '💔', '💙', '💚',
               '💛', '💜', '💞', '💥', '🔥', '🔪', 
               '🕊', '🕯', '🕷', '🖤', '🥝', '🥤']

    while True:
        ct = sp.current_user_playing_track()
        if ct is not None:
            name, album = ct['item']['name'], ct['item']['album']['name']
            artists = ', '.join([el['name'] for el in ct['item']['artists']])
            text = f'{random.choice(emoji)} Spotify playing: {name} {random.choice(emoji)} {album} {random.choice(emoji)} {artists} {random.choice(emoji)}'
            vk.status.set(text=text)
            print(text)
        else:
            ct = vk.status.get()
            if 'audio' in ct:
                name, artists = ct['audio']['title'], ct['audio']['artist']
                text = f'{random.choice(emoji)} Vk playing: {name} {random.choice(emoji)} {artists} {random.choice(emoji)}'
                vk.status.set(text=text)
                print(text)
            else:
                text = f'{random.choice(emoji)} Vk playing: {name} {random.choice(emoji)} {artists} {random.choice(emoji)}'
                vk.status.set(text=text)

        time.sleep(3)


def test():
    while True:
        emoji = ['✝', '⚡', '✔', '❤', '⭐', '🆗',
                '🈳', '🈵' '🈶', '🌈', '🍒', '🎄',
                '👽', '💉', '💊', '💔', '💙', '💚',
                '💛', '💜', '💞', '💥', '🔥', '🔪', 
                '🕊', '🕯', '🕷', '🖤', '🥝', '🥤']
        print(random.choice(emoji))



if __name__ == '__main__':
    main()