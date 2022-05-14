import pytest
from ya_disk import YandexDisk

# TOKEN = ''

with open('token.txt', 'r') as file_object:
    TOKEN = file_object.read().strip()
ya_disk = YandexDisk(token=TOKEN)


def test_folder_create_success():
    req = ya_disk.create_folder('AdvPy')
    assert req == 201
    ya_disk.delete_folder('AdvPy')


def test_folder_create_fail():
    req = ya_disk.create_folder('\AdvPy/*bad')
    assert req == 409


def test_folder_exists_success():
    ya_disk.create_folder('AdvPy')
    req = ya_disk.check('AdvPy')
    assert req == 200
    ya_disk.delete_folder('AdvPy')


def test_folder_exists_fail():
    ya_disk.create_folder('\AdvPy/*fjdf')
    req = ya_disk.check('\AdvPy/*fjdf')
    assert req == 404


def test_folder_delete_success():
    ya_disk.create_folder('AdvPy')
    req_d = ya_disk.delete_folder('AdvPy')
    assert req_d in [200, 201, 202, 204]


def test_folder_delete_fail():
    ya_disk.create_folder('AdvPy')
    req_d = ya_disk.delete_folder('adv')
    assert req_d in [404, 409]
