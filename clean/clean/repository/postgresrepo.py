from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from clean.domain import room
from clean.repository.postgress_objects import Base, Room


class PostgresRepo:
    def __init__(self, connection_data):
        conn_str = "postgresql+psycopg2://{}:{}@{}/{}".format(
            connection_data['user'],
            connection_data['password'],
            connection_data['host'],
            connection_data['dbname']
        )
        self.engine = create_engine(conn_str)
        Base.metadata.bind = self.engine

    def _create_room_objects(self, results):
        return [
            room.Room(
                code=q.code,
                size=q.size,
                price=q.price,
                latitude=q.latitude,
                longitude=q.longitude
            ) for q in results
        ]

    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(Room)

        if filters is None:
            return self._create_room_objects(query.all())

        if 'code__eq' in filters:
            query = query.filter(Room.code == filters['code__eq'])
        if 'price__eq' in filters:
            query = query.filter(r.price == filters['price__eq'])
        if 'price__lt' in filters:
            query = query.filter(Room.price < filters['price__lt'])
        if 'price__gt' in filters:
            query = query.filter(Room.price > filters['price__lt'])
        return self._create_room_objects(query.all())
