import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFirewallResult",
    "AwaitableGetFirewallResult",
    "get_firewall",
    "get_firewall_output",
]

@pulumi.output_type
class GetFirewallResult:
    def __init__(
        __self__,
        arn=...,
        availability_zone_change_protection=...,
        availability_zone_mappings=...,
        delete_protection=...,
        description=...,
        enabled_analysis_types=...,
        encryption_configurations=...,
        firewall_policy_arn=...,
        firewall_policy_change_protection=...,
        firewall_statuses=...,
        id=...,
        name=...,
        region=...,
        subnet_change_protection=...,
        subnet_mappings=...,
        tags=...,
        transit_gateway_id=...,
        transit_gateway_owner_account_id=...,
        update_token=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneChangeProtection")
    def availability_zone_change_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneMappings")
    def availability_zone_mappings(
        self,
    ) -> Sequence[outputs.GetFirewallAvailabilityZoneMappingResult]: ...
    @_builtins.property
    @pulumi.getter(name="deleteProtection")
    def delete_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enabledAnalysisTypes")
    def enabled_analysis_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Sequence[outputs.GetFirewallEncryptionConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicyArn")
    def firewall_policy_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firewallPolicyChangeProtection")
    def firewall_policy_change_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="firewallStatuses")
    def firewall_statuses(
        self,
    ) -> Sequence[outputs.GetFirewallFirewallStatusResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetChangeProtection")
    def subnet_change_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> Sequence[outputs.GetFirewallSubnetMappingResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayOwnerAccountId")
    def transit_gateway_owner_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetFirewallResult(GetFirewallResult):
    def __await__(self): ...

def get_firewall(
    arn: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFirewallResult: ...
def get_firewall_output(
    arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFirewallResult]: ...
