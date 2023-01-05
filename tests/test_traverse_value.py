from typing import List

from specklepy.objects.base import Base
from specklepy.serialization.base_object_serializer import BaseObjectSerializer


class TestBase(Base):
    foo: List[str]
    bar: int


def test_traverse_value():
    base = TestBase(bar=1)
    base.foo = [None]
    serializer = BaseObjectSerializer()
    object_id, object_dict = serializer.traverse_base(base)
    assert object_dict == {
        "id": object_id,
        "speckle_type": "Tests.TestTraverseValue.TestBase",
        "applicationId": None,
        "foo": [None],
        "units": None,
        "bar": 1,
        "totalChildrenCount": 0,
    }