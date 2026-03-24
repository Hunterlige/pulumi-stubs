import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccountIdTokenResult",
    "AwaitableGetAccountIdTokenResult",
    "get_account_id_token",
    "get_account_id_token_output",
]

@pulumi.output_type
class GetAccountIdTokenResult:
    def __init__(
        __self__,
        delegates=...,
        id=...,
        id_token=...,
        include_email=...,
        target_audience=...,
        target_service_account=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delegates(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="idToken")
    def id_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeEmail")
    def include_email(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="targetAudience")
    def target_audience(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetServiceAccount")
    def target_service_account(self) -> Optional[_builtins.str]: ...

class AwaitableGetAccountIdTokenResult(GetAccountIdTokenResult):
    def __await__(self): ...

def get_account_id_token(
    delegates: Optional[Sequence[_builtins.str]] = ...,
    include_email: Optional[_builtins.bool] = ...,
    target_audience: Optional[_builtins.str] = ...,
    target_service_account: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccountIdTokenResult: ...
def get_account_id_token_output(
    delegates: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    include_email: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    target_audience: Optional[pulumi.Input[_builtins.str]] = ...,
    target_service_account: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccountIdTokenResult]: ...
