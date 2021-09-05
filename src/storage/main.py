from storage.base import AbstractStorage


"""
A bit tricky way to implement dependency injection
"""


class Storage:
    storage: AbstractStorage


async def get_storage() -> AbstractStorage:
    return storage.storage


storage = Storage()
