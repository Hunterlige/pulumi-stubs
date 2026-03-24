import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectionProfileBigqueryProfile",
    "ConnectionProfileForwardSshConnectivity",
    "ConnectionProfileGcsProfile",
    "ConnectionProfileMongodbProfile",
    "ConnectionProfileMongodbProfileHostAddress",
    "ConnectionProfileMongodbProfileSrvConnectionFormat",
    "ConnectionProfileMongodbProfileSslConfig",
    ...,
    "ConnectionProfileMysqlProfile",
    "ConnectionProfileMysqlProfileSslConfig",
    "ConnectionProfileOracleProfile",
    "ConnectionProfilePostgresqlProfile",
    "ConnectionProfilePostgresqlProfileSslConfig",
    ...,
    ...,
    "ConnectionProfilePrivateConnectivity",
    "ConnectionProfileSalesforceProfile",
    ...,
    "ConnectionProfileSalesforceProfileUserCredentials",
    "ConnectionProfileSpannerProfile",
    "ConnectionProfileSqlServerProfile",
    "PrivateConnectionError",
    "PrivateConnectionPscInterfaceConfig",
    "PrivateConnectionVpcPeeringConfig",
    "StreamBackfillAll",
    "StreamBackfillAllMongodbExcludedObjects",
    "StreamBackfillAllMongodbExcludedObjectsDatabase",
    ...,
    ...,
    "StreamBackfillAllMysqlExcludedObjects",
    "StreamBackfillAllMysqlExcludedObjectsMysqlDatabase",
    ...,
    ...,
    "StreamBackfillAllOracleExcludedObjects",
    "StreamBackfillAllOracleExcludedObjectsOracleSchema",
    ...,
    ...,
    "StreamBackfillAllPostgresqlExcludedObjects",
    ...,
    ...,
    ...,
    "StreamBackfillAllSalesforceExcludedObjects",
    "StreamBackfillAllSalesforceExcludedObjectsObject",
    ...,
    "StreamBackfillAllSpannerExcludedObjects",
    "StreamBackfillAllSpannerExcludedObjectsSchema",
    "StreamBackfillAllSpannerExcludedObjectsSchemaTable",
    ...,
    "StreamBackfillAllSqlServerExcludedObjects",
    "StreamBackfillAllSqlServerExcludedObjectsSchema",
    ...,
    ...,
    "StreamBackfillNone",
    "StreamDestinationConfig",
    "StreamDestinationConfigBigqueryDestinationConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamDestinationConfigGcsDestinationConfig",
    ...,
    ...,
    "StreamRuleSet",
    "StreamRuleSetCustomizationRule",
    "StreamRuleSetCustomizationRuleBigqueryClustering",
    "StreamRuleSetCustomizationRuleBigqueryPartitioning",
    ...,
    ...,
    ...,
    "StreamRuleSetObjectFilter",
    "StreamRuleSetObjectFilterSourceObjectIdentifier",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfig",
    "StreamSourceConfigMongodbSourceConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigMysqlSourceConfig",
    ...,
    "StreamSourceConfigMysqlSourceConfigExcludeObjects",
    ...,
    ...,
    ...,
    "StreamSourceConfigMysqlSourceConfigGtid",
    "StreamSourceConfigMysqlSourceConfigIncludeObjects",
    ...,
    ...,
    ...,
    "StreamSourceConfigOracleSourceConfig",
    ...,
    "StreamSourceConfigOracleSourceConfigExcludeObjects",
    ...,
    ...,
    ...,
    "StreamSourceConfigOracleSourceConfigIncludeObjects",
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigPostgresqlSourceConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigSalesforceSourceConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigSpannerSourceConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigSqlServerSourceConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

