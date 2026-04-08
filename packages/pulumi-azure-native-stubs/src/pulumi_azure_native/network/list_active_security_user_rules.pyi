import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListActiveSecurityUserRulesResult",
    "AwaitableListActiveSecurityUserRulesResult",
    "list_active_security_user_rules",
    "list_active_security_user_rules_output",
]

@pulumi.output_type
class ListActiveSecurityUserRulesResult:
    def __init__(__self__, skip_token=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]: ...

class AwaitableListActiveSecurityUserRulesResult(ListActiveSecurityUserRulesResult):
    def __await__(self): ...

def list_active_security_user_rules(
    network_manager_name: Optional[_builtins.str] = ...,
    regions: Optional[Sequence[_builtins.str]] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip_token: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListActiveSecurityUserRulesResult: ...
def list_active_security_user_rules_output(
    network_manager_name: Optional[pulumi.Input[_builtins.str]] = ...,
    regions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListActiveSecurityUserRulesResult]: ...
