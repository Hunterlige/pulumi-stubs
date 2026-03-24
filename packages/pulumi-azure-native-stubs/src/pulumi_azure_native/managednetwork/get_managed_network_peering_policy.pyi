

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedNetworkPeeringPolicyResult', 'AwaitableGetManagedNetworkPeeringPolicyResult', 'get_managed_network_peering_policy', 'get_managed_network_peering_policy_output']
@pulumi.output_type
class GetManagedNetworkPeeringPolicyResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., type=...) -> None:
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
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ManagedNetworkPeeringPolicyPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagedNetworkPeeringPolicyResult(GetManagedNetworkPeeringPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedNetworkPeeringPolicyResult]:
        ...
    


def get_managed_network_peering_policy(managed_network_name: Optional[_builtins.str] = ..., managed_network_peering_policy_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedNetworkPeeringPolicyResult:
    
    ...

def get_managed_network_peering_policy_output(managed_network_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_network_peering_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedNetworkPeeringPolicyResult]:
    
    ...

