

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterAutomatedBackupConfigArgs', 'ClusterAutomatedBackupConfigArgsDict', ..., ..., ..., ..., 'ClusterCrossClusterReplicationConfigArgs', 'ClusterCrossClusterReplicationConfigArgsDict', 'ClusterCrossClusterReplicationConfigMembershipArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ClusterDiscoveryEndpointArgs', 'ClusterDiscoveryEndpointArgsDict', 'ClusterDiscoveryEndpointPscConfigArgs', 'ClusterDiscoveryEndpointPscConfigArgsDict', 'ClusterGcsSourceArgs', 'ClusterGcsSourceArgsDict', 'ClusterMaintenancePolicyArgs', 'ClusterMaintenancePolicyArgsDict', ..., ..., ..., ..., 'ClusterMaintenanceScheduleArgs', 'ClusterMaintenanceScheduleArgsDict', 'ClusterManagedBackupSourceArgs', 'ClusterManagedBackupSourceArgsDict', 'ClusterManagedServerCaArgs', 'ClusterManagedServerCaArgsDict', 'ClusterManagedServerCaCaCertArgs', 'ClusterManagedServerCaCaCertArgsDict', 'ClusterPersistenceConfigArgs', 'ClusterPersistenceConfigArgsDict', 'ClusterPersistenceConfigAofConfigArgs', 'ClusterPersistenceConfigAofConfigArgsDict', 'ClusterPersistenceConfigRdbConfigArgs', 'ClusterPersistenceConfigRdbConfigArgsDict', 'ClusterPscConfigArgs', 'ClusterPscConfigArgsDict', 'ClusterPscConnectionArgs', 'ClusterPscConnectionArgsDict', 'ClusterPscServiceAttachmentArgs', 'ClusterPscServiceAttachmentArgsDict', 'ClusterStateInfoArgs', 'ClusterStateInfoArgsDict', 'ClusterStateInfoUpdateInfoArgs', 'ClusterStateInfoUpdateInfoArgsDict', 'ClusterUserCreatedConnectionsClusterEndpointArgs', ..., ..., ..., ..., ..., 'ClusterZoneDistributionConfigArgs', 'ClusterZoneDistributionConfigArgsDict', 'InstanceMaintenancePolicyArgs', 'InstanceMaintenancePolicyArgsDict', ..., ..., ..., ..., 'InstanceMaintenanceScheduleArgs', 'InstanceMaintenanceScheduleArgsDict', 'InstanceNodeArgs', 'InstanceNodeArgsDict', 'InstancePersistenceConfigArgs', 'InstancePersistenceConfigArgsDict', 'InstanceServerCaCertArgs', 'InstanceServerCaCertArgsDict']
class ClusterAutomatedBackupConfigArgsDict(TypedDict):
    fixed_frequency_schedule: pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleArgsDict]
    retention: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClusterAutomatedBackupConfigArgs:
    def __init__(__self__, *, fixed_frequency_schedule: pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleArgs], retention: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedFrequencySchedule")
    def fixed_frequency_schedule(self) -> pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleArgs]:
        
        ...
    
    @fixed_frequency_schedule.setter
    def fixed_frequency_schedule(self, value: pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @retention.setter
    def retention(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClusterAutomatedBackupConfigFixedFrequencyScheduleArgsDict(TypedDict):
    start_time: pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgsDict]


@pulumi.input_type
class ClusterAutomatedBackupConfigFixedFrequencyScheduleArgs:
    def __init__(__self__, *, start_time: pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: pulumi.Input[ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs]): # -> None:
        ...
    


class ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgsDict(TypedDict):
    hours: pulumi.Input[_builtins.int]


@pulumi.input_type
class ClusterAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs:
    def __init__(__self__, *, hours: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @hours.setter
    def hours(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class ClusterCrossClusterReplicationConfigArgsDict(TypedDict):
    cluster_role: NotRequired[pulumi.Input[_builtins.str]]
    memberships: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipArgsDict]]]]
    primary_cluster: NotRequired[pulumi.Input[ClusterCrossClusterReplicationConfigPrimaryClusterArgsDict]]
    secondary_clusters: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigSecondaryClusterArgsDict]]]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterCrossClusterReplicationConfigArgs:
    def __init__(__self__, *, cluster_role: Optional[pulumi.Input[_builtins.str]] = ..., memberships: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipArgs]]]] = ..., primary_cluster: Optional[pulumi.Input[ClusterCrossClusterReplicationConfigPrimaryClusterArgs]] = ..., secondary_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigSecondaryClusterArgs]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterRole")
    def cluster_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_role.setter
    def cluster_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memberships(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipArgs]]]]:
        
        ...
    
    @memberships.setter
    def memberships(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryCluster")
    def primary_cluster(self) -> Optional[pulumi.Input[ClusterCrossClusterReplicationConfigPrimaryClusterArgs]]:
        
        ...
    
    @primary_cluster.setter
    def primary_cluster(self, value: Optional[pulumi.Input[ClusterCrossClusterReplicationConfigPrimaryClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryClusters")
    def secondary_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigSecondaryClusterArgs]]]]:
        
        ...
    
    @secondary_clusters.setter
    def secondary_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigSecondaryClusterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterCrossClusterReplicationConfigMembershipArgsDict(TypedDict):
    primary_clusters: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipPrimaryClusterArgsDict]]]]
    secondary_clusters: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipSecondaryClusterArgsDict]]]]


