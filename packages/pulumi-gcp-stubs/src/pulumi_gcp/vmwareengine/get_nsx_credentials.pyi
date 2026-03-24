

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNsxCredentialsResult', 'AwaitableGetNsxCredentialsResult', 'get_nsx_credentials', 'get_nsx_credentials_output']
@pulumi.output_type
class GetNsxCredentialsResult:
    
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
    


class AwaitableGetNsxCredentialsResult(GetNsxCredentialsResult):
    def __await__(self): # -> Generator[Never, Any, GetNsxCredentialsResult]:
        ...
    


def get_nsx_credentials(parent: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNsxCredentialsResult:
    
    ...

def get_nsx_credentials_output(parent: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNsxCredentialsResult]:
    
    ...

