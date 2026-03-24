import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccountPublicAccessBlockResult",
    "AwaitableGetAccountPublicAccessBlockResult",
    "get_account_public_access_block",
    "get_account_public_access_block_output",
]

@pulumi.output_type
class GetAccountPublicAccessBlockResult:
    def __init__(
        __self__,
        account_id=...,
        block_public_acls=...,
        block_public_policy=...,
        id=...,
        ignore_public_acls=...,
        restrict_public_buckets=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> _builtins.bool: ...

class AwaitableGetAccountPublicAccessBlockResult(GetAccountPublicAccessBlockResult):
    def __await__(self): ...

def get_account_public_access_block(
    account_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccountPublicAccessBlockResult: ...
def get_account_public_access_block_output(
    account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccountPublicAccessBlockResult]: ...
