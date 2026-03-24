

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAclResult', 'AwaitableGetWebAclResult', 'get_web_acl', 'get_web_acl_output']
@pulumi.output_type
class GetWebAclResult:
    
    def __init__(__self__, id=..., name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


class AwaitableGetWebAclResult(GetWebAclResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAclResult]:
        ...
    


def get_web_acl(name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAclResult:
    
    ...

def get_web_acl_output(name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAclResult]:
    
    ...

