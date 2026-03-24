import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOriginAccessIdentitiesResult",
    "AwaitableGetOriginAccessIdentitiesResult",
    "get_origin_access_identities",
    "get_origin_access_identities_output",
]

@pulumi.output_type
class GetOriginAccessIdentitiesResult:
    def __init__(
        __self__, comments=..., iam_arns=..., id=..., ids=..., s3_canonical_user_ids=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comments(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="iamArns")
    def iam_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3CanonicalUserIds")
    def s3_canonical_user_ids(self) -> Sequence[_builtins.str]: ...

class AwaitableGetOriginAccessIdentitiesResult(GetOriginAccessIdentitiesResult):
    def __await__(self): ...

def get_origin_access_identities(
    comments: Optional[Sequence[_builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOriginAccessIdentitiesResult: ...
def get_origin_access_identities_output(
    comments: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOriginAccessIdentitiesResult]: ...
