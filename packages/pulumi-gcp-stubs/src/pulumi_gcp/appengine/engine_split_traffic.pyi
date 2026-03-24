import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EngineSplitTrafficArgs", "EngineSplitTraffic"]

@pulumi.input_type
class EngineSplitTrafficArgs:
    def __init__(
        __self__,
        *,
        service: pulumi.Input[_builtins.str],
        split: pulumi.Input[EngineSplitTrafficSplitArgs],
        migrate_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def split(self) -> pulumi.Input[EngineSplitTrafficSplitArgs]: ...
    @split.setter
    def split(self, value: pulumi.Input[EngineSplitTrafficSplitArgs]): ...
    @_builtins.property
    @pulumi.getter(name="migrateTraffic")
    def migrate_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @migrate_traffic.setter
    def migrate_traffic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EngineSplitTrafficState:
    def __init__(
        __self__,
        *,
        migrate_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        split: Optional[pulumi.Input[EngineSplitTrafficSplitArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="migrateTraffic")
    def migrate_traffic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @migrate_traffic.setter
    def migrate_traffic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def split(self) -> Optional[pulumi.Input[EngineSplitTrafficSplitArgs]]: ...
    @split.setter
    def split(self, value: Optional[pulumi.Input[EngineSplitTrafficSplitArgs]]): ...

@pulumi.type_token(...)
class EngineSplitTraffic(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        migrate_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        split: Optional[
            pulumi.Input[
                Union[EngineSplitTrafficSplitArgs, EngineSplitTrafficSplitArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EngineSplitTrafficArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        migrate_traffic: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        split: Optional[
            pulumi.Input[
                Union[EngineSplitTrafficSplitArgs, EngineSplitTrafficSplitArgsDict]
            ]
        ] = ...,
    ) -> EngineSplitTraffic: ...
    @_builtins.property
    @pulumi.getter(name="migrateTraffic")
    def migrate_traffic(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def split(self) -> pulumi.Output[outputs.EngineSplitTrafficSplit]: ...
