

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceAutomatedBackupConfig', ..., ..., 'InstanceCrossInstanceReplicationConfig', 'InstanceCrossInstanceReplicationConfigMembership', ..., ..., ..., ..., 'InstanceDesiredAutoCreatedEndpoint', 'InstanceDesiredPscAutoConnection', ..., ..., ..., 'InstanceDiscoveryEndpoint', 'InstanceEndpoint', 'InstanceEndpointConnection', 'InstanceEndpointConnectionPscAutoConnection', 'InstanceGcsSource', 'InstanceMaintenancePolicy', 'InstanceMaintenancePolicyWeeklyMaintenanceWindow', ..., 'InstanceMaintenanceSchedule', 'InstanceManagedBackupSource', 'InstanceManagedServerCa', 'InstanceManagedServerCaCaCert', 'InstanceNodeConfig', 'InstancePersistenceConfig', 'InstancePersistenceConfigAofConfig', 'InstancePersistenceConfigRdbConfig', 'InstancePscAttachmentDetail', 'InstancePscAutoConnection', 'InstanceStateInfo', 'InstanceStateInfoUpdateInfo', 'InstanceZoneDistributionConfig', 'GetInstanceAutomatedBackupConfigResult', ..., ..., 'GetInstanceCrossInstanceReplicationConfigResult', ..., ..., ..., ..., ..., 'GetInstanceDesiredAutoCreatedEndpointResult', 'GetInstanceDesiredPscAutoConnectionResult', 'GetInstanceDiscoveryEndpointResult', 'GetInstanceEndpointResult', 'GetInstanceEndpointConnectionResult', ..., 'GetInstanceGcsSourceResult', 'GetInstanceMaintenancePolicyResult', ..., ..., 'GetInstanceMaintenanceScheduleResult', 'GetInstanceManagedBackupSourceResult', 'GetInstanceManagedServerCaResult', 'GetInstanceManagedServerCaCaCertResult', 'GetInstanceNodeConfigResult', 'GetInstancePersistenceConfigResult', 'GetInstancePersistenceConfigAofConfigResult', 'GetInstancePersistenceConfigRdbConfigResult', 'GetInstancePscAttachmentDetailResult', 'GetInstancePscAutoConnectionResult', 'GetInstanceStateInfoResult', 'GetInstanceStateInfoUpdateInfoResult', 'GetInstanceZoneDistributionConfigResult']
@pulumi.output_type
class InstanceAutomatedBackupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fixed_frequency_schedule: outputs.InstanceAutomatedBackupConfigFixedFrequencySchedule, retention: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedFrequencySchedule")
    def fixed_frequency_schedule(self) -> outputs.InstanceAutomatedBackupConfigFixedFrequencySchedule:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceAutomatedBackupConfigFixedFrequencySchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_time: outputs.InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTime) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTime:
        
        ...
    


@pulumi.output_type
class InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTime(dict):
    def __init__(__self__, *, hours: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InstanceCrossInstanceReplicationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_role: Optional[_builtins.str] = ..., memberships: Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigMembership]] = ..., primary_instance: Optional[outputs.InstanceCrossInstanceReplicationConfigPrimaryInstance] = ..., secondary_instances: Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigSecondaryInstance]] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memberships(self) -> Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigMembership]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryInstance")
    def primary_instance(self) -> Optional[outputs.InstanceCrossInstanceReplicationConfigPrimaryInstance]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInstances")
    def secondary_instances(self) -> Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigSecondaryInstance]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceCrossInstanceReplicationConfigMembership(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, primary_instances: Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigMembershipPrimaryInstance]] = ..., secondary_instances: Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigMembershipSecondaryInstance]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryInstances")
    def primary_instances(self) -> Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigMembershipPrimaryInstance]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInstances")
    def secondary_instances(self) -> Optional[Sequence[outputs.InstanceCrossInstanceReplicationConfigMembershipSecondaryInstance]]:
        
        ...
    


