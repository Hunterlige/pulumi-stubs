import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ChannelArgs", "Channel"]

@pulumi.input_type
class ChannelArgs:
    def __init__(
        __self__,
        *,
        channel_class: pulumi.Input[_builtins.str],
        destinations: pulumi.Input[Sequence[pulumi.Input[ChannelDestinationArgs]]],
        encoder_settings: pulumi.Input[ChannelEncoderSettingsArgs],
        input_attachments: pulumi.Input[
            Sequence[pulumi.Input[ChannelInputAttachmentArgs]]
        ],
        input_specification: pulumi.Input[ChannelInputSpecificationArgs],
        cdi_input_specification: Optional[
            pulumi.Input[ChannelCdiInputSpecificationArgs]
        ] = ...,
        log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance: Optional[pulumi.Input[ChannelMaintenanceArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        start_channel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc: Optional[pulumi.Input[ChannelVpcArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelClass")
    def channel_class(self) -> pulumi.Input[_builtins.str]: ...
    @channel_class.setter
    def channel_class(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ChannelDestinationArgs]]]: ...
    @destinations.setter
    def destinations(
        self, value: pulumi.Input[Sequence[pulumi.Input[ChannelDestinationArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encoderSettings")
    def encoder_settings(self) -> pulumi.Input[ChannelEncoderSettingsArgs]: ...
    @encoder_settings.setter
    def encoder_settings(self, value: pulumi.Input[ChannelEncoderSettingsArgs]): ...
    @_builtins.property
    @pulumi.getter(name="inputAttachments")
    def input_attachments(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ChannelInputAttachmentArgs]]]: ...
    @input_attachments.setter
    def input_attachments(
        self, value: pulumi.Input[Sequence[pulumi.Input[ChannelInputAttachmentArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputSpecification")
    def input_specification(self) -> pulumi.Input[ChannelInputSpecificationArgs]: ...
    @input_specification.setter
    def input_specification(
        self, value: pulumi.Input[ChannelInputSpecificationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cdiInputSpecification")
    def cdi_input_specification(
        self,
    ) -> Optional[pulumi.Input[ChannelCdiInputSpecificationArgs]]: ...
    @cdi_input_specification.setter
    def cdi_input_specification(
        self, value: Optional[pulumi.Input[ChannelCdiInputSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def maintenance(self) -> Optional[pulumi.Input[ChannelMaintenanceArgs]]: ...
    @maintenance.setter
    def maintenance(self, value: Optional[pulumi.Input[ChannelMaintenanceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startChannel")
    def start_channel(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @start_channel.setter
    def start_channel(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    def vpc(self) -> Optional[pulumi.Input[ChannelVpcArgs]]: ...
    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input[ChannelVpcArgs]]): ...

@pulumi.input_type
class _ChannelState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cdi_input_specification: Optional[
            pulumi.Input[ChannelCdiInputSpecificationArgs]
        ] = ...,
        channel_class: Optional[pulumi.Input[_builtins.str]] = ...,
        channel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ChannelDestinationArgs]]]
        ] = ...,
        encoder_settings: Optional[pulumi.Input[ChannelEncoderSettingsArgs]] = ...,
        input_attachments: Optional[
            pulumi.Input[Sequence[pulumi.Input[ChannelInputAttachmentArgs]]]
        ] = ...,
        input_specification: Optional[
            pulumi.Input[ChannelInputSpecificationArgs]
        ] = ...,
        log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance: Optional[pulumi.Input[ChannelMaintenanceArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        start_channel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc: Optional[pulumi.Input[ChannelVpcArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cdiInputSpecification")
    def cdi_input_specification(
        self,
    ) -> Optional[pulumi.Input[ChannelCdiInputSpecificationArgs]]: ...
    @cdi_input_specification.setter
    def cdi_input_specification(
        self, value: Optional[pulumi.Input[ChannelCdiInputSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="channelClass")
    def channel_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_class.setter
    def channel_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ChannelDestinationArgs]]]]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ChannelDestinationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encoderSettings")
    def encoder_settings(
        self,
    ) -> Optional[pulumi.Input[ChannelEncoderSettingsArgs]]: ...
    @encoder_settings.setter
    def encoder_settings(
        self, value: Optional[pulumi.Input[ChannelEncoderSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputAttachments")
    def input_attachments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ChannelInputAttachmentArgs]]]]: ...
    @input_attachments.setter
    def input_attachments(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ChannelInputAttachmentArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputSpecification")
    def input_specification(
        self,
    ) -> Optional[pulumi.Input[ChannelInputSpecificationArgs]]: ...
    @input_specification.setter
    def input_specification(
        self, value: Optional[pulumi.Input[ChannelInputSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def maintenance(self) -> Optional[pulumi.Input[ChannelMaintenanceArgs]]: ...
    @maintenance.setter
    def maintenance(self, value: Optional[pulumi.Input[ChannelMaintenanceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startChannel")
    def start_channel(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @start_channel.setter
    def start_channel(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    def vpc(self) -> Optional[pulumi.Input[ChannelVpcArgs]]: ...
    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input[ChannelVpcArgs]]): ...

@pulumi.type_token("aws:medialive/channel:Channel")
class Channel(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cdi_input_specification: Optional[
            pulumi.Input[
                Union[
                    ChannelCdiInputSpecificationArgs,
                    ChannelCdiInputSpecificationArgsDict,
                ]
            ]
        ] = ...,
        channel_class: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ChannelDestinationArgs, ChannelDestinationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        encoder_settings: Optional[
            pulumi.Input[
                Union[ChannelEncoderSettingsArgs, ChannelEncoderSettingsArgsDict]
            ]
        ] = ...,
        input_attachments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ChannelInputAttachmentArgs, ChannelInputAttachmentArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_specification: Optional[
            pulumi.Input[
                Union[ChannelInputSpecificationArgs, ChannelInputSpecificationArgsDict]
            ]
        ] = ...,
        log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance: Optional[
            pulumi.Input[Union[ChannelMaintenanceArgs, ChannelMaintenanceArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        start_channel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc: Optional[pulumi.Input[Union[ChannelVpcArgs, ChannelVpcArgsDict]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ChannelArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cdi_input_specification: Optional[
            pulumi.Input[
                Union[
                    ChannelCdiInputSpecificationArgs,
                    ChannelCdiInputSpecificationArgsDict,
                ]
            ]
        ] = ...,
        channel_class: Optional[pulumi.Input[_builtins.str]] = ...,
        channel_id: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ChannelDestinationArgs, ChannelDestinationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        encoder_settings: Optional[
            pulumi.Input[
                Union[ChannelEncoderSettingsArgs, ChannelEncoderSettingsArgsDict]
            ]
        ] = ...,
        input_attachments: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ChannelInputAttachmentArgs, ChannelInputAttachmentArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_specification: Optional[
            pulumi.Input[
                Union[ChannelInputSpecificationArgs, ChannelInputSpecificationArgsDict]
            ]
        ] = ...,
        log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance: Optional[
            pulumi.Input[Union[ChannelMaintenanceArgs, ChannelMaintenanceArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        start_channel: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc: Optional[pulumi.Input[Union[ChannelVpcArgs, ChannelVpcArgsDict]]] = ...,
    ) -> Channel: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cdiInputSpecification")
    def cdi_input_specification(
        self,
    ) -> pulumi.Output[Optional[outputs.ChannelCdiInputSpecification]]: ...
    @_builtins.property
    @pulumi.getter(name="channelClass")
    def channel_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Sequence[outputs.ChannelDestination]]: ...
    @_builtins.property
    @pulumi.getter(name="encoderSettings")
    def encoder_settings(self) -> pulumi.Output[outputs.ChannelEncoderSettings]: ...
    @_builtins.property
    @pulumi.getter(name="inputAttachments")
    def input_attachments(
        self,
    ) -> pulumi.Output[Sequence[outputs.ChannelInputAttachment]]: ...
    @_builtins.property
    @pulumi.getter(name="inputSpecification")
    def input_specification(
        self,
    ) -> pulumi.Output[outputs.ChannelInputSpecification]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def maintenance(self) -> pulumi.Output[outputs.ChannelMaintenance]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startChannel")
    def start_channel(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> pulumi.Output[Optional[outputs.ChannelVpc]]: ...
