

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomerManagedKeyEncryptionArgs', 'CustomerManagedKeyEncryptionArgsDict', 'KeyEncryptionKeyIdentityArgs', 'KeyEncryptionKeyIdentityArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'OnlineExperimentationWorkspacePropertiesArgs', 'OnlineExperimentationWorkspacePropertiesArgsDict', 'OnlineExperimentationWorkspaceSkuArgs', 'OnlineExperimentationWorkspaceSkuArgsDict', 'PrivateEndpointConnectionPropertiesArgs', 'PrivateEndpointConnectionPropertiesArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'ResourceEncryptionConfigurationArgs', 'ResourceEncryptionConfigurationArgsDict']
class CustomerManagedKeyEncryptionArgsDict(TypedDict):
    
    key_encryption_key_identity: NotRequired[pulumi.Input[KeyEncryptionKeyIdentityArgsDict]]
    key_encryption_key_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomerManagedKeyEncryptionArgs:
    def __init__(__self__, *, key_encryption_key_identity: Optional[pulumi.Input[KeyEncryptionKeyIdentityArgs]] = ..., key_encryption_key_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(self) -> Optional[pulumi.Input[KeyEncryptionKeyIdentityArgs]]:
        
        ...
    
    @key_encryption_key_identity.setter
    def key_encryption_key_identity(self, value: Optional[pulumi.Input[KeyEncryptionKeyIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_encryption_key_url.setter
    def key_encryption_key_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyEncryptionKeyIdentityArgsDict(TypedDict):
    
    federated_client_id: NotRequired[pulumi.Input[_builtins.str]]
    identity_type: NotRequired[pulumi.Input[Union[_builtins.str, KeyEncryptionKeyIdentityType]]]
    user_assigned_identity_resource_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyEncryptionKeyIdentityArgs:
    def __init__(__self__, *, federated_client_id: Optional[pulumi.Input[_builtins.str]] = ..., identity_type: Optional[pulumi.Input[Union[_builtins.str, KeyEncryptionKeyIdentityType]]] = ..., user_assigned_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="federatedClientId")
    def federated_client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @federated_client_id.setter
    def federated_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[Union[_builtins.str, KeyEncryptionKeyIdentityType]]]:
        
        ...
    
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[Union[_builtins.str, KeyEncryptionKeyIdentityType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


class OnlineExperimentationWorkspacePropertiesArgsDict(TypedDict):
    
    app_configuration_resource_id: pulumi.Input[_builtins.str]
    log_analytics_workspace_resource_id: pulumi.Input[_builtins.str]
    logs_exporter_storage_account_resource_id: pulumi.Input[_builtins.str]
    encryption: NotRequired[pulumi.Input[ResourceEncryptionConfigurationArgsDict]]


@pulumi.input_type
class OnlineExperimentationWorkspacePropertiesArgs:
    def __init__(__self__, *, app_configuration_resource_id: pulumi.Input[_builtins.str], log_analytics_workspace_resource_id: pulumi.Input[_builtins.str], logs_exporter_storage_account_resource_id: pulumi.Input[_builtins.str], encryption: Optional[pulumi.Input[ResourceEncryptionConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConfigurationResourceId")
    def app_configuration_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_configuration_resource_id.setter
    def app_configuration_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceResourceId")
    def log_analytics_workspace_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_analytics_workspace_resource_id.setter
    def log_analytics_workspace_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsExporterStorageAccountResourceId")
    def logs_exporter_storage_account_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @logs_exporter_storage_account_resource_id.setter
    def logs_exporter_storage_account_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[ResourceEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[ResourceEncryptionConfigurationArgs]]): # -> None:
        ...
    


class OnlineExperimentationWorkspaceSkuArgsDict(TypedDict):
    
    name: pulumi.Input[Union[_builtins.str, OnlineExperimentationWorkspaceSkuName]]


@pulumi.input_type
class OnlineExperimentationWorkspaceSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[Union[_builtins.str, OnlineExperimentationWorkspaceSkuName]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, OnlineExperimentationWorkspaceSkuName]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, OnlineExperimentationWorkspaceSkuName]]): # -> None:
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
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
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
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class ResourceEncryptionConfigurationArgsDict(TypedDict):
    
    customer_managed_key_encryption: NotRequired[pulumi.Input[CustomerManagedKeyEncryptionArgsDict]]


@pulumi.input_type
class ResourceEncryptionConfigurationArgs:
    def __init__(__self__, *, customer_managed_key_encryption: Optional[pulumi.Input[CustomerManagedKeyEncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(self) -> Optional[pulumi.Input[CustomerManagedKeyEncryptionArgs]]:
        
        ...
    
    @customer_managed_key_encryption.setter
    def customer_managed_key_encryption(self, value: Optional[pulumi.Input[CustomerManagedKeyEncryptionArgs]]): # -> None:
        ...
    


