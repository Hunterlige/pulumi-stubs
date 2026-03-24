

import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataPlaneAadOrApiKeyAuthOptionArgs', 'DataPlaneAadOrApiKeyAuthOptionArgsDict', 'DataPlaneAuthOptionsArgs', 'DataPlaneAuthOptionsArgsDict', 'EncryptionWithCmkArgs', 'EncryptionWithCmkArgsDict', 'IdentityArgs', 'IdentityArgsDict', 'IpRuleArgs', 'IpRuleArgsDict', 'NetworkRuleSetArgs', 'NetworkRuleSetArgsDict', ..., ..., ..., ..., 'PrivateEndpointConnectionPropertiesArgs', 'PrivateEndpointConnectionPropertiesArgsDict', 'SharedPrivateLinkResourcePropertiesArgs', 'SharedPrivateLinkResourcePropertiesArgsDict', 'SkuArgs', 'SkuArgsDict']
class DataPlaneAadOrApiKeyAuthOptionArgsDict(TypedDict):
    
    aad_auth_failure_mode: NotRequired[pulumi.Input[AadAuthFailureMode]]


@pulumi.input_type
class DataPlaneAadOrApiKeyAuthOptionArgs:
    def __init__(__self__, *, aad_auth_failure_mode: Optional[pulumi.Input[AadAuthFailureMode]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadAuthFailureMode")
    def aad_auth_failure_mode(self) -> Optional[pulumi.Input[AadAuthFailureMode]]:
        
        ...
    
    @aad_auth_failure_mode.setter
    def aad_auth_failure_mode(self, value: Optional[pulumi.Input[AadAuthFailureMode]]): # -> None:
        ...
    


class DataPlaneAuthOptionsArgsDict(TypedDict):
    
    aad_or_api_key: NotRequired[pulumi.Input[DataPlaneAadOrApiKeyAuthOptionArgsDict]]
    api_key_only: NotRequired[Any]


@pulumi.input_type
class DataPlaneAuthOptionsArgs:
    def __init__(__self__, *, aad_or_api_key: Optional[pulumi.Input[DataPlaneAadOrApiKeyAuthOptionArgs]] = ..., api_key_only: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadOrApiKey")
    def aad_or_api_key(self) -> Optional[pulumi.Input[DataPlaneAadOrApiKeyAuthOptionArgs]]:
        
        ...
    
    @aad_or_api_key.setter
    def aad_or_api_key(self, value: Optional[pulumi.Input[DataPlaneAadOrApiKeyAuthOptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyOnly")
    def api_key_only(self) -> Optional[Any]:
        
        ...
    
    @api_key_only.setter
    def api_key_only(self, value: Optional[Any]): # -> None:
        ...
    


class EncryptionWithCmkArgsDict(TypedDict):
    
    enforcement: NotRequired[pulumi.Input[SearchEncryptionWithCmk]]


@pulumi.input_type
class EncryptionWithCmkArgs:
    def __init__(__self__, *, enforcement: Optional[pulumi.Input[SearchEncryptionWithCmk]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforcement(self) -> Optional[pulumi.Input[SearchEncryptionWithCmk]]:
        
        ...
    
    @enforcement.setter
    def enforcement(self, value: Optional[pulumi.Input[SearchEncryptionWithCmk]]): # -> None:
        ...
    


class IdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, IdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, IdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, IdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, IdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class IpRuleArgsDict(TypedDict):
    
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpRuleArgs:
    def __init__(__self__, *, value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkRuleSetArgsDict(TypedDict):
    
    bypass: NotRequired[pulumi.Input[Union[_builtins.str, SearchBypass]]]
    ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpRuleArgsDict]]]]


@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(__self__, *, bypass: Optional[pulumi.Input[Union[_builtins.str, SearchBypass]]] = ..., ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[IpRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bypass(self) -> Optional[pulumi.Input[Union[_builtins.str, SearchBypass]]]:
        
        ...
    
    @bypass.setter
    def bypass(self, value: Optional[pulumi.Input[Union[_builtins.str, SearchBypass]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpRuleArgs]]]]:
        
        ...
    
    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpRuleArgs]]]]): # -> None:
        ...
    


class PrivateEndpointConnectionPropertiesPrivateEndpointArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PrivateEndpointConnectionPropertiesPrivateEndpointArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[PrivateLinkServiceConnectionStatus]]


@pulumi.input_type
class PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[PrivateLinkServiceConnectionStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[PrivateLinkServiceConnectionStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[PrivateLinkServiceConnectionStatus]]): # -> None:
        ...
    


class PrivateEndpointConnectionPropertiesArgsDict(TypedDict):
    
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateEndpointArgsDict]]
    private_link_service_connection_state: NotRequired[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionProvisioningState]]]


@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(__self__, *, group_id: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint: Optional[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateEndpointArgs]] = ..., private_link_service_connection_state: Optional[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionProvisioningState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateEndpointArgs]]:
        
        ...
    
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs]]:
        
        ...
    
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input[PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionProvisioningState]]]): # -> None:
        ...
    


class SharedPrivateLinkResourcePropertiesArgsDict(TypedDict):
    
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    private_link_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceProvisioningState]]]
    request_message: NotRequired[pulumi.Input[_builtins.str]]
    resource_region: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceStatus]]]


@pulumi.input_type
class SharedPrivateLinkResourcePropertiesArgs:
    def __init__(__self__, *, group_id: Optional[pulumi.Input[_builtins.str]] = ..., private_link_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceProvisioningState]]] = ..., request_message: Optional[pulumi.Input[_builtins.str]] = ..., resource_region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_resource_id.setter
    def private_link_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_region.setter
    def resource_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, SharedPrivateLinkResourceStatus]]]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[Union[_builtins.str, SkuName]]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[Union[_builtins.str, SkuName]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuName]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuName]]]): # -> None:
        ...
    


