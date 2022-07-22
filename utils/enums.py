from enum import Enum


class UserTypeEnum(Enum):
    """Класс, который содержит константы, используемые при выборе роли."""
    ADMINISTRATOR = "ADMINISTRATOR"
    INSTRUCTOR = "INSTRUCTOR"
    SHOOTER = "SHOOTER"


class Gender(Enum):
    """Класс, который содержит константы, используемые для обозначения половой принадлежности."""
    MALE = "MALE"
    FEMALE = "FEMALE"


class ExTypeEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения типа упражнения."""
    DUEL = "DUEL"
    RAZVEDKA = "RAZVEDKA"
    EX3D = "EX3D"
    VIDEO = "VIDEO"
    SHOOTINGUNKNOWN = "SHOOTINGUNKNOWN"
    SHOOTINGUPS = "SHOOTINGUPS"
    SHOOTINGUNS = "SHOOTINGUNS"
    SHOOTINGUUS = "SHOOTINGUUS"
    SHOOTINGUKS = "SHOOTINGUKS"
    UNKNOWN = "UNKNOWN"


class SeasonEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения сезона."""
    WINTER = "WINTER"
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    AUTUMN = "AUTUMN"


class ShooterPositionEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения позиции стрелка."""
    STAY = "STAY"
    KNEES = "KNEES"
    LAY = "LAY"


class PrecipitationEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения уровня осадков."""
    NOTHING = "NOTHING"
    LITTLE = "LITTLE"
    MIDDLE = "MIDDLE"
    HEAVY = "HEAVY"


class ScreenSizeEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения экранных режимов/ширины экрана."""
    WIDE = "WIDE"
    TIDE = "TIDE"
    FULL = "FULL"
    DUEL = "DUEL"
    FULLLEFT = "FULLLEFT"
    FULLRIGHT = "FULLRIGHT"


class WeaponModeEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения режима оружия."""
    LIGHTWEIGHT = "LIGHTWEIGHT"
    COMBAT = "COMBAT"
    IMITATORS = "IMITATORS"


class StateEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения статуса полосы."""
    CHOOSE = "CHOOSE"
    PAUSE = "PAUSE"
    START = "START"
    STOP = "STOP"


class AllTasksEnum(Enum):
    """Класс, который содержит константы, используемые для обозначения сервисов."""
    EX_EDITOR = "ExerciseEditor"
    CAMERA_SETTINGS = "CameraSettings"
    SERVICE = "Service"