@pulumi.input_type
class ClusterCrossClusterReplicationConfigMembershipArgs:
    def __init__(__self__, *, primary_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipPrimaryClusterArgs]]]] = ..., secondary_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipSecondaryClusterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryClusters")
    def primary_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipPrimaryClusterArgs]]]]:
        
        ...
    
    @primary_clusters.setter
    def primary_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipPrimaryClusterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryClusters")
    def secondary_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipSecondaryClusterArgs]]]]:
        
        ...
    
    @secondary_clusters.setter
    def secondary_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCrossClusterReplicationConfigMembershipSecondaryClusterArgs]]]]): # -> None:
        ...
    


class ClusterCrossClusterReplicationConfigMembershipPrimaryClusterArgsDict(TypedDict):
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterCrossClusterReplicationConfigMembershipPrimaryClusterArgs:
    def __init__(__self__, *, cluster: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterCrossClusterReplicationConfigMembershipSecondaryClusterArgsDict(TypedDict):
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterCrossClusterReplicationConfigMembershipSecondaryClusterArgs:
    def __init__(__self__, *, cluster: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterCrossClusterReplicationConfigPrimaryClusterArgsDict(TypedDict):
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterCrossClusterReplicationConfigPrimaryClusterArgs:
    def __init__(__self__, *, cluster: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterCrossClusterReplicationConfigSecondaryClusterArgsDict(TypedDict):
    cluster: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterCrossClusterReplicationConfigSecondaryClusterArgs:
    def __init__(__self__, *, cluster: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterDiscoveryEndpointArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    psc_config: NotRequired[pulumi.Input[ClusterDiscoveryEndpointPscConfigArgsDict]]


@pulumi.input_type
class ClusterDiscoveryEndpointArgs:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., psc_config: Optional[pulumi.Input[ClusterDiscoveryEndpointPscConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfig")
    def psc_config(self) -> Optional[pulumi.Input[ClusterDiscoveryEndpointPscConfigArgs]]:
        
        ...
    
    @psc_config.setter
    def psc_config(self, value: Optional[pulumi.Input[ClusterDiscoveryEndpointPscConfigArgs]]): # -> None:
        ...
    


class ClusterDiscoveryEndpointPscConfigArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterDiscoveryEndpointPscConfigArgs:
    def __init__(__self__, *, network: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterGcsSourceArgsDict(TypedDict):
    uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ClusterGcsSourceArgs:
    def __init__(__self__, *, uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uris(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @uris.setter
    def uris(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ClusterMaintenancePolicyArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    weekly_maintenance_windows: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowArgsDict]]]]


@pulumi.input_type
class ClusterMaintenancePolicyArgs:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., weekly_maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowArgs]]]]:
        
        ...
    
    @weekly_maintenance_windows.setter
    def weekly_maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowArgs]]]]): # -> None:
        ...
    


class ClusterMaintenancePolicyWeeklyMaintenanceWindowArgsDict(TypedDict):
    day: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict]
    duration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterMaintenancePolicyWeeklyMaintenanceWindowArgs:
    def __init__(__self__, *, day: pulumi.Input[_builtins.str], start_time: pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs], duration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @day.setter
    def day(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: pulumi.Input[ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ClusterMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs:
    def __init__(__self__, *, hours: Optional[pulumi.Input[_builtins.int]] = ..., minutes: Optional[pulumi.Input[_builtins.int]] = ..., nanos: Optional[pulumi.Input[_builtins.int]] = ..., seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ClusterMaintenanceScheduleArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    schedule_deadline_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterMaintenanceScheduleArgs:
    def __init__(__self__, *, end_time: Optional[pulumi.Input[_builtins.str]] = ..., schedule_deadline_time: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_deadline_time.setter
    def schedule_deadline_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterManagedBackupSourceArgsDict(TypedDict):
    backup: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClusterManagedBackupSourceArgs:
    def __init__(__self__, *, backup: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def backup(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup.setter
    def backup(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClusterManagedServerCaArgsDict(TypedDict):
    ca_certs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterManagedServerCaCaCertArgsDict]]]]


@pulumi.input_type
class ClusterManagedServerCaArgs:
    def __init__(__self__, *, ca_certs: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterManagedServerCaCaCertArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterManagedServerCaCaCertArgs]]]]:
        
        ...
    
    @ca_certs.setter
    def ca_certs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterManagedServerCaCaCertArgs]]]]): # -> None:
        ...
    


