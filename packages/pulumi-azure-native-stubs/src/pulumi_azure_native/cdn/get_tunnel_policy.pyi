import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTunnelPolicyResult",
    "AwaitableGetTunnelPolicyResult",
    "get_tunnel_policy",
    "get_tunnel_policy_output",
]

@pulumi.output_type
class GetTunnelPolicyResult:
    def __init__(
        __self__,
        azure_api_version=...,
        deployment_status=...,
        domains=...,
        id=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        target_groups=...,
        tunnel_type=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Sequence[outputs.ActivatedResourceReferenceResponse]: ...
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Optional[Sequence[outputs.ResourceReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="tunnelType")
    def tunnel_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTunnelPolicyResult(GetTunnelPolicyResult):
    def __await__(self): ...

def get_tunnel_policy(
    profile_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    tunnel_policy_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTunnelPolicyResult: ...
def get_tunnel_policy_output(
    profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    tunnel_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTunnelPolicyResult]: ...
