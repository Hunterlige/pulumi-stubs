

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
__all__ = ['TableBucketReplicationArgs', 'TableBucketReplication']
@pulumi.input_type
class TableBucketReplicationArgs:
    def __init__(__self__, *, role: pulumi.Input[_builtins.str], table_bucket_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[TableBucketReplicationRuleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input[TableBucketReplicationRuleArgs]]:
        
        ...
    
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[TableBucketReplicationRuleArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TableBucketReplicationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[TableBucketReplicationRuleArgs]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., version_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input[TableBucketReplicationRuleArgs]]:
        
        ...
    
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[TableBucketReplicationRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_bucket_arn.setter
    def table_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionToken")
    def version_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @version_token.setter
    def version_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TableBucketReplication(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[Union[TableBucketReplicationRuleArgs, TableBucketReplicationRuleArgsDict]]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TableBucketReplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[Union[TableBucketReplicationRuleArgs, TableBucketReplicationRuleArgsDict]]] = ..., table_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ..., version_token: Optional[pulumi.Input[_builtins.str]] = ...) -> TableBucketReplication:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Output[Optional[outputs.TableBucketReplicationRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionToken")
    def version_token(self) -> pulumi.Output[_builtins.str]:
        ...
    


