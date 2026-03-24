

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDataSourceResult', 'AwaitableGetDataSourceResult', 'get_data_source', 'get_data_source_output']
@pulumi.output_type
class GetDataSourceResult:
    
    def __init__(__self__, backup_config_infos=..., backup_count=..., backup_vault_id=..., config_state=..., create_time=..., data_source_backup_appliance_applications=..., data_source_gcp_resources=..., data_source_id=..., etag=..., id=..., labels=..., location=..., name=..., project=..., state=..., total_stored_bytes=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfigInfos")
    def backup_config_infos(self) -> Sequence[outputs.GetDataSourceBackupConfigInfoResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCount")
    def backup_count(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupVaultId")
    def backup_vault_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configState")
    def config_state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceBackupApplianceApplications")
    def data_source_backup_appliance_applications(self) -> Sequence[outputs.GetDataSourceDataSourceBackupApplianceApplicationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceGcpResources")
    def data_source_gcp_resources(self) -> Sequence[outputs.GetDataSourceDataSourceGcpResourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
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
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalStoredBytes")
    def total_stored_bytes(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetDataSourceResult(GetDataSourceResult):
    def __await__(self): # -> Generator[Never, Any, GetDataSourceResult]:
        ...
    


def get_data_source(backup_vault_id: Optional[_builtins.str] = ..., data_source_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDataSourceResult:
    
    ...

def get_data_source_output(backup_vault_id: Optional[pulumi.Input[_builtins.str]] = ..., data_source_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDataSourceResult]:
    
    ...

