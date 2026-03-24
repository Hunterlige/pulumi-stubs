import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEventBusesResult",
    "AwaitableGetEventBusesResult",
    "get_event_buses",
    "get_event_buses_output",
]

@pulumi.output_type
class GetEventBusesResult:
    def __init__(
        __self__, event_buses=..., id=..., name_prefix=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventBuses")
    def event_buses(self) -> Sequence[outputs.GetEventBusesEventBusResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetEventBusesResult(GetEventBusesResult):
    def __await__(self): ...

def get_event_buses(
    name_prefix: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEventBusesResult: ...
def get_event_buses_output(
    name_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEventBusesResult]: ...
