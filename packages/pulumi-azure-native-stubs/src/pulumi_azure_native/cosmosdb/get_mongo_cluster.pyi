

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMongoClusterResult', 'AwaitableGetMongoClusterResult', 'get_mongo_cluster', 'get_mongo_cluster_output']
@pulumi.output_type
class GetMongoClusterResult:
    
    def __init__(__self__, administrator_login=..., azure_api_version=..., cluster_status=..., connection_string=..., earliest_restore_time=..., id=..., location=..., name=..., node_group_specs=..., provisioning_state=..., server_version=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterStatus")
    def cluster_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="nodeGroupSpecs")
    def node_group_specs(self) -> Optional[Sequence[outputs.NodeGroupSpecResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
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
    


class AwaitableGetMongoClusterResult(GetMongoClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetMongoClusterResult]:
        ...
    


def get_mongo_cluster(mongo_cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMongoClusterResult:
    
    ...

def get_mongo_cluster_output(mongo_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMongoClusterResult]:
    
    ...

