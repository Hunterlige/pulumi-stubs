import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PacketMirroringArgs", "PacketMirroring"]

@pulumi.input_type
class PacketMirroringArgs:
    def __init__(
        __self__,
        *,
        collector_ilb: pulumi.Input[PacketMirroringCollectorIlbArgs],
        mirrored_resources: pulumi.Input[PacketMirroringMirroredResourcesArgs],
        network: pulumi.Input[PacketMirroringNetworkArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[PacketMirroringFilterArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectorIlb")
    def collector_ilb(self) -> pulumi.Input[PacketMirroringCollectorIlbArgs]: ...
    @collector_ilb.setter
    def collector_ilb(self, value: pulumi.Input[PacketMirroringCollectorIlbArgs]): ...
    @_builtins.property
    @pulumi.getter(name="mirroredResources")
    def mirrored_resources(
        self,
    ) -> pulumi.Input[PacketMirroringMirroredResourcesArgs]: ...
    @mirrored_resources.setter
    def mirrored_resources(
        self, value: pulumi.Input[PacketMirroringMirroredResourcesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[PacketMirroringNetworkArgs]: ...
    @network.setter
    def network(self, value: pulumi.Input[PacketMirroringNetworkArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[PacketMirroringFilterArgs]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[PacketMirroringFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PacketMirroringState:
    def __init__(
        __self__,
        *,
        collector_ilb: Optional[pulumi.Input[PacketMirroringCollectorIlbArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[PacketMirroringFilterArgs]] = ...,
        mirrored_resources: Optional[
            pulumi.Input[PacketMirroringMirroredResourcesArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[PacketMirroringNetworkArgs]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectorIlb")
    def collector_ilb(
        self,
    ) -> Optional[pulumi.Input[PacketMirroringCollectorIlbArgs]]: ...
    @collector_ilb.setter
    def collector_ilb(
        self, value: Optional[pulumi.Input[PacketMirroringCollectorIlbArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[PacketMirroringFilterArgs]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[PacketMirroringFilterArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="mirroredResources")
    def mirrored_resources(
        self,
    ) -> Optional[pulumi.Input[PacketMirroringMirroredResourcesArgs]]: ...
    @mirrored_resources.setter
    def mirrored_resources(
        self, value: Optional[pulumi.Input[PacketMirroringMirroredResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[PacketMirroringNetworkArgs]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[PacketMirroringNetworkArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/packetMirroring:PacketMirroring")
class PacketMirroring(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        collector_ilb: Optional[
            pulumi.Input[
                Union[
                    PacketMirroringCollectorIlbArgs, PacketMirroringCollectorIlbArgsDict
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[PacketMirroringFilterArgs, PacketMirroringFilterArgsDict]
            ]
        ] = ...,
        mirrored_resources: Optional[
            pulumi.Input[
                Union[
                    PacketMirroringMirroredResourcesArgs,
                    PacketMirroringMirroredResourcesArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[
            pulumi.Input[
                Union[PacketMirroringNetworkArgs, PacketMirroringNetworkArgsDict]
            ]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PacketMirroringArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        collector_ilb: Optional[
            pulumi.Input[
                Union[
                    PacketMirroringCollectorIlbArgs, PacketMirroringCollectorIlbArgsDict
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enable: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[
            pulumi.Input[
                Union[PacketMirroringFilterArgs, PacketMirroringFilterArgsDict]
            ]
        ] = ...,
        mirrored_resources: Optional[
            pulumi.Input[
                Union[
                    PacketMirroringMirroredResourcesArgs,
                    PacketMirroringMirroredResourcesArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[
            pulumi.Input[
                Union[PacketMirroringNetworkArgs, PacketMirroringNetworkArgsDict]
            ]
        ] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> PacketMirroring: ...
    @_builtins.property
    @pulumi.getter(name="collectorIlb")
    def collector_ilb(self) -> pulumi.Output[outputs.PacketMirroringCollectorIlb]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[outputs.PacketMirroringFilter]]: ...
    @_builtins.property
    @pulumi.getter(name="mirroredResources")
    def mirrored_resources(
        self,
    ) -> pulumi.Output[outputs.PacketMirroringMirroredResources]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[outputs.PacketMirroringNetwork]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
