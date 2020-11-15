import pytest

from clean.repository.postgress_objects import Room
from clean.repository import postgresrepo

pytestmark = pytest.mark.integration


def test_repository_list_without_parameters(docker_setup, pg_data, pg_session):
    repo = postgresrepo.PostgresRepo(docker_setup['postgress'])
    repo_rooms = rep.list()

    assert set([r.code for r in repo_rooms]) == set(
        [r['code'] for r in pg_data])
