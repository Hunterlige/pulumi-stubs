import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DatabaseIdentityArgs",
    "DatabaseIdentityArgsDict",
    ...,
    ...,
    "DistributedAvailabilityGroupDatabaseArgs",
    "DistributedAvailabilityGroupDatabaseArgsDict",
    "ElasticPoolPerDatabaseSettingsArgs",
    "ElasticPoolPerDatabaseSettingsArgsDict",
    "FailoverGroupReadOnlyEndpointArgs",
    "FailoverGroupReadOnlyEndpointArgsDict",
    "FailoverGroupReadWriteEndpointArgs",
    "FailoverGroupReadWriteEndpointArgsDict",
    "InstanceFailoverGroupReadOnlyEndpointArgs",
    "InstanceFailoverGroupReadOnlyEndpointArgsDict",
    "InstanceFailoverGroupReadWriteEndpointArgs",
    "InstanceFailoverGroupReadWriteEndpointArgsDict",
    "JobAgentIdentityArgs",
    "JobAgentIdentityArgsDict",
    "JobScheduleArgs",
    "JobScheduleArgsDict",
    "JobStepActionArgs",
    "JobStepActionArgsDict",
    "JobStepExecutionOptionsArgs",
    "JobStepExecutionOptionsArgsDict",
    "JobStepOutputArgs",
    "JobStepOutputArgsDict",
    "JobTargetArgs",
    "JobTargetArgsDict",
    "ManagedInstanceExternalAdministratorArgs",
    "ManagedInstanceExternalAdministratorArgsDict",
    "ManagedInstancePairInfoArgs",
    "ManagedInstancePairInfoArgsDict",
    "ManagedInstancePrivateEndpointPropertyArgs",
    "ManagedInstancePrivateEndpointPropertyArgsDict",
    ...,
    ...,
    "PartnerInfoArgs",
    "PartnerInfoArgsDict",
    "PartnerRegionInfoArgs",
    "PartnerRegionInfoArgsDict",
    "PrivateEndpointPropertyArgs",
    "PrivateEndpointPropertyArgsDict",
    "PrivateLinkServiceConnectionStatePropertyArgs",
    "PrivateLinkServiceConnectionStatePropertyArgsDict",
    "ResourceIdentityArgs",
    "ResourceIdentityArgsDict",
    "ScheduleItemArgs",
    "ScheduleItemArgsDict",
    "ServerExternalAdministratorArgs",
    "ServerExternalAdministratorArgsDict",
    "ServerInfoArgs",
    "ServerInfoArgsDict",
    "ServicePrincipalArgs",
    "ServicePrincipalArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SyncGroupSchemaTableColumnArgs",
    "SyncGroupSchemaTableColumnArgsDict",
    "SyncGroupSchemaTableArgs",
    "SyncGroupSchemaTableArgsDict",
    "SyncGroupSchemaArgs",
    "SyncGroupSchemaArgsDict",
    ...,
    ...,
]

class DatabaseIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, DatabaseIdentityType]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DatabaseIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, DatabaseIdentityType]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DatabaseIdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DatabaseIdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DatabaseVulnerabilityAssessmentRuleBaselineItemArgsDict(TypedDict):
    result: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DatabaseVulnerabilityAssessmentRuleBaselineItemArgs:
    def __init__(
        __self__, *, result: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @result.setter
    def result(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class DistributedAvailabilityGroupDatabaseArgsDict(TypedDict):
    database_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DistributedAvailabilityGroupDatabaseArgs:
    def __init__(
        __self__, *, database_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ElasticPoolPerDatabaseSettingsArgsDict(TypedDict):
    auto_pause_delay: NotRequired[pulumi.Input[_builtins.int]]
    max_capacity: NotRequired[pulumi.Input[_builtins.float]]
    min_capacity: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ElasticPoolPerDatabaseSettingsArgs:
    def __init__(
        __self__,
        *,
        auto_pause_delay: Optional[pulumi.Input[_builtins.int]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
        min_capacity: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoPauseDelay")
    def auto_pause_delay(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @auto_pause_delay.setter
    def auto_pause_delay(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_capacity.setter
    def min_capacity(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class FailoverGroupReadOnlyEndpointArgsDict(TypedDict):
    failover_policy: NotRequired[
        pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
    ]
    target_server: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FailoverGroupReadOnlyEndpointArgs:
    def __init__(
        __self__,
        *,
        failover_policy: Optional[
            pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
        ] = ...,
        target_server: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
    ]: ...
    @failover_policy.setter
    def failover_policy(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetServer")
    def target_server(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_server.setter
    def target_server(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FailoverGroupReadWriteEndpointArgsDict(TypedDict):
    failover_policy: pulumi.Input[Union[_builtins.str, ReadWriteEndpointFailoverPolicy]]
    failover_with_data_loss_grace_period_minutes: NotRequired[
        pulumi.Input[_builtins.int]
    ]

@pulumi.input_type
class FailoverGroupReadWriteEndpointArgs:
    def __init__(
        __self__,
        *,
        failover_policy: pulumi.Input[
            Union[_builtins.str, ReadWriteEndpointFailoverPolicy]
        ],
        failover_with_data_loss_grace_period_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ReadWriteEndpointFailoverPolicy]]: ...
    @failover_policy.setter
    def failover_policy(
        self, value: pulumi.Input[Union[_builtins.str, ReadWriteEndpointFailoverPolicy]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverWithDataLossGracePeriodMinutes")
    def failover_with_data_loss_grace_period_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failover_with_data_loss_grace_period_minutes.setter
    def failover_with_data_loss_grace_period_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class InstanceFailoverGroupReadOnlyEndpointArgsDict(TypedDict):
    failover_policy: NotRequired[
        pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
    ]

@pulumi.input_type
class InstanceFailoverGroupReadOnlyEndpointArgs:
    def __init__(
        __self__,
        *,
        failover_policy: Optional[
            pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
    ]: ...
    @failover_policy.setter
    def failover_policy(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ReadOnlyEndpointFailoverPolicy]]
        ],
    ): ...

class InstanceFailoverGroupReadWriteEndpointArgsDict(TypedDict):
    failover_policy: pulumi.Input[Union[_builtins.str, ReadWriteEndpointFailoverPolicy]]
    failover_with_data_loss_grace_period_minutes: NotRequired[
        pulumi.Input[_builtins.int]
    ]

@pulumi.input_type
class InstanceFailoverGroupReadWriteEndpointArgs:
    def __init__(
        __self__,
        *,
        failover_policy: pulumi.Input[
            Union[_builtins.str, ReadWriteEndpointFailoverPolicy]
        ],
        failover_with_data_loss_grace_period_minutes: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ReadWriteEndpointFailoverPolicy]]: ...
    @failover_policy.setter
    def failover_policy(
        self, value: pulumi.Input[Union[_builtins.str, ReadWriteEndpointFailoverPolicy]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failoverWithDataLossGracePeriodMinutes")
    def failover_with_data_loss_grace_period_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failover_with_data_loss_grace_period_minutes.setter
    def failover_with_data_loss_grace_period_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class JobAgentIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, JobAgentIdentityType]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class JobAgentIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, JobAgentIdentityType]],
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, JobAgentIdentityType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, JobAgentIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class JobScheduleArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    interval: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[JobScheduleType]]

@pulumi.input_type
class JobScheduleArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        interval: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[JobScheduleType]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[JobScheduleType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[JobScheduleType]]): ...

class JobStepActionArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]
    source: NotRequired[pulumi.Input[Union[_builtins.str, JobStepActionSource]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, JobStepActionType]]]

@pulumi.input_type
class JobStepActionArgs:
    def __init__(
        __self__,
        *,
        value: pulumi.Input[_builtins.str],
        source: Optional[pulumi.Input[Union[_builtins.str, JobStepActionSource]]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, JobStepActionType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, JobStepActionSource]]]: ...
    @source.setter
    def source(
        self, value: Optional[pulumi.Input[Union[_builtins.str, JobStepActionSource]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, JobStepActionType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, JobStepActionType]]]
    ): ...

class JobStepExecutionOptionsArgsDict(TypedDict):
    initial_retry_interval_seconds: NotRequired[pulumi.Input[_builtins.int]]
    maximum_retry_interval_seconds: NotRequired[pulumi.Input[_builtins.int]]
    retry_attempts: NotRequired[pulumi.Input[_builtins.int]]
    retry_interval_backoff_multiplier: NotRequired[pulumi.Input[_builtins.float]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class JobStepExecutionOptionsArgs:
    def __init__(
        __self__,
        *,
        initial_retry_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_retry_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        retry_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        retry_interval_backoff_multiplier: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initialRetryIntervalSeconds")
    def initial_retry_interval_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_retry_interval_seconds.setter
    def initial_retry_interval_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryIntervalSeconds")
    def maximum_retry_interval_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_retry_interval_seconds.setter
    def maximum_retry_interval_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retryAttempts")
    def retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_attempts.setter
    def retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="retryIntervalBackoffMultiplier")
    def retry_interval_backoff_multiplier(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @retry_interval_backoff_multiplier.setter
    def retry_interval_backoff_multiplier(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class JobStepOutputArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    server_name: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    credential: NotRequired[pulumi.Input[_builtins.str]]
    resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    schema_name: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, JobStepOutputType]]]

@pulumi.input_type
class JobStepOutputArgs:
    def __init__(
        __self__,
        *,
        database_name: pulumi.Input[_builtins.str],
        server_name: pulumi.Input[_builtins.str],
        table_name: pulumi.Input[_builtins.str],
        credential: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_name: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, JobStepOutputType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]: ...
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]: ...
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def credential(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential.setter
    def credential(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, JobStepOutputType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, JobStepOutputType]]]
    ): ...

class JobTargetArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, JobTargetType]]
    database_name: NotRequired[pulumi.Input[_builtins.str]]
    elastic_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    membership_type: NotRequired[pulumi.Input[JobTargetGroupMembershipType]]
    refresh_credential: NotRequired[pulumi.Input[_builtins.str]]
    server_name: NotRequired[pulumi.Input[_builtins.str]]
    shard_map_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTargetArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, JobTargetType]],
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elastic_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_type: Optional[pulumi.Input[JobTargetGroupMembershipType]] = ...,
        refresh_credential: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        shard_map_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, JobTargetType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, JobTargetType]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticPoolName")
    def elastic_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elastic_pool_name.setter
    def elastic_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipType")
    def membership_type(
        self,
    ) -> Optional[pulumi.Input[JobTargetGroupMembershipType]]: ...
    @membership_type.setter
    def membership_type(
        self, value: Optional[pulumi.Input[JobTargetGroupMembershipType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="refreshCredential")
    def refresh_credential(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_credential.setter
    def refresh_credential(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shardMapName")
    def shard_map_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shard_map_name.setter
    def shard_map_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedInstanceExternalAdministratorArgsDict(TypedDict):
    administrator_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AdministratorType]]
    ]
    azure_ad_only_authentication: NotRequired[pulumi.Input[_builtins.bool]]
    login: NotRequired[pulumi.Input[_builtins.str]]
    principal_type: NotRequired[pulumi.Input[Union[_builtins.str, PrincipalType]]]
    sid: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedInstanceExternalAdministratorArgs:
    def __init__(
        __self__,
        *,
        administrator_type: Optional[
            pulumi.Input[Union[_builtins.str, AdministratorType]]
        ] = ...,
        azure_ad_only_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        login: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalType]]
        ] = ...,
        sid: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AdministratorType]]]: ...
    @administrator_type.setter
    def administrator_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AdministratorType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @azure_ad_only_authentication.setter
    def azure_ad_only_authentication(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login.setter
    def login(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]: ...
    @principal_type.setter
    def principal_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sid.setter
    def sid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedInstancePairInfoArgsDict(TypedDict):
    partner_managed_instance_id: NotRequired[pulumi.Input[_builtins.str]]
    primary_managed_instance_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedInstancePairInfoArgs:
    def __init__(
        __self__,
        *,
        partner_managed_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_managed_instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerManagedInstanceId")
    def partner_managed_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_managed_instance_id.setter
    def partner_managed_instance_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryManagedInstanceId")
    def primary_managed_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_managed_instance_id.setter
    def primary_managed_instance_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ManagedInstancePrivateEndpointPropertyArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedInstancePrivateEndpointPropertyArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedInstancePrivateLinkServiceConnectionStatePropertyArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]

@pulumi.input_type
class ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class PartnerInfoArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class PartnerInfoArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class PartnerRegionInfoArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PartnerRegionInfoArgs:
    def __init__(
        __self__, *, location: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateEndpointPropertyArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointPropertyArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStatePropertyArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    status: pulumi.Input[Union[_builtins.str, PrivateLinkServiceConnectionStateStatus]]

@pulumi.input_type
class PrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        status: pulumi.Input[
            Union[_builtins.str, PrivateLinkServiceConnectionStateStatus]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, PrivateLinkServiceConnectionStateStatus]
    ]: ...
    @status.setter
    def status(
        self,
        value: pulumi.Input[
            Union[_builtins.str, PrivateLinkServiceConnectionStateStatus]
        ],
    ): ...

class ResourceIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ScheduleItemArgsDict(TypedDict):
    start_day: pulumi.Input[Union[_builtins.str, DayOfWeek]]
    start_time: pulumi.Input[_builtins.str]
    stop_day: pulumi.Input[Union[_builtins.str, DayOfWeek]]
    stop_time: pulumi.Input[_builtins.str]

@pulumi.input_type
class ScheduleItemArgs:
    def __init__(
        __self__,
        *,
        start_day: pulumi.Input[Union[_builtins.str, DayOfWeek]],
        start_time: pulumi.Input[_builtins.str],
        stop_day: pulumi.Input[Union[_builtins.str, DayOfWeek]],
        stop_time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startDay")
    def start_day(self) -> pulumi.Input[Union[_builtins.str, DayOfWeek]]: ...
    @start_day.setter
    def start_day(self, value: pulumi.Input[Union[_builtins.str, DayOfWeek]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[_builtins.str]: ...
    @start_time.setter
    def start_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stopDay")
    def stop_day(self) -> pulumi.Input[Union[_builtins.str, DayOfWeek]]: ...
    @stop_day.setter
    def stop_day(self, value: pulumi.Input[Union[_builtins.str, DayOfWeek]]): ...
    @_builtins.property
    @pulumi.getter(name="stopTime")
    def stop_time(self) -> pulumi.Input[_builtins.str]: ...
    @stop_time.setter
    def stop_time(self, value: pulumi.Input[_builtins.str]): ...

class ServerExternalAdministratorArgsDict(TypedDict):
    administrator_type: NotRequired[
        pulumi.Input[Union[_builtins.str, AdministratorType]]
    ]
    azure_ad_only_authentication: NotRequired[pulumi.Input[_builtins.bool]]
    login: NotRequired[pulumi.Input[_builtins.str]]
    principal_type: NotRequired[pulumi.Input[Union[_builtins.str, PrincipalType]]]
    sid: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServerExternalAdministratorArgs:
    def __init__(
        __self__,
        *,
        administrator_type: Optional[
            pulumi.Input[Union[_builtins.str, AdministratorType]]
        ] = ...,
        azure_ad_only_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        login: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalType]]
        ] = ...,
        sid: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AdministratorType]]]: ...
    @administrator_type.setter
    def administrator_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AdministratorType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @azure_ad_only_authentication.setter
    def azure_ad_only_authentication(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @login.setter
    def login(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]: ...
    @principal_type.setter
    def principal_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sid.setter
    def sid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServerInfoArgsDict(TypedDict):
    server_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServerInfoArgs:
    def __init__(__self__, *, server_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[_builtins.str]: ...
    @server_id.setter
    def server_id(self, value: pulumi.Input[_builtins.str]): ...

class ServicePrincipalArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, ServicePrincipalType]]]

