import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExtendedDatabaseBlobAuditingPolicyResult",
    ...,
    "get_extended_database_blob_auditing_policy",
    "get_extended_database_blob_auditing_policy_output",
]

@pulumi.output_type
class GetExtendedDatabaseBlobAuditingPolicyResult:
    def __init__(
        __self__,
        audit_actions_and_groups=...,
        azure_api_version=...,
        id=...,
        is_azure_monitor_target_enabled=...,
        is_managed_identity_in_use=...,
        is_storage_secondary_key_in_use=...,
        name=...,
        predicate_expression=...,
        queue_delay_ms=...,
        retention_days=...,
        state=...,
        storage_account_subscription_id=...,
        storage_endpoint=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditActionsAndGroups")
    def audit_actions_and_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isAzureMonitorTargetEnabled")
    def is_azure_monitor_target_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isManagedIdentityInUse")
    def is_managed_identity_in_use(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isStorageSecondaryKeyInUse")
    def is_storage_secondary_key_in_use(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="predicateExpression")
    def predicate_expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queueDelayMs")
    def queue_delay_ms(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSubscriptionId")
    def storage_account_subscription_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetExtendedDatabaseBlobAuditingPolicyResult(
    GetExtendedDatabaseBlobAuditingPolicyResult
):
    def __await__(self): ...

def get_extended_database_blob_auditing_policy(
    blob_auditing_policy_name: Optional[_builtins.str] = ...,
    database_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExtendedDatabaseBlobAuditingPolicyResult: ...
def get_extended_database_blob_auditing_policy_output(
    blob_auditing_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExtendedDatabaseBlobAuditingPolicyResult]: ...
