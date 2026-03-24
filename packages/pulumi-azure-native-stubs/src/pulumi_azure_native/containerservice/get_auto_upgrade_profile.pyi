

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAutoUpgradeProfileResult', 'AwaitableGetAutoUpgradeProfileResult', 'get_auto_upgrade_profile', 'get_auto_upgrade_profile_output']
@pulumi.output_type
class GetAutoUpgradeProfileResult:
    
    def __init__(__self__, azure_api_version=..., channel=..., disabled=..., e_tag=..., id=..., name=..., node_image_selection=..., provisioning_state=..., system_data=..., type=..., update_strategy_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
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
    @pulumi.getter(name="nodeImageSelection")
    def node_image_selection(self) -> Optional[outputs.AutoUpgradeNodeImageSelectionResponse]:
        
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
    
    @_builtins.property
    @pulumi.getter(name="updateStrategyId")
    def update_strategy_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetAutoUpgradeProfileResult(GetAutoUpgradeProfileResult):
    def __await__(self): # -> Generator[Never, Any, GetAutoUpgradeProfileResult]:
        ...
    


def get_auto_upgrade_profile(auto_upgrade_profile_name: Optional[_builtins.str] = ..., fleet_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAutoUpgradeProfileResult:
    
    ...

def get_auto_upgrade_profile_output(auto_upgrade_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., fleet_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAutoUpgradeProfileResult]:
    
    ...

