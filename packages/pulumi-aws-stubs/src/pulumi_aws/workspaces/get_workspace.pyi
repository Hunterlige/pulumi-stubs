

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceResult', 'AwaitableGetWorkspaceResult', 'get_workspace', 'get_workspace_output']
@pulumi.output_type
class GetWorkspaceResult:
    
    def __init__(__self__, bundle_id=..., computer_name=..., directory_id=..., id=..., ip_address=..., region=..., root_volume_encryption_enabled=..., state=..., tags=..., user_name=..., user_volume_encryption_enabled=..., volume_encryption_key=..., workspace_id=..., workspace_properties=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computerName")
    def computer_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeEncryptionKey")
    def volume_encryption_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceProperties")
    def workspace_properties(self) -> Sequence[outputs.GetWorkspaceWorkspacePropertyResult]:
        
        ...
    


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceResult]:
        ...
    


def get_workspace(directory_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., user_name: Optional[_builtins.str] = ..., workspace_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceResult:
    
    ...

def get_workspace_output(directory_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., user_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workspace_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceResult]:
    
    ...

