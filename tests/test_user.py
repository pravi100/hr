
import pytest
import crypt
import subprocess

from hr import users

password = ''
password = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
user_credentials = {
  'name': 'kevin',
  'groups': ['wheel', 'dev'],
  'password': password
}


def test_user_add(mocker):
    """

    :param mocker:
    :return:
    """
    mocker.patch('subprocess.call')
    users.add(user_credentials)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin',
    ])

def test_user_del(mocker):
    """

    :param mocker:
    :return:
    """
    mocker.patch('subprocess.call')
    users.remove(user_credentials)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        'kevin',
    ])

def test_user_update(mocker):
    """

    :param mocker:
    :return:
    """
    mocker.patch('subprocess.call')
    users.update(user_credentials)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin',
    ])

def test_users_sync(mocker):
    """
    Given a list of user dictionaries, `users.sync(...)` should
    create missing users, remove extra non-system users, and update
    existing users. A list of existing usernames can be passed in
    or default users will be used.
    """
    existing_user_names = ['kevin', 'bob']
    users_info = [
        user_credentials,
        {
            'name': 'jose',
            'groups': ['wheel'],
            'password': password
        }
    ]
    mocker.patch('subprocess.call')
    users.sync(users_info, existing_user_names)

    subprocess.call.assert_has_calls([
        mocker.call([
            'usermod',
            '-p',
            password,
            '-G',
            'wheel,dev',
            'kevin',
        ]),
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'wheel',
            'jose',
        ]),
        mocker.call([
            'userdel',
            '-r',
            'bob',
        ]),
    ])







