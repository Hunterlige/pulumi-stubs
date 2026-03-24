import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RoutingProfileArgs", "RoutingProfile"]

@pulumi.input_type
class RoutingProfileArgs:
    def __init__(
        __self__,
        *,
        default_outbound_queue_id: pulumi.Input[_builtins.str],
        description: pulumi.Input[_builtins.str],
        instance_id: pulumi.Input[_builtins.str],
        media_concurrencies: pulumi.Input[
            Sequence[pulumi.Input[RoutingProfileMediaConcurrencyArgs]]
        ],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        queue_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingProfileQueueConfigArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultOutboundQueueId")
    def default_outbound_queue_id(self) -> pulumi.Input[_builtins.str]: ...
    @default_outbound_queue_id.setter
    def default_outbound_queue_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mediaConcurrencies")
    def media_concurrencies(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[RoutingProfileMediaConcurrencyArgs]]]: ...
    @media_concurrencies.setter
    def media_concurrencies(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[RoutingProfileMediaConcurrencyArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RoutingProfileQueueConfigArgs]]]
    ]: ...
    @queue_configs.setter
    def queue_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingProfileQueueConfigArgs]]]
        ],
    ): ...
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

@pulumi.input_type
class _RoutingProfileState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_outbound_queue_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        media_concurrencies: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingProfileMediaConcurrencyArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        queue_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingProfileQueueConfigArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultOutboundQueueId")
    def default_outbound_queue_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_outbound_queue_id.setter
    def default_outbound_queue_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mediaConcurrencies")
    def media_concurrencies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RoutingProfileMediaConcurrencyArgs]]]
    ]: ...
    @media_concurrencies.setter
    def media_concurrencies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingProfileMediaConcurrencyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RoutingProfileQueueConfigArgs]]]
    ]: ...
    @queue_configs.setter
    def queue_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RoutingProfileQueueConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_profile_id.setter
    def routing_profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:connect/routingProfile:RoutingProfile")
class RoutingProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        default_outbound_queue_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        media_concurrencies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RoutingProfileMediaConcurrencyArgs,
                            RoutingProfileMediaConcurrencyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        queue_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RoutingProfileQueueConfigArgs,
                            RoutingProfileQueueConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RoutingProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_outbound_queue_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        media_concurrencies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RoutingProfileMediaConcurrencyArgs,
                            RoutingProfileMediaConcurrencyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        queue_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RoutingProfileQueueConfigArgs,
                            RoutingProfileQueueConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> RoutingProfile: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultOutboundQueueId")
    def default_outbound_queue_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mediaConcurrencies")
    def media_concurrencies(
        self,
    ) -> pulumi.Output[Sequence[outputs.RoutingProfileMediaConcurrency]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RoutingProfileQueueConfig]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
