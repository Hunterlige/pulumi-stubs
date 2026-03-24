

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
__all__ = ['GetInstanceTypeOfferingResult', 'AwaitableGetInstanceTypeOfferingResult', 'get_instance_type_offering', 'get_instance_type_offering_output']
@pulumi.output_type
class GetInstanceTypeOfferingResult:
    
    def __init__(__self__, filters=..., id=..., instance_type=..., location=..., location_type=..., preferred_instance_types=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInstanceTypeOfferingFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationType")
    def location_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredInstanceTypes")
    def preferred_instance_types(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceTypeOfferingResult(GetInstanceTypeOfferingResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceTypeOfferingResult]:
        ...
    


def get_instance_type_offering(filters: Optional[Sequence[Union[GetInstanceTypeOfferingFilterArgs, GetInstanceTypeOfferingFilterArgsDict]]] = ..., location_type: Optional[_builtins.str] = ..., preferred_instance_types: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceTypeOfferingResult:
    
    ...

def get_instance_type_offering_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetInstanceTypeOfferingFilterArgs, GetInstanceTypeOfferingFilterArgsDict]]]]] = ..., location_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., preferred_instance_types: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceTypeOfferingResult]:
    
    ...

