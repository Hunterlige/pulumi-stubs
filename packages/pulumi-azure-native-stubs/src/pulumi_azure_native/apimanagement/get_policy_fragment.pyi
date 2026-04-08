import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPolicyFragmentResult",
    "AwaitableGetPolicyFragmentResult",
    "get_policy_fragment",
    "get_policy_fragment_output",
]

@pulumi.output_type
class GetPolicyFragmentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        format=...,
        id=...,
        name=...,
        provisioning_state=...,
        type=...,
        value=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

class AwaitableGetPolicyFragmentResult(GetPolicyFragmentResult):
    def __await__(self): ...

def get_policy_fragment(
    format: Optional[_builtins.str] = ...,
    id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPolicyFragmentResult: ...
def get_policy_fragment_output(
    format: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPolicyFragmentResult]: ...
