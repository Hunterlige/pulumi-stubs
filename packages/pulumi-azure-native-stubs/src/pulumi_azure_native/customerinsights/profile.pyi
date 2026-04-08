import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProfileArgs", "Profile"]

@pulumi.input_type
class ProfileArgs:
    def __init__(
        __self__,
        *,
        hub_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        api_entity_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        attributes: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        entity_type: Optional[pulumi.Input[EntityTypes]] = ...,
        fields: Optional[
            pulumi.Input[Sequence[pulumi.Input[PropertyDefinitionArgs]]]
        ] = ...,
        instances_count: Optional[pulumi.Input[_builtins.int]] = ...,
        large_image: Optional[pulumi.Input[_builtins.str]] = ...,
        localized_attributes: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        medium_image: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_item_type_link: Optional[pulumi.Input[_builtins.str]] = ...,
        small_image: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_ids: Optional[pulumi.Input[Sequence[pulumi.Input[StrongIdArgs]]]] = ...,
        timestamp_field_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiEntitySetName")
    def api_entity_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_entity_set_name.setter
    def api_entity_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]]
    ]: ...
    @attributes.setter
    def attributes(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...
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
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[EntityTypes]]: ...
    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[EntityTypes]]): ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PropertyDefinitionArgs]]]]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PropertyDefinitionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instancesCount")
    def instances_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instances_count.setter
    def instances_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="largeImage")
    def large_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @large_image.setter
    def large_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localizedAttributes")
    def localized_attributes(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
        ]
    ]: ...
    @localized_attributes.setter
    def localized_attributes(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mediumImage")
    def medium_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medium_image.setter
    def medium_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_name.setter
    def profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaItemTypeLink")
    def schema_item_type_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_item_type_link.setter
    def schema_item_type_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="smallImage")
    def small_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @small_image.setter
    def small_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongIds")
    def strong_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[StrongIdArgs]]]]: ...
    @strong_ids.setter
    def strong_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StrongIdArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampFieldName")
    def timestamp_field_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_field_name.setter
    def timestamp_field_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:customerinsights:Profile")
class Profile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_entity_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        attributes: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        description: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        entity_type: Optional[pulumi.Input[EntityTypes]] = ...,
        fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PropertyDefinitionArgs, PropertyDefinitionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instances_count: Optional[pulumi.Input[_builtins.int]] = ...,
        large_image: Optional[pulumi.Input[_builtins.str]] = ...,
        localized_attributes: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        medium_image: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_item_type_link: Optional[pulumi.Input[_builtins.str]] = ...,
        small_image: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[StrongIdArgs, StrongIdArgsDict]]]]
        ] = ...,
        timestamp_field_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Profile: ...
    @_builtins.property
    @pulumi.getter(name="apiEntitySetName")
    def api_entity_set_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, Sequence[_builtins.str]]]]: ...
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
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PropertyDefinitionResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="instancesCount")
    def instances_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="largeImage")
    def large_image(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastChangedUtc")
    def last_changed_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localizedAttributes")
    def localized_attributes(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, Mapping[str, _builtins.str]]]]: ...
    @_builtins.property
    @pulumi.getter(name="mediumImage")
    def medium_image(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaItemTypeLink")
    def schema_item_type_link(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="smallImage")
    def small_image(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="strongIds")
    def strong_ids(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.StrongIdResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timestampFieldName")
    def timestamp_field_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
