import pytest

from models.api.querys.startup_adapter_query import StartupApiAdapterQuery


@pytest.mark.test_case("1")
def test_get_users():
    users = StartupApiAdapterQuery().get_query("users")
    assert type(users[0]['id']) == str, "Ошибка тип не равен str"
    assert users, "Нет ответа от запроса"


@pytest.mark.test_case("2")
def test_get_availableWeapons():
    availableWeapons = StartupApiAdapterQuery().get_query("availableWeapons")


@pytest.mark.test_case("3")
def test_get_weapons():
    weapons = StartupApiAdapterQuery().get_query("weapons")
    assert type(weapons[0]['id']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("4")
def test_get_laneDatas():
    laneDatas = StartupApiAdapterQuery().get_query("laneDatas")
    assert type(laneDatas[0]['laneNumber']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("5")
def test_get_units():
    units = StartupApiAdapterQuery().get_query("units")
    assert type(units[0]['id']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("6")
def test_get_ammoTypes():
    ammoTypes = StartupApiAdapterQuery().get_query("ammoTypes")
    assert type(ammoTypes[0]['id']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("7")
def test_get_weaponTypes():
    weaponTypes = StartupApiAdapterQuery().get_query("weaponTypes")
    assert type(weaponTypes[0]['id']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("8")
def test_get_startupApiVersion():
    startupApiVersion = StartupApiAdapterQuery().get_query("startupApiVersion")
    assert type(startupApiVersion) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("9")
def test_get_allTasks():
    allTasks = StartupApiAdapterQuery().get_query("allTasks")
    assert type(allTasks[0]) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("10")
def test_get_hunterApiVersion():
    hunterApiVersion = StartupApiAdapterQuery().get_query("hunterApiVersion")
    assert type(hunterApiVersion[0]) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("11")
def test_get_availableUsers():
    availableUsers = StartupApiAdapterQuery().get_query("availableUsers")
    assert type(availableUsers[0]['id']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("12")
def test_get_shootingMode():
    shootingMode = StartupApiAdapterQuery().get_query("shootingMode")
    assert type(shootingMode['shootingMode']['laneCount']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("13")
def test_get_objectsByExerciseId():
    objectsByExerciseId = StartupApiAdapterQuery().get_query("objectsByExerciseId",
                                                             {"objectsByExerciseId": {"id": "1"}, })
    assert type(objectsByExerciseId[0]['id']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("14")
def test_get_exercises():
    exercises = StartupApiAdapterQuery().get_query("exercises")
    assert type(exercises[0]['name']) == str, "Ошибка. Имя пустое"


@pytest.mark.test_case("15")
def test_get_objects():
    objects = StartupApiAdapterQuery().get_query("objects")
    assert type(objects[0]['name']) == str, "Ошибка. Имя пустое"
    assert objects, "Нет ответа от запроса"


@pytest.mark.test_case("16")
def test_get_scenes():
    scenes = StartupApiAdapterQuery().get_query("scenes")
    assert type(scenes[0]['name']) == 'null', "Ошибка. Имя пустое"


@pytest.mark.test_case("17")
def test_get_exerciseApiVersion():
    exerciseApiVersion = StartupApiAdapterQuery().get_query("exerciseApiVersion")
    assert type(exerciseApiVersion[0]) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("18")
def test_get_screenSizes():
    screenSizes = StartupApiAdapterQuery().get_query("screenSizes")
    assert type(screenSizes[0]['id']) == str, "Ошибка тип не равен str"


@pytest.mark.test_case("19")
def test_get_performedExercises():
    performedExercises = StartupApiAdapterQuery().get_query("performedExercises")
    assert type(performedExercises[0]['id']) == str, "Ошибка тип не равен str"
