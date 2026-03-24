

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
__all__ = ['GetResourceShareResult', 'AwaitableGetResourceShareResult', 'get_resource_share', 'get_resource_share_output']
@pulumi.output_type
class GetResourceShareResult:
    
    def __init__(__self__, arn=..., filters=..., id=..., name=..., owning_account_id=..., region=..., resource_arns=..., resource_owner=..., resource_share_status=..., status=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetResourceShareFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="owningAccountId")
    def owning_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceShareStatus")
    def resource_share_status(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetResourceShareResult(GetResourceShareResult):
    def __await__(self): # -> Generator[Never, Any, GetResourceShareResult]:
        ...
    


def get_resource_share(filters: Optional[Sequence[Union[GetResourceShareFilterArgs, GetResourceShareFilterArgsDict]]] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., resource_owner: Optional[_builtins.str] = ..., resource_share_status: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourceShareResult:
    
    ...

def get_resource_share_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetResourceShareFilterArgs, GetResourceShareFilterArgsDict]]]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_owner: Optional[pulumi.Input[_builtins.str]] = ..., resource_share_status: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourceShareResult]:
    
    ...

