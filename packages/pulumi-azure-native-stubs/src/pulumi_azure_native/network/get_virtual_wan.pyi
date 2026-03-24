

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualWanResult', 'AwaitableGetVirtualWanResult', 'get_virtual_wan', 'get_virtual_wan_output']
@pulumi.output_type
class GetVirtualWanResult:
    
    def __init__(__self__, allow_branch_to_branch_traffic=..., allow_vnet_to_vnet_traffic=..., azure_api_version=..., disable_vpn_encryption=..., etag=..., id=..., location=..., name=..., office365_local_breakout_category=..., provisioning_state=..., tags=..., type=..., virtual_hubs=..., vpn_sites=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowVnetToVnetTraffic")
    def allow_vnet_to_vnet_traffic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableVpnEncryption")
    def disable_vpn_encryption(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="office365LocalBreakoutCategory")
    def office365_local_breakout_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
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
    @pulumi.getter(name="virtualHubs")
    def virtual_hubs(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnSites")
    def vpn_sites(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    


class AwaitableGetVirtualWanResult(GetVirtualWanResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualWanResult]:
        ...
    


def get_virtual_wan(resource_group_name: Optional[_builtins.str] = ..., virtual_wan_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualWanResult:
    
    ...

def get_virtual_wan_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_wan_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualWanResult]:
    
    ...