@pulumi.input_type
class ServicePrincipalArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, ServicePrincipalType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ServicePrincipalType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ServicePrincipalType]]]
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SyncGroupSchemaTableColumnArgsDict(TypedDict):
    data_size: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    quoted_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SyncGroupSchemaTableColumnArgs:
    def __init__(
        __self__,
        *,
        data_size: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        quoted_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSize")
    def data_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_size.setter
    def data_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quotedName")
    def quoted_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quoted_name.setter
    def quoted_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SyncGroupSchemaTableArgsDict(TypedDict):
    columns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableColumnArgsDict]]]
    ]
    quoted_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SyncGroupSchemaTableArgs:
    def __init__(
        __self__,
        *,
        columns: Optional[
            pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableColumnArgs]]]
        ] = ...,
        quoted_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableColumnArgs]]]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableColumnArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="quotedName")
    def quoted_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quoted_name.setter
    def quoted_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SyncGroupSchemaArgsDict(TypedDict):
    master_sync_member_name: NotRequired[pulumi.Input[_builtins.str]]
    tables: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableArgsDict]]]
    ]

@pulumi.input_type
class SyncGroupSchemaArgs:
    def __init__(
        __self__,
        *,
        master_sync_member_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tables: Optional[
            pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="masterSyncMemberName")
    def master_sync_member_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_sync_member_name.setter
    def master_sync_member_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableArgs]]]]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SyncGroupSchemaTableArgs]]]],
    ): ...

class VulnerabilityAssessmentRecurringScansPropertiesArgsDict(TypedDict):
    email_subscription_admins: NotRequired[pulumi.Input[_builtins.bool]]
    emails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VulnerabilityAssessmentRecurringScansPropertiesArgs:
    def __init__(
        __self__,
        *,
        email_subscription_admins: Optional[pulumi.Input[_builtins.bool]] = ...,
        emails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailSubscriptionAdmins")
    def email_subscription_admins(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @email_subscription_admins.setter
    def email_subscription_admins(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @emails.setter
    def emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
