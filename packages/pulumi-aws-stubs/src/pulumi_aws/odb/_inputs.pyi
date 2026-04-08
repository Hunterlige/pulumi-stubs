import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CloudAutonomousVmClusterMaintenanceWindowArgs",
    "CloudAutonomousVmClusterMaintenanceWindowArgsDict",
    ...,
    ...,
    "CloudAutonomousVmClusterMaintenanceWindowMonthArgs",
    ...,
    "CloudAutonomousVmClusterTimeoutsArgs",
    "CloudAutonomousVmClusterTimeoutsArgsDict",
    ...,
    ...,
    "CloudExadataInfrastructureMaintenanceWindowArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "CloudExadataInfrastructureTimeoutsArgs",
    "CloudExadataInfrastructureTimeoutsArgsDict",
    "CloudVmClusterDataCollectionOptionsArgs",
    "CloudVmClusterDataCollectionOptionsArgsDict",
    "CloudVmClusterIormConfigCacheArgs",
    "CloudVmClusterIormConfigCacheArgsDict",
    "CloudVmClusterIormConfigCacheDbPlanArgs",
    "CloudVmClusterIormConfigCacheDbPlanArgsDict",
    "CloudVmClusterTimeoutsArgs",
    "CloudVmClusterTimeoutsArgsDict",
    "NetworkManagedServiceArgs",
    "NetworkManagedServiceArgsDict",
    "NetworkManagedServiceKmsAccessArgs",
    "NetworkManagedServiceKmsAccessArgsDict",
    "NetworkManagedServiceManagedS3BackupAccessArgs",
    "NetworkManagedServiceManagedS3BackupAccessArgsDict",
    "NetworkManagedServiceS3AccessArgs",
    "NetworkManagedServiceS3AccessArgsDict",
    "NetworkManagedServiceServiceNetworkEndpointArgs",
    ...,
    "NetworkManagedServiceStsAccessArgs",
    "NetworkManagedServiceStsAccessArgsDict",
    "NetworkManagedServiceZeroEtlAccessArgs",
    "NetworkManagedServiceZeroEtlAccessArgsDict",
    "NetworkOciDnsForwardingConfigArgs",
    "NetworkOciDnsForwardingConfigArgsDict",
    "NetworkPeeringConnectionTimeoutsArgs",
    "NetworkPeeringConnectionTimeoutsArgsDict",
    "NetworkTimeoutsArgs",
    "NetworkTimeoutsArgsDict",
]

