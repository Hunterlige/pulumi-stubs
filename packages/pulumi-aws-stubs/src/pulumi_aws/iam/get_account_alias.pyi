import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccountAliasResult",
    "AwaitableGetAccountAliasResult",
    "get_account_alias",
    "get_account_alias_output",
]

@pulumi.output_type
class GetAccountAliasResult:
    def __init__(__self__, account_alias=..., id=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

class AwaitableGetAccountAliasResult(GetAccountAliasResult):
    def __await__(self): ...

def get_account_alias(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccountAliasResult: ...
def get_account_alias_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccountAliasResult]: ...
