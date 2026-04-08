import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CommunityArgs", "Community"]

@pulumi.input_type
class CommunityArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        address_space: Optional[pulumi.Input[_builtins.str]] = ...,
        approval_settings: Optional[pulumi.Input[ApprovalSettingsArgs]] = ...,
        community_name: Optional[pulumi.Input[_builtins.str]] = ...,
        community_role_assignments: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]
        ] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        firewall_sku: Optional[pulumi.Input[Union[_builtins.str, FirewallSKU]]] = ...,
        governed_service_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[GovernedServiceItemArgs]]]
        ] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_mode_configuration: Optional[
            pulumi.Input[MaintenanceModeConfigurationModelArgs]
        ] = ...,
        policy_override: Optional[
            pulumi.Input[Union[_builtins.str, PolicyOverride]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address_space.setter
    def address_space(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="approvalSettings")
    def approval_settings(self) -> Optional[pulumi.Input[ApprovalSettingsArgs]]: ...
    @approval_settings.setter
    def approval_settings(
        self, value: Optional[pulumi.Input[ApprovalSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="communityName")
    def community_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @community_name.setter
    def community_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="communityRoleAssignments")
    def community_role_assignments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]]: ...
    @community_role_assignments.setter
    def community_role_assignments(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RoleAssignmentItemArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_servers.setter
    def dns_servers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="firewallSku")
    def firewall_sku(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FirewallSKU]]]: ...
    @firewall_sku.setter
    def firewall_sku(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FirewallSKU]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="governedServiceList")
    def governed_service_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GovernedServiceItemArgs]]]]: ...
    @governed_service_list.setter
    def governed_service_list(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[GovernedServiceItemArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceModeConfiguration")
    def maintenance_mode_configuration(
        self,
    ) -> Optional[pulumi.Input[MaintenanceModeConfigurationModelArgs]]: ...
    @maintenance_mode_configuration.setter
    def maintenance_mode_configuration(
        self, value: Optional[pulumi.Input[MaintenanceModeConfigurationModelArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyOverride")
    def policy_override(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyOverride]]]: ...
    @policy_override.setter
    def policy_override(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyOverride]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:mission:Community")
class Community(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        address_space: Optional[pulumi.Input[_builtins.str]] = ...,
        approval_settings: Optional[
            pulumi.Input[Union[ApprovalSettingsArgs, ApprovalSettingsArgsDict]]
        ] = ...,
        community_name: Optional[pulumi.Input[_builtins.str]] = ...,
        community_role_assignments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RoleAssignmentItemArgs, RoleAssignmentItemArgsDict]
                    ]
                ]
            ]
        ] = ...,
        dns_servers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        firewall_sku: Optional[pulumi.Input[Union[_builtins.str, FirewallSKU]]] = ...,
        governed_service_list: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[GovernedServiceItemArgs, GovernedServiceItemArgsDict]
                    ]
                ]
            ]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_mode_configuration: Optional[
            pulumi.Input[
                Union[
                    MaintenanceModeConfigurationModelArgs,
                    MaintenanceModeConfigurationModelArgsDict,
                ]
            ]
        ] = ...,
        policy_override: Optional[
            pulumi.Input[Union[_builtins.str, PolicyOverride]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CommunityArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Community: ...
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="approvalSettings")
    def approval_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ApprovalSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="communityRoleAssignments")
    def community_role_assignments(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RoleAssignmentItemResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="firewallSku")
    def firewall_sku(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="governedServiceList")
    def governed_service_list(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.GovernedServiceItemResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceModeConfiguration")
    def maintenance_mode_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.MaintenanceModeConfigurationModelResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(
        self,
    ) -> pulumi.Output[outputs.ManagedOnBehalfOfConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyOverride")
    def policy_override(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceCollection")
    def resource_collection(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
