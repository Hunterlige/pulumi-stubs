

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAttachedNetworkByDevCenterResult', 'AwaitableGetAttachedNetworkByDevCenterResult', 'get_attached_network_by_dev_center', 'get_attached_network_by_dev_center_output']
@pulumi.output_type
class GetAttachedNetworkByDevCenterResult:
    
    def __init__(__self__, azure_api_version=..., domain_join_type=..., health_check_status=..., id=..., name=..., network_connection_id=..., network_connection_location=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckStatus")
    def health_check_status(self) -> _builtins.str:
        
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
    @pulumi.getter(name="networkConnectionId")
    def network_connection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConnectionLocation")
    def network_connection_location(self) -> _builtins.str:
        
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
    


class AwaitableGetAttachedNetworkByDevCenterResult(GetAttachedNetworkByDevCenterResult):
    def __await__(self): # -> Generator[Never, Any, GetAttachedNetworkByDevCenterResult]:
        ...
    


def get_attached_network_by_dev_center(attached_network_connection_name: Optional[_builtins.str] = ..., dev_center_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAttachedNetworkByDevCenterResult:
    
    ...

def get_attached_network_by_dev_center_output(attached_network_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., dev_center_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAttachedNetworkByDevCenterResult]:
    
    ...

