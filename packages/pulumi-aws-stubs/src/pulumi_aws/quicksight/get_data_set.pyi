import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDataSetResult",
    "AwaitableGetDataSetResult",
    "get_data_set",
    "get_data_set_output",
]

@pulumi.output_type
class GetDataSetResult:
    def __init__(
        __self__,
        arn=...,
        aws_account_id=...,
        column_groups=...,
        column_level_permission_rules=...,
        data_set_id=...,
        data_set_usage_configurations=...,
        field_folders=...,
        id=...,
        import_mode=...,
        logical_table_maps=...,
        name=...,
        permissions=...,
        physical_table_maps=...,
        region=...,
        row_level_permission_data_sets=...,
        row_level_permission_tag_configurations=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="columnGroups")
    def column_groups(self) -> Sequence[outputs.GetDataSetColumnGroupResult]: ...
    @_builtins.property
    @pulumi.getter(name="columnLevelPermissionRules")
    def column_level_permission_rules(
        self,
    ) -> Sequence[outputs.GetDataSetColumnLevelPermissionRuleResult]: ...
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetUsageConfigurations")
    def data_set_usage_configurations(
        self,
    ) -> Sequence[outputs.GetDataSetDataSetUsageConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter(name="fieldFolders")
    def field_folders(self) -> Sequence[outputs.GetDataSetFieldFolderResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="importMode")
    def import_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logicalTableMaps")
    def logical_table_maps(
        self,
    ) -> Sequence[outputs.GetDataSetLogicalTableMapResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[outputs.GetDataSetPermissionResult]: ...
    @_builtins.property
    @pulumi.getter(name="physicalTableMaps")
    def physical_table_maps(
        self,
    ) -> Sequence[outputs.GetDataSetPhysicalTableMapResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionDataSets")
    def row_level_permission_data_sets(
        self,
    ) -> Sequence[outputs.GetDataSetRowLevelPermissionDataSetResult]: ...
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionTagConfigurations")
    def row_level_permission_tag_configurations(
        self,
    ) -> Sequence[outputs.GetDataSetRowLevelPermissionTagConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetDataSetResult(GetDataSetResult):
    def __await__(self): ...

def get_data_set(
    aws_account_id: Optional[_builtins.str] = ...,
    data_set_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDataSetResult: ...
def get_data_set_output(
    aws_account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    data_set_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDataSetResult]: ...
