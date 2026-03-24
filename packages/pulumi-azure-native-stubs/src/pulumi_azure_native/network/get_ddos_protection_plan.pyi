

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDdosProtectionPlanResult', 'AwaitableGetDdosProtectionPlanResult', 'get_ddos_protection_plan', 'get_ddos_protection_plan_output']
@pulumi.output_type
class GetDdosProtectionPlanResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., location=..., name=..., provisioning_state=..., public_ip_addresses=..., resource_guid=..., tags=..., type=..., virtual_networks=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddresses")
    def public_ip_addresses(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
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
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    


class AwaitableGetDdosProtectionPlanResult(GetDdosProtectionPlanResult):
    def __await__(self): # -> Generator[Never, Any, GetDdosProtectionPlanResult]:
        ...
    


def get_ddos_protection_plan(ddos_protection_plan_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDdosProtectionPlanResult:
    
    ...

def get_ddos_protection_plan_output(ddos_protection_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDdosProtectionPlanResult]:
    
    ...

