import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHostedZoneIdResult",
    "AwaitableGetHostedZoneIdResult",
    "get_hosted_zone_id",
    "get_hosted_zone_id_output",
]

@pulumi.output_type
class GetHostedZoneIdResult:
    def __init__(__self__, id=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetHostedZoneIdResult(GetHostedZoneIdResult):
    def __await__(self): ...

def get_hosted_zone_id(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetHostedZoneIdResult: ...
def get_hosted_zone_id_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHostedZoneIdResult]: ...
