

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
__all__ = ['BatchOperationsJobArgs', 'BatchOperationsJob']
@pulumi.input_type
class BatchOperationsJobArgs:
    def __init__(__self__, *, bucket_list: Optional[pulumi.Input[BatchOperationsJobBucketListArgs]] = ..., delete_object: Optional[pulumi.Input[BatchOperationsJobDeleteObjectArgs]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., job_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., put_metadata: Optional[pulumi.Input[BatchOperationsJobPutMetadataArgs]] = ..., put_object_hold: Optional[pulumi.Input[BatchOperationsJobPutObjectHoldArgs]] = ..., rewrite_object: Optional[pulumi.Input[BatchOperationsJobRewriteObjectArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketList")
    def bucket_list(self) -> Optional[pulumi.Input[BatchOperationsJobBucketListArgs]]:
        
        ...
    
    @bucket_list.setter
    def bucket_list(self, value: Optional[pulumi.Input[BatchOperationsJobBucketListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObject")
    def delete_object(self) -> Optional[pulumi.Input[BatchOperationsJobDeleteObjectArgs]]:
        
        ...
    
    @delete_object.setter
    def delete_object(self, value: Optional[pulumi.Input[BatchOperationsJobDeleteObjectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtection")
    def delete_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_protection.setter
    def delete_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="putMetadata")
    def put_metadata(self) -> Optional[pulumi.Input[BatchOperationsJobPutMetadataArgs]]:
        
        ...
    
    @put_metadata.setter
    def put_metadata(self, value: Optional[pulumi.Input[BatchOperationsJobPutMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="putObjectHold")
    def put_object_hold(self) -> Optional[pulumi.Input[BatchOperationsJobPutObjectHoldArgs]]:
        
        ...
    
    @put_object_hold.setter
    def put_object_hold(self, value: Optional[pulumi.Input[BatchOperationsJobPutObjectHoldArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rewriteObject")
    def rewrite_object(self) -> Optional[pulumi.Input[BatchOperationsJobRewriteObjectArgs]]:
        
        ...
    
    @rewrite_object.setter
    def rewrite_object(self, value: Optional[pulumi.Input[BatchOperationsJobRewriteObjectArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _BatchOperationsJobState:
    def __init__(__self__, *, bucket_list: Optional[pulumi.Input[BatchOperationsJobBucketListArgs]] = ..., complete_time: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_object: Optional[pulumi.Input[BatchOperationsJobDeleteObjectArgs]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., job_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., put_metadata: Optional[pulumi.Input[BatchOperationsJobPutMetadataArgs]] = ..., put_object_hold: Optional[pulumi.Input[BatchOperationsJobPutObjectHoldArgs]] = ..., rewrite_object: Optional[pulumi.Input[BatchOperationsJobRewriteObjectArgs]] = ..., schedule_time: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketList")
    def bucket_list(self) -> Optional[pulumi.Input[BatchOperationsJobBucketListArgs]]:
        
        ...
    
    @bucket_list.setter
    def bucket_list(self, value: Optional[pulumi.Input[BatchOperationsJobBucketListArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="completeTime")
    def complete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @complete_time.setter
    def complete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObject")
    def delete_object(self) -> Optional[pulumi.Input[BatchOperationsJobDeleteObjectArgs]]:
        
        ...
    
    @delete_object.setter
    def delete_object(self, value: Optional[pulumi.Input[BatchOperationsJobDeleteObjectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtection")
    def delete_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_protection.setter
    def delete_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="putMetadata")
    def put_metadata(self) -> Optional[pulumi.Input[BatchOperationsJobPutMetadataArgs]]:
        
        ...
    
    @put_metadata.setter
    def put_metadata(self, value: Optional[pulumi.Input[BatchOperationsJobPutMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="putObjectHold")
    def put_object_hold(self) -> Optional[pulumi.Input[BatchOperationsJobPutObjectHoldArgs]]:
        
        ...
    
    @put_object_hold.setter
    def put_object_hold(self, value: Optional[pulumi.Input[BatchOperationsJobPutObjectHoldArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rewriteObject")
    def rewrite_object(self) -> Optional[pulumi.Input[BatchOperationsJobRewriteObjectArgs]]:
        
        ...
    
    @rewrite_object.setter
    def rewrite_object(self, value: Optional[pulumi.Input[BatchOperationsJobRewriteObjectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleTime")
    def schedule_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_time.setter
    def schedule_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:storage/batchOperationsJob:BatchOperationsJob")
class BatchOperationsJob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., bucket_list: Optional[pulumi.Input[Union[BatchOperationsJobBucketListArgs, BatchOperationsJobBucketListArgsDict]]] = ..., delete_object: Optional[pulumi.Input[Union[BatchOperationsJobDeleteObjectArgs, BatchOperationsJobDeleteObjectArgsDict]]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., job_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., put_metadata: Optional[pulumi.Input[Union[BatchOperationsJobPutMetadataArgs, BatchOperationsJobPutMetadataArgsDict]]] = ..., put_object_hold: Optional[pulumi.Input[Union[BatchOperationsJobPutObjectHoldArgs, BatchOperationsJobPutObjectHoldArgsDict]]] = ..., rewrite_object: Optional[pulumi.Input[Union[BatchOperationsJobRewriteObjectArgs, BatchOperationsJobRewriteObjectArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[BatchOperationsJobArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., bucket_list: Optional[pulumi.Input[Union[BatchOperationsJobBucketListArgs, BatchOperationsJobBucketListArgsDict]]] = ..., complete_time: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_object: Optional[pulumi.Input[Union[BatchOperationsJobDeleteObjectArgs, BatchOperationsJobDeleteObjectArgsDict]]] = ..., delete_protection: Optional[pulumi.Input[_builtins.bool]] = ..., job_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., put_metadata: Optional[pulumi.Input[Union[BatchOperationsJobPutMetadataArgs, BatchOperationsJobPutMetadataArgsDict]]] = ..., put_object_hold: Optional[pulumi.Input[Union[BatchOperationsJobPutObjectHoldArgs, BatchOperationsJobPutObjectHoldArgsDict]]] = ..., rewrite_object: Optional[pulumi.Input[Union[BatchOperationsJobRewriteObjectArgs, BatchOperationsJobRewriteObjectArgsDict]]] = ..., schedule_time: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> BatchOperationsJob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketList")
    def bucket_list(self) -> pulumi.Output[Optional[outputs.BatchOperationsJobBucketList]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completeTime")
    def complete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObject")
    def delete_object(self) -> pulumi.Output[Optional[outputs.BatchOperationsJobDeleteObject]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteProtection")
    def delete_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="putMetadata")
    def put_metadata(self) -> pulumi.Output[Optional[outputs.BatchOperationsJobPutMetadata]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="putObjectHold")
    def put_object_hold(self) -> pulumi.Output[Optional[outputs.BatchOperationsJobPutObjectHold]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rewriteObject")
    def rewrite_object(self) -> pulumi.Output[Optional[outputs.BatchOperationsJobRewriteObject]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleTime")
    def schedule_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


