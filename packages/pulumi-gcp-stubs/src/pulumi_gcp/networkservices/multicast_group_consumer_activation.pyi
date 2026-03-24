import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MulticastGroupConsumerActivationArgs", "MulticastGroupConsumerActivation"]

@pulumi.input_type
class MulticastGroupConsumerActivationArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        multicast_consumer_association: pulumi.Input[_builtins.str],
        multicast_group_consumer_activation_id: pulumi.Input[_builtins.str],
        multicast_group_range_activation: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        log_config: Optional[
            pulumi.Input[MulticastGroupConsumerActivationLogConfigArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multicastConsumerAssociation")
    def multicast_consumer_association(self) -> pulumi.Input[_builtins.str]: ...
    @multicast_consumer_association.setter
    def multicast_consumer_association(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupConsumerActivationId")
    def multicast_group_consumer_activation_id(self) -> pulumi.Input[_builtins.str]: ...
    @multicast_group_consumer_activation_id.setter
    def multicast_group_consumer_activation_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRangeActivation")
    def multicast_group_range_activation(self) -> pulumi.Input[_builtins.str]: ...
    @multicast_group_range_activation.setter
    def multicast_group_range_activation(self, value: pulumi.Input[_builtins.str]): ...
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
    ) -> Optional[pulumi.Input[MulticastGroupConsumerActivationLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self,
        value: Optional[pulumi.Input[MulticastGroupConsumerActivationLogConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MulticastGroupConsumerActivationState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[MulticastGroupConsumerActivationLogConfigArgs]
        ] = ...,
        multicast_consumer_association: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_consumer_activation_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        multicast_group_range_activation: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        states: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MulticastGroupConsumerActivationStateArgs]]
            ]
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
    ) -> Optional[pulumi.Input[MulticastGroupConsumerActivationLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self,
        value: Optional[pulumi.Input[MulticastGroupConsumerActivationLogConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="multicastConsumerAssociation")
    def multicast_consumer_association(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_consumer_association.setter
    def multicast_consumer_association(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupConsumerActivationId")
    def multicast_group_consumer_activation_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_group_consumer_activation_id.setter
    def multicast_group_consumer_activation_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRangeActivation")
    def multicast_group_range_activation(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multicast_group_range_activation.setter
    def multicast_group_range_activation(
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
        pulumi.Input[Sequence[pulumi.Input[MulticastGroupConsumerActivationStateArgs]]]
    ]: ...
    @states.setter
    def states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MulticastGroupConsumerActivationStateArgs]]
            ]
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
class MulticastGroupConsumerActivation(pulumi.CustomResource):
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
                    MulticastGroupConsumerActivationLogConfigArgs,
                    MulticastGroupConsumerActivationLogConfigArgsDict,
                ]
            ]
        ] = ...,
        multicast_consumer_association: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_consumer_activation_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        multicast_group_range_activation: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MulticastGroupConsumerActivationArgs,
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
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[
                    MulticastGroupConsumerActivationLogConfigArgs,
                    MulticastGroupConsumerActivationLogConfigArgsDict,
                ]
            ]
        ] = ...,
        multicast_consumer_association: Optional[pulumi.Input[_builtins.str]] = ...,
        multicast_group_consumer_activation_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        multicast_group_range_activation: Optional[pulumi.Input[_builtins.str]] = ...,
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
                            MulticastGroupConsumerActivationStateArgs,
                            MulticastGroupConsumerActivationStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        unique_id: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MulticastGroupConsumerActivation: ...
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
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(
        self,
    ) -> pulumi.Output[Optional[outputs.MulticastGroupConsumerActivationLogConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="multicastConsumerAssociation")
    def multicast_consumer_association(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupConsumerActivationId")
    def multicast_group_consumer_activation_id(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multicastGroupRangeActivation")
    def multicast_group_range_activation(self) -> pulumi.Output[_builtins.str]: ...
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
    ) -> pulumi.Output[Sequence[outputs.MulticastGroupConsumerActivationState]]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
