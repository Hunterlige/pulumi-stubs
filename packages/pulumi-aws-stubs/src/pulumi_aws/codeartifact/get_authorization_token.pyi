import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAuthorizationTokenResult",
    "AwaitableGetAuthorizationTokenResult",
    "get_authorization_token",
    "get_authorization_token_output",
]

@pulumi.output_type
class GetAuthorizationTokenResult:
    def __init__(
        __self__,
        authorization_token=...,
        domain=...,
        domain_owner=...,
        duration_seconds=...,
        expiration=...,
        id=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationToken")
    def authorization_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetAuthorizationTokenResult(GetAuthorizationTokenResult):
    def __await__(self): ...

def get_authorization_token(
    domain: Optional[_builtins.str] = ...,
    domain_owner: Optional[_builtins.str] = ...,
    duration_seconds: Optional[_builtins.int] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAuthorizationTokenResult: ...
def get_authorization_token_output(
    domain: Optional[pulumi.Input[_builtins.str]] = ...,
    domain_owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    duration_seconds: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAuthorizationTokenResult]: ...
