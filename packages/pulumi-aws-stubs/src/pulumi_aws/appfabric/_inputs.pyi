import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppAuthorizationConnectionAuthRequestArgs",
    "AppAuthorizationConnectionAuthRequestArgsDict",
    "AppAuthorizationConnectionTenantArgs",
    "AppAuthorizationConnectionTenantArgsDict",
    "AppAuthorizationConnectionTimeoutsArgs",
    "AppAuthorizationConnectionTimeoutsArgsDict",
    "AppAuthorizationCredentialArgs",
    "AppAuthorizationCredentialArgsDict",
    "AppAuthorizationCredentialApiKeyCredentialArgs",
    "AppAuthorizationCredentialApiKeyCredentialArgsDict",
    "AppAuthorizationCredentialOauth2CredentialArgs",
    "AppAuthorizationCredentialOauth2CredentialArgsDict",
    "AppAuthorizationTenantArgs",
    "AppAuthorizationTenantArgsDict",
    "AppAuthorizationTimeoutsArgs",
    "AppAuthorizationTimeoutsArgsDict",
    "IngestionDestinationDestinationConfigurationArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "IngestionDestinationProcessingConfigurationArgs",
    ...,
    ...,
    ...,
    "IngestionDestinationTimeoutsArgs",
    "IngestionDestinationTimeoutsArgsDict",
]

class AppAuthorizationConnectionAuthRequestArgsDict(TypedDict):
    code: pulumi.Input[_builtins.str]
    redirect_uri: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AppAuthorizationConnectionAuthRequestArgs:
    def __init__(
        __self__,
        *,
        code: pulumi.Input[_builtins.str],
        redirect_uri: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> pulumi.Input[_builtins.str]: ...
    @code.setter
    def code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> pulumi.Input[_builtins.str]: ...
    @redirect_uri.setter
    def redirect_uri(self, value: pulumi.Input[_builtins.str]): ...

class AppAuthorizationConnectionTenantArgsDict(TypedDict):
    tenant_display_name: pulumi.Input[_builtins.str]
    tenant_identifier: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AppAuthorizationConnectionTenantArgs:
    def __init__(
        __self__,
        *,
        tenant_display_name: pulumi.Input[_builtins.str],
        tenant_identifier: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantDisplayName")
    def tenant_display_name(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_display_name.setter
    def tenant_display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantIdentifier")
    def tenant_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_identifier.setter
    def tenant_identifier(self, value: pulumi.Input[_builtins.str]): ...

class AppAuthorizationConnectionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppAuthorizationConnectionTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppAuthorizationCredentialArgsDict(TypedDict):
    api_key_credentials: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppAuthorizationCredentialApiKeyCredentialArgsDict]]
        ]
    ]
    oauth2_credential: NotRequired[
        pulumi.Input[AppAuthorizationCredentialOauth2CredentialArgsDict]
    ]
    ...

@pulumi.input_type
class AppAuthorizationCredentialArgs:
    def __init__(
        __self__,
        *,
        api_key_credentials: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppAuthorizationCredentialApiKeyCredentialArgs]]
            ]
        ] = ...,
        oauth2_credential: Optional[
            pulumi.Input[AppAuthorizationCredentialOauth2CredentialArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyCredentials")
    def api_key_credentials(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppAuthorizationCredentialApiKeyCredentialArgs]]
        ]
    ]: ...
    @api_key_credentials.setter
    def api_key_credentials(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppAuthorizationCredentialApiKeyCredentialArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauth2Credential")
    def oauth2_credential(
        self,
    ) -> Optional[pulumi.Input[AppAuthorizationCredentialOauth2CredentialArgs]]: ...
    @oauth2_credential.setter
    def oauth2_credential(
        self,
        value: Optional[pulumi.Input[AppAuthorizationCredentialOauth2CredentialArgs]],
    ): ...

class AppAuthorizationCredentialApiKeyCredentialArgsDict(TypedDict):
    api_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AppAuthorizationCredentialApiKeyCredentialArgs:
    def __init__(__self__, *, api_key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[_builtins.str]: ...
    @api_key.setter
    def api_key(self, value: pulumi.Input[_builtins.str]): ...

class AppAuthorizationCredentialOauth2CredentialArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AppAuthorizationCredentialOauth2CredentialArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]: ...
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): ...

