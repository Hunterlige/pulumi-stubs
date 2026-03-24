

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTriggerResult', 'AwaitableGetTriggerResult', 'get_trigger', 'get_trigger_output']
@pulumi.output_type
class GetTriggerResult:
    
    def __init__(__self__, azure_api_version=..., id=..., kind=..., name=..., provisioning_state=..., status=..., system_data=..., type=...) -> None:
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
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.TriggerStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTriggerResult(GetTriggerResult):
    def __await__(self): # -> Generator[Never, Any, GetTriggerResult]:
        ...
    


def get_trigger(image_template_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., trigger_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTriggerResult:
    
    ...

def get_trigger_output(image_template_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., trigger_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTriggerResult]:
    
    ...

