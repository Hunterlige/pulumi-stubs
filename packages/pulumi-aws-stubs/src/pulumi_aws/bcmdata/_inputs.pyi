

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExportExportArgs', 'ExportExportArgsDict', 'ExportExportDataQueryArgs', 'ExportExportDataQueryArgsDict', 'ExportExportDestinationConfigurationArgs', 'ExportExportDestinationConfigurationArgsDict', ..., ..., ..., ..., 'ExportExportRefreshCadenceArgs', 'ExportExportRefreshCadenceArgsDict', 'ExportTimeoutsArgs', 'ExportTimeoutsArgsDict']
class ExportExportArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    data_queries: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExportExportDataQueryArgsDict]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    destination_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationArgsDict]]]]
    export_arn: NotRequired[pulumi.Input[_builtins.str]]
    refresh_cadences: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExportExportRefreshCadenceArgsDict]]]]


@pulumi.input_type
class ExportExportArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], data_queries: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDataQueryArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationArgs]]]] = ..., export_arn: Optional[pulumi.Input[_builtins.str]] = ..., refresh_cadences: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportRefreshCadenceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataQueries")
    def data_queries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDataQueryArgs]]]]:
        
        ...
    
    @data_queries.setter
    def data_queries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDataQueryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfigurations")
    def destination_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationArgs]]]]:
        
        ...
    
    @destination_configurations.setter
    def destination_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportArn")
    def export_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @export_arn.setter
    def export_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshCadences")
    def refresh_cadences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportRefreshCadenceArgs]]]]:
        
        ...
    
    @refresh_cadences.setter
    def refresh_cadences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportRefreshCadenceArgs]]]]): # -> None:
        ...
    


class ExportExportDataQueryArgsDict(TypedDict):
    query_statement: pulumi.Input[_builtins.str]
    table_configurations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]


@pulumi.input_type
class ExportExportDataQueryArgs:
    def __init__(__self__, *, query_statement: pulumi.Input[_builtins.str], table_configurations: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStatement")
    def query_statement(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query_statement.setter
    def query_statement(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableConfigurations")
    def table_configurations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]:
        
        ...
    
    @table_configurations.setter
    def table_configurations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]): # -> None:
        ...
    


class ExportExportDestinationConfigurationArgsDict(TypedDict):
    s3_destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationArgsDict]]]]


@pulumi.input_type
class ExportExportDestinationConfigurationArgs:
    def __init__(__self__, *, s3_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Destinations")
    def s3_destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationArgs]]]]:
        
        ...
    
    @s3_destinations.setter
    def s3_destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationArgs]]]]): # -> None:
        ...
    


class ExportExportDestinationConfigurationS3DestinationArgsDict(TypedDict):
    s3_bucket: pulumi.Input[_builtins.str]
    s3_prefix: pulumi.Input[_builtins.str]
    s3_region: pulumi.Input[_builtins.str]
    s3_output_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationS3OutputConfigurationArgsDict]]]]


@pulumi.input_type
class ExportExportDestinationConfigurationS3DestinationArgs:
    def __init__(__self__, *, s3_bucket: pulumi.Input[_builtins.str], s3_prefix: pulumi.Input[_builtins.str], s3_region: pulumi.Input[_builtins.str], s3_output_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationS3OutputConfigurationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_prefix.setter
    def s3_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_region.setter
    def s3_region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputConfigurations")
    def s3_output_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationS3OutputConfigurationArgs]]]]:
        
        ...
    
    @s3_output_configurations.setter
    def s3_output_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExportExportDestinationConfigurationS3DestinationS3OutputConfigurationArgs]]]]): # -> None:
        ...
    


class ExportExportDestinationConfigurationS3DestinationS3OutputConfigurationArgsDict(TypedDict):
    compression: pulumi.Input[_builtins.str]
    format: pulumi.Input[_builtins.str]
    output_type: pulumi.Input[_builtins.str]
    overwrite: pulumi.Input[_builtins.str]


@pulumi.input_type
class ExportExportDestinationConfigurationS3DestinationS3OutputConfigurationArgs:
    def __init__(__self__, *, compression: pulumi.Input[_builtins.str], format: pulumi.Input[_builtins.str], output_type: pulumi.Input[_builtins.str], overwrite: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @compression.setter
    def compression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @output_type.setter
    def output_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def overwrite(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @overwrite.setter
    def overwrite(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ExportExportRefreshCadenceArgsDict(TypedDict):
    frequency: pulumi.Input[_builtins.str]


@pulumi.input_type
class ExportExportRefreshCadenceArgs:
    def __init__(__self__, *, frequency: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ExportTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ExportTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


