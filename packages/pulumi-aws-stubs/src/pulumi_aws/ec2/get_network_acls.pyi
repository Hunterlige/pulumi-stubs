

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkAclsResult', 'AwaitableGetNetworkAclsResult', 'get_network_acls', 'get_network_acls_output']
@pulumi.output_type
class GetNetworkAclsResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., region=..., tags=..., vpc_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetNetworkAclsFilterResult]]:
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
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetNetworkAclsResult(GetNetworkAclsResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkAclsResult]:
        ...
    


def get_network_acls(filters: Optional[Sequence[Union[GetNetworkAclsFilterArgs, GetNetworkAclsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., vpc_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkAclsResult:
    
    ...

def get_network_acls_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetNetworkAclsFilterArgs, GetNetworkAclsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkAclsResult]:
    
    ...

