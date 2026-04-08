import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PacketCaptureArgs", "PacketCapture"]

@pulumi.input_type
class PacketCaptureArgs:
    def __init__(
        __self__,
        *,
        network_watcher_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        storage_location: pulumi.Input[PacketCaptureStorageLocationArgs],
        target: pulumi.Input[_builtins.str],
        bytes_to_capture_per_packet: Optional[pulumi.Input[_builtins.float]] = ...,
        capture_settings: Optional[pulumi.Input[PacketCaptureSettingsArgs]] = ...,
        continuous_capture: Optional[pulumi.Input[_builtins.bool]] = ...,
        filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[PacketCaptureFilterArgs]]]
        ] = ...,
        packet_capture_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[PacketCaptureMachineScopeArgs]] = ...,
        target_type: Optional[pulumi.Input[PacketCaptureTargetType]] = ...,
        time_limit_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        total_bytes_per_session: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkWatcherName")
    def network_watcher_name(self) -> pulumi.Input[_builtins.str]: ...
    @network_watcher_name.setter
    def network_watcher_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> pulumi.Input[PacketCaptureStorageLocationArgs]: ...
    @storage_location.setter
    def storage_location(
        self, value: pulumi.Input[PacketCaptureStorageLocationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @bytes_to_capture_per_packet.setter
    def bytes_to_capture_per_packet(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="captureSettings")
    def capture_settings(self) -> Optional[pulumi.Input[PacketCaptureSettingsArgs]]: ...
    @capture_settings.setter
    def capture_settings(
        self, value: Optional[pulumi.Input[PacketCaptureSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="continuousCapture")
    def continuous_capture(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continuous_capture.setter
    def continuous_capture(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PacketCaptureFilterArgs]]]]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PacketCaptureFilterArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="packetCaptureName")
    def packet_capture_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @packet_capture_name.setter
    def packet_capture_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[PacketCaptureMachineScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[PacketCaptureMachineScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[PacketCaptureTargetType]]: ...
    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[PacketCaptureTargetType]]): ...
    @_builtins.property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @time_limit_in_seconds.setter
    def time_limit_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @total_bytes_per_session.setter
    def total_bytes_per_session(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

@pulumi.type_token("azure-native:network:PacketCapture")
class PacketCapture(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bytes_to_capture_per_packet: Optional[pulumi.Input[_builtins.float]] = ...,
        capture_settings: Optional[
            pulumi.Input[
                Union[PacketCaptureSettingsArgs, PacketCaptureSettingsArgsDict]
            ]
        ] = ...,
        continuous_capture: Optional[pulumi.Input[_builtins.bool]] = ...,
        filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PacketCaptureFilterArgs, PacketCaptureFilterArgsDict]
                    ]
                ]
            ]
        ] = ...,
        network_watcher_name: Optional[pulumi.Input[_builtins.str]] = ...,
        packet_capture_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[
            pulumi.Input[
                Union[PacketCaptureMachineScopeArgs, PacketCaptureMachineScopeArgsDict]
            ]
        ] = ...,
        storage_location: Optional[
            pulumi.Input[
                Union[
                    PacketCaptureStorageLocationArgs,
                    PacketCaptureStorageLocationArgsDict,
                ]
            ]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        target_type: Optional[pulumi.Input[PacketCaptureTargetType]] = ...,
        time_limit_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        total_bytes_per_session: Optional[pulumi.Input[_builtins.float]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PacketCaptureArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PacketCapture: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="captureSettings")
    def capture_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.PacketCaptureSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="continuousCapture")
    def continuous_capture(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PacketCaptureFilterResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(
        self,
    ) -> pulumi.Output[Optional[outputs.PacketCaptureMachineScopeResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(
        self,
    ) -> pulumi.Output[outputs.PacketCaptureStorageLocationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> pulumi.Output[Optional[_builtins.float]]: ...
