

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGlobalClusterResult', 'AwaitableGetGlobalClusterResult', 'get_global_cluster', 'get_global_cluster_output']
@pulumi.output_type
class GetGlobalClusterResult:
    
    def __init__(__self__, arn=..., database_name=..., deletion_protection=..., endpoint=..., engine=..., engine_lifecycle_support=..., engine_version=..., id=..., identifier=..., members=..., region=..., resource_id=..., storage_encrypted=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineLifecycleSupport")
    def engine_lifecycle_support(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Sequence[outputs.GetGlobalClusterMemberResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetGlobalClusterResult(GetGlobalClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetGlobalClusterResult]:
        ...
    


def get_global_cluster(identifier: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGlobalClusterResult:
    
    ...

def get_global_cluster_output(identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGlobalClusterResult]:
    
    ...

