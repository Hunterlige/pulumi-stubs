

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetScopingConfigurationResult', 'AwaitableGetScopingConfigurationResult', 'get_scoping_configuration', 'get_scoping_configuration_output']
@pulumi.output_type
class GetScopingConfigurationResult:
    
    def __init__(__self__, answers=..., azure_api_version=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def answers(self) -> Optional[Sequence[outputs.ScopingAnswerResponse]]:
        
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
    


class AwaitableGetScopingConfigurationResult(GetScopingConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetScopingConfigurationResult]:
        ...
    


def get_scoping_configuration(report_name: Optional[_builtins.str] = ..., scoping_configuration_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetScopingConfigurationResult:
    
    ...

def get_scoping_configuration_output(report_name: Optional[pulumi.Input[_builtins.str]] = ..., scoping_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetScopingConfigurationResult]:
    
    ...

