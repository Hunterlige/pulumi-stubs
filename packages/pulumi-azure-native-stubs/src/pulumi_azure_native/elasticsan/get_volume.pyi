

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVolumeResult', 'AwaitableGetVolumeResult', 'get_volume', 'get_volume_output']
@pulumi.output_type
class GetVolumeResult:
    
    def __init__(__self__, azure_api_version=..., creation_data=..., id=..., managed_by=..., name=..., provisioning_state=..., size_gi_b=..., storage_target=..., system_data=..., type=..., volume_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional[outputs.SourceCreationDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[outputs.ManagedByInfoResponse]:
        
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
    @pulumi.getter(name="sizeGiB")
    def size_gi_b(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageTarget")
    def storage_target(self) -> outputs.IscsiTargetInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVolumeResult(GetVolumeResult):
    def __await__(self): # -> Generator[Never, Any, GetVolumeResult]:
        ...
    


def get_volume(elastic_san_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., volume_group_name: Optional[_builtins.str] = ..., volume_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVolumeResult:
    
    ...

def get_volume_output(elastic_san_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVolumeResult]:
    
    ...

