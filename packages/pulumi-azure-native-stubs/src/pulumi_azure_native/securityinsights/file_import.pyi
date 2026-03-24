

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FileImportArgs', 'FileImport']
@pulumi.input_type
class FileImportArgs:
    def __init__(__self__, *, content_type: pulumi.Input[Union[_builtins.str, FileImportContentType]], import_file: pulumi.Input[FileMetadataArgs], ingestion_mode: pulumi.Input[Union[_builtins.str, IngestionMode]], resource_group_name: pulumi.Input[_builtins.str], source: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], file_import_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[Union[_builtins.str, FileImportContentType]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: pulumi.Input[Union[_builtins.str, FileImportContentType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importFile")
    def import_file(self) -> pulumi.Input[FileMetadataArgs]:
        
        ...
    
    @import_file.setter
    def import_file(self, value: pulumi.Input[FileMetadataArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> pulumi.Input[Union[_builtins.str, IngestionMode]]:
        
        ...
    
    @ingestion_mode.setter
    def ingestion_mode(self, value: pulumi.Input[Union[_builtins.str, IngestionMode]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileImportId")
    def file_import_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_import_id.setter
    def file_import_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:FileImport")
class FileImport(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., content_type: Optional[pulumi.Input[Union[_builtins.str, FileImportContentType]]] = ..., file_import_id: Optional[pulumi.Input[_builtins.str]] = ..., import_file: Optional[pulumi.Input[Union[FileMetadataArgs, FileMetadataArgsDict]]] = ..., ingestion_mode: Optional[pulumi.Input[Union[_builtins.str, IngestionMode]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FileImportArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> FileImport:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimeUTC")
    def created_time_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorFile")
    def error_file(self) -> pulumi.Output[outputs.FileMetadataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorsPreview")
    def errors_preview(self) -> pulumi.Output[Sequence[outputs.ValidationErrorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesValidUntilTimeUTC")
    def files_valid_until_time_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importFile")
    def import_file(self) -> pulumi.Output[outputs.FileMetadataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importValidUntilTimeUTC")
    def import_valid_until_time_utc(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestedRecordCount")
    def ingested_record_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalRecordCount")
    def total_record_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validRecordCount")
    def valid_record_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


