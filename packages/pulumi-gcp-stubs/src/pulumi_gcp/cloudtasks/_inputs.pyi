import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "QueueAppEngineRoutingOverrideArgs",
    "QueueAppEngineRoutingOverrideArgsDict",
    "QueueHttpTargetArgs",
    "QueueHttpTargetArgsDict",
    "QueueHttpTargetHeaderOverrideArgs",
    "QueueHttpTargetHeaderOverrideArgsDict",
    "QueueHttpTargetHeaderOverrideHeaderArgs",
    "QueueHttpTargetHeaderOverrideHeaderArgsDict",
    "QueueHttpTargetOauthTokenArgs",
    "QueueHttpTargetOauthTokenArgsDict",
    "QueueHttpTargetOidcTokenArgs",
    "QueueHttpTargetOidcTokenArgsDict",
    "QueueHttpTargetUriOverrideArgs",
    "QueueHttpTargetUriOverrideArgsDict",
    "QueueHttpTargetUriOverridePathOverrideArgs",
    "QueueHttpTargetUriOverridePathOverrideArgsDict",
    "QueueHttpTargetUriOverrideQueryOverrideArgs",
    "QueueHttpTargetUriOverrideQueryOverrideArgsDict",
    "QueueIamBindingConditionArgs",
    "QueueIamBindingConditionArgsDict",
    "QueueIamMemberConditionArgs",
    "QueueIamMemberConditionArgsDict",
    "QueueRateLimitsArgs",
    "QueueRateLimitsArgsDict",
    "QueueRetryConfigArgs",
    "QueueRetryConfigArgsDict",
    "QueueStackdriverLoggingConfigArgs",
    "QueueStackdriverLoggingConfigArgsDict",
]

class QueueAppEngineRoutingOverrideArgsDict(TypedDict):
    host: NotRequired[pulumi.Input[_builtins.str]]
    instance: NotRequired[pulumi.Input[_builtins.str]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueAppEngineRoutingOverrideArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueHttpTargetArgsDict(TypedDict):
    header_overrides: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[QueueHttpTargetHeaderOverrideArgsDict]]]
    ]
    http_method: NotRequired[pulumi.Input[_builtins.str]]
    oauth_token: NotRequired[pulumi.Input[QueueHttpTargetOauthTokenArgsDict]]
    oidc_token: NotRequired[pulumi.Input[QueueHttpTargetOidcTokenArgsDict]]
    uri_override: NotRequired[pulumi.Input[QueueHttpTargetUriOverrideArgsDict]]

