from unittest import mock
import pytest
import uuid

from clean.request_objects import room_list_request_object as req
from clean.response_objects import response_objects as res
from clean.use_cases import room_list_use_case as uc
from clean.domain import room as r


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
    request = req.RoomListRequestObject()
    response = room_list_use_case.execute(request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_rooms


def test_room_list_with_filters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    room_list_use_case = uc.RoomListUseCase(repo)
    qry_filters = {'code__eq': 5}
    request_object = req.RoomListRequestObject.from_dict(
        {'filters': qry_filters})
    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_rooms


def test_room_list_handle_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    room_list_use_case = uc.RoomListUseCase(repo)
    request_object = req.RoomListRequestObject.from_dict({})
    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_room_list_handles_bad_request():
    repo = mock.Mock()
    room_list_use_case = uc.RoomListUseCase(repo)
    request_object = req.RoomListRequestObject.from_dict({'filters': 5})
    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': 'filters: Is not iterable'
    }
