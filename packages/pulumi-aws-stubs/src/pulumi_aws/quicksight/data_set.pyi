

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataSetArgs', 'DataSet']
@pulumi.input_type
class DataSetArgs:
    def __init__(__self__, *, data_set_id: pulumi.Input[_builtins.str], import_mode: pulumi.Input[_builtins.str], aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., column_groups: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnGroupArgs]]]] = ..., column_level_permission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnLevelPermissionRuleArgs]]]] = ..., data_set_usage_configuration: Optional[pulumi.Input[DataSetDataSetUsageConfigurationArgs]] = ..., field_folders: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetFieldFolderArgs]]]] = ..., logical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetLogicalTableMapArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPermissionArgs]]]] = ..., physical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPhysicalTableMapArgs]]]] = ..., refresh_properties: Optional[pulumi.Input[DataSetRefreshPropertiesArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., row_level_permission_data_set: Optional[pulumi.Input[DataSetRowLevelPermissionDataSetArgs]] = ..., row_level_permission_tag_configuration: Optional[pulumi.Input[DataSetRowLevelPermissionTagConfigurationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., use_as: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_set_id.setter
    def data_set_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importMode")
    def import_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @import_mode.setter
    def import_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnGroups")
    def column_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnGroupArgs]]]]:
        
        ...
    
    @column_groups.setter
    def column_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnLevelPermissionRules")
    def column_level_permission_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnLevelPermissionRuleArgs]]]]:
        
        ...
    
    @column_level_permission_rules.setter
    def column_level_permission_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnLevelPermissionRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetUsageConfiguration")
    def data_set_usage_configuration(self) -> Optional[pulumi.Input[DataSetDataSetUsageConfigurationArgs]]:
        
        ...
    
    @data_set_usage_configuration.setter
    def data_set_usage_configuration(self, value: Optional[pulumi.Input[DataSetDataSetUsageConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldFolders")
    def field_folders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetFieldFolderArgs]]]]:
        
        ...
    
    @field_folders.setter
    def field_folders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetFieldFolderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalTableMaps")
    def logical_table_maps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetLogicalTableMapArgs]]]]:
        
        ...
    
    @logical_table_maps.setter
    def logical_table_maps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetLogicalTableMapArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPermissionArgs]]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalTableMaps")
    def physical_table_maps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPhysicalTableMapArgs]]]]:
        
        ...
    
    @physical_table_maps.setter
    def physical_table_maps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPhysicalTableMapArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshProperties")
    def refresh_properties(self) -> Optional[pulumi.Input[DataSetRefreshPropertiesArgs]]:
        
        ...
    
    @refresh_properties.setter
    def refresh_properties(self, value: Optional[pulumi.Input[DataSetRefreshPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionDataSet")
    def row_level_permission_data_set(self) -> Optional[pulumi.Input[DataSetRowLevelPermissionDataSetArgs]]:
        
        ...
    
    @row_level_permission_data_set.setter
    def row_level_permission_data_set(self, value: Optional[pulumi.Input[DataSetRowLevelPermissionDataSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionTagConfiguration")
    def row_level_permission_tag_configuration(self) -> Optional[pulumi.Input[DataSetRowLevelPermissionTagConfigurationArgs]]:
        
        ...
    
    @row_level_permission_tag_configuration.setter
    def row_level_permission_tag_configuration(self, value: Optional[pulumi.Input[DataSetRowLevelPermissionTagConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useAs")
    def use_as(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @use_as.setter
    def use_as(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DataSetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., column_groups: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnGroupArgs]]]] = ..., column_level_permission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnLevelPermissionRuleArgs]]]] = ..., data_set_id: Optional[pulumi.Input[_builtins.str]] = ..., data_set_usage_configuration: Optional[pulumi.Input[DataSetDataSetUsageConfigurationArgs]] = ..., field_folders: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetFieldFolderArgs]]]] = ..., import_mode: Optional[pulumi.Input[_builtins.str]] = ..., logical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetLogicalTableMapArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_columns: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetOutputColumnArgs]]]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPermissionArgs]]]] = ..., physical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPhysicalTableMapArgs]]]] = ..., refresh_properties: Optional[pulumi.Input[DataSetRefreshPropertiesArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., row_level_permission_data_set: Optional[pulumi.Input[DataSetRowLevelPermissionDataSetArgs]] = ..., row_level_permission_tag_configuration: Optional[pulumi.Input[DataSetRowLevelPermissionTagConfigurationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., use_as: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnGroups")
    def column_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnGroupArgs]]]]:
        
        ...
    
    @column_groups.setter
    def column_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnGroupArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnLevelPermissionRules")
    def column_level_permission_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnLevelPermissionRuleArgs]]]]:
        
        ...
    
    @column_level_permission_rules.setter
    def column_level_permission_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetColumnLevelPermissionRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_set_id.setter
    def data_set_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetUsageConfiguration")
    def data_set_usage_configuration(self) -> Optional[pulumi.Input[DataSetDataSetUsageConfigurationArgs]]:
        
        ...
    
    @data_set_usage_configuration.setter
    def data_set_usage_configuration(self, value: Optional[pulumi.Input[DataSetDataSetUsageConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldFolders")
    def field_folders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetFieldFolderArgs]]]]:
        
        ...
    
    @field_folders.setter
    def field_folders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetFieldFolderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importMode")
    def import_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @import_mode.setter
    def import_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalTableMaps")
    def logical_table_maps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetLogicalTableMapArgs]]]]:
        
        ...
    
    @logical_table_maps.setter
    def logical_table_maps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetLogicalTableMapArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputColumns")
    def output_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetOutputColumnArgs]]]]:
        
        ...
    
    @output_columns.setter
    def output_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetOutputColumnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPermissionArgs]]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalTableMaps")
    def physical_table_maps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPhysicalTableMapArgs]]]]:
        
        ...
    
    @physical_table_maps.setter
    def physical_table_maps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSetPhysicalTableMapArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshProperties")
    def refresh_properties(self) -> Optional[pulumi.Input[DataSetRefreshPropertiesArgs]]:
        
        ...
    
    @refresh_properties.setter
    def refresh_properties(self, value: Optional[pulumi.Input[DataSetRefreshPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionDataSet")
    def row_level_permission_data_set(self) -> Optional[pulumi.Input[DataSetRowLevelPermissionDataSetArgs]]:
        
        ...
    
    @row_level_permission_data_set.setter
    def row_level_permission_data_set(self, value: Optional[pulumi.Input[DataSetRowLevelPermissionDataSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionTagConfiguration")
    def row_level_permission_tag_configuration(self) -> Optional[pulumi.Input[DataSetRowLevelPermissionTagConfigurationArgs]]:
        
        ...
    
    @row_level_permission_tag_configuration.setter
    def row_level_permission_tag_configuration(self, value: Optional[pulumi.Input[DataSetRowLevelPermissionTagConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useAs")
    def use_as(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @use_as.setter
    def use_as(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:quicksight/dataSet:DataSet")
class DataSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., column_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetColumnGroupArgs, DataSetColumnGroupArgsDict]]]]] = ..., column_level_permission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetColumnLevelPermissionRuleArgs, DataSetColumnLevelPermissionRuleArgsDict]]]]] = ..., data_set_id: Optional[pulumi.Input[_builtins.str]] = ..., data_set_usage_configuration: Optional[pulumi.Input[Union[DataSetDataSetUsageConfigurationArgs, DataSetDataSetUsageConfigurationArgsDict]]] = ..., field_folders: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetFieldFolderArgs, DataSetFieldFolderArgsDict]]]]] = ..., import_mode: Optional[pulumi.Input[_builtins.str]] = ..., logical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetLogicalTableMapArgs, DataSetLogicalTableMapArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetPermissionArgs, DataSetPermissionArgsDict]]]]] = ..., physical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetPhysicalTableMapArgs, DataSetPhysicalTableMapArgsDict]]]]] = ..., refresh_properties: Optional[pulumi.Input[Union[DataSetRefreshPropertiesArgs, DataSetRefreshPropertiesArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., row_level_permission_data_set: Optional[pulumi.Input[Union[DataSetRowLevelPermissionDataSetArgs, DataSetRowLevelPermissionDataSetArgsDict]]] = ..., row_level_permission_tag_configuration: Optional[pulumi.Input[Union[DataSetRowLevelPermissionTagConfigurationArgs, DataSetRowLevelPermissionTagConfigurationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., use_as: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DataSetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., column_groups: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetColumnGroupArgs, DataSetColumnGroupArgsDict]]]]] = ..., column_level_permission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetColumnLevelPermissionRuleArgs, DataSetColumnLevelPermissionRuleArgsDict]]]]] = ..., data_set_id: Optional[pulumi.Input[_builtins.str]] = ..., data_set_usage_configuration: Optional[pulumi.Input[Union[DataSetDataSetUsageConfigurationArgs, DataSetDataSetUsageConfigurationArgsDict]]] = ..., field_folders: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetFieldFolderArgs, DataSetFieldFolderArgsDict]]]]] = ..., import_mode: Optional[pulumi.Input[_builtins.str]] = ..., logical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetLogicalTableMapArgs, DataSetLogicalTableMapArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_columns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetOutputColumnArgs, DataSetOutputColumnArgsDict]]]]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetPermissionArgs, DataSetPermissionArgsDict]]]]] = ..., physical_table_maps: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DataSetPhysicalTableMapArgs, DataSetPhysicalTableMapArgsDict]]]]] = ..., refresh_properties: Optional[pulumi.Input[Union[DataSetRefreshPropertiesArgs, DataSetRefreshPropertiesArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., row_level_permission_data_set: Optional[pulumi.Input[Union[DataSetRowLevelPermissionDataSetArgs, DataSetRowLevelPermissionDataSetArgsDict]]] = ..., row_level_permission_tag_configuration: Optional[pulumi.Input[Union[DataSetRowLevelPermissionTagConfigurationArgs, DataSetRowLevelPermissionTagConfigurationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., use_as: Optional[pulumi.Input[_builtins.str]] = ...) -> DataSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnGroups")
    def column_groups(self) -> pulumi.Output[Optional[Sequence[outputs.DataSetColumnGroup]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="columnLevelPermissionRules")
    def column_level_permission_rules(self) -> pulumi.Output[Optional[Sequence[outputs.DataSetColumnLevelPermissionRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSetUsageConfiguration")
    def data_set_usage_configuration(self) -> pulumi.Output[outputs.DataSetDataSetUsageConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldFolders")
    def field_folders(self) -> pulumi.Output[Optional[Sequence[outputs.DataSetFieldFolder]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importMode")
    def import_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalTableMaps")
    def logical_table_maps(self) -> pulumi.Output[Sequence[outputs.DataSetLogicalTableMap]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputColumns")
    def output_columns(self) -> pulumi.Output[Sequence[outputs.DataSetOutputColumn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence[outputs.DataSetPermission]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalTableMaps")
    def physical_table_maps(self) -> pulumi.Output[Optional[Sequence[outputs.DataSetPhysicalTableMap]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshProperties")
    def refresh_properties(self) -> pulumi.Output[Optional[outputs.DataSetRefreshProperties]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionDataSet")
    def row_level_permission_data_set(self) -> pulumi.Output[Optional[outputs.DataSetRowLevelPermissionDataSet]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowLevelPermissionTagConfiguration")
    def row_level_permission_tag_configuration(self) -> pulumi.Output[Optional[outputs.DataSetRowLevelPermissionTagConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useAs")
    def use_as(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


