

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
__all__ = ['DataCollectionEndpointArgs', 'DataCollectionEndpoint']
@pulumi.input_type
class DataCollectionEndpointArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], data_collection_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[DataCollectionEndpointResourceIdentityArgs]] = ..., immutable_id: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, KnownDataCollectionEndpointResourceKind]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_acls: Optional[pulumi.Input[DataCollectionEndpointNetworkAclsArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpointName")
    def data_collection_endpoint_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_collection_endpoint_name.setter
    def data_collection_endpoint_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def identity(self) -> Optional[pulumi.Input[DataCollectionEndpointResourceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[DataCollectionEndpointResourceIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @immutable_id.setter
    def immutable_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, KnownDataCollectionEndpointResourceKind]]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[_builtins.str, KnownDataCollectionEndpointResourceKind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[pulumi.Input[DataCollectionEndpointNetworkAclsArgs]]:
        
        ...
    
    @network_acls.setter
    def network_acls(self, value: Optional[pulumi.Input[DataCollectionEndpointNetworkAclsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:monitor:DataCollectionEndpoint")
class DataCollectionEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_collection_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., identity: Optional[pulumi.Input[Union[DataCollectionEndpointResourceIdentityArgs, DataCollectionEndpointResourceIdentityArgsDict]]] = ..., immutable_id: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, KnownDataCollectionEndpointResourceKind]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_acls: Optional[pulumi.Input[Union[DataCollectionEndpointNetworkAclsArgs, DataCollectionEndpointNetworkAclsArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataCollectionEndpointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DataCollectionEndpoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationAccess")
    def configuration_access(self) -> pulumi.Output[Optional[outputs.DataCollectionEndpointResponseConfigurationAccess]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverConfiguration")
    def failover_configuration(self) -> pulumi.Output[outputs.DataCollectionEndpointResponseFailoverConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.DataCollectionEndpointResourceResponseIdentity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsIngestion")
    def logs_ingestion(self) -> pulumi.Output[Optional[outputs.DataCollectionEndpointResponseLogsIngestion]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[outputs.DataCollectionEndpointResponseMetadata]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsIngestion")
    def metrics_ingestion(self) -> pulumi.Output[Optional[outputs.DataCollectionEndpointResponseMetricsIngestion]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> pulumi.Output[Optional[outputs.DataCollectionEndpointResponseNetworkAcls]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopedResources")
    def private_link_scoped_resources(self) -> pulumi.Output[Sequence[outputs.PrivateLinkScopedResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.DataCollectionEndpointResourceResponseSystemData]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


