

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceTypeOfferingsResult', 'AwaitableGetInstanceTypeOfferingsResult', 'get_instance_type_offerings', 'get_instance_type_offerings_output']
@pulumi.output_type
class GetInstanceTypeOfferingsResult:
    
    def __init__(__self__, filters=..., id=..., instance_types=..., location_type=..., location_types=..., locations=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInstanceTypeOfferingsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationType")
    def location_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationTypes")
    def location_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceTypeOfferingsResult(GetInstanceTypeOfferingsResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceTypeOfferingsResult]:
        ...
    


def get_instance_type_offerings(filters: Optional[Sequence[Union[GetInstanceTypeOfferingsFilterArgs, GetInstanceTypeOfferingsFilterArgsDict]]] = ..., location_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceTypeOfferingsResult:
    
    ...

def get_instance_type_offerings_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetInstanceTypeOfferingsFilterArgs, GetInstanceTypeOfferingsFilterArgsDict]]]]] = ..., location_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceTypeOfferingsResult]:
    
    ...

