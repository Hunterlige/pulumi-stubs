

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificatePropertiesArgs', 'CertificatePropertiesArgsDict', 'IotDpsPropertiesDescriptionArgs', 'IotDpsPropertiesDescriptionArgsDict', 'IotDpsSkuInfoArgs', 'IotDpsSkuInfoArgsDict', 'IotHubDefinitionDescriptionArgs', 'IotHubDefinitionDescriptionArgsDict', 'IpFilterRuleArgs', 'IpFilterRuleArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'PrivateEndpointConnectionPropertiesArgs', 'PrivateEndpointConnectionPropertiesArgsDict', 'PrivateEndpointConnectionArgs', 'PrivateEndpointConnectionArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', ..., ...]
class CertificatePropertiesArgsDict(TypedDict):
    
    certificate: NotRequired[pulumi.Input[_builtins.str]]
    is_verified: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CertificatePropertiesArgs:
    def __init__(__self__, *, certificate: Optional[pulumi.Input[_builtins.str]] = ..., is_verified: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isVerified")
    def is_verified(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_verified.setter
    def is_verified(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class IotDpsPropertiesDescriptionArgsDict(TypedDict):
    
    allocation_policy: NotRequired[pulumi.Input[Union[_builtins.str, AllocationPolicy]]]
    authorization_policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionArgsDict]]]]
    enable_data_residency: NotRequired[pulumi.Input[_builtins.bool]]
    iot_hubs: NotRequired[pulumi.Input[Sequence[pulumi.Input[IotHubDefinitionDescriptionArgsDict]]]]
    ip_filter_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpFilterRuleArgsDict]]]]
    portal_operations_host_name: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgsDict]]]]
    provisioning_state: NotRequired[pulumi.Input[_builtins.str]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, State]]]


@pulumi.input_type
class IotDpsPropertiesDescriptionArgs:
    def __init__(__self__, *, allocation_policy: Optional[pulumi.Input[Union[_builtins.str, AllocationPolicy]]] = ..., authorization_policies: Optional[pulumi.Input[Sequence[pulumi.Input[SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionArgs]]]] = ..., enable_data_residency: Optional[pulumi.Input[_builtins.bool]] = ..., iot_hubs: Optional[pulumi.Input[Sequence[pulumi.Input[IotHubDefinitionDescriptionArgs]]]] = ..., ip_filter_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IpFilterRuleArgs]]]] = ..., portal_operations_host_name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]] = ..., provisioning_state: Optional[pulumi.Input[_builtins.str]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, State]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationPolicy")
    def allocation_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, AllocationPolicy]]]:
        
        ...
    
    @allocation_policy.setter
    def allocation_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, AllocationPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationPolicies")
    def authorization_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionArgs]]]]:
        
        ...
    
    @authorization_policies.setter
    def authorization_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataResidency")
    def enable_data_residency(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_data_residency.setter
    def enable_data_residency(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IotHubDefinitionDescriptionArgs]]]]:
        
        ...
    
    @iot_hubs.setter
    def iot_hubs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IotHubDefinitionDescriptionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipFilterRules")
    def ip_filter_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpFilterRuleArgs]]]]:
        
        ...
    
    @ip_filter_rules.setter
    def ip_filter_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpFilterRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalOperationsHostName")
    def portal_operations_host_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_operations_host_name.setter
    def portal_operations_host_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]]:
        
        ...
    
    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, State]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, State]]]): # -> None:
        ...
    


class IotDpsSkuInfoArgsDict(TypedDict):
    
    capacity: NotRequired[pulumi.Input[_builtins.float]]
    name: NotRequired[pulumi.Input[Union[_builtins.str, IotDpsSku]]]


@pulumi.input_type
class IotDpsSkuInfoArgs:
    def __init__(__self__, *, capacity: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[Union[_builtins.str, IotDpsSku]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, IotDpsSku]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, IotDpsSku]]]): # -> None:
        ...
    


class IotHubDefinitionDescriptionArgsDict(TypedDict):
    
    connection_string: pulumi.Input[_builtins.str]
    location: pulumi.Input[_builtins.str]
    allocation_weight: NotRequired[pulumi.Input[_builtins.int]]
    apply_allocation_policy: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class IotHubDefinitionDescriptionArgs:
    def __init__(__self__, *, connection_string: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], allocation_weight: Optional[pulumi.Input[_builtins.int]] = ..., apply_allocation_policy: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_string.setter
    def connection_string(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationWeight")
    def allocation_weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allocation_weight.setter
    def allocation_weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyAllocationPolicy")
    def apply_allocation_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_allocation_policy.setter
    def apply_allocation_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class IpFilterRuleArgsDict(TypedDict):
    
    action: pulumi.Input[IpFilterActionType]
    filter_name: pulumi.Input[_builtins.str]
    ip_mask: pulumi.Input[_builtins.str]
    target: NotRequired[pulumi.Input[IpFilterTargetType]]


@pulumi.input_type
class IpFilterRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[IpFilterActionType], filter_name: pulumi.Input[_builtins.str], ip_mask: pulumi.Input[_builtins.str], target: Optional[pulumi.Input[IpFilterTargetType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[IpFilterActionType]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[IpFilterActionType]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter_name.setter
    def filter_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_mask.setter
    def ip_mask(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[IpFilterTargetType]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[IpFilterTargetType]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PrivateEndpointConnectionPropertiesArgsDict(TypedDict):
    
    private_link_service_connection_state: pulumi.Input[PrivateLinkServiceConnectionStateArgsDict]


@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(__self__, *, private_link_service_connection_state: pulumi.Input[PrivateLinkServiceConnectionStateArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Input[PrivateLinkServiceConnectionStateArgs]:
        
        ...
    
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: pulumi.Input[PrivateLinkServiceConnectionStateArgs]): # -> None:
        ...
    


class PrivateEndpointConnectionArgsDict(TypedDict):
    
    properties: pulumi.Input[PrivateEndpointConnectionPropertiesArgsDict]


@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *, properties: pulumi.Input[PrivateEndpointConnectionPropertiesArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[PrivateEndpointConnectionPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[PrivateEndpointConnectionPropertiesArgs]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    description: pulumi.Input[_builtins.str]
    status: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]
    actions_required: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], status: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]], actions_required: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStatus]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionArgsDict(TypedDict):
    
    key_name: pulumi.Input[_builtins.str]
    rights: pulumi.Input[Union[_builtins.str, AccessRightsDescription]]
    primary_key: NotRequired[pulumi.Input[_builtins.str]]
    secondary_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionArgs:
    def __init__(__self__, *, key_name: pulumi.Input[_builtins.str], rights: pulumi.Input[Union[_builtins.str, AccessRightsDescription]], primary_key: Optional[pulumi.Input[_builtins.str]] = ..., secondary_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rights(self) -> pulumi.Input[Union[_builtins.str, AccessRightsDescription]]:
        
        ...
    
    @rights.setter
    def rights(self, value: pulumi.Input[Union[_builtins.str, AccessRightsDescription]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_key.setter
    def secondary_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