class CloudAutonomousVmClusterMaintenanceWindowArgsDict(TypedDict):
    preference: pulumi.Input[_builtins.str]
    days_of_weeks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CloudAutonomousVmClusterMaintenanceWindowDaysOfWeekArgsDict
                ]
            ]
        ]
    ]
    hours_of_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    lead_time_in_weeks: NotRequired[pulumi.Input[_builtins.int]]
    months: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowMonthArgsDict]
            ]
        ]
    ]
    weeks_of_months: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class CloudAutonomousVmClusterMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        preference: pulumi.Input[_builtins.str],
        days_of_weeks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudAutonomousVmClusterMaintenanceWindowDaysOfWeekArgs
                    ]
                ]
            ]
        ] = ...,
        hours_of_days: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        lead_time_in_weeks: Optional[pulumi.Input[_builtins.int]] = ...,
        months: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowMonthArgs]
                ]
            ]
        ] = ...,
        weeks_of_months: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> pulumi.Input[_builtins.str]: ...
    @preference.setter
    def preference(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowDaysOfWeekArgs]
            ]
        ]
    ]: ...
    @days_of_weeks.setter
    def days_of_weeks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudAutonomousVmClusterMaintenanceWindowDaysOfWeekArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @hours_of_days.setter
    def hours_of_days(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="leadTimeInWeeks")
    def lead_time_in_weeks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @lead_time_in_weeks.setter
    def lead_time_in_weeks(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowMonthArgs]]
        ]
    ]: ...
    @months.setter
    def months(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowMonthArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @weeks_of_months.setter
    def weeks_of_months(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CloudAutonomousVmClusterMaintenanceWindowDaysOfWeekArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudAutonomousVmClusterMaintenanceWindowDaysOfWeekArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class CloudAutonomousVmClusterMaintenanceWindowMonthArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudAutonomousVmClusterMaintenanceWindowMonthArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class CloudAutonomousVmClusterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudAutonomousVmClusterTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudExadataInfrastructureCustomerContactsToSendToOciArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudExadataInfrastructureCustomerContactsToSendToOciArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...

class CloudExadataInfrastructureMaintenanceWindowArgsDict(TypedDict):
    custom_action_timeout_in_mins: pulumi.Input[_builtins.int]
    is_custom_action_timeout_enabled: pulumi.Input[_builtins.bool]
    patching_mode: pulumi.Input[_builtins.str]
    preference: pulumi.Input[_builtins.str]
    days_of_weeks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CloudExadataInfrastructureMaintenanceWindowDaysOfWeekArgsDict
                ]
            ]
        ]
    ]
    hours_of_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    lead_time_in_weeks: NotRequired[pulumi.Input[_builtins.int]]
    months: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[CloudExadataInfrastructureMaintenanceWindowMonthArgsDict]
            ]
        ]
    ]
    weeks_of_months: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class CloudExadataInfrastructureMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        custom_action_timeout_in_mins: pulumi.Input[_builtins.int],
        is_custom_action_timeout_enabled: pulumi.Input[_builtins.bool],
        patching_mode: pulumi.Input[_builtins.str],
        preference: pulumi.Input[_builtins.str],
        days_of_weeks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudExadataInfrastructureMaintenanceWindowDaysOfWeekArgs
                    ]
                ]
            ]
        ] = ...,
        hours_of_days: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        lead_time_in_weeks: Optional[pulumi.Input[_builtins.int]] = ...,
        months: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CloudExadataInfrastructureMaintenanceWindowMonthArgs]
                ]
            ]
        ] = ...,
        weeks_of_months: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customActionTimeoutInMins")
    def custom_action_timeout_in_mins(self) -> pulumi.Input[_builtins.int]: ...
    @custom_action_timeout_in_mins.setter
    def custom_action_timeout_in_mins(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="isCustomActionTimeoutEnabled")
    def is_custom_action_timeout_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_custom_action_timeout_enabled.setter
    def is_custom_action_timeout_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> pulumi.Input[_builtins.str]: ...
    @patching_mode.setter
    def patching_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> pulumi.Input[_builtins.str]: ...
    @preference.setter
    def preference(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CloudExadataInfrastructureMaintenanceWindowDaysOfWeekArgs]
            ]
        ]
    ]: ...
    @days_of_weeks.setter
    def days_of_weeks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudExadataInfrastructureMaintenanceWindowDaysOfWeekArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @hours_of_days.setter
    def hours_of_days(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="leadTimeInWeeks")
    def lead_time_in_weeks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @lead_time_in_weeks.setter
    def lead_time_in_weeks(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[CloudExadataInfrastructureMaintenanceWindowMonthArgs]]
        ]
    ]: ...
    @months.setter
    def months(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[CloudExadataInfrastructureMaintenanceWindowMonthArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @weeks_of_months.setter
    def weeks_of_months(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CloudExadataInfrastructureMaintenanceWindowDaysOfWeekArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudExadataInfrastructureMaintenanceWindowDaysOfWeekArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class CloudExadataInfrastructureMaintenanceWindowMonthArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudExadataInfrastructureMaintenanceWindowMonthArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class CloudExadataInfrastructureTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudExadataInfrastructureTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudVmClusterDataCollectionOptionsArgsDict(TypedDict):
    is_diagnostics_events_enabled: pulumi.Input[_builtins.bool]
    is_health_monitoring_enabled: pulumi.Input[_builtins.bool]
    is_incident_logs_enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class CloudVmClusterDataCollectionOptionsArgs:
    def __init__(
        __self__,
        *,
        is_diagnostics_events_enabled: pulumi.Input[_builtins.bool],
        is_health_monitoring_enabled: pulumi.Input[_builtins.bool],
        is_incident_logs_enabled: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDiagnosticsEventsEnabled")
    def is_diagnostics_events_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_diagnostics_events_enabled.setter
    def is_diagnostics_events_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="isHealthMonitoringEnabled")
    def is_health_monitoring_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_health_monitoring_enabled.setter
    def is_health_monitoring_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="isIncidentLogsEnabled")
    def is_incident_logs_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_incident_logs_enabled.setter
    def is_incident_logs_enabled(self, value: pulumi.Input[_builtins.bool]): ...

class CloudVmClusterIormConfigCacheArgsDict(TypedDict):
    db_plans: pulumi.Input[
        Sequence[pulumi.Input[CloudVmClusterIormConfigCacheDbPlanArgsDict]]
    ]
    lifecycle_details: pulumi.Input[_builtins.str]
    lifecycle_state: pulumi.Input[_builtins.str]
    objective: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudVmClusterIormConfigCacheArgs:
    def __init__(
        __self__,
        *,
        db_plans: pulumi.Input[
            Sequence[pulumi.Input[CloudVmClusterIormConfigCacheDbPlanArgs]]
        ],
        lifecycle_details: pulumi.Input[_builtins.str],
        lifecycle_state: pulumi.Input[_builtins.str],
        objective: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbPlans")
    def db_plans(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[CloudVmClusterIormConfigCacheDbPlanArgs]]
    ]: ...
    @db_plans.setter
    def db_plans(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[CloudVmClusterIormConfigCacheDbPlanArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Input[_builtins.str]: ...
    @lifecycle_details.setter
    def lifecycle_details(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> pulumi.Input[_builtins.str]: ...
    @lifecycle_state.setter
    def lifecycle_state(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def objective(self) -> pulumi.Input[_builtins.str]: ...
    @objective.setter
    def objective(self, value: pulumi.Input[_builtins.str]): ...

class CloudVmClusterIormConfigCacheDbPlanArgsDict(TypedDict):
    db_name: pulumi.Input[_builtins.str]
    flash_cache_limit: pulumi.Input[_builtins.str]
    share: pulumi.Input[_builtins.int]

@pulumi.input_type
class CloudVmClusterIormConfigCacheDbPlanArgs:
    def __init__(
        __self__,
        *,
        db_name: pulumi.Input[_builtins.str],
        flash_cache_limit: pulumi.Input[_builtins.str],
        share: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> pulumi.Input[_builtins.str]: ...
    @db_name.setter
    def db_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="flashCacheLimit")
    def flash_cache_limit(self) -> pulumi.Input[_builtins.str]: ...
    @flash_cache_limit.setter
    def flash_cache_limit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def share(self) -> pulumi.Input[_builtins.int]: ...
    @share.setter
    def share(self, value: pulumi.Input[_builtins.int]): ...

class CloudVmClusterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudVmClusterTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkManagedServiceArgsDict(TypedDict):
    kms_accesses: pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceKmsAccessArgsDict]]
    ]
    managed_s3_backup_accesses: pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceManagedS3BackupAccessArgsDict]]
    ]
    managed_service_ipv4_cidrs: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    resource_gateway_arn: pulumi.Input[_builtins.str]
    s3_accesses: pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceS3AccessArgsDict]]
    ]
    service_network_arn: pulumi.Input[_builtins.str]
    service_network_endpoints: pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceServiceNetworkEndpointArgsDict]]
    ]
    sts_accesses: pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceStsAccessArgsDict]]
    ]
    zero_etl_accesses: pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceZeroEtlAccessArgsDict]]
    ]

