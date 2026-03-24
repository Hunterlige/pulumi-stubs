

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
__all__ = ['GetSecurityGroupsResult', 'AwaitableGetSecurityGroupsResult', 'get_security_groups', 'get_security_groups_output']
@pulumi.output_type
class GetSecurityGroupsResult:
    
    def __init__(__self__, arns=..., filters=..., id=..., ids=..., region=..., tags=..., vpc_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetSecurityGroupsFilterResult]]:
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
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetSecurityGroupsResult(GetSecurityGroupsResult):
    def __await__(self): # -> Generator[Never, Any, GetSecurityGroupsResult]:
        ...
    


def get_security_groups(filters: Optional[Sequence[Union[GetSecurityGroupsFilterArgs, GetSecurityGroupsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecurityGroupsResult:
    
    ...

def get_security_groups_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetSecurityGroupsFilterArgs, GetSecurityGroupsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecurityGroupsResult]:
    
    ...

