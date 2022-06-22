import allure
from constants import API_USER_ID

from models.api.adapters.api_adapter import ApiAdapter


@allure.suite("api")
@allure.sub_suite("example")
class TestsGqlApi:
    # pylint: disable=too-few-public-methods

    @allure.title("Пример автотеста по взаимодействию с API")
    @allure.testcase("https://jira.steor.tech/browse/Template-02")
    def test_gql_qpi(self):
        """Не пугайтесь, тест может не работать из-за ограничения тестового сервиса!"""
        response = ApiAdapter().get_user(API_USER_ID)
        assert response, "Нет ответа от запроса"
        assert response.get("user").get("id") == str(API_USER_ID), "ID пользователя не совпадает с ожидаемым"
