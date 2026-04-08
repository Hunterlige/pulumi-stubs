import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConfigurationPolicyGroupResult",
    "AwaitableGetConfigurationPolicyGroupResult",
    "get_configuration_policy_group",
    "get_configuration_policy_group_output",
]

@pulumi.output_type
class GetConfigurationPolicyGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        is_default=...,
        name=...,
        p2_s_connection_configurations=...,
        policy_members=...,
        priority=...,
        provisioning_state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="p2SConnectionConfigurations")
    def p2_s_connection_configurations(
        self,
    ) -> Sequence[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="policyMembers")
    def policy_members(
        self,
    ) -> Optional[
        Sequence[outputs.VpnServerConfigurationPolicyGroupMemberResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConfigurationPolicyGroupResult(GetConfigurationPolicyGroupResult):
    def __await__(self): ...

def get_configuration_policy_group(
    configuration_policy_group_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vpn_server_configuration_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConfigurationPolicyGroupResult: ...
def get_configuration_policy_group_output(
    configuration_policy_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vpn_server_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConfigurationPolicyGroupResult]: ...
