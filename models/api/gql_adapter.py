import json
import re
from typing import Union

import allure
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from gql_query_builder import GqlQuery


class GraphQLDataAdapter:

    def __init__(self):
        self.__service_name = None
        self.__base_url = None
        self.__port = None
        self.__token = None
        self.__timeout = 5
        self.query_builder = GqlQuery

    def __repr__(self):
        return f"{self.service_name}; {self.url};"

    @property
    def service_name(self):
        return self.__service_name

    @service_name.setter
    def service_name(self, value):
        if value is not None:
            self.__service_name = value

    @property
    def base_url(self):
        return self.__base_url

    @base_url.setter
    def base_url(self, value):
        if value is not None:
            self.__base_url = value

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        if value is not None:
            self.__port = value

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        if value is not None:
            self.__token = value

    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, value):
        if value is not None:
            self.__timeout = value

    @property
    def url(self):
        if self.port:
            return f"{self.base_url}:{self.port}/graphql"
        return f"{self.base_url}/{self.service_name}"

    @property
    def auth_headers(self):
        if self.token:
            return {"Authorization": "Bearer " + self.token}
        return None

    @staticmethod
    def convert_parameter(param: Union[list[str], str]):
        if param is not (None or "null"):
            if isinstance(param, list):
                return str(param).replace("\'", '"')
            return f'"{param}"'
        return param

    @staticmethod
    def format_mutation(mutation_value: str):
        # flake8: noqa: Q000
        """
        Метод для форматирования мутаций, созданных билдером

        :param mutation_value: Мутация GraphQL
        :return: Мутация без двойных дополнительных двойных кавычек
        """
        del_double_double_quotes = re.sub('"{2}', "'", mutation_value)
        del_double_quotes = re.sub('"{1}', '', del_double_double_quotes)
        return re.sub("'", '"', del_double_quotes).replace('True', 'true').replace('False', 'false')

    def _call_service_method(self, call_schema: str, expect_errors: bool = False):
        """
        Метод по выполнению запроса GraphQL

        :param call_schema: Схема для отправки запроса
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        :return: Результат выполнения запроса
        """
        transport = RequestsHTTPTransport(url=self.url, use_json=True, timeout=self.timeout, headers=self.auth_headers)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql(call_schema)
        response = None
        try:
            allure.attach(f"{self.url}\r{call_schema}", name="Query", extension=".txt")
            response = client.execute(query)
        except Exception as error:
            if expect_errors is True or expect_errors is None:
                try:
                    if len(error.args) == 1:
                        response = json.loads(error.args[0].replace("\'", '\"'))
                except json.JSONDecodeError:
                    return error.args[0]
                return response
            raise
        finally:
            transport.close()

        allure.attach(json.dumps(response), name="Response", extension=".json")
        return response
