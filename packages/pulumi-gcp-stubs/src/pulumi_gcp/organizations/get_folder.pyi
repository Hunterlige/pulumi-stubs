

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFolderResult', 'AwaitableGetFolderResult', 'get_folder', 'get_folder_output']
@pulumi.output_type
class GetFolderResult:
    
    def __init__(__self__, configured_capabilities=..., create_time=..., deletion_protection=..., display_name=..., folder=..., folder_id=..., id=..., lifecycle_state=..., lookup_organization=..., management_project=..., name=..., organization=..., parent=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configuredCapabilities")
    def configured_capabilities(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookupOrganization")
    def lookup_organization(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementProject")
    def management_project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFolderResult(GetFolderResult):
    def __await__(self): # -> Generator[Never, Any, GetFolderResult]:
        ...
    


def get_folder(folder: Optional[_builtins.str] = ..., lookup_organization: Optional[_builtins.bool] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFolderResult:
    
    ...

def get_folder_output(folder: Optional[pulumi.Input[_builtins.str]] = ..., lookup_organization: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFolderResult]:
    
    ...

