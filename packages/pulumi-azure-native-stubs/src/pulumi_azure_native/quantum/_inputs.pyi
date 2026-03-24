

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'ProviderArgs', 'ProviderArgsDict', 'WorkspaceResourcePropertiesArgs', 'WorkspaceResourcePropertiesArgsDict']
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
    


class ProviderArgsDict(TypedDict):
    
    application_name: NotRequired[pulumi.Input[_builtins.str]]
    instance_uri: NotRequired[pulumi.Input[_builtins.str]]
    provider_id: NotRequired[pulumi.Input[_builtins.str]]
    provider_sku: NotRequired[pulumi.Input[_builtins.str]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, ProviderStatus]]]
    resource_usage_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *, application_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_uri: Optional[pulumi.Input[_builtins.str]] = ..., provider_id: Optional[pulumi.Input[_builtins.str]] = ..., provider_sku: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ProviderStatus]]] = ..., resource_usage_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_name.setter
    def application_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUri")
    def instance_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_uri.setter
    def instance_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerSku")
    def provider_sku(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provider_sku.setter
    def provider_sku(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ProviderStatus]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ProviderStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUsageId")
    def resource_usage_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_usage_id.setter
    def resource_usage_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkspaceResourcePropertiesArgsDict(TypedDict):
    
    api_key_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    providers: NotRequired[pulumi.Input[Sequence[pulumi.Input[ProviderArgsDict]]]]
    storage_account: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkspaceResourcePropertiesArgs:
    def __init__(__self__, *, api_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., providers: Optional[pulumi.Input[Sequence[pulumi.Input[ProviderArgs]]]] = ..., storage_account: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyEnabled")
    def api_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @api_key_enabled.setter
    def api_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProviderArgs]]]]:
        
        ...
    
    @providers.setter
    def providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProviderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account.setter
    def storage_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


