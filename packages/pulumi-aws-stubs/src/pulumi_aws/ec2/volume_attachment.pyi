import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VolumeAttachmentArgs", "VolumeAttachment"]

@pulumi.input_type
class VolumeAttachmentArgs:
    def __init__(
        __self__,
        *,
        device_name: pulumi.Input[_builtins.str],
        instance_id: pulumi.Input[_builtins.str],
        volume_id: pulumi.Input[_builtins.str],
        force_detach: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        stop_instance_before_detaching: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[_builtins.str]: ...
    @device_name.setter
    def device_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Input[_builtins.str]: ...
    @volume_id.setter
    def volume_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="forceDetach")
    def force_detach(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_detach.setter
    def force_detach(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="stopInstanceBeforeDetaching")
    def stop_instance_before_detaching(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @stop_instance_before_detaching.setter
    def stop_instance_before_detaching(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _VolumeAttachmentState:
    def __init__(
        __self__,
        *,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_detach: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        stop_instance_before_detaching: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDetach")
    def force_detach(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_detach.setter
    def force_detach(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="stopInstanceBeforeDetaching")
    def stop_instance_before_detaching(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @stop_instance_before_detaching.setter
    def stop_instance_before_detaching(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:ec2/volumeAttachment:VolumeAttachment")
class VolumeAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_detach: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        stop_instance_before_detaching: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VolumeAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        force_detach: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        stop_instance_before_detaching: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> VolumeAttachment: ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forceDetach")
    def force_detach(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="stopInstanceBeforeDetaching")
    def stop_instance_before_detaching(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[_builtins.str]: ...
