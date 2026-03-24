import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHostedZoneResult",
    "AwaitableGetHostedZoneResult",
    "get_hosted_zone",
    "get_hosted_zone_output",
]

@pulumi.output_type
class GetHostedZoneResult:
    def __init__(__self__, id=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetHostedZoneResult(GetHostedZoneResult):
    def __await__(self): ...

def get_hosted_zone(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetHostedZoneResult: ...
def get_hosted_zone_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHostedZoneResult]: ...
