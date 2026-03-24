

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMetastoreServiceResult', 'AwaitableGetMetastoreServiceResult', 'get_metastore_service', 'get_metastore_service_output']
@pulumi.output_type
class GetMetastoreServiceResult:
    
    def __init__(__self__, artifact_gcs_uri=..., create_time=..., database_type=..., deletion_protection=..., effective_labels=..., encryption_configs=..., endpoint_uri=..., hive_metastore_configs=..., id=..., labels=..., location=..., maintenance_windows=..., metadata_integrations=..., name=..., network=..., network_configs=..., port=..., project=..., pulumi_labels=..., release_channel=..., scaling_configs=..., scheduled_backups=..., service_id=..., state=..., state_message=..., tags=..., telemetry_configs=..., tier=..., uid=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactGcsUri")
    def artifact_gcs_uri(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigs")
    def encryption_configs(self) -> Sequence[outputs.GetMetastoreServiceEncryptionConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiveMetastoreConfigs")
    def hive_metastore_configs(self) -> Sequence[outputs.GetMetastoreServiceHiveMetastoreConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence[outputs.GetMetastoreServiceMaintenanceWindowResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataIntegrations")
    def metadata_integrations(self) -> Sequence[outputs.GetMetastoreServiceMetadataIntegrationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(self) -> Sequence[outputs.GetMetastoreServiceNetworkConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseChannel")
    def release_channel(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingConfigs")
    def scaling_configs(self) -> Sequence[outputs.GetMetastoreServiceScalingConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledBackups")
    def scheduled_backups(self) -> Sequence[outputs.GetMetastoreServiceScheduledBackupResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telemetryConfigs")
    def telemetry_configs(self) -> Sequence[outputs.GetMetastoreServiceTelemetryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetMetastoreServiceResult(GetMetastoreServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetMetastoreServiceResult]:
        ...
    


def get_metastore_service(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., service_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMetastoreServiceResult:
    
    ...

def get_metastore_service_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMetastoreServiceResult]:
    
    ...

