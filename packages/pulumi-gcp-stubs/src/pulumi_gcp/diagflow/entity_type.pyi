import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EntityTypeArgs", "EntityType"]

@pulumi.input_type
class EntityTypeArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntityTypeEntityArgs]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fuzzy_extraction.setter
    def enable_fuzzy_extraction(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def entities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EntityTypeEntityArgs]]]]: ...
    @entities.setter
    def entities(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EntityTypeEntityArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EntityTypeState:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities: Optional[
            pulumi.Input[Sequence[pulumi.Input[EntityTypeEntityArgs]]]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fuzzy_extraction.setter
    def enable_fuzzy_extraction(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def entities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EntityTypeEntityArgs]]]]: ...
    @entities.setter
    def entities(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EntityTypeEntityArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("gcp:diagflow/entityType:EntityType")
class EntityType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[EntityTypeEntityArgs, EntityTypeEntityArgsDict]]
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EntityTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[EntityTypeEntityArgs, EntityTypeEntityArgsDict]]
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EntityType: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def entities(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.EntityTypeEntity]]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
