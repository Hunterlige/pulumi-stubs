import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PublishedBlueprintArgs", "PublishedBlueprint"]

@pulumi.input_type
class PublishedBlueprintArgs:
    def __init__(
        __self__,
        *,
        blueprint_name: pulumi.Input[_builtins.str],
        resource_scope: pulumi.Input[_builtins.str],
        change_notes: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterDefinitionArgs]]]
        ] = ...,
        resource_groups: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ResourceGroupDefinitionArgs]]]
        ] = ...,
        target_scope: Optional[
            pulumi.Input[Union[_builtins.str, BlueprintTargetScope]]
        ] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueprintName")
    def blueprint_name(self) -> pulumi.Input[_builtins.str]: ...
    @blueprint_name.setter
    def blueprint_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceScope")
    def resource_scope(self) -> pulumi.Input[_builtins.str]: ...
    @resource_scope.setter
    def resource_scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="changeNotes")
    def change_notes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @change_notes.setter
    def change_notes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ParameterDefinitionArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ParameterDefinitionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ResourceGroupDefinitionArgs]]]
    ]: ...
    @resource_groups.setter
    def resource_groups(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ResourceGroupDefinitionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetScope")
    def target_scope(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BlueprintTargetScope]]]: ...
    @target_scope.setter
    def target_scope(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BlueprintTargetScope]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:blueprint:PublishedBlueprint")
class PublishedBlueprint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        blueprint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        change_notes: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[ParameterDefinitionArgs, ParameterDefinitionArgsDict]
                    ],
                ]
            ]
        ] = ...,
        resource_groups: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            ResourceGroupDefinitionArgs, ResourceGroupDefinitionArgsDict
                        ]
                    ],
                ]
            ]
        ] = ...,
        resource_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        target_scope: Optional[
            pulumi.Input[Union[_builtins.str, BlueprintTargetScope]]
        ] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PublishedBlueprintArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> PublishedBlueprint: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blueprintName")
    def blueprint_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="changeNotes")
    def change_notes(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, outputs.ParameterDefinitionResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(
        self,
    ) -> pulumi.Output[
        Optional[Mapping[str, outputs.ResourceGroupDefinitionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.BlueprintStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="targetScope")
    def target_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
