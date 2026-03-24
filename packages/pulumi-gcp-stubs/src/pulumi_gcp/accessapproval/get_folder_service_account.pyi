

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFolderServiceAccountResult', 'AwaitableGetFolderServiceAccountResult', 'get_folder_service_account', 'get_folder_service_account_output']
@pulumi.output_type
class GetFolderServiceAccountResult:
    
    def __init__(__self__, account_email=..., folder_id=..., id=..., name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountEmail")
    def account_email(self) -> _builtins.str:
        
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFolderServiceAccountResult(GetFolderServiceAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetFolderServiceAccountResult]:
        ...
    


def get_folder_service_account(folder_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFolderServiceAccountResult:
    
    ...

def get_folder_service_account_output(folder_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFolderServiceAccountResult]:
    
    ...

