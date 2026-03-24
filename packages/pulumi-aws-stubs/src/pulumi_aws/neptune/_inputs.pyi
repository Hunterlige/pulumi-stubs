import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterParameterGroupParameterArgs",
    "ClusterParameterGroupParameterArgsDict",
    "ClusterServerlessV2ScalingConfigurationArgs",
    "ClusterServerlessV2ScalingConfigurationArgsDict",
    "GlobalClusterGlobalClusterMemberArgs",
    "GlobalClusterGlobalClusterMemberArgsDict",
    "ParameterGroupParameterArgs",
    "ParameterGroupParameterArgsDict",
]

class ClusterParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    apply_method: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterParameterGroupParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        apply_method: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apply_method.setter
    def apply_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterServerlessV2ScalingConfigurationArgsDict(TypedDict):
    max_capacity: NotRequired[pulumi.Input[_builtins.float]]
    min_capacity: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class ClusterServerlessV2ScalingConfigurationArgs:
    def __init__(
        __self__,
        *,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        min_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class GlobalClusterGlobalClusterMemberArgsDict(TypedDict):
    db_cluster_arn: NotRequired[pulumi.Input[_builtins.str]]
    is_writer: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GlobalClusterGlobalClusterMemberArgs:
    def __init__(
        __self__,
        *,
        db_cluster_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        is_writer: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_arn.setter
    def db_cluster_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_writer.setter
    def is_writer(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    apply_method: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ParameterGroupParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        apply_method: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apply_method.setter
    def apply_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
