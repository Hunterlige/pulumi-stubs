

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStorageDiscoveryWorkspaceResult', 'AwaitableGetStorageDiscoveryWorkspaceResult', 'get_storage_discovery_workspace', 'get_storage_discovery_workspace_output']
@pulumi.output_type
class GetStorageDiscoveryWorkspaceResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
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
    @pulumi.getter
    def properties(self) -> outputs.StorageDiscoveryWorkspacePropertiesResponse:
        
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
    


class AwaitableGetStorageDiscoveryWorkspaceResult(GetStorageDiscoveryWorkspaceResult):
    def __await__(self): # -> Generator[Never, Any, GetStorageDiscoveryWorkspaceResult]:
        ...
    


def get_storage_discovery_workspace(resource_group_name: Optional[_builtins.str] = ..., storage_discovery_workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStorageDiscoveryWorkspaceResult:
    
    ...

def get_storage_discovery_workspace_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_discovery_workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStorageDiscoveryWorkspaceResult]:
    
    ...

