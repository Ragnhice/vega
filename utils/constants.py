class API:
    """Класс, который содержит константы, используемые в тестах API."""
    ROLE = [
        "SHOOTER",
        "INSTRUCTOR",
        "ADMINISTRATOR",
    ]

    TEST_PASSWORD_1 = "1111"
    TEST_PASSWORD_2 = "2222"

    FAKE_PAST_TIME = '"2022-07-13T13:16:13"'

    WEAPON_MODE = [
        "LIGHTWEIGHT",
        "COMBAT",
        "IMITATORS",
    ]

    TIMELIMIT = [
        "10:00:00",
    ]

    WEAPON_TYPE_IDS = {
        "АК74": 2,
        "SVDM": 3,
        "RPG26": 7,
        "PKM": 8,
        "PM": 9,
        "AK101": 12,
        "AK102": 13,
        "AK103": 14,
        "AK104": 15,
        "PKP": 18,
    }

    AMMO_TYPE_IDS = {
        "5,45x39mm": 1,
        "PG_7VL": 4,
        "PG_7VR": 5,
        "TBG_7V": 6,
        "OG_7V": 7,
        "VOG_25": 10,
        "VOG_25PM": 11,
        "VOG_17MU": 12,
        "GPD_30": 13,
        "12,7x108mm": 15,
    }

    PARENT_UNIT_ID = 1
    EX_ID_SHOOTING_RANGE = 1
    SCENE_ID_APOCALYPSE = "dc3370a4-5de4-4bad-8731-d96541c02dfb"
    SCENE_ID_FOREST = "9c5b0fee-ae5b-4e75-adb1-4df0c620eb26"
    SCENE_ID_MOUNTAIN_RIVER = "481d20e8-af4b-4c74-9a32-01d5be9f1b95"
    SCENE_ID_SHOOTING_RANGE = "a6d795e1-a39b-41af-82bc-7f3f265ec3b5"

    OBJECTS_GUUD_FLAT_TARGET = "7a36e6ac-ec91-4c51-9b00-110ad44e1af0"
    OBJECTS_NAME = "Flat target 12a"
    COMMAND_MOVE_ID = 34684

    POSITION = "{'x':341.012,'y':229.2,'z':-4.5}"
    WEAPON_ID_EX = 6
    AMMO_ID_EX = 9


class UI:
    """Класс, который содержит константы, используемые в тестах UI."""
    EMPTY = "p - emptylabel"
    TEST_LASTNAME = "Фамилия_тест"
    TEST_PASSWORD = "1111"
    TEST_NAME_ORGANISATION = "Организация_тест"
