import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ResourceSetArgs", "ResourceSet"]

@pulumi.input_type
class ResourceSetArgs:
    def __init__(
        __self__,
        *,
        resource_set_name: pulumi.Input[_builtins.str],
        resource_set_type: pulumi.Input[_builtins.str],
        resources: pulumi.Input[Sequence[pulumi.Input[ResourceSetResourceArgs]]],
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceSetName")
    def resource_set_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_set_name.setter
    def resource_set_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceSetType")
    def resource_set_type(self) -> pulumi.Input[_builtins.str]: ...
    @resource_set_type.setter
    def resource_set_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ResourceSetResourceArgs]]]: ...
    @resources.setter
    def resources(
        self, value: pulumi.Input[Sequence[pulumi.Input[ResourceSetResourceArgs]]]
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

@pulumi.input_type
class _ResourceSetState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_set_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceSetResourceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceSetName")
    def resource_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_set_name.setter
    def resource_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceSetType")
    def resource_set_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_set_type.setter
    def resource_set_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceSetResourceArgs]]]]: ...
    @resources.setter
    def resources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceSetResourceArgs]]]],
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
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class ResourceSet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        resource_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_set_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ResourceSetResourceArgs, ResourceSetResourceArgsDict]
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
        args: ResourceSetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_set_type: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ResourceSetResourceArgs, ResourceSetResourceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> ResourceSet: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceSetName")
    def resource_set_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceSetType")
    def resource_set_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[outputs.ResourceSetResource]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
