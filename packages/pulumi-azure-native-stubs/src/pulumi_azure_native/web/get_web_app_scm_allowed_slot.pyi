

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppScmAllowedSlotResult', 'AwaitableGetWebAppScmAllowedSlotResult', 'get_web_app_scm_allowed_slot', 'get_web_app_scm_allowed_slot_output']
@pulumi.output_type
class GetWebAppScmAllowedSlotResult:
    
    def __init__(__self__, allow=..., azure_api_version=..., id=..., kind=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> _builtins.bool:
        
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
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebAppScmAllowedSlotResult(GetWebAppScmAllowedSlotResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppScmAllowedSlotResult]:
        ...
    


def get_web_app_scm_allowed_slot(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., slot: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppScmAllowedSlotResult:
    
    ...

def get_web_app_scm_allowed_slot_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppScmAllowedSlotResult]:
    
    ...

