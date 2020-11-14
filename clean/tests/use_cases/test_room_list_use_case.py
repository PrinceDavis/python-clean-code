from unittest import mock
import pytest
import uuid

from clean.domain import room as r
from clean.use_cases import room_list_use_case as uc


@pytest.fixture()
def domain_rooms():
    room1 = r.Room(
        code=uuid.uuid4(),
        size=213,
        price=10,
        longitude=0.0003,
        latitude=41.344
    )
    room2 = r.Room(
        code=uuid.uuid4(),
        size=321,
        price=32,
        longitude=0.0003,
        latitude=41.344
    )
    room3 = r.Room(
        code=uuid.uuid4(),
        size=353,
        price=21,
        longitude=0.0003,
        latitude=41.344
    )
    room4 = r.Room(
        code=uuid.uuid4(),
        size=112,
        price=54,
        longitude=0.0003,
        latitude=41.344
    )
    return [room1, room2, room3, room4]


def test_room_list_without_parameters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    room_list_use_case = uc.RoomListUseCase(repo)
    result = room_list_use_case.excute()
    repo.list.assert_called_with()
    assert result == domain_rooms
