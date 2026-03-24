import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOriginAccessIdentityResult",
    "AwaitableGetOriginAccessIdentityResult",
    "get_origin_access_identity",
    "get_origin_access_identity_output",
]

@pulumi.output_type
class GetOriginAccessIdentityResult:
    def __init__(
        __self__,
        arn=...,
        caller_reference=...,
        cloudfront_access_identity_path=...,
        comment=...,
        etag=...,
        iam_arn=...,
        id=...,
        s3_canonical_user_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontAccessIdentityPath")
    def cloudfront_access_identity_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamArn")
    def iam_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3CanonicalUserId")
    def s3_canonical_user_id(self) -> _builtins.str: ...

class AwaitableGetOriginAccessIdentityResult(GetOriginAccessIdentityResult):
    def __await__(self): ...

def get_origin_access_identity(
    id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetOriginAccessIdentityResult: ...
def get_origin_access_identity_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOriginAccessIdentityResult]: ...
