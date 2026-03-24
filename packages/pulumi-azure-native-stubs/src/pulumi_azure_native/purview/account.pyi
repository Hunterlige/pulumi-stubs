

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountArgs', 'Account']
@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], account_name: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[IdentityArgs]] = ..., ingestion_storage: Optional[pulumi.Input[IngestionStorageArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_event_hub_state: Optional[pulumi.Input[Union[_builtins.str, ManagedEventHubState]]] = ..., managed_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_resources_public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., sku: Optional[pulumi.Input[AccountSkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenant_endpoint_state: Optional[pulumi.Input[Union[_builtins.str, TenantEndpointState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionStorage")
    def ingestion_storage(self) -> Optional[pulumi.Input[IngestionStorageArgs]]:
        
        ...
    
    @ingestion_storage.setter
    def ingestion_storage(self, value: Optional[pulumi.Input[IngestionStorageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedEventHubState")
    def managed_event_hub_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedEventHubState]]]:
        
        ...
    
    @managed_event_hub_state.setter
    def managed_event_hub_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedEventHubState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_resource_group_name.setter
    def managed_resource_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourcesPublicNetworkAccess")
    def managed_resources_public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]:
        
        ...
    
    @managed_resources_public_network_access.setter
    def managed_resources_public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]): # -> None:
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
    def sku(self) -> Optional[pulumi.Input[AccountSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[AccountSkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantEndpointState")
    def tenant_endpoint_state(self) -> Optional[pulumi.Input[Union[_builtins.str, TenantEndpointState]]]:
        
        ...
    
    @tenant_endpoint_state.setter
    def tenant_endpoint_state(self, value: Optional[pulumi.Input[Union[_builtins.str, TenantEndpointState]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:purview:Account")
class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ..., ingestion_storage: Optional[pulumi.Input[Union[IngestionStorageArgs, IngestionStorageArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_event_hub_state: Optional[pulumi.Input[Union[_builtins.str, ManagedEventHubState]]] = ..., managed_resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_resources_public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[AccountSkuArgs, AccountSkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenant_endpoint_state: Optional[pulumi.Input[Union[_builtins.str, TenantEndpointState]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccountArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Account:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountStatus")
    def account_status(self) -> pulumi.Output[outputs.AccountPropertiesAccountStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudConnectors")
    def cloud_connectors(self) -> pulumi.Output[Optional[outputs.CloudConnectorsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByObjectId")
    def created_by_object_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[outputs.AccountPropertiesEndpointsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionStorage")
    def ingestion_storage(self) -> pulumi.Output[Optional[outputs.IngestionStorageResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedEventHubState")
    def managed_event_hub_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResources")
    def managed_resources(self) -> pulumi.Output[outputs.AccountPropertiesManagedResourcesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourcesPublicNetworkAccess")
    def managed_resources_public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mergeInfo")
    def merge_info(self) -> pulumi.Output[Optional[outputs.AccountMergeInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.AccountSkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantEndpointState")
    def tenant_endpoint_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


