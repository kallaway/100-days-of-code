from dataclasses import dataclass, field
import typing
import uuid

@dataclass
class Customer(object):
    id: int
    name: str
    address: str

@dataclass(frozen=True, order=True)
class CustomerOrder(object):
    id: uuid.UUID = field(compare=False, default_factory=uuid.uuid4)
    value: float = field(compare=False)
    product: str = field(compare=False)


