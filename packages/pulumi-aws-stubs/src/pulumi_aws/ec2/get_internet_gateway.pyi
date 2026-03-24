

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
__all__ = ['GetInternetGatewayResult', 'AwaitableGetInternetGatewayResult', 'get_internet_gateway', 'get_internet_gateway_output']
@pulumi.output_type
class GetInternetGatewayResult:
    
    def __init__(__self__, arn=..., attachments=..., filters=..., id=..., internet_gateway_id=..., owner_id=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attachments(self) -> Sequence[outputs.GetInternetGatewayAttachmentResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInternetGatewayFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGatewayId")
    def internet_gateway_id(self) -> _builtins.str:
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
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetInternetGatewayResult(GetInternetGatewayResult):
    def __await__(self): # -> Generator[Never, Any, GetInternetGatewayResult]:
        ...
    


def get_internet_gateway(filters: Optional[Sequence[Union[GetInternetGatewayFilterArgs, GetInternetGatewayFilterArgsDict]]] = ..., internet_gateway_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInternetGatewayResult:
    
    ...

def get_internet_gateway_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetInternetGatewayFilterArgs, GetInternetGatewayFilterArgsDict]]]]] = ..., internet_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInternetGatewayResult]:
    
    ...

