import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MulticastGroupRangeActivationArgs", "MulticastGroupRangeActivation"]

@pulumi.input_type
class MulticastGroupRangeActivationArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        multicast_domain_activation: pulumi.Input[_builtins.str],
        multicast_group_range: pulumi.Input[_builtins.str],
        multicast_group_range_activation_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        log_config: Optional[
            pulumi.Input[MulticastGroupRangeActivationLogConfigArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multicastDomainActivation")
    def multicast_domain_activation(self) -> pulumi.Input[_builtins.str]: ...
    @multicast_domain_activation.setter
    def multicast_domain_activation(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRange")
    def multicast_group_range(self) -> pulumi.Input[_builtins.str]: ...
    @multicast_group_range.setter
    def multicast_group_range(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRangeActivationId")
    def multicast_group_range_activation_id(self) -> pulumi.Input[_builtins.str]: ...
    @multicast_group_range_activation_id.setter
    def multicast_group_range_activation_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="logConfig")
    def log_config(
        self,
    ) -> Optional[pulumi.Input[MulticastGroupRangeActivationLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[MulticastGroupRangeActivationLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MulticastGroupRangeActivationState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[MulticastGroupRangeActivationLogConfigArgs]
        ] = ...,
        multicast_domain_activation: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_consumer_activations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multicast_group_range: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_range_activation_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        states: Optional[
            pulumi.Input[Sequence[pulumi.Input[MulticastGroupRangeActivationStateArgs]]]
        ] = ...,
        unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_cidr_range.setter
    def ip_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(
        self,
    ) -> Optional[pulumi.Input[MulticastGroupRangeActivationLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[MulticastGroupRangeActivationLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multicastDomainActivation")
    def multicast_domain_activation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_domain_activation.setter
    def multicast_domain_activation(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupConsumerActivations")
    def multicast_group_consumer_activations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @multicast_group_consumer_activations.setter
    def multicast_group_consumer_activations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRange")
    def multicast_group_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_group_range.setter
    def multicast_group_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRangeActivationId")
    def multicast_group_range_activation_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_group_range_activation_id.setter
    def multicast_group_range_activation_id(
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
    @pulumi.getter
    def states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MulticastGroupRangeActivationStateArgs]]]
    ]: ...
    @states.setter
    def states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MulticastGroupRangeActivationStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unique_id.setter
    def unique_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class MulticastGroupRangeActivation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[
                    MulticastGroupRangeActivationLogConfigArgs,
                    MulticastGroupRangeActivationLogConfigArgsDict,
                ]
            ]
        ] = ...,
        multicast_domain_activation: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_range: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_range_activation_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MulticastGroupRangeActivationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_cidr_range: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[
                    MulticastGroupRangeActivationLogConfigArgs,
                    MulticastGroupRangeActivationLogConfigArgsDict,
                ]
            ]
        ] = ...,
        multicast_domain_activation: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_consumer_activations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multicast_group_range: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_range_activation_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MulticastGroupRangeActivationStateArgs,
                            MulticastGroupRangeActivationStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MulticastGroupRangeActivation: ...
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
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(
        self,
    ) -> pulumi.Output[Optional[outputs.MulticastGroupRangeActivationLogConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="multicastDomainActivation")
    def multicast_domain_activation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupConsumerActivations")
    def multicast_group_consumer_activations(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRange")
    def multicast_group_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRangeActivationId")
    def multicast_group_range_activation_id(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter
    def states(
        self,
    ) -> pulumi.Output[Sequence[outputs.MulticastGroupRangeActivationState]]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
