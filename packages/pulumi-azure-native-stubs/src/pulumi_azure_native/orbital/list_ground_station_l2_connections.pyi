import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListGroundStationL2ConnectionsResult",
    "AwaitableListGroundStationL2ConnectionsResult",
    "list_ground_station_l2_connections",
    "list_ground_station_l2_connections_output",
]

@pulumi.output_type
class ListGroundStationL2ConnectionsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[Sequence[outputs.ResourceIdListResultResponseValue]]: ...

class AwaitableListGroundStationL2ConnectionsResult(
    ListGroundStationL2ConnectionsResult
):
    def __await__(self): ...

def list_ground_station_l2_connections(
    ground_station_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListGroundStationL2ConnectionsResult: ...
def list_ground_station_l2_connections_output(
    ground_station_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListGroundStationL2ConnectionsResult]: ...
