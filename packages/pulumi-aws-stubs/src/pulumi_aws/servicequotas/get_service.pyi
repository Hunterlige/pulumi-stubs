import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceResult",
    "AwaitableGetServiceResult",
    "get_service",
    "get_service_output",
]

@pulumi.output_type
class GetServiceResult:
    def __init__(
        __self__, id=..., region=..., service_code=..., service_name=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): ...

def get_service(
    region: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceResult: ...
def get_service_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceResult]: ...
