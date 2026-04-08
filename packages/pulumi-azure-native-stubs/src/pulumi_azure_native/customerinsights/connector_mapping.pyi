import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectorMappingArgs", "ConnectorMapping"]

@pulumi.input_type
class ConnectorMappingArgs:
    def __init__(
        __self__,
        *,
        connector_name: pulumi.Input[_builtins.str],
        entity_type: pulumi.Input[EntityTypes],
        entity_type_name: pulumi.Input[_builtins.str],
        hub_name: pulumi.Input[_builtins.str],
        mapping_properties: pulumi.Input[ConnectorMappingPropertiesArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        connector_type: Optional[
            pulumi.Input[Union[_builtins.str, ConnectorTypes]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mapping_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Input[_builtins.str]: ...
    @connector_name.setter
    def connector_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[EntityTypes]: ...
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[EntityTypes]): ...
    @_builtins.property
    @pulumi.getter(name="entityTypeName")
    def entity_type_name(self) -> pulumi.Input[_builtins.str]: ...
    @entity_type_name.setter
    def entity_type_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mappingProperties")
    def mapping_properties(self) -> pulumi.Input[ConnectorMappingPropertiesArgs]: ...
    @mapping_properties.setter
    def mapping_properties(
        self, value: pulumi.Input[ConnectorMappingPropertiesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectorTypes]]]: ...
    @connector_type.setter
    def connector_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectorTypes]]]
    ): ...
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
    @pulumi.getter(name="mappingName")
    def mapping_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mapping_name.setter
    def mapping_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:customerinsights:ConnectorMapping")
class ConnectorMapping(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
        connector_type: Optional[
            pulumi.Input[Union[_builtins.str, ConnectorTypes]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entity_type: Optional[pulumi.Input[EntityTypes]] = ...,
        entity_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mapping_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mapping_properties: Optional[
            pulumi.Input[
                Union[
                    ConnectorMappingPropertiesArgs, ConnectorMappingPropertiesArgsDict
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConnectorMappingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ConnectorMapping: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorMappingName")
    def connector_mapping_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataFormatId")
    def data_format_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityTypeName")
    def entity_type_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mappingProperties")
    def mapping_properties(
        self,
    ) -> pulumi.Output[outputs.ConnectorMappingPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextRunTime")
    def next_run_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runId")
    def run_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
