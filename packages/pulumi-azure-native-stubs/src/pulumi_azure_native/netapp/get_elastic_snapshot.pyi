

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetElasticSnapshotResult', 'AwaitableGetElasticSnapshotResult', 'get_elastic_snapshot', 'get_elastic_snapshot_output']
@pulumi.output_type
class GetElasticSnapshotResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ElasticSnapshotPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetElasticSnapshotResult(GetElasticSnapshotResult):
    def __await__(self): # -> Generator[Never, Any, GetElasticSnapshotResult]:
        ...
    


def get_elastic_snapshot(account_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., snapshot_name: Optional[_builtins.str] = ..., volume_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetElasticSnapshotResult:
    
    ...

def get_elastic_snapshot_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetElasticSnapshotResult]:
    
    ...

