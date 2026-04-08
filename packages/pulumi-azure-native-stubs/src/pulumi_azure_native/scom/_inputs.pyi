import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureHybridBenefitPropertiesArgs",
    "AzureHybridBenefitPropertiesArgsDict",
    "DatabaseInstancePropertiesArgs",
    "DatabaseInstancePropertiesArgsDict",
    "DomainControllerPropertiesArgs",
    "DomainControllerPropertiesArgsDict",
    "DomainUserCredentialsArgs",
    "DomainUserCredentialsArgsDict",
    "GmsaDetailsArgs",
    "GmsaDetailsArgsDict",
    "ManagedIdentityArgs",
    "ManagedIdentityArgsDict",
    "MonitoringInstancePropertiesArgs",
    "MonitoringInstancePropertiesArgsDict",
]

class AzureHybridBenefitPropertiesArgsDict(TypedDict):
    scom_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, HybridLicenseType]]
    ]
    sql_server_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, HybridLicenseType]]
    ]
    windows_server_license_type: NotRequired[
        pulumi.Input[Union[_builtins.str, HybridLicenseType]]
    ]

@pulumi.input_type
class AzureHybridBenefitPropertiesArgs:
    def __init__(
        __self__,
        *,
        scom_license_type: Optional[
            pulumi.Input[Union[_builtins.str, HybridLicenseType]]
        ] = ...,
        sql_server_license_type: Optional[
            pulumi.Input[Union[_builtins.str, HybridLicenseType]]
        ] = ...,
        windows_server_license_type: Optional[
            pulumi.Input[Union[_builtins.str, HybridLicenseType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scomLicenseType")
    def scom_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HybridLicenseType]]]: ...
    @scom_license_type.setter
    def scom_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HybridLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HybridLicenseType]]]: ...
    @sql_server_license_type.setter
    def sql_server_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HybridLicenseType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsServerLicenseType")
    def windows_server_license_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HybridLicenseType]]]: ...
    @windows_server_license_type.setter
    def windows_server_license_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HybridLicenseType]]]
    ): ...

class DatabaseInstancePropertiesArgsDict(TypedDict):
    database_instance_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatabaseInstancePropertiesArgs:
    def __init__(
        __self__, *, database_instance_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseInstanceId")
    def database_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_instance_id.setter
    def database_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainControllerPropertiesArgsDict(TypedDict):
    dns_server: NotRequired[pulumi.Input[_builtins.str]]
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    ou_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainControllerPropertiesArgs:
    def __init__(
        __self__,
        *,
        dns_server: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ou_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsServer")
    def dns_server(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_server.setter
    def dns_server(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ouPath")
    def ou_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ou_path.setter
    def ou_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainUserCredentialsArgsDict(TypedDict):
    key_vault_url: NotRequired[pulumi.Input[_builtins.str]]
    password_secret: NotRequired[pulumi.Input[_builtins.str]]
    user_name_secret: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainUserCredentialsArgs:
    def __init__(
        __self__,
        *,
        key_vault_url: Optional[pulumi.Input[_builtins.str]] = ...,
        password_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        user_name_secret: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_url.setter
    def key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordSecret")
    def password_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_secret.setter
    def password_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userNameSecret")
    def user_name_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_name_secret.setter
    def user_name_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GmsaDetailsArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    gmsa_account: NotRequired[pulumi.Input[_builtins.str]]
    load_balancer_ip: NotRequired[pulumi.Input[_builtins.str]]
    management_server_group_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GmsaDetailsArgs:
    def __init__(
        __self__,
        *,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gmsa_account: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancer_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        management_server_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gmsaAccount")
    def gmsa_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gmsa_account.setter
    def gmsa_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerIP")
    def load_balancer_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancer_ip.setter
    def load_balancer_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managementServerGroupName")
    def management_server_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_server_group_name.setter
    def management_server_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ManagedIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedIdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MonitoringInstancePropertiesArgsDict(TypedDict):
    azure_hybrid_benefit: NotRequired[
        pulumi.Input[AzureHybridBenefitPropertiesArgsDict]
    ]
    database_instance: NotRequired[pulumi.Input[DatabaseInstancePropertiesArgsDict]]
    domain_controller: NotRequired[pulumi.Input[DomainControllerPropertiesArgsDict]]
    domain_user_credentials: NotRequired[pulumi.Input[DomainUserCredentialsArgsDict]]
    gmsa_details: NotRequired[pulumi.Input[GmsaDetailsArgsDict]]
    v_net_subnet_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MonitoringInstancePropertiesArgs:
    def __init__(
        __self__,
        *,
        azure_hybrid_benefit: Optional[
            pulumi.Input[AzureHybridBenefitPropertiesArgs]
        ] = ...,
        database_instance: Optional[pulumi.Input[DatabaseInstancePropertiesArgs]] = ...,
        domain_controller: Optional[pulumi.Input[DomainControllerPropertiesArgs]] = ...,
        domain_user_credentials: Optional[
            pulumi.Input[DomainUserCredentialsArgs]
        ] = ...,
        gmsa_details: Optional[pulumi.Input[GmsaDetailsArgs]] = ...,
        v_net_subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureHybridBenefit")
    def azure_hybrid_benefit(
        self,
    ) -> Optional[pulumi.Input[AzureHybridBenefitPropertiesArgs]]: ...
    @azure_hybrid_benefit.setter
    def azure_hybrid_benefit(
        self, value: Optional[pulumi.Input[AzureHybridBenefitPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseInstance")
    def database_instance(
        self,
    ) -> Optional[pulumi.Input[DatabaseInstancePropertiesArgs]]: ...
    @database_instance.setter
    def database_instance(
        self, value: Optional[pulumi.Input[DatabaseInstancePropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainController")
    def domain_controller(
        self,
    ) -> Optional[pulumi.Input[DomainControllerPropertiesArgs]]: ...
    @domain_controller.setter
    def domain_controller(
        self, value: Optional[pulumi.Input[DomainControllerPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainUserCredentials")
    def domain_user_credentials(
        self,
    ) -> Optional[pulumi.Input[DomainUserCredentialsArgs]]: ...
    @domain_user_credentials.setter
    def domain_user_credentials(
        self, value: Optional[pulumi.Input[DomainUserCredentialsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gmsaDetails")
    def gmsa_details(self) -> Optional[pulumi.Input[GmsaDetailsArgs]]: ...
    @gmsa_details.setter
    def gmsa_details(self, value: Optional[pulumi.Input[GmsaDetailsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="vNetSubnetId")
    def v_net_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @v_net_subnet_id.setter
    def v_net_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
