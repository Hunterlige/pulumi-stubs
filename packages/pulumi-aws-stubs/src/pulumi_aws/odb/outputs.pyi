import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CloudAutonomousVmClusterMaintenanceWindow",
    ...,
    "CloudAutonomousVmClusterMaintenanceWindowMonth",
    "CloudAutonomousVmClusterTimeouts",
    ...,
    "CloudExadataInfrastructureMaintenanceWindow",
    ...,
    "CloudExadataInfrastructureMaintenanceWindowMonth",
    "CloudExadataInfrastructureTimeouts",
    "CloudVmClusterDataCollectionOptions",
    "CloudVmClusterIormConfigCache",
    "CloudVmClusterIormConfigCacheDbPlan",
    "CloudVmClusterTimeouts",
    "NetworkManagedService",
    "NetworkManagedServiceKmsAccess",
    "NetworkManagedServiceManagedS3BackupAccess",
    "NetworkManagedServiceS3Access",
    "NetworkManagedServiceServiceNetworkEndpoint",
    "NetworkManagedServiceStsAccess",
    "NetworkManagedServiceZeroEtlAccess",
    "NetworkOciDnsForwardingConfig",
    "NetworkPeeringConnectionTimeouts",
    "NetworkTimeouts",
    "GetCloudAutonomousVmClusterMaintenanceWindowResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetCloudVmClusterDataCollectionOptionResult",
    "GetCloudVmClusterIormConfigCacheResult",
    "GetCloudVmClusterIormConfigCacheDbPlanResult",
    "GetCloudVmClustersCloudVmClusterResult",
    "GetDbNodesDbNodeResult",
    "GetDbServerDbServerPatchingDetailResult",
    "GetDbServersDbServerResult",
    "GetDbServersDbServerDbServerPatchingDetailResult",
    "GetDbSystemShapesDbSystemShapeResult",
    "GetGiVersionsGiVersionResult",
    "GetNetworkManagedServiceResult",
    "GetNetworkManagedServiceKmsAccessResult",
    ...,
    "GetNetworkManagedServiceS3AccessResult",
    ...,
    "GetNetworkManagedServiceStsAccessResult",
    "GetNetworkManagedServiceZeroTlAccessResult",
    "GetNetworkOciDnsForwardingConfigResult",
    ...,
    "GetNetworksOdbNetworkResult",
]

