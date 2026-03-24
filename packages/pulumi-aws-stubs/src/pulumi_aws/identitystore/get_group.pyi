import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetGroupResult", "AwaitableGetGroupResult", "get_group", "get_group_output"]

@pulumi.output_type
class GetGroupResult:
    def __init__(
        __self__,
        alternate_identifier=...,
        description=...,
        display_name=...,
        external_ids=...,
        group_id=...,
        id=...,
        identity_store_id=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alternateIdentifier")
    def alternate_identifier(
        self,
    ) -> Optional[outputs.GetGroupAlternateIdentifierResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalIds")
    def external_ids(self) -> Sequence[outputs.GetGroupExternalIdResult]: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetGroupResult(GetGroupResult):
    def __await__(self): ...

def get_group(
    alternate_identifier: Optional[
        Union[GetGroupAlternateIdentifierArgs, GetGroupAlternateIdentifierArgsDict]
    ] = ...,
    group_id: Optional[_builtins.str] = ...,
    identity_store_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGroupResult: ...
def get_group_output(
    alternate_identifier: Optional[
        pulumi.Input[
            Optional[
                Union[
                    GetGroupAlternateIdentifierArgs, GetGroupAlternateIdentifierArgsDict
                ]
            ]
        ]
    ] = ...,
    group_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    identity_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGroupResult]: ...
