

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListGeodataByIpResult', 'AwaitableListGeodataByIpResult', 'list_geodata_by_ip', 'list_geodata_by_ip_output']
@pulumi.output_type
class ListGeodataByIpResult:
    
    def __init__(__self__, asn=..., carrier=..., city=..., city_confidence_factor=..., continent=..., country=..., country_confidence_factor=..., ip_addr=..., ip_routing_type=..., latitude=..., longitude=..., organization=..., organization_type=..., region=..., state=..., state_code=..., state_confidence_factor=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def carrier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cityConfidenceFactor")
    def city_confidence_factor(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def continent(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryConfidenceFactor")
    def country_confidence_factor(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddr")
    def ip_addr(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRoutingType")
    def ip_routing_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def latitude(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def longitude(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationType")
    def organization_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateCode")
    def state_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateConfidenceFactor")
    def state_confidence_factor(self) -> Optional[_builtins.int]:
        
        ...
    


class AwaitableListGeodataByIpResult(ListGeodataByIpResult):
    def __await__(self): # -> Generator[Never, Any, ListGeodataByIpResult]:
        ...
    


def list_geodata_by_ip(enrichment_type: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListGeodataByIpResult:
    
    ...

def list_geodata_by_ip_output(enrichment_type: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListGeodataByIpResult]:
    
    ...