@pulumi.output_type
class CloudAutonomousVmClusterMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        preference: _builtins.str,
        days_of_weeks: Optional[
            Sequence[outputs.CloudAutonomousVmClusterMaintenanceWindowDaysOfWeek]
        ] = ...,
        hours_of_days: Optional[Sequence[_builtins.int]] = ...,
        lead_time_in_weeks: Optional[_builtins.int] = ...,
        months: Optional[
            Sequence[outputs.CloudAutonomousVmClusterMaintenanceWindowMonth]
        ] = ...,
        weeks_of_months: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Optional[
        Sequence[outputs.CloudAutonomousVmClusterMaintenanceWindowDaysOfWeek]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="leadTimeInWeeks")
    def lead_time_in_weeks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Optional[Sequence[outputs.CloudAutonomousVmClusterMaintenanceWindowMonth]]: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class CloudAutonomousVmClusterMaintenanceWindowDaysOfWeek(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class CloudAutonomousVmClusterMaintenanceWindowMonth(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class CloudAutonomousVmClusterTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CloudExadataInfrastructureCustomerContactsToSendToOci(dict):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class CloudExadataInfrastructureMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_action_timeout_in_mins: _builtins.int,
        is_custom_action_timeout_enabled: _builtins.bool,
        patching_mode: _builtins.str,
        preference: _builtins.str,
        days_of_weeks: Optional[
            Sequence[outputs.CloudExadataInfrastructureMaintenanceWindowDaysOfWeek]
        ] = ...,
        hours_of_days: Optional[Sequence[_builtins.int]] = ...,
        lead_time_in_weeks: Optional[_builtins.int] = ...,
        months: Optional[
            Sequence[outputs.CloudExadataInfrastructureMaintenanceWindowMonth]
        ] = ...,
        weeks_of_months: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customActionTimeoutInMins")
    def custom_action_timeout_in_mins(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="isCustomActionTimeoutEnabled")
    def is_custom_action_timeout_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Optional[
        Sequence[outputs.CloudExadataInfrastructureMaintenanceWindowDaysOfWeek]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="leadTimeInWeeks")
    def lead_time_in_weeks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Optional[
        Sequence[outputs.CloudExadataInfrastructureMaintenanceWindowMonth]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class CloudExadataInfrastructureMaintenanceWindowDaysOfWeek(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class CloudExadataInfrastructureMaintenanceWindowMonth(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class CloudExadataInfrastructureTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CloudVmClusterDataCollectionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_diagnostics_events_enabled: _builtins.bool,
        is_health_monitoring_enabled: _builtins.bool,
        is_incident_logs_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDiagnosticsEventsEnabled")
    def is_diagnostics_events_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isHealthMonitoringEnabled")
    def is_health_monitoring_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isIncidentLogsEnabled")
    def is_incident_logs_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class CloudVmClusterIormConfigCache(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        db_plans: Sequence[outputs.CloudVmClusterIormConfigCacheDbPlan],
        lifecycle_details: _builtins.str,
        lifecycle_state: _builtins.str,
        objective: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbPlans")
    def db_plans(self) -> Sequence[outputs.CloudVmClusterIormConfigCacheDbPlan]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def objective(self) -> _builtins.str: ...

@pulumi.output_type
class CloudVmClusterIormConfigCacheDbPlan(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        db_name: _builtins.str,
        flash_cache_limit: _builtins.str,
        share: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="flashCacheLimit")
    def flash_cache_limit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def share(self) -> _builtins.int: ...

@pulumi.output_type
class CloudVmClusterTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkManagedService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_accesses: Sequence[outputs.NetworkManagedServiceKmsAccess],
        managed_s3_backup_accesses: Sequence[
            outputs.NetworkManagedServiceManagedS3BackupAccess
        ],
        managed_service_ipv4_cidrs: Sequence[_builtins.str],
        resource_gateway_arn: _builtins.str,
        s3_accesses: Sequence[outputs.NetworkManagedServiceS3Access],
        service_network_arn: _builtins.str,
        service_network_endpoints: Sequence[
            outputs.NetworkManagedServiceServiceNetworkEndpoint
        ],
        sts_accesses: Sequence[outputs.NetworkManagedServiceStsAccess],
        zero_etl_accesses: Sequence[outputs.NetworkManagedServiceZeroEtlAccess],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsAccesses")
    def kms_accesses(self) -> Sequence[outputs.NetworkManagedServiceKmsAccess]: ...
    @_builtins.property
    @pulumi.getter(name="managedS3BackupAccesses")
    def managed_s3_backup_accesses(
        self,
    ) -> Sequence[outputs.NetworkManagedServiceManagedS3BackupAccess]: ...
    @_builtins.property
    @pulumi.getter(name="managedServiceIpv4Cidrs")
    def managed_service_ipv4_cidrs(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGatewayArn")
    def resource_gateway_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Accesses")
    def s3_accesses(self) -> Sequence[outputs.NetworkManagedServiceS3Access]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkEndpoints")
    def service_network_endpoints(
        self,
    ) -> Sequence[outputs.NetworkManagedServiceServiceNetworkEndpoint]: ...
    @_builtins.property
    @pulumi.getter(name="stsAccesses")
    def sts_accesses(self) -> Sequence[outputs.NetworkManagedServiceStsAccess]: ...
    @_builtins.property
    @pulumi.getter(name="zeroEtlAccesses")
    def zero_etl_accesses(
        self,
    ) -> Sequence[outputs.NetworkManagedServiceZeroEtlAccess]: ...

@pulumi.output_type
class NetworkManagedServiceKmsAccess(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        ipv4_addresses: Sequence[_builtins.str],
        kms_policy_document: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsPolicyDocument")
    def kms_policy_document(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkManagedServiceManagedS3BackupAccess(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ipv4_addresses: Sequence[_builtins.str], status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkManagedServiceS3Access(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        ipv4_addresses: Sequence[_builtins.str],
        s3_policy_document: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3PolicyDocument")
    def s3_policy_document(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkManagedServiceServiceNetworkEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, vpc_endpoint_id: _builtins.str, vpc_endpoint_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointType")
    def vpc_endpoint_type(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkManagedServiceStsAccess(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        ipv4_addresses: Sequence[_builtins.str],
        status: _builtins.str,
        sts_policy_document: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stsPolicyDocument")
    def sts_policy_document(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkManagedServiceZeroEtlAccess(dict):
    def __init__(__self__, *, cidr: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkOciDnsForwardingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, domain_name: _builtins.str, oci_dns_listener_ip: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociDnsListenerIp")
    def oci_dns_listener_ip(self) -> _builtins.str: ...

@pulumi.output_type
class NetworkPeeringConnectionTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetCloudAutonomousVmClusterMaintenanceWindowResult(dict):
    def __init__(
        __self__,
        *,
        days_of_weeks: Sequence[
            outputs.GetCloudAutonomousVmClusterMaintenanceWindowDaysOfWeekResult
        ],
        hours_of_days: Sequence[_builtins.int],
        lead_time_in_weeks: _builtins.int,
        months: Sequence[
            outputs.GetCloudAutonomousVmClusterMaintenanceWindowMonthResult
        ],
        preference: _builtins.str,
        weeks_of_months: Sequence[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Sequence[
        outputs.GetCloudAutonomousVmClusterMaintenanceWindowDaysOfWeekResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="leadTimeInWeeks")
    def lead_time_in_weeks(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Sequence[outputs.GetCloudAutonomousVmClusterMaintenanceWindowMonthResult]: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetCloudAutonomousVmClusterMaintenanceWindowDaysOfWeekResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudAutonomousVmClusterMaintenanceWindowMonthResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudAutonomousVmClustersCloudAutonomousVmClusterResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cloud_exadata_infrastructure_id: _builtins.str,
        display_name: _builtins.str,
        id: _builtins.str,
        oci_resource_anchor_name: _builtins.str,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        odb_network_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetworkId")
    def odb_network_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudExadataInfrastructureCustomerContactsToSendToOciResult(dict):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudExadataInfrastructureMaintenanceWindowResult(dict):
    def __init__(
        __self__,
        *,
        custom_action_timeout_in_mins: _builtins.int,
        days_of_weeks: Sequence[
            outputs.GetCloudExadataInfrastructureMaintenanceWindowDaysOfWeekResult
        ],
        hours_of_days: Sequence[_builtins.int],
        is_custom_action_timeout_enabled: _builtins.bool,
        lead_time_in_weeks: _builtins.int,
        months: Sequence[
            outputs.GetCloudExadataInfrastructureMaintenanceWindowMonthResult
        ],
        patching_mode: _builtins.str,
        preference: _builtins.str,
        weeks_of_months: Sequence[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customActionTimeoutInMins")
    def custom_action_timeout_in_mins(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Sequence[
        outputs.GetCloudExadataInfrastructureMaintenanceWindowDaysOfWeekResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="isCustomActionTimeoutEnabled")
    def is_custom_action_timeout_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="leadTimeInWeeks")
    def lead_time_in_weeks(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Sequence[
        outputs.GetCloudExadataInfrastructureMaintenanceWindowMonthResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetCloudExadataInfrastructureMaintenanceWindowDaysOfWeekResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudExadataInfrastructureMaintenanceWindowMonthResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudExadataInfrastructuresCloudExadataInfrastructureResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        display_name: _builtins.str,
        id: _builtins.str,
        oci_resource_anchor_name: _builtins.str,
        oci_url: _builtins.str,
        ocid: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudVmClusterDataCollectionOptionResult(dict):
    def __init__(
        __self__,
        *,
        is_diagnostics_events_enabled: _builtins.bool,
        is_health_monitoring_enabled: _builtins.bool,
        is_incident_logs_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDiagnosticsEventsEnabled")
    def is_diagnostics_events_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isHealthMonitoringEnabled")
    def is_health_monitoring_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isIncidentLogsEnabled")
    def is_incident_logs_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetCloudVmClusterIormConfigCacheResult(dict):
    def __init__(
        __self__,
        *,
        db_plans: Sequence[outputs.GetCloudVmClusterIormConfigCacheDbPlanResult],
        lifecycle_details: _builtins.str,
        lifecycle_state: _builtins.str,
        objective: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbPlans")
    def db_plans(
        self,
    ) -> Sequence[outputs.GetCloudVmClusterIormConfigCacheDbPlanResult]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def objective(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudVmClusterIormConfigCacheDbPlanResult(dict):
    def __init__(
        __self__,
        *,
        db_name: _builtins.str,
        flash_cache_limit: _builtins.str,
        share: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="flashCacheLimit")
    def flash_cache_limit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def share(self) -> _builtins.int: ...

@pulumi.output_type
class GetCloudVmClustersCloudVmClusterResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        cloud_exadata_infrastructure_id: _builtins.str,
        display_name: _builtins.str,
        id: _builtins.str,
        oci_resource_anchor_name: _builtins.str,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        odb_network_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetworkId")
    def odb_network_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDbNodesDbNodeResult(dict):
    def __init__(
        __self__,
        *,
        additional_details: _builtins.str,
        arn: _builtins.str,
        backup_ip_id: _builtins.str,
        backup_vnic2_id: _builtins.str,
        backup_vnic_id: _builtins.str,
        cpu_core_count: _builtins.int,
        created_at: _builtins.str,
        db_node_storage_size: _builtins.int,
        db_server_id: _builtins.str,
        db_system_id: _builtins.str,
        fault_domain: _builtins.str,
        host_ip_id: _builtins.str,
        hostname: _builtins.str,
        id: _builtins.str,
        maintenance_type: _builtins.str,
        memory_size: _builtins.int,
        oci_resource_anchor_name: _builtins.str,
        ocid: _builtins.str,
        software_storage_size: _builtins.int,
        status: _builtins.str,
        status_reason: _builtins.str,
        time_maintenance_window_end: _builtins.str,
        time_maintenance_window_start: _builtins.str,
        total_cpu_core_count: _builtins.int,
        vnic2_id: _builtins.str,
        vnic_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalDetails")
    def additional_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupIpId")
    def backup_ip_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupVnic2Id")
    def backup_vnic2_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupVnicId")
    def backup_vnic_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSize")
    def db_node_storage_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServerId")
    def db_server_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="faultDomain")
    def fault_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostIpId")
    def host_ip_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceType")
    def maintenance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memorySize")
    def memory_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softwareStorageSize")
    def software_storage_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeMaintenanceWindowEnd")
    def time_maintenance_window_end(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeMaintenanceWindowStart")
    def time_maintenance_window_start(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalCpuCoreCount")
    def total_cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vnic2Id")
    def vnic2_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vnicId")
    def vnic_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDbServerDbServerPatchingDetailResult(dict):
    def __init__(
        __self__,
        *,
        estimated_patch_duration: _builtins.int,
        patching_status: _builtins.str,
        time_patching_ended: _builtins.str,
        time_patching_started: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="estimatedPatchDuration")
    def estimated_patch_duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="patchingStatus")
    def patching_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timePatchingEnded")
    def time_patching_ended(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timePatchingStarted")
    def time_patching_started(self) -> _builtins.str: ...

@pulumi.output_type
class GetDbServersDbServerResult(dict):
    def __init__(
        __self__,
        *,
        autonomous_virtual_machine_ids: Sequence[_builtins.str],
        autonomous_vm_cluster_ids: Sequence[_builtins.str],
        compute_model: _builtins.str,
        cpu_core_count: _builtins.int,
        created_at: _builtins.str,
        db_node_storage_size_in_gbs: _builtins.int,
        db_server_patching_details: Sequence[
            outputs.GetDbServersDbServerDbServerPatchingDetailResult
        ],
        display_name: _builtins.str,
        exadata_infrastructure_id: _builtins.str,
        id: _builtins.str,
        max_cpu_count: _builtins.int,
        max_db_node_storage_in_gbs: _builtins.int,
        max_memory_in_gbs: _builtins.int,
        memory_size_in_gbs: _builtins.int,
        oci_resource_anchor_name: _builtins.str,
        ocid: _builtins.str,
        shape: _builtins.str,
        status: _builtins.str,
        status_reason: _builtins.str,
        vm_cluster_ids: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autonomousVirtualMachineIds")
    def autonomous_virtual_machine_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autonomousVmClusterIds")
    def autonomous_vm_cluster_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServerPatchingDetails")
    def db_server_patching_details(
        self,
    ) -> Sequence[outputs.GetDbServersDbServerDbServerPatchingDetailResult]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exadataInfrastructureId")
    def exadata_infrastructure_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageInGbs")
    def max_db_node_storage_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxMemoryInGbs")
    def max_memory_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmClusterIds")
    def vm_cluster_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDbServersDbServerDbServerPatchingDetailResult(dict):
    def __init__(
        __self__,
        *,
        estimated_patch_duration: _builtins.int,
        patching_status: _builtins.str,
        time_patching_ended: _builtins.str,
        time_patching_started: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="estimatedPatchDuration")
    def estimated_patch_duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="patchingStatus")
    def patching_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timePatchingEnded")
    def time_patching_ended(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timePatchingStarted")
    def time_patching_started(self) -> _builtins.str: ...

@pulumi.output_type
class GetDbSystemShapesDbSystemShapeResult(dict):
    def __init__(
        __self__,
        *,
        available_core_count: _builtins.int,
        available_core_count_per_node: _builtins.int,
        available_data_storage_in_tbs: _builtins.int,
        available_data_storage_per_server_in_tbs: _builtins.int,
        available_db_node_per_node_in_gbs: _builtins.int,
        available_db_node_storage_in_gbs: _builtins.int,
        available_memory_in_gbs: _builtins.int,
        available_memory_per_node_in_gbs: _builtins.int,
        core_count_increment: _builtins.int,
        max_storage_count: _builtins.int,
        maximum_node_count: _builtins.int,
        min_core_count_per_node: _builtins.int,
        min_data_storage_in_tbs: _builtins.int,
        min_db_node_storage_per_node_in_gbs: _builtins.int,
        min_memory_per_node_in_gbs: _builtins.int,
        min_storage_count: _builtins.int,
        minimum_core_count: _builtins.int,
        minimum_node_count: _builtins.int,
        name: _builtins.str,
        runtime_minimum_core_count: _builtins.int,
        shape_family: _builtins.str,
        shape_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availableCoreCount")
    def available_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableCoreCountPerNode")
    def available_core_count_per_node(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableDataStorageInTbs")
    def available_data_storage_in_tbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableDataStoragePerServerInTbs")
    def available_data_storage_per_server_in_tbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableDbNodePerNodeInGbs")
    def available_db_node_per_node_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableDbNodeStorageInGbs")
    def available_db_node_storage_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableMemoryInGbs")
    def available_memory_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableMemoryPerNodeInGbs")
    def available_memory_per_node_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="coreCountIncrement")
    def core_count_increment(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxStorageCount")
    def max_storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumNodeCount")
    def maximum_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minCoreCountPerNode")
    def min_core_count_per_node(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minDataStorageInTbs")
    def min_data_storage_in_tbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minDbNodeStoragePerNodeInGbs")
    def min_db_node_storage_per_node_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minMemoryPerNodeInGbs")
    def min_memory_per_node_in_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minStorageCount")
    def min_storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minimumCoreCount")
    def minimum_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minimumNodeCount")
    def minimum_node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runtimeMinimumCoreCount")
    def runtime_minimum_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="shapeFamily")
    def shape_family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shapeType")
    def shape_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetGiVersionsGiVersionResult(dict):
    def __init__(__self__, *, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkManagedServiceResult(dict):
    def __init__(
        __self__,
        *,
        kms_accesses: Sequence[outputs.GetNetworkManagedServiceKmsAccessResult],
        managed_s3_backup_accesses: Sequence[
            outputs.GetNetworkManagedServiceManagedS3BackupAccessResult
        ],
        managed_service_ipv4_cidrs: Sequence[_builtins.str],
        resource_gateway_arn: _builtins.str,
        s3_accesses: Sequence[outputs.GetNetworkManagedServiceS3AccessResult],
        service_network_arn: _builtins.str,
        service_network_endpoints: Sequence[
            outputs.GetNetworkManagedServiceServiceNetworkEndpointResult
        ],
        sts_accesses: Sequence[outputs.GetNetworkManagedServiceStsAccessResult],
        zero_tl_accesses: Sequence[outputs.GetNetworkManagedServiceZeroTlAccessResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsAccesses")
    def kms_accesses(
        self,
    ) -> Sequence[outputs.GetNetworkManagedServiceKmsAccessResult]: ...
    @_builtins.property
    @pulumi.getter(name="managedS3BackupAccesses")
    def managed_s3_backup_accesses(
        self,
    ) -> Sequence[outputs.GetNetworkManagedServiceManagedS3BackupAccessResult]: ...
    @_builtins.property
    @pulumi.getter(name="managedServiceIpv4Cidrs")
    def managed_service_ipv4_cidrs(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGatewayArn")
    def resource_gateway_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Accesses")
    def s3_accesses(
        self,
    ) -> Sequence[outputs.GetNetworkManagedServiceS3AccessResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceNetworkEndpoints")
    def service_network_endpoints(
        self,
    ) -> Sequence[outputs.GetNetworkManagedServiceServiceNetworkEndpointResult]: ...
    @_builtins.property
    @pulumi.getter(name="stsAccesses")
    def sts_accesses(
        self,
    ) -> Sequence[outputs.GetNetworkManagedServiceStsAccessResult]: ...
    @_builtins.property
    @pulumi.getter(name="zeroTlAccesses")
    def zero_tl_accesses(
        self,
    ) -> Sequence[outputs.GetNetworkManagedServiceZeroTlAccessResult]: ...

@pulumi.output_type
class GetNetworkManagedServiceKmsAccessResult(dict):
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        ipv4_addresses: Sequence[_builtins.str],
        kms_policy_document: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsPolicyDocument")
    def kms_policy_document(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkManagedServiceManagedS3BackupAccessResult(dict):
    def __init__(
        __self__, *, ipv4_addresses: Sequence[_builtins.str], status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkManagedServiceS3AccessResult(dict):
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        ipv4_addresses: Sequence[_builtins.str],
        s3_policy_document: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3PolicyDocument")
    def s3_policy_document(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkManagedServiceServiceNetworkEndpointResult(dict):
    def __init__(
        __self__, *, vpc_endpoint_id: _builtins.str, vpc_endpoint_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointType")
    def vpc_endpoint_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkManagedServiceStsAccessResult(dict):
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        ipv4_addresses: Sequence[_builtins.str],
        status: _builtins.str,
        sts_policy_document: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stsPolicyDocument")
    def sts_policy_document(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkManagedServiceZeroTlAccessResult(dict):
    def __init__(__self__, *, cidr: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkOciDnsForwardingConfigResult(dict):
    def __init__(
        __self__, *, domain_name: _builtins.str, oci_dns_listener_ip: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociDnsListenerIp")
    def oci_dns_listener_ip(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworkPeeringConnectionsOdbPeeringConnectionResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        display_name: _builtins.str,
        id: _builtins.str,
        odb_network_arn: _builtins.str,
        peer_network_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetworkArn")
    def odb_network_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerNetworkArn")
    def peer_network_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetNetworksOdbNetworkResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        display_name: _builtins.str,
        id: _builtins.str,
        oci_network_anchor_id: _builtins.str,
        oci_vcn_id: _builtins.str,
        oci_vcn_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociNetworkAnchorId")
    def oci_network_anchor_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociVcnId")
    def oci_vcn_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociVcnUrl")
    def oci_vcn_url(self) -> _builtins.str: ...
