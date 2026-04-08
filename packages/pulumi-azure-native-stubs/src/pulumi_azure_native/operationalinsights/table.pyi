import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TableArgs", "Table"]

@pulumi.input_type
class TableArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        plan: Optional[pulumi.Input[Union[_builtins.str, TablePlanEnum]]] = ...,
        restored_logs: Optional[pulumi.Input[RestoredLogsArgs]] = ...,
        retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        schema: Optional[pulumi.Input[SchemaArgs]] = ...,
        search_results: Optional[pulumi.Input[SearchResultsArgs]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        total_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[Union[_builtins.str, TablePlanEnum]]]: ...
    @plan.setter
    def plan(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TablePlanEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restoredLogs")
    def restored_logs(self) -> Optional[pulumi.Input[RestoredLogsArgs]]: ...
    @restored_logs.setter
    def restored_logs(self, value: Optional[pulumi.Input[RestoredLogsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_in_days.setter
    def retention_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[SchemaArgs]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[SchemaArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="searchResults")
    def search_results(self) -> Optional[pulumi.Input[SearchResultsArgs]]: ...
    @search_results.setter
    def search_results(self, value: Optional[pulumi.Input[SearchResultsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="totalRetentionInDays")
    def total_retention_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_retention_in_days.setter
    def total_retention_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("azure-native:operationalinsights:Table")
class Table(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        plan: Optional[pulumi.Input[Union[_builtins.str, TablePlanEnum]]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        restored_logs: Optional[
            pulumi.Input[Union[RestoredLogsArgs, RestoredLogsArgsDict]]
        ] = ...,
        retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        schema: Optional[pulumi.Input[Union[SchemaArgs, SchemaArgsDict]]] = ...,
        search_results: Optional[
            pulumi.Input[Union[SearchResultsArgs, SearchResultsArgsDict]]
        ] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
        total_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TableArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Table: ...
    @_builtins.property
    @pulumi.getter(name="archiveRetentionInDays")
    def archive_retention_in_days(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastPlanModifiedDate")
    def last_plan_modified_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restoredLogs")
    def restored_logs(
        self,
    ) -> pulumi.Output[Optional[outputs.RestoredLogsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resultStatistics")
    def result_statistics(self) -> pulumi.Output[outputs.ResultStatisticsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInDaysAsDefault")
    def retention_in_days_as_default(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[outputs.SchemaResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="searchResults")
    def search_results(
        self,
    ) -> pulumi.Output[Optional[outputs.SearchResultsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="totalRetentionInDays")
    def total_retention_in_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="totalRetentionInDaysAsDefault")
    def total_retention_in_days_as_default(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
