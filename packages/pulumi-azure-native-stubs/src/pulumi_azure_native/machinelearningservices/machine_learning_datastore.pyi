import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MachineLearningDatastoreArgs", "MachineLearningDatastore"]

@pulumi.input_type
class MachineLearningDatastoreArgs:
    def __init__(
        __self__,
        *,
        data_store_type: pulumi.Input[Union[_builtins.str, DatastoreTypeArm]],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        account_key: Optional[pulumi.Input[_builtins.str]] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        adls_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        adls_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        authority_url: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        datastore_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce_ssl: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system: Optional[pulumi.Input[_builtins.str]] = ...,
        include_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_url: Optional[pulumi.Input[_builtins.str]] = ...,
        sas_token: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_account_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        store_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_system_assigned_identity: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DatastoreTypeArm]]: ...
    @data_store_type.setter
    def data_store_type(
        self, value: pulumi.Input[Union[_builtins.str, DatastoreTypeArm]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_key.setter
    def account_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="adlsResourceGroup")
    def adls_resource_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @adls_resource_group.setter
    def adls_resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="adlsSubscriptionId")
    def adls_subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @adls_subscription_id.setter
    def adls_subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authorityUrl")
    def authority_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority_url.setter
    def authority_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enforceSSL")
    def enforce_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce_ssl.setter
    def enforce_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystem")
    def file_system(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system.setter
    def file_system(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includeSecret")
    def include_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_secret.setter
    def include_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUrl")
    def resource_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_url.setter
    def resource_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sas_token.setter
    def sas_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipValidation")
    def skip_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_validation.setter
    def skip_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceGroup")
    def storage_account_resource_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_group.setter
    def storage_account_resource_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountSubscriptionId")
    def storage_account_subscription_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_subscription_id.setter
    def storage_account_subscription_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storeName")
    def store_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @store_name.setter
    def store_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceSystemAssignedIdentity")
    def workspace_system_assigned_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @workspace_system_assigned_identity.setter
    def workspace_system_assigned_identity(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token(...)
class MachineLearningDatastore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_key: Optional[pulumi.Input[_builtins.str]] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        adls_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        adls_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        authority_url: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        data_store_type: Optional[
            pulumi.Input[Union[_builtins.str, DatastoreTypeArm]]
        ] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        datastore_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce_ssl: Optional[pulumi.Input[_builtins.bool]] = ...,
        file_system: Optional[pulumi.Input[_builtins.str]] = ...,
        include_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_url: Optional[pulumi.Input[_builtins.str]] = ...,
        sas_token: Optional[pulumi.Input[_builtins.str]] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        share_name: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_account_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        store_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_system_assigned_identity: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MachineLearningDatastoreArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> MachineLearningDatastore: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponseV2]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.DatastoreResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponseV2]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
