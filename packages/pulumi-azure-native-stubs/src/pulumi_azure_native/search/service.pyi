

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
__all__ = ['ServiceArgs', 'Service']
@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], auth_options: Optional[pulumi.Input[DataPlaneAuthOptionsArgs]] = ..., compute_type: Optional[pulumi.Input[Union[_builtins.str, ComputeType]]] = ..., data_exfiltration_protections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SearchDataExfiltrationProtection]]]]] = ..., disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_with_cmk: Optional[pulumi.Input[EncryptionWithCmkArgs]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., hosting_mode: Optional[pulumi.Input[HostingMode]] = ..., identity: Optional[pulumi.Input[IdentityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_rule_set: Optional[pulumi.Input[NetworkRuleSetArgs]] = ..., partition_count: Optional[pulumi.Input[_builtins.int]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., search_service_name: Optional[pulumi.Input[_builtins.str]] = ..., semantic_search: Optional[pulumi.Input[Union[_builtins.str, SearchSemanticSearch]]] = ..., sku: Optional[pulumi.Input[SkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_available: Optional[pulumi.Input[Union[_builtins.str, UpgradeAvailable]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authOptions")
    def auth_options(self) -> Optional[pulumi.Input[DataPlaneAuthOptionsArgs]]:
        
        ...
    
    @auth_options.setter
    def auth_options(self, value: Optional[pulumi.Input[DataPlaneAuthOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ComputeType]]]:
        
        ...
    
    @compute_type.setter
    def compute_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ComputeType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExfiltrationProtections")
    def data_exfiltration_protections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SearchDataExfiltrationProtection]]]]]:
        
        ...
    
    @data_exfiltration_protections.setter
    def data_exfiltration_protections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SearchDataExfiltrationProtection]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionWithCmk")
    def encryption_with_cmk(self) -> Optional[pulumi.Input[EncryptionWithCmkArgs]]:
        
        ...
    
    @encryption_with_cmk.setter
    def encryption_with_cmk(self, value: Optional[pulumi.Input[EncryptionWithCmkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingMode")
    def hosting_mode(self) -> Optional[pulumi.Input[HostingMode]]:
        
        ...
    
    @hosting_mode.setter
    def hosting_mode(self, value: Optional[pulumi.Input[HostingMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkRuleSet")
    def network_rule_set(self) -> Optional[pulumi.Input[NetworkRuleSetArgs]]:
        
        ...
    
    @network_rule_set.setter
    def network_rule_set(self, value: Optional[pulumi.Input[NetworkRuleSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @partition_count.setter
    def partition_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchServiceName")
    def search_service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @search_service_name.setter
    def search_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="semanticSearch")
    def semantic_search(self) -> Optional[pulumi.Input[Union[_builtins.str, SearchSemanticSearch]]]:
        
        ...
    
    @semantic_search.setter
    def semantic_search(self, value: Optional[pulumi.Input[Union[_builtins.str, SearchSemanticSearch]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeAvailable")
    def upgrade_available(self) -> Optional[pulumi.Input[Union[_builtins.str, UpgradeAvailable]]]:
        
        ...
    
    @upgrade_available.setter
    def upgrade_available(self, value: Optional[pulumi.Input[Union[_builtins.str, UpgradeAvailable]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:search:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auth_options: Optional[pulumi.Input[Union[DataPlaneAuthOptionsArgs, DataPlaneAuthOptionsArgsDict]]] = ..., compute_type: Optional[pulumi.Input[Union[_builtins.str, ComputeType]]] = ..., data_exfiltration_protections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SearchDataExfiltrationProtection]]]]] = ..., disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_with_cmk: Optional[pulumi.Input[Union[EncryptionWithCmkArgs, EncryptionWithCmkArgsDict]]] = ..., endpoint: Optional[pulumi.Input[_builtins.str]] = ..., hosting_mode: Optional[pulumi.Input[HostingMode]] = ..., identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_rule_set: Optional[pulumi.Input[Union[NetworkRuleSetArgs, NetworkRuleSetArgsDict]]] = ..., partition_count: Optional[pulumi.Input[_builtins.int]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., search_service_name: Optional[pulumi.Input[_builtins.str]] = ..., semantic_search: Optional[pulumi.Input[Union[_builtins.str, SearchSemanticSearch]]] = ..., sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., upgrade_available: Optional[pulumi.Input[Union[_builtins.str, UpgradeAvailable]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Service:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authOptions")
    def auth_options(self) -> pulumi.Output[Optional[outputs.DataPlaneAuthOptionsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExfiltrationProtections")
    def data_exfiltration_protections(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionWithCmk")
    def encryption_with_cmk(self) -> pulumi.Output[Optional[outputs.EncryptionWithCmkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingMode")
    def hosting_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkRuleSet")
    def network_rule_set(self) -> pulumi.Output[Optional[outputs.NetworkRuleSetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
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
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="semanticSearch")
    def semantic_search(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUpgradedAt")
    def service_upgraded_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(self) -> pulumi.Output[Sequence[outputs.SharedPrivateLinkResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeAvailable")
    def upgrade_available(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