@pulumi.output_type
class ConnectionProfileBigqueryProfile(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectionProfileForwardSshConnectivity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hostname: _builtins.str,
        username: _builtins.str,
        password: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        private_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileGcsProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, bucket: _builtins.str, root_path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootPath")
    def root_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileMongodbProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_addresses: Sequence[outputs.ConnectionProfileMongodbProfileHostAddress],
        username: _builtins.str,
        password: Optional[_builtins.str] = ...,
        replica_set: Optional[_builtins.str] = ...,
        secret_manager_stored_password: Optional[_builtins.str] = ...,
        srv_connection_format: Optional[
            outputs.ConnectionProfileMongodbProfileSrvConnectionFormat
        ] = ...,
        ssl_config: Optional[outputs.ConnectionProfileMongodbProfileSslConfig] = ...,
        standard_connection_format: Optional[
            outputs.ConnectionProfileMongodbProfileStandardConnectionFormat
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostAddresses")
    def host_addresses(
        self,
    ) -> Sequence[outputs.ConnectionProfileMongodbProfileHostAddress]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaSet")
    def replica_set(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="srvConnectionFormat")
    def srv_connection_format(
        self,
    ) -> Optional[outputs.ConnectionProfileMongodbProfileSrvConnectionFormat]: ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[outputs.ConnectionProfileMongodbProfileSslConfig]: ...
    @_builtins.property
    @pulumi.getter(name="standardConnectionFormat")
    def standard_connection_format(
        self,
    ) -> Optional[outputs.ConnectionProfileMongodbProfileStandardConnectionFormat]: ...

@pulumi.output_type
class ConnectionProfileMongodbProfileHostAddress(dict):
    def __init__(
        __self__, *, hostname: _builtins.str, port: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConnectionProfileMongodbProfileSrvConnectionFormat(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectionProfileMongodbProfileSslConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificate: Optional[_builtins.str] = ...,
        ca_certificate_set: Optional[_builtins.bool] = ...,
        client_certificate: Optional[_builtins.str] = ...,
        client_certificate_set: Optional[_builtins.bool] = ...,
        client_key: Optional[_builtins.str] = ...,
        client_key_set: Optional[_builtins.bool] = ...,
        secret_manager_stored_client_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateSet")
    def ca_certificate_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSet")
    def client_certificate_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientKeySet")
    def client_key_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredClientKey")
    def secret_manager_stored_client_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileMongodbProfileStandardConnectionFormat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, direct_connection: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directConnection")
    def direct_connection(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectionProfileMysqlProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hostname: _builtins.str,
        username: _builtins.str,
        password: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        secret_manager_stored_password: Optional[_builtins.str] = ...,
        ssl_config: Optional[outputs.ConnectionProfileMysqlProfileSslConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[outputs.ConnectionProfileMysqlProfileSslConfig]: ...

@pulumi.output_type
class ConnectionProfileMysqlProfileSslConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificate: Optional[_builtins.str] = ...,
        ca_certificate_set: Optional[_builtins.bool] = ...,
        client_certificate: Optional[_builtins.str] = ...,
        client_certificate_set: Optional[_builtins.bool] = ...,
        client_key: Optional[_builtins.str] = ...,
        client_key_set: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateSet")
    def ca_certificate_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSet")
    def client_certificate_set(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientKeySet")
    def client_key_set(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectionProfileOracleProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_service: _builtins.str,
        hostname: _builtins.str,
        username: _builtins.str,
        connection_attributes: Optional[Mapping[str, _builtins.str]] = ...,
        password: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        secret_manager_stored_password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseService")
    def database_service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionAttributes")
    def connection_attributes(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfilePostgresqlProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        hostname: _builtins.str,
        username: _builtins.str,
        password: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        secret_manager_stored_password: Optional[_builtins.str] = ...,
        ssl_config: Optional[outputs.ConnectionProfilePostgresqlProfileSslConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[outputs.ConnectionProfilePostgresqlProfileSslConfig]: ...

@pulumi.output_type
class ConnectionProfilePostgresqlProfileSslConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        server_and_client_verification: Optional[
            outputs.ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerification
        ] = ...,
        server_verification: Optional[
            outputs.ConnectionProfilePostgresqlProfileSslConfigServerVerification
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverAndClientVerification")
    def server_and_client_verification(
        self,
    ) -> Optional[
        outputs.ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerification
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serverVerification")
    def server_verification(
        self,
    ) -> Optional[
        outputs.ConnectionProfilePostgresqlProfileSslConfigServerVerification
    ]: ...

@pulumi.output_type
class ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificate: _builtins.str,
        client_certificate: _builtins.str,
        client_key: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionProfilePostgresqlProfileSslConfigServerVerification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ca_certificate: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionProfilePrivateConnectivity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, private_connection: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateConnection")
    def private_connection(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionProfileSalesforceProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain: _builtins.str,
        oauth2_client_credentials: Optional[
            outputs.ConnectionProfileSalesforceProfileOauth2ClientCredentials
        ] = ...,
        user_credentials: Optional[
            outputs.ConnectionProfileSalesforceProfileUserCredentials
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentials")
    def oauth2_client_credentials(
        self,
    ) -> Optional[
        outputs.ConnectionProfileSalesforceProfileOauth2ClientCredentials
    ]: ...
    @_builtins.property
    @pulumi.getter(name="userCredentials")
    def user_credentials(
        self,
    ) -> Optional[outputs.ConnectionProfileSalesforceProfileUserCredentials]: ...

@pulumi.output_type
class ConnectionProfileSalesforceProfileOauth2ClientCredentials(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        secret_manager_stored_client_secret: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredClientSecret")
    def secret_manager_stored_client_secret(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileSalesforceProfileUserCredentials(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        password: Optional[_builtins.str] = ...,
        secret_manager_stored_password: Optional[_builtins.str] = ...,
        secret_manager_stored_security_token: Optional[_builtins.str] = ...,
        security_token: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredSecurityToken")
    def secret_manager_stored_security_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileSpannerProfile(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionProfileSqlServerProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        hostname: _builtins.str,
        username: _builtins.str,
        password: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        secret_manager_stored_password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateConnectionError(dict):
    def __init__(
        __self__,
        *,
        details: Optional[Mapping[str, _builtins.str]] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateConnectionPscInterfaceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, network_attachment: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateConnectionVpcPeeringConfig(dict):
    def __init__(__self__, *, subnet: _builtins.str, vpc: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> _builtins.str: ...

@pulumi.output_type
class StreamBackfillAll(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mongodb_excluded_objects: Optional[
            outputs.StreamBackfillAllMongodbExcludedObjects
        ] = ...,
        mysql_excluded_objects: Optional[
            outputs.StreamBackfillAllMysqlExcludedObjects
        ] = ...,
        oracle_excluded_objects: Optional[
            outputs.StreamBackfillAllOracleExcludedObjects
        ] = ...,
        postgresql_excluded_objects: Optional[
            outputs.StreamBackfillAllPostgresqlExcludedObjects
        ] = ...,
        salesforce_excluded_objects: Optional[
            outputs.StreamBackfillAllSalesforceExcludedObjects
        ] = ...,
        spanner_excluded_objects: Optional[
            outputs.StreamBackfillAllSpannerExcludedObjects
        ] = ...,
        sql_server_excluded_objects: Optional[
            outputs.StreamBackfillAllSqlServerExcludedObjects
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mongodbExcludedObjects")
    def mongodb_excluded_objects(
        self,
    ) -> Optional[outputs.StreamBackfillAllMongodbExcludedObjects]: ...
    @_builtins.property
    @pulumi.getter(name="mysqlExcludedObjects")
    def mysql_excluded_objects(
        self,
    ) -> Optional[outputs.StreamBackfillAllMysqlExcludedObjects]: ...
    @_builtins.property
    @pulumi.getter(name="oracleExcludedObjects")
    def oracle_excluded_objects(
        self,
    ) -> Optional[outputs.StreamBackfillAllOracleExcludedObjects]: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlExcludedObjects")
    def postgresql_excluded_objects(
        self,
    ) -> Optional[outputs.StreamBackfillAllPostgresqlExcludedObjects]: ...
    @_builtins.property
    @pulumi.getter(name="salesforceExcludedObjects")
    def salesforce_excluded_objects(
        self,
    ) -> Optional[outputs.StreamBackfillAllSalesforceExcludedObjects]: ...
    @_builtins.property
    @pulumi.getter(name="spannerExcludedObjects")
    def spanner_excluded_objects(
        self,
    ) -> Optional[outputs.StreamBackfillAllSpannerExcludedObjects]: ...
    @_builtins.property
    @pulumi.getter(name="sqlServerExcludedObjects")
    def sql_server_excluded_objects(
        self,
    ) -> Optional[outputs.StreamBackfillAllSqlServerExcludedObjects]: ...

@pulumi.output_type
class StreamBackfillAllMongodbExcludedObjects(dict):
    def __init__(
        __self__,
        *,
        databases: Sequence[outputs.StreamBackfillAllMongodbExcludedObjectsDatabase],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Sequence[outputs.StreamBackfillAllMongodbExcludedObjectsDatabase]: ...

@pulumi.output_type
class StreamBackfillAllMongodbExcludedObjectsDatabase(dict):
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        collections: Optional[
            Sequence[outputs.StreamBackfillAllMongodbExcludedObjectsDatabaseCollection]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def collections(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllMongodbExcludedObjectsDatabaseCollection]
    ]: ...

@pulumi.output_type
class StreamBackfillAllMongodbExcludedObjectsDatabaseCollection(dict):
    def __init__(
        __self__,
        *,
        collection: _builtins.str,
        fields: Optional[
            Sequence[
                outputs.StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionField
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionField]
    ]: ...

@pulumi.output_type
class StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionField(dict):
    def __init__(__self__, *, field: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamBackfillAllMysqlExcludedObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mysql_databases: Sequence[
            outputs.StreamBackfillAllMysqlExcludedObjectsMysqlDatabase
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> Sequence[outputs.StreamBackfillAllMysqlExcludedObjectsMysqlDatabase]: ...

@pulumi.output_type
class StreamBackfillAllMysqlExcludedObjectsMysqlDatabase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        mysql_tables: Optional[
            Sequence[
                outputs.StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mysqlTables")
    def mysql_tables(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTable]
    ]: ...

@pulumi.output_type
class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        mysql_columns: Optional[
            Sequence[
                outputs.StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumn
        ]
    ]: ...

@pulumi.output_type
class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collation: Optional[_builtins.str] = ...,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StreamBackfillAllOracleExcludedObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oracle_schemas: Sequence[
            outputs.StreamBackfillAllOracleExcludedObjectsOracleSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> Sequence[outputs.StreamBackfillAllOracleExcludedObjectsOracleSchema]: ...

@pulumi.output_type
class StreamBackfillAllOracleExcludedObjectsOracleSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        oracle_tables: Optional[
            Sequence[
                outputs.StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oracleTables")
    def oracle_tables(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTable]
    ]: ...

@pulumi.output_type
class StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        oracle_columns: Optional[
            Sequence[
                outputs.StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oracleColumns")
    def oracle_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumn
        ]
    ]: ...

@pulumi.output_type
class StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        encoding: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamBackfillAllPostgresqlExcludedObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        postgresql_schemas: Sequence[
            outputs.StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> Sequence[
        outputs.StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchema
    ]: ...

@pulumi.output_type
class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        postgresql_tables: Optional[
            Sequence[
                outputs.StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTable
        ]
    ]: ...

@pulumi.output_type
class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        postgresql_columns: Optional[
            Sequence[
                outputs.StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn
        ]
    ]: ...

@pulumi.output_type
class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamBackfillAllSalesforceExcludedObjects(dict):
    def __init__(
        __self__,
        *,
        objects: Sequence[outputs.StreamBackfillAllSalesforceExcludedObjectsObject],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def objects(
        self,
    ) -> Sequence[outputs.StreamBackfillAllSalesforceExcludedObjectsObject]: ...

@pulumi.output_type
class StreamBackfillAllSalesforceExcludedObjectsObject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fields: Optional[
            Sequence[outputs.StreamBackfillAllSalesforceExcludedObjectsObjectField]
        ] = ...,
        object_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllSalesforceExcludedObjectsObjectField]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamBackfillAllSalesforceExcludedObjectsObjectField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamBackfillAllSpannerExcludedObjects(dict):
    def __init__(
        __self__,
        *,
        schemas: Sequence[outputs.StreamBackfillAllSpannerExcludedObjectsSchema],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Sequence[outputs.StreamBackfillAllSpannerExcludedObjectsSchema]: ...

@pulumi.output_type
class StreamBackfillAllSpannerExcludedObjectsSchema(dict):
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        tables: Optional[
            Sequence[outputs.StreamBackfillAllSpannerExcludedObjectsSchemaTable]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllSpannerExcludedObjectsSchemaTable]
    ]: ...

@pulumi.output_type
class StreamBackfillAllSpannerExcludedObjectsSchemaTable(dict):
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        columns: Optional[
            Sequence[outputs.StreamBackfillAllSpannerExcludedObjectsSchemaTableColumn]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllSpannerExcludedObjectsSchemaTableColumn]
    ]: ...

@pulumi.output_type
class StreamBackfillAllSpannerExcludedObjectsSchemaTableColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: _builtins.str,
        data_type: Optional[_builtins.str] = ...,
        is_primary_key: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isPrimaryKey")
    def is_primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamBackfillAllSqlServerExcludedObjects(dict):
    def __init__(
        __self__,
        *,
        schemas: Sequence[outputs.StreamBackfillAllSqlServerExcludedObjectsSchema],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Sequence[outputs.StreamBackfillAllSqlServerExcludedObjectsSchema]: ...

@pulumi.output_type
class StreamBackfillAllSqlServerExcludedObjectsSchema(dict):
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        tables: Optional[
            Sequence[outputs.StreamBackfillAllSqlServerExcludedObjectsSchemaTable]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllSqlServerExcludedObjectsSchemaTable]
    ]: ...

@pulumi.output_type
class StreamBackfillAllSqlServerExcludedObjectsSchemaTable(dict):
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        columns: Optional[
            Sequence[outputs.StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumn]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[outputs.StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumn]
    ]: ...

@pulumi.output_type
class StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamBackfillNone(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamDestinationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_connection_profile: _builtins.str,
        bigquery_destination_config: Optional[
            outputs.StreamDestinationConfigBigqueryDestinationConfig
        ] = ...,
        gcs_destination_config: Optional[
            outputs.StreamDestinationConfigGcsDestinationConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationConnectionProfile")
    def destination_connection_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestinationConfig")
    def bigquery_destination_config(
        self,
    ) -> Optional[outputs.StreamDestinationConfigBigqueryDestinationConfig]: ...
    @_builtins.property
    @pulumi.getter(name="gcsDestinationConfig")
    def gcs_destination_config(
        self,
    ) -> Optional[outputs.StreamDestinationConfigGcsDestinationConfig]: ...

@pulumi.output_type
class StreamDestinationConfigBigqueryDestinationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        append_only: Optional[
            outputs.StreamDestinationConfigBigqueryDestinationConfigAppendOnly
        ] = ...,
        blmt_config: Optional[
            outputs.StreamDestinationConfigBigqueryDestinationConfigBlmtConfig
        ] = ...,
        data_freshness: Optional[_builtins.str] = ...,
        merge: Optional[
            outputs.StreamDestinationConfigBigqueryDestinationConfigMerge
        ] = ...,
        single_target_dataset: Optional[
            outputs.StreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset
        ] = ...,
        source_hierarchy_datasets: Optional[
            outputs.StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendOnly")
    def append_only(
        self,
    ) -> Optional[
        outputs.StreamDestinationConfigBigqueryDestinationConfigAppendOnly
    ]: ...
    @_builtins.property
    @pulumi.getter(name="blmtConfig")
    def blmt_config(
        self,
    ) -> Optional[
        outputs.StreamDestinationConfigBigqueryDestinationConfigBlmtConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataFreshness")
    def data_freshness(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def merge(
        self,
    ) -> Optional[outputs.StreamDestinationConfigBigqueryDestinationConfigMerge]: ...
    @_builtins.property
    @pulumi.getter(name="singleTargetDataset")
    def single_target_dataset(
        self,
    ) -> Optional[
        outputs.StreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceHierarchyDatasets")
    def source_hierarchy_datasets(
        self,
    ) -> Optional[
        outputs.StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets
    ]: ...

@pulumi.output_type
class StreamDestinationConfigBigqueryDestinationConfigAppendOnly(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamDestinationConfigBigqueryDestinationConfigBlmtConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        connection_name: _builtins.str,
        file_format: _builtins.str,
        table_format: _builtins.str,
        root_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableFormat")
    def table_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootPath")
    def root_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamDestinationConfigBigqueryDestinationConfigMerge(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamDestinationConfigBigqueryDestinationConfigSingleTargetDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, dataset_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...

@pulumi.output_type
class StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasets(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_template: outputs.StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetTemplate")
    def dataset_template(
        self,
    ) -> outputs.StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplate(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        dataset_id_prefix: Optional[_builtins.str] = ...,
        kms_key_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetIdPrefix")
    def dataset_id_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamDestinationConfigGcsDestinationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        avro_file_format: Optional[
            outputs.StreamDestinationConfigGcsDestinationConfigAvroFileFormat
        ] = ...,
        file_rotation_interval: Optional[_builtins.str] = ...,
        file_rotation_mb: Optional[_builtins.int] = ...,
        json_file_format: Optional[
            outputs.StreamDestinationConfigGcsDestinationConfigJsonFileFormat
        ] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="avroFileFormat")
    def avro_file_format(
        self,
    ) -> Optional[
        outputs.StreamDestinationConfigGcsDestinationConfigAvroFileFormat
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fileRotationInterval")
    def file_rotation_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileRotationMb")
    def file_rotation_mb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="jsonFileFormat")
    def json_file_format(
        self,
    ) -> Optional[
        outputs.StreamDestinationConfigGcsDestinationConfigJsonFileFormat
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamDestinationConfigGcsDestinationConfigAvroFileFormat(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamDestinationConfigGcsDestinationConfigJsonFileFormat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compression: Optional[_builtins.str] = ...,
        schema_file_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaFileFormat")
    def schema_file_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamRuleSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        customization_rules: Sequence[outputs.StreamRuleSetCustomizationRule],
        object_filter: outputs.StreamRuleSetObjectFilter,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customizationRules")
    def customization_rules(
        self,
    ) -> Sequence[outputs.StreamRuleSetCustomizationRule]: ...
    @_builtins.property
    @pulumi.getter(name="objectFilter")
    def object_filter(self) -> outputs.StreamRuleSetObjectFilter: ...

@pulumi.output_type
class StreamRuleSetCustomizationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bigquery_clustering: Optional[
            outputs.StreamRuleSetCustomizationRuleBigqueryClustering
        ] = ...,
        bigquery_partitioning: Optional[
            outputs.StreamRuleSetCustomizationRuleBigqueryPartitioning
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryClustering")
    def bigquery_clustering(
        self,
    ) -> Optional[outputs.StreamRuleSetCustomizationRuleBigqueryClustering]: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryPartitioning")
    def bigquery_partitioning(
        self,
    ) -> Optional[outputs.StreamRuleSetCustomizationRuleBigqueryPartitioning]: ...

@pulumi.output_type
class StreamRuleSetCustomizationRuleBigqueryClustering(dict):
    def __init__(__self__, *, columns: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class StreamRuleSetCustomizationRuleBigqueryPartitioning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingestion_time_partition: Optional[
            outputs.StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartition
        ] = ...,
        integer_range_partition: Optional[
            outputs.StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartition
        ] = ...,
        require_partition_filter: Optional[_builtins.bool] = ...,
        time_unit_partition: Optional[
            outputs.StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartition
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionTimePartition")
    def ingestion_time_partition(
        self,
    ) -> Optional[
        outputs.StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartition
    ]: ...
    @_builtins.property
    @pulumi.getter(name="integerRangePartition")
    def integer_range_partition(
        self,
    ) -> Optional[
        outputs.StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartition
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeUnitPartition")
    def time_unit_partition(
        self,
    ) -> Optional[
        outputs.StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartition
    ]: ...

@pulumi.output_type
class StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, partitioning_time_granularity: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitioningTimeGranularity")
    def partitioning_time_granularity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartition(dict):
    def __init__(
        __self__,
        *,
        column: _builtins.str,
        end: _builtins.int,
        interval: _builtins.int,
        start: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: _builtins.str,
        partitioning_time_granularity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partitioningTimeGranularity")
    def partitioning_time_granularity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamRuleSetObjectFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_object_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifier
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceObjectIdentifier")
    def source_object_identifier(
        self,
    ) -> Optional[outputs.StreamRuleSetObjectFilterSourceObjectIdentifier]: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifier(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mongodb_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifier
        ] = ...,
        mysql_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifier
        ] = ...,
        oracle_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifier
        ] = ...,
        postgresql_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifier
        ] = ...,
        salesforce_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifier
        ] = ...,
        spanner_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifier
        ] = ...,
        sql_server_identifier: Optional[
            outputs.StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifier
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mongodbIdentifier")
    def mongodb_identifier(
        self,
    ) -> Optional[
        outputs.StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifier
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mysqlIdentifier")
    def mysql_identifier(
        self,
    ) -> Optional[
        outputs.StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifier
    ]: ...
    @_builtins.property
    @pulumi.getter(name="oracleIdentifier")
    def oracle_identifier(
        self,
    ) -> Optional[
        outputs.StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifier
    ]: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlIdentifier")
    def postgresql_identifier(
        self,
    ) -> Optional[
        outputs.StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifier
    ]: ...
    @_builtins.property
    @pulumi.getter(name="salesforceIdentifier")
    def salesforce_identifier(
        self,
    ) -> Optional[
        outputs.StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifier
    ]: ...
    @_builtins.property
    @pulumi.getter(name="spannerIdentifier")
    def spanner_identifier(
        self,
    ) -> Optional[
        outputs.StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifier
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sqlServerIdentifier")
    def sql_server_identifier(
        self,
    ) -> Optional[
        outputs.StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifier
    ]: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifier(dict):
    def __init__(
        __self__, *, collection: _builtins.str, database: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifier(dict):
    def __init__(
        __self__, *, database: _builtins.str, table: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifier(dict):
    def __init__(__self__, *, schema: _builtins.str, table: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifier(dict):
    def __init__(__self__, *, schema: _builtins.str, table: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifier(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> _builtins.str: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifier(dict):
    def __init__(
        __self__, *, table: _builtins.str, schema: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifier(dict):
    def __init__(__self__, *, schema: _builtins.str, table: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...

@pulumi.output_type
class StreamSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_connection_profile: _builtins.str,
        mongodb_source_config: Optional[
            outputs.StreamSourceConfigMongodbSourceConfig
        ] = ...,
        mysql_source_config: Optional[
            outputs.StreamSourceConfigMysqlSourceConfig
        ] = ...,
        oracle_source_config: Optional[
            outputs.StreamSourceConfigOracleSourceConfig
        ] = ...,
        postgresql_source_config: Optional[
            outputs.StreamSourceConfigPostgresqlSourceConfig
        ] = ...,
        salesforce_source_config: Optional[
            outputs.StreamSourceConfigSalesforceSourceConfig
        ] = ...,
        spanner_source_config: Optional[
            outputs.StreamSourceConfigSpannerSourceConfig
        ] = ...,
        sql_server_source_config: Optional[
            outputs.StreamSourceConfigSqlServerSourceConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceConnectionProfile")
    def source_connection_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mongodbSourceConfig")
    def mongodb_source_config(
        self,
    ) -> Optional[outputs.StreamSourceConfigMongodbSourceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="mysqlSourceConfig")
    def mysql_source_config(
        self,
    ) -> Optional[outputs.StreamSourceConfigMysqlSourceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="oracleSourceConfig")
    def oracle_source_config(
        self,
    ) -> Optional[outputs.StreamSourceConfigOracleSourceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSourceConfig")
    def postgresql_source_config(
        self,
    ) -> Optional[outputs.StreamSourceConfigPostgresqlSourceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="salesforceSourceConfig")
    def salesforce_source_config(
        self,
    ) -> Optional[outputs.StreamSourceConfigSalesforceSourceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="spannerSourceConfig")
    def spanner_source_config(
        self,
    ) -> Optional[outputs.StreamSourceConfigSpannerSourceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="sqlServerSourceConfig")
    def sql_server_source_config(
        self,
    ) -> Optional[outputs.StreamSourceConfigSqlServerSourceConfig]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exclude_objects: Optional[
            outputs.StreamSourceConfigMongodbSourceConfigExcludeObjects
        ] = ...,
        include_objects: Optional[
            outputs.StreamSourceConfigMongodbSourceConfigIncludeObjects
        ] = ...,
        max_concurrent_backfill_tasks: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigMongodbSourceConfigExcludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigMongodbSourceConfigIncludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigExcludeObjects(dict):
    def __init__(
        __self__,
        *,
        databases: Optional[
            Sequence[
                outputs.StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabase
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[
        Sequence[outputs.StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabase]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabase(dict):
    def __init__(
        __self__,
        *,
        collections: Optional[
            Sequence[
                outputs.StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollection
            ]
        ] = ...,
        database: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collections(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollection
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollection(dict):
    def __init__(
        __self__,
        *,
        collection: Optional[_builtins.str] = ...,
        fields: Optional[
            Sequence[
                outputs.StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionField
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionField
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionField(dict):
    def __init__(__self__, *, field: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigIncludeObjects(dict):
    def __init__(
        __self__,
        *,
        databases: Optional[
            Sequence[
                outputs.StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabase
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[
        Sequence[outputs.StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabase]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabase(dict):
    def __init__(
        __self__,
        *,
        collections: Optional[
            Sequence[
                outputs.StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollection
            ]
        ] = ...,
        database: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collections(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollection
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollection(dict):
    def __init__(
        __self__,
        *,
        collection: Optional[_builtins.str] = ...,
        fields: Optional[
            Sequence[
                outputs.StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionField
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionField
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionField(dict):
    def __init__(__self__, *, field: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        binary_log_position: Optional[
            outputs.StreamSourceConfigMysqlSourceConfigBinaryLogPosition
        ] = ...,
        exclude_objects: Optional[
            outputs.StreamSourceConfigMysqlSourceConfigExcludeObjects
        ] = ...,
        gtid: Optional[outputs.StreamSourceConfigMysqlSourceConfigGtid] = ...,
        include_objects: Optional[
            outputs.StreamSourceConfigMysqlSourceConfigIncludeObjects
        ] = ...,
        max_concurrent_backfill_tasks: Optional[_builtins.int] = ...,
        max_concurrent_cdc_tasks: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="binaryLogPosition")
    def binary_log_position(
        self,
    ) -> Optional[outputs.StreamSourceConfigMysqlSourceConfigBinaryLogPosition]: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigMysqlSourceConfigExcludeObjects]: ...
    @_builtins.property
    @pulumi.getter
    def gtid(self) -> Optional[outputs.StreamSourceConfigMysqlSourceConfigGtid]: ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigMysqlSourceConfigIncludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigBinaryLogPosition(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigExcludeObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mysql_databases: Sequence[
            outputs.StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabase
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabase
    ]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        mysql_tables: Optional[
            Sequence[
                outputs.StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mysqlTables")
    def mysql_tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        mysql_columns: Optional[
            Sequence[
                outputs.StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumn(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collation: Optional[_builtins.str] = ...,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigGtid(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigIncludeObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mysql_databases: Sequence[
            outputs.StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabase
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabase
    ]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        mysql_tables: Optional[
            Sequence[
                outputs.StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mysqlTables")
    def mysql_tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        mysql_columns: Optional[
            Sequence[
                outputs.StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumn(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collation: Optional[_builtins.str] = ...,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        drop_large_objects: Optional[
            outputs.StreamSourceConfigOracleSourceConfigDropLargeObjects
        ] = ...,
        exclude_objects: Optional[
            outputs.StreamSourceConfigOracleSourceConfigExcludeObjects
        ] = ...,
        include_objects: Optional[
            outputs.StreamSourceConfigOracleSourceConfigIncludeObjects
        ] = ...,
        max_concurrent_backfill_tasks: Optional[_builtins.int] = ...,
        max_concurrent_cdc_tasks: Optional[_builtins.int] = ...,
        stream_large_objects: Optional[
            outputs.StreamSourceConfigOracleSourceConfigStreamLargeObjects
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dropLargeObjects")
    def drop_large_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigOracleSourceConfigDropLargeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigOracleSourceConfigExcludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigOracleSourceConfigIncludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="streamLargeObjects")
    def stream_large_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigOracleSourceConfigStreamLargeObjects]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigDropLargeObjects(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigExcludeObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oracle_schemas: Sequence[
            outputs.StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        oracle_tables: Optional[
            Sequence[
                outputs.StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oracleTables")
    def oracle_tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        oracle_columns: Optional[
            Sequence[
                outputs.StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oracleColumns")
    def oracle_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumn(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        encoding: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigIncludeObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oracle_schemas: Sequence[
            outputs.StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        oracle_tables: Optional[
            Sequence[
                outputs.StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oracleTables")
    def oracle_tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        oracle_columns: Optional[
            Sequence[
                outputs.StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oracleColumns")
    def oracle_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumn(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        encoding: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigOracleSourceConfigStreamLargeObjects(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        publication: _builtins.str,
        replication_slot: _builtins.str,
        exclude_objects: Optional[
            outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjects
        ] = ...,
        include_objects: Optional[
            outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjects
        ] = ...,
        max_concurrent_backfill_tasks: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def publication(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationSlot")
    def replication_slot(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        postgresql_schemas: Sequence[
            outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        postgresql_tables: Optional[
            Sequence[
                outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTable(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        postgresql_columns: Optional[
            Sequence[
                outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjects(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        postgresql_schemas: Sequence[
            outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        postgresql_tables: Optional[
            Sequence[
                outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTable(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        postgresql_columns: Optional[
            Sequence[
                outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumn(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigSalesforceSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        polling_interval: _builtins.str,
        exclude_objects: Optional[
            outputs.StreamSourceConfigSalesforceSourceConfigExcludeObjects
        ] = ...,
        include_objects: Optional[
            outputs.StreamSourceConfigSalesforceSourceConfigIncludeObjects
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pollingInterval")
    def polling_interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigSalesforceSourceConfigExcludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigSalesforceSourceConfigIncludeObjects]: ...

@pulumi.output_type
class StreamSourceConfigSalesforceSourceConfigExcludeObjects(dict):
    def __init__(
        __self__,
        *,
        objects: Sequence[
            outputs.StreamSourceConfigSalesforceSourceConfigExcludeObjectsObject
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def objects(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigSalesforceSourceConfigExcludeObjectsObject
    ]: ...

@pulumi.output_type
class StreamSourceConfigSalesforceSourceConfigExcludeObjectsObject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fields: Optional[
            Sequence[
                outputs.StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectField
            ]
        ] = ...,
        object_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectField
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigSalesforceSourceConfigIncludeObjects(dict):
    def __init__(
        __self__,
        *,
        objects: Sequence[
            outputs.StreamSourceConfigSalesforceSourceConfigIncludeObjectsObject
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def objects(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigSalesforceSourceConfigIncludeObjectsObject
    ]: ...

@pulumi.output_type
class StreamSourceConfigSalesforceSourceConfigIncludeObjectsObject(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fields: Optional[
            Sequence[
                outputs.StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectField
            ]
        ] = ...,
        object_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectField
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backfill_data_boost_enabled: Optional[_builtins.bool] = ...,
        change_stream_name: Optional[_builtins.str] = ...,
        exclude_objects: Optional[
            outputs.StreamSourceConfigSpannerSourceConfigExcludeObjects
        ] = ...,
        fgac_role: Optional[_builtins.str] = ...,
        include_objects: Optional[
            outputs.StreamSourceConfigSpannerSourceConfigIncludeObjects
        ] = ...,
        max_concurrent_backfill_tasks: Optional[_builtins.int] = ...,
        max_concurrent_cdc_tasks: Optional[_builtins.int] = ...,
        spanner_rpc_priority: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backfillDataBoostEnabled")
    def backfill_data_boost_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="changeStreamName")
    def change_stream_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigSpannerSourceConfigExcludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="fgacRole")
    def fgac_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigSpannerSourceConfigIncludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="spannerRpcPriority")
    def spanner_rpc_priority(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigExcludeObjects(dict):
    def __init__(
        __self__,
        *,
        schemas: Sequence[
            outputs.StreamSourceConfigSpannerSourceConfigExcludeObjectsSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigSpannerSourceConfigExcludeObjectsSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchema(dict):
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        tables: Optional[
            Sequence[
                outputs.StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        Sequence[outputs.StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTable]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTable(dict):
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        columns: Optional[
            Sequence[
                outputs.StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        is_primary_key: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isPrimaryKey")
    def is_primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigIncludeObjects(dict):
    def __init__(
        __self__,
        *,
        schemas: Sequence[
            outputs.StreamSourceConfigSpannerSourceConfigIncludeObjectsSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigSpannerSourceConfigIncludeObjectsSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchema(dict):
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        tables: Optional[
            Sequence[
                outputs.StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        Sequence[outputs.StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTable]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTable(dict):
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        columns: Optional[
            Sequence[
                outputs.StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        is_primary_key: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isPrimaryKey")
    def is_primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        change_tables: Optional[
            outputs.StreamSourceConfigSqlServerSourceConfigChangeTables
        ] = ...,
        exclude_objects: Optional[
            outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjects
        ] = ...,
        include_objects: Optional[
            outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjects
        ] = ...,
        max_concurrent_backfill_tasks: Optional[_builtins.int] = ...,
        max_concurrent_cdc_tasks: Optional[_builtins.int] = ...,
        transaction_logs: Optional[
            outputs.StreamSourceConfigSqlServerSourceConfigTransactionLogs
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="changeTables")
    def change_tables(
        self,
    ) -> Optional[outputs.StreamSourceConfigSqlServerSourceConfigChangeTables]: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjects]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="transactionLogs")
    def transaction_logs(
        self,
    ) -> Optional[outputs.StreamSourceConfigSqlServerSourceConfigTransactionLogs]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigChangeTables(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjects(dict):
    def __init__(
        __self__,
        *,
        schemas: Sequence[
            outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchema(dict):
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        tables: Optional[
            Sequence[
                outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTable(dict):
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        columns: Optional[
            Sequence[
                outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjects(dict):
    def __init__(
        __self__,
        *,
        schemas: Sequence[
            outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchema
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Sequence[
        outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchema
    ]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchema(dict):
    def __init__(
        __self__,
        *,
        schema: _builtins.str,
        tables: Optional[
            Sequence[
                outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTable
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTable
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTable(dict):
    def __init__(
        __self__,
        *,
        table: _builtins.str,
        columns: Optional[
            Sequence[
                outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumn
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumn
        ]
    ]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        length: Optional[_builtins.int] = ...,
        nullable: Optional[_builtins.bool] = ...,
        ordinal_position: Optional[_builtins.int] = ...,
        precision: Optional[_builtins.int] = ...,
        primary_key: Optional[_builtins.bool] = ...,
        scale: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class StreamSourceConfigSqlServerSourceConfigTransactionLogs(dict):
    def __init__(__self__) -> None: ...
