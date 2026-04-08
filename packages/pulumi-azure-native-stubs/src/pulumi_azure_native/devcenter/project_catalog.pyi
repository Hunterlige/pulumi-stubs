import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProjectCatalogArgs", "ProjectCatalog"]

@pulumi.input_type
class ProjectCatalogArgs:
    def __init__(
        __self__,
        *,
        project_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        ado_git: Optional[pulumi.Input[GitCatalogArgs]] = ...,
        catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub: Optional[pulumi.Input[GitCatalogArgs]] = ...,
        sync_type: Optional[pulumi.Input[Union[_builtins.str, CatalogSyncType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> Optional[pulumi.Input[GitCatalogArgs]]: ...
    @ado_git.setter
    def ado_git(self, value: Optional[pulumi.Input[GitCatalogArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog_name.setter
    def catalog_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional[pulumi.Input[GitCatalogArgs]]: ...
    @git_hub.setter
    def git_hub(self, value: Optional[pulumi.Input[GitCatalogArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="syncType")
    def sync_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CatalogSyncType]]]: ...
    @sync_type.setter
    def sync_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CatalogSyncType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:devcenter:ProjectCatalog")
class ProjectCatalog(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ado_git: Optional[
            pulumi.Input[Union[GitCatalogArgs, GitCatalogArgsDict]]
        ] = ...,
        catalog_name: Optional[pulumi.Input[_builtins.str]] = ...,
        git_hub: Optional[
            pulumi.Input[Union[GitCatalogArgs, GitCatalogArgsDict]]
        ] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_type: Optional[pulumi.Input[Union[_builtins.str, CatalogSyncType]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProjectCatalogArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ProjectCatalog: ...
    @_builtins.property
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> pulumi.Output[Optional[outputs.GitCatalogResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> pulumi.Output[Optional[outputs.GitCatalogResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="lastConnectionTime")
    def last_connection_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastSyncStats")
    def last_sync_stats(self) -> pulumi.Output[outputs.SyncStatsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncType")
    def sync_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
