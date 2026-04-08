import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LinkArgs", "Link"]

@pulumi.input_type
class LinkArgs:
    def __init__(
        __self__,
        *,
        hub_name: pulumi.Input[_builtins.str],
        participant_property_references: pulumi.Input[
            Sequence[pulumi.Input[ParticipantPropertyReferenceArgs]]
        ],
        resource_group_name: pulumi.Input[_builtins.str],
        source_entity_type: pulumi.Input[EntityType],
        source_entity_type_name: pulumi.Input[_builtins.str],
        target_entity_type: pulumi.Input[EntityType],
        target_entity_type_name: pulumi.Input[_builtins.str],
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        link_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mappings: Optional[
            pulumi.Input[Sequence[pulumi.Input[TypePropertiesMappingArgs]]]
        ] = ...,
        operation_type: Optional[pulumi.Input[InstanceOperationType]] = ...,
        reference_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="participantPropertyReferences")
    def participant_property_references(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ParticipantPropertyReferenceArgs]]]: ...
    @participant_property_references.setter
    def participant_property_references(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[ParticipantPropertyReferenceArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEntityType")
    def source_entity_type(self) -> pulumi.Input[EntityType]: ...
    @source_entity_type.setter
    def source_entity_type(self, value: pulumi.Input[EntityType]): ...
    @_builtins.property
    @pulumi.getter(name="sourceEntityTypeName")
    def source_entity_type_name(self) -> pulumi.Input[_builtins.str]: ...
    @source_entity_type_name.setter
    def source_entity_type_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetEntityType")
    def target_entity_type(self) -> pulumi.Input[EntityType]: ...
    @target_entity_type.setter
    def target_entity_type(self, value: pulumi.Input[EntityType]): ...
    @_builtins.property
    @pulumi.getter(name="targetEntityTypeName")
    def target_entity_type_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_entity_type_name.setter
    def target_entity_type_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @description.setter
    def description(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @display_name.setter
    def display_name(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkName")
    def link_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @link_name.setter
    def link_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mappings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TypePropertiesMappingArgs]]]]: ...
    @mappings.setter
    def mappings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TypePropertiesMappingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[pulumi.Input[InstanceOperationType]]: ...
    @operation_type.setter
    def operation_type(self, value: Optional[pulumi.Input[InstanceOperationType]]): ...
    @_builtins.property
    @pulumi.getter(name="referenceOnly")
    def reference_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reference_only.setter
    def reference_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("azure-native:customerinsights:Link")
class Link(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        link_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mappings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TypePropertiesMappingArgs, TypePropertiesMappingArgsDict]
                    ]
                ]
            ]
        ] = ...,
        operation_type: Optional[pulumi.Input[InstanceOperationType]] = ...,
        participant_property_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ParticipantPropertyReferenceArgs,
                            ParticipantPropertyReferenceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        reference_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_entity_type: Optional[pulumi.Input[EntityType]] = ...,
        source_entity_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_entity_type: Optional[pulumi.Input[EntityType]] = ...,
        target_entity_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LinkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Link: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="linkName")
    def link_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mappings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TypePropertiesMappingResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="participantPropertyReferences")
    def participant_property_references(
        self,
    ) -> pulumi.Output[Sequence[outputs.ParticipantPropertyReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="referenceOnly")
    def reference_only(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceEntityType")
    def source_entity_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceEntityTypeName")
    def source_entity_type_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetEntityType")
    def target_entity_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetEntityTypeName")
    def target_entity_type_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
