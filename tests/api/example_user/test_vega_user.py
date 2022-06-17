from models.api.mutations.crus.user.startup_adapter_mutation_user import StartupApiAdapterMutation


def test_create_user():
    user = StartupApiAdapterMutation().create_user()
    assert isinstance(user['id'], int)
    user_id_created = user['CreateUser']['user']['id']
    return user_id_created


def test_update_user():
    user = StartupApiAdapterMutation().create_user()
    user_id_1 = user['id']
    user_updated = StartupApiAdapterMutation().update_user(user_id_1)
    assert user_updated['id'] != user_id_1, "Ошибка пользователь не обновился"
