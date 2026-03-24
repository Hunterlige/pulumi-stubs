

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['JobAppEngineHttpTarget', 'JobAppEngineHttpTargetAppEngineRouting', 'JobHttpTarget', 'JobHttpTargetOauthToken', 'JobHttpTargetOidcToken', 'JobPubsubTarget', 'JobRetryConfig']
@pulumi.output_type
class JobAppEngineHttpTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, relative_uri: _builtins.str, app_engine_routing: Optional[outputs.JobAppEngineHttpTargetAppEngineRouting] = ..., body: Optional[_builtins.str] = ..., headers: Optional[Mapping[str, _builtins.str]] = ..., http_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativeUri")
    def relative_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineRouting")
    def app_engine_routing(self) -> Optional[outputs.JobAppEngineHttpTargetAppEngineRouting]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobAppEngineHttpTargetAppEngineRouting(dict):
    def __init__(__self__, *, instance: Optional[_builtins.str] = ..., service: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobHttpTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, uri: _builtins.str, body: Optional[_builtins.str] = ..., headers: Optional[Mapping[str, _builtins.str]] = ..., http_method: Optional[_builtins.str] = ..., oauth_token: Optional[outputs.JobHttpTargetOauthToken] = ..., oidc_token: Optional[outputs.JobHttpTargetOidcToken] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[outputs.JobHttpTargetOauthToken]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[outputs.JobHttpTargetOidcToken]:
        
        ...
    


@pulumi.output_type
class JobHttpTargetOauthToken(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account_email: _builtins.str, scope: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobHttpTargetOidcToken(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account_email: _builtins.str, audience: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobPubsubTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, topic_name: _builtins.str, attributes: Optional[Mapping[str, _builtins.str]] = ..., data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobRetryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_backoff_duration: Optional[_builtins.str] = ..., max_doublings: Optional[_builtins.int] = ..., max_retry_duration: Optional[_builtins.str] = ..., min_backoff_duration: Optional[_builtins.str] = ..., retry_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxBackoffDuration")
    def max_backoff_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDoublings")
    def max_doublings(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetryDuration")
    def max_retry_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minBackoffDuration")
    def min_backoff_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[_builtins.int]:
        
        ...
    


