

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSlotTypeResult', 'AwaitableGetSlotTypeResult', 'get_slot_type', 'get_slot_type_output']
@pulumi.output_type
class GetSlotTypeResult:
    
    def __init__(__self__, checksum=..., created_date=..., description=..., enumeration_values=..., id=..., last_updated_date=..., name=..., region=..., value_selection_strategy=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enumerationValues")
    def enumeration_values(self) -> Sequence[outputs.GetSlotTypeEnumerationValueResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSelectionStrategy")
    def value_selection_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetSlotTypeResult(GetSlotTypeResult):
    def __await__(self): # -> Generator[Never, Any, GetSlotTypeResult]:
        ...
    


def get_slot_type(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSlotTypeResult:
    
    ...

def get_slot_type_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSlotTypeResult]:
    
    ...

