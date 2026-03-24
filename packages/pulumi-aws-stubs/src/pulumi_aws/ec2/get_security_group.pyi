import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityGroupResult",
    "AwaitableGetSecurityGroupResult",
    "get_security_group",
    "get_security_group_output",
]

@pulumi.output_type
class GetSecurityGroupResult:
    def __init__(
        __self__,
        arn=...,
        description=...,
        filters=...,
        id=...,
        name=...,
        region=...,
        tags=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetSecurityGroupFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetSecurityGroupResult(GetSecurityGroupResult):
    def __await__(self): ...

def get_security_group(
    filters: Optional[
        Sequence[Union[GetSecurityGroupFilterArgs, GetSecurityGroupFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    vpc_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityGroupResult: ...
def get_security_group_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[GetSecurityGroupFilterArgs, GetSecurityGroupFilterArgsDict]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    vpc_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityGroupResult]: ...
