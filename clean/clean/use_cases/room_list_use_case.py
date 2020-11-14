from clean.response_objects import response_objects as res


class RoomListUseCase():
    """
    docstring
    """

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        rooms = self.repo.list()
        return res.ResponseSuccess(rooms)
