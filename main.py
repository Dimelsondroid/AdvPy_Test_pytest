from ya_disk import YandexDisk

# TOKEN = ''


if __name__ == '__main__':
    with open('token.txt', 'r') as file_object:
        TOKEN = file_object.read().strip()
    ya_disk = YandexDisk(token=TOKEN)

    ya_disk.create_folder('AdvPy_Tests')