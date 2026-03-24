

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppAuthorizationConnectionAuthRequest', 'AppAuthorizationConnectionTenant', 'AppAuthorizationConnectionTimeouts', 'AppAuthorizationCredential', 'AppAuthorizationCredentialApiKeyCredential', 'AppAuthorizationCredentialOauth2Credential', 'AppAuthorizationTenant', 'AppAuthorizationTimeouts', 'IngestionDestinationDestinationConfiguration', ..., ..., ..., ..., 'IngestionDestinationProcessingConfiguration', ..., 'IngestionDestinationTimeouts']
@pulumi.output_type
class AppAuthorizationConnectionAuthRequest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code: _builtins.str, redirect_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AppAuthorizationConnectionTenant(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tenant_display_name: _builtins.str, tenant_identifier: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantDisplayName")
    def tenant_display_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantIdentifier")
    def tenant_identifier(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AppAuthorizationConnectionTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppAuthorizationCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_credentials: Optional[Sequence[outputs.AppAuthorizationCredentialApiKeyCredential]] = ..., oauth2_credential: Optional[outputs.AppAuthorizationCredentialOauth2Credential] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyCredentials")
    def api_key_credentials(self) -> Optional[Sequence[outputs.AppAuthorizationCredentialApiKeyCredential]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2Credential")
    def oauth2_credential(self) -> Optional[outputs.AppAuthorizationCredentialOauth2Credential]:
        
        ...
    


@pulumi.output_type
class AppAuthorizationCredentialApiKeyCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AppAuthorizationCredentialOauth2Credential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, client_secret: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AppAuthorizationTenant(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tenant_display_name: _builtins.str, tenant_identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantDisplayName")
    def tenant_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantIdentifier")
    def tenant_identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AppAuthorizationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IngestionDestinationDestinationConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audit_log: outputs.IngestionDestinationDestinationConfigurationAuditLog) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditLog")
    def audit_log(self) -> outputs.IngestionDestinationDestinationConfigurationAuditLog:
        
        ...
    


@pulumi.output_type
class IngestionDestinationDestinationConfigurationAuditLog(dict):
    def __init__(__self__, *, destination: outputs.IngestionDestinationDestinationConfigurationAuditLogDestination) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.IngestionDestinationDestinationConfigurationAuditLogDestination:
        
        ...
    


@pulumi.output_type
class IngestionDestinationDestinationConfigurationAuditLogDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, firehose_stream: Optional[outputs.IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStream] = ..., s3_bucket: Optional[outputs.IngestionDestinationDestinationConfigurationAuditLogDestinationS3Bucket] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firehoseStream")
    def firehose_stream(self) -> Optional[outputs.IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStream]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[outputs.IngestionDestinationDestinationConfigurationAuditLogDestinationS3Bucket]:
        
        ...
    


@pulumi.output_type
class IngestionDestinationDestinationConfigurationAuditLogDestinationFirehoseStream(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, stream_name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class IngestionDestinationDestinationConfigurationAuditLogDestinationS3Bucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IngestionDestinationProcessingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audit_log: outputs.IngestionDestinationProcessingConfigurationAuditLog) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditLog")
    def audit_log(self) -> outputs.IngestionDestinationProcessingConfigurationAuditLog:
        
        ...
    


@pulumi.output_type
class IngestionDestinationProcessingConfigurationAuditLog(dict):
    def __init__(__self__, *, format: _builtins.str, schema: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IngestionDestinationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


