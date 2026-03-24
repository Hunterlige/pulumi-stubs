

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFleetAnalyticResult', 'AwaitableGetFleetAnalyticResult', 'get_fleet_analytic', 'get_fleet_analytic_output']
@pulumi.output_type
class GetFleetAnalyticResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., provisioning_state=..., storage_location_type=..., storage_location_uri=..., system_data=..., type=...) -> None:
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
    @pulumi.getter(name="storageLocationType")
    def storage_location_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocationUri")
    def storage_location_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFleetAnalyticResult(GetFleetAnalyticResult):
    def __await__(self): # -> Generator[Never, Any, GetFleetAnalyticResult]:
        ...
    


def get_fleet_analytic(fleet_analytics_name: Optional[_builtins.str] = ..., fleet_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFleetAnalyticResult:
    
    ...

def get_fleet_analytic_output(fleet_analytics_name: Optional[pulumi.Input[_builtins.str]] = ..., fleet_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFleetAnalyticResult]:
    
    ...

