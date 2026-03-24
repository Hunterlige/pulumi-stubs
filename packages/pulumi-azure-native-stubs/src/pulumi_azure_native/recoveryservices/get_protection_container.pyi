

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProtectionContainerResult', 'AwaitableGetProtectionContainerResult', 'get_protection_container', 'get_protection_container_output']
@pulumi.output_type
class GetProtectionContainerResult:
    
    def __init__(__self__, azure_api_version=..., e_tag=..., id=..., location=..., name=..., properties=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetProtectionContainerResult(GetProtectionContainerResult):
    def __await__(self): # -> Generator[Never, Any, GetProtectionContainerResult]:
        ...
    


def get_protection_container(container_name: Optional[_builtins.str] = ..., fabric_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., vault_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProtectionContainerResult:
    
    ...

def get_protection_container_output(container_name: Optional[pulumi.Input[_builtins.str]] = ..., fabric_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vault_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProtectionContainerResult]:
    
    ...

