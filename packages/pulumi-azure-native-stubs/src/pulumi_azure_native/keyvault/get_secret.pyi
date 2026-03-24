

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecretResult', 'AwaitableGetSecretResult', 'get_secret', 'get_secret_output']
@pulumi.output_type
class GetSecretResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter
    def properties(self) -> outputs.SecretPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSecretResult(GetSecretResult):
    def __await__(self): # -> Generator[Never, Any, GetSecretResult]:
        ...
    


def get_secret(resource_group_name: Optional[_builtins.str] = ..., secret_name: Optional[_builtins.str] = ..., vault_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecretResult:
    
    ...

def get_secret_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., secret_name: Optional[pulumi.Input[_builtins.str]] = ..., vault_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecretResult]:
    
    ...

