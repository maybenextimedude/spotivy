# -*- coding: utf-8 -*-
import vk_api
from config import vk_token


def main():
    try:
        vk_session = vk_api.VkApi(token=vk_token)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    
    vk = vk_session.get_api()
    vk.status.set(text='awdzxc')


if __name__ == '__main__':
    main()