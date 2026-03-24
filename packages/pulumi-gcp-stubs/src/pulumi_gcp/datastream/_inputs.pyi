import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectionProfileBigqueryProfileArgs",
    "ConnectionProfileBigqueryProfileArgsDict",
    "ConnectionProfileForwardSshConnectivityArgs",
    "ConnectionProfileForwardSshConnectivityArgsDict",
    "ConnectionProfileGcsProfileArgs",
    "ConnectionProfileGcsProfileArgsDict",
    "ConnectionProfileMongodbProfileArgs",
    "ConnectionProfileMongodbProfileArgsDict",
    "ConnectionProfileMongodbProfileHostAddressArgs",
    "ConnectionProfileMongodbProfileHostAddressArgsDict",
    ...,
    ...,
    "ConnectionProfileMongodbProfileSslConfigArgs",
    "ConnectionProfileMongodbProfileSslConfigArgsDict",
    ...,
    ...,
    "ConnectionProfileMysqlProfileArgs",
    "ConnectionProfileMysqlProfileArgsDict",
    "ConnectionProfileMysqlProfileSslConfigArgs",
    "ConnectionProfileMysqlProfileSslConfigArgsDict",
    "ConnectionProfileOracleProfileArgs",
    "ConnectionProfileOracleProfileArgsDict",
    "ConnectionProfilePostgresqlProfileArgs",
    "ConnectionProfilePostgresqlProfileArgsDict",
    "ConnectionProfilePostgresqlProfileSslConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ConnectionProfilePrivateConnectivityArgs",
    "ConnectionProfilePrivateConnectivityArgsDict",
    "ConnectionProfileSalesforceProfileArgs",
    "ConnectionProfileSalesforceProfileArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ConnectionProfileSpannerProfileArgs",
    "ConnectionProfileSpannerProfileArgsDict",
    "ConnectionProfileSqlServerProfileArgs",
    "ConnectionProfileSqlServerProfileArgsDict",
    "PrivateConnectionErrorArgs",
    "PrivateConnectionErrorArgsDict",
    "PrivateConnectionPscInterfaceConfigArgs",
    "PrivateConnectionPscInterfaceConfigArgsDict",
    "PrivateConnectionVpcPeeringConfigArgs",
    "PrivateConnectionVpcPeeringConfigArgsDict",
    "StreamBackfillAllArgs",
    "StreamBackfillAllArgsDict",
    "StreamBackfillAllMongodbExcludedObjectsArgs",
    "StreamBackfillAllMongodbExcludedObjectsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamBackfillAllMysqlExcludedObjectsArgs",
    "StreamBackfillAllMysqlExcludedObjectsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamBackfillAllOracleExcludedObjectsArgs",
    "StreamBackfillAllOracleExcludedObjectsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamBackfillAllPostgresqlExcludedObjectsArgs",
    "StreamBackfillAllPostgresqlExcludedObjectsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamBackfillAllSalesforceExcludedObjectsArgs",
    "StreamBackfillAllSalesforceExcludedObjectsArgsDict",
    ...,
    ...,
    ...,
    ...,
    "StreamBackfillAllSpannerExcludedObjectsArgs",
    "StreamBackfillAllSpannerExcludedObjectsArgsDict",
    "StreamBackfillAllSpannerExcludedObjectsSchemaArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamBackfillAllSqlServerExcludedObjectsArgs",
    "StreamBackfillAllSqlServerExcludedObjectsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamBackfillNoneArgs",
    "StreamBackfillNoneArgsDict",
    "StreamDestinationConfigArgs",
    "StreamDestinationConfigArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    "StreamDestinationConfigGcsDestinationConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamRuleSetArgs",
    "StreamRuleSetArgsDict",
    "StreamRuleSetCustomizationRuleArgs",
    "StreamRuleSetCustomizationRuleArgsDict",
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
    "StreamRuleSetObjectFilterArgs",
    "StreamRuleSetObjectFilterArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigArgs",
    "StreamSourceConfigArgsDict",
    "StreamSourceConfigMongodbSourceConfigArgs",
    "StreamSourceConfigMongodbSourceConfigArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigMysqlSourceConfigArgs",
    "StreamSourceConfigMysqlSourceConfigArgsDict",
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
    "StreamSourceConfigMysqlSourceConfigGtidArgs",
    "StreamSourceConfigMysqlSourceConfigGtidArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigOracleSourceConfigArgs",
    "StreamSourceConfigOracleSourceConfigArgsDict",
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
    "StreamSourceConfigPostgresqlSourceConfigArgs",
    "StreamSourceConfigPostgresqlSourceConfigArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigSalesforceSourceConfigArgs",
    "StreamSourceConfigSalesforceSourceConfigArgsDict",
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
    ...,
    ...,
    "StreamSourceConfigSpannerSourceConfigArgs",
    "StreamSourceConfigSpannerSourceConfigArgsDict",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "StreamSourceConfigSqlServerSourceConfigArgs",
    "StreamSourceConfigSqlServerSourceConfigArgsDict",
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

class ConnectionProfileBigqueryProfileArgsDict(TypedDict): ...

@pulumi.input_type
class ConnectionProfileBigqueryProfileArgs:
    def __init__(__self__) -> None: ...

class ConnectionProfileForwardSshConnectivityArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    private_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileForwardSshConnectivityArgs:
    def __init__(
        __self__,
        *,
        hostname: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionProfileGcsProfileArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    root_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileGcsProfileArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        root_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rootPath")
    def root_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_path.setter
    def root_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionProfileMongodbProfileArgsDict(TypedDict):
    host_addresses: pulumi.Input[
        Sequence[pulumi.Input[ConnectionProfileMongodbProfileHostAddressArgsDict]]
    ]
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    replica_set: NotRequired[pulumi.Input[_builtins.str]]
    secret_manager_stored_password: NotRequired[pulumi.Input[_builtins.str]]
    srv_connection_format: NotRequired[
        pulumi.Input[ConnectionProfileMongodbProfileSrvConnectionFormatArgsDict]
    ]
    ssl_config: NotRequired[
        pulumi.Input[ConnectionProfileMongodbProfileSslConfigArgsDict]
    ]
    standard_connection_format: NotRequired[
        pulumi.Input[ConnectionProfileMongodbProfileStandardConnectionFormatArgsDict]
    ]
    ...

@pulumi.input_type
class ConnectionProfileMongodbProfileArgs:
    def __init__(
        __self__,
        *,
        host_addresses: pulumi.Input[
            Sequence[pulumi.Input[ConnectionProfileMongodbProfileHostAddressArgs]]
        ],
        username: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_set: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_manager_stored_password: Optional[pulumi.Input[_builtins.str]] = ...,
        srv_connection_format: Optional[
            pulumi.Input[ConnectionProfileMongodbProfileSrvConnectionFormatArgs]
        ] = ...,
        ssl_config: Optional[
            pulumi.Input[ConnectionProfileMongodbProfileSslConfigArgs]
        ] = ...,
        standard_connection_format: Optional[
            pulumi.Input[ConnectionProfileMongodbProfileStandardConnectionFormatArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostAddresses")
    def host_addresses(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ConnectionProfileMongodbProfileHostAddressArgs]]
    ]: ...
    @host_addresses.setter
    def host_addresses(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ConnectionProfileMongodbProfileHostAddressArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaSet")
    def replica_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_set.setter
    def replica_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_password.setter
    def secret_manager_stored_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="srvConnectionFormat")
    def srv_connection_format(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionProfileMongodbProfileSrvConnectionFormatArgs]
    ]: ...
    @srv_connection_format.setter
    def srv_connection_format(
        self,
        value: Optional[
            pulumi.Input[ConnectionProfileMongodbProfileSrvConnectionFormatArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileMongodbProfileSslConfigArgs]]: ...
    @ssl_config.setter
    def ssl_config(
        self,
        value: Optional[pulumi.Input[ConnectionProfileMongodbProfileSslConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="standardConnectionFormat")
    def standard_connection_format(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionProfileMongodbProfileStandardConnectionFormatArgs]
    ]: ...
    @standard_connection_format.setter
    def standard_connection_format(
        self,
        value: Optional[
            pulumi.Input[ConnectionProfileMongodbProfileStandardConnectionFormatArgs]
        ],
    ): ...

class ConnectionProfileMongodbProfileHostAddressArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ConnectionProfileMongodbProfileHostAddressArgs:
    def __init__(
        __self__,
        *,
        hostname: pulumi.Input[_builtins.str],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConnectionProfileMongodbProfileSrvConnectionFormatArgsDict(TypedDict): ...

@pulumi.input_type
class ConnectionProfileMongodbProfileSrvConnectionFormatArgs:
    def __init__(__self__) -> None: ...

class ConnectionProfileMongodbProfileSslConfigArgsDict(TypedDict):
    ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    ca_certificate_set: NotRequired[pulumi.Input[_builtins.bool]]
    client_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_certificate_set: NotRequired[pulumi.Input[_builtins.bool]]
    client_key: NotRequired[pulumi.Input[_builtins.str]]
    client_key_set: NotRequired[pulumi.Input[_builtins.bool]]
    secret_manager_stored_client_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileMongodbProfileSslConfigArgs:
    def __init__(
        __self__,
        *,
        ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_set: Optional[pulumi.Input[_builtins.bool]] = ...,
        client_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        client_certificate_set: Optional[pulumi.Input[_builtins.bool]] = ...,
        client_key: Optional[pulumi.Input[_builtins.str]] = ...,
        client_key_set: Optional[pulumi.Input[_builtins.bool]] = ...,
        secret_manager_stored_client_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificateSet")
    def ca_certificate_set(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ca_certificate_set.setter
    def ca_certificate_set(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSet")
    def client_certificate_set(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_certificate_set.setter
    def client_certificate_set(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientKeySet")
    def client_key_set(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_key_set.setter
    def client_key_set(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredClientKey")
    def secret_manager_stored_client_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_client_key.setter
    def secret_manager_stored_client_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ConnectionProfileMongodbProfileStandardConnectionFormatArgsDict(TypedDict):
    direct_connection: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ConnectionProfileMongodbProfileStandardConnectionFormatArgs:
    def __init__(
        __self__, *, direct_connection: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directConnection")
    def direct_connection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @direct_connection.setter
    def direct_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConnectionProfileMysqlProfileArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    secret_manager_stored_password: NotRequired[pulumi.Input[_builtins.str]]
    ssl_config: NotRequired[
        pulumi.Input[ConnectionProfileMysqlProfileSslConfigArgsDict]
    ]
    ...

@pulumi.input_type
class ConnectionProfileMysqlProfileArgs:
    def __init__(
        __self__,
        *,
        hostname: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_manager_stored_password: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_config: Optional[
            pulumi.Input[ConnectionProfileMysqlProfileSslConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_password.setter
    def secret_manager_stored_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileMysqlProfileSslConfigArgs]]: ...
    @ssl_config.setter
    def ssl_config(
        self, value: Optional[pulumi.Input[ConnectionProfileMysqlProfileSslConfigArgs]]
    ): ...

class ConnectionProfileMysqlProfileSslConfigArgsDict(TypedDict):
    ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    ca_certificate_set: NotRequired[pulumi.Input[_builtins.bool]]
    client_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_certificate_set: NotRequired[pulumi.Input[_builtins.bool]]
    client_key: NotRequired[pulumi.Input[_builtins.str]]
    client_key_set: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ConnectionProfileMysqlProfileSslConfigArgs:
    def __init__(
        __self__,
        *,
        ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_set: Optional[pulumi.Input[_builtins.bool]] = ...,
        client_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        client_certificate_set: Optional[pulumi.Input[_builtins.bool]] = ...,
        client_key: Optional[pulumi.Input[_builtins.str]] = ...,
        client_key_set: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificateSet")
    def ca_certificate_set(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ca_certificate_set.setter
    def ca_certificate_set(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSet")
    def client_certificate_set(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_certificate_set.setter
    def client_certificate_set(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientKeySet")
    def client_key_set(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_key_set.setter
    def client_key_set(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConnectionProfileOracleProfileArgsDict(TypedDict):
    database_service: pulumi.Input[_builtins.str]
    hostname: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    connection_attributes: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    secret_manager_stored_password: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileOracleProfileArgs:
    def __init__(
        __self__,
        *,
        database_service: pulumi.Input[_builtins.str],
        hostname: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        connection_attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_manager_stored_password: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseService")
    def database_service(self) -> pulumi.Input[_builtins.str]: ...
    @database_service.setter
    def database_service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectionAttributes")
    def connection_attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @connection_attributes.setter
    def connection_attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_password.setter
    def secret_manager_stored_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ConnectionProfilePostgresqlProfileArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    hostname: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    secret_manager_stored_password: NotRequired[pulumi.Input[_builtins.str]]
    ssl_config: NotRequired[
        pulumi.Input[ConnectionProfilePostgresqlProfileSslConfigArgsDict]
    ]
    ...

@pulumi.input_type
class ConnectionProfilePostgresqlProfileArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        hostname: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_manager_stored_password: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_config: Optional[
            pulumi.Input[ConnectionProfilePostgresqlProfileSslConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_password.setter
    def secret_manager_stored_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslConfig")
    def ssl_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfilePostgresqlProfileSslConfigArgs]]: ...
    @ssl_config.setter
    def ssl_config(
        self,
        value: Optional[pulumi.Input[ConnectionProfilePostgresqlProfileSslConfigArgs]],
    ): ...

class ConnectionProfilePostgresqlProfileSslConfigArgsDict(TypedDict):
    server_and_client_verification: NotRequired[
        pulumi.Input[
            ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerificationArgsDict
        ]
    ]
    server_verification: NotRequired[
        pulumi.Input[
            ConnectionProfilePostgresqlProfileSslConfigServerVerificationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ConnectionProfilePostgresqlProfileSslConfigArgs:
    def __init__(
        __self__,
        *,
        server_and_client_verification: Optional[
            pulumi.Input[
                ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerificationArgs
            ]
        ] = ...,
        server_verification: Optional[
            pulumi.Input[
                ConnectionProfilePostgresqlProfileSslConfigServerVerificationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverAndClientVerification")
    def server_and_client_verification(
        self,
    ) -> Optional[
        pulumi.Input[
            ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerificationArgs
        ]
    ]: ...
    @server_and_client_verification.setter
    def server_and_client_verification(
        self,
        value: Optional[
            pulumi.Input[
                ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerificationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverVerification")
    def server_verification(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionProfilePostgresqlProfileSslConfigServerVerificationArgs]
    ]: ...
    @server_verification.setter
    def server_verification(
        self,
        value: Optional[
            pulumi.Input[
                ConnectionProfilePostgresqlProfileSslConfigServerVerificationArgs
            ]
        ],
    ): ...

class ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerificationArgsDict(
    TypedDict
):
    ca_certificate: pulumi.Input[_builtins.str]
    client_certificate: pulumi.Input[_builtins.str]
    client_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ConnectionProfilePostgresqlProfileSslConfigServerAndClientVerificationArgs:
    def __init__(
        __self__,
        *,
        ca_certificate: pulumi.Input[_builtins.str],
        client_certificate: pulumi.Input[_builtins.str],
        client_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @ca_certificate.setter
    def ca_certificate(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @client_certificate.setter
    def client_certificate(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> pulumi.Input[_builtins.str]: ...
    @client_key.setter
    def client_key(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionProfilePostgresqlProfileSslConfigServerVerificationArgsDict(TypedDict):
    ca_certificate: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ConnectionProfilePostgresqlProfileSslConfigServerVerificationArgs:
    def __init__(__self__, *, ca_certificate: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @ca_certificate.setter
    def ca_certificate(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionProfilePrivateConnectivityArgsDict(TypedDict):
    private_connection: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ConnectionProfilePrivateConnectivityArgs:
    def __init__(
        __self__, *, private_connection: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateConnection")
    def private_connection(self) -> pulumi.Input[_builtins.str]: ...
    @private_connection.setter
    def private_connection(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionProfileSalesforceProfileArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]
    oauth2_client_credentials: NotRequired[
        pulumi.Input[ConnectionProfileSalesforceProfileOauth2ClientCredentialsArgsDict]
    ]
    user_credentials: NotRequired[
        pulumi.Input[ConnectionProfileSalesforceProfileUserCredentialsArgsDict]
    ]
    ...

@pulumi.input_type
class ConnectionProfileSalesforceProfileArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        oauth2_client_credentials: Optional[
            pulumi.Input[ConnectionProfileSalesforceProfileOauth2ClientCredentialsArgs]
        ] = ...,
        user_credentials: Optional[
            pulumi.Input[ConnectionProfileSalesforceProfileUserCredentialsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentials")
    def oauth2_client_credentials(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionProfileSalesforceProfileOauth2ClientCredentialsArgs]
    ]: ...
    @oauth2_client_credentials.setter
    def oauth2_client_credentials(
        self,
        value: Optional[
            pulumi.Input[ConnectionProfileSalesforceProfileOauth2ClientCredentialsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userCredentials")
    def user_credentials(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionProfileSalesforceProfileUserCredentialsArgs]
    ]: ...
    @user_credentials.setter
    def user_credentials(
        self,
        value: Optional[
            pulumi.Input[ConnectionProfileSalesforceProfileUserCredentialsArgs]
        ],
    ): ...

class ConnectionProfileSalesforceProfileOauth2ClientCredentialsArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    secret_manager_stored_client_secret: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileSalesforceProfileOauth2ClientCredentialsArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_manager_stored_client_secret: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="secretManagerStoredClientSecret")
    def secret_manager_stored_client_secret(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_client_secret.setter
    def secret_manager_stored_client_secret(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ConnectionProfileSalesforceProfileUserCredentialsArgsDict(TypedDict):
    password: NotRequired[pulumi.Input[_builtins.str]]
    secret_manager_stored_password: NotRequired[pulumi.Input[_builtins.str]]
    secret_manager_stored_security_token: NotRequired[pulumi.Input[_builtins.str]]
    security_token: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileSalesforceProfileUserCredentialsArgs:
    def __init__(
        __self__,
        *,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_manager_stored_password: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_manager_stored_security_token: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        security_token: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_password.setter
    def secret_manager_stored_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredSecurityToken")
    def secret_manager_stored_security_token(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_security_token.setter
    def secret_manager_stored_security_token(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_token.setter
    def security_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionProfileSpannerProfileArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileSpannerProfileArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionProfileSqlServerProfileArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    hostname: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    secret_manager_stored_password: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ConnectionProfileSqlServerProfileArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        hostname: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_manager_stored_password: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretManagerStoredPassword")
    def secret_manager_stored_password(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_manager_stored_password.setter
    def secret_manager_stored_password(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PrivateConnectionErrorArgsDict(TypedDict):
    details: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PrivateConnectionErrorArgs:
    def __init__(
        __self__,
        *,
        details: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @details.setter
    def details(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateConnectionPscInterfaceConfigArgsDict(TypedDict):
    network_attachment: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PrivateConnectionPscInterfaceConfigArgs:
    def __init__(
        __self__, *, network_attachment: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> pulumi.Input[_builtins.str]: ...
    @network_attachment.setter
    def network_attachment(self, value: pulumi.Input[_builtins.str]): ...

class PrivateConnectionVpcPeeringConfigArgsDict(TypedDict):
    subnet: pulumi.Input[_builtins.str]
    vpc: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PrivateConnectionVpcPeeringConfigArgs:
    def __init__(
        __self__,
        *,
        subnet: pulumi.Input[_builtins.str],
        vpc: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Input[_builtins.str]: ...
    @subnet.setter
    def subnet(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> pulumi.Input[_builtins.str]: ...
    @vpc.setter
    def vpc(self, value: pulumi.Input[_builtins.str]): ...

class StreamBackfillAllArgsDict(TypedDict):
    mongodb_excluded_objects: NotRequired[
        pulumi.Input[StreamBackfillAllMongodbExcludedObjectsArgsDict]
    ]
    mysql_excluded_objects: NotRequired[
        pulumi.Input[StreamBackfillAllMysqlExcludedObjectsArgsDict]
    ]
    oracle_excluded_objects: NotRequired[
        pulumi.Input[StreamBackfillAllOracleExcludedObjectsArgsDict]
    ]
    postgresql_excluded_objects: NotRequired[
        pulumi.Input[StreamBackfillAllPostgresqlExcludedObjectsArgsDict]
    ]
    salesforce_excluded_objects: NotRequired[
        pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsArgsDict]
    ]
    spanner_excluded_objects: NotRequired[
        pulumi.Input[StreamBackfillAllSpannerExcludedObjectsArgsDict]
    ]
    sql_server_excluded_objects: NotRequired[
        pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsArgsDict]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllArgs:
    def __init__(
        __self__,
        *,
        mongodb_excluded_objects: Optional[
            pulumi.Input[StreamBackfillAllMongodbExcludedObjectsArgs]
        ] = ...,
        mysql_excluded_objects: Optional[
            pulumi.Input[StreamBackfillAllMysqlExcludedObjectsArgs]
        ] = ...,
        oracle_excluded_objects: Optional[
            pulumi.Input[StreamBackfillAllOracleExcludedObjectsArgs]
        ] = ...,
        postgresql_excluded_objects: Optional[
            pulumi.Input[StreamBackfillAllPostgresqlExcludedObjectsArgs]
        ] = ...,
        salesforce_excluded_objects: Optional[
            pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsArgs]
        ] = ...,
        spanner_excluded_objects: Optional[
            pulumi.Input[StreamBackfillAllSpannerExcludedObjectsArgs]
        ] = ...,
        sql_server_excluded_objects: Optional[
            pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mongodbExcludedObjects")
    def mongodb_excluded_objects(
        self,
    ) -> Optional[pulumi.Input[StreamBackfillAllMongodbExcludedObjectsArgs]]: ...
    @mongodb_excluded_objects.setter
    def mongodb_excluded_objects(
        self, value: Optional[pulumi.Input[StreamBackfillAllMongodbExcludedObjectsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mysqlExcludedObjects")
    def mysql_excluded_objects(
        self,
    ) -> Optional[pulumi.Input[StreamBackfillAllMysqlExcludedObjectsArgs]]: ...
    @mysql_excluded_objects.setter
    def mysql_excluded_objects(
        self, value: Optional[pulumi.Input[StreamBackfillAllMysqlExcludedObjectsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oracleExcludedObjects")
    def oracle_excluded_objects(
        self,
    ) -> Optional[pulumi.Input[StreamBackfillAllOracleExcludedObjectsArgs]]: ...
    @oracle_excluded_objects.setter
    def oracle_excluded_objects(
        self, value: Optional[pulumi.Input[StreamBackfillAllOracleExcludedObjectsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlExcludedObjects")
    def postgresql_excluded_objects(
        self,
    ) -> Optional[pulumi.Input[StreamBackfillAllPostgresqlExcludedObjectsArgs]]: ...
    @postgresql_excluded_objects.setter
    def postgresql_excluded_objects(
        self,
        value: Optional[pulumi.Input[StreamBackfillAllPostgresqlExcludedObjectsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="salesforceExcludedObjects")
    def salesforce_excluded_objects(
        self,
    ) -> Optional[pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsArgs]]: ...
    @salesforce_excluded_objects.setter
    def salesforce_excluded_objects(
        self,
        value: Optional[pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spannerExcludedObjects")
    def spanner_excluded_objects(
        self,
    ) -> Optional[pulumi.Input[StreamBackfillAllSpannerExcludedObjectsArgs]]: ...
    @spanner_excluded_objects.setter
    def spanner_excluded_objects(
        self, value: Optional[pulumi.Input[StreamBackfillAllSpannerExcludedObjectsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerExcludedObjects")
    def sql_server_excluded_objects(
        self,
    ) -> Optional[pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsArgs]]: ...
    @sql_server_excluded_objects.setter
    def sql_server_excluded_objects(
        self,
        value: Optional[pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsArgs]],
    ): ...

class StreamBackfillAllMongodbExcludedObjectsArgsDict(TypedDict):
    databases: pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllMongodbExcludedObjectsDatabaseArgsDict]]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllMongodbExcludedObjectsArgs:
    def __init__(
        __self__,
        *,
        databases: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllMongodbExcludedObjectsDatabaseArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllMongodbExcludedObjectsDatabaseArgs]]
    ]: ...
    @databases.setter
    def databases(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllMongodbExcludedObjectsDatabaseArgs]]
        ],
    ): ...

class StreamBackfillAllMongodbExcludedObjectsDatabaseArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    collections: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllMongodbExcludedObjectsDatabaseArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        collections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def collections(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionArgs
                ]
            ]
        ]
    ]: ...
    @collections.setter
    def collections(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionArgsDict(TypedDict):
    collection: pulumi.Input[_builtins.str]
    fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionFieldArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionArgs:
    def __init__(
        __self__,
        *,
        collection: pulumi.Input[_builtins.str],
        fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionFieldArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> pulumi.Input[_builtins.str]: ...
    @collection.setter
    def collection(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionFieldArgs
                ]
            ]
        ]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionFieldArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionFieldArgsDict(TypedDict):
    field: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamBackfillAllMongodbExcludedObjectsDatabaseCollectionFieldArgs:
    def __init__(
        __self__, *, field: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamBackfillAllMysqlExcludedObjectsArgsDict(TypedDict):
    mysql_databases: pulumi.Input[
        Sequence[
            pulumi.Input[StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseArgsDict]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllMysqlExcludedObjectsArgs:
    def __init__(
        __self__,
        *,
        mysql_databases: pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseArgs]]
    ]: ...
    @mysql_databases.setter
    def mysql_databases(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseArgs]
            ]
        ],
    ): ...

class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    mysql_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        mysql_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mysqlTables")
    def mysql_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableArgs
                ]
            ]
        ]
    ]: ...
    @mysql_tables.setter
    def mysql_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableArgsDict(TypedDict):
    table: pulumi.Input[_builtins.str]
    mysql_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        mysql_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                ]
            ]
        ]
    ]: ...
    @mysql_columns.setter
    def mysql_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumnArgsDict(
    TypedDict
):
    collation: NotRequired[pulumi.Input[_builtins.str]]
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class StreamBackfillAllMysqlExcludedObjectsMysqlDatabaseMysqlTableMysqlColumnArgs:
    def __init__(
        __self__,
        *,
        collation: Optional[pulumi.Input[_builtins.str]] = ...,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StreamBackfillAllOracleExcludedObjectsArgsDict(TypedDict):
    oracle_schemas: pulumi.Input[
        Sequence[
            pulumi.Input[StreamBackfillAllOracleExcludedObjectsOracleSchemaArgsDict]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllOracleExcludedObjectsArgs:
    def __init__(
        __self__,
        *,
        oracle_schemas: pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllOracleExcludedObjectsOracleSchemaArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllOracleExcludedObjectsOracleSchemaArgs]]
    ]: ...
    @oracle_schemas.setter
    def oracle_schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllOracleExcludedObjectsOracleSchemaArgs]
            ]
        ],
    ): ...

class StreamBackfillAllOracleExcludedObjectsOracleSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    oracle_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllOracleExcludedObjectsOracleSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        oracle_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oracleTables")
    def oracle_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableArgs
                ]
            ]
        ]
    ]: ...
    @oracle_tables.setter
    def oracle_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableArgsDict(TypedDict):
    table: pulumi.Input[_builtins.str]
    oracle_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        oracle_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oracleColumns")
    def oracle_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumnArgs
                ]
            ]
        ]
    ]: ...
    @oracle_columns.setter
    def oracle_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamBackfillAllOracleExcludedObjectsOracleSchemaOracleTableOracleColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamBackfillAllPostgresqlExcludedObjectsArgsDict(TypedDict):
    postgresql_schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllPostgresqlExcludedObjectsArgs:
    def __init__(
        __self__,
        *,
        postgresql_schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaArgs]
        ]
    ]: ...
    @postgresql_schemas.setter
    def postgresql_schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    postgresql_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        postgresql_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTableArgs
                ]
            ]
        ]
    ]: ...
    @postgresql_tables.setter
    def postgresql_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    postgresql_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        postgresql_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                ]
            ]
        ]
    ]: ...
    @postgresql_columns.setter
    def postgresql_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamBackfillAllPostgresqlExcludedObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamBackfillAllSalesforceExcludedObjectsArgsDict(TypedDict):
    objects: pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsObjectArgsDict]]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllSalesforceExcludedObjectsArgs:
    def __init__(
        __self__,
        *,
        objects: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsObjectArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def objects(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsObjectArgs]]
    ]: ...
    @objects.setter
    def objects(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsObjectArgs]]
        ],
    ): ...

class StreamBackfillAllSalesforceExcludedObjectsObjectArgsDict(TypedDict):
    fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllSalesforceExcludedObjectsObjectFieldArgsDict
                ]
            ]
        ]
    ]
    object_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamBackfillAllSalesforceExcludedObjectsObjectArgs:
    def __init__(
        __self__,
        *,
        fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSalesforceExcludedObjectsObjectFieldArgs
                    ]
                ]
            ]
        ] = ...,
        object_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllSalesforceExcludedObjectsObjectFieldArgs]
            ]
        ]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSalesforceExcludedObjectsObjectFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_name.setter
    def object_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamBackfillAllSalesforceExcludedObjectsObjectFieldArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamBackfillAllSalesforceExcludedObjectsObjectFieldArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamBackfillAllSpannerExcludedObjectsArgsDict(TypedDict):
    schemas: pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaArgsDict]]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllSpannerExcludedObjectsArgs:
    def __init__(
        __self__,
        *,
        schemas: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaArgs]]
    ]: ...
    @schemas.setter
    def schemas(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaArgs]]
        ],
    ): ...

class StreamBackfillAllSpannerExcludedObjectsSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaTableArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllSpannerExcludedObjectsSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaTableArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaTableArgs]
            ]
        ]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[StreamBackfillAllSpannerExcludedObjectsSchemaTableArgs]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllSpannerExcludedObjectsSchemaTableArgsDict(TypedDict):
    table: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllSpannerExcludedObjectsSchemaTableColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllSpannerExcludedObjectsSchemaTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSpannerExcludedObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllSpannerExcludedObjectsSchemaTableColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSpannerExcludedObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllSpannerExcludedObjectsSchemaTableColumnArgsDict(TypedDict):
    column: pulumi.Input[_builtins.str]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    is_primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamBackfillAllSpannerExcludedObjectsSchemaTableColumnArgs:
    def __init__(
        __self__,
        *,
        column: pulumi.Input[_builtins.str],
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        is_primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> pulumi.Input[_builtins.str]: ...
    @column.setter
    def column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isPrimaryKey")
    def is_primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_primary_key.setter
    def is_primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamBackfillAllSqlServerExcludedObjectsArgsDict(TypedDict):
    schemas: pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsSchemaArgsDict]]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllSqlServerExcludedObjectsArgs:
    def __init__(
        __self__,
        *,
        schemas: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsSchemaArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsSchemaArgs]]
    ]: ...
    @schemas.setter
    def schemas(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsSchemaArgs]]
        ],
    ): ...

class StreamBackfillAllSqlServerExcludedObjectsSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllSqlServerExcludedObjectsSchemaTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllSqlServerExcludedObjectsSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSqlServerExcludedObjectsSchemaTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[StreamBackfillAllSqlServerExcludedObjectsSchemaTableArgs]
            ]
        ]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSqlServerExcludedObjectsSchemaTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllSqlServerExcludedObjectsSchemaTableArgsDict(TypedDict):
    table: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamBackfillAllSqlServerExcludedObjectsSchemaTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumnArgsDict(TypedDict):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamBackfillAllSqlServerExcludedObjectsSchemaTableColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamBackfillNoneArgsDict(TypedDict): ...

@pulumi.input_type
class StreamBackfillNoneArgs:
    def __init__(__self__) -> None: ...

class StreamDestinationConfigArgsDict(TypedDict):
    destination_connection_profile: pulumi.Input[_builtins.str]
    bigquery_destination_config: NotRequired[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigArgsDict]
    ]
    gcs_destination_config: NotRequired[
        pulumi.Input[StreamDestinationConfigGcsDestinationConfigArgsDict]
    ]
    ...

@pulumi.input_type
class StreamDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        destination_connection_profile: pulumi.Input[_builtins.str],
        bigquery_destination_config: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigArgs]
        ] = ...,
        gcs_destination_config: Optional[
            pulumi.Input[StreamDestinationConfigGcsDestinationConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationConnectionProfile")
    def destination_connection_profile(self) -> pulumi.Input[_builtins.str]: ...
    @destination_connection_profile.setter
    def destination_connection_profile(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryDestinationConfig")
    def bigquery_destination_config(
        self,
    ) -> Optional[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigArgs]
    ]: ...
    @bigquery_destination_config.setter
    def bigquery_destination_config(
        self,
        value: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsDestinationConfig")
    def gcs_destination_config(
        self,
    ) -> Optional[pulumi.Input[StreamDestinationConfigGcsDestinationConfigArgs]]: ...
    @gcs_destination_config.setter
    def gcs_destination_config(
        self,
        value: Optional[pulumi.Input[StreamDestinationConfigGcsDestinationConfigArgs]],
    ): ...

class StreamDestinationConfigBigqueryDestinationConfigArgsDict(TypedDict):
    append_only: NotRequired[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigAppendOnlyArgsDict]
    ]
    blmt_config: NotRequired[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigBlmtConfigArgsDict]
    ]
    data_freshness: NotRequired[pulumi.Input[_builtins.str]]
    merge: NotRequired[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigMergeArgsDict]
    ]
    single_target_dataset: NotRequired[
        pulumi.Input[
            StreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetArgsDict
        ]
    ]
    source_hierarchy_datasets: NotRequired[
        pulumi.Input[
            StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class StreamDestinationConfigBigqueryDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        append_only: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigAppendOnlyArgs]
        ] = ...,
        blmt_config: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigBlmtConfigArgs]
        ] = ...,
        data_freshness: Optional[pulumi.Input[_builtins.str]] = ...,
        merge: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigMergeArgs]
        ] = ...,
        single_target_dataset: Optional[
            pulumi.Input[
                StreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetArgs
            ]
        ] = ...,
        source_hierarchy_datasets: Optional[
            pulumi.Input[
                StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendOnly")
    def append_only(
        self,
    ) -> Optional[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigAppendOnlyArgs]
    ]: ...
    @append_only.setter
    def append_only(
        self,
        value: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigAppendOnlyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="blmtConfig")
    def blmt_config(
        self,
    ) -> Optional[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigBlmtConfigArgs]
    ]: ...
    @blmt_config.setter
    def blmt_config(
        self,
        value: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigBlmtConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataFreshness")
    def data_freshness(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_freshness.setter
    def data_freshness(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def merge(
        self,
    ) -> Optional[
        pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigMergeArgs]
    ]: ...
    @merge.setter
    def merge(
        self,
        value: Optional[
            pulumi.Input[StreamDestinationConfigBigqueryDestinationConfigMergeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleTargetDataset")
    def single_target_dataset(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetArgs
        ]
    ]: ...
    @single_target_dataset.setter
    def single_target_dataset(
        self,
        value: Optional[
            pulumi.Input[
                StreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceHierarchyDatasets")
    def source_hierarchy_datasets(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsArgs
        ]
    ]: ...
    @source_hierarchy_datasets.setter
    def source_hierarchy_datasets(
        self,
        value: Optional[
            pulumi.Input[
                StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsArgs
            ]
        ],
    ): ...

class StreamDestinationConfigBigqueryDestinationConfigAppendOnlyArgsDict(TypedDict): ...

@pulumi.input_type
class StreamDestinationConfigBigqueryDestinationConfigAppendOnlyArgs:
    def __init__(__self__) -> None: ...

class StreamDestinationConfigBigqueryDestinationConfigBlmtConfigArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    connection_name: pulumi.Input[_builtins.str]
    file_format: pulumi.Input[_builtins.str]
    table_format: pulumi.Input[_builtins.str]
    root_path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamDestinationConfigBigqueryDestinationConfigBlmtConfigArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        connection_name: pulumi.Input[_builtins.str],
        file_format: pulumi.Input[_builtins.str],
        table_format: pulumi.Input[_builtins.str],
        root_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Input[_builtins.str]: ...
    @connection_name.setter
    def connection_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> pulumi.Input[_builtins.str]: ...
    @file_format.setter
    def file_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableFormat")
    def table_format(self) -> pulumi.Input[_builtins.str]: ...
    @table_format.setter
    def table_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rootPath")
    def root_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_path.setter
    def root_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamDestinationConfigBigqueryDestinationConfigMergeArgsDict(TypedDict): ...

@pulumi.input_type
class StreamDestinationConfigBigqueryDestinationConfigMergeArgs:
    def __init__(__self__) -> None: ...

class StreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetArgsDict(
    TypedDict
):
    dataset_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StreamDestinationConfigBigqueryDestinationConfigSingleTargetDatasetArgs:
    def __init__(__self__, *, dataset_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...

class StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsArgsDict(
    TypedDict
):
    dataset_template: pulumi.Input[
        StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateArgsDict
    ]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsArgs:
    def __init__(
        __self__,
        *,
        dataset_template: pulumi.Input[
            StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateArgs
        ],
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetTemplate")
    def dataset_template(
        self,
    ) -> pulumi.Input[
        StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateArgs
    ]: ...
    @dataset_template.setter
    def dataset_template(
        self,
        value: pulumi.Input[
            StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateArgsDict(
    TypedDict
):
    location: pulumi.Input[_builtins.str]
    dataset_id_prefix: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamDestinationConfigBigqueryDestinationConfigSourceHierarchyDatasetsDatasetTemplateArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        dataset_id_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datasetIdPrefix")
    def dataset_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id_prefix.setter
    def dataset_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamDestinationConfigGcsDestinationConfigArgsDict(TypedDict):
    avro_file_format: NotRequired[
        pulumi.Input[StreamDestinationConfigGcsDestinationConfigAvroFileFormatArgsDict]
    ]
    file_rotation_interval: NotRequired[pulumi.Input[_builtins.str]]
    file_rotation_mb: NotRequired[pulumi.Input[_builtins.int]]
    json_file_format: NotRequired[
        pulumi.Input[StreamDestinationConfigGcsDestinationConfigJsonFileFormatArgsDict]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamDestinationConfigGcsDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        avro_file_format: Optional[
            pulumi.Input[StreamDestinationConfigGcsDestinationConfigAvroFileFormatArgs]
        ] = ...,
        file_rotation_interval: Optional[pulumi.Input[_builtins.str]] = ...,
        file_rotation_mb: Optional[pulumi.Input[_builtins.int]] = ...,
        json_file_format: Optional[
            pulumi.Input[StreamDestinationConfigGcsDestinationConfigJsonFileFormatArgs]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="avroFileFormat")
    def avro_file_format(
        self,
    ) -> Optional[
        pulumi.Input[StreamDestinationConfigGcsDestinationConfigAvroFileFormatArgs]
    ]: ...
    @avro_file_format.setter
    def avro_file_format(
        self,
        value: Optional[
            pulumi.Input[StreamDestinationConfigGcsDestinationConfigAvroFileFormatArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileRotationInterval")
    def file_rotation_interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_rotation_interval.setter
    def file_rotation_interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileRotationMb")
    def file_rotation_mb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @file_rotation_mb.setter
    def file_rotation_mb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="jsonFileFormat")
    def json_file_format(
        self,
    ) -> Optional[
        pulumi.Input[StreamDestinationConfigGcsDestinationConfigJsonFileFormatArgs]
    ]: ...
    @json_file_format.setter
    def json_file_format(
        self,
        value: Optional[
            pulumi.Input[StreamDestinationConfigGcsDestinationConfigJsonFileFormatArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamDestinationConfigGcsDestinationConfigAvroFileFormatArgsDict(TypedDict): ...

@pulumi.input_type
class StreamDestinationConfigGcsDestinationConfigAvroFileFormatArgs:
    def __init__(__self__) -> None: ...

class StreamDestinationConfigGcsDestinationConfigJsonFileFormatArgsDict(TypedDict):
    compression: NotRequired[pulumi.Input[_builtins.str]]
    schema_file_format: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamDestinationConfigGcsDestinationConfigJsonFileFormatArgs:
    def __init__(
        __self__,
        *,
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_file_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaFileFormat")
    def schema_file_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_file_format.setter
    def schema_file_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamRuleSetArgsDict(TypedDict):
    customization_rules: pulumi.Input[
        Sequence[pulumi.Input[StreamRuleSetCustomizationRuleArgsDict]]
    ]
    object_filter: pulumi.Input[StreamRuleSetObjectFilterArgsDict]
    ...

@pulumi.input_type
class StreamRuleSetArgs:
    def __init__(
        __self__,
        *,
        customization_rules: pulumi.Input[
            Sequence[pulumi.Input[StreamRuleSetCustomizationRuleArgs]]
        ],
        object_filter: pulumi.Input[StreamRuleSetObjectFilterArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customizationRules")
    def customization_rules(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[StreamRuleSetCustomizationRuleArgs]]]: ...
    @customization_rules.setter
    def customization_rules(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[StreamRuleSetCustomizationRuleArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectFilter")
    def object_filter(self) -> pulumi.Input[StreamRuleSetObjectFilterArgs]: ...
    @object_filter.setter
    def object_filter(self, value: pulumi.Input[StreamRuleSetObjectFilterArgs]): ...

class StreamRuleSetCustomizationRuleArgsDict(TypedDict):
    bigquery_clustering: NotRequired[
        pulumi.Input[StreamRuleSetCustomizationRuleBigqueryClusteringArgsDict]
    ]
    bigquery_partitioning: NotRequired[
        pulumi.Input[StreamRuleSetCustomizationRuleBigqueryPartitioningArgsDict]
    ]
    ...

@pulumi.input_type
class StreamRuleSetCustomizationRuleArgs:
    def __init__(
        __self__,
        *,
        bigquery_clustering: Optional[
            pulumi.Input[StreamRuleSetCustomizationRuleBigqueryClusteringArgs]
        ] = ...,
        bigquery_partitioning: Optional[
            pulumi.Input[StreamRuleSetCustomizationRuleBigqueryPartitioningArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryClustering")
    def bigquery_clustering(
        self,
    ) -> Optional[
        pulumi.Input[StreamRuleSetCustomizationRuleBigqueryClusteringArgs]
    ]: ...
    @bigquery_clustering.setter
    def bigquery_clustering(
        self,
        value: Optional[
            pulumi.Input[StreamRuleSetCustomizationRuleBigqueryClusteringArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryPartitioning")
    def bigquery_partitioning(
        self,
    ) -> Optional[
        pulumi.Input[StreamRuleSetCustomizationRuleBigqueryPartitioningArgs]
    ]: ...
    @bigquery_partitioning.setter
    def bigquery_partitioning(
        self,
        value: Optional[
            pulumi.Input[StreamRuleSetCustomizationRuleBigqueryPartitioningArgs]
        ],
    ): ...

class StreamRuleSetCustomizationRuleBigqueryClusteringArgsDict(TypedDict):
    columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class StreamRuleSetCustomizationRuleBigqueryClusteringArgs:
    def __init__(
        __self__, *, columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @columns.setter
    def columns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class StreamRuleSetCustomizationRuleBigqueryPartitioningArgsDict(TypedDict):
    ingestion_time_partition: NotRequired[
        pulumi.Input[
            StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartitionArgsDict
        ]
    ]
    integer_range_partition: NotRequired[
        pulumi.Input[
            StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartitionArgsDict
        ]
    ]
    require_partition_filter: NotRequired[pulumi.Input[_builtins.bool]]
    time_unit_partition: NotRequired[
        pulumi.Input[
            StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartitionArgsDict
        ]
    ]
    ...

@pulumi.input_type
class StreamRuleSetCustomizationRuleBigqueryPartitioningArgs:
    def __init__(
        __self__,
        *,
        ingestion_time_partition: Optional[
            pulumi.Input[
                StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartitionArgs
            ]
        ] = ...,
        integer_range_partition: Optional[
            pulumi.Input[
                StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartitionArgs
            ]
        ] = ...,
        require_partition_filter: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_unit_partition: Optional[
            pulumi.Input[
                StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartitionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionTimePartition")
    def ingestion_time_partition(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartitionArgs
        ]
    ]: ...
    @ingestion_time_partition.setter
    def ingestion_time_partition(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartitionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerRangePartition")
    def integer_range_partition(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartitionArgs
        ]
    ]: ...
    @integer_range_partition.setter
    def integer_range_partition(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartitionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_partition_filter.setter
    def require_partition_filter(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeUnitPartition")
    def time_unit_partition(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartitionArgs
        ]
    ]: ...
    @time_unit_partition.setter
    def time_unit_partition(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartitionArgs
            ]
        ],
    ): ...

class StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartitionArgsDict(
    TypedDict
):
    partitioning_time_granularity: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamRuleSetCustomizationRuleBigqueryPartitioningIngestionTimePartitionArgs:
    def __init__(
        __self__,
        *,
        partitioning_time_granularity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitioningTimeGranularity")
    def partitioning_time_granularity(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partitioning_time_granularity.setter
    def partitioning_time_granularity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartitionArgsDict(
    TypedDict
):
    column: pulumi.Input[_builtins.str]
    end: pulumi.Input[_builtins.int]
    interval: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class StreamRuleSetCustomizationRuleBigqueryPartitioningIntegerRangePartitionArgs:
    def __init__(
        __self__,
        *,
        column: pulumi.Input[_builtins.str],
        end: pulumi.Input[_builtins.int],
        interval: pulumi.Input[_builtins.int],
        start: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> pulumi.Input[_builtins.str]: ...
    @column.setter
    def column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> pulumi.Input[_builtins.int]: ...
    @end.setter
    def end(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> pulumi.Input[_builtins.int]: ...
    @start.setter
    def start(self, value: pulumi.Input[_builtins.int]): ...

class StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartitionArgsDict(
    TypedDict
):
    column: pulumi.Input[_builtins.str]
    partitioning_time_granularity: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamRuleSetCustomizationRuleBigqueryPartitioningTimeUnitPartitionArgs:
    def __init__(
        __self__,
        *,
        column: pulumi.Input[_builtins.str],
        partitioning_time_granularity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> pulumi.Input[_builtins.str]: ...
    @column.setter
    def column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="partitioningTimeGranularity")
    def partitioning_time_granularity(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partitioning_time_granularity.setter
    def partitioning_time_granularity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class StreamRuleSetObjectFilterArgsDict(TypedDict):
    source_object_identifier: NotRequired[
        pulumi.Input[StreamRuleSetObjectFilterSourceObjectIdentifierArgsDict]
    ]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterArgs:
    def __init__(
        __self__,
        *,
        source_object_identifier: Optional[
            pulumi.Input[StreamRuleSetObjectFilterSourceObjectIdentifierArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceObjectIdentifier")
    def source_object_identifier(
        self,
    ) -> Optional[
        pulumi.Input[StreamRuleSetObjectFilterSourceObjectIdentifierArgs]
    ]: ...
    @source_object_identifier.setter
    def source_object_identifier(
        self,
        value: Optional[
            pulumi.Input[StreamRuleSetObjectFilterSourceObjectIdentifierArgs]
        ],
    ): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierArgsDict(TypedDict):
    mongodb_identifier: NotRequired[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifierArgsDict
        ]
    ]
    mysql_identifier: NotRequired[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifierArgsDict
        ]
    ]
    oracle_identifier: NotRequired[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifierArgsDict
        ]
    ]
    postgresql_identifier: NotRequired[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifierArgsDict
        ]
    ]
    salesforce_identifier: NotRequired[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifierArgsDict
        ]
    ]
    spanner_identifier: NotRequired[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifierArgsDict
        ]
    ]
    sql_server_identifier: NotRequired[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifierArgsDict
        ]
    ]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierArgs:
    def __init__(
        __self__,
        *,
        mongodb_identifier: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifierArgs
            ]
        ] = ...,
        mysql_identifier: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifierArgs
            ]
        ] = ...,
        oracle_identifier: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifierArgs
            ]
        ] = ...,
        postgresql_identifier: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifierArgs
            ]
        ] = ...,
        salesforce_identifier: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifierArgs
            ]
        ] = ...,
        spanner_identifier: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifierArgs
            ]
        ] = ...,
        sql_server_identifier: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifierArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mongodbIdentifier")
    def mongodb_identifier(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifierArgs
        ]
    ]: ...
    @mongodb_identifier.setter
    def mongodb_identifier(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifierArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mysqlIdentifier")
    def mysql_identifier(
        self,
    ) -> Optional[
        pulumi.Input[StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifierArgs]
    ]: ...
    @mysql_identifier.setter
    def mysql_identifier(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifierArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oracleIdentifier")
    def oracle_identifier(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifierArgs
        ]
    ]: ...
    @oracle_identifier.setter
    def oracle_identifier(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifierArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlIdentifier")
    def postgresql_identifier(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifierArgs
        ]
    ]: ...
    @postgresql_identifier.setter
    def postgresql_identifier(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifierArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="salesforceIdentifier")
    def salesforce_identifier(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifierArgs
        ]
    ]: ...
    @salesforce_identifier.setter
    def salesforce_identifier(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifierArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spannerIdentifier")
    def spanner_identifier(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifierArgs
        ]
    ]: ...
    @spanner_identifier.setter
    def spanner_identifier(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifierArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerIdentifier")
    def sql_server_identifier(
        self,
    ) -> Optional[
        pulumi.Input[
            StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifierArgs
        ]
    ]: ...
    @sql_server_identifier.setter
    def sql_server_identifier(
        self,
        value: Optional[
            pulumi.Input[
                StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifierArgs
            ]
        ],
    ): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifierArgsDict(
    TypedDict
):
    collection: pulumi.Input[_builtins.str]
    database: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierMongodbIdentifierArgs:
    def __init__(
        __self__,
        *,
        collection: pulumi.Input[_builtins.str],
        database: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> pulumi.Input[_builtins.str]: ...
    @collection.setter
    def collection(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifierArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    table: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierMysqlIdentifierArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        table: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifierArgsDict(
    TypedDict
):
    schema: pulumi.Input[_builtins.str]
    table: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierOracleIdentifierArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        table: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifierArgsDict(
    TypedDict
):
    schema: pulumi.Input[_builtins.str]
    table: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierPostgresqlIdentifierArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        table: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifierArgsDict(
    TypedDict
):
    object_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierSalesforceIdentifierArgs:
    def __init__(__self__, *, object_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> pulumi.Input[_builtins.str]: ...
    @object_name.setter
    def object_name(self, value: pulumi.Input[_builtins.str]): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifierArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    schema: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierSpannerIdentifierArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifierArgsDict(
    TypedDict
):
    schema: pulumi.Input[_builtins.str]
    table: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class StreamRuleSetObjectFilterSourceObjectIdentifierSqlServerIdentifierArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        table: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...

class StreamSourceConfigArgsDict(TypedDict):
    source_connection_profile: pulumi.Input[_builtins.str]
    mongodb_source_config: NotRequired[
        pulumi.Input[StreamSourceConfigMongodbSourceConfigArgsDict]
    ]
    mysql_source_config: NotRequired[
        pulumi.Input[StreamSourceConfigMysqlSourceConfigArgsDict]
    ]
    oracle_source_config: NotRequired[
        pulumi.Input[StreamSourceConfigOracleSourceConfigArgsDict]
    ]
    postgresql_source_config: NotRequired[
        pulumi.Input[StreamSourceConfigPostgresqlSourceConfigArgsDict]
    ]
    salesforce_source_config: NotRequired[
        pulumi.Input[StreamSourceConfigSalesforceSourceConfigArgsDict]
    ]
    spanner_source_config: NotRequired[
        pulumi.Input[StreamSourceConfigSpannerSourceConfigArgsDict]
    ]
    sql_server_source_config: NotRequired[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigArgsDict]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigArgs:
    def __init__(
        __self__,
        *,
        source_connection_profile: pulumi.Input[_builtins.str],
        mongodb_source_config: Optional[
            pulumi.Input[StreamSourceConfigMongodbSourceConfigArgs]
        ] = ...,
        mysql_source_config: Optional[
            pulumi.Input[StreamSourceConfigMysqlSourceConfigArgs]
        ] = ...,
        oracle_source_config: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigArgs]
        ] = ...,
        postgresql_source_config: Optional[
            pulumi.Input[StreamSourceConfigPostgresqlSourceConfigArgs]
        ] = ...,
        salesforce_source_config: Optional[
            pulumi.Input[StreamSourceConfigSalesforceSourceConfigArgs]
        ] = ...,
        spanner_source_config: Optional[
            pulumi.Input[StreamSourceConfigSpannerSourceConfigArgs]
        ] = ...,
        sql_server_source_config: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceConnectionProfile")
    def source_connection_profile(self) -> pulumi.Input[_builtins.str]: ...
    @source_connection_profile.setter
    def source_connection_profile(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mongodbSourceConfig")
    def mongodb_source_config(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigMongodbSourceConfigArgs]]: ...
    @mongodb_source_config.setter
    def mongodb_source_config(
        self, value: Optional[pulumi.Input[StreamSourceConfigMongodbSourceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mysqlSourceConfig")
    def mysql_source_config(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigMysqlSourceConfigArgs]]: ...
    @mysql_source_config.setter
    def mysql_source_config(
        self, value: Optional[pulumi.Input[StreamSourceConfigMysqlSourceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oracleSourceConfig")
    def oracle_source_config(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigOracleSourceConfigArgs]]: ...
    @oracle_source_config.setter
    def oracle_source_config(
        self, value: Optional[pulumi.Input[StreamSourceConfigOracleSourceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSourceConfig")
    def postgresql_source_config(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigPostgresqlSourceConfigArgs]]: ...
    @postgresql_source_config.setter
    def postgresql_source_config(
        self,
        value: Optional[pulumi.Input[StreamSourceConfigPostgresqlSourceConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="salesforceSourceConfig")
    def salesforce_source_config(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigSalesforceSourceConfigArgs]]: ...
    @salesforce_source_config.setter
    def salesforce_source_config(
        self,
        value: Optional[pulumi.Input[StreamSourceConfigSalesforceSourceConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="spannerSourceConfig")
    def spanner_source_config(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigSpannerSourceConfigArgs]]: ...
    @spanner_source_config.setter
    def spanner_source_config(
        self, value: Optional[pulumi.Input[StreamSourceConfigSpannerSourceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerSourceConfig")
    def sql_server_source_config(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigSqlServerSourceConfigArgs]]: ...
    @sql_server_source_config.setter
    def sql_server_source_config(
        self, value: Optional[pulumi.Input[StreamSourceConfigSqlServerSourceConfigArgs]]
    ): ...

class StreamSourceConfigMongodbSourceConfigArgsDict(TypedDict):
    exclude_objects: NotRequired[
        pulumi.Input[StreamSourceConfigMongodbSourceConfigExcludeObjectsArgsDict]
    ]
    include_objects: NotRequired[
        pulumi.Input[StreamSourceConfigMongodbSourceConfigIncludeObjectsArgsDict]
    ]
    max_concurrent_backfill_tasks: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigArgs:
    def __init__(
        __self__,
        *,
        exclude_objects: Optional[
            pulumi.Input[StreamSourceConfigMongodbSourceConfigExcludeObjectsArgs]
        ] = ...,
        include_objects: Optional[
            pulumi.Input[StreamSourceConfigMongodbSourceConfigIncludeObjectsArgs]
        ] = ...,
        max_concurrent_backfill_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigMongodbSourceConfigExcludeObjectsArgs]
    ]: ...
    @exclude_objects.setter
    def exclude_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigMongodbSourceConfigExcludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigMongodbSourceConfigIncludeObjectsArgs]
    ]: ...
    @include_objects.setter
    def include_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigMongodbSourceConfigIncludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class StreamSourceConfigMongodbSourceConfigExcludeObjectsArgsDict(TypedDict):
    databases: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigExcludeObjectsArgs:
    def __init__(
        __self__,
        *,
        databases: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseArgs
                ]
            ]
        ]
    ]: ...
    @databases.setter
    def databases(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseArgsDict(TypedDict):
    collections: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionArgsDict
                ]
            ]
        ]
    ]
    database: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseArgs:
    def __init__(
        __self__,
        *,
        collections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionArgs
                    ]
                ]
            ]
        ] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collections(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionArgs
                ]
            ]
        ]
    ]: ...
    @collections.setter
    def collections(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionArgsDict(
    TypedDict
):
    collection: NotRequired[pulumi.Input[_builtins.str]]
    fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionFieldArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionArgs:
    def __init__(
        __self__,
        *,
        collection: Optional[pulumi.Input[_builtins.str]] = ...,
        fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionFieldArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection.setter
    def collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionFieldArgs
                ]
            ]
        ]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionFieldArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionFieldArgsDict(
    TypedDict
):
    field: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigExcludeObjectsDatabaseCollectionFieldArgs:
    def __init__(
        __self__, *, field: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigMongodbSourceConfigIncludeObjectsArgsDict(TypedDict):
    databases: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigIncludeObjectsArgs:
    def __init__(
        __self__,
        *,
        databases: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def databases(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseArgs
                ]
            ]
        ]
    ]: ...
    @databases.setter
    def databases(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseArgsDict(TypedDict):
    collections: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionArgsDict
                ]
            ]
        ]
    ]
    database: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseArgs:
    def __init__(
        __self__,
        *,
        collections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionArgs
                    ]
                ]
            ]
        ] = ...,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collections(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionArgs
                ]
            ]
        ]
    ]: ...
    @collections.setter
    def collections(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionArgsDict(
    TypedDict
):
    collection: NotRequired[pulumi.Input[_builtins.str]]
    fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionFieldArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionArgs:
    def __init__(
        __self__,
        *,
        collection: Optional[pulumi.Input[_builtins.str]] = ...,
        fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionFieldArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection.setter
    def collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionFieldArgs
                ]
            ]
        ]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionFieldArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionFieldArgsDict(
    TypedDict
):
    field: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigMongodbSourceConfigIncludeObjectsDatabaseCollectionFieldArgs:
    def __init__(
        __self__, *, field: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigMysqlSourceConfigArgsDict(TypedDict):
    binary_log_position: NotRequired[
        pulumi.Input[StreamSourceConfigMysqlSourceConfigBinaryLogPositionArgsDict]
    ]
    exclude_objects: NotRequired[
        pulumi.Input[StreamSourceConfigMysqlSourceConfigExcludeObjectsArgsDict]
    ]
    gtid: NotRequired[pulumi.Input[StreamSourceConfigMysqlSourceConfigGtidArgsDict]]
    include_objects: NotRequired[
        pulumi.Input[StreamSourceConfigMysqlSourceConfigIncludeObjectsArgsDict]
    ]
    max_concurrent_backfill_tasks: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_cdc_tasks: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigArgs:
    def __init__(
        __self__,
        *,
        binary_log_position: Optional[
            pulumi.Input[StreamSourceConfigMysqlSourceConfigBinaryLogPositionArgs]
        ] = ...,
        exclude_objects: Optional[
            pulumi.Input[StreamSourceConfigMysqlSourceConfigExcludeObjectsArgs]
        ] = ...,
        gtid: Optional[pulumi.Input[StreamSourceConfigMysqlSourceConfigGtidArgs]] = ...,
        include_objects: Optional[
            pulumi.Input[StreamSourceConfigMysqlSourceConfigIncludeObjectsArgs]
        ] = ...,
        max_concurrent_backfill_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
        max_concurrent_cdc_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="binaryLogPosition")
    def binary_log_position(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigMysqlSourceConfigBinaryLogPositionArgs]
    ]: ...
    @binary_log_position.setter
    def binary_log_position(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigMysqlSourceConfigBinaryLogPositionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigMysqlSourceConfigExcludeObjectsArgs]
    ]: ...
    @exclude_objects.setter
    def exclude_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigMysqlSourceConfigExcludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def gtid(
        self,
    ) -> Optional[pulumi.Input[StreamSourceConfigMysqlSourceConfigGtidArgs]]: ...
    @gtid.setter
    def gtid(
        self, value: Optional[pulumi.Input[StreamSourceConfigMysqlSourceConfigGtidArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigMysqlSourceConfigIncludeObjectsArgs]
    ]: ...
    @include_objects.setter
    def include_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigMysqlSourceConfigIncludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_cdc_tasks.setter
    def max_concurrent_cdc_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class StreamSourceConfigMysqlSourceConfigBinaryLogPositionArgsDict(TypedDict): ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigBinaryLogPositionArgs:
    def __init__(__self__) -> None: ...

class StreamSourceConfigMysqlSourceConfigExcludeObjectsArgsDict(TypedDict):
    mysql_databases: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigExcludeObjectsArgs:
    def __init__(
        __self__,
        *,
        mysql_databases: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseArgs
            ]
        ]
    ]: ...
    @mysql_databases.setter
    def mysql_databases(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    mysql_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        mysql_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mysqlTables")
    def mysql_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableArgs
                ]
            ]
        ]
    ]: ...
    @mysql_tables.setter
    def mysql_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    mysql_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        mysql_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                ]
            ]
        ]
    ]: ...
    @mysql_columns.setter
    def mysql_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgsDict(
    TypedDict
):
    collation: NotRequired[pulumi.Input[_builtins.str]]
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigExcludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs:
    def __init__(
        __self__,
        *,
        collation: Optional[pulumi.Input[_builtins.str]] = ...,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StreamSourceConfigMysqlSourceConfigGtidArgsDict(TypedDict): ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigGtidArgs:
    def __init__(__self__) -> None: ...

class StreamSourceConfigMysqlSourceConfigIncludeObjectsArgsDict(TypedDict):
    mysql_databases: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigIncludeObjectsArgs:
    def __init__(
        __self__,
        *,
        mysql_databases: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mysqlDatabases")
    def mysql_databases(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseArgs
            ]
        ]
    ]: ...
    @mysql_databases.setter
    def mysql_databases(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    mysql_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        mysql_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mysqlTables")
    def mysql_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableArgs
                ]
            ]
        ]
    ]: ...
    @mysql_tables.setter
    def mysql_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    mysql_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        mysql_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mysqlColumns")
    def mysql_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                ]
            ]
        ]
    ]: ...
    @mysql_columns.setter
    def mysql_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgsDict(
    TypedDict
):
    collation: NotRequired[pulumi.Input[_builtins.str]]
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class StreamSourceConfigMysqlSourceConfigIncludeObjectsMysqlDatabaseMysqlTableMysqlColumnArgs:
    def __init__(
        __self__,
        *,
        collation: Optional[pulumi.Input[_builtins.str]] = ...,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StreamSourceConfigOracleSourceConfigArgsDict(TypedDict):
    drop_large_objects: NotRequired[
        pulumi.Input[StreamSourceConfigOracleSourceConfigDropLargeObjectsArgsDict]
    ]
    exclude_objects: NotRequired[
        pulumi.Input[StreamSourceConfigOracleSourceConfigExcludeObjectsArgsDict]
    ]
    include_objects: NotRequired[
        pulumi.Input[StreamSourceConfigOracleSourceConfigIncludeObjectsArgsDict]
    ]
    max_concurrent_backfill_tasks: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_cdc_tasks: NotRequired[pulumi.Input[_builtins.int]]
    stream_large_objects: NotRequired[
        pulumi.Input[StreamSourceConfigOracleSourceConfigStreamLargeObjectsArgsDict]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigArgs:
    def __init__(
        __self__,
        *,
        drop_large_objects: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigDropLargeObjectsArgs]
        ] = ...,
        exclude_objects: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigExcludeObjectsArgs]
        ] = ...,
        include_objects: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigIncludeObjectsArgs]
        ] = ...,
        max_concurrent_backfill_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
        max_concurrent_cdc_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
        stream_large_objects: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigStreamLargeObjectsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dropLargeObjects")
    def drop_large_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigOracleSourceConfigDropLargeObjectsArgs]
    ]: ...
    @drop_large_objects.setter
    def drop_large_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigDropLargeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigOracleSourceConfigExcludeObjectsArgs]
    ]: ...
    @exclude_objects.setter
    def exclude_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigExcludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigOracleSourceConfigIncludeObjectsArgs]
    ]: ...
    @include_objects.setter
    def include_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigIncludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_cdc_tasks.setter
    def max_concurrent_cdc_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="streamLargeObjects")
    def stream_large_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigOracleSourceConfigStreamLargeObjectsArgs]
    ]: ...
    @stream_large_objects.setter
    def stream_large_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigOracleSourceConfigStreamLargeObjectsArgs]
        ],
    ): ...

class StreamSourceConfigOracleSourceConfigDropLargeObjectsArgsDict(TypedDict): ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigDropLargeObjectsArgs:
    def __init__(__self__) -> None: ...

class StreamSourceConfigOracleSourceConfigExcludeObjectsArgsDict(TypedDict):
    oracle_schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigExcludeObjectsArgs:
    def __init__(
        __self__,
        *,
        oracle_schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaArgs
            ]
        ]
    ]: ...
    @oracle_schemas.setter
    def oracle_schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    oracle_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        oracle_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oracleTables")
    def oracle_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableArgs
                ]
            ]
        ]
    ]: ...
    @oracle_tables.setter
    def oracle_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    oracle_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        oracle_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oracleColumns")
    def oracle_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumnArgs
                ]
            ]
        ]
    ]: ...
    @oracle_columns.setter
    def oracle_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigExcludeObjectsOracleSchemaOracleTableOracleColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigOracleSourceConfigIncludeObjectsArgsDict(TypedDict):
    oracle_schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigIncludeObjectsArgs:
    def __init__(
        __self__,
        *,
        oracle_schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oracleSchemas")
    def oracle_schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaArgs
            ]
        ]
    ]: ...
    @oracle_schemas.setter
    def oracle_schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    oracle_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        oracle_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oracleTables")
    def oracle_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableArgs
                ]
            ]
        ]
    ]: ...
    @oracle_tables.setter
    def oracle_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    oracle_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        oracle_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oracleColumns")
    def oracle_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumnArgs
                ]
            ]
        ]
    ]: ...
    @oracle_columns.setter
    def oracle_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigIncludeObjectsOracleSchemaOracleTableOracleColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigOracleSourceConfigStreamLargeObjectsArgsDict(TypedDict): ...

@pulumi.input_type
class StreamSourceConfigOracleSourceConfigStreamLargeObjectsArgs:
    def __init__(__self__) -> None: ...

class StreamSourceConfigPostgresqlSourceConfigArgsDict(TypedDict):
    publication: pulumi.Input[_builtins.str]
    replication_slot: pulumi.Input[_builtins.str]
    exclude_objects: NotRequired[
        pulumi.Input[StreamSourceConfigPostgresqlSourceConfigExcludeObjectsArgsDict]
    ]
    include_objects: NotRequired[
        pulumi.Input[StreamSourceConfigPostgresqlSourceConfigIncludeObjectsArgsDict]
    ]
    max_concurrent_backfill_tasks: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigArgs:
    def __init__(
        __self__,
        *,
        publication: pulumi.Input[_builtins.str],
        replication_slot: pulumi.Input[_builtins.str],
        exclude_objects: Optional[
            pulumi.Input[StreamSourceConfigPostgresqlSourceConfigExcludeObjectsArgs]
        ] = ...,
        include_objects: Optional[
            pulumi.Input[StreamSourceConfigPostgresqlSourceConfigIncludeObjectsArgs]
        ] = ...,
        max_concurrent_backfill_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def publication(self) -> pulumi.Input[_builtins.str]: ...
    @publication.setter
    def publication(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationSlot")
    def replication_slot(self) -> pulumi.Input[_builtins.str]: ...
    @replication_slot.setter
    def replication_slot(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigPostgresqlSourceConfigExcludeObjectsArgs]
    ]: ...
    @exclude_objects.setter
    def exclude_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigPostgresqlSourceConfigExcludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigPostgresqlSourceConfigIncludeObjectsArgs]
    ]: ...
    @include_objects.setter
    def include_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigPostgresqlSourceConfigIncludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsArgsDict(TypedDict):
    postgresql_schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsArgs:
    def __init__(
        __self__,
        *,
        postgresql_schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaArgs
            ]
        ]
    ]: ...
    @postgresql_schemas.setter
    def postgresql_schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaArgsDict(
    TypedDict
):
    schema: pulumi.Input[_builtins.str]
    postgresql_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        postgresql_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTableArgs
                ]
            ]
        ]
    ]: ...
    @postgresql_tables.setter
    def postgresql_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    postgresql_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        postgresql_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                ]
            ]
        ]
    ]: ...
    @postgresql_columns.setter
    def postgresql_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigExcludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsArgsDict(TypedDict):
    postgresql_schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsArgs:
    def __init__(
        __self__,
        *,
        postgresql_schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlSchemas")
    def postgresql_schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaArgs
            ]
        ]
    ]: ...
    @postgresql_schemas.setter
    def postgresql_schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaArgsDict(
    TypedDict
):
    schema: pulumi.Input[_builtins.str]
    postgresql_tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        postgresql_tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlTables")
    def postgresql_tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTableArgs
                ]
            ]
        ]
    ]: ...
    @postgresql_tables.setter
    def postgresql_tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    postgresql_columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        postgresql_columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlColumns")
    def postgresql_columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                ]
            ]
        ]
    ]: ...
    @postgresql_columns.setter
    def postgresql_columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigPostgresqlSourceConfigIncludeObjectsPostgresqlSchemaPostgresqlTablePostgresqlColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigSalesforceSourceConfigArgsDict(TypedDict):
    polling_interval: pulumi.Input[_builtins.str]
    exclude_objects: NotRequired[
        pulumi.Input[StreamSourceConfigSalesforceSourceConfigExcludeObjectsArgsDict]
    ]
    include_objects: NotRequired[
        pulumi.Input[StreamSourceConfigSalesforceSourceConfigIncludeObjectsArgsDict]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSalesforceSourceConfigArgs:
    def __init__(
        __self__,
        *,
        polling_interval: pulumi.Input[_builtins.str],
        exclude_objects: Optional[
            pulumi.Input[StreamSourceConfigSalesforceSourceConfigExcludeObjectsArgs]
        ] = ...,
        include_objects: Optional[
            pulumi.Input[StreamSourceConfigSalesforceSourceConfigIncludeObjectsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pollingInterval")
    def polling_interval(self) -> pulumi.Input[_builtins.str]: ...
    @polling_interval.setter
    def polling_interval(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSalesforceSourceConfigExcludeObjectsArgs]
    ]: ...
    @exclude_objects.setter
    def exclude_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSalesforceSourceConfigExcludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSalesforceSourceConfigIncludeObjectsArgs]
    ]: ...
    @include_objects.setter
    def include_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSalesforceSourceConfigIncludeObjectsArgs]
        ],
    ): ...

class StreamSourceConfigSalesforceSourceConfigExcludeObjectsArgsDict(TypedDict):
    objects: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSalesforceSourceConfigExcludeObjectsArgs:
    def __init__(
        __self__,
        *,
        objects: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def objects(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectArgs
            ]
        ]
    ]: ...
    @objects.setter
    def objects(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectArgsDict(TypedDict):
    fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectFieldArgsDict
                ]
            ]
        ]
    ]
    object_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectArgs:
    def __init__(
        __self__,
        *,
        fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectFieldArgs
                    ]
                ]
            ]
        ] = ...,
        object_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectFieldArgs
                ]
            ]
        ]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_name.setter
    def object_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectFieldArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigSalesforceSourceConfigExcludeObjectsObjectFieldArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigSalesforceSourceConfigIncludeObjectsArgsDict(TypedDict):
    objects: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSalesforceSourceConfigIncludeObjectsArgs:
    def __init__(
        __self__,
        *,
        objects: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def objects(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectArgs
            ]
        ]
    ]: ...
    @objects.setter
    def objects(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectArgsDict(TypedDict):
    fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectFieldArgsDict
                ]
            ]
        ]
    ]
    object_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectArgs:
    def __init__(
        __self__,
        *,
        fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectFieldArgs
                    ]
                ]
            ]
        ] = ...,
        object_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectFieldArgs
                ]
            ]
        ]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectName")
    def object_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_name.setter
    def object_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectFieldArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigSalesforceSourceConfigIncludeObjectsObjectFieldArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigSpannerSourceConfigArgsDict(TypedDict):
    backfill_data_boost_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    change_stream_name: NotRequired[pulumi.Input[_builtins.str]]
    exclude_objects: NotRequired[
        pulumi.Input[StreamSourceConfigSpannerSourceConfigExcludeObjectsArgsDict]
    ]
    fgac_role: NotRequired[pulumi.Input[_builtins.str]]
    include_objects: NotRequired[
        pulumi.Input[StreamSourceConfigSpannerSourceConfigIncludeObjectsArgsDict]
    ]
    max_concurrent_backfill_tasks: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_cdc_tasks: NotRequired[pulumi.Input[_builtins.int]]
    spanner_rpc_priority: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigArgs:
    def __init__(
        __self__,
        *,
        backfill_data_boost_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        change_stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_objects: Optional[
            pulumi.Input[StreamSourceConfigSpannerSourceConfigExcludeObjectsArgs]
        ] = ...,
        fgac_role: Optional[pulumi.Input[_builtins.str]] = ...,
        include_objects: Optional[
            pulumi.Input[StreamSourceConfigSpannerSourceConfigIncludeObjectsArgs]
        ] = ...,
        max_concurrent_backfill_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
        max_concurrent_cdc_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
        spanner_rpc_priority: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backfillDataBoostEnabled")
    def backfill_data_boost_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @backfill_data_boost_enabled.setter
    def backfill_data_boost_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="changeStreamName")
    def change_stream_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @change_stream_name.setter
    def change_stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSpannerSourceConfigExcludeObjectsArgs]
    ]: ...
    @exclude_objects.setter
    def exclude_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSpannerSourceConfigExcludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fgacRole")
    def fgac_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fgac_role.setter
    def fgac_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSpannerSourceConfigIncludeObjectsArgs]
    ]: ...
    @include_objects.setter
    def include_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSpannerSourceConfigIncludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_cdc_tasks.setter
    def max_concurrent_cdc_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spannerRpcPriority")
    def spanner_rpc_priority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @spanner_rpc_priority.setter
    def spanner_rpc_priority(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamSourceConfigSpannerSourceConfigExcludeObjectsArgsDict(TypedDict):
    schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigExcludeObjectsArgs:
    def __init__(
        __self__,
        *,
        schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaArgs]
        ]
    ]: ...
    @schemas.setter
    def schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableArgs
                ]
            ]
        ]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableArgsDict(TypedDict):
    table: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    is_primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigExcludeObjectsSchemaTableColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        is_primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isPrimaryKey")
    def is_primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_primary_key.setter
    def is_primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigSpannerSourceConfigIncludeObjectsArgsDict(TypedDict):
    schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigIncludeObjectsArgs:
    def __init__(
        __self__,
        *,
        schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaArgs]
        ]
    ]: ...
    @schemas.setter
    def schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableArgs
                ]
            ]
        ]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableArgsDict(TypedDict):
    table: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    is_primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigSpannerSourceConfigIncludeObjectsSchemaTableColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        is_primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isPrimaryKey")
    def is_primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_primary_key.setter
    def is_primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigSqlServerSourceConfigArgsDict(TypedDict):
    change_tables: NotRequired[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigChangeTablesArgsDict]
    ]
    exclude_objects: NotRequired[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigExcludeObjectsArgsDict]
    ]
    include_objects: NotRequired[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigIncludeObjectsArgsDict]
    ]
    max_concurrent_backfill_tasks: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_cdc_tasks: NotRequired[pulumi.Input[_builtins.int]]
    transaction_logs: NotRequired[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigTransactionLogsArgsDict]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigArgs:
    def __init__(
        __self__,
        *,
        change_tables: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigChangeTablesArgs]
        ] = ...,
        exclude_objects: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigExcludeObjectsArgs]
        ] = ...,
        include_objects: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigIncludeObjectsArgs]
        ] = ...,
        max_concurrent_backfill_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
        max_concurrent_cdc_tasks: Optional[pulumi.Input[_builtins.int]] = ...,
        transaction_logs: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigTransactionLogsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="changeTables")
    def change_tables(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigChangeTablesArgs]
    ]: ...
    @change_tables.setter
    def change_tables(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigChangeTablesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeObjects")
    def exclude_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigExcludeObjectsArgs]
    ]: ...
    @exclude_objects.setter
    def exclude_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigExcludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeObjects")
    def include_objects(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigIncludeObjectsArgs]
    ]: ...
    @include_objects.setter
    def include_objects(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigIncludeObjectsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentBackfillTasks")
    def max_concurrent_backfill_tasks(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_backfill_tasks.setter
    def max_concurrent_backfill_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentCdcTasks")
    def max_concurrent_cdc_tasks(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_cdc_tasks.setter
    def max_concurrent_cdc_tasks(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transactionLogs")
    def transaction_logs(
        self,
    ) -> Optional[
        pulumi.Input[StreamSourceConfigSqlServerSourceConfigTransactionLogsArgs]
    ]: ...
    @transaction_logs.setter
    def transaction_logs(
        self,
        value: Optional[
            pulumi.Input[StreamSourceConfigSqlServerSourceConfigTransactionLogsArgs]
        ],
    ): ...

class StreamSourceConfigSqlServerSourceConfigChangeTablesArgsDict(TypedDict): ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigChangeTablesArgs:
    def __init__(__self__) -> None: ...

class StreamSourceConfigSqlServerSourceConfigExcludeObjectsArgsDict(TypedDict):
    schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjectsArgs:
    def __init__(
        __self__,
        *,
        schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaArgs
            ]
        ]
    ]: ...
    @schemas.setter
    def schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableArgs
                ]
            ]
        ]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigExcludeObjectsSchemaTableColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigSqlServerSourceConfigIncludeObjectsArgsDict(TypedDict):
    schemas: pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjectsArgs:
    def __init__(
        __self__,
        *,
        schemas: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaArgs
            ]
        ]
    ]: ...
    @schemas.setter
    def schemas(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaArgs
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaArgsDict(TypedDict):
    schema: pulumi.Input[_builtins.str]
    tables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaArgs:
    def __init__(
        __self__,
        *,
        schema: pulumi.Input[_builtins.str],
        tables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableArgs
                ]
            ]
        ]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableArgsDict(
    TypedDict
):
    table: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumnArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> pulumi.Input[_builtins.str]: ...
    @table.setter
    def table(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumnArgs
                    ]
                ]
            ]
        ],
    ): ...

class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumnArgsDict(
    TypedDict
):
    column: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    length: NotRequired[pulumi.Input[_builtins.int]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    ordinal_position: NotRequired[pulumi.Input[_builtins.int]]
    precision: NotRequired[pulumi.Input[_builtins.int]]
    primary_key: NotRequired[pulumi.Input[_builtins.bool]]
    scale: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigIncludeObjectsSchemaTableColumnArgs:
    def __init__(
        __self__,
        *,
        column: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        length: Optional[pulumi.Input[_builtins.int]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        ordinal_position: Optional[pulumi.Input[_builtins.int]] = ...,
        precision: Optional[pulumi.Input[_builtins.int]] = ...,
        primary_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column.setter
    def column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @length.setter
    def length(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ordinalPosition")
    def ordinal_position(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ordinal_position.setter
    def ordinal_position(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def precision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @precision.setter
    def precision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @primary_key.setter
    def primary_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class StreamSourceConfigSqlServerSourceConfigTransactionLogsArgsDict(TypedDict): ...

@pulumi.input_type
class StreamSourceConfigSqlServerSourceConfigTransactionLogsArgs:
    def __init__(__self__) -> None: ...