@pulumi.input_type
class NetworkManagedServiceArgs:
    def __init__(
        __self__,
        *,
        kms_accesses: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceKmsAccessArgs]]
        ],
        managed_s3_backup_accesses: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceManagedS3BackupAccessArgs]]
        ],
        managed_service_ipv4_cidrs: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        resource_gateway_arn: pulumi.Input[_builtins.str],
        s3_accesses: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceS3AccessArgs]]
        ],
        service_network_arn: pulumi.Input[_builtins.str],
        service_network_endpoints: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceServiceNetworkEndpointArgs]]
        ],
        sts_accesses: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceStsAccessArgs]]
        ],
        zero_etl_accesses: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceZeroEtlAccessArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsAccesses")
    def kms_accesses(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceKmsAccessArgs]]]: ...
    @kms_accesses.setter
    def kms_accesses(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceKmsAccessArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedS3BackupAccesses")
    def managed_s3_backup_accesses(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceManagedS3BackupAccessArgs]]
    ]: ...
    @managed_s3_backup_accesses.setter
    def managed_s3_backup_accesses(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceManagedS3BackupAccessArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedServiceIpv4Cidrs")
    def managed_service_ipv4_cidrs(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @managed_service_ipv4_cidrs.setter
    def managed_service_ipv4_cidrs(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGatewayArn")
    def resource_gateway_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_gateway_arn.setter
    def resource_gateway_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Accesses")
    def s3_accesses(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceS3AccessArgs]]]: ...
    @s3_accesses.setter
    def s3_accesses(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceS3AccessArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> pulumi.Input[_builtins.str]: ...
    @service_network_arn.setter
    def service_network_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkEndpoints")
    def service_network_endpoints(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceServiceNetworkEndpointArgs]]
    ]: ...
    @service_network_endpoints.setter
    def service_network_endpoints(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceServiceNetworkEndpointArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stsAccesses")
    def sts_accesses(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceStsAccessArgs]]]: ...
    @sts_accesses.setter
    def sts_accesses(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[NetworkManagedServiceStsAccessArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="zeroEtlAccesses")
    def zero_etl_accesses(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[NetworkManagedServiceZeroEtlAccessArgs]]
    ]: ...
    @zero_etl_accesses.setter
    def zero_etl_accesses(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[NetworkManagedServiceZeroEtlAccessArgs]]
        ],
    ): ...

class NetworkManagedServiceKmsAccessArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    kms_policy_document: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]

@pulumi.input_type
class NetworkManagedServiceKmsAccessArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        kms_policy_document: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ipv4_addresses.setter
    def ipv4_addresses(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsPolicyDocument")
    def kms_policy_document(self) -> pulumi.Input[_builtins.str]: ...
    @kms_policy_document.setter
    def kms_policy_document(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class NetworkManagedServiceManagedS3BackupAccessArgsDict(TypedDict):
    ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    status: pulumi.Input[_builtins.str]

@pulumi.input_type
class NetworkManagedServiceManagedS3BackupAccessArgs:
    def __init__(
        __self__,
        *,
        ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        status: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ipv4_addresses.setter
    def ipv4_addresses(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class NetworkManagedServiceS3AccessArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    s3_policy_document: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]

@pulumi.input_type
class NetworkManagedServiceS3AccessArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        s3_policy_document: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ipv4_addresses.setter
    def ipv4_addresses(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3PolicyDocument")
    def s3_policy_document(self) -> pulumi.Input[_builtins.str]: ...
    @s3_policy_document.setter
    def s3_policy_document(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class NetworkManagedServiceServiceNetworkEndpointArgsDict(TypedDict):
    vpc_endpoint_id: pulumi.Input[_builtins.str]
    vpc_endpoint_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class NetworkManagedServiceServiceNetworkEndpointArgs:
    def __init__(
        __self__,
        *,
        vpc_endpoint_id: pulumi.Input[_builtins.str],
        vpc_endpoint_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointType")
    def vpc_endpoint_type(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_endpoint_type.setter
    def vpc_endpoint_type(self, value: pulumi.Input[_builtins.str]): ...

class NetworkManagedServiceStsAccessArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    status: pulumi.Input[_builtins.str]
    sts_policy_document: pulumi.Input[_builtins.str]

@pulumi.input_type
class NetworkManagedServiceStsAccessArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        ipv4_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        status: pulumi.Input[_builtins.str],
        sts_policy_document: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ipv4_addresses.setter
    def ipv4_addresses(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="stsPolicyDocument")
    def sts_policy_document(self) -> pulumi.Input[_builtins.str]: ...
    @sts_policy_document.setter
    def sts_policy_document(self, value: pulumi.Input[_builtins.str]): ...

class NetworkManagedServiceZeroEtlAccessArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]

@pulumi.input_type
class NetworkManagedServiceZeroEtlAccessArgs:
    def __init__(
        __self__,
        *,
        cidr: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class NetworkOciDnsForwardingConfigArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    oci_dns_listener_ip: pulumi.Input[_builtins.str]

@pulumi.input_type
class NetworkOciDnsForwardingConfigArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        oci_dns_listener_ip: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ociDnsListenerIp")
    def oci_dns_listener_ip(self) -> pulumi.Input[_builtins.str]: ...
    @oci_dns_listener_ip.setter
    def oci_dns_listener_ip(self, value: pulumi.Input[_builtins.str]): ...

class NetworkPeeringConnectionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkPeeringConnectionTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...
