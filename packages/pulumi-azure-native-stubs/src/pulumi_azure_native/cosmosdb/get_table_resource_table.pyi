

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTableResourceTableResult', 'AwaitableGetTableResourceTableResult', 'get_table_resource_table', 'get_table_resource_table_output']
@pulumi.output_type
class GetTableResourceTableResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., options=..., resource=..., tags=..., type=...) -> None:
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
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[outputs.TableGetPropertiesResponseOptions]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[outputs.TableGetPropertiesResponseResource]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTableResourceTableResult(GetTableResourceTableResult):
    def __await__(self): # -> Generator[Never, Any, GetTableResourceTableResult]:
        ...
    


def get_table_resource_table(account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., table_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTableResourceTableResult:
    
    ...

def get_table_resource_table_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTableResourceTableResult]:
    
    ...

