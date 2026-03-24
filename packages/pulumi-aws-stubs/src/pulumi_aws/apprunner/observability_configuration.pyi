import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ObservabilityConfigurationArgs", "ObservabilityConfiguration"]

@pulumi.input_type
class ObservabilityConfigurationArgs:
    def __init__(
        __self__,
        *,
        observability_configuration_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        trace_configuration: Optional[
            pulumi.Input[ObservabilityConfigurationTraceConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfigurationName")
    def observability_configuration_name(self) -> pulumi.Input[_builtins.str]: ...
    @observability_configuration_name.setter
    def observability_configuration_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="traceConfiguration")
    def trace_configuration(
        self,
    ) -> Optional[pulumi.Input[ObservabilityConfigurationTraceConfigurationArgs]]: ...
    @trace_configuration.setter
    def trace_configuration(
        self,
        value: Optional[pulumi.Input[ObservabilityConfigurationTraceConfigurationArgs]],
    ): ...

@pulumi.input_type
class _ObservabilityConfigurationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        observability_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        observability_configuration_revision: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        trace_configuration: Optional[
            pulumi.Input[ObservabilityConfigurationTraceConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def latest(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @latest.setter
    def latest(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfigurationName")
    def observability_configuration_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @observability_configuration_name.setter
    def observability_configuration_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfigurationRevision")
    def observability_configuration_revision(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @observability_configuration_revision.setter
    def observability_configuration_revision(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
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
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="traceConfiguration")
    def trace_configuration(
        self,
    ) -> Optional[pulumi.Input[ObservabilityConfigurationTraceConfigurationArgs]]: ...
    @trace_configuration.setter
    def trace_configuration(
        self,
        value: Optional[pulumi.Input[ObservabilityConfigurationTraceConfigurationArgs]],
    ): ...

@pulumi.type_token(...)
class ObservabilityConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        observability_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        trace_configuration: Optional[
            pulumi.Input[
                Union[
                    ObservabilityConfigurationTraceConfigurationArgs,
                    ObservabilityConfigurationTraceConfigurationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ObservabilityConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        observability_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        observability_configuration_revision: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        trace_configuration: Optional[
            pulumi.Input[
                Union[
                    ObservabilityConfigurationTraceConfigurationArgs,
                    ObservabilityConfigurationTraceConfigurationArgsDict,
                ]
            ]
        ] = ...,
    ) -> ObservabilityConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def latest(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfigurationName")
    def observability_configuration_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="observabilityConfigurationRevision")
    def observability_configuration_revision(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="traceConfiguration")
    def trace_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ObservabilityConfigurationTraceConfiguration]
    ]: ...