@pulumi.input_type
class QueueHttpTargetArgs:
    def __init__(
        __self__,
        *,
        header_overrides: Optional[
            pulumi.Input[Sequence[pulumi.Input[QueueHttpTargetHeaderOverrideArgs]]]
        ] = ...,
        http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_token: Optional[pulumi.Input[QueueHttpTargetOauthTokenArgs]] = ...,
        oidc_token: Optional[pulumi.Input[QueueHttpTargetOidcTokenArgs]] = ...,
        uri_override: Optional[pulumi.Input[QueueHttpTargetUriOverrideArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerOverrides")
    def header_overrides(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[QueueHttpTargetHeaderOverrideArgs]]]
    ]: ...
    @header_overrides.setter
    def header_overrides(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[QueueHttpTargetHeaderOverrideArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[pulumi.Input[QueueHttpTargetOauthTokenArgs]]: ...
    @oauth_token.setter
    def oauth_token(
        self, value: Optional[pulumi.Input[QueueHttpTargetOauthTokenArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[pulumi.Input[QueueHttpTargetOidcTokenArgs]]: ...
    @oidc_token.setter
    def oidc_token(
        self, value: Optional[pulumi.Input[QueueHttpTargetOidcTokenArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uriOverride")
    def uri_override(
        self,
    ) -> Optional[pulumi.Input[QueueHttpTargetUriOverrideArgs]]: ...
    @uri_override.setter
    def uri_override(
        self, value: Optional[pulumi.Input[QueueHttpTargetUriOverrideArgs]]
    ): ...

class QueueHttpTargetHeaderOverrideArgsDict(TypedDict):
    header: pulumi.Input[QueueHttpTargetHeaderOverrideHeaderArgsDict]

@pulumi.input_type
class QueueHttpTargetHeaderOverrideArgs:
    def __init__(
        __self__, *, header: pulumi.Input[QueueHttpTargetHeaderOverrideHeaderArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> pulumi.Input[QueueHttpTargetHeaderOverrideHeaderArgs]: ...
    @header.setter
    def header(self, value: pulumi.Input[QueueHttpTargetHeaderOverrideHeaderArgs]): ...

class QueueHttpTargetHeaderOverrideHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class QueueHttpTargetHeaderOverrideHeaderArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class QueueHttpTargetOauthTokenArgsDict(TypedDict):
    service_account_email: pulumi.Input[_builtins.str]
    scope: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueHttpTargetOauthTokenArgs:
    def __init__(
        __self__,
        *,
        service_account_email: pulumi.Input[_builtins.str],
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Input[_builtins.str]: ...
    @service_account_email.setter
    def service_account_email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueHttpTargetOidcTokenArgsDict(TypedDict):
    service_account_email: pulumi.Input[_builtins.str]
    audience: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueHttpTargetOidcTokenArgs:
    def __init__(
        __self__,
        *,
        service_account_email: pulumi.Input[_builtins.str],
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> pulumi.Input[_builtins.str]: ...
    @service_account_email.setter
    def service_account_email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueHttpTargetUriOverrideArgsDict(TypedDict):
    host: NotRequired[pulumi.Input[_builtins.str]]
    path_override: NotRequired[
        pulumi.Input[QueueHttpTargetUriOverridePathOverrideArgsDict]
    ]
    port: NotRequired[pulumi.Input[_builtins.str]]
    query_override: NotRequired[
        pulumi.Input[QueueHttpTargetUriOverrideQueryOverrideArgsDict]
    ]
    scheme: NotRequired[pulumi.Input[_builtins.str]]
    uri_override_enforce_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueHttpTargetUriOverrideArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        path_override: Optional[
            pulumi.Input[QueueHttpTargetUriOverridePathOverrideArgs]
        ] = ...,
        port: Optional[pulumi.Input[_builtins.str]] = ...,
        query_override: Optional[
            pulumi.Input[QueueHttpTargetUriOverrideQueryOverrideArgs]
        ] = ...,
        scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        uri_override_enforce_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pathOverride")
    def path_override(
        self,
    ) -> Optional[pulumi.Input[QueueHttpTargetUriOverridePathOverrideArgs]]: ...
    @path_override.setter
    def path_override(
        self, value: Optional[pulumi.Input[QueueHttpTargetUriOverridePathOverrideArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryOverride")
    def query_override(
        self,
    ) -> Optional[pulumi.Input[QueueHttpTargetUriOverrideQueryOverrideArgs]]: ...
    @query_override.setter
    def query_override(
        self, value: Optional[pulumi.Input[QueueHttpTargetUriOverrideQueryOverrideArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uriOverrideEnforceMode")
    def uri_override_enforce_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri_override_enforce_mode.setter
    def uri_override_enforce_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class QueueHttpTargetUriOverridePathOverrideArgsDict(TypedDict):
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueHttpTargetUriOverridePathOverrideArgs:
    def __init__(
        __self__, *, path: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueHttpTargetUriOverrideQueryOverrideArgsDict(TypedDict):
    query_params: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueHttpTargetUriOverrideQueryOverrideArgs:
    def __init__(
        __self__, *, query_params: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryParams")
    def query_params(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_params.setter
    def query_params(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueRateLimitsArgsDict(TypedDict):
    max_burst_size: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_dispatches: NotRequired[pulumi.Input[_builtins.int]]
    max_dispatches_per_second: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class QueueRateLimitsArgs:
    def __init__(
        __self__,
        *,
        max_burst_size: Optional[pulumi.Input[_builtins.int]] = ...,
        max_concurrent_dispatches: Optional[pulumi.Input[_builtins.int]] = ...,
        max_dispatches_per_second: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxBurstSize")
    def max_burst_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_burst_size.setter
    def max_burst_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentDispatches")
    def max_concurrent_dispatches(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_dispatches.setter
    def max_concurrent_dispatches(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxDispatchesPerSecond")
    def max_dispatches_per_second(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_dispatches_per_second.setter
    def max_dispatches_per_second(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class QueueRetryConfigArgsDict(TypedDict):
    max_attempts: NotRequired[pulumi.Input[_builtins.int]]
    max_backoff: NotRequired[pulumi.Input[_builtins.str]]
    max_doublings: NotRequired[pulumi.Input[_builtins.int]]
    max_retry_duration: NotRequired[pulumi.Input[_builtins.str]]
    min_backoff: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class QueueRetryConfigArgs:
    def __init__(
        __self__,
        *,
        max_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
        max_backoff: Optional[pulumi.Input[_builtins.str]] = ...,
        max_doublings: Optional[pulumi.Input[_builtins.int]] = ...,
        max_retry_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        min_backoff: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_attempts.setter
    def max_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBackoff")
    def max_backoff(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_backoff.setter
    def max_backoff(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDoublings")
    def max_doublings(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_doublings.setter
    def max_doublings(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetryDuration")
    def max_retry_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_retry_duration.setter
    def max_retry_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minBackoff")
    def min_backoff(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_backoff.setter
    def min_backoff(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class QueueStackdriverLoggingConfigArgsDict(TypedDict):
    sampling_ratio: pulumi.Input[_builtins.float]

@pulumi.input_type
class QueueStackdriverLoggingConfigArgs:
    def __init__(
        __self__, *, sampling_ratio: pulumi.Input[_builtins.float]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="samplingRatio")
    def sampling_ratio(self) -> pulumi.Input[_builtins.float]: ...
    @sampling_ratio.setter
    def sampling_ratio(self, value: pulumi.Input[_builtins.float]): ...
