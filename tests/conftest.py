import tempfile
import pytest
import yaml
import os

from clean.flask_settings import TestConfig
from clean.app import create_app


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)


# def pytest_addoption(parser):
#     parser.addoption("--integration", action="store_true",
#                      help="run integration tests")


# def pytest_runtest_setup(item):
#     if 'integration' in item.keywords and not item.config.getvalue("integration"):
#         pytest.skip("need --integration option to run")


@pytest.fixture(scope='session')
def docker_setup(docker_ip):
    return {
        'postgres': {
            'dbname': 'clean',
            'user': 'postgres',
            'password': 'cleandb',
            'host': docker_ip
        }
    }


@pytest.fixture(scope='session')
def docker_tempfile():
    f = tempfile.mkstemp()
    yield f
    os.remove(f[1])


@pytest.fixture(scope='session')
def docker_compose_file(docker_tempfile, docker_setup):
    content = {
        'version': '3.1',
        'services': {
            'postgresql': {
                'restart': 'always',
                'image': 'postgres',
                'ports': ["5432:5432"],
                'environment': [
                    'POSTGRES_PASSWORD={}'.format(
                        docker_setup['postgres']['password'])
                ]
            }
        }
    }
    f = os.fdopen(docker_tempfile[0], 'w')
    f.write(yaml.dump(content))
    f.close()

    return docker_tempfile[1]
