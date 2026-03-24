import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStaticIpsResult",
    "AwaitableGetStaticIpsResult",
    "get_static_ips",
    "get_static_ips_output",
]

@pulumi.output_type
class GetStaticIpsResult:
    def __init__(
        __self__, id=..., location=..., project=..., static_ips=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="staticIps")
    def static_ips(self) -> Sequence[_builtins.str]: ...

class AwaitableGetStaticIpsResult(GetStaticIpsResult):
    def __await__(self): ...

def get_static_ips(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStaticIpsResult: ...
def get_static_ips_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStaticIpsResult]: ...
