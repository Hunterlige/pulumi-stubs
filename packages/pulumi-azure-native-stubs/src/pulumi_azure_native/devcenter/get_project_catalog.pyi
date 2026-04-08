import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProjectCatalogResult",
    "AwaitableGetProjectCatalogResult",
    "get_project_catalog",
    "get_project_catalog_output",
]

@pulumi.output_type
class GetProjectCatalogResult:
    def __init__(
        __self__,
        ado_git=...,
        azure_api_version=...,
        connection_state=...,
        git_hub=...,
        id=...,
        last_connection_time=...,
        last_sync_stats=...,
        last_sync_time=...,
        name=...,
        provisioning_state=...,
        sync_state=...,
        sync_type=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> Optional[outputs.GitCatalogResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional[outputs.GitCatalogResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastConnectionTime")
    def last_connection_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastSyncStats")
    def last_sync_stats(self) -> outputs.SyncStatsResponse: ...
    @_builtins.property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncType")
    def sync_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetProjectCatalogResult(GetProjectCatalogResult):
    def __await__(self): ...

def get_project_catalog(
    catalog_name: Optional[_builtins.str] = ...,
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProjectCatalogResult: ...
def get_project_catalog_output(
    catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProjectCatalogResult]: ...
