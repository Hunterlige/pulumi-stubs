

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVolumeGroupResult', 'AwaitableGetVolumeGroupResult', 'get_volume_group', 'get_volume_group_output']
@pulumi.output_type
class GetVolumeGroupResult:
    
    def __init__(__self__, azure_api_version=..., group_meta_data=..., id=..., location=..., name=..., provisioning_state=..., type=..., volumes=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupMetaData")
    def group_meta_data(self) -> Optional[outputs.VolumeGroupMetaDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.VolumeGroupVolumePropertiesResponse]]:
        
        ...
    


class AwaitableGetVolumeGroupResult(GetVolumeGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetVolumeGroupResult]:
        ...
    


def get_volume_group(account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., volume_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVolumeGroupResult:
    
    ...

def get_volume_group_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVolumeGroupResult]:
    
    ...

