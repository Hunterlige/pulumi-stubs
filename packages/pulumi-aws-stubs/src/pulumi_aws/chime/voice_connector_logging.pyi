import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VoiceConnectorLoggingArgs", "VoiceConnectorLogging"]

@pulumi.input_type
class VoiceConnectorLoggingArgs:
    def __init__(
        __self__,
        *,
        voice_connector_id: pulumi.Input[_builtins.str],
        enable_media_metric_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sip_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Input[_builtins.str]: ...
    @voice_connector_id.setter
    def voice_connector_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enableMediaMetricLogs")
    def enable_media_metric_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_media_metric_logs.setter
    def enable_media_metric_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSipLogs")
    def enable_sip_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_sip_logs.setter
    def enable_sip_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _VoiceConnectorLoggingState:
    def __init__(
        __self__,
        *,
        enable_media_metric_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sip_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMediaMetricLogs")
    def enable_media_metric_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_media_metric_logs.setter
    def enable_media_metric_logs(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSipLogs")
    def enable_sip_logs(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_sip_logs.setter
    def enable_sip_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @voice_connector_id.setter
    def voice_connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class VoiceConnectorLogging(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        enable_media_metric_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sip_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VoiceConnectorLoggingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        enable_media_metric_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_sip_logs: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        voice_connector_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VoiceConnectorLogging: ...
    @_builtins.property
    @pulumi.getter(name="enableMediaMetricLogs")
    def enable_media_metric_logs(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableSipLogs")
    def enable_sip_logs(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Output[_builtins.str]: ...
