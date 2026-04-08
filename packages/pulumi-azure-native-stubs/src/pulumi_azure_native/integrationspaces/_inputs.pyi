import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BusinessProcessIdentifierArgs",
    "BusinessProcessIdentifierArgsDict",
    "BusinessProcessMappingItemArgs",
    "BusinessProcessMappingItemArgsDict",
    "BusinessProcessStageArgs",
    "BusinessProcessStageArgsDict",
    "TrackingDataStoreArgs",
    "TrackingDataStoreArgsDict",
]

class BusinessProcessIdentifierArgsDict(TypedDict):
    property_name: NotRequired[pulumi.Input[_builtins.str]]
    property_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BusinessProcessIdentifierArgs:
    def __init__(
        __self__,
        *,
        property_name: Optional[pulumi.Input[_builtins.str]] = ...,
        property_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propertyType")
    def property_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @property_type.setter
    def property_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BusinessProcessMappingItemArgsDict(TypedDict):
    logic_app_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    operation_name: NotRequired[pulumi.Input[_builtins.str]]
    operation_type: NotRequired[pulumi.Input[_builtins.str]]
    workflow_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BusinessProcessMappingItemArgs:
    def __init__(
        __self__,
        *,
        logic_app_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        operation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logic_app_resource_id.setter
    def logic_app_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation_name.setter
    def operation_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation_type.setter
    def operation_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow_name.setter
    def workflow_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BusinessProcessStageArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    stages_before: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BusinessProcessStageArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        stages_before: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stagesBefore")
    def stages_before(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @stages_before.setter
    def stages_before(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TrackingDataStoreArgsDict(TypedDict):
    data_store_ingestion_uri: NotRequired[pulumi.Input[_builtins.str]]
    data_store_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    data_store_uri: NotRequired[pulumi.Input[_builtins.str]]
    database_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TrackingDataStoreArgs:
    def __init__(
        __self__,
        *,
        data_store_ingestion_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        data_store_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_store_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreIngestionUri")
    def data_store_ingestion_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_store_ingestion_uri.setter
    def data_store_ingestion_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataStoreResourceId")
    def data_store_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_store_resource_id.setter
    def data_store_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataStoreUri")
    def data_store_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_store_uri.setter
    def data_store_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
