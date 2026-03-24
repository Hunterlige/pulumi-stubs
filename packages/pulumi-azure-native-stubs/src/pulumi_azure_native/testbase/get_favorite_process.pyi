

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFavoriteProcessResult', 'AwaitableGetFavoriteProcessResult', 'get_favorite_process', 'get_favorite_process_output']
@pulumi.output_type
class GetFavoriteProcessResult:
    
    def __init__(__self__, actual_process_name=..., azure_api_version=..., id=..., name=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actualProcessName")
    def actual_process_name(self) -> _builtins.str:
        
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFavoriteProcessResult(GetFavoriteProcessResult):
    def __await__(self): # -> Generator[Never, Any, GetFavoriteProcessResult]:
        ...
    


def get_favorite_process(favorite_process_resource_name: Optional[_builtins.str] = ..., package_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., test_base_account_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFavoriteProcessResult:
    
    ...

def get_favorite_process_output(favorite_process_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., package_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFavoriteProcessResult]:
    
    ...

