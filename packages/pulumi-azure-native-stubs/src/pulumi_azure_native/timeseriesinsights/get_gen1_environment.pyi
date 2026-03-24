

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGen1EnvironmentResult', 'AwaitableGetGen1EnvironmentResult', 'get_gen1_environment', 'get_gen1_environment_output']
@pulumi.output_type
class GetGen1EnvironmentResult:
    
    def __init__(__self__, azure_api_version=..., creation_time=..., data_access_fqdn=..., data_access_id=..., data_retention_time=..., id=..., kind=..., location=..., name=..., partition_key_properties=..., provisioning_state=..., sku=..., status=..., storage_limit_exceeded_behavior=..., tags=..., type=...) -> None:
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
    @pulumi.getter(name="dataRetentionTime")
    def data_retention_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="partitionKeyProperties")
    def partition_key_properties(self) -> Optional[Sequence[outputs.TimeSeriesIdPropertyResponse]]:
        
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
    @pulumi.getter(name="storageLimitExceededBehavior")
    def storage_limit_exceeded_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetGen1EnvironmentResult(GetGen1EnvironmentResult):
    def __await__(self): # -> Generator[Never, Any, GetGen1EnvironmentResult]:
        ...
    


def get_gen1_environment(environment_name: Optional[_builtins.str] = ..., expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGen1EnvironmentResult:
    
    ...

def get_gen1_environment_output(environment_name: Optional[pulumi.Input[_builtins.str]] = ..., expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGen1EnvironmentResult]:
    
    ...

