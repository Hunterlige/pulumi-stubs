

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NamespaceArgs', 'Namespace']
@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *, namespace: pulumi.Input[_builtins.str], table_bucket_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
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
class _NamespaceState:
    def __init__(__self__, *, created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_bucket_arn.setter
    def table_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3tables/namespace:Namespace")
class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NamespaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., created_by: Optional[pulumi.Input[_builtins.str]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> Namespace:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


