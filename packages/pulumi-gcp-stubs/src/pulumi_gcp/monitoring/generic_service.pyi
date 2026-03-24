import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GenericServiceArgs", "GenericService"]

@pulumi.input_type
class GenericServiceArgs:
    def __init__(
        __self__,
        *,
        service_id: pulumi.Input[_builtins.str],
        basic_service: Optional[pulumi.Input[GenericServiceBasicServiceArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Input[_builtins.str]: ...
    @service_id.setter
    def service_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="basicService")
    def basic_service(
        self,
    ) -> Optional[pulumi.Input[GenericServiceBasicServiceArgs]]: ...
    @basic_service.setter
    def basic_service(
        self, value: Optional[pulumi.Input[GenericServiceBasicServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_labels.setter
    def user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _GenericServiceState:
    def __init__(
        __self__,
        *,
        basic_service: Optional[pulumi.Input[GenericServiceBasicServiceArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        telemetries: Optional[
            pulumi.Input[Sequence[pulumi.Input[GenericServiceTelemetryArgs]]]
        ] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicService")
    def basic_service(
        self,
    ) -> Optional[pulumi.Input[GenericServiceBasicServiceArgs]]: ...
    @basic_service.setter
    def basic_service(
        self, value: Optional[pulumi.Input[GenericServiceBasicServiceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def telemetries(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GenericServiceTelemetryArgs]]]
    ]: ...
    @telemetries.setter
    def telemetries(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GenericServiceTelemetryArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_labels.setter
    def user_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:monitoring/genericService:GenericService")
class GenericService(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        basic_service: Optional[
            pulumi.Input[
                Union[
                    GenericServiceBasicServiceArgs, GenericServiceBasicServiceArgsDict
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GenericServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        basic_service: Optional[
            pulumi.Input[
                Union[
                    GenericServiceBasicServiceArgs, GenericServiceBasicServiceArgsDict
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
        telemetries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            GenericServiceTelemetryArgs, GenericServiceTelemetryArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        user_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> GenericService: ...
    @_builtins.property
    @pulumi.getter(name="basicService")
    def basic_service(
        self,
    ) -> pulumi.Output[Optional[outputs.GenericServiceBasicService]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def telemetries(
        self,
    ) -> pulumi.Output[Sequence[outputs.GenericServiceTelemetry]]: ...
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
