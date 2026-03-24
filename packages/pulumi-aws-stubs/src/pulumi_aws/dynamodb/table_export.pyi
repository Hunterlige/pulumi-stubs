

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TableExportArgs', 'TableExport']
@pulumi.input_type
class TableExportArgs:
    def __init__(__self__, *, s3_bucket: pulumi.Input[_builtins.str], table_arn: pulumi.Input[_builtins.str], export_format: Optional[pulumi.Input[_builtins.str]] = ..., export_time: Optional[pulumi.Input[_builtins.str]] = ..., export_type: Optional[pulumi.Input[_builtins.str]] = ..., incremental_export_specification: Optional[pulumi.Input[TableExportIncrementalExportSpecificationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_arn.setter
    def table_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportFormat")
    def export_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_format.setter
    def export_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportTime")
    def export_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_time.setter
    def export_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportType")
    def export_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_type.setter
    def export_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalExportSpecification")
    def incremental_export_specification(self) -> Optional[pulumi.Input[TableExportIncrementalExportSpecificationArgs]]:
        ...
    
    @incremental_export_specification.setter
    def incremental_export_specification(self, value: Optional[pulumi.Input[TableExportIncrementalExportSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketOwner")
    def s3_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket_owner.setter
    def s3_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_prefix.setter
    def s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3SseAlgorithm")
    def s3_sse_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_sse_algorithm.setter
    def s3_sse_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3SseKmsKeyId")
    def s3_sse_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_sse_kms_key_id.setter
    def s3_sse_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TableExportState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., billed_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., export_format: Optional[pulumi.Input[_builtins.str]] = ..., export_status: Optional[pulumi.Input[_builtins.str]] = ..., export_time: Optional[pulumi.Input[_builtins.str]] = ..., export_type: Optional[pulumi.Input[_builtins.str]] = ..., incremental_export_specification: Optional[pulumi.Input[TableExportIncrementalExportSpecificationArgs]] = ..., item_count: Optional[pulumi.Input[_builtins.int]] = ..., manifest_files_s3_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., table_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billedSizeInBytes")
    def billed_size_in_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @billed_size_in_bytes.setter
    def billed_size_in_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportFormat")
    def export_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_format.setter
    def export_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportStatus")
    def export_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_status.setter
    def export_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportTime")
    def export_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_time.setter
    def export_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportType")
    def export_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_type.setter
    def export_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalExportSpecification")
    def incremental_export_specification(self) -> Optional[pulumi.Input[TableExportIncrementalExportSpecificationArgs]]:
        ...
    
    @incremental_export_specification.setter
    def incremental_export_specification(self, value: Optional[pulumi.Input[TableExportIncrementalExportSpecificationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemCount")
    def item_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @item_count.setter
    def item_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestFilesS3Key")
    def manifest_files_s3_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @manifest_files_s3_key.setter
    def manifest_files_s3_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketOwner")
    def s3_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket_owner.setter
    def s3_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_prefix.setter
    def s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3SseAlgorithm")
    def s3_sse_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_sse_algorithm.setter
    def s3_sse_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3SseKmsKeyId")
    def s3_sse_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_sse_kms_key_id.setter
    def s3_sse_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_arn.setter
    def table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:dynamodb/tableExport:TableExport")
class TableExport(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., export_format: Optional[pulumi.Input[_builtins.str]] = ..., export_time: Optional[pulumi.Input[_builtins.str]] = ..., export_type: Optional[pulumi.Input[_builtins.str]] = ..., incremental_export_specification: Optional[pulumi.Input[Union[TableExportIncrementalExportSpecificationArgs, TableExportIncrementalExportSpecificationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., table_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TableExportArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., billed_size_in_bytes: Optional[pulumi.Input[_builtins.int]] = ..., end_time: Optional[pulumi.Input[_builtins.str]] = ..., export_format: Optional[pulumi.Input[_builtins.str]] = ..., export_status: Optional[pulumi.Input[_builtins.str]] = ..., export_time: Optional[pulumi.Input[_builtins.str]] = ..., export_type: Optional[pulumi.Input[_builtins.str]] = ..., incremental_export_specification: Optional[pulumi.Input[Union[TableExportIncrementalExportSpecificationArgs, TableExportIncrementalExportSpecificationArgsDict]]] = ..., item_count: Optional[pulumi.Input[_builtins.int]] = ..., manifest_files_s3_key: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., s3_sse_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., table_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> TableExport:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billedSizeInBytes")
    def billed_size_in_bytes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportFormat")
    def export_format(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportStatus")
    def export_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportTime")
    def export_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportType")
    def export_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalExportSpecification")
    def incremental_export_specification(self) -> pulumi.Output[Optional[outputs.TableExportIncrementalExportSpecification]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="itemCount")
    def item_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestFilesS3Key")
    def manifest_files_s3_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketOwner")
    def s3_bucket_owner(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3SseAlgorithm")
    def s3_sse_algorithm(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3SseKmsKeyId")
    def s3_sse_kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


