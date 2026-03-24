

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetComponentResult', 'AwaitableGetComponentResult', 'get_component', 'get_component_output']
@pulumi.output_type
class GetComponentResult:
    
    def __init__(__self__, app_id=..., application_id=..., application_type=..., azure_api_version=..., connection_string=..., creation_date=..., disable_ip_masking=..., disable_local_auth=..., etag=..., flow_type=..., force_customer_storage_for_profiler=..., hockey_app_id=..., hockey_app_token=..., id=..., immediate_purge_data_on30_days=..., ingestion_mode=..., instrumentation_key=..., kind=..., la_migration_date=..., location=..., name=..., private_link_scoped_resources=..., provisioning_state=..., public_network_access_for_ingestion=..., public_network_access_for_query=..., request_source=..., retention_in_days=..., sampling_percentage=..., tags=..., tenant_id=..., type=..., workspace_resource_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableIpMasking")
    def disable_ip_masking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowType")
    def flow_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceCustomerStorageForProfiler")
    def force_customer_storage_for_profiler(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hockeyAppId")
    def hockey_app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hockeyAppToken")
    def hockey_app_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immediatePurgeDataOn30Days")
    def immediate_purge_data_on30_days(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instrumentationKey")
    def instrumentation_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="laMigrationDate")
    def la_migration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
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
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestSource")
    def request_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="samplingPercentage")
    def sampling_percentage(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetComponentResult(GetComponentResult):
    def __await__(self): # -> Generator[Never, Any, GetComponentResult]:
        ...
    


def get_component(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetComponentResult:
    
    ...

def get_component_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetComponentResult]:
    
    ...

