

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStorageMoverResult', 'AwaitableGetStorageMoverResult', 'get_storage_mover', 'get_storage_mover_output']
@pulumi.output_type
class GetStorageMoverResult:
    
    def __init__(__self__, azure_api_version=..., description=..., id=..., location=..., name=..., provisioning_state=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
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
    


class AwaitableGetStorageMoverResult(GetStorageMoverResult):
    def __await__(self): # -> Generator[Never, Any, GetStorageMoverResult]:
        ...
    


def get_storage_mover(resource_group_name: Optional[_builtins.str] = ..., storage_mover_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStorageMoverResult:
    
    ...

def get_storage_mover_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_mover_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStorageMoverResult]:
    
    ...

