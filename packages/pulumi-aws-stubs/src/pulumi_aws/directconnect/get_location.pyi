import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocationResult",
    "AwaitableGetLocationResult",
    "get_location",
    "get_location_output",
]

@pulumi.output_type
class GetLocationResult:
    def __init__(
        __self__,
        available_macsec_port_speeds=...,
        available_port_speeds=...,
        available_providers=...,
        id=...,
        location_code=...,
        location_name=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availableMacsecPortSpeeds")
    def available_macsec_port_speeds(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availablePortSpeeds")
    def available_port_speeds(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availableProviders")
    def available_providers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="locationCode")
    def location_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="locationName")
    def location_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetLocationResult(GetLocationResult):
    def __await__(self): ...

def get_location(
    location_code: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocationResult: ...
def get_location_output(
    location_code: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocationResult]: ...
