import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ScopeArgs", "Scope"]

@pulumi.input_type
class ScopeArgs:
    def __init__(
        __self__,
        *,
        targets: pulumi.Input[Sequence[pulumi.Input[ScopeTargetArgs]]],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ScopeTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input[ScopeTargetArgs]]]: ...
    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input[ScopeTargetArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ScopeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ScopeTimeoutsArgs]]): ...

@pulumi.input_type
class _ScopeState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        targets: Optional[pulumi.Input[Sequence[pulumi.Input[ScopeTargetArgs]]]] = ...,
        timeouts: Optional[pulumi.Input[ScopeTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeArn")
    def scope_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope_arn.setter
    def scope_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope_id.setter
    def scope_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScopeTargetArgs]]]]: ...
    @targets.setter
    def targets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScopeTargetArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ScopeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ScopeTimeoutsArgs]]): ...

@pulumi.type_token("aws:networkflowmonitor/scope:Scope")
class Scope(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ScopeTargetArgs, ScopeTargetArgsDict]]]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ScopeTimeoutsArgs, ScopeTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ScopeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ScopeTargetArgs, ScopeTargetArgsDict]]]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ScopeTimeoutsArgs, ScopeTimeoutsArgsDict]]
        ] = ...,
    ) -> Scope: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scopeArn")
    def scope_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Output[Sequence[outputs.ScopeTarget]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ScopeTimeouts]]: ...
