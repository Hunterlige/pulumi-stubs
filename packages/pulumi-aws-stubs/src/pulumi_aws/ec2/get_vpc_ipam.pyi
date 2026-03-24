

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpcIpamResult', 'AwaitableGetVpcIpamResult', 'get_vpc_ipam', 'get_vpc_ipam_output']
@pulumi.output_type
class GetVpcIpamResult:
    
    def __init__(__self__, arn=..., default_resource_discovery_association_id=..., default_resource_discovery_id=..., description=..., enable_private_gua=..., id=..., ipam_region=..., metered_account=..., operating_regions=..., owner_id=..., private_default_scope_id=..., public_default_scope_id=..., region=..., resource_discovery_association_count=..., scope_count=..., state=..., state_message=..., tags=..., tier=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryAssociationId")
    def default_resource_discovery_association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultResourceDiscoveryId")
    def default_resource_discovery_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateGua")
    def enable_private_gua(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamRegion")
    def ipam_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="meteredAccount")
    def metered_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingRegions")
    def operating_regions(self) -> Sequence[outputs.GetVpcIpamOperatingRegionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDefaultScopeId")
    def private_default_scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDefaultScopeId")
    def public_default_scope_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceDiscoveryAssociationCount")
    def resource_discovery_association_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeCount")
    def scope_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVpcIpamResult(GetVpcIpamResult):
    def __await__(self): # -> Generator[Never, Any, GetVpcIpamResult]:
        ...
    


def get_vpc_ipam(id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpcIpamResult:
    
    ...

def get_vpc_ipam_output(id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpcIpamResult]:
    
    ...

