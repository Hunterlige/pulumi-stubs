

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceStorageConfigResult', 'AwaitableGetInstanceStorageConfigResult', 'get_instance_storage_config', 'get_instance_storage_config_output']
@pulumi.output_type
class GetInstanceStorageConfigResult:
    
    def __init__(__self__, association_id=..., id=..., instance_id=..., region=..., resource_type=..., storage_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfigs")
    def storage_configs(self) -> Sequence[outputs.GetInstanceStorageConfigStorageConfigResult]:
        
        ...
    


class AwaitableGetInstanceStorageConfigResult(GetInstanceStorageConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceStorageConfigResult]:
        ...
    


def get_instance_storage_config(association_id: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceStorageConfigResult:
    
    ...

def get_instance_storage_config_output(association_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceStorageConfigResult]:
    
    ...

