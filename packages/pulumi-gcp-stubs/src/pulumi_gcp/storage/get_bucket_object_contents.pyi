import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBucketObjectContentsResult",
    "AwaitableGetBucketObjectContentsResult",
    "get_bucket_object_contents",
    "get_bucket_object_contents_output",
]

@pulumi.output_type
class GetBucketObjectContentsResult:
    def __init__(
        __self__, bucket=..., bucket_objects=..., id=..., match_glob=..., prefix=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketObjects")
    def bucket_objects(
        self,
    ) -> Sequence[outputs.GetBucketObjectContentsBucketObjectResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchGlob")
    def match_glob(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

class AwaitableGetBucketObjectContentsResult(GetBucketObjectContentsResult):
    def __await__(self): ...

def get_bucket_object_contents(
    bucket: Optional[_builtins.str] = ...,
    match_glob: Optional[_builtins.str] = ...,
    prefix: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBucketObjectContentsResult: ...
def get_bucket_object_contents_output(
    bucket: Optional[pulumi.Input[_builtins.str]] = ...,
    match_glob: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBucketObjectContentsResult]: ...
