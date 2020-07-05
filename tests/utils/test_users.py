import pytest

from rest_registration.exceptions import UserNotFound
from rest_registration.utils.users import authenticate_by_login_data
from tests.helpers.constants import USER_PASSWORD, USERNAME


@pytest.mark.parametrize('data', [
    pytest.param(
        {
            'login': USERNAME,
        },
        id='missing password',
    ),
    pytest.param(
        {
            'login': USERNAME,
            'password': USER_PASSWORD + 'blah',
        },
        id='invalid password',
    ),
    pytest.param(
        {
            'username': USERNAME,
            'password': USER_PASSWORD + 'blah',
        },
        id='username but invalid password',
    ),
])
def test_authenticate_by_login_data_fails(user, data):
    with pytest.raises(UserNotFound):
        authenticate_by_login_data(data)