class ClusterManagedServerCaCaCertArgsDict(TypedDict):
    certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ClusterManagedServerCaCaCertArgs:
    def __init__(__self__, *, certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @certificates.setter
    def certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ClusterPersistenceConfigArgsDict(TypedDict):
    aof_config: NotRequired[pulumi.Input[ClusterPersistenceConfigAofConfigArgsDict]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    rdb_config: NotRequired[pulumi.Input[ClusterPersistenceConfigRdbConfigArgsDict]]


@pulumi.input_type
class ClusterPersistenceConfigArgs:
    def __init__(__self__, *, aof_config: Optional[pulumi.Input[ClusterPersistenceConfigAofConfigArgs]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., rdb_config: Optional[pulumi.Input[ClusterPersistenceConfigRdbConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aofConfig")
    def aof_config(self) -> Optional[pulumi.Input[ClusterPersistenceConfigAofConfigArgs]]:
        
        ...
    
    @aof_config.setter
    def aof_config(self, value: Optional[pulumi.Input[ClusterPersistenceConfigAofConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbConfig")
    def rdb_config(self) -> Optional[pulumi.Input[ClusterPersistenceConfigRdbConfigArgs]]:
        
        ...
    
    @rdb_config.setter
    def rdb_config(self, value: Optional[pulumi.Input[ClusterPersistenceConfigRdbConfigArgs]]): # -> None:
        ...
    


class ClusterPersistenceConfigAofConfigArgsDict(TypedDict):
    append_fsync: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterPersistenceConfigAofConfigArgs:
    def __init__(__self__, *, append_fsync: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appendFsync")
    def append_fsync(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @append_fsync.setter
    def append_fsync(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterPersistenceConfigRdbConfigArgsDict(TypedDict):
    rdb_snapshot_period: NotRequired[pulumi.Input[_builtins.str]]
    rdb_snapshot_start_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterPersistenceConfigRdbConfigArgs:
    def __init__(__self__, *, rdb_snapshot_period: Optional[pulumi.Input[_builtins.str]] = ..., rdb_snapshot_start_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rdb_snapshot_period.setter
    def rdb_snapshot_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rdb_snapshot_start_time.setter
    def rdb_snapshot_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterPscConfigArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClusterPscConfigArgs:
    def __init__(__self__, *, network: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClusterPscConnectionArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_rule: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    psc_connection_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterPscConnectionArgs:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ..., forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., project_id: Optional[pulumi.Input[_builtins.str]] = ..., psc_connection_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @forwarding_rule.setter
    def forwarding_rule(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @psc_connection_id.setter
    def psc_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterPscServiceAttachmentArgsDict(TypedDict):
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterPscServiceAttachmentArgs:
    def __init__(__self__, *, connection_type: Optional[pulumi.Input[_builtins.str]] = ..., service_attachment: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterStateInfoArgsDict(TypedDict):
    update_info: NotRequired[pulumi.Input[ClusterStateInfoUpdateInfoArgsDict]]


@pulumi.input_type
class ClusterStateInfoArgs:
    def __init__(__self__, *, update_info: Optional[pulumi.Input[ClusterStateInfoUpdateInfoArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateInfo")
    def update_info(self) -> Optional[pulumi.Input[ClusterStateInfoUpdateInfoArgs]]:
        
        ...
    
    @update_info.setter
    def update_info(self, value: Optional[pulumi.Input[ClusterStateInfoUpdateInfoArgs]]): # -> None:
        ...
    


class ClusterStateInfoUpdateInfoArgsDict(TypedDict):
    target_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    target_shard_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ClusterStateInfoUpdateInfoArgs:
    def __init__(__self__, *, target_replica_count: Optional[pulumi.Input[_builtins.int]] = ..., target_shard_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetReplicaCount")
    def target_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_replica_count.setter
    def target_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetShardCount")
    def target_shard_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_shard_count.setter
    def target_shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ClusterUserCreatedConnectionsClusterEndpointArgsDict(TypedDict):
    connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionArgsDict]]]]


@pulumi.input_type
class ClusterUserCreatedConnectionsClusterEndpointArgs:
    def __init__(__self__, *, connections: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionArgs]]]]:
        
        ...
    
    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionArgs]]]]): # -> None:
        ...
    


class ClusterUserCreatedConnectionsClusterEndpointConnectionArgsDict(TypedDict):
    psc_connection: NotRequired[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnectionArgsDict]]


@pulumi.input_type
class ClusterUserCreatedConnectionsClusterEndpointConnectionArgs:
    def __init__(__self__, *, psc_connection: Optional[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnectionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnection")
    def psc_connection(self) -> Optional[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnectionArgs]]:
        
        ...
    
    @psc_connection.setter
    def psc_connection(self, value: Optional[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnectionArgs]]): # -> None:
        ...
    


class ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnectionArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    forwarding_rule: pulumi.Input[_builtins.str]
    network: pulumi.Input[_builtins.str]
    psc_connection_id: pulumi.Input[_builtins.str]
    service_attachment: pulumi.Input[_builtins.str]
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    psc_connection_status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterUserCreatedConnectionsClusterEndpointConnectionPscConnectionArgs:
    def __init__(__self__, *, address: pulumi.Input[_builtins.str], forwarding_rule: pulumi.Input[_builtins.str], network: pulumi.Input[_builtins.str], psc_connection_id: pulumi.Input[_builtins.str], service_attachment: pulumi.Input[_builtins.str], connection_type: Optional[pulumi.Input[_builtins.str]] = ..., project_id: Optional[pulumi.Input[_builtins.str]] = ..., psc_connection_status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @forwarding_rule.setter
    def forwarding_rule(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @psc_connection_id.setter
    def psc_connection_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_attachment.setter
    def service_attachment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @psc_connection_status.setter
    def psc_connection_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClusterZoneDistributionConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterZoneDistributionConfigArgs:
    def __init__(__self__, *, mode: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceMaintenancePolicyArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    weekly_maintenance_windows: NotRequired[pulumi.Input[Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgsDict]]]]


@pulumi.input_type
class InstanceMaintenancePolicyArgs:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., weekly_maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]]]]:
        
        ...
    
    @weekly_maintenance_windows.setter
    def weekly_maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]]]]): # -> None:
        ...
    


