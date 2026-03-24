

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVcenterCredentialsResult', 'AwaitableGetVcenterCredentialsResult', 'get_vcenter_credentials', 'get_vcenter_credentials_output']
@pulumi.output_type
class GetVcenterCredentialsResult:
    
    def __init__(__self__, id=..., parent=..., password=..., username=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVcenterCredentialsResult(GetVcenterCredentialsResult):
    def __await__(self): # -> Generator[Never, Any, GetVcenterCredentialsResult]:
        ...
    


def get_vcenter_credentials(parent: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVcenterCredentialsResult:
    
    ...

def get_vcenter_credentials_output(parent: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVcenterCredentialsResult]:
    
    ...

