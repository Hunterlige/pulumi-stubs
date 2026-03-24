

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCredentialsResult', 'AwaitableGetCredentialsResult', 'get_credentials', 'get_credentials_output']
@pulumi.output_type
class GetCredentialsResult:
    
    def __init__(__self__, db_name=..., db_password=..., db_user=..., duration_seconds=..., expiration=..., id=..., region=..., workgroup_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbPassword")
    def db_password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> _builtins.str:
        ...
    


class AwaitableGetCredentialsResult(GetCredentialsResult):
    def __await__(self): # -> Generator[Never, Any, GetCredentialsResult]:
        ...
    


def get_credentials(db_name: Optional[_builtins.str] = ..., duration_seconds: Optional[_builtins.int] = ..., region: Optional[_builtins.str] = ..., workgroup_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCredentialsResult:
    
    ...

def get_credentials_output(db_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., duration_seconds: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCredentialsResult]:
    
    ...

