import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProjectSinkArgs", "ProjectSink"]

@pulumi.input_type
class ProjectSinkArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[_builtins.str],
        bigquery_options: Optional[pulumi.Input[ProjectSinkBigqueryOptionsArgs]] = ...,
        custom_writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSinkExclusionArgs]]]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_writer_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(
        self,
    ) -> Optional[pulumi.Input[ProjectSinkBigqueryOptionsArgs]]: ...
    @bigquery_options.setter
    def bigquery_options(
        self, value: Optional[pulumi.Input[ProjectSinkBigqueryOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customWriterIdentity")
    def custom_writer_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_writer_identity.setter
    def custom_writer_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProjectSinkExclusionArgs]]]]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectSinkExclusionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="uniqueWriterIdentity")
    def unique_writer_identity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_writer_identity.setter
    def unique_writer_identity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _ProjectSinkState:
    def __init__(
        __self__,
        *,
        bigquery_options: Optional[pulumi.Input[ProjectSinkBigqueryOptionsArgs]] = ...,
        custom_writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProjectSinkExclusionArgs]]]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_writer_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
        writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(
        self,
    ) -> Optional[pulumi.Input[ProjectSinkBigqueryOptionsArgs]]: ...
    @bigquery_options.setter
    def bigquery_options(
        self, value: Optional[pulumi.Input[ProjectSinkBigqueryOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customWriterIdentity")
    def custom_writer_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_writer_identity.setter
    def custom_writer_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProjectSinkExclusionArgs]]]]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ProjectSinkExclusionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="uniqueWriterIdentity")
    def unique_writer_identity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_writer_identity.setter
    def unique_writer_identity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @writer_identity.setter
    def writer_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:logging/projectSink:ProjectSink")
class ProjectSink(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bigquery_options: Optional[
            pulumi.Input[
                Union[
                    ProjectSinkBigqueryOptionsArgs, ProjectSinkBigqueryOptionsArgsDict
                ]
            ]
        ] = ...,
        custom_writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ProjectSinkExclusionArgs, ProjectSinkExclusionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_writer_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProjectSinkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bigquery_options: Optional[
            pulumi.Input[
                Union[
                    ProjectSinkBigqueryOptionsArgs, ProjectSinkBigqueryOptionsArgsDict
                ]
            ]
        ] = ...,
        custom_writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ProjectSinkExclusionArgs, ProjectSinkExclusionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_writer_identity: Optional[pulumi.Input[_builtins.bool]] = ...,
        writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ProjectSink: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> pulumi.Output[outputs.ProjectSinkBigqueryOptions]: ...
    @_builtins.property
    @pulumi.getter(name="customWriterIdentity")
    def custom_writer_identity(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ProjectSinkExclusion]]]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueWriterIdentity")
    def unique_writer_identity(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> pulumi.Output[_builtins.str]: ...
