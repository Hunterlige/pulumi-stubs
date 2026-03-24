import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceLbPoliciesArgs", "ServiceLbPolicies"]

@pulumi.input_type
class ServiceLbPoliciesArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        auto_capacity_drain: Optional[
            pulumi.Input[ServiceLbPoliciesAutoCapacityDrainArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        failover_config: Optional[
            pulumi.Input[ServiceLbPoliciesFailoverConfigArgs]
        ] = ...,
        isolation_config: Optional[
            pulumi.Input[ServiceLbPoliciesIsolationConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoCapacityDrain")
    def auto_capacity_drain(
        self,
    ) -> Optional[pulumi.Input[ServiceLbPoliciesAutoCapacityDrainArgs]]: ...
    @auto_capacity_drain.setter
    def auto_capacity_drain(
        self, value: Optional[pulumi.Input[ServiceLbPoliciesAutoCapacityDrainArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failoverConfig")
    def failover_config(
        self,
    ) -> Optional[pulumi.Input[ServiceLbPoliciesFailoverConfigArgs]]: ...
    @failover_config.setter
    def failover_config(
        self, value: Optional[pulumi.Input[ServiceLbPoliciesFailoverConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isolationConfig")
    def isolation_config(
        self,
    ) -> Optional[pulumi.Input[ServiceLbPoliciesIsolationConfigArgs]]: ...
    @isolation_config.setter
    def isolation_config(
        self, value: Optional[pulumi.Input[ServiceLbPoliciesIsolationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAlgorithm")
    def load_balancing_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_algorithm.setter
    def load_balancing_algorithm(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ServiceLbPoliciesState:
    def __init__(
        __self__,
        *,
        auto_capacity_drain: Optional[
            pulumi.Input[ServiceLbPoliciesAutoCapacityDrainArgs]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        failover_config: Optional[
            pulumi.Input[ServiceLbPoliciesFailoverConfigArgs]
        ] = ...,
        isolation_config: Optional[
            pulumi.Input[ServiceLbPoliciesIsolationConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoCapacityDrain")
    def auto_capacity_drain(
        self,
    ) -> Optional[pulumi.Input[ServiceLbPoliciesAutoCapacityDrainArgs]]: ...
    @auto_capacity_drain.setter
    def auto_capacity_drain(
        self, value: Optional[pulumi.Input[ServiceLbPoliciesAutoCapacityDrainArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverConfig")
    def failover_config(
        self,
    ) -> Optional[pulumi.Input[ServiceLbPoliciesFailoverConfigArgs]]: ...
    @failover_config.setter
    def failover_config(
        self, value: Optional[pulumi.Input[ServiceLbPoliciesFailoverConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isolationConfig")
    def isolation_config(
        self,
    ) -> Optional[pulumi.Input[ServiceLbPoliciesIsolationConfigArgs]]: ...
    @isolation_config.setter
    def isolation_config(
        self, value: Optional[pulumi.Input[ServiceLbPoliciesIsolationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAlgorithm")
    def load_balancing_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_algorithm.setter
    def load_balancing_algorithm(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ServiceLbPolicies(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_capacity_drain: Optional[
            pulumi.Input[
                Union[
                    ServiceLbPoliciesAutoCapacityDrainArgs,
                    ServiceLbPoliciesAutoCapacityDrainArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        failover_config: Optional[
            pulumi.Input[
                Union[
                    ServiceLbPoliciesFailoverConfigArgs,
                    ServiceLbPoliciesFailoverConfigArgsDict,
                ]
            ]
        ] = ...,
        isolation_config: Optional[
            pulumi.Input[
                Union[
                    ServiceLbPoliciesIsolationConfigArgs,
                    ServiceLbPoliciesIsolationConfigArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceLbPoliciesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_capacity_drain: Optional[
            pulumi.Input[
                Union[
                    ServiceLbPoliciesAutoCapacityDrainArgs,
                    ServiceLbPoliciesAutoCapacityDrainArgsDict,
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        failover_config: Optional[
            pulumi.Input[
                Union[
                    ServiceLbPoliciesFailoverConfigArgs,
                    ServiceLbPoliciesFailoverConfigArgsDict,
                ]
            ]
        ] = ...,
        isolation_config: Optional[
            pulumi.Input[
                Union[
                    ServiceLbPoliciesIsolationConfigArgs,
                    ServiceLbPoliciesIsolationConfigArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load_balancing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ServiceLbPolicies: ...
    @_builtins.property
    @pulumi.getter(name="autoCapacityDrain")
    def auto_capacity_drain(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceLbPoliciesAutoCapacityDrain]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="failoverConfig")
    def failover_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceLbPoliciesFailoverConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="isolationConfig")
    def isolation_config(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceLbPoliciesIsolationConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingAlgorithm")
    def load_balancing_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
