import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VoiceConnectorStreamingArgs", "VoiceConnectorStreaming"]

@pulumi.input_type
class VoiceConnectorStreamingArgs:
    def __init__(
        __self__,
        *,
        data_retention: pulumi.Input[_builtins.int],
        voice_connector_id: pulumi.Input[_builtins.str],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        media_insights_configuration: Optional[
            pulumi.Input[VoiceConnectorStreamingMediaInsightsConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        streaming_notification_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataRetention")
    def data_retention(self) -> pulumi.Input[_builtins.int]: ...
    @data_retention.setter
    def data_retention(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Input[_builtins.str]: ...
    @voice_connector_id.setter
    def voice_connector_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mediaInsightsConfiguration")
    def media_insights_configuration(
        self,
    ) -> Optional[
        pulumi.Input[VoiceConnectorStreamingMediaInsightsConfigurationArgs]
    ]: ...
    @media_insights_configuration.setter
    def media_insights_configuration(
        self,
        value: Optional[
            pulumi.Input[VoiceConnectorStreamingMediaInsightsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamingNotificationTargets")
    def streaming_notification_targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @streaming_notification_targets.setter
    def streaming_notification_targets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _VoiceConnectorStreamingState:
    def __init__(
        __self__,
        *,
        data_retention: Optional[pulumi.Input[_builtins.int]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        media_insights_configuration: Optional[
            pulumi.Input[VoiceConnectorStreamingMediaInsightsConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        streaming_notification_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataRetention")
    def data_retention(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_retention.setter
    def data_retention(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mediaInsightsConfiguration")
    def media_insights_configuration(
        self,
    ) -> Optional[
        pulumi.Input[VoiceConnectorStreamingMediaInsightsConfigurationArgs]
    ]: ...
    @media_insights_configuration.setter
    def media_insights_configuration(
        self,
        value: Optional[
            pulumi.Input[VoiceConnectorStreamingMediaInsightsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamingNotificationTargets")
    def streaming_notification_targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @streaming_notification_targets.setter
    def streaming_notification_targets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @voice_connector_id.setter
    def voice_connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VoiceConnectorStreaming(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_retention: Optional[pulumi.Input[_builtins.int]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        media_insights_configuration: Optional[
            pulumi.Input[
                Union[
                    VoiceConnectorStreamingMediaInsightsConfigurationArgs,
                    VoiceConnectorStreamingMediaInsightsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        streaming_notification_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VoiceConnectorStreamingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_retention: Optional[pulumi.Input[_builtins.int]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        media_insights_configuration: Optional[
            pulumi.Input[
                Union[
                    VoiceConnectorStreamingMediaInsightsConfigurationArgs,
                    VoiceConnectorStreamingMediaInsightsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        streaming_notification_targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VoiceConnectorStreaming: ...
    @_builtins.property
    @pulumi.getter(name="dataRetention")
    def data_retention(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="mediaInsightsConfiguration")
    def media_insights_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.VoiceConnectorStreamingMediaInsightsConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamingNotificationTargets")
    def streaming_notification_targets(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Output[_builtins.str]: ...
