

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDotNetComponentResult', 'AwaitableGetDotNetComponentResult', 'get_dot_net_component', 'get_dot_net_component_output']
@pulumi.output_type
class GetDotNetComponentResult:
    
    def __init__(__self__, azure_api_version=..., component_type=..., configurations=..., id=..., name=..., provisioning_state=..., service_binds=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.DotNetComponentConfigurationPropertyResponse]]:
        
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
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence[outputs.DotNetComponentServiceBindResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDotNetComponentResult(GetDotNetComponentResult):
    def __await__(self): # -> Generator[Never, Any, GetDotNetComponentResult]:
        ...
    


def get_dot_net_component(environment_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDotNetComponentResult:
    
    ...

def get_dot_net_component_output(environment_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDotNetComponentResult]:
    
    ...

