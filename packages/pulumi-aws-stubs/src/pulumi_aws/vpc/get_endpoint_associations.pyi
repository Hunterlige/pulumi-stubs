

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEndpointAssociationsResult', 'AwaitableGetEndpointAssociationsResult', 'get_endpoint_associations', 'get_endpoint_associations_output']
@pulumi.output_type
class GetEndpointAssociationsResult:
    
    def __init__(__self__, associations=..., id=..., region=..., vpc_endpoint_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def associations(self) -> Sequence[outputs.GetEndpointAssociationsAssociationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> _builtins.str:
        ...
    


class AwaitableGetEndpointAssociationsResult(GetEndpointAssociationsResult):
    def __await__(self): # -> Generator[Never, Any, GetEndpointAssociationsResult]:
        ...
    


def get_endpoint_associations(region: Optional[_builtins.str] = ..., vpc_endpoint_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEndpointAssociationsResult:
    
    ...

def get_endpoint_associations_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEndpointAssociationsResult]:
    
    ...

