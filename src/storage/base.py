import abc

from models.node import NodeCreate, Node


class AbstractStorage(abc.ABC):
    class BaseException(Exception):
        """Base exception for all custom exceptions in this class"""
        pass

    class NotFoundError(BaseException):
        """Custom exception when entity not found in the storage"""
        pass

    @abc.abstractmethod
    def add_node(self, node: NodeCreate) -> Node:
        """Add new node to the storage"""
        raise NotImplementedError

    @abc.abstractmethod
    def delete_node(self, node_id) -> None:
        """Delete the node by node's ID"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_node(self, node_id) -> Node:
        """Retrieve info about the node by node's ID"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_nodes(self):
        """Retrieve all available IDs of all nodes"""
        raise NotImplementedError
