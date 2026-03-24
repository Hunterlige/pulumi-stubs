

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TableBucketPolicyArgs', 'TableBucketPolicy']
@pulumi.input_type
class TableBucketPolicyArgs:
    def __init__(__self__, *, resource_policy: pulumi.Input[_builtins.str], table_bucket_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicy")
    def resource_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_policy.setter
    def resource_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_bucket_arn.setter
    def table_bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _TableBucketPolicyState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., resource_policy: Optional[pulumi.Input[_builtins.str]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicy")
    def resource_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_policy.setter
    def resource_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_bucket_arn.setter
    def table_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3tables/tableBucketPolicy:TableBucketPolicy")
class TableBucketPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_policy: Optional[pulumi.Input[_builtins.str]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TableBucketPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_policy: Optional[pulumi.Input[_builtins.str]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> TableBucketPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicy")
    def resource_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