class AppAuthorizationTenantArgsDict(TypedDict):
    tenant_display_name: pulumi.Input[_builtins.str]
    tenant_identifier: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AppAuthorizationTenantArgs:
    def __init__(
        __self__,
        *,
        tenant_display_name: pulumi.Input[_builtins.str],
        tenant_identifier: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tenantDisplayName")
    def tenant_display_name(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_display_name.setter
    def tenant_display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tenantIdentifier")
    def tenant_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @tenant_identifier.setter
    def tenant_identifier(self, value: pulumi.Input[_builtins.str]): ...

class AppAuthorizationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppAuthorizationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IngestionDestinationDestinationConfigurationArgsDict(TypedDict):
    audit_log: pulumi.Input[
        IngestionDestinationDestinationConfigurationAuditLogArgsDict
    ]
    ...

@pulumi.input_type
class IngestionDestinationDestinationConfigurationArgs:
    def __init__(
        __self__,
        *,
        audit_log: pulumi.Input[
            IngestionDestinationDestinationConfigurationAuditLogArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLog")
    def audit_log(
        self,
    ) -> pulumi.Input[IngestionDestinationDestinationConfigurationAuditLogArgs]: ...
    @audit_log.setter
    def audit_log(
        self,
        value: pulumi.Input[IngestionDestinationDestinationConfigurationAuditLogArgs],
    ): ...

class IngestionDestinationDestinationConfigurationAuditLogArgsDict(TypedDict):
    destination: pulumi.Input[
        IngestionDestinationDestinationConfigurationAuditLogDestinationArgsDict
    ]
    ...

@pulumi.input_type
class IngestionDestinationDestinationConfigurationAuditLogArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[
            IngestionDestinationDestinationConfigurationAuditLogDestinationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> pulumi.Input[
        IngestionDestinationDestinationConfigurationAuditLogDestinationArgs
    ]: ...
    @destination.setter
    def destination(
        self,
        value: pulumi.Input[
            IngestionDestinationDestinationConfigurationAuditLogDestinationArgs
        ],
    ): ...

class IngestionDestinationDestinationConfigurationAuditLogDestinationArgsDict(
    TypedDict
):
    firehose_stream: NotRequired[
        pulumi.Input[
            IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStreamArgsDict
        ]
    ]
    s3_bucket: NotRequired[
        pulumi.Input[
            IngestionDestinationDestinationConfigurationAuditLogDestinationS3BucketArgsDict
        ]
    ]
    ...

@pulumi.input_type
class IngestionDestinationDestinationConfigurationAuditLogDestinationArgs:
    def __init__(
        __self__,
        *,
        firehose_stream: Optional[
            pulumi.Input[
                IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStreamArgs
            ]
        ] = ...,
        s3_bucket: Optional[
            pulumi.Input[
                IngestionDestinationDestinationConfigurationAuditLogDestinationS3BucketArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="firehoseStream")
    def firehose_stream(
        self,
    ) -> Optional[
        pulumi.Input[
            IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStreamArgs
        ]
    ]: ...
    @firehose_stream.setter
    def firehose_stream(
        self,
        value: Optional[
            pulumi.Input[
                IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStreamArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(
        self,
    ) -> Optional[
        pulumi.Input[
            IngestionDestinationDestinationConfigurationAuditLogDestinationS3BucketArgs
        ]
    ]: ...
    @s3_bucket.setter
    def s3_bucket(
        self,
        value: Optional[
            pulumi.Input[
                IngestionDestinationDestinationConfigurationAuditLogDestinationS3BucketArgs
            ]
        ],
    ): ...

class IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStreamArgsDict(
    TypedDict
):
    stream_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStreamArgs:
    def __init__(__self__, *, stream_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> pulumi.Input[_builtins.str]: ...
    @stream_name.setter
    def stream_name(self, value: pulumi.Input[_builtins.str]): ...

class IngestionDestinationDestinationConfigurationAuditLogDestinationS3BucketArgsDict(
    TypedDict
):
    bucket_name: pulumi.Input[_builtins.str]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IngestionDestinationDestinationConfigurationAuditLogDestinationS3BucketArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IngestionDestinationProcessingConfigurationArgsDict(TypedDict):
    audit_log: pulumi.Input[IngestionDestinationProcessingConfigurationAuditLogArgsDict]
    ...

@pulumi.input_type
class IngestionDestinationProcessingConfigurationArgs:
    def __init__(
        __self__,
        *,
        audit_log: pulumi.Input[
            IngestionDestinationProcessingConfigurationAuditLogArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLog")
    def audit_log(
        self,
    ) -> pulumi.Input[IngestionDestinationProcessingConfigurationAuditLogArgs]: ...
    @audit_log.setter
    def audit_log(
        self,
        value: pulumi.Input[IngestionDestinationProcessingConfigurationAuditLogArgs],
    ): ...

class IngestionDestinationProcessingConfigurationAuditLogArgsDict(TypedDict):
    format: pulumi.Input[_builtins.str]
    schema: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class IngestionDestinationProcessingConfigurationAuditLogArgs:
    def __init__(
        __self__,
        *,
        format: pulumi.Input[_builtins.str],
        schema: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]: ...
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[_builtins.str]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[_builtins.str]): ...

class IngestionDestinationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IngestionDestinationTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...
