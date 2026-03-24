import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceArgs", "Service"]

@pulumi.input_type
class ServiceArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        autogenerate_revision_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        metadata: Optional[pulumi.Input[ServiceMetadataArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        template: Optional[pulumi.Input[ServiceTemplateArgs]] = ...,
        traffics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autogenerateRevisionName")
    def autogenerate_revision_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @autogenerate_revision_name.setter
    def autogenerate_revision_name(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[ServiceMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[ServiceMetadataArgs]]): ...
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
    def template(self) -> Optional[pulumi.Input[ServiceTemplateArgs]]: ...
    @template.setter
    def template(self, value: Optional[pulumi.Input[ServiceTemplateArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def traffics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]: ...
    @traffics.setter
    def traffics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]
    ): ...

@pulumi.input_type
class _ServiceState:
    def __init__(
        __self__,
        *,
        autogenerate_revision_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[pulumi.Input[ServiceMetadataArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceStatusArgs]]]
        ] = ...,
        template: Optional[pulumi.Input[ServiceTemplateArgs]] = ...,
        traffics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autogenerateRevisionName")
    def autogenerate_revision_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @autogenerate_revision_name.setter
    def autogenerate_revision_name(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[ServiceMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[ServiceMetadataArgs]]): ...
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
    def statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceStatusArgs]]]]: ...
    @statuses.setter
    def statuses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceStatusArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[ServiceTemplateArgs]]: ...
    @template.setter
    def template(self, value: Optional[pulumi.Input[ServiceTemplateArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def traffics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]: ...
    @traffics.setter
    def traffics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]
    ): ...

@pulumi.type_token("gcp:cloudrun/service:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        autogenerate_revision_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Union[ServiceMetadataArgs, ServiceMetadataArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        template: Optional[
            pulumi.Input[Union[ServiceTemplateArgs, ServiceTemplateArgsDict]]
        ] = ...,
        traffics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ServiceTrafficArgs, ServiceTrafficArgsDict]]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        autogenerate_revision_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Union[ServiceMetadataArgs, ServiceMetadataArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ServiceStatusArgs, ServiceStatusArgsDict]]]
            ]
        ] = ...,
        template: Optional[
            pulumi.Input[Union[ServiceTemplateArgs, ServiceTemplateArgsDict]]
        ] = ...,
        traffics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ServiceTrafficArgs, ServiceTrafficArgsDict]]
                ]
            ]
        ] = ...,
    ) -> Service: ...
    @_builtins.property
    @pulumi.getter(name="autogenerateRevisionName")
    def autogenerate_revision_name(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[outputs.ServiceMetadata]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.ServiceStatus]]: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Output[Optional[outputs.ServiceTemplate]]: ...
    @_builtins.property
    @pulumi.getter
    def traffics(self) -> pulumi.Output[Sequence[outputs.ServiceTraffic]]: ...
