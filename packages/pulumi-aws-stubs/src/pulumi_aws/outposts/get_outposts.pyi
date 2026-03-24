

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOutpostsResult', 'AwaitableGetOutpostsResult', 'get_outposts', 'get_outposts_output']
@pulumi.output_type
class GetOutpostsResult:
    
    def __init__(__self__, arns=..., availability_zone=..., availability_zone_id=..., id=..., ids=..., owner_id=..., region=..., site_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
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
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        ...
    


class AwaitableGetOutpostsResult(GetOutpostsResult):
    def __await__(self): # -> Generator[Never, Any, GetOutpostsResult]:
        ...
    


def get_outposts(availability_zone: Optional[_builtins.str] = ..., availability_zone_id: Optional[_builtins.str] = ..., owner_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., site_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOutpostsResult:
    
    ...

def get_outposts_output(availability_zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., availability_zone_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., owner_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., site_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOutpostsResult]:
    
    ...

