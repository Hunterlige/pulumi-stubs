

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResourceResult', 'AwaitableGetResourceResult', 'get_resource', 'get_resource_output']
@pulumi.output_type
class GetResourceResult:
    
    def __init__(__self__, id=..., identifier=..., properties=..., region=..., role_arn=..., type_name=..., type_version_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeVersionId")
    def type_version_id(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetResourceResult(GetResourceResult):
    def __await__(self): # -> Generator[Never, Any, GetResourceResult]:
        ...
    


def get_resource(identifier: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., role_arn: Optional[_builtins.str] = ..., type_name: Optional[_builtins.str] = ..., type_version_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourceResult:
    
    ...

def get_resource_output(identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., role_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type_name: Optional[pulumi.Input[_builtins.str]] = ..., type_version_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourceResult]:
    
    ...

