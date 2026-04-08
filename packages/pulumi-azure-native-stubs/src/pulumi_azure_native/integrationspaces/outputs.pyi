import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    "BusinessProcessIdentifierResponse",
    "BusinessProcessMappingItemResponse",
    "BusinessProcessReferenceResponse",
    "BusinessProcessStageResponse",
    "FlowTrackingDefinitionResponse",
    ...,
    "SystemDataResponse",
    "TrackingCorrelationContextResponse",
    "TrackingDataStoreResponse",
    "TrackingEventDefinitionResponse",
    "TrackingProfileDefinitionResponse",
]

@pulumi.output_type
class BusinessProcessDevelopmentArtifactPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        business_process_mapping: Optional[
            Mapping[str, outputs.BusinessProcessMappingItemResponse]
        ] = ...,
        business_process_stages: Optional[
            Mapping[str, outputs.BusinessProcessStageResponse]
        ] = ...,
        description: Optional[_builtins.str] = ...,
        identifier: Optional[outputs.BusinessProcessIdentifierResponse] = ...,
        tracking_profiles: Optional[
            Mapping[str, outputs.TrackingProfileDefinitionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="businessProcessMapping")
    def business_process_mapping(
        self,
    ) -> Optional[Mapping[str, outputs.BusinessProcessMappingItemResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="businessProcessStages")
    def business_process_stages(
        self,
    ) -> Optional[Mapping[str, outputs.BusinessProcessStageResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[outputs.BusinessProcessIdentifierResponse]: ...
    @_builtins.property
    @pulumi.getter(name="trackingProfiles")
    def tracking_profiles(
        self,
    ) -> Optional[Mapping[str, outputs.TrackingProfileDefinitionResponse]]: ...

@pulumi.output_type
class BusinessProcessIdentifierResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        property_name: Optional[_builtins.str] = ...,
        property_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyType")
    def property_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BusinessProcessMappingItemResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        logic_app_resource_id: Optional[_builtins.str] = ...,
        operation_name: Optional[_builtins.str] = ...,
        operation_type: Optional[_builtins.str] = ...,
        workflow_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BusinessProcessReferenceResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BusinessProcessStageResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        stages_before: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stagesBefore")
    def stages_before(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FlowTrackingDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        correlation_context: Optional[outputs.TrackingCorrelationContextResponse] = ...,
        events: Optional[Mapping[str, outputs.TrackingEventDefinitionResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="correlationContext")
    def correlation_context(
        self,
    ) -> Optional[outputs.TrackingCorrelationContextResponse]: ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[Mapping[str, outputs.TrackingEventDefinitionResponse]]: ...

@pulumi.output_type
class SaveOrGetBusinessProcessDevelopmentArtifactResponseResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        properties: Optional[
            outputs.BusinessProcessDevelopmentArtifactPropertiesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.BusinessProcessDevelopmentArtifactPropertiesResponse]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrackingCorrelationContextResponse(dict):
    def __init__(
        __self__,
        *,
        operation_name: Optional[_builtins.str] = ...,
        operation_type: Optional[_builtins.str] = ...,
        property_name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrackingDataStoreResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store_ingestion_uri: Optional[_builtins.str] = ...,
        data_store_resource_id: Optional[_builtins.str] = ...,
        data_store_uri: Optional[_builtins.str] = ...,
        database_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreIngestionUri")
    def data_store_ingestion_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreResourceId")
    def data_store_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreUri")
    def data_store_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrackingEventDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        operation_name: Optional[_builtins.str] = ...,
        operation_type: Optional[_builtins.str] = ...,
        properties: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, Any]]: ...

@pulumi.output_type
class TrackingProfileDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        business_process: Optional[outputs.BusinessProcessReferenceResponse] = ...,
        schema: Optional[_builtins.str] = ...,
        tracking_definitions: Optional[
            Mapping[str, outputs.FlowTrackingDefinitionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="businessProcess")
    def business_process(
        self,
    ) -> Optional[outputs.BusinessProcessReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackingDefinitions")
    def tracking_definitions(
        self,
    ) -> Optional[Mapping[str, outputs.FlowTrackingDefinitionResponse]]: ...