@pulumi.output_type
class InstanceCrossInstanceReplicationConfigMembershipPrimaryInstance(dict):
    def __init__(__self__, *, instance: Optional[_builtins.str] = ..., uid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceCrossInstanceReplicationConfigMembershipSecondaryInstance(dict):
    def __init__(__self__, *, instance: Optional[_builtins.str] = ..., uid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceCrossInstanceReplicationConfigPrimaryInstance(dict):
    def __init__(__self__, *, instance: Optional[_builtins.str] = ..., uid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceCrossInstanceReplicationConfigSecondaryInstance(dict):
    def __init__(__self__, *, instance: Optional[_builtins.str] = ..., uid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceDesiredAutoCreatedEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network: _builtins.str, project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceDesiredPscAutoConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network: _builtins.str, project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpoint(dict):
    def __init__(__self__, *, connections: Optional[Sequence[outputs.InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnection]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connections(self) -> Optional[Sequence[outputs.InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnection]]:
        
        ...
    


@pulumi.output_type
class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, psc_connection: Optional[outputs.InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnection] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnection")
    def psc_connection(self) -> Optional[outputs.InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnection]:
        
        ...
    


@pulumi.output_type
class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, forwarding_rule: _builtins.str, ip_address: _builtins.str, network: _builtins.str, psc_connection_id: _builtins.str, service_attachment: _builtins.str, connection_type: Optional[_builtins.str] = ..., project_id: Optional[_builtins.str] = ..., psc_connection_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceDiscoveryEndpoint(dict):
    def __init__(__self__, *, address: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceEndpoint(dict):
    def __init__(__self__, *, connections: Optional[Sequence[outputs.InstanceEndpointConnection]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connections(self) -> Optional[Sequence[outputs.InstanceEndpointConnection]]:
        
        ...
    


@pulumi.output_type
class InstanceEndpointConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, psc_auto_connection: Optional[outputs.InstanceEndpointConnectionPscAutoConnection] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAutoConnection")
    def psc_auto_connection(self) -> Optional[outputs.InstanceEndpointConnectionPscAutoConnection]:
        
        ...
    


@pulumi.output_type
class InstanceEndpointConnectionPscAutoConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_type: Optional[_builtins.str] = ..., forwarding_rule: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., project_id: Optional[_builtins.str] = ..., psc_connection_id: Optional[_builtins.str] = ..., service_attachment: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceGcsSource(dict):
    def __init__(__self__, *, uris: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceMaintenancePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_time: Optional[_builtins.str] = ..., update_time: Optional[_builtins.str] = ..., weekly_maintenance_windows: Optional[Sequence[outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(self) -> Optional[Sequence[outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindow]]:
        
        ...
    


@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, day: _builtins.str, start_time: outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime, duration: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTime(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceMaintenanceSchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_time: Optional[_builtins.str] = ..., schedule_deadline_time: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceManagedBackupSource(dict):
    def __init__(__self__, *, backup: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backup(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceManagedServerCa(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_certs: Optional[Sequence[outputs.InstanceManagedServerCaCaCert]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Optional[Sequence[outputs.InstanceManagedServerCaCaCert]]:
        
        ...
    


@pulumi.output_type
class InstanceManagedServerCaCaCert(dict):
    def __init__(__self__, *, certificates: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class InstanceNodeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, size_gb: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class InstancePersistenceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aof_config: Optional[outputs.InstancePersistenceConfigAofConfig] = ..., mode: Optional[_builtins.str] = ..., rdb_config: Optional[outputs.InstancePersistenceConfigRdbConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aofConfig")
    def aof_config(self) -> Optional[outputs.InstancePersistenceConfigAofConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbConfig")
    def rdb_config(self) -> Optional[outputs.InstancePersistenceConfigRdbConfig]:
        
        ...
    


@pulumi.output_type
class InstancePersistenceConfigAofConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, append_fsync: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appendFsync")
    def append_fsync(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstancePersistenceConfigRdbConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rdb_snapshot_period: Optional[_builtins.str] = ..., rdb_snapshot_start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstancePscAttachmentDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_type: Optional[_builtins.str] = ..., service_attachment: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstancePscAutoConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_type: Optional[_builtins.str] = ..., forwarding_rule: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., network: Optional[_builtins.str] = ..., port: Optional[_builtins.int] = ..., project_id: Optional[_builtins.str] = ..., psc_connection_id: Optional[_builtins.str] = ..., psc_connection_status: Optional[_builtins.str] = ..., service_attachment: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceStateInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, update_infos: Optional[Sequence[outputs.InstanceStateInfoUpdateInfo]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateInfos")
    def update_infos(self) -> Optional[Sequence[outputs.InstanceStateInfoUpdateInfo]]:
        
        ...
    


@pulumi.output_type
class InstanceStateInfoUpdateInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_engine_version: Optional[_builtins.str] = ..., target_node_type: Optional[_builtins.str] = ..., target_replica_count: Optional[_builtins.int] = ..., target_shard_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEngineVersion")
    def target_engine_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNodeType")
    def target_node_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReplicaCount")
    def target_replica_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetShardCount")
    def target_shard_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class InstanceZoneDistributionConfig(dict):
    def __init__(__self__, *, mode: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstanceAutomatedBackupConfigResult(dict):
    def __init__(__self__, *, fixed_frequency_schedules: Sequence[outputs.GetInstanceAutomatedBackupConfigFixedFrequencyScheduleResult], retention: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedFrequencySchedules")
    def fixed_frequency_schedules(self) -> Sequence[outputs.GetInstanceAutomatedBackupConfigFixedFrequencyScheduleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceAutomatedBackupConfigFixedFrequencyScheduleResult(dict):
    def __init__(__self__, *, start_times: Sequence[outputs.GetInstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(self) -> Sequence[outputs.GetInstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetInstanceCrossInstanceReplicationConfigResult(dict):
    def __init__(__self__, *, instance_role: _builtins.str, memberships: Sequence[outputs.GetInstanceCrossInstanceReplicationConfigMembershipResult], primary_instances: Sequence[outputs.GetInstanceCrossInstanceReplicationConfigPrimaryInstanceResult], secondary_instances: Sequence[outputs.GetInstanceCrossInstanceReplicationConfigSecondaryInstanceResult], update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memberships(self) -> Sequence[outputs.GetInstanceCrossInstanceReplicationConfigMembershipResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryInstances")
    def primary_instances(self) -> Sequence[outputs.GetInstanceCrossInstanceReplicationConfigPrimaryInstanceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInstances")
    def secondary_instances(self) -> Sequence[outputs.GetInstanceCrossInstanceReplicationConfigSecondaryInstanceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceCrossInstanceReplicationConfigMembershipResult(dict):
    def __init__(__self__, *, primary_instances: Sequence[outputs.GetInstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceResult], secondary_instances: Sequence[outputs.GetInstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryInstances")
    def primary_instances(self) -> Sequence[outputs.GetInstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryInstances")
    def secondary_instances(self) -> Sequence[outputs.GetInstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceResult(dict):
    def __init__(__self__, *, instance: _builtins.str, uid: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceResult(dict):
    def __init__(__self__, *, instance: _builtins.str, uid: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceCrossInstanceReplicationConfigPrimaryInstanceResult(dict):
    def __init__(__self__, *, instance: _builtins.str, uid: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceCrossInstanceReplicationConfigSecondaryInstanceResult(dict):
    def __init__(__self__, *, instance: _builtins.str, uid: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceDesiredAutoCreatedEndpointResult(dict):
    def __init__(__self__, *, network: _builtins.str, project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceDesiredPscAutoConnectionResult(dict):
    def __init__(__self__, *, network: _builtins.str, project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceDiscoveryEndpointResult(dict):
    def __init__(__self__, *, address: _builtins.str, network: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetInstanceEndpointResult(dict):
    def __init__(__self__, *, connections: Sequence[outputs.GetInstanceEndpointConnectionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connections(self) -> Sequence[outputs.GetInstanceEndpointConnectionResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceEndpointConnectionResult(dict):
    def __init__(__self__, *, psc_auto_connections: Sequence[outputs.GetInstanceEndpointConnectionPscAutoConnectionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(self) -> Sequence[outputs.GetInstanceEndpointConnectionPscAutoConnectionResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceEndpointConnectionPscAutoConnectionResult(dict):
    def __init__(__self__, *, connection_type: _builtins.str, forwarding_rule: _builtins.str, ip_address: _builtins.str, network: _builtins.str, port: _builtins.int, project_id: _builtins.str, psc_connection_id: _builtins.str, service_attachment: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceGcsSourceResult(dict):
    def __init__(__self__, *, uris: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uris(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstanceMaintenancePolicyResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, update_time: _builtins.str, weekly_maintenance_windows: Sequence[outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(self) -> Sequence[outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceMaintenancePolicyWeeklyMaintenanceWindowResult(dict):
    def __init__(__self__, *, day: _builtins.str, duration: _builtins.str, start_times: Sequence[outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(self) -> Sequence[outputs.GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeResult(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int, nanos: _builtins.int, seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetInstanceMaintenanceScheduleResult(dict):
    def __init__(__self__, *, end_time: _builtins.str, schedule_deadline_time: _builtins.str, start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceManagedBackupSourceResult(dict):
    def __init__(__self__, *, backup: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backup(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceManagedServerCaResult(dict):
    def __init__(__self__, *, ca_certs: Sequence[outputs.GetInstanceManagedServerCaCaCertResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Sequence[outputs.GetInstanceManagedServerCaCaCertResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceManagedServerCaCaCertResult(dict):
    def __init__(__self__, *, certificates: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInstanceNodeConfigResult(dict):
    def __init__(__self__, *, size_gb: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetInstancePersistenceConfigResult(dict):
    def __init__(__self__, *, aof_configs: Sequence[outputs.GetInstancePersistenceConfigAofConfigResult], mode: _builtins.str, rdb_configs: Sequence[outputs.GetInstancePersistenceConfigRdbConfigResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aofConfigs")
    def aof_configs(self) -> Sequence[outputs.GetInstancePersistenceConfigAofConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbConfigs")
    def rdb_configs(self) -> Sequence[outputs.GetInstancePersistenceConfigRdbConfigResult]:
        
        ...
    


@pulumi.output_type
class GetInstancePersistenceConfigAofConfigResult(dict):
    def __init__(__self__, *, append_fsync: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appendFsync")
    def append_fsync(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstancePersistenceConfigRdbConfigResult(dict):
    def __init__(__self__, *, rdb_snapshot_period: _builtins.str, rdb_snapshot_start_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstancePscAttachmentDetailResult(dict):
    def __init__(__self__, *, connection_type: _builtins.str, service_attachment: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstancePscAutoConnectionResult(dict):
    def __init__(__self__, *, connection_type: _builtins.str, forwarding_rule: _builtins.str, ip_address: _builtins.str, network: _builtins.str, port: _builtins.int, project_id: _builtins.str, psc_connection_id: _builtins.str, psc_connection_status: _builtins.str, service_attachment: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInstanceStateInfoResult(dict):
    def __init__(__self__, *, update_infos: Sequence[outputs.GetInstanceStateInfoUpdateInfoResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateInfos")
    def update_infos(self) -> Sequence[outputs.GetInstanceStateInfoUpdateInfoResult]:
        
        ...
    


@pulumi.output_type
class GetInstanceStateInfoUpdateInfoResult(dict):
    def __init__(__self__, *, target_engine_version: _builtins.str, target_node_type: _builtins.str, target_replica_count: _builtins.int, target_shard_count: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEngineVersion")
    def target_engine_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNodeType")
    def target_node_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReplicaCount")
    def target_replica_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetShardCount")
    def target_shard_count(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetInstanceZoneDistributionConfigResult(dict):
    def __init__(__self__, *, mode: _builtins.str, zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


