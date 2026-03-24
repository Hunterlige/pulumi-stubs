

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCapacityPoolCacheResult', 'AwaitableGetCapacityPoolCacheResult', 'get_capacity_pool_cache', 'get_capacity_pool_cache_output']
@pulumi.output_type
class GetCapacityPoolCacheResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter
    def properties(self) -> outputs.CachePropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetCapacityPoolCacheResult(GetCapacityPoolCacheResult):
    def __await__(self): # -> Generator[Never, Any, GetCapacityPoolCacheResult]:
        ...
    


def get_capacity_pool_cache(account_name: Optional[_builtins.str] = ..., cache_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCapacityPoolCacheResult:
    
    ...

def get_capacity_pool_cache_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., cache_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCapacityPoolCacheResult]:
    
    ...

