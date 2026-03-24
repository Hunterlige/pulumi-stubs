import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDbSystemShapesResult",
    "AwaitableGetDbSystemShapesResult",
    "get_db_system_shapes",
    "get_db_system_shapes_output",
]

@pulumi.output_type
class GetDbSystemShapesResult:
    def __init__(
        __self__, availability_zone_id=..., db_system_shapes=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbSystemShapes")
    def db_system_shapes(
        self,
    ) -> Sequence[outputs.GetDbSystemShapesDbSystemShapeResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetDbSystemShapesResult(GetDbSystemShapesResult):
    def __await__(self): ...

def get_db_system_shapes(
    availability_zone_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDbSystemShapesResult: ...
def get_db_system_shapes_output(
    availability_zone_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDbSystemShapesResult]: ...
