import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedScalingPolicyArgs", "ManagedScalingPolicy"]

@pulumi.input_type
class ManagedScalingPolicyArgs:
    def __init__(
        __self__,
        *,
        cluster_id: pulumi.Input[_builtins.str],
        compute_limits: pulumi.Input[
            Sequence[pulumi.Input[ManagedScalingPolicyComputeLimitArgs]]
        ],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        utilization_performance_index: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeLimits")
    def compute_limits(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ManagedScalingPolicyComputeLimitArgs]]]: ...
    @compute_limits.setter
    def compute_limits(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ManagedScalingPolicyComputeLimitArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingStrategy")
    def scaling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_strategy.setter
    def scaling_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="utilizationPerformanceIndex")
    def utilization_performance_index(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @utilization_performance_index.setter
    def utilization_performance_index(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.input_type
class _ManagedScalingPolicyState:
    def __init__(
        __self__,
        *,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_limits: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedScalingPolicyComputeLimitArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        utilization_performance_index: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeLimits")
    def compute_limits(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ManagedScalingPolicyComputeLimitArgs]]]
    ]: ...
    @compute_limits.setter
    def compute_limits(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ManagedScalingPolicyComputeLimitArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingStrategy")
    def scaling_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_strategy.setter
    def scaling_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="utilizationPerformanceIndex")
    def utilization_performance_index(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @utilization_performance_index.setter
    def utilization_performance_index(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.type_token("aws:emr/managedScalingPolicy:ManagedScalingPolicy")
class ManagedScalingPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_limits: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ManagedScalingPolicyComputeLimitArgs,
                            ManagedScalingPolicyComputeLimitArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        utilization_performance_index: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedScalingPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_limits: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ManagedScalingPolicyComputeLimitArgs,
                            ManagedScalingPolicyComputeLimitArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        utilization_performance_index: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> ManagedScalingPolicy: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeLimits")
    def compute_limits(
        self,
    ) -> pulumi.Output[Sequence[outputs.ManagedScalingPolicyComputeLimit]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingStrategy")
    def scaling_strategy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="utilizationPerformanceIndex")
    def utilization_performance_index(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
