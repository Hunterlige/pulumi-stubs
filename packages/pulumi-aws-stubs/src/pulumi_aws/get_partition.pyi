import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPartitionResult",
    "AwaitableGetPartitionResult",
    "get_partition",
    "get_partition_output",
]

@pulumi.output_type
class GetPartitionResult:
    def __init__(
        __self__, dns_suffix=..., id=..., partition=..., reverse_dns_prefix=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def partition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reverseDnsPrefix")
    def reverse_dns_prefix(self) -> _builtins.str: ...

class AwaitableGetPartitionResult(GetPartitionResult):
    def __await__(self): ...

def get_partition(
    id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetPartitionResult: ...
def get_partition_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPartitionResult]: ...
