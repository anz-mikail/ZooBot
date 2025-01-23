# -*- coding: utf-8 -*-
import vk_api


def main():
    """ Пример загрузки фото """

    login, password = '', ''
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    """ В VkUpload реализованы методы загрузки файлов в ВК
    """

    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo(  # Подставьте свои данные
        'image/mammals/predatory/dogs/европейский волк.jpg',
        album_id=200851098,
        group_id=74030368
    )

    vk_photo_url = f"https://vk.com/photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, '\nLink: ', vk_photo_url)


if __name__ == '__main__':
    main()
