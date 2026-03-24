

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['QueueAppEngineRoutingOverride', 'QueueHttpTarget', 'QueueHttpTargetHeaderOverride', 'QueueHttpTargetHeaderOverrideHeader', 'QueueHttpTargetOauthToken', 'QueueHttpTargetOidcToken', 'QueueHttpTargetUriOverride', 'QueueHttpTargetUriOverridePathOverride', 'QueueHttpTargetUriOverrideQueryOverride', 'QueueIamBindingCondition', 'QueueIamMemberCondition', 'QueueRateLimits', 'QueueRetryConfig', 'QueueStackdriverLoggingConfig']
@pulumi.output_type
class QueueAppEngineRoutingOverride(dict):
    def __init__(__self__, *, host: Optional[_builtins.str] = ..., instance: Optional[_builtins.str] = ..., service: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
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
class QueueHttpTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_overrides: Optional[Sequence[outputs.QueueHttpTargetHeaderOverride]] = ..., http_method: Optional[_builtins.str] = ..., oauth_token: Optional[outputs.QueueHttpTargetOauthToken] = ..., oidc_token: Optional[outputs.QueueHttpTargetOidcToken] = ..., uri_override: Optional[outputs.QueueHttpTargetUriOverride] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOverrides")
    def header_overrides(self) -> Optional[Sequence[outputs.QueueHttpTargetHeaderOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[outputs.QueueHttpTargetOauthToken]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[outputs.QueueHttpTargetOidcToken]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriOverride")
    def uri_override(self) -> Optional[outputs.QueueHttpTargetUriOverride]:
        
        ...
    


@pulumi.output_type
class QueueHttpTargetHeaderOverride(dict):
    def __init__(__self__, *, header: outputs.QueueHttpTargetHeaderOverrideHeader) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> outputs.QueueHttpTargetHeaderOverrideHeader:
        
        ...
    


@pulumi.output_type
class QueueHttpTargetHeaderOverrideHeader(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class QueueHttpTargetOauthToken(dict):
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
class QueueHttpTargetOidcToken(dict):
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
class QueueHttpTargetUriOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, host: Optional[_builtins.str] = ..., path_override: Optional[outputs.QueueHttpTargetUriOverridePathOverride] = ..., port: Optional[_builtins.str] = ..., query_override: Optional[outputs.QueueHttpTargetUriOverrideQueryOverride] = ..., scheme: Optional[_builtins.str] = ..., uri_override_enforce_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathOverride")
    def path_override(self) -> Optional[outputs.QueueHttpTargetUriOverridePathOverride]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryOverride")
    def query_override(self) -> Optional[outputs.QueueHttpTargetUriOverrideQueryOverride]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriOverrideEnforceMode")
    def uri_override_enforce_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QueueHttpTargetUriOverridePathOverride(dict):
    def __init__(__self__, *, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QueueHttpTargetUriOverrideQueryOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, query_params: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParams")
    def query_params(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QueueIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class QueueIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class QueueRateLimits(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_burst_size: Optional[_builtins.int] = ..., max_concurrent_dispatches: Optional[_builtins.int] = ..., max_dispatches_per_second: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxBurstSize")
    def max_burst_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentDispatches")
    def max_concurrent_dispatches(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDispatchesPerSecond")
    def max_dispatches_per_second(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class QueueRetryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_attempts: Optional[_builtins.int] = ..., max_backoff: Optional[_builtins.str] = ..., max_doublings: Optional[_builtins.int] = ..., max_retry_duration: Optional[_builtins.str] = ..., min_backoff: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxBackoff")
    def max_backoff(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="minBackoff")
    def min_backoff(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QueueStackdriverLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sampling_ratio: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="samplingRatio")
    def sampling_ratio(self) -> _builtins.float:
        
        ...
    


