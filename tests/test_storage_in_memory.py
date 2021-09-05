import pytest

from models.node import NodeCreate, Node
from storage.base import AbstractStorage
from storage.in_memory import InMemoryStorage


@pytest.mark.parametrize("storage", [
    InMemoryStorage()
]
)
def test_can_create_node(storage: AbstractStorage):
    assert storage.get_nodes() == []
    node_to_create = NodeCreate(name="node name", attr="node attr")
    new_node = storage.add_node(node_to_create)

    assert isinstance(new_node, Node)
    assert new_node.name == "node name"
    assert new_node.attr == "node attr"

    nodes = storage.get_nodes()
    assert len(nodes) == 1
    assert nodes[0] == new_node.id


@pytest.mark.parametrize("storage", [
    InMemoryStorage()
]
)
def test_can_delete_node(storage: AbstractStorage):
    assert storage.get_nodes() == []
    # add two nodes into storage
    node_1 = NodeCreate(name="node 1", attr="node 1")
    node_2 = NodeCreate(name="node 2", attr="node 2")
    new_node_1 = storage.add_node(node_1)
    new_node_2 = storage.add_node(node_2)

    storage.delete_node(new_node_1.id)

    nodes = storage.get_nodes()
    # only one node is left in the storage
    assert len(nodes) == 1
    assert nodes[0] == new_node_2.id
