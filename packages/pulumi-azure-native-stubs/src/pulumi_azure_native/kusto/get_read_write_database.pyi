

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReadWriteDatabaseResult', 'AwaitableGetReadWriteDatabaseResult', 'get_read_write_database', 'get_read_write_database_output']
@pulumi.output_type
class GetReadWriteDatabaseResult:
    
    def __init__(__self__, azure_api_version=..., hot_cache_period=..., id=..., is_followed=..., key_vault_properties=..., kind=..., location=..., name=..., provisioning_state=..., soft_delete_period=..., statistics=..., suspension_details=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFollowed")
    def is_followed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statistics(self) -> outputs.DatabaseStatisticsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspensionDetails")
    def suspension_details(self) -> outputs.SuspensionDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetReadWriteDatabaseResult(GetReadWriteDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetReadWriteDatabaseResult]:
        ...
    


def get_read_write_database(cluster_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReadWriteDatabaseResult:
    
    ...

def get_read_write_database_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReadWriteDatabaseResult]:
    
    ...

