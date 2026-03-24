import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NetworkInterfaceAttachmentInitArgs", "NetworkInterfaceAttachment"]

@pulumi.input_type
class NetworkInterfaceAttachmentInitArgs:
    def __init__(
        __self__,
        *,
        device_index: pulumi.Input[_builtins.int],
        instance_id: pulumi.Input[_builtins.str],
        network_interface_id: pulumi.Input[_builtins.str],
        network_card_index: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> pulumi.Input[_builtins.int]: ...
    @device_index.setter
    def device_index(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[_builtins.str]: ...
    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @network_card_index.setter
    def network_card_index(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _NetworkInterfaceAttachmentState:
    def __init__(
        __self__,
        *,
        attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        device_index: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_card_index: Optional[pulumi.Input[_builtins.int]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attachment_id.setter
    def attachment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @device_index.setter
    def device_index(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @network_card_index.setter
    def network_card_index(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class NetworkInterfaceAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        device_index: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_card_index: Optional[pulumi.Input[_builtins.int]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NetworkInterfaceAttachmentInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        attachment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        device_index: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        network_card_index: Optional[pulumi.Input[_builtins.int]] = ...,
        network_interface_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> NetworkInterfaceAttachment: ...
    @_builtins.property
    @pulumi.getter(name="attachmentId")
    def attachment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceIndex")
    def device_index(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkCardIndex")
    def network_card_index(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
