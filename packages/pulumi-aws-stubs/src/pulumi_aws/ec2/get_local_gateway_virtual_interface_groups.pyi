import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocalGatewayVirtualInterfaceGroupsResult",
    ...,
    "get_local_gateway_virtual_interface_groups",
    "get_local_gateway_virtual_interface_groups_output",
]

@pulumi.output_type
class GetLocalGatewayVirtualInterfaceGroupsResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        ids=...,
        local_gateway_virtual_interface_ids=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        Sequence[outputs.GetLocalGatewayVirtualInterfaceGroupsFilterResult]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayVirtualInterfaceIds")
    def local_gateway_virtual_interface_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

class AwaitableGetLocalGatewayVirtualInterfaceGroupsResult(
    GetLocalGatewayVirtualInterfaceGroupsResult
):
    def __await__(self): ...

def get_local_gateway_virtual_interface_groups(
    filters: Optional[
        Sequence[
            Union[
                GetLocalGatewayVirtualInterfaceGroupsFilterArgs,
                GetLocalGatewayVirtualInterfaceGroupsFilterArgsDict,
            ]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocalGatewayVirtualInterfaceGroupsResult: ...
def get_local_gateway_virtual_interface_groups_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetLocalGatewayVirtualInterfaceGroupsFilterArgs,
                        GetLocalGatewayVirtualInterfaceGroupsFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocalGatewayVirtualInterfaceGroupsResult]: ...
