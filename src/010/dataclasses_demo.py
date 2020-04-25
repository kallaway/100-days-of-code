from dataclasses import dataclass, field, InitVar
import typing
import uuid

@dataclass
class Customer(object):
    database: InitVar[typing.Any]
    id: int
    name: str
    address: str

    def __post_init__(self, database):
        self.address = self.address.capitalize()
        self._connection = database.connect()


@dataclass(frozen=True, order=True)
class CustomerOrder(object):
    processing_time: typing.ClassVar[int]

    id: uuid.UUID = field(compare=False, default_factory=uuid.uuid4, init=False)
    value: float = field(compare=False)
    product: str = field(compare=False)

    def __post_init__(self):
        self.product = self.product.capitalize()

@dataclass(frozen=True)
class CustomerOrderExtended(CustomerOrder):
    data_ordered: str
