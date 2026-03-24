

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCapacityPoolSubvolumeMetadataResult', 'AwaitableGetCapacityPoolSubvolumeMetadataResult', 'get_capacity_pool_subvolume_metadata', 'get_capacity_pool_subvolume_metadata_output']
@pulumi.output_type
class GetCapacityPoolSubvolumeMetadataResult:
    
    def __init__(__self__, accessed_time_stamp=..., bytes_used=..., changed_time_stamp=..., creation_time_stamp=..., id=..., modified_time_stamp=..., name=..., parent_path=..., path=..., permissions=..., provisioning_state=..., size=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessedTimeStamp")
    def accessed_time_stamp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesUsed")
    def bytes_used(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTimeStamp")
    def changed_time_stamp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimeStamp")
    def creation_time_stamp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modifiedTimeStamp")
    def modified_time_stamp(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentPath")
    def parent_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCapacityPoolSubvolumeMetadataResult(GetCapacityPoolSubvolumeMetadataResult):
    def __await__(self): # -> Generator[Never, Any, GetCapacityPoolSubvolumeMetadataResult]:
        ...
    


def get_capacity_pool_subvolume_metadata(account_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., subvolume_name: Optional[_builtins.str] = ..., volume_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCapacityPoolSubvolumeMetadataResult:
    
    ...

def get_capacity_pool_subvolume_metadata_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., subvolume_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCapacityPoolSubvolumeMetadataResult]:
    
    ...

