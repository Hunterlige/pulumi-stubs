import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "JobAppEngineHttpTargetArgs",
    "JobAppEngineHttpTargetArgsDict",
    "JobAppEngineHttpTargetAppEngineRoutingArgs",
    "JobAppEngineHttpTargetAppEngineRoutingArgsDict",
    "JobHttpTargetArgs",
    "JobHttpTargetArgsDict",
    "JobHttpTargetOauthTokenArgs",
    "JobHttpTargetOauthTokenArgsDict",
    "JobHttpTargetOidcTokenArgs",
    "JobHttpTargetOidcTokenArgsDict",
    "JobPubsubTargetArgs",
    "JobPubsubTargetArgsDict",
    "JobRetryConfigArgs",
    "JobRetryConfigArgsDict",
]

class JobAppEngineHttpTargetArgsDict(TypedDict):
    relative_uri: pulumi.Input[_builtins.str]
    app_engine_routing: NotRequired[
        pulumi.Input[JobAppEngineHttpTargetAppEngineRoutingArgsDict]
    ]
    body: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    http_method: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class JobAppEngineHttpTargetArgs:
    def __init__(
        __self__,
        *,
        relative_uri: pulumi.Input[_builtins.str],
        app_engine_routing: Optional[
            pulumi.Input[JobAppEngineHttpTargetAppEngineRoutingArgs]
        ] = ...,
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        http_method: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="relativeUri")
    def relative_uri(self) -> pulumi.Input[_builtins.str]: ...
    @relative_uri.setter
    def relative_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appEngineRouting")
    def app_engine_routing(
        self,
    ) -> Optional[pulumi.Input[JobAppEngineHttpTargetAppEngineRoutingArgs]]: ...
    @app_engine_routing.setter
    def app_engine_routing(
        self, value: Optional[pulumi.Input[JobAppEngineHttpTargetAppEngineRoutingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @headers.setter
    def headers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobAppEngineHttpTargetAppEngineRoutingArgsDict(TypedDict):
    instance: NotRequired[pulumi.Input[_builtins.str]]
    service: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class JobAppEngineHttpTargetAppEngineRoutingArgs:
    def __init__(
        __self__,
        *,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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

class JobHttpTargetArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    body: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    http_method: NotRequired[pulumi.Input[_builtins.str]]
    oauth_token: NotRequired[pulumi.Input[JobHttpTargetOauthTokenArgsDict]]
    oidc_token: NotRequired[pulumi.Input[JobHttpTargetOidcTokenArgsDict]]
    ...

@pulumi.input_type
class JobHttpTargetArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        body: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        http_method: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_token: Optional[pulumi.Input[JobHttpTargetOauthTokenArgs]] = ...,
        oidc_token: Optional[pulumi.Input[JobHttpTargetOidcTokenArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @body.setter
    def body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @headers.setter
    def headers(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[pulumi.Input[JobHttpTargetOauthTokenArgs]]: ...
    @oauth_token.setter
    def oauth_token(
        self, value: Optional[pulumi.Input[JobHttpTargetOauthTokenArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[pulumi.Input[JobHttpTargetOidcTokenArgs]]: ...
    @oidc_token.setter
    def oidc_token(self, value: Optional[pulumi.Input[JobHttpTargetOidcTokenArgs]]): ...

class JobHttpTargetOauthTokenArgsDict(TypedDict):
    service_account_email: pulumi.Input[_builtins.str]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class JobHttpTargetOauthTokenArgs:
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

class JobHttpTargetOidcTokenArgsDict(TypedDict):
    service_account_email: pulumi.Input[_builtins.str]
    audience: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class JobHttpTargetOidcTokenArgs:
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

class JobPubsubTargetArgsDict(TypedDict):
    topic_name: pulumi.Input[_builtins.str]
    attributes: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    data: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class JobPubsubTargetArgs:
    def __init__(
        __self__,
        *,
        topic_name: pulumi.Input[_builtins.str],
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[_builtins.str]: ...
    @topic_name.setter
    def topic_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @attributes.setter
    def attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobRetryConfigArgsDict(TypedDict):
    max_backoff_duration: NotRequired[pulumi.Input[_builtins.str]]
    max_doublings: NotRequired[pulumi.Input[_builtins.int]]
    max_retry_duration: NotRequired[pulumi.Input[_builtins.str]]
    min_backoff_duration: NotRequired[pulumi.Input[_builtins.str]]
    retry_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class JobRetryConfigArgs:
    def __init__(
        __self__,
        *,
        max_backoff_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        max_doublings: Optional[pulumi.Input[_builtins.int]] = ...,
        max_retry_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        min_backoff_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxBackoffDuration")
    def max_backoff_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_backoff_duration.setter
    def max_backoff_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="minBackoffDuration")
    def min_backoff_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_backoff_duration.setter
    def min_backoff_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retry_count.setter
    def retry_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
