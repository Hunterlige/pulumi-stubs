

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDraftPackagePathResult', 'AwaitableGetDraftPackagePathResult', 'get_draft_package_path', 'get_draft_package_path_output']
@pulumi.output_type
class GetDraftPackagePathResult:
    
    def __init__(__self__, base_url=..., draft_package_path=..., expiration_time=..., sas_token=..., working_path=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="draftPackagePath")
    def draft_package_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingPath")
    def working_path(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDraftPackagePathResult(GetDraftPackagePathResult):
    def __await__(self): # -> Generator[Never, Any, GetDraftPackagePathResult]:
        ...
    


def get_draft_package_path(draft_package_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., test_base_account_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDraftPackagePathResult:
    
    ...

def get_draft_package_path_output(draft_package_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDraftPackagePathResult]:
    
    ...

