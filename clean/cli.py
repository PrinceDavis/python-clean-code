#!/usr/bin/env python

from clean.repository import memrepo as mr
from clean.use_cases import room_list_use_case as uc

repo = mr.MemRepo([])
use_case = uc.RoomListUseCase(repo)
result = use_case.execute()

print(result)
