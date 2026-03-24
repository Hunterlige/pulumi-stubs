import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListenerDefaultAction",
    "ListenerDefaultActionAuthenticateCognito",
    "ListenerDefaultActionAuthenticateOidc",
    "ListenerDefaultActionFixedResponse",
    "ListenerDefaultActionForward",
    "ListenerDefaultActionForwardStickiness",
    "ListenerDefaultActionForwardTargetGroup",
    "ListenerDefaultActionJwtValidation",
    "ListenerDefaultActionJwtValidationAdditionalClaim",
    "ListenerDefaultActionRedirect",
    "ListenerMutualAuthentication",
    "ListenerRuleAction",
    "ListenerRuleActionAuthenticateCognito",
    "ListenerRuleActionAuthenticateOidc",
    "ListenerRuleActionFixedResponse",
    "ListenerRuleActionForward",
    "ListenerRuleActionForwardStickiness",
    "ListenerRuleActionForwardTargetGroup",
    "ListenerRuleActionJwtValidation",
    "ListenerRuleActionJwtValidationAdditionalClaim",
    "ListenerRuleActionRedirect",
    "ListenerRuleCondition",
    "ListenerRuleConditionHostHeader",
    "ListenerRuleConditionHttpHeader",
    "ListenerRuleConditionHttpRequestMethod",
    "ListenerRuleConditionPathPattern",
    "ListenerRuleConditionQueryString",
    "ListenerRuleConditionSourceIp",
    "ListenerRuleTransform",
    "ListenerRuleTransformHostHeaderRewriteConfig",
    ...,
    "ListenerRuleTransformUrlRewriteConfig",
    "ListenerRuleTransformUrlRewriteConfigRewrite",
    "LoadBalancerAccessLogs",
    "LoadBalancerConnectionLogs",
    "LoadBalancerHealthCheckLogs",
    "LoadBalancerIpamPools",
    "LoadBalancerMinimumLoadBalancerCapacity",
    "LoadBalancerSubnetMapping",
    "TargetGroupHealthCheck",
    "TargetGroupStickiness",
    "TargetGroupTargetFailover",
    "TargetGroupTargetGroupHealth",
    "TargetGroupTargetGroupHealthDnsFailover",
    "TargetGroupTargetGroupHealthUnhealthyStateRouting",
    "TargetGroupTargetHealthState",
    "GetListenerDefaultActionResult",
    "GetListenerDefaultActionAuthenticateCognitoResult",
    "GetListenerDefaultActionAuthenticateOidcResult",
    "GetListenerDefaultActionFixedResponseResult",
    "GetListenerDefaultActionForwardResult",
    "GetListenerDefaultActionForwardStickinessResult",
    "GetListenerDefaultActionForwardTargetGroupResult",
    "GetListenerDefaultActionJwtValidationResult",
    ...,
    "GetListenerDefaultActionRedirectResult",
    "GetListenerMutualAuthenticationResult",
    "GetListenerRuleActionResult",
    "GetListenerRuleActionAuthenticateCognitoResult",
    "GetListenerRuleActionAuthenticateOidcResult",
    "GetListenerRuleActionFixedResponseResult",
    "GetListenerRuleActionForwardResult",
    "GetListenerRuleActionForwardStickinessResult",
    "GetListenerRuleActionForwardTargetGroupResult",
    "GetListenerRuleActionJwtValidationResult",
    ...,
    "GetListenerRuleActionRedirectResult",
    "GetListenerRuleConditionResult",
    "GetListenerRuleConditionHostHeaderResult",
    "GetListenerRuleConditionHttpHeaderResult",
    "GetListenerRuleConditionHttpRequestMethodResult",
    "GetListenerRuleConditionPathPatternResult",
    "GetListenerRuleConditionQueryStringResult",
    "GetListenerRuleConditionQueryStringValueResult",
    "GetListenerRuleConditionSourceIpResult",
    "GetListenerRuleTransformResult",
    ...,
    ...,
    "GetListenerRuleTransformUrlRewriteConfigResult",
    ...,
    "GetLoadBalancerAccessLogsResult",
    "GetLoadBalancerConnectionLogResult",
    "GetLoadBalancerHealthCheckLogResult",
    "GetLoadBalancerIpamPoolResult",
    "GetLoadBalancerSubnetMappingResult",
    "GetTargetGroupHealthCheckResult",
    "GetTargetGroupStickinessResult",
]

