

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEdgeActionVersionResult', 'AwaitableGetEdgeActionVersionResult', 'get_edge_action_version', 'get_edge_action_version_output']
@pulumi.output_type
class GetEdgeActionVersionResult:
    
    def __init__(__self__, azure_api_version=..., deployment_type=..., id=..., is_default_version=..., last_package_update_time=..., location=..., name=..., provisioning_state=..., system_data=..., tags=..., type=..., validation_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPackageUpdateTime")
    def last_package_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
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
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEdgeActionVersionResult(GetEdgeActionVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetEdgeActionVersionResult]:
        ...
    


def get_edge_action_version(edge_action_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEdgeActionVersionResult:
    
    ...

def get_edge_action_version_output(edge_action_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEdgeActionVersionResult]:
    
    ...

