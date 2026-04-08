import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProtectionPolicyResult",
    "AwaitableGetProtectionPolicyResult",
    "get_protection_policy",
    "get_protection_policy_output",
]

@pulumi.output_type
class GetProtectionPolicyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        e_tag=...,
        id=...,
        location=...,
        name=...,
        properties=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetProtectionPolicyResult(GetProtectionPolicyResult):
    def __await__(self): ...

def get_protection_policy(
    policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vault_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProtectionPolicyResult: ...
def get_protection_policy_output(
    policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProtectionPolicyResult]: ...
