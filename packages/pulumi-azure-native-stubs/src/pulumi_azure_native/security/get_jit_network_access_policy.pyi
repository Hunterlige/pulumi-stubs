import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetJitNetworkAccessPolicyResult",
    "AwaitableGetJitNetworkAccessPolicyResult",
    "get_jit_network_access_policy",
    "get_jit_network_access_policy_output",
]

@pulumi.output_type
class GetJitNetworkAccessPolicyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        kind=...,
        location=...,
        name=...,
        provisioning_state=...,
        requests=...,
        type=...,
        virtual_machines=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def requests(
        self,
    ) -> Optional[Sequence[outputs.JitNetworkAccessRequestResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> Sequence[outputs.JitNetworkAccessPolicyVirtualMachineResponse]: ...

class AwaitableGetJitNetworkAccessPolicyResult(GetJitNetworkAccessPolicyResult):
    def __await__(self): ...

def get_jit_network_access_policy(
    asc_location: Optional[_builtins.str] = ...,
    jit_network_access_policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetJitNetworkAccessPolicyResult: ...
def get_jit_network_access_policy_output(
    asc_location: Optional[pulumi.Input[_builtins.str]] = ...,
    jit_network_access_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetJitNetworkAccessPolicyResult]: ...
