

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOutpostResult', 'AwaitableGetOutpostResult', 'get_outpost', 'get_outpost_output']
@pulumi.output_type
class GetOutpostResult:
    
    def __init__(__self__, arn=..., availability_zone=..., availability_zone_id=..., description=..., id=..., lifecycle_status=..., name=..., owner_id=..., region=..., site_arn=..., site_id=..., supported_hardware_type=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleStatus")
    def lifecycle_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteArn")
    def site_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedHardwareType")
    def supported_hardware_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetOutpostResult(GetOutpostResult):
    def __await__(self): # -> Generator[Never, Any, GetOutpostResult]:
        ...
    


def get_outpost(arn: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., owner_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOutpostResult:
    
    ...

def get_outpost_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., owner_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOutpostResult]:
    
    ...

