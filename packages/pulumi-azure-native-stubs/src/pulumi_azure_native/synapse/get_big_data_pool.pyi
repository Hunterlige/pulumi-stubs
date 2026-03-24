

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBigDataPoolResult', 'AwaitableGetBigDataPoolResult', 'get_big_data_pool', 'get_big_data_pool_output']
@pulumi.output_type
class GetBigDataPoolResult:
    
    def __init__(__self__, auto_pause=..., auto_scale=..., azure_api_version=..., cache_size=..., creation_date=..., custom_libraries=..., default_spark_log_folder=..., dynamic_executor_allocation=..., id=..., is_autotune_enabled=..., is_compute_isolation_enabled=..., last_succeeded_timestamp=..., library_requirements=..., location=..., name=..., node_count=..., node_size=..., node_size_family=..., provisioning_state=..., session_level_packages_enabled=..., spark_config_properties=..., spark_events_folder=..., spark_version=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> Optional[outputs.AutoPausePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> Optional[outputs.AutoScalePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheSize")
    def cache_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLibraries")
    def custom_libraries(self) -> Optional[Sequence[outputs.LibraryInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSparkLogFolder")
    def default_spark_log_folder(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicExecutorAllocation")
    def dynamic_executor_allocation(self) -> Optional[outputs.DynamicExecutorAllocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutotuneEnabled")
    def is_autotune_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isComputeIsolationEnabled")
    def is_compute_isolation_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSucceededTimestamp")
    def last_succeeded_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="libraryRequirements")
    def library_requirements(self) -> Optional[outputs.LibraryRequirementsResponse]:
        
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
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSizeFamily")
    def node_size_family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionLevelPackagesEnabled")
    def session_level_packages_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkConfigProperties")
    def spark_config_properties(self) -> Optional[outputs.SparkConfigPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkEventsFolder")
    def spark_events_folder(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkVersion")
    def spark_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBigDataPoolResult(GetBigDataPoolResult):
    def __await__(self): # -> Generator[Never, Any, GetBigDataPoolResult]:
        ...
    


def get_big_data_pool(big_data_pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBigDataPoolResult:
    
    ...

def get_big_data_pool_output(big_data_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBigDataPoolResult]:
    
    ...

