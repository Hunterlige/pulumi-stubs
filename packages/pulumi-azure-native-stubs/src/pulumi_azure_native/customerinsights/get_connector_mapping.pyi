import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectorMappingResult",
    "AwaitableGetConnectorMappingResult",
    "get_connector_mapping",
    "get_connector_mapping_output",
]

@pulumi.output_type
class GetConnectorMappingResult:
    def __init__(
        __self__,
        azure_api_version=...,
        connector_mapping_name=...,
        connector_name=...,
        connector_type=...,
        created=...,
        data_format_id=...,
        description=...,
        display_name=...,
        entity_type=...,
        entity_type_name=...,
        id=...,
        last_modified=...,
        mapping_properties=...,
        name=...,
        next_run_time=...,
        run_id=...,
        state=...,
        tenant_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorMappingName")
    def connector_mapping_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataFormatId")
    def data_format_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="entityTypeName")
    def entity_type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mappingProperties")
    def mapping_properties(self) -> outputs.ConnectorMappingPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextRunTime")
    def next_run_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runId")
    def run_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConnectorMappingResult(GetConnectorMappingResult):
    def __await__(self): ...

def get_connector_mapping(
    connector_name: Optional[_builtins.str] = ...,
    hub_name: Optional[_builtins.str] = ...,
    mapping_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectorMappingResult: ...
def get_connector_mapping_output(
    connector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mapping_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectorMappingResult]: ...
