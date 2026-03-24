

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGen2EnvironmentResult', 'AwaitableGetGen2EnvironmentResult', 'get_gen2_environment', 'get_gen2_environment_output']
@pulumi.output_type
class GetGen2EnvironmentResult:
    
    def __init__(__self__, azure_api_version=..., creation_time=..., data_access_fqdn=..., data_access_id=..., id=..., kind=..., location=..., name=..., provisioning_state=..., sku=..., status=..., storage_configuration=..., tags=..., time_series_id_properties=..., type=..., warm_store_configuration=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessFqdn")
    def data_access_fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessId")
    def data_access_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.EnvironmentStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfiguration")
    def storage_configuration(self) -> outputs.Gen2StorageConfigurationOutputResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeriesIdProperties")
    def time_series_id_properties(self) -> Sequence[outputs.TimeSeriesIdPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmStoreConfiguration")
    def warm_store_configuration(self) -> Optional[outputs.WarmStoreConfigurationPropertiesResponse]:
        
        ...
    


class AwaitableGetGen2EnvironmentResult(GetGen2EnvironmentResult):
    def __await__(self): # -> Generator[Never, Any, GetGen2EnvironmentResult]:
        ...
    


def get_gen2_environment(environment_name: Optional[_builtins.str] = ..., expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGen2EnvironmentResult:
    
    ...

def get_gen2_environment_output(environment_name: Optional[pulumi.Input[_builtins.str]] = ..., expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGen2EnvironmentResult]:
    
    ...

