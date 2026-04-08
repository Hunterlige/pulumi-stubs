import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataPartitionNamesArgs",
    "DataPartitionNamesArgsDict",
    "EnergyServicePropertiesArgs",
    "EnergyServicePropertiesArgsDict",
]

class DataPartitionNamesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataPartitionNamesArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnergyServicePropertiesArgsDict(TypedDict):
    auth_app_id: NotRequired[pulumi.Input[_builtins.str]]
    data_partition_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DataPartitionNamesArgsDict]]]
    ]

@pulumi.input_type
class EnergyServicePropertiesArgs:
    def __init__(
        __self__,
        *,
        auth_app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_partition_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataPartitionNamesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authAppId")
    def auth_app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_app_id.setter
    def auth_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataPartitionNames")
    def data_partition_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataPartitionNamesArgs]]]]: ...
    @data_partition_names.setter
    def data_partition_names(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataPartitionNamesArgs]]]],
    ): ...
