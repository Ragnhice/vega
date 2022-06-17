from aqas.utils.gql_adapter import GraphQLDataAdapter
from aqas.utils.singleton import Singleton


class ApiAdapter(GraphQLDataAdapter, metaclass=Singleton):
    def __init__(self):
        super().__init__(service="api")

    def get_user(self, user_id: int = 1, expect_errors: bool = False):
        geo = (self.query_builder()
               .query("geo")
               .fields(["lat", "lng"])
               .generate())

        address = (self.query_builder()
                   .query("address")
                   .fields([geo])
                   .generate())

        query = (self.query_builder()
                 .operation()
                 .query("user", input={"id": user_id})
                 .fields(["id", "username", "email", address])
                 .generate())

        return self._call_service_method(query, expect_errors=expect_errors)
