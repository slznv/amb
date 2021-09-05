from uuid import uuid4

from models.node import Node
from storage.base import AbstractStorage


class InMemoryStorage(AbstractStorage):
    """Implementation of the in-memory storage. """

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        _id = uuid4().hex
        _node = Node(id=_id, name=node.name, attr=node.attr)
        self.nodes[_id] = _node

        return _node

    def delete_node(self, node_id):
        try:
            self.nodes.pop(node_id)
        except KeyError:
            raise self.NotFoundError("Can not find node with provided id")

    def get_nodes(self):
        return list(self.nodes.keys())

    def get_node(self, node_id):
        return self.nodes.get(node_id, None)
