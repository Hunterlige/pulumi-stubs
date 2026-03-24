import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBucketsResult",
    "AwaitableGetBucketsResult",
    "get_buckets",
    "get_buckets_output",
]

@pulumi.output_type
class GetBucketsResult:
    def __init__(__self__, buckets=..., id=..., prefix=..., project=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Sequence[outputs.GetBucketsBucketResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

class AwaitableGetBucketsResult(GetBucketsResult):
    def __await__(self): ...

def get_buckets(
    prefix: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBucketsResult: ...
def get_buckets_output(
    prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBucketsResult]: ...
