import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataTableArgs", "DataTable"]

@pulumi.input_type
class DataTableArgs:
    def __init__(
        __self__,
        *,
        data_table_id: pulumi.Input[_builtins.str],
        description: pulumi.Input[_builtins.str],
        instance: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        column_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataTableColumnInfoArgs]]]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_info: Optional[pulumi.Input[DataTableScopeInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataTableId")
    def data_table_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_table_id.setter
    def data_table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]: ...
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="columnInfos")
    def column_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataTableColumnInfoArgs]]]]: ...
    @column_infos.setter
    def column_infos(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataTableColumnInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rowTimeToLive")
    def row_time_to_live(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @row_time_to_live.setter
    def row_time_to_live(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scopeInfo")
    def scope_info(self) -> Optional[pulumi.Input[DataTableScopeInfoArgs]]: ...
    @scope_info.setter
    def scope_info(self, value: Optional[pulumi.Input[DataTableScopeInfoArgs]]): ...

@pulumi.input_type
class _DataTableState:
    def __init__(
        __self__,
        *,
        approximate_row_count: Optional[pulumi.Input[_builtins.int]] = ...,
        column_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataTableColumnInfoArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_table_uuid: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        row_time_to_live_update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_associations_count: Optional[pulumi.Input[_builtins.int]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        scope_info: Optional[pulumi.Input[DataTableScopeInfoArgs]] = ...,
        update_source: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approximateRowCount")
    def approximate_row_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @approximate_row_count.setter
    def approximate_row_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="columnInfos")
    def column_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataTableColumnInfoArgs]]]]: ...
    @column_infos.setter
    def column_infos(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataTableColumnInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataTableId")
    def data_table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_table_id.setter
    def data_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataTableUuid")
    def data_table_uuid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_table_uuid.setter
    def data_table_uuid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter(name="rowTimeToLive")
    def row_time_to_live(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @row_time_to_live.setter
    def row_time_to_live(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rowTimeToLiveUpdateTime")
    def row_time_to_live_update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @row_time_to_live_update_time.setter
    def row_time_to_live_update_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ruleAssociationsCount")
    def rule_associations_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rule_associations_count.setter
    def rule_associations_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scopeInfo")
    def scope_info(self) -> Optional[pulumi.Input[DataTableScopeInfoArgs]]: ...
    @scope_info.setter
    def scope_info(self, value: Optional[pulumi.Input[DataTableScopeInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="updateSource")
    def update_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_source.setter
    def update_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:chronicle/dataTable:DataTable")
class DataTable(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        column_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DataTableColumnInfoArgs, DataTableColumnInfoArgsDict]
                    ]
                ]
            ]
        ] = ...,
        data_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        scope_info: Optional[
            pulumi.Input[Union[DataTableScopeInfoArgs, DataTableScopeInfoArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DataTableArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        approximate_row_count: Optional[pulumi.Input[_builtins.int]] = ...,
        column_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DataTableColumnInfoArgs, DataTableColumnInfoArgsDict]
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_table_uuid: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        row_time_to_live: Optional[pulumi.Input[_builtins.str]] = ...,
        row_time_to_live_update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_associations_count: Optional[pulumi.Input[_builtins.int]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        scope_info: Optional[
            pulumi.Input[Union[DataTableScopeInfoArgs, DataTableScopeInfoArgsDict]]
        ] = ...,
        update_source: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DataTable: ...
    @_builtins.property
    @pulumi.getter(name="approximateRowCount")
    def approximate_row_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="columnInfos")
    def column_infos(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DataTableColumnInfo]]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataTableId")
    def data_table_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataTableUuid")
    def data_table_uuid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rowTimeToLive")
    def row_time_to_live(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="rowTimeToLiveUpdateTime")
    def row_time_to_live_update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleAssociationsCount")
    def rule_associations_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scopeInfo")
    def scope_info(self) -> pulumi.Output[Optional[outputs.DataTableScopeInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="updateSource")
    def update_source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
