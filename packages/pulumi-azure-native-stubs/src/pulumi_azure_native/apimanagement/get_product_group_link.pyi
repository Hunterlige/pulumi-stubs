

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProductGroupLinkResult', 'AwaitableGetProductGroupLinkResult', 'get_product_group_link', 'get_product_group_link_output']
@pulumi.output_type
class GetProductGroupLinkResult:
    
    def __init__(__self__, azure_api_version=..., group_id=..., id=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetProductGroupLinkResult(GetProductGroupLinkResult):
    def __await__(self): # -> Generator[Never, Any, GetProductGroupLinkResult]:
        ...
    


def get_product_group_link(group_link_id: Optional[_builtins.str] = ..., product_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProductGroupLinkResult:
    
    ...

def get_product_group_link_output(group_link_id: Optional[pulumi.Input[_builtins.str]] = ..., product_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProductGroupLinkResult]:
    
    ...

