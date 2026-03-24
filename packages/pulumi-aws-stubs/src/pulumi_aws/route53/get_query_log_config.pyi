import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetQueryLogConfigResult",
    "AwaitableGetQueryLogConfigResult",
    "get_query_log_config",
    "get_query_log_config_output",
]

@pulumi.output_type
class GetQueryLogConfigResult:
    def __init__(
        __self__,
        arn=...,
        destination_arn=...,
        filters=...,
        id=...,
        name=...,
        owner_id=...,
        region=...,
        resolver_query_log_config_id=...,
        share_status=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetQueryLogConfigFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetQueryLogConfigResult(GetQueryLogConfigResult):
    def __await__(self): ...

def get_query_log_config(
    filters: Optional[
        Sequence[Union[GetQueryLogConfigFilterArgs, GetQueryLogConfigFilterArgsDict]]
    ] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    resolver_query_log_config_id: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetQueryLogConfigResult: ...
def get_query_log_config_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[GetQueryLogConfigFilterArgs, GetQueryLogConfigFilterArgsDict]
                ]
            ]
        ]
    ] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resolver_query_log_config_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetQueryLogConfigResult]: ...
