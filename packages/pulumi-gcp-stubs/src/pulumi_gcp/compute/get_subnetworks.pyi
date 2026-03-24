

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSubnetworksResult', 'AwaitableGetSubnetworksResult', 'get_subnetworks', 'get_subnetworks_output']
@pulumi.output_type
class GetSubnetworksResult:
    
    def __init__(__self__, filter=..., id=..., project=..., region=..., subnetworks=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetworks(self) -> Sequence[outputs.GetSubnetworksSubnetworkResult]:
        
        ...
    


class AwaitableGetSubnetworksResult(GetSubnetworksResult):
    def __await__(self): # -> Generator[Never, Any, GetSubnetworksResult]:
        ...
    


def get_subnetworks(filter: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSubnetworksResult:
    
    ...

def get_subnetworks_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSubnetworksResult]:
    
    ...

