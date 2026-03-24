

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCopilotSettingResult', 'AwaitableGetCopilotSettingResult', 'get_copilot_setting', 'get_copilot_setting_output']
@pulumi.output_type
class GetCopilotSettingResult:
    
    def __init__(__self__, access_control_enabled=..., azure_api_version=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlEnabled")
    def access_control_enabled(self) -> _builtins.bool:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCopilotSettingResult(GetCopilotSettingResult):
    def __await__(self): # -> Generator[Never, Any, GetCopilotSettingResult]:
        ...
    


def get_copilot_setting(opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCopilotSettingResult:
    
    ...

def get_copilot_setting_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCopilotSettingResult]:
    
    ...

