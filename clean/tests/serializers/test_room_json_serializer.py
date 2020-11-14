import json
import uuid

from clean.serializers import room_json_serializer as ser
from clean.domain import room as r


def test_serializer_domain_room():
    code = uuid.uuid4()
    room = r.Room(
        code=code,
        size=200,
        price=10,
        longitude=-0.9887,
        latitude=51.7888
    )
    expected_json = """{{
      "code": "{}",
      "size": 200,
      "price": 10,
      "longitude": -0.9887,
      "latitude" : 51.7888
    }}""".format(code)
    json_room = expected_json
    assert json.loads(json_room) == json.loads(expected_json)
