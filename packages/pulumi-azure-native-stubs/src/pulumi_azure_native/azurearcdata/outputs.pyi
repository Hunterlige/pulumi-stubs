

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ActiveDirectoryConnectorDNSDetailsResponse', 'ActiveDirectoryConnectorDomainDetailsResponse', 'ActiveDirectoryConnectorPropertiesResponse', 'ActiveDirectoryConnectorSpecResponse', 'ActiveDirectoryConnectorStatusResponse', 'ActiveDirectoryDomainControllerResponse', 'ActiveDirectoryDomainControllersResponse', 'AuthenticationResponse', 'AvailabilityGroupConfigureResponse', 'AvailabilityGroupInfoResponse', 'AvailabilityGroupStateResponse', 'BackgroundJobResponse', 'BackupPolicyResponse', 'BasicLoginInformationResponse', 'ClientConnectionResponse', 'DBMEndpointResponse', 'DataBaseMigrationAssessmentResponse', ..., 'DataBaseMigrationResponse', 'DataControllerPropertiesResponse', 'EntraAuthenticationResponse', 'ExtendedLocationResponse', 'FailoverClusterResponse', 'FailoverGroupPropertiesResponse', 'FailoverGroupSpecResponse', 'HostIPAddressInformationResponse', 'K8sActiveDirectoryResponse', 'K8sActiveDirectoryResponseConnector', 'K8sNetworkSettingsResponse', 'K8sResourceRequirementsResponse', 'K8sSchedulingOptionsResponse', 'K8sSchedulingResponse', 'K8sSecurityResponse', 'K8sSettingsResponse', 'K8stransparentDataEncryptionResponse', 'LogAnalyticsWorkspaceConfigResponse', 'MigrationAssessmentResponse', 'MigrationAssessmentResponseImpactedObjects', 'MigrationAssessmentResponseServerAssessments', 'MigrationResponse', 'MonitoringResponse', 'OnPremisePropertyResponse', 'PostgresInstancePropertiesResponse', 'PostgresInstanceSkuResponse', 'SequencerActionResponse', 'SkuRecommendationResultsAzureSqlDatabaseResponse', ..., ..., ..., ..., ..., ..., ..., ..., 'SkuRecommendationResultsMonthlyCostResponse', 'SkuRecommendationResultsResponse', 'SkuRecommendationSummaryResponse', ..., ..., ..., ..., 'SqlManagedInstanceK8sRawResponse', 'SqlManagedInstanceK8sSpecResponse', 'SqlManagedInstancePropertiesResponse', 'SqlManagedInstanceSkuResponse', ..., ..., ..., 'SqlServerDatabaseResourcePropertiesResponse', ..., ..., 'SqlServerEsuLicensePropertiesResponse', 'SqlServerInstanceJobStatusResponse', 'SqlServerInstancePropertiesResponse', 'SqlServerInstanceTelemetryColumnResponse', 'SqlServerLicensePropertiesResponse', 'SystemDataResponse', 'TargetReadinessResponse', 'UploadServicePrincipalResponse', 'UploadWatermarkResponse']
@pulumi.output_type
class ActiveDirectoryConnectorDNSDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, nameserver_ip_addresses: Sequence[_builtins.str], domain_name: Optional[_builtins.str] = ..., prefer_k8s_dns_for_ptr_lookups: Optional[_builtins.bool] = ..., replicas: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameserverIPAddresses")
    def nameserver_ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferK8sDnsForPtrLookups")
    def prefer_k8s_dns_for_ptr_lookups(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ActiveDirectoryConnectorDomainDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, realm: _builtins.str, domain_controllers: Optional[outputs.ActiveDirectoryDomainControllersResponse] = ..., netbios_domain_name: Optional[_builtins.str] = ..., ou_distinguished_name: Optional[_builtins.str] = ..., service_account_provisioning: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def realm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainControllers")
    def domain_controllers(self) -> Optional[outputs.ActiveDirectoryDomainControllersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="netbiosDomainName")
    def netbios_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ouDistinguishedName")
    def ou_distinguished_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountProvisioning")
    def service_account_provisioning(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ActiveDirectoryConnectorPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, spec: outputs.ActiveDirectoryConnectorSpecResponse, domain_service_account_login_information: Optional[outputs.BasicLoginInformationResponse] = ..., status: Optional[outputs.ActiveDirectoryConnectorStatusResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> outputs.ActiveDirectoryConnectorSpecResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainServiceAccountLoginInformation")
    def domain_service_account_login_information(self) -> Optional[outputs.BasicLoginInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.ActiveDirectoryConnectorStatusResponse]:
        
        ...
    


@pulumi.output_type
class ActiveDirectoryConnectorSpecResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_directory: outputs.ActiveDirectoryConnectorDomainDetailsResponse, dns: outputs.ActiveDirectoryConnectorDNSDetailsResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectory")
    def active_directory(self) -> outputs.ActiveDirectoryConnectorDomainDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dns(self) -> outputs.ActiveDirectoryConnectorDNSDetailsResponse:
        
        ...
    


@pulumi.output_type
class ActiveDirectoryConnectorStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_update_time: Optional[_builtins.str] = ..., observed_generation: Optional[_builtins.float] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateTime")
    def last_update_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ActiveDirectoryDomainControllerResponse(dict):
    
    def __init__(__self__, *, hostname: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ActiveDirectoryDomainControllersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, primary_domain_controller: Optional[outputs.ActiveDirectoryDomainControllerResponse] = ..., secondary_domain_controllers: Optional[Sequence[outputs.ActiveDirectoryDomainControllerResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryDomainController")
    def primary_domain_controller(self) -> Optional[outputs.ActiveDirectoryDomainControllerResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryDomainControllers")
    def secondary_domain_controllers(self) -> Optional[Sequence[outputs.ActiveDirectoryDomainControllerResponse]]:
        
        ...
    


@pulumi.output_type
class AuthenticationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mode: Optional[_builtins.str] = ..., sql_server_entra_identity: Optional[Sequence[outputs.EntraAuthenticationResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerEntraIdentity")
    def sql_server_entra_identity(self) -> Optional[Sequence[outputs.EntraAuthenticationResponse]]:
        
        ...
    


@pulumi.output_type
class AvailabilityGroupConfigureResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_mode_description: _builtins.str, failover_mode_description: _builtins.str, primary_role_allow_connections_description: _builtins.str, replica_create_date: _builtins.str, replica_modify_date: _builtins.str, secondary_role_allow_connections_description: _builtins.str, seeding_mode_description: _builtins.str, availability_mode: Optional[_builtins.str] = ..., backup_priority: Optional[_builtins.int] = ..., certificate_name: Optional[_builtins.str] = ..., endpoint_authentication_mode: Optional[_builtins.str] = ..., endpoint_connect_login: Optional[_builtins.str] = ..., endpoint_name: Optional[_builtins.str] = ..., endpoint_url: Optional[_builtins.str] = ..., failover_mode: Optional[_builtins.str] = ..., primary_allow_connections: Optional[_builtins.str] = ..., read_only_routing_url: Optional[_builtins.str] = ..., read_write_routing_url: Optional[_builtins.str] = ..., secondary_allow_connections: Optional[_builtins.str] = ..., seeding_mode: Optional[_builtins.str] = ..., session_timeout: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityModeDescription")
    def availability_mode_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverModeDescription")
    def failover_mode_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryRoleAllowConnectionsDescription")
    def primary_role_allow_connections_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCreateDate")
    def replica_create_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaModifyDate")
    def replica_modify_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryRoleAllowConnectionsDescription")
    def secondary_role_allow_connections_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedingModeDescription")
    def seeding_mode_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityMode")
    def availability_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPriority")
    def backup_priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointAuthenticationMode")
    def endpoint_authentication_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointConnectLogin")
    def endpoint_connect_login(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUrl")
    def endpoint_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverMode")
    def failover_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryAllowConnections")
    def primary_allow_connections(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyRoutingUrl")
    def read_only_routing_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readWriteRoutingUrl")
    def read_write_routing_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryAllowConnections")
    def secondary_allow_connections(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedingMode")
    def seeding_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AvailabilityGroupInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automated_backup_preference_description: _builtins.str, cluster_type_description: _builtins.str, primary_recovery_health_description: _builtins.str, primary_replica: _builtins.str, replication_partner_type: _builtins.str, secondary_recovery_health_description: _builtins.str, synchronization_health_description: _builtins.str, version: _builtins.int, basic_features: Optional[_builtins.bool] = ..., db_failover: Optional[_builtins.bool] = ..., dtc_support: Optional[_builtins.bool] = ..., failure_condition_level: Optional[_builtins.int] = ..., health_check_timeout: Optional[_builtins.int] = ..., is_contained: Optional[_builtins.bool] = ..., is_distributed: Optional[_builtins.bool] = ..., listener: Optional[outputs.SqlAvailabilityGroupStaticIPListenerPropertiesResponse] = ..., required_synchronized_secondaries_to_commit: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedBackupPreferenceDescription")
    def automated_backup_preference_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterTypeDescription")
    def cluster_type_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryRecoveryHealthDescription")
    def primary_recovery_health_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryReplica")
    def primary_replica(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationPartnerType")
    def replication_partner_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryRecoveryHealthDescription")
    def secondary_recovery_health_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationHealthDescription")
    def synchronization_health_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicFeatures")
    def basic_features(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbFailover")
    def db_failover(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtcSupport")
    def dtc_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureConditionLevel")
    def failure_condition_level(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckTimeout")
    def health_check_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isContained")
    def is_contained(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDistributed")
    def is_distributed(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def listener(self) -> Optional[outputs.SqlAvailabilityGroupStaticIPListenerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredSynchronizedSecondariesToCommit")
    def required_synchronized_secondaries_to_commit(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AvailabilityGroupStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_group_replica_role: _builtins.str, connected_state_description: _builtins.str, last_connect_error_description: _builtins.str, last_connect_error_timestamp: _builtins.str, operational_state_description: _builtins.str, recovery_health_description: _builtins.str, synchronization_health_description: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityGroupReplicaRole")
    def availability_group_replica_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedStateDescription")
    def connected_state_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastConnectErrorDescription")
    def last_connect_error_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastConnectErrorTimestamp")
    def last_connect_error_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationalStateDescription")
    def operational_state_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryHealthDescription")
    def recovery_health_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationHealthDescription")
    def synchronization_health_description(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BackgroundJobResponse(dict):
    
    def __init__(__self__, *, end_time: Optional[_builtins.str] = ..., execution_state: Optional[_builtins.str] = ..., last_execution_status: Optional[_builtins.str] = ..., last_execution_time: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionState")
    def execution_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionStatus")
    def last_execution_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastExecutionTime")
    def last_execution_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BackupPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, differential_backup_hours: Optional[_builtins.int] = ..., full_backup_days: Optional[_builtins.int] = ..., retention_period_days: Optional[_builtins.int] = ..., transaction_log_backup_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="differentialBackupHours")
    def differential_backup_hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullBackupDays")
    def full_backup_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionLogBackupMinutes")
    def transaction_log_backup_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BasicLoginInformationResponse(dict):
    
    def __init__(__self__, *, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClientConnectionResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DBMEndpointResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_name: _builtins.str, connection_auth: _builtins.str, encryption_algorithm: _builtins.str, endpoint_name: _builtins.str, ip_address: _builtins.str, is_dynamic_port: _builtins.bool, is_encryption_enabled: _builtins.bool, port: _builtins.int, role: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionAuth")
    def connection_auth(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDynamicPort")
    def is_dynamic_port(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEncryptionEnabled")
    def is_encryption_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DataBaseMigrationAssessmentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assessment_upload_time: _builtins.str, database_assessments: Sequence[outputs.DataBaseMigrationAssessmentResponseDatabaseAssessments], target_readiness: outputs.TargetReadinessResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentUploadTime")
    def assessment_upload_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseAssessments")
    def database_assessments(self) -> Sequence[outputs.DataBaseMigrationAssessmentResponseDatabaseAssessments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReadiness")
    def target_readiness(self) -> outputs.TargetReadinessResponse:
        
        ...
    


@pulumi.output_type
class DataBaseMigrationAssessmentResponseDatabaseAssessments(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applies_to_migration_target_platform: Optional[_builtins.str] = ..., feature_id: Optional[_builtins.str] = ..., issue_category: Optional[_builtins.str] = ..., more_information: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliesToMigrationTargetPlatform")
    def applies_to_migration_target_platform(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureId")
    def feature_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueCategory")
    def issue_category(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="moreInformation")
    def more_information(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class DataBaseMigrationResponse(dict):
    
    def __init__(__self__, *, assessment: Optional[outputs.DataBaseMigrationAssessmentResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assessment(self) -> Optional[outputs.DataBaseMigrationAssessmentResponse]:
        
        ...
    


@pulumi.output_type
class DataControllerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, basic_login_information: Optional[outputs.BasicLoginInformationResponse] = ..., cluster_id: Optional[_builtins.str] = ..., extension_id: Optional[_builtins.str] = ..., infrastructure: Optional[_builtins.str] = ..., k8s_raw: Optional[Any] = ..., last_uploaded_date: Optional[_builtins.str] = ..., log_analytics_workspace_config: Optional[outputs.LogAnalyticsWorkspaceConfigResponse] = ..., logs_dashboard_credential: Optional[outputs.BasicLoginInformationResponse] = ..., metrics_dashboard_credential: Optional[outputs.BasicLoginInformationResponse] = ..., on_premise_property: Optional[outputs.OnPremisePropertyResponse] = ..., upload_service_principal: Optional[outputs.UploadServicePrincipalResponse] = ..., upload_watermark: Optional[outputs.UploadWatermarkResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicLoginInformation")
    def basic_login_information(self) -> Optional[outputs.BasicLoginInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionId")
    def extension_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def infrastructure(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="k8sRaw")
    def k8s_raw(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUploadedDate")
    def last_uploaded_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceConfig")
    def log_analytics_workspace_config(self) -> Optional[outputs.LogAnalyticsWorkspaceConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsDashboardCredential")
    def logs_dashboard_credential(self) -> Optional[outputs.BasicLoginInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsDashboardCredential")
    def metrics_dashboard_credential(self) -> Optional[outputs.BasicLoginInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPremiseProperty")
    def on_premise_property(self) -> Optional[outputs.OnPremisePropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadServicePrincipal")
    def upload_service_principal(self) -> Optional[outputs.UploadServicePrincipalResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadWatermark")
    def upload_watermark(self) -> Optional[outputs.UploadWatermarkResponse]:
        
        ...
    


@pulumi.output_type
class EntraAuthenticationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., identity_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtendedLocationResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FailoverClusterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, host_ip_addresses: Sequence[outputs.HostIPAddressInformationResponse], host_names: Sequence[_builtins.str], id: _builtins.str, network_name: _builtins.str, sql_instance_ids: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostIPAddresses")
    def host_ip_addresses(self) -> Sequence[outputs.HostIPAddressInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostNames")
    def host_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlInstanceIds")
    def sql_instance_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FailoverGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, partner_managed_instance_id: _builtins.str, provisioning_state: _builtins.str, spec: outputs.FailoverGroupSpecResponse, status: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerManagedInstanceId")
    def partner_managed_instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> outputs.FailoverGroupSpecResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class FailoverGroupSpecResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role: Optional[_builtins.str] = ..., partner_mi: Optional[_builtins.str] = ..., partner_mirroring_cert: Optional[_builtins.str] = ..., partner_mirroring_url: Optional[_builtins.str] = ..., partner_sync_mode: Optional[_builtins.str] = ..., shared_name: Optional[_builtins.str] = ..., source_mi: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerMI")
    def partner_mi(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerMirroringCert")
    def partner_mirroring_cert(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerMirroringURL")
    def partner_mirroring_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerSyncMode")
    def partner_sync_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedName")
    def shared_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMI")
    def source_mi(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostIPAddressInformationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: _builtins.str, subnet_mask: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class K8sActiveDirectoryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_name: Optional[_builtins.str] = ..., connector: Optional[outputs.K8sActiveDirectoryResponseConnector] = ..., encryption_types: Optional[Sequence[_builtins.str]] = ..., keytab_secret: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[outputs.K8sActiveDirectoryResponseConnector]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionTypes")
    def encryption_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keytabSecret")
    def keytab_secret(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class K8sActiveDirectoryResponseConnector(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class K8sNetworkSettingsResponse(dict):
    
    def __init__(__self__, *, forceencryption: Optional[_builtins.int] = ..., tlsciphers: Optional[_builtins.str] = ..., tlsprotocols: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def forceencryption(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tlsciphers(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tlsprotocols(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class K8sResourceRequirementsResponse(dict):
    
    def __init__(__self__, *, limits: Optional[Mapping[str, _builtins.str]] = ..., requests: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class K8sSchedulingOptionsResponse(dict):
    
    def __init__(__self__, *, resources: Optional[outputs.K8sResourceRequirementsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.K8sResourceRequirementsResponse]:
        
        ...
    


@pulumi.output_type
class K8sSchedulingResponse(dict):
    
    def __init__(__self__, *, default: Optional[outputs.K8sSchedulingOptionsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[outputs.K8sSchedulingOptionsResponse]:
        
        ...
    


@pulumi.output_type
class K8sSecurityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_directory: Optional[outputs.K8sActiveDirectoryResponse] = ..., admin_login_secret: Optional[_builtins.str] = ..., service_certificate_secret: Optional[_builtins.str] = ..., transparent_data_encryption: Optional[outputs.K8stransparentDataEncryptionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectory")
    def active_directory(self) -> Optional[outputs.K8sActiveDirectoryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminLoginSecret")
    def admin_login_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCertificateSecret")
    def service_certificate_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transparentDataEncryption")
    def transparent_data_encryption(self) -> Optional[outputs.K8stransparentDataEncryptionResponse]:
        
        ...
    


@pulumi.output_type
class K8sSettingsResponse(dict):
    
    def __init__(__self__, *, network: Optional[outputs.K8sNetworkSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[outputs.K8sNetworkSettingsResponse]:
        
        ...
    


@pulumi.output_type
class K8stransparentDataEncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mode: Optional[_builtins.str] = ..., protector_secret: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectorSecret")
    def protector_secret(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LogAnalyticsWorkspaceConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, workspace_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MigrationAssessmentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assessment_upload_time: _builtins.str, server_assessments: Sequence[outputs.MigrationAssessmentResponseServerAssessments], sku_recommendation_results: outputs.SkuRecommendationResultsResponse, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentUploadTime")
    def assessment_upload_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverAssessments")
    def server_assessments(self) -> Sequence[outputs.MigrationAssessmentResponseServerAssessments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuRecommendationResults")
    def sku_recommendation_results(self) -> outputs.SkuRecommendationResultsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MigrationAssessmentResponseImpactedObjects(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, impact_detail: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., object_type: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactDetail")
    def impact_detail(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectType")
    def object_type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MigrationAssessmentResponseServerAssessments(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applies_to_migration_target_platform: Optional[_builtins.str] = ..., feature_id: Optional[_builtins.str] = ..., impacted_objects: Optional[Sequence[outputs.MigrationAssessmentResponseImpactedObjects]] = ..., issue_category: Optional[_builtins.str] = ..., more_information: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliesToMigrationTargetPlatform")
    def applies_to_migration_target_platform(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureId")
    def feature_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impactedObjects")
    def impacted_objects(self) -> Optional[Sequence[outputs.MigrationAssessmentResponseImpactedObjects]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueCategory")
    def issue_category(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="moreInformation")
    def more_information(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class MigrationResponse(dict):
    
    def __init__(__self__, *, assessment: Optional[outputs.MigrationAssessmentResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assessment(self) -> Optional[outputs.MigrationAssessmentResponse]:
        
        ...
    


@pulumi.output_type
class MonitoringResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class OnPremisePropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, public_signing_key: _builtins.str, signing_certificate_thumbprint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicSigningKey")
    def public_signing_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingCertificateThumbprint")
    def signing_certificate_thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PostgresInstancePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, admin: Optional[_builtins.str] = ..., basic_login_information: Optional[outputs.BasicLoginInformationResponse] = ..., data_controller_id: Optional[_builtins.str] = ..., k8s_raw: Optional[Any] = ..., last_uploaded_date: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def admin(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicLoginInformation")
    def basic_login_information(self) -> Optional[outputs.BasicLoginInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataControllerId")
    def data_controller_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="k8sRaw")
    def k8s_raw(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUploadedDate")
    def last_uploaded_date(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PostgresInstanceSkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., dev: Optional[_builtins.bool] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dev(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SequencerActionResponse(dict):
    
    def __init__(__self__, *, action_id: Optional[_builtins.str] = ..., result: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def result(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlDatabaseResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, monthly_cost: Optional[outputs.SkuRecommendationResultsMonthlyCostResponse] = ..., number_of_server_blocker_issues: Optional[_builtins.int] = ..., recommendation_status: Optional[_builtins.str] = ..., target_sku: Optional[outputs.SkuRecommendationResultsAzureSqlDatabaseResponseTargetSku] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyCost")
    def monthly_cost(self) -> Optional[outputs.SkuRecommendationResultsMonthlyCostResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfServerBlockerIssues")
    def number_of_server_blocker_issues(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendationStatus")
    def recommendation_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSku")
    def target_sku(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlDatabaseResponseTargetSku]:
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlDatabaseResponseCategory(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compute_tier: Optional[_builtins.str] = ..., hardware_type: Optional[_builtins.str] = ..., sql_purchasing_model: Optional[_builtins.str] = ..., sql_service_tier: Optional[_builtins.str] = ..., zone_redundancy_available: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeTier")
    def compute_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareType")
    def hardware_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlPurchasingModel")
    def sql_purchasing_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServiceTier")
    def sql_service_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundancyAvailable")
    def zone_redundancy_available(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlDatabaseResponseTargetSku(dict):
    def __init__(__self__, *, category: Optional[outputs.SkuRecommendationResultsAzureSqlDatabaseResponseCategory] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlDatabaseResponseCategory]:
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlManagedInstanceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, monthly_cost: Optional[outputs.SkuRecommendationResultsMonthlyCostResponse] = ..., number_of_server_blocker_issues: Optional[_builtins.int] = ..., recommendation_status: Optional[_builtins.str] = ..., target_sku: Optional[outputs.SkuRecommendationResultsAzureSqlManagedInstanceResponseTargetSku] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyCost")
    def monthly_cost(self) -> Optional[outputs.SkuRecommendationResultsMonthlyCostResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfServerBlockerIssues")
    def number_of_server_blocker_issues(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendationStatus")
    def recommendation_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSku")
    def target_sku(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlManagedInstanceResponseTargetSku]:
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlManagedInstanceResponseCategory(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compute_tier: Optional[_builtins.str] = ..., hardware_type: Optional[_builtins.str] = ..., sql_purchasing_model: Optional[_builtins.str] = ..., sql_service_tier: Optional[_builtins.str] = ..., zone_redundancy_available: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeTier")
    def compute_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareType")
    def hardware_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlPurchasingModel")
    def sql_purchasing_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServiceTier")
    def sql_service_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundancyAvailable")
    def zone_redundancy_available(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlManagedInstanceResponseTargetSku(dict):
    def __init__(__self__, *, category: Optional[outputs.SkuRecommendationResultsAzureSqlManagedInstanceResponseCategory] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlManagedInstanceResponseCategory]:
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlVirtualMachineResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, monthly_cost: Optional[outputs.SkuRecommendationResultsMonthlyCostResponse] = ..., number_of_server_blocker_issues: Optional[_builtins.int] = ..., recommendation_status: Optional[_builtins.str] = ..., target_sku: Optional[outputs.SkuRecommendationResultsAzureSqlVirtualMachineResponseTargetSku] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyCost")
    def monthly_cost(self) -> Optional[outputs.SkuRecommendationResultsMonthlyCostResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfServerBlockerIssues")
    def number_of_server_blocker_issues(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendationStatus")
    def recommendation_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetSku")
    def target_sku(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlVirtualMachineResponseTargetSku]:
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlVirtualMachineResponseCategory(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, available_vm_skus: Optional[Sequence[_builtins.str]] = ..., virtual_machine_family: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableVmSkus")
    def available_vm_skus(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineFamily")
    def virtual_machine_family(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuRecommendationResultsAzureSqlVirtualMachineResponseTargetSku(dict):
    def __init__(__self__, *, category: Optional[outputs.SkuRecommendationResultsAzureSqlVirtualMachineResponseCategory] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlVirtualMachineResponseCategory]:
        ...
    


@pulumi.output_type
class SkuRecommendationResultsMonthlyCostResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compute_cost: Optional[_builtins.float] = ..., storage_cost: Optional[_builtins.float] = ..., total_cost: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCost")
    def compute_cost(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCost")
    def storage_cost(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalCost")
    def total_cost(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SkuRecommendationResultsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_sql_database: Optional[outputs.SkuRecommendationResultsAzureSqlDatabaseResponse] = ..., azure_sql_managed_instance: Optional[outputs.SkuRecommendationResultsAzureSqlManagedInstanceResponse] = ..., azure_sql_virtual_machine: Optional[outputs.SkuRecommendationResultsAzureSqlVirtualMachineResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlDatabase")
    def azure_sql_database(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlDatabaseResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlManagedInstance")
    def azure_sql_managed_instance(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlManagedInstanceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlVirtualMachine")
    def azure_sql_virtual_machine(self) -> Optional[outputs.SkuRecommendationResultsAzureSqlVirtualMachineResponse]:
        
        ...
    


@pulumi.output_type
class SkuRecommendationSummaryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, num_of_blocker_issues: Optional[_builtins.int] = ..., recommendation_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numOfBlockerIssues")
    def num_of_blocker_issues(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendationStatus")
    def recommendation_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlAvailabilityGroupDatabaseReplicaResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_state_description: _builtins.str, is_commit_participant: _builtins.bool, is_local: _builtins.bool, is_primary_replica: _builtins.bool, is_suspended: _builtins.bool, replica_name: _builtins.str, suspend_reason_description: _builtins.str, synchronization_health_description: _builtins.str, synchronization_state_description: _builtins.str, database_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseStateDescription")
    def database_state_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCommitParticipant")
    def is_commit_participant(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocal")
    def is_local(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrimaryReplica")
    def is_primary_replica(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSuspended")
    def is_suspended(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaName")
    def replica_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendReasonDescription")
    def suspend_reason_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationHealthDescription")
    def synchronization_health_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationStateDescription")
    def synchronization_state_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlAvailabilityGroupReplicaResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replica_id: _builtins.str, configure: Optional[outputs.AvailabilityGroupConfigureResponse] = ..., replica_name: Optional[_builtins.str] = ..., replica_resource_id: Optional[_builtins.str] = ..., state: Optional[outputs.AvailabilityGroupStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaId")
    def replica_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configure(self) -> Optional[outputs.AvailabilityGroupConfigureResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaName")
    def replica_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaResourceId")
    def replica_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[outputs.AvailabilityGroupStateResponse]:
        
        ...
    


@pulumi.output_type
class SqlAvailabilityGroupStaticIPListenerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dns_name: Optional[_builtins.str] = ..., ip_v4_addresses_and_masks: Optional[Sequence[outputs.SqlAvailabilityGroupStaticIPListenerPropertiesResponseIpV4AddressesAndMasks]] = ..., ip_v6_addresses: Optional[Sequence[_builtins.str]] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipV4AddressesAndMasks")
    def ip_v4_addresses_and_masks(self) -> Optional[Sequence[outputs.SqlAvailabilityGroupStaticIPListenerPropertiesResponseIpV4AddressesAndMasks]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipV6Addresses")
    def ip_v6_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SqlAvailabilityGroupStaticIPListenerPropertiesResponseIpV4AddressesAndMasks(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: Optional[_builtins.str] = ..., mask: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mask(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlManagedInstanceK8sRawResponse(dict):
    
    def __init__(__self__, *, spec: Optional[outputs.SqlManagedInstanceK8sSpecResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[outputs.SqlManagedInstanceK8sSpecResponse]:
        
        ...
    


@pulumi.output_type
class SqlManagedInstanceK8sSpecResponse(dict):
    
    def __init__(__self__, *, replicas: Optional[_builtins.int] = ..., scheduling: Optional[outputs.K8sSchedulingResponse] = ..., security: Optional[outputs.K8sSecurityResponse] = ..., settings: Optional[outputs.K8sSettingsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> Optional[outputs.K8sSchedulingResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def security(self) -> Optional[outputs.K8sSecurityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.K8sSettingsResponse]:
        
        ...
    


@pulumi.output_type
class SqlManagedInstancePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, admin: Optional[_builtins.str] = ..., basic_login_information: Optional[outputs.BasicLoginInformationResponse] = ..., cluster_id: Optional[_builtins.str] = ..., data_controller_id: Optional[_builtins.str] = ..., end_time: Optional[_builtins.str] = ..., extension_id: Optional[_builtins.str] = ..., k8s_raw: Optional[outputs.SqlManagedInstanceK8sRawResponse] = ..., last_uploaded_date: Optional[_builtins.str] = ..., license_type: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def admin(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicLoginInformation")
    def basic_login_information(self) -> Optional[outputs.BasicLoginInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataControllerId")
    def data_controller_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionId")
    def extension_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="k8sRaw")
    def k8s_raw(self) -> Optional[outputs.SqlManagedInstanceK8sRawResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUploadedDate")
    def last_uploaded_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlManagedInstanceSkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., dev: Optional[_builtins.bool] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dev(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlServerAvailabilityGroupResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_group_id: _builtins.str, collection_timestamp: _builtins.str, instance_name: _builtins.str, provisioning_state: _builtins.str, server_name: _builtins.str, vm_id: _builtins.str, databases: Optional[outputs.SqlServerAvailabilityGroupResourcePropertiesResponseDatabases] = ..., info: Optional[outputs.AvailabilityGroupInfoResponse] = ..., replicas: Optional[outputs.SqlServerAvailabilityGroupResourcePropertiesResponseReplicas] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityGroupId")
    def availability_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionTimestamp")
    def collection_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Optional[outputs.SqlServerAvailabilityGroupResourcePropertiesResponseDatabases]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def info(self) -> Optional[outputs.AvailabilityGroupInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[outputs.SqlServerAvailabilityGroupResourcePropertiesResponseReplicas]:
        
        ...
    


@pulumi.output_type
class SqlServerAvailabilityGroupResourcePropertiesResponseDatabases(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_link: _builtins.str, value: Optional[Sequence[outputs.SqlAvailabilityGroupDatabaseReplicaResourcePropertiesResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.SqlAvailabilityGroupDatabaseReplicaResourcePropertiesResponse]]:
        
        ...
    


@pulumi.output_type
class SqlServerAvailabilityGroupResourcePropertiesResponseReplicas(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_link: _builtins.str, value: Optional[Sequence[outputs.SqlAvailabilityGroupReplicaResourcePropertiesResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.SqlAvailabilityGroupReplicaResourcePropertiesResponse]]:
        
        ...
    


@pulumi.output_type
class SqlServerDatabaseResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, earliest_restore_date: _builtins.str, last_database_upload_time: _builtins.str, provisioning_state: _builtins.str, vm_id: _builtins.str, backup_information: Optional[outputs.SqlServerDatabaseResourcePropertiesResponseBackupInformation] = ..., backup_policy: Optional[outputs.BackupPolicyResponse] = ..., collation_name: Optional[_builtins.str] = ..., compatibility_level: Optional[_builtins.int] = ..., create_mode: Optional[_builtins.str] = ..., data_file_size_mb: Optional[_builtins.float] = ..., database_creation_date: Optional[_builtins.str] = ..., database_options: Optional[outputs.SqlServerDatabaseResourcePropertiesResponseDatabaseOptions] = ..., is_read_only: Optional[_builtins.bool] = ..., log_file_size_mb: Optional[_builtins.float] = ..., migration: Optional[outputs.DataBaseMigrationResponse] = ..., recovery_mode: Optional[_builtins.str] = ..., restore_point_in_time: Optional[_builtins.str] = ..., size_mb: Optional[_builtins.float] = ..., source_database_id: Optional[_builtins.str] = ..., space_available_mb: Optional[_builtins.float] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDatabaseUploadTime")
    def last_database_upload_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupInformation")
    def backup_information(self) -> Optional[outputs.SqlServerDatabaseResourcePropertiesResponseBackupInformation]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> Optional[outputs.BackupPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collationName")
    def collation_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFileSizeMB")
    def data_file_size_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseCreationDate")
    def database_creation_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseOptions")
    def database_options(self) -> Optional[outputs.SqlServerDatabaseResourcePropertiesResponseDatabaseOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isReadOnly")
    def is_read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logFileSizeMB")
    def log_file_size_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def migration(self) -> Optional[outputs.DataBaseMigrationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryMode")
    def recovery_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeMB")
    def size_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseId")
    def source_database_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceAvailableMB")
    def space_available_mb(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlServerDatabaseResourcePropertiesResponseBackupInformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_full_backup: Optional[_builtins.str] = ..., last_log_backup: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastFullBackup")
    def last_full_backup(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastLogBackup")
    def last_log_backup(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlServerDatabaseResourcePropertiesResponseDatabaseOptions(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_auto_close_on: Optional[_builtins.bool] = ..., is_auto_create_stats_on: Optional[_builtins.bool] = ..., is_auto_shrink_on: Optional[_builtins.bool] = ..., is_auto_update_stats_on: Optional[_builtins.bool] = ..., is_encrypted: Optional[_builtins.bool] = ..., is_memory_optimization_enabled: Optional[_builtins.bool] = ..., is_remote_data_archive_enabled: Optional[_builtins.bool] = ..., is_trustworthy_on: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutoCloseOn")
    def is_auto_close_on(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutoCreateStatsOn")
    def is_auto_create_stats_on(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutoShrinkOn")
    def is_auto_shrink_on(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutoUpdateStatsOn")
    def is_auto_update_stats_on(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEncrypted")
    def is_encrypted(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMemoryOptimizationEnabled")
    def is_memory_optimization_enabled(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRemoteDataArchiveEnabled")
    def is_remote_data_archive_enabled(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTrustworthyOn")
    def is_trustworthy_on(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class SqlServerEsuLicensePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, activated_at: _builtins.str, activation_state: _builtins.str, billing_plan: _builtins.str, physical_cores: _builtins.int, scope_type: _builtins.str, tenant_id: _builtins.str, terminated_at: _builtins.str, unique_id: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activatedAt")
    def activated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingPlan")
    def billing_plan(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalCores")
    def physical_cores(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminatedAt")
    def terminated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SqlServerInstanceJobStatusResponse(dict):
    
    def __init__(__self__, *, background_job: Optional[outputs.BackgroundJobResponse] = ..., id: Optional[_builtins.str] = ..., instance_name: Optional[_builtins.str] = ..., job_exception: Optional[_builtins.str] = ..., job_status: Optional[_builtins.str] = ..., sequencer_actions: Optional[Sequence[outputs.SequencerActionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backgroundJob")
    def background_job(self) -> Optional[outputs.BackgroundJobResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobException")
    def job_exception(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobStatus")
    def job_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sequencerActions")
    def sequencer_actions(self) -> Optional[Sequence[outputs.SequencerActionResponse]]:
        
        ...
    


@pulumi.output_type
class SqlServerInstancePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, always_on_role: _builtins.str, azure_defender_status: _builtins.str, azure_defender_status_last_updated: _builtins.str, collation: _builtins.str, container_resource_id: _builtins.str, create_time: _builtins.str, current_version: _builtins.str, db_master_key_exists: _builtins.bool, is_digi_cert_pki_cert_trust_configured: _builtins.bool, is_hadr_enabled: _builtins.bool, is_microsoft_pki_cert_trust_configured: _builtins.bool, last_inventory_upload_time: _builtins.str, last_usage_upload_time: _builtins.str, license_type: _builtins.str, max_server_memory_mb: _builtins.float, patch_level: _builtins.str, product_id: _builtins.str, provisioning_state: _builtins.str, status: _builtins.str, tcp_dynamic_ports: _builtins.str, tcp_static_ports: _builtins.str, trace_flags: Sequence[_builtins.int], v_core: _builtins.str, vm_id: _builtins.str, authentication: Optional[outputs.AuthenticationResponse] = ..., backup_policy: Optional[outputs.BackupPolicyResponse] = ..., client_connection: Optional[outputs.ClientConnectionResponse] = ..., cores: Optional[_builtins.str] = ..., database_mirroring_endpoint: Optional[outputs.DBMEndpointResponse] = ..., edition: Optional[_builtins.str] = ..., failover_cluster: Optional[outputs.FailoverClusterResponse] = ..., host_type: Optional[_builtins.str] = ..., instance_name: Optional[_builtins.str] = ..., migration: Optional[outputs.MigrationResponse] = ..., monitoring: Optional[outputs.MonitoringResponse] = ..., service_type: Optional[_builtins.str] = ..., upgrade_locked_until: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alwaysOnRole")
    def always_on_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDefenderStatus")
    def azure_defender_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDefenderStatusLastUpdated")
    def azure_defender_status_last_updated(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerResourceId")
    def container_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbMasterKeyExists")
    def db_master_key_exists(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDigiCertPkiCertTrustConfigured")
    def is_digi_cert_pki_cert_trust_configured(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHadrEnabled")
    def is_hadr_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMicrosoftPkiCertTrustConfigured")
    def is_microsoft_pki_cert_trust_configured(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastInventoryUploadTime")
    def last_inventory_upload_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUsageUploadTime")
    def last_usage_upload_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxServerMemoryMB")
    def max_server_memory_mb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchLevel")
    def patch_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpDynamicPorts")
    def tcp_dynamic_ports(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpStaticPorts")
    def tcp_static_ports(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="traceFlags")
    def trace_flags(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vCore")
    def v_core(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.AuthenticationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPolicy")
    def backup_policy(self) -> Optional[outputs.BackupPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientConnection")
    def client_connection(self) -> Optional[outputs.ClientConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cores(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseMirroringEndpoint")
    def database_mirroring_endpoint(self) -> Optional[outputs.DBMEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverCluster")
    def failover_cluster(self) -> Optional[outputs.FailoverClusterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def migration(self) -> Optional[outputs.MigrationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def monitoring(self) -> Optional[outputs.MonitoringResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeLockedUntil")
    def upgrade_locked_until(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlServerInstanceTelemetryColumnResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlServerLicensePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, activation_state: _builtins.str, billing_plan: _builtins.str, last_activated_at: _builtins.str, last_deactivated_at: _builtins.str, license_category: _builtins.str, physical_cores: _builtins.int, scope_type: _builtins.str, tenant_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingPlan")
    def billing_plan(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastActivatedAt")
    def last_activated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDeactivatedAt")
    def last_deactivated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseCategory")
    def license_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalCores")
    def physical_cores(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TargetReadinessResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_sql_database: Optional[outputs.SkuRecommendationSummaryResponse] = ..., azure_sql_managed_instance: Optional[outputs.SkuRecommendationSummaryResponse] = ..., azure_sql_virtual_machine: Optional[outputs.SkuRecommendationSummaryResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlDatabase")
    def azure_sql_database(self) -> Optional[outputs.SkuRecommendationSummaryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlManagedInstance")
    def azure_sql_managed_instance(self) -> Optional[outputs.SkuRecommendationSummaryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureSqlVirtualMachine")
    def azure_sql_virtual_machine(self) -> Optional[outputs.SkuRecommendationSummaryResponse]:
        
        ...
    


@pulumi.output_type
class UploadServicePrincipalResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authority: Optional[_builtins.str] = ..., client_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UploadWatermarkResponse(dict):
    
    def __init__(__self__, *, logs: Optional[_builtins.str] = ..., metrics: Optional[_builtins.str] = ..., usages: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def usages(self) -> Optional[_builtins.str]:
        
        ...
    


