import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainMappingArgs", "DomainMapping"]

@pulumi.input_type
class DomainMappingArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        spec: pulumi.Input[DomainMappingSpecArgs],
        metadata: Optional[pulumi.Input[DomainMappingMetadataArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> pulumi.Input[DomainMappingSpecArgs]: ...
    @spec.setter
    def spec(self, value: pulumi.Input[DomainMappingSpecArgs]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[DomainMappingMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[DomainMappingMetadataArgs]]): ...
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
class _DomainMappingState:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[pulumi.Input[DomainMappingMetadataArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[pulumi.Input[DomainMappingSpecArgs]] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[DomainMappingMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[DomainMappingMetadataArgs]]): ...
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
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[DomainMappingSpecArgs]]: ...
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[DomainMappingSpecArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusArgs]]]]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusArgs]]]],
    ): ...

@pulumi.type_token("gcp:cloudrun/domainMapping:DomainMapping")
class DomainMapping(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[
                Union[DomainMappingMetadataArgs, DomainMappingMetadataArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[
            pulumi.Input[Union[DomainMappingSpecArgs, DomainMappingSpecArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainMappingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[
                Union[DomainMappingMetadataArgs, DomainMappingMetadataArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        spec: Optional[
            pulumi.Input[Union[DomainMappingSpecArgs, DomainMappingSpecArgsDict]]
        ] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DomainMappingStatusArgs, DomainMappingStatusArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> DomainMapping: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[outputs.DomainMappingMetadata]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> pulumi.Output[outputs.DomainMappingSpec]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.DomainMappingStatus]]: ...
