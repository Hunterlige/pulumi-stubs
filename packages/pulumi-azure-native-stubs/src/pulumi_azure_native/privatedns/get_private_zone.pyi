

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateZoneResult', 'AwaitableGetPrivateZoneResult', 'get_private_zone', 'get_private_zone_output']
@pulumi.output_type
class GetPrivateZoneResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., internal_id=..., location=..., max_number_of_record_sets=..., max_number_of_virtual_network_links=..., max_number_of_virtual_network_links_with_registration=..., name=..., number_of_record_sets=..., number_of_virtual_network_links=..., number_of_virtual_network_links_with_registration=..., provisioning_state=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNumberOfRecordSets")
    def max_number_of_record_sets(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNumberOfVirtualNetworkLinks")
    def max_number_of_virtual_network_links(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNumberOfVirtualNetworkLinksWithRegistration")
    def max_number_of_virtual_network_links_with_registration(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfRecordSets")
    def number_of_record_sets(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfVirtualNetworkLinks")
    def number_of_virtual_network_links(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfVirtualNetworkLinksWithRegistration")
    def number_of_virtual_network_links_with_registration(self) -> _builtins.float:
        
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
    


class AwaitableGetPrivateZoneResult(GetPrivateZoneResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateZoneResult]:
        ...
    


def get_private_zone(private_zone_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateZoneResult:
    
    ...

def get_private_zone_output(private_zone_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateZoneResult]:
    
    ...

