

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExtendedDatabaseBlobAuditingPolicyArgs', 'ExtendedDatabaseBlobAuditingPolicy']
@pulumi.input_type
class ExtendedDatabaseBlobAuditingPolicyArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], state: pulumi.Input[BlobAuditingPolicyState], audit_actions_and_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blob_auditing_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., is_azure_monitor_target_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_managed_identity_in_use: Optional[pulumi.Input[_builtins.bool]] = ..., is_storage_secondary_key_in_use: Optional[pulumi.Input[_builtins.bool]] = ..., predicate_expression: Optional[pulumi.Input[_builtins.str]] = ..., queue_delay_ms: Optional[pulumi.Input[_builtins.int]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ..., storage_account_access_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., storage_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[BlobAuditingPolicyState]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[BlobAuditingPolicyState]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditActionsAndGroups")
    def audit_actions_and_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @audit_actions_and_groups.setter
    def audit_actions_and_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobAuditingPolicyName")
    def blob_auditing_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_auditing_policy_name.setter
    def blob_auditing_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAzureMonitorTargetEnabled")
    def is_azure_monitor_target_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_azure_monitor_target_enabled.setter
    def is_azure_monitor_target_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isManagedIdentityInUse")
    def is_managed_identity_in_use(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_managed_identity_in_use.setter
    def is_managed_identity_in_use(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStorageSecondaryKeyInUse")
    def is_storage_secondary_key_in_use(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_storage_secondary_key_in_use.setter
    def is_storage_secondary_key_in_use(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predicateExpression")
    def predicate_expression(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @predicate_expression.setter
    def predicate_expression(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueDelayMs")
    def queue_delay_ms(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @queue_delay_ms.setter
    def queue_delay_ms(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_access_key.setter
    def storage_account_access_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountSubscriptionId")
    def storage_account_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_account_subscription_id.setter
    def storage_account_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ExtendedDatabaseBlobAuditingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., audit_actions_and_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., blob_auditing_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., is_azure_monitor_target_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_managed_identity_in_use: Optional[pulumi.Input[_builtins.bool]] = ..., is_storage_secondary_key_in_use: Optional[pulumi.Input[_builtins.bool]] = ..., predicate_expression: Optional[pulumi.Input[_builtins.str]] = ..., queue_delay_ms: Optional[pulumi.Input[_builtins.int]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[BlobAuditingPolicyState]] = ..., storage_account_access_key: Optional[pulumi.Input[_builtins.str]] = ..., storage_account_subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., storage_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExtendedDatabaseBlobAuditingPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExtendedDatabaseBlobAuditingPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditActionsAndGroups")
    def audit_actions_and_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAzureMonitorTargetEnabled")
    def is_azure_monitor_target_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isManagedIdentityInUse")
    def is_managed_identity_in_use(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStorageSecondaryKeyInUse")
    def is_storage_secondary_key_in_use(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predicateExpression")
    def predicate_expression(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueDelayMs")
    def queue_delay_ms(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountSubscriptionId")
    def storage_account_subscription_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


