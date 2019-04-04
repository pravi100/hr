import tempfile

from hr import inventory

def test_inventory_load():
    """

    :return:
    """
    inv_file = tempfile.NamedTemporaryFile(delete=False)
    inv_file.write(b"""
    [
        {
        "name": "kevin",
        "groups": ["wheel", "dev"],
        "password": "password_one"
      },
      {
        "name": "lisa",
        "groups": ["wheel"],
        "password": "password_two"
      },
      {
        "name": "jim",
        "groups": [],
        "password": "password_three"
      }
    ]
    """)
    inv_file.close()

    user_list = inventory.load(inv_file.name)
    assert users_list[0] == {
        'name': 'kevin',
        'groups': ['wheel', 'dev'],
        'password': 'password_one'
    }
    assert users_list[1] == {
        'name': 'lisa',
        'groups': ['wheel'],
        'password': 'password_two'
    }
    assert users_list[2] == {
        'name': 'jim',
        'groups': [],
        'password': 'password_three'
    }


def test_inventory_dump(mocker):
    """

    :param mocker:
    :return:
    """
    dest_file = tempfile.NamedTemporaryFile(delete=False)
    dest_file.close()

    mocker.patch('spwd.getspname', return_value=mocker.Mock(sp_pwd='password'))

    mocker.patch('grp.getgrall', return_value=[
        mocker.Mock(gr_name='super', gr_mem=['bob']),
        mocker.Mock(gr_name='other', gr_mem=[]),
        mocker.Mock(gr_name='wheel', gr_mem=['bob', 'kevin']),
    ])

    inventory.dump(dest_file.name, ['kevin', 'bob'])

    with open(dest_file.name) as f:
        assert f.read() == """[{"name": "kevin", "groups": ["wheel"], "password": "password"}, {"name": "bob", "groups": ["super", "wheel"], "password": "password"}]"""