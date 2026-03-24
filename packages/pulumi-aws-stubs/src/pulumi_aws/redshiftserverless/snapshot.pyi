

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SnapshotArgs', 'Snapshot']
@pulumi.input_type
class SnapshotArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], snapshot_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @snapshot_name.setter
    def snapshot_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
class _SnapshotState:
    def __init__(__self__, *, accounts_with_provisioned_restore_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accounts_with_restore_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., namespace_arn: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountsWithProvisionedRestoreAccesses")
    def accounts_with_provisioned_restore_accesses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts_with_provisioned_restore_accesses.setter
    def accounts_with_provisioned_restore_accesses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountsWithRestoreAccesses")
    def accounts_with_restore_accesses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @accounts_with_restore_accesses.setter
    def accounts_with_restore_accesses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_username.setter
    def admin_username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceArn")
    def namespace_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace_arn.setter
    def namespace_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account.setter
    def owner_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:redshiftserverless/snapshot:Snapshot")
class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SnapshotArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accounts_with_provisioned_restore_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., accounts_with_restore_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., admin_username: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., namespace_arn: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., owner_account: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...) -> Snapshot:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountsWithProvisionedRestoreAccesses")
    def accounts_with_provisioned_restore_accesses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountsWithRestoreAccesses")
    def accounts_with_restore_accesses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceArn")
    def namespace_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


