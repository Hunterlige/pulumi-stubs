

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFolderSettingsResult', 'AwaitableGetFolderSettingsResult', 'get_folder_settings', 'get_folder_settings_output']
@pulumi.output_type
class GetFolderSettingsResult:
    
    def __init__(__self__, default_storage_location=..., folder=..., id=..., kms_key_name=..., location=..., name=..., service_account_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultStorageLocation")
    def default_storage_location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
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
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> _builtins.str:
        ...
    


class AwaitableGetFolderSettingsResult(GetFolderSettingsResult):
    def __await__(self): # -> Generator[Never, Any, GetFolderSettingsResult]:
        ...
    


def get_folder_settings(folder: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFolderSettingsResult:
    
    ...

def get_folder_settings_output(folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFolderSettingsResult]:
    
    ...

