

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExportTaskArgs', 'ExportTask']
@pulumi.input_type
class ExportTaskArgs:
    def __init__(__self__, *, export_task_identifier: pulumi.Input[_builtins.str], iam_role_arn: pulumi.Input[_builtins.str], kms_key_id: pulumi.Input[_builtins.str], s3_bucket_name: pulumi.Input[_builtins.str], source_arn: pulumi.Input[_builtins.str], export_onlies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ExportTaskTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportTaskIdentifier")
    def export_task_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @export_task_identifier.setter
    def export_task_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_arn.setter
    def source_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportOnlies")
    def export_onlies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_onlies.setter
    def export_onlies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_prefix.setter
    def s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ExportTaskTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ExportTaskTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ExportTaskState:
    def __init__(__self__, *, export_onlies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., export_task_identifier: Optional[pulumi.Input[_builtins.str]] = ..., failure_cause: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., percent_progress: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_time: Optional[pulumi.Input[_builtins.str]] = ..., source_arn: Optional[pulumi.Input[_builtins.str]] = ..., source_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., task_end_time: Optional[pulumi.Input[_builtins.str]] = ..., task_start_time: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ExportTaskTimeoutsArgs]] = ..., warning_message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportOnlies")
    def export_onlies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @export_onlies.setter
    def export_onlies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportTaskIdentifier")
    def export_task_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export_task_identifier.setter
    def export_task_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCause")
    def failure_cause(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @failure_cause.setter
    def failure_cause(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @percent_progress.setter
    def percent_progress(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_prefix.setter
    def s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_time.setter
    def snapshot_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_arn.setter
    def source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskEndTime")
    def task_end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_end_time.setter
    def task_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskStartTime")
    def task_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_start_time.setter
    def task_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ExportTaskTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ExportTaskTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @warning_message.setter
    def warning_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:rds/exportTask:ExportTask")
class ExportTask(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., export_onlies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., export_task_identifier: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., source_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ExportTaskTimeoutsArgs, ExportTaskTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExportTaskArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., export_onlies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., export_task_identifier: Optional[pulumi.Input[_builtins.str]] = ..., failure_cause: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., percent_progress: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., s3_prefix: Optional[pulumi.Input[_builtins.str]] = ..., snapshot_time: Optional[pulumi.Input[_builtins.str]] = ..., source_arn: Optional[pulumi.Input[_builtins.str]] = ..., source_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., task_end_time: Optional[pulumi.Input[_builtins.str]] = ..., task_start_time: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ExportTaskTimeoutsArgs, ExportTaskTimeoutsArgsDict]]] = ..., warning_message: Optional[pulumi.Input[_builtins.str]] = ...) -> ExportTask:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportOnlies")
    def export_onlies(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportTaskIdentifier")
    def export_task_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCause")
    def failure_cause(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskEndTime")
    def task_end_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskStartTime")
    def task_start_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ExportTaskTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


