

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListActiveConnectivityConfigurationResult', 'AwaitableListActiveConnectivityConfigurationResult', 'list_active_connectivity_configuration', 'list_active_connectivity_configuration_output']
@pulumi.output_type
class ListActiveConnectivityConfigurationResult:
    
    def __init__(__self__, skip_token=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ActiveConnectivityConfigurationResponse]]:
        
        ...
    


class AwaitableListActiveConnectivityConfigurationResult(ListActiveConnectivityConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, ListActiveConnectivityConfigurationResult]:
        ...
    


def list_active_connectivity_configuration(network_manager_name: Optional[_builtins.str] = ..., regions: Optional[Sequence[_builtins.str]] = ..., resource_group_name: Optional[_builtins.str] = ..., skip_token: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListActiveConnectivityConfigurationResult:
    
    ...

def list_active_connectivity_configuration_output(network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., regions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListActiveConnectivityConfigurationResult]:
    
    ...

