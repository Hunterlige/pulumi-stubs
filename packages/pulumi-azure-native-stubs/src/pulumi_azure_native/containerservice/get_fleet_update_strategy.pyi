

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFleetUpdateStrategyResult', 'AwaitableGetFleetUpdateStrategyResult', 'get_fleet_update_strategy', 'get_fleet_update_strategy_output']
@pulumi.output_type
class GetFleetUpdateStrategyResult:
    
    def __init__(__self__, azure_api_version=..., e_tag=..., id=..., name=..., provisioning_state=..., strategy=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str:
        
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
    @pulumi.getter
    def strategy(self) -> outputs.UpdateRunStrategyResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFleetUpdateStrategyResult(GetFleetUpdateStrategyResult):
    def __await__(self): # -> Generator[Never, Any, GetFleetUpdateStrategyResult]:
        ...
    


def get_fleet_update_strategy(fleet_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., update_strategy_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFleetUpdateStrategyResult:
    
    ...

def get_fleet_update_strategy_output(fleet_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., update_strategy_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFleetUpdateStrategyResult]:
    
    ...