class InstanceMaintenancePolicyWeeklyMaintenanceWindowArgsDict(TypedDict):
    day: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict]
    duration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs:
    def __init__(__self__, *, day: pulumi.Input[_builtins.str], start_time: pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs], duration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @day.setter
    def day(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs:
    def __init__(__self__, *, hours: Optional[pulumi.Input[_builtins.int]] = ..., minutes: Optional[pulumi.Input[_builtins.int]] = ..., nanos: Optional[pulumi.Input[_builtins.int]] = ..., seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class InstanceMaintenanceScheduleArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    schedule_deadline_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceMaintenanceScheduleArgs:
    def __init__(__self__, *, end_time: Optional[pulumi.Input[_builtins.str]] = ..., schedule_deadline_time: Optional[pulumi.Input[_builtins.str]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_deadline_time.setter
    def schedule_deadline_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceNodeArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceNodeArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstancePersistenceConfigArgsDict(TypedDict):
    persistence_mode: NotRequired[pulumi.Input[_builtins.str]]
    rdb_next_snapshot_time: NotRequired[pulumi.Input[_builtins.str]]
    rdb_snapshot_period: NotRequired[pulumi.Input[_builtins.str]]
    rdb_snapshot_start_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstancePersistenceConfigArgs:
    def __init__(__self__, *, persistence_mode: Optional[pulumi.Input[_builtins.str]] = ..., rdb_next_snapshot_time: Optional[pulumi.Input[_builtins.str]] = ..., rdb_snapshot_period: Optional[pulumi.Input[_builtins.str]] = ..., rdb_snapshot_start_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceMode")
    def persistence_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @persistence_mode.setter
    def persistence_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbNextSnapshotTime")
    def rdb_next_snapshot_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rdb_next_snapshot_time.setter
    def rdb_next_snapshot_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rdb_snapshot_period.setter
    def rdb_snapshot_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rdb_snapshot_start_time.setter
    def rdb_snapshot_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceServerCaCertArgsDict(TypedDict):
    cert: NotRequired[pulumi.Input[_builtins.str]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    expire_time: NotRequired[pulumi.Input[_builtins.str]]
    serial_number: NotRequired[pulumi.Input[_builtins.str]]
    sha1_fingerprint: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InstanceServerCaCertArgs:
    def __init__(__self__, *, cert: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., expire_time: Optional[pulumi.Input[_builtins.str]] = ..., serial_number: Optional[pulumi.Input[_builtins.str]] = ..., sha1_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sha1_fingerprint.setter
    def sha1_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


