import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEventGridDataConnectionResult",
    "AwaitableGetEventGridDataConnectionResult",
    "get_event_grid_data_connection",
    "get_event_grid_data_connection_output",
]

@pulumi.output_type
class GetEventGridDataConnectionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        blob_storage_event_type=...,
        consumer_group=...,
        data_format=...,
        event_hub_resource_id=...,
        id=...,
        ignore_first_record=...,
        kind=...,
        location=...,
        mapping_rule_name=...,
        name=...,
        provisioning_state=...,
        storage_account_resource_id=...,
        system_data=...,
        table_name=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="blobStorageEventType")
    def blob_storage_event_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ignoreFirstRecord")
    def ignore_first_record(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetEventGridDataConnectionResult(GetEventGridDataConnectionResult):
    def __await__(self): ...

def get_event_grid_data_connection(
    data_connection_name: Optional[_builtins.str] = ...,
    database_name: Optional[_builtins.str] = ...,
    kusto_pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEventGridDataConnectionResult: ...
def get_event_grid_data_connection_output(
    data_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    kusto_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEventGridDataConnectionResult]: ...
