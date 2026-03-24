

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataCollectionEndpointResult', 'AwaitableGetDataCollectionEndpointResult', 'get_data_collection_endpoint', 'get_data_collection_endpoint_output']
@pulumi.output_type
class GetDataCollectionEndpointResult:
    
    def __init__(__self__, azure_api_version=..., configuration_access=..., description=..., etag=..., failover_configuration=..., id=..., identity=..., immutable_id=..., kind=..., location=..., logs_ingestion=..., metadata=..., metrics_ingestion=..., name=..., network_acls=..., private_link_scoped_resources=..., provisioning_state=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationAccess")
    def configuration_access(self) -> Optional[outputs.DataCollectionEndpointResponseConfigurationAccess]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverConfiguration")
    def failover_configuration(self) -> outputs.DataCollectionEndpointResponseFailoverConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.DataCollectionEndpointResourceResponseIdentity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsIngestion")
    def logs_ingestion(self) -> Optional[outputs.DataCollectionEndpointResponseLogsIngestion]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> outputs.DataCollectionEndpointResponseMetadata:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsIngestion")
    def metrics_ingestion(self) -> Optional[outputs.DataCollectionEndpointResponseMetricsIngestion]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[outputs.DataCollectionEndpointResponseNetworkAcls]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopedResources")
    def private_link_scoped_resources(self) -> Sequence[outputs.PrivateLinkScopedResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.DataCollectionEndpointResourceResponseSystemData:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDataCollectionEndpointResult(GetDataCollectionEndpointResult):
    def __await__(self): # -> Generator[Never, Any, GetDataCollectionEndpointResult]:
        ...
    


def get_data_collection_endpoint(data_collection_endpoint_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataCollectionEndpointResult:
    
    ...

def get_data_collection_endpoint_output(data_collection_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataCollectionEndpointResult]:
    
    ...

