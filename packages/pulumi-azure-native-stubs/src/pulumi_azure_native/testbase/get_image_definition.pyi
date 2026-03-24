

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetImageDefinitionResult', 'AwaitableGetImageDefinitionResult', 'get_image_definition', 'get_image_definition_output']
@pulumi.output_type
class GetImageDefinitionResult:
    
    def __init__(__self__, architecture=..., azure_api_version=..., id=..., name=..., os_state=..., provisioning_state=..., security_type=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> _builtins.str:
        
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
    @pulumi.getter(name="osState")
    def os_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityType")
    def security_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetImageDefinitionResult(GetImageDefinitionResult):
    def __await__(self): # -> Generator[Never, Any, GetImageDefinitionResult]:
        ...
    


def get_image_definition(image_definition_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., test_base_account_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetImageDefinitionResult:
    
    ...

def get_image_definition_output(image_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetImageDefinitionResult]:
    
    ...