@pulumi.output_type
class ListenerDefaultAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authenticate_cognito: Optional[
            outputs.ListenerDefaultActionAuthenticateCognito
        ] = ...,
        authenticate_oidc: Optional[
            outputs.ListenerDefaultActionAuthenticateOidc
        ] = ...,
        fixed_response: Optional[outputs.ListenerDefaultActionFixedResponse] = ...,
        forward: Optional[outputs.ListenerDefaultActionForward] = ...,
        jwt_validation: Optional[outputs.ListenerDefaultActionJwtValidation] = ...,
        order: Optional[_builtins.int] = ...,
        redirect: Optional[outputs.ListenerDefaultActionRedirect] = ...,
        target_group_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticateCognito")
    def authenticate_cognito(
        self,
    ) -> Optional[outputs.ListenerDefaultActionAuthenticateCognito]: ...
    @_builtins.property
    @pulumi.getter(name="authenticateOidc")
    def authenticate_oidc(
        self,
    ) -> Optional[outputs.ListenerDefaultActionAuthenticateOidc]: ...
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(
        self,
    ) -> Optional[outputs.ListenerDefaultActionFixedResponse]: ...
    @_builtins.property
    @pulumi.getter
    def forward(self) -> Optional[outputs.ListenerDefaultActionForward]: ...
    @_builtins.property
    @pulumi.getter(name="jwtValidation")
    def jwt_validation(
        self,
    ) -> Optional[outputs.ListenerDefaultActionJwtValidation]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[outputs.ListenerDefaultActionRedirect]: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerDefaultActionAuthenticateCognito(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        user_pool_arn: _builtins.str,
        user_pool_client_id: _builtins.str,
        user_pool_domain: _builtins.str,
        authentication_request_extra_params: Optional[
            Mapping[str, _builtins.str]
        ] = ...,
        on_unauthenticated_request: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
        session_cookie_name: Optional[_builtins.str] = ...,
        session_timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolClientId")
    def user_pool_client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolDomain")
    def user_pool_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerDefaultActionAuthenticateOidc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        issuer: _builtins.str,
        token_endpoint: _builtins.str,
        user_info_endpoint: _builtins.str,
        authentication_request_extra_params: Optional[
            Mapping[str, _builtins.str]
        ] = ...,
        on_unauthenticated_request: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
        session_cookie_name: Optional[_builtins.str] = ...,
        session_timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerDefaultActionFixedResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_type: _builtins.str,
        message_body: Optional[_builtins.str] = ...,
        status_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageBody")
    def message_body(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerDefaultActionForward(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_groups: Sequence[outputs.ListenerDefaultActionForwardTargetGroup],
        stickiness: Optional[outputs.ListenerDefaultActionForwardStickiness] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Sequence[outputs.ListenerDefaultActionForwardTargetGroup]: ...
    @_builtins.property
    @pulumi.getter
    def stickiness(
        self,
    ) -> Optional[outputs.ListenerDefaultActionForwardStickiness]: ...

@pulumi.output_type
class ListenerDefaultActionForwardStickiness(dict):
    def __init__(
        __self__, *, duration: _builtins.int, enabled: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ListenerDefaultActionForwardTargetGroup(dict):
    def __init__(
        __self__, *, arn: _builtins.str, weight: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerDefaultActionJwtValidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        issuer: _builtins.str,
        jwks_endpoint: _builtins.str,
        additional_claims: Optional[
            Sequence[outputs.ListenerDefaultActionJwtValidationAdditionalClaim]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jwksEndpoint")
    def jwks_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalClaims")
    def additional_claims(
        self,
    ) -> Optional[
        Sequence[outputs.ListenerDefaultActionJwtValidationAdditionalClaim]
    ]: ...

@pulumi.output_type
class ListenerDefaultActionJwtValidationAdditionalClaim(dict):
    def __init__(
        __self__,
        *,
        format: _builtins.str,
        name: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ListenerDefaultActionRedirect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        status_code: _builtins.str,
        host: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
        query: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerMutualAuthentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mode: _builtins.str,
        advertise_trust_store_ca_names: Optional[_builtins.str] = ...,
        ignore_client_certificate_expiry: Optional[_builtins.bool] = ...,
        trust_store_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="advertiseTrustStoreCaNames")
    def advertise_trust_store_ca_names(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreClientCertificateExpiry")
    def ignore_client_certificate_expiry(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authenticate_cognito: Optional[
            outputs.ListenerRuleActionAuthenticateCognito
        ] = ...,
        authenticate_oidc: Optional[outputs.ListenerRuleActionAuthenticateOidc] = ...,
        fixed_response: Optional[outputs.ListenerRuleActionFixedResponse] = ...,
        forward: Optional[outputs.ListenerRuleActionForward] = ...,
        jwt_validation: Optional[outputs.ListenerRuleActionJwtValidation] = ...,
        order: Optional[_builtins.int] = ...,
        redirect: Optional[outputs.ListenerRuleActionRedirect] = ...,
        target_group_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticateCognito")
    def authenticate_cognito(
        self,
    ) -> Optional[outputs.ListenerRuleActionAuthenticateCognito]: ...
    @_builtins.property
    @pulumi.getter(name="authenticateOidc")
    def authenticate_oidc(
        self,
    ) -> Optional[outputs.ListenerRuleActionAuthenticateOidc]: ...
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional[outputs.ListenerRuleActionFixedResponse]: ...
    @_builtins.property
    @pulumi.getter
    def forward(self) -> Optional[outputs.ListenerRuleActionForward]: ...
    @_builtins.property
    @pulumi.getter(name="jwtValidation")
    def jwt_validation(self) -> Optional[outputs.ListenerRuleActionJwtValidation]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[outputs.ListenerRuleActionRedirect]: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleActionAuthenticateCognito(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        user_pool_arn: _builtins.str,
        user_pool_client_id: _builtins.str,
        user_pool_domain: _builtins.str,
        authentication_request_extra_params: Optional[
            Mapping[str, _builtins.str]
        ] = ...,
        on_unauthenticated_request: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
        session_cookie_name: Optional[_builtins.str] = ...,
        session_timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolClientId")
    def user_pool_client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolDomain")
    def user_pool_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerRuleActionAuthenticateOidc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        issuer: _builtins.str,
        token_endpoint: _builtins.str,
        user_info_endpoint: _builtins.str,
        authentication_request_extra_params: Optional[
            Mapping[str, _builtins.str]
        ] = ...,
        on_unauthenticated_request: Optional[_builtins.str] = ...,
        scope: Optional[_builtins.str] = ...,
        session_cookie_name: Optional[_builtins.str] = ...,
        session_timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerRuleActionFixedResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_type: _builtins.str,
        message_body: Optional[_builtins.str] = ...,
        status_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageBody")
    def message_body(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleActionForward(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_groups: Sequence[outputs.ListenerRuleActionForwardTargetGroup],
        stickiness: Optional[outputs.ListenerRuleActionForwardStickiness] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Sequence[outputs.ListenerRuleActionForwardTargetGroup]: ...
    @_builtins.property
    @pulumi.getter
    def stickiness(self) -> Optional[outputs.ListenerRuleActionForwardStickiness]: ...

@pulumi.output_type
class ListenerRuleActionForwardStickiness(dict):
    def __init__(
        __self__, *, duration: _builtins.int, enabled: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ListenerRuleActionForwardTargetGroup(dict):
    def __init__(
        __self__, *, arn: _builtins.str, weight: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ListenerRuleActionJwtValidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        issuer: _builtins.str,
        jwks_endpoint: _builtins.str,
        additional_claims: Optional[
            Sequence[outputs.ListenerRuleActionJwtValidationAdditionalClaim]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jwksEndpoint")
    def jwks_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalClaims")
    def additional_claims(
        self,
    ) -> Optional[Sequence[outputs.ListenerRuleActionJwtValidationAdditionalClaim]]: ...

@pulumi.output_type
class ListenerRuleActionJwtValidationAdditionalClaim(dict):
    def __init__(
        __self__,
        *,
        format: _builtins.str,
        name: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleActionRedirect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        status_code: _builtins.str,
        host: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
        query: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_header: Optional[outputs.ListenerRuleConditionHostHeader] = ...,
        http_header: Optional[outputs.ListenerRuleConditionHttpHeader] = ...,
        http_request_method: Optional[
            outputs.ListenerRuleConditionHttpRequestMethod
        ] = ...,
        path_pattern: Optional[outputs.ListenerRuleConditionPathPattern] = ...,
        query_strings: Optional[
            Sequence[outputs.ListenerRuleConditionQueryString]
        ] = ...,
        source_ip: Optional[outputs.ListenerRuleConditionSourceIp] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostHeader")
    def host_header(self) -> Optional[outputs.ListenerRuleConditionHostHeader]: ...
    @_builtins.property
    @pulumi.getter(name="httpHeader")
    def http_header(self) -> Optional[outputs.ListenerRuleConditionHttpHeader]: ...
    @_builtins.property
    @pulumi.getter(name="httpRequestMethod")
    def http_request_method(
        self,
    ) -> Optional[outputs.ListenerRuleConditionHttpRequestMethod]: ...
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> Optional[outputs.ListenerRuleConditionPathPattern]: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[Sequence[outputs.ListenerRuleConditionQueryString]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[outputs.ListenerRuleConditionSourceIp]: ...

@pulumi.output_type
class ListenerRuleConditionHostHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regex_values: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ListenerRuleConditionHttpHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_header_name: _builtins.str,
        regex_values: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaderName")
    def http_header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ListenerRuleConditionHttpRequestMethod(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleConditionPathPattern(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regex_values: Optional[Sequence[_builtins.str]] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ListenerRuleConditionQueryString(dict):
    def __init__(
        __self__, *, value: _builtins.str, key: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleConditionSourceIp(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ListenerRuleTransform(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        host_header_rewrite_config: Optional[
            outputs.ListenerRuleTransformHostHeaderRewriteConfig
        ] = ...,
        url_rewrite_config: Optional[
            outputs.ListenerRuleTransformUrlRewriteConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostHeaderRewriteConfig")
    def host_header_rewrite_config(
        self,
    ) -> Optional[outputs.ListenerRuleTransformHostHeaderRewriteConfig]: ...
    @_builtins.property
    @pulumi.getter(name="urlRewriteConfig")
    def url_rewrite_config(
        self,
    ) -> Optional[outputs.ListenerRuleTransformUrlRewriteConfig]: ...

@pulumi.output_type
class ListenerRuleTransformHostHeaderRewriteConfig(dict):
    def __init__(
        __self__,
        *,
        rewrite: Optional[
            outputs.ListenerRuleTransformHostHeaderRewriteConfigRewrite
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rewrite(
        self,
    ) -> Optional[outputs.ListenerRuleTransformHostHeaderRewriteConfigRewrite]: ...

@pulumi.output_type
class ListenerRuleTransformHostHeaderRewriteConfigRewrite(dict):
    def __init__(__self__, *, regex: _builtins.str, replace: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> _builtins.str: ...

@pulumi.output_type
class ListenerRuleTransformUrlRewriteConfig(dict):
    def __init__(
        __self__,
        *,
        rewrite: Optional[outputs.ListenerRuleTransformUrlRewriteConfigRewrite] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rewrite(
        self,
    ) -> Optional[outputs.ListenerRuleTransformUrlRewriteConfigRewrite]: ...

@pulumi.output_type
class ListenerRuleTransformUrlRewriteConfigRewrite(dict):
    def __init__(__self__, *, regex: _builtins.str, replace: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> _builtins.str: ...

@pulumi.output_type
class LoadBalancerAccessLogs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        enabled: Optional[_builtins.bool] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoadBalancerConnectionLogs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        enabled: Optional[_builtins.bool] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoadBalancerHealthCheckLogs(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        enabled: Optional[_builtins.bool] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoadBalancerIpamPools(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ipv4_ipam_pool_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> _builtins.str: ...

@pulumi.output_type
class LoadBalancerMinimumLoadBalancerCapacity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, capacity_units: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityUnits")
    def capacity_units(self) -> _builtins.int: ...

@pulumi.output_type
class LoadBalancerSubnetMapping(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnet_id: _builtins.str,
        allocation_id: Optional[_builtins.str] = ...,
        ipv6_address: Optional[_builtins.str] = ...,
        outpost_id: Optional[_builtins.str] = ...,
        private_ipv4_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outpostId")
    def outpost_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIpv4Address")
    def private_ipv4_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetGroupHealthCheck(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        healthy_threshold: Optional[_builtins.int] = ...,
        interval: Optional[_builtins.int] = ...,
        matcher: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.int] = ...,
        unhealthy_threshold: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def matcher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TargetGroupStickiness(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        cookie_duration: Optional[_builtins.int] = ...,
        cookie_name: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cookieDuration")
    def cookie_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cookieName")
    def cookie_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TargetGroupTargetFailover(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, on_deregistration: _builtins.str, on_unhealthy: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDeregistration")
    def on_deregistration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onUnhealthy")
    def on_unhealthy(self) -> _builtins.str: ...

@pulumi.output_type
class TargetGroupTargetGroupHealth(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_failover: Optional[outputs.TargetGroupTargetGroupHealthDnsFailover] = ...,
        unhealthy_state_routing: Optional[
            outputs.TargetGroupTargetGroupHealthUnhealthyStateRouting
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsFailover")
    def dns_failover(
        self,
    ) -> Optional[outputs.TargetGroupTargetGroupHealthDnsFailover]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyStateRouting")
    def unhealthy_state_routing(
        self,
    ) -> Optional[outputs.TargetGroupTargetGroupHealthUnhealthyStateRouting]: ...

@pulumi.output_type
class TargetGroupTargetGroupHealthDnsFailover(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        minimum_healthy_targets_count: Optional[_builtins.str] = ...,
        minimum_healthy_targets_percentage: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsCount")
    def minimum_healthy_targets_count(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsPercentage")
    def minimum_healthy_targets_percentage(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetGroupTargetGroupHealthUnhealthyStateRouting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        minimum_healthy_targets_count: Optional[_builtins.int] = ...,
        minimum_healthy_targets_percentage: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsCount")
    def minimum_healthy_targets_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsPercentage")
    def minimum_healthy_targets_percentage(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetGroupTargetHealthState(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_unhealthy_connection_termination: _builtins.bool,
        unhealthy_draining_interval: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableUnhealthyConnectionTermination")
    def enable_unhealthy_connection_termination(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyDrainingInterval")
    def unhealthy_draining_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetListenerDefaultActionResult(dict):
    def __init__(
        __self__,
        *,
        authenticate_cognitos: Sequence[
            outputs.GetListenerDefaultActionAuthenticateCognitoResult
        ],
        authenticate_oidcs: Sequence[
            outputs.GetListenerDefaultActionAuthenticateOidcResult
        ],
        fixed_responses: Sequence[outputs.GetListenerDefaultActionFixedResponseResult],
        forwards: Sequence[outputs.GetListenerDefaultActionForwardResult],
        jwt_validations: Sequence[outputs.GetListenerDefaultActionJwtValidationResult],
        order: _builtins.int,
        redirects: Sequence[outputs.GetListenerDefaultActionRedirectResult],
        target_group_arn: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticateCognitos")
    def authenticate_cognitos(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionAuthenticateCognitoResult]: ...
    @_builtins.property
    @pulumi.getter(name="authenticateOidcs")
    def authenticate_oidcs(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionAuthenticateOidcResult]: ...
    @_builtins.property
    @pulumi.getter(name="fixedResponses")
    def fixed_responses(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionFixedResponseResult]: ...
    @_builtins.property
    @pulumi.getter
    def forwards(self) -> Sequence[outputs.GetListenerDefaultActionForwardResult]: ...
    @_builtins.property
    @pulumi.getter(name="jwtValidations")
    def jwt_validations(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionJwtValidationResult]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def redirects(self) -> Sequence[outputs.GetListenerDefaultActionRedirectResult]: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerDefaultActionAuthenticateCognitoResult(dict):
    def __init__(
        __self__,
        *,
        authentication_request_extra_params: Mapping[str, _builtins.str],
        on_unauthenticated_request: _builtins.str,
        scope: _builtins.str,
        session_cookie_name: _builtins.str,
        session_timeout: _builtins.int,
        user_pool_arn: _builtins.str,
        user_pool_client_id: _builtins.str,
        user_pool_domain: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolClientId")
    def user_pool_client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolDomain")
    def user_pool_domain(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerDefaultActionAuthenticateOidcResult(dict):
    def __init__(
        __self__,
        *,
        authentication_request_extra_params: Mapping[str, _builtins.str],
        authorization_endpoint: _builtins.str,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        issuer: _builtins.str,
        on_unauthenticated_request: _builtins.str,
        scope: _builtins.str,
        session_cookie_name: _builtins.str,
        session_timeout: _builtins.int,
        token_endpoint: _builtins.str,
        user_info_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerDefaultActionFixedResponseResult(dict):
    def __init__(
        __self__,
        *,
        content_type: _builtins.str,
        message_body: _builtins.str,
        status_code: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageBody")
    def message_body(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerDefaultActionForwardResult(dict):
    def __init__(
        __self__,
        *,
        stickinesses: Sequence[outputs.GetListenerDefaultActionForwardStickinessResult],
        target_groups: Sequence[
            outputs.GetListenerDefaultActionForwardTargetGroupResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def stickinesses(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionForwardStickinessResult]: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Sequence[outputs.GetListenerDefaultActionForwardTargetGroupResult]: ...

@pulumi.output_type
class GetListenerDefaultActionForwardStickinessResult(dict):
    def __init__(
        __self__, *, duration: _builtins.int, enabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetListenerDefaultActionForwardTargetGroupResult(dict):
    def __init__(__self__, *, arn: _builtins.str, weight: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetListenerDefaultActionJwtValidationResult(dict):
    def __init__(
        __self__,
        *,
        additional_claims: Sequence[
            outputs.GetListenerDefaultActionJwtValidationAdditionalClaimResult
        ],
        issuer: _builtins.str,
        jwks_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalClaims")
    def additional_claims(
        self,
    ) -> Sequence[
        outputs.GetListenerDefaultActionJwtValidationAdditionalClaimResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jwksEndpoint")
    def jwks_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerDefaultActionJwtValidationAdditionalClaimResult(dict):
    def __init__(
        __self__,
        *,
        format: _builtins.str,
        name: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetListenerDefaultActionRedirectResult(dict):
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        path: _builtins.str,
        port: _builtins.str,
        protocol: _builtins.str,
        query: _builtins.str,
        status_code: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerMutualAuthenticationResult(dict):
    def __init__(
        __self__,
        *,
        advertise_trust_store_ca_names: _builtins.str,
        ignore_client_certificate_expiry: _builtins.bool,
        mode: _builtins.str,
        trust_store_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advertiseTrustStoreCaNames")
    def advertise_trust_store_ca_names(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ignoreClientCertificateExpiry")
    def ignore_client_certificate_expiry(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerRuleActionResult(dict):
    def __init__(
        __self__,
        *,
        order: _builtins.int,
        type: _builtins.str,
        authenticate_cognitos: Optional[
            Sequence[outputs.GetListenerRuleActionAuthenticateCognitoResult]
        ] = ...,
        authenticate_oidcs: Optional[
            Sequence[outputs.GetListenerRuleActionAuthenticateOidcResult]
        ] = ...,
        fixed_responses: Optional[
            Sequence[outputs.GetListenerRuleActionFixedResponseResult]
        ] = ...,
        forwards: Optional[Sequence[outputs.GetListenerRuleActionForwardResult]] = ...,
        jwt_validations: Optional[
            Sequence[outputs.GetListenerRuleActionJwtValidationResult]
        ] = ...,
        redirects: Optional[
            Sequence[outputs.GetListenerRuleActionRedirectResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticateCognitos")
    def authenticate_cognitos(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionAuthenticateCognitoResult]]: ...
    @_builtins.property
    @pulumi.getter(name="authenticateOidcs")
    def authenticate_oidcs(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionAuthenticateOidcResult]]: ...
    @_builtins.property
    @pulumi.getter(name="fixedResponses")
    def fixed_responses(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionFixedResponseResult]]: ...
    @_builtins.property
    @pulumi.getter
    def forwards(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionForwardResult]]: ...
    @_builtins.property
    @pulumi.getter(name="jwtValidations")
    def jwt_validations(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionJwtValidationResult]]: ...
    @_builtins.property
    @pulumi.getter
    def redirects(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionRedirectResult]]: ...

@pulumi.output_type
class GetListenerRuleActionAuthenticateCognitoResult(dict):
    def __init__(
        __self__,
        *,
        authentication_request_extra_params: Mapping[str, _builtins.str],
        on_unauthenticated_request: _builtins.str,
        scope: _builtins.str,
        session_cookie_name: _builtins.str,
        session_timeout: _builtins.int,
        user_pool_arn: _builtins.str,
        user_pool_client_id: _builtins.str,
        user_pool_domain: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolClientId")
    def user_pool_client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPoolDomain")
    def user_pool_domain(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerRuleActionAuthenticateOidcResult(dict):
    def __init__(
        __self__,
        *,
        authentication_request_extra_params: Mapping[str, _builtins.str],
        authorization_endpoint: _builtins.str,
        client_id: _builtins.str,
        issuer: _builtins.str,
        on_unauthenticated_request: _builtins.str,
        scope: _builtins.str,
        session_cookie_name: _builtins.str,
        session_timeout: _builtins.int,
        token_endpoint: _builtins.str,
        user_info_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerRuleActionFixedResponseResult(dict):
    def __init__(
        __self__,
        *,
        content_type: _builtins.str,
        message_body: _builtins.str,
        status_code: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="messageBody")
    def message_body(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerRuleActionForwardResult(dict):
    def __init__(
        __self__,
        *,
        stickinesses: Optional[
            Sequence[outputs.GetListenerRuleActionForwardStickinessResult]
        ] = ...,
        target_groups: Optional[
            Sequence[outputs.GetListenerRuleActionForwardTargetGroupResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def stickinesses(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionForwardStickinessResult]]: ...
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleActionForwardTargetGroupResult]]: ...

@pulumi.output_type
class GetListenerRuleActionForwardStickinessResult(dict):
    def __init__(
        __self__, *, duration: _builtins.int, enabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetListenerRuleActionForwardTargetGroupResult(dict):
    def __init__(__self__, *, arn: _builtins.str, weight: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetListenerRuleActionJwtValidationResult(dict):
    def __init__(
        __self__,
        *,
        issuer: _builtins.str,
        jwks_endpoint: _builtins.str,
        additional_claims: Optional[
            Sequence[outputs.GetListenerRuleActionJwtValidationAdditionalClaimResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jwksEndpoint")
    def jwks_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalClaims")
    def additional_claims(
        self,
    ) -> Optional[
        Sequence[outputs.GetListenerRuleActionJwtValidationAdditionalClaimResult]
    ]: ...

@pulumi.output_type
class GetListenerRuleActionJwtValidationAdditionalClaimResult(dict):
    def __init__(
        __self__,
        *,
        format: _builtins.str,
        name: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetListenerRuleActionRedirectResult(dict):
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        path: _builtins.str,
        port: _builtins.str,
        protocol: _builtins.str,
        query: _builtins.str,
        status_code: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerRuleConditionResult(dict):
    def __init__(
        __self__,
        *,
        host_headers: Optional[
            Sequence[outputs.GetListenerRuleConditionHostHeaderResult]
        ] = ...,
        http_headers: Optional[
            Sequence[outputs.GetListenerRuleConditionHttpHeaderResult]
        ] = ...,
        http_request_methods: Optional[
            Sequence[outputs.GetListenerRuleConditionHttpRequestMethodResult]
        ] = ...,
        path_patterns: Optional[
            Sequence[outputs.GetListenerRuleConditionPathPatternResult]
        ] = ...,
        query_strings: Optional[
            Sequence[outputs.GetListenerRuleConditionQueryStringResult]
        ] = ...,
        source_ips: Optional[
            Sequence[outputs.GetListenerRuleConditionSourceIpResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostHeaders")
    def host_headers(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleConditionHostHeaderResult]]: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleConditionHttpHeaderResult]]: ...
    @_builtins.property
    @pulumi.getter(name="httpRequestMethods")
    def http_request_methods(
        self,
    ) -> Optional[
        Sequence[outputs.GetListenerRuleConditionHttpRequestMethodResult]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="pathPatterns")
    def path_patterns(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleConditionPathPatternResult]]: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleConditionQueryStringResult]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceIps")
    def source_ips(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleConditionSourceIpResult]]: ...

@pulumi.output_type
class GetListenerRuleConditionHostHeaderResult(dict):
    def __init__(
        __self__,
        *,
        regex_values: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetListenerRuleConditionHttpHeaderResult(dict):
    def __init__(
        __self__,
        *,
        http_header_name: _builtins.str,
        regex_values: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaderName")
    def http_header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetListenerRuleConditionHttpRequestMethodResult(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetListenerRuleConditionPathPatternResult(dict):
    def __init__(
        __self__,
        *,
        regex_values: Sequence[_builtins.str],
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetListenerRuleConditionQueryStringResult(dict):
    def __init__(
        __self__,
        *,
        values: Optional[
            Sequence[outputs.GetListenerRuleConditionQueryStringValueResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleConditionQueryStringValueResult]]: ...

@pulumi.output_type
class GetListenerRuleConditionQueryStringValueResult(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerRuleConditionSourceIpResult(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetListenerRuleTransformResult(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        host_header_rewrite_configs: Optional[
            Sequence[outputs.GetListenerRuleTransformHostHeaderRewriteConfigResult]
        ] = ...,
        url_rewrite_configs: Optional[
            Sequence[outputs.GetListenerRuleTransformUrlRewriteConfigResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostHeaderRewriteConfigs")
    def host_header_rewrite_configs(
        self,
    ) -> Optional[
        Sequence[outputs.GetListenerRuleTransformHostHeaderRewriteConfigResult]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="urlRewriteConfigs")
    def url_rewrite_configs(
        self,
    ) -> Optional[Sequence[outputs.GetListenerRuleTransformUrlRewriteConfigResult]]: ...

@pulumi.output_type
class GetListenerRuleTransformHostHeaderRewriteConfigResult(dict):
    def __init__(
        __self__,
        *,
        rewrites: Optional[
            Sequence[
                outputs.GetListenerRuleTransformHostHeaderRewriteConfigRewriteResult
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rewrites(
        self,
    ) -> Optional[
        Sequence[outputs.GetListenerRuleTransformHostHeaderRewriteConfigRewriteResult]
    ]: ...

@pulumi.output_type
class GetListenerRuleTransformHostHeaderRewriteConfigRewriteResult(dict):
    def __init__(__self__, *, regex: _builtins.str, replace: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> _builtins.str: ...

@pulumi.output_type
class GetListenerRuleTransformUrlRewriteConfigResult(dict):
    def __init__(
        __self__,
        *,
        rewrites: Optional[
            Sequence[outputs.GetListenerRuleTransformUrlRewriteConfigRewriteResult]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rewrites(
        self,
    ) -> Optional[
        Sequence[outputs.GetListenerRuleTransformUrlRewriteConfigRewriteResult]
    ]: ...

@pulumi.output_type
class GetListenerRuleTransformUrlRewriteConfigRewriteResult(dict):
    def __init__(__self__, *, regex: _builtins.str, replace: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> _builtins.str: ...

@pulumi.output_type
class GetLoadBalancerAccessLogsResult(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        enabled: _builtins.bool,
        prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetLoadBalancerConnectionLogResult(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        enabled: _builtins.bool,
        prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetLoadBalancerHealthCheckLogResult(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        enabled: _builtins.bool,
        prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetLoadBalancerIpamPoolResult(dict):
    def __init__(__self__, *, ipv4_ipam_pool_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetLoadBalancerSubnetMappingResult(dict):
    def __init__(
        __self__,
        *,
        allocation_id: _builtins.str,
        ipv6_address: _builtins.str,
        outpost_id: _builtins.str,
        private_ipv4_address: _builtins.str,
        subnet_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outpostId")
    def outpost_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateIpv4Address")
    def private_ipv4_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetTargetGroupHealthCheckResult(dict):
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        healthy_threshold: _builtins.int,
        interval: _builtins.int,
        matcher: _builtins.str,
        path: _builtins.str,
        port: _builtins.str,
        protocol: _builtins.str,
        timeout: _builtins.int,
        unhealthy_threshold: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def matcher(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int: ...

@pulumi.output_type
class GetTargetGroupStickinessResult(dict):
    def __init__(
        __self__,
        *,
        cookie_duration: _builtins.int,
        cookie_name: _builtins.str,
        enabled: _builtins.bool,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookieDuration")
    def cookie_duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cookieName")
    def cookie_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
