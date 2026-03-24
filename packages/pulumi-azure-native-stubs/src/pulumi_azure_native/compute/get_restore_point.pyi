

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRestorePointResult', 'AwaitableGetRestorePointResult', 'get_restore_point', 'get_restore_point_output']
@pulumi.output_type
class GetRestorePointResult:
    
    def __init__(__self__, azure_api_version=..., consistency_mode=..., exclude_disks=..., id=..., instance_view=..., name=..., provisioning_state=..., source_metadata=..., source_restore_point=..., system_data=..., time_created=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consistencyMode")
    def consistency_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeDisks")
    def exclude_disks(self) -> Optional[Sequence[outputs.ApiEntityReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.RestorePointInstanceViewResponse:
        
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
    @pulumi.getter(name="sourceMetadata")
    def source_metadata(self) -> Optional[outputs.RestorePointSourceMetadataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRestorePoint")
    def source_restore_point(self) -> Optional[outputs.ApiEntityReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRestorePointResult(GetRestorePointResult):
    def __await__(self): # -> Generator[Never, Any, GetRestorePointResult]:
        ...
    


def get_restore_point(expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., restore_point_collection_name: Optional[_builtins.str] = ..., restore_point_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRestorePointResult:
    
    ...

def get_restore_point_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRestorePointResult]:
    
    ...

