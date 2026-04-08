import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGetPrivateDnsZoneSuffixExecuteResult",
    "AwaitableGetGetPrivateDnsZoneSuffixExecuteResult",
    "get_get_private_dns_zone_suffix_execute",
    "get_get_private_dns_zone_suffix_execute_output",
]

@pulumi.output_type
class GetGetPrivateDnsZoneSuffixExecuteResult:
    def __init__(__self__, private_dns_zone_suffix=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateDnsZoneSuffix")
    def private_dns_zone_suffix(self) -> Optional[_builtins.str]: ...

class AwaitableGetGetPrivateDnsZoneSuffixExecuteResult(
    GetGetPrivateDnsZoneSuffixExecuteResult
):
    def __await__(self): ...

def get_get_private_dns_zone_suffix_execute(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGetPrivateDnsZoneSuffixExecuteResult: ...
def get_get_private_dns_zone_suffix_execute_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGetPrivateDnsZoneSuffixExecuteResult]: ...
