

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStorageTargetResult', 'AwaitableGetStorageTargetResult', 'get_storage_target', 'get_storage_target_output']
@pulumi.output_type
class GetStorageTargetResult:
    
    def __init__(__self__, allocation_percentage=..., azure_api_version=..., blob_nfs=..., clfs=..., id=..., junctions=..., location=..., name=..., nfs3=..., provisioning_state=..., state=..., system_data=..., target_type=..., type=..., unknown=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationPercentage")
    def allocation_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobNfs")
    def blob_nfs(self) -> Optional[outputs.BlobNfsTargetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clfs(self) -> Optional[outputs.ClfsTargetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def junctions(self) -> Optional[Sequence[outputs.NamespaceJunctionResponse]]:
        
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
    def nfs3(self) -> Optional[outputs.Nfs3TargetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unknown(self) -> Optional[outputs.UnknownTargetResponse]:
        
        ...
    


class AwaitableGetStorageTargetResult(GetStorageTargetResult):
    def __await__(self): # -> Generator[Never, Any, GetStorageTargetResult]:
        ...
    


def get_storage_target(cache_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., storage_target_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStorageTargetResult:
    
    ...

def get_storage_target_output(cache_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_target_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStorageTargetResult]:
    
    ...

