import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MachineImageArgs", "MachineImage"]

@pulumi.input_type
class MachineImageArgs:
    def __init__(
        __self__,
        *,
        source_instance: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_image_encryption_key: Optional[
            pulumi.Input[MachineImageMachineImageEncryptionKeyArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceInstance")
    def source_instance(self) -> pulumi.Input[_builtins.str]: ...
    @source_instance.setter
    def source_instance(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @guest_flush.setter
    def guest_flush(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="machineImageEncryptionKey")
    def machine_image_encryption_key(
        self,
    ) -> Optional[pulumi.Input[MachineImageMachineImageEncryptionKeyArgs]]: ...
    @machine_image_encryption_key.setter
    def machine_image_encryption_key(
        self, value: Optional[pulumi.Input[MachineImageMachineImageEncryptionKeyArgs]]
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
class _MachineImageState:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_image_encryption_key: Optional[
            pulumi.Input[MachineImageMachineImageEncryptionKeyArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        source_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @guest_flush.setter
    def guest_flush(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="machineImageEncryptionKey")
    def machine_image_encryption_key(
        self,
    ) -> Optional[pulumi.Input[MachineImageMachineImageEncryptionKeyArgs]]: ...
    @machine_image_encryption_key.setter
    def machine_image_encryption_key(
        self, value: Optional[pulumi.Input[MachineImageMachineImageEncryptionKeyArgs]]
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
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceInstance")
    def source_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_instance.setter
    def source_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_locations.setter
    def storage_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:compute/machineImage:MachineImage")
class MachineImage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_image_encryption_key: Optional[
            pulumi.Input[
                Union[
                    MachineImageMachineImageEncryptionKeyArgs,
                    MachineImageMachineImageEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        source_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MachineImageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_image_encryption_key: Optional[
            pulumi.Input[
                Union[
                    MachineImageMachineImageEncryptionKeyArgs,
                    MachineImageMachineImageEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        source_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> MachineImage: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="machineImageEncryptionKey")
    def machine_image_encryption_key(
        self,
    ) -> pulumi.Output[Optional[outputs.MachineImageMachineImageEncryptionKey]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceInstance")
    def source_instance(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
