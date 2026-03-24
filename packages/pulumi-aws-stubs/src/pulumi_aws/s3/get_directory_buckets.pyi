import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDirectoryBucketsResult",
    "AwaitableGetDirectoryBucketsResult",
    "get_directory_buckets",
    "get_directory_buckets_output",
]

@pulumi.output_type
class GetDirectoryBucketsResult:
    def __init__(__self__, arns=..., buckets=..., id=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetDirectoryBucketsResult(GetDirectoryBucketsResult):
    def __await__(self): ...

def get_directory_buckets(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetDirectoryBucketsResult: ...
def get_directory_buckets_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDirectoryBucketsResult]: ...
