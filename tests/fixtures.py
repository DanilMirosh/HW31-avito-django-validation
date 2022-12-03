import pytest


@pytest.fixture
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = 'user'
    password = 'password'

    django_user_model.objacts.create_user(
        userbane=username,
        password=password
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data['access']

