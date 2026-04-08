import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationArgs", "Application"]

@pulumi.input_type
class ApplicationArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        application_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        debug_params: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        diagnostics: Optional[pulumi.Input[DiagnosticsDescriptionArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        services: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceResourceDescriptionArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationResourceName")
    def application_resource_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_resource_name.setter
    def application_resource_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="debugParams")
    def debug_params(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @debug_params.setter
    def debug_params(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[pulumi.Input[DiagnosticsDescriptionArgs]]: ...
    @diagnostics.setter
    def diagnostics(
        self, value: Optional[pulumi.Input[DiagnosticsDescriptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceResourceDescriptionArgs]]]
    ]: ...
    @services.setter
    def services(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceResourceDescriptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:servicefabricmesh:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
        debug_params: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        diagnostics: Optional[
            pulumi.Input[
                Union[DiagnosticsDescriptionArgs, DiagnosticsDescriptionArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        services: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServiceResourceDescriptionArgs,
                            ServiceResourceDescriptionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Application: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="debugParams")
    def debug_params(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(
        self,
    ) -> pulumi.Output[Optional[outputs.DiagnosticsDescriptionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNames")
    def service_names(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ServiceResourceDescriptionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyEvaluation")
    def unhealthy_evaluation(self) -> pulumi.Output[_builtins.str]: ...
