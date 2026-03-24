

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
__all__ = ['GetLocalGatewayVirtualInterfaceGroupResult', ..., 'get_local_gateway_virtual_interface_group', 'get_local_gateway_virtual_interface_group_output']
@pulumi.output_type
class GetLocalGatewayVirtualInterfaceGroupResult:
    
    def __init__(__self__, filters=..., id=..., local_gateway_id=..., local_gateway_virtual_interface_ids=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetLocalGatewayVirtualInterfaceGroupFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localGatewayVirtualInterfaceIds")
    def local_gateway_virtual_interface_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetLocalGatewayVirtualInterfaceGroupResult(GetLocalGatewayVirtualInterfaceGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetLocalGatewayVirtualInterfaceGroupResult]:
        ...
    


def get_local_gateway_virtual_interface_group(filters: Optional[Sequence[Union[GetLocalGatewayVirtualInterfaceGroupFilterArgs, GetLocalGatewayVirtualInterfaceGroupFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., local_gateway_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLocalGatewayVirtualInterfaceGroupResult:
    
    ...

def get_local_gateway_virtual_interface_group_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetLocalGatewayVirtualInterfaceGroupFilterArgs, GetLocalGatewayVirtualInterfaceGroupFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., local_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLocalGatewayVirtualInterfaceGroupResult]:
    
    ...

