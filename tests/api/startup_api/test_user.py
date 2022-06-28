import allure
import pytest

from models.api.startup_api_adapter import StartupApiAdapter


@allure.parent_suite("api")
@allure.suite("StartupApi")
@allure.sub_suite("user")
class TestsStartupApiUser:

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-360")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("create_user")
    def test_create_user(self):
        user = StartupApiAdapter().create_user()
        assert isinstance(user["id"], int)

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-361")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("update_user")
    def test_update_user(self):
        user = StartupApiAdapter().create_user()
        user_id_1 = user["id"]
        user_updated = StartupApiAdapter().update_user(user_id_1)
        assert user_updated["id"] == user_id_1, "Пользователь не обновился"
        assert user_updated["shortName"] != user["shortName"], "Пользователь не обновился"
        assert user_updated["firstName"] != user["firstName"], "Пользователь не обновился"
