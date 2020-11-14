import pytest

from clean.flask_settings import TestConfig
from clean.app import create_app


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
