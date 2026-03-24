

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceAutomatedBackupsReplicationArgs', 'InstanceAutomatedBackupsReplication']
@pulumi.input_type
class InstanceAutomatedBackupsReplicationArgs:
    def __init__(__self__, *, source_db_instance_arn: pulumi.Input[_builtins.str], kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., pre_signed_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbInstanceArn")
    def source_db_instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_db_instance_arn.setter
    def source_db_instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preSignedUrl")
    def pre_signed_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pre_signed_url.setter
    def pre_signed_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceAutomatedBackupsReplicationState:
    def __init__(__self__, *, kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., pre_signed_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., source_db_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preSignedUrl")
    def pre_signed_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pre_signed_url.setter
    def pre_signed_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbInstanceArn")
    def source_db_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_db_instance_arn.setter
    def source_db_instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InstanceAutomatedBackupsReplication(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., pre_signed_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., source_db_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceAutomatedBackupsReplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., pre_signed_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., source_db_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> InstanceAutomatedBackupsReplication:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preSignedUrl")
    def pre_signed_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbInstanceArn")
    def source_db_instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


