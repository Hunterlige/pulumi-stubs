

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRestorePointCollectionResult', 'AwaitableGetRestorePointCollectionResult', 'get_restore_point_collection', 'get_restore_point_collection_output']
@pulumi.output_type
class GetRestorePointCollectionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., provisioning_state=..., restore_point_collection_id=..., restore_points=..., source=..., system_data=..., tags=..., type=...) -> None:
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
    @pulumi.getter(name="restorePointCollectionId")
    def restore_point_collection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePoints")
    def restore_points(self) -> Sequence[outputs.RestorePointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[outputs.RestorePointCollectionSourcePropertiesResponse]:
        
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
    


class AwaitableGetRestorePointCollectionResult(GetRestorePointCollectionResult):
    def __await__(self): # -> Generator[Never, Any, GetRestorePointCollectionResult]:
        ...
    


def get_restore_point_collection(expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., restore_point_collection_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRestorePointCollectionResult:
    
    ...

def get_restore_point_collection_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRestorePointCollectionResult]:
    
    ...

