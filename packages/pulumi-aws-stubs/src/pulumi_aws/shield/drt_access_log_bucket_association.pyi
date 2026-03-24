

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
__all__ = ['DrtAccessLogBucketAssociationArgs', 'DrtAccessLogBucketAssociation']
@pulumi.input_type
class DrtAccessLogBucketAssociationArgs:
    def __init__(__self__, *, log_bucket: pulumi.Input[_builtins.str], role_arn_association_id: pulumi.Input[_builtins.str], timeouts: Optional[pulumi.Input[DrtAccessLogBucketAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logBucket")
    def log_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_bucket.setter
    def log_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArnAssociationId")
    def role_arn_association_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn_association_id.setter
    def role_arn_association_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DrtAccessLogBucketAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DrtAccessLogBucketAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DrtAccessLogBucketAssociationState:
    def __init__(__self__, *, log_bucket: Optional[pulumi.Input[_builtins.str]] = ..., role_arn_association_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[DrtAccessLogBucketAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logBucket")
    def log_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_bucket.setter
    def log_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArnAssociationId")
    def role_arn_association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn_association_id.setter
    def role_arn_association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[DrtAccessLogBucketAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DrtAccessLogBucketAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DrtAccessLogBucketAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., log_bucket: Optional[pulumi.Input[_builtins.str]] = ..., role_arn_association_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DrtAccessLogBucketAssociationTimeoutsArgs, DrtAccessLogBucketAssociationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DrtAccessLogBucketAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., log_bucket: Optional[pulumi.Input[_builtins.str]] = ..., role_arn_association_id: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DrtAccessLogBucketAssociationTimeoutsArgs, DrtAccessLogBucketAssociationTimeoutsArgsDict]]] = ...) -> DrtAccessLogBucketAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logBucket")
    def log_bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArnAssociationId")
    def role_arn_association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DrtAccessLogBucketAssociationTimeouts]]:
        ...
    


