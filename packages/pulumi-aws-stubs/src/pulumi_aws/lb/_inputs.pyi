

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListenerDefaultActionArgs', 'ListenerDefaultActionArgsDict', 'ListenerDefaultActionAuthenticateCognitoArgs', 'ListenerDefaultActionAuthenticateCognitoArgsDict', 'ListenerDefaultActionAuthenticateOidcArgs', 'ListenerDefaultActionAuthenticateOidcArgsDict', 'ListenerDefaultActionFixedResponseArgs', 'ListenerDefaultActionFixedResponseArgsDict', 'ListenerDefaultActionForwardArgs', 'ListenerDefaultActionForwardArgsDict', 'ListenerDefaultActionForwardStickinessArgs', 'ListenerDefaultActionForwardStickinessArgsDict', 'ListenerDefaultActionForwardTargetGroupArgs', 'ListenerDefaultActionForwardTargetGroupArgsDict', 'ListenerDefaultActionJwtValidationArgs', 'ListenerDefaultActionJwtValidationArgsDict', ..., ..., 'ListenerDefaultActionRedirectArgs', 'ListenerDefaultActionRedirectArgsDict', 'ListenerMutualAuthenticationArgs', 'ListenerMutualAuthenticationArgsDict', 'ListenerRuleActionArgs', 'ListenerRuleActionArgsDict', 'ListenerRuleActionAuthenticateCognitoArgs', 'ListenerRuleActionAuthenticateCognitoArgsDict', 'ListenerRuleActionAuthenticateOidcArgs', 'ListenerRuleActionAuthenticateOidcArgsDict', 'ListenerRuleActionFixedResponseArgs', 'ListenerRuleActionFixedResponseArgsDict', 'ListenerRuleActionForwardArgs', 'ListenerRuleActionForwardArgsDict', 'ListenerRuleActionForwardStickinessArgs', 'ListenerRuleActionForwardStickinessArgsDict', 'ListenerRuleActionForwardTargetGroupArgs', 'ListenerRuleActionForwardTargetGroupArgsDict', 'ListenerRuleActionJwtValidationArgs', 'ListenerRuleActionJwtValidationArgsDict', 'ListenerRuleActionJwtValidationAdditionalClaimArgs', ..., 'ListenerRuleActionRedirectArgs', 'ListenerRuleActionRedirectArgsDict', 'ListenerRuleConditionArgs', 'ListenerRuleConditionArgsDict', 'ListenerRuleConditionHostHeaderArgs', 'ListenerRuleConditionHostHeaderArgsDict', 'ListenerRuleConditionHttpHeaderArgs', 'ListenerRuleConditionHttpHeaderArgsDict', 'ListenerRuleConditionHttpRequestMethodArgs', 'ListenerRuleConditionHttpRequestMethodArgsDict', 'ListenerRuleConditionPathPatternArgs', 'ListenerRuleConditionPathPatternArgsDict', 'ListenerRuleConditionQueryStringArgs', 'ListenerRuleConditionQueryStringArgsDict', 'ListenerRuleConditionSourceIpArgs', 'ListenerRuleConditionSourceIpArgsDict', 'ListenerRuleTransformArgs', 'ListenerRuleTransformArgsDict', 'ListenerRuleTransformHostHeaderRewriteConfigArgs', ..., ..., ..., 'ListenerRuleTransformUrlRewriteConfigArgs', 'ListenerRuleTransformUrlRewriteConfigArgsDict', 'ListenerRuleTransformUrlRewriteConfigRewriteArgs', ..., 'LoadBalancerAccessLogsArgs', 'LoadBalancerAccessLogsArgsDict', 'LoadBalancerConnectionLogsArgs', 'LoadBalancerConnectionLogsArgsDict', 'LoadBalancerHealthCheckLogsArgs', 'LoadBalancerHealthCheckLogsArgsDict', 'LoadBalancerIpamPoolsArgs', 'LoadBalancerIpamPoolsArgsDict', 'LoadBalancerMinimumLoadBalancerCapacityArgs', 'LoadBalancerMinimumLoadBalancerCapacityArgsDict', 'LoadBalancerSubnetMappingArgs', 'LoadBalancerSubnetMappingArgsDict', 'TargetGroupHealthCheckArgs', 'TargetGroupHealthCheckArgsDict', 'TargetGroupStickinessArgs', 'TargetGroupStickinessArgsDict', 'TargetGroupTargetFailoverArgs', 'TargetGroupTargetFailoverArgsDict', 'TargetGroupTargetGroupHealthArgs', 'TargetGroupTargetGroupHealthArgsDict', 'TargetGroupTargetGroupHealthDnsFailoverArgs', 'TargetGroupTargetGroupHealthDnsFailoverArgsDict', ..., ..., 'TargetGroupTargetHealthStateArgs', 'TargetGroupTargetHealthStateArgsDict', 'GetListenerRuleActionArgs', 'GetListenerRuleActionArgsDict', 'GetListenerRuleActionAuthenticateCognitoArgs', 'GetListenerRuleActionAuthenticateCognitoArgsDict', 'GetListenerRuleActionAuthenticateOidcArgs', 'GetListenerRuleActionAuthenticateOidcArgsDict', 'GetListenerRuleActionFixedResponseArgs', 'GetListenerRuleActionFixedResponseArgsDict', 'GetListenerRuleActionForwardArgs', 'GetListenerRuleActionForwardArgsDict', 'GetListenerRuleActionForwardStickinessArgs', 'GetListenerRuleActionForwardStickinessArgsDict', 'GetListenerRuleActionForwardTargetGroupArgs', 'GetListenerRuleActionForwardTargetGroupArgsDict', 'GetListenerRuleActionJwtValidationArgs', 'GetListenerRuleActionJwtValidationArgsDict', ..., ..., 'GetListenerRuleActionRedirectArgs', 'GetListenerRuleActionRedirectArgsDict', 'GetListenerRuleConditionArgs', 'GetListenerRuleConditionArgsDict', 'GetListenerRuleConditionHostHeaderArgs', 'GetListenerRuleConditionHostHeaderArgsDict', 'GetListenerRuleConditionHttpHeaderArgs', 'GetListenerRuleConditionHttpHeaderArgsDict', 'GetListenerRuleConditionHttpRequestMethodArgs', 'GetListenerRuleConditionHttpRequestMethodArgsDict', 'GetListenerRuleConditionPathPatternArgs', 'GetListenerRuleConditionPathPatternArgsDict', 'GetListenerRuleConditionQueryStringArgs', 'GetListenerRuleConditionQueryStringArgsDict', 'GetListenerRuleConditionQueryStringValueArgs', 'GetListenerRuleConditionQueryStringValueArgsDict', 'GetListenerRuleConditionSourceIpArgs', 'GetListenerRuleConditionSourceIpArgsDict', 'GetListenerRuleTransformArgs', 'GetListenerRuleTransformArgsDict', ..., ..., ..., ..., 'GetListenerRuleTransformUrlRewriteConfigArgs', 'GetListenerRuleTransformUrlRewriteConfigArgsDict', ..., ...]
class ListenerDefaultActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    authenticate_cognito: NotRequired[pulumi.Input[ListenerDefaultActionAuthenticateCognitoArgsDict]]
    authenticate_oidc: NotRequired[pulumi.Input[ListenerDefaultActionAuthenticateOidcArgsDict]]
    fixed_response: NotRequired[pulumi.Input[ListenerDefaultActionFixedResponseArgsDict]]
    forward: NotRequired[pulumi.Input[ListenerDefaultActionForwardArgsDict]]
    jwt_validation: NotRequired[pulumi.Input[ListenerDefaultActionJwtValidationArgsDict]]
    order: NotRequired[pulumi.Input[_builtins.int]]
    redirect: NotRequired[pulumi.Input[ListenerDefaultActionRedirectArgsDict]]
    target_group_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerDefaultActionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], authenticate_cognito: Optional[pulumi.Input[ListenerDefaultActionAuthenticateCognitoArgs]] = ..., authenticate_oidc: Optional[pulumi.Input[ListenerDefaultActionAuthenticateOidcArgs]] = ..., fixed_response: Optional[pulumi.Input[ListenerDefaultActionFixedResponseArgs]] = ..., forward: Optional[pulumi.Input[ListenerDefaultActionForwardArgs]] = ..., jwt_validation: Optional[pulumi.Input[ListenerDefaultActionJwtValidationArgs]] = ..., order: Optional[pulumi.Input[_builtins.int]] = ..., redirect: Optional[pulumi.Input[ListenerDefaultActionRedirectArgs]] = ..., target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticateCognito")
    def authenticate_cognito(self) -> Optional[pulumi.Input[ListenerDefaultActionAuthenticateCognitoArgs]]:
        
        ...
    
    @authenticate_cognito.setter
    def authenticate_cognito(self, value: Optional[pulumi.Input[ListenerDefaultActionAuthenticateCognitoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticateOidc")
    def authenticate_oidc(self) -> Optional[pulumi.Input[ListenerDefaultActionAuthenticateOidcArgs]]:
        
        ...
    
    @authenticate_oidc.setter
    def authenticate_oidc(self, value: Optional[pulumi.Input[ListenerDefaultActionAuthenticateOidcArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional[pulumi.Input[ListenerDefaultActionFixedResponseArgs]]:
        
        ...
    
    @fixed_response.setter
    def fixed_response(self, value: Optional[pulumi.Input[ListenerDefaultActionFixedResponseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def forward(self) -> Optional[pulumi.Input[ListenerDefaultActionForwardArgs]]:
        
        ...
    
    @forward.setter
    def forward(self, value: Optional[pulumi.Input[ListenerDefaultActionForwardArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtValidation")
    def jwt_validation(self) -> Optional[pulumi.Input[ListenerDefaultActionJwtValidationArgs]]:
        
        ...
    
    @jwt_validation.setter
    def jwt_validation(self, value: Optional[pulumi.Input[ListenerDefaultActionJwtValidationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[pulumi.Input[ListenerDefaultActionRedirectArgs]]:
        
        ...
    
    @redirect.setter
    def redirect(self, value: Optional[pulumi.Input[ListenerDefaultActionRedirectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_group_arn.setter
    def target_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerDefaultActionAuthenticateCognitoArgsDict(TypedDict):
    user_pool_arn: pulumi.Input[_builtins.str]
    user_pool_client_id: pulumi.Input[_builtins.str]
    user_pool_domain: pulumi.Input[_builtins.str]
    authentication_request_extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    on_unauthenticated_request: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    session_cookie_name: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerDefaultActionAuthenticateCognitoArgs:
    def __init__(__self__, *, user_pool_arn: pulumi.Input[_builtins.str], user_pool_client_id: pulumi.Input[_builtins.str], user_pool_domain: pulumi.Input[_builtins.str], authentication_request_extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., on_unauthenticated_request: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., session_cookie_name: Optional[pulumi.Input[_builtins.str]] = ..., session_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_arn.setter
    def user_pool_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolClientId")
    def user_pool_client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_client_id.setter
    def user_pool_client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolDomain")
    def user_pool_domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_domain.setter
    def user_pool_domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authentication_request_extra_params.setter
    def authentication_request_extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_cookie_name.setter
    def session_cookie_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @session_timeout.setter
    def session_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerDefaultActionAuthenticateOidcArgsDict(TypedDict):
    authorization_endpoint: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    user_info_endpoint: pulumi.Input[_builtins.str]
    authentication_request_extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    on_unauthenticated_request: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    session_cookie_name: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerDefaultActionAuthenticateOidcArgs:
    def __init__(__self__, *, authorization_endpoint: pulumi.Input[_builtins.str], client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], issuer: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], user_info_endpoint: pulumi.Input[_builtins.str], authentication_request_extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., on_unauthenticated_request: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., session_cookie_name: Optional[pulumi.Input[_builtins.str]] = ..., session_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_info_endpoint.setter
    def user_info_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authentication_request_extra_params.setter
    def authentication_request_extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_cookie_name.setter
    def session_cookie_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @session_timeout.setter
    def session_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerDefaultActionFixedResponseArgsDict(TypedDict):
    content_type: pulumi.Input[_builtins.str]
    message_body: NotRequired[pulumi.Input[_builtins.str]]
    status_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerDefaultActionFixedResponseArgs:
    def __init__(__self__, *, content_type: pulumi.Input[_builtins.str], message_body: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageBody")
    def message_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_body.setter
    def message_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerDefaultActionForwardArgsDict(TypedDict):
    target_groups: pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgsDict]]]
    stickiness: NotRequired[pulumi.Input[ListenerDefaultActionForwardStickinessArgsDict]]


@pulumi.input_type
class ListenerDefaultActionForwardArgs:
    def __init__(__self__, *, target_groups: pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgs]]], stickiness: Optional[pulumi.Input[ListenerDefaultActionForwardStickinessArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgs]]]:
        
        ...
    
    @target_groups.setter
    def target_groups(self, value: pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionForwardTargetGroupArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stickiness(self) -> Optional[pulumi.Input[ListenerDefaultActionForwardStickinessArgs]]:
        
        ...
    
    @stickiness.setter
    def stickiness(self, value: Optional[pulumi.Input[ListenerDefaultActionForwardStickinessArgs]]): # -> None:
        ...
    


class ListenerDefaultActionForwardStickinessArgsDict(TypedDict):
    duration: pulumi.Input[_builtins.int]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ListenerDefaultActionForwardStickinessArgs:
    def __init__(__self__, *, duration: pulumi.Input[_builtins.int], enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ListenerDefaultActionForwardTargetGroupArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerDefaultActionForwardTargetGroupArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerDefaultActionJwtValidationArgsDict(TypedDict):
    issuer: pulumi.Input[_builtins.str]
    jwks_endpoint: pulumi.Input[_builtins.str]
    additional_claims: NotRequired[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionJwtValidationAdditionalClaimArgsDict]]]]


@pulumi.input_type
class ListenerDefaultActionJwtValidationArgs:
    def __init__(__self__, *, issuer: pulumi.Input[_builtins.str], jwks_endpoint: pulumi.Input[_builtins.str], additional_claims: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionJwtValidationAdditionalClaimArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksEndpoint")
    def jwks_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @jwks_endpoint.setter
    def jwks_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalClaims")
    def additional_claims(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionJwtValidationAdditionalClaimArgs]]]]:
        
        ...
    
    @additional_claims.setter
    def additional_claims(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerDefaultActionJwtValidationAdditionalClaimArgs]]]]): # -> None:
        ...
    


class ListenerDefaultActionJwtValidationAdditionalClaimArgsDict(TypedDict):
    format: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ListenerDefaultActionJwtValidationAdditionalClaimArgs:
    def __init__(__self__, *, format: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ListenerDefaultActionRedirectArgsDict(TypedDict):
    status_code: pulumi.Input[_builtins.str]
    host: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    query: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerDefaultActionRedirectArgs:
    def __init__(__self__, *, status_code: pulumi.Input[_builtins.str], host: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerMutualAuthenticationArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    advertise_trust_store_ca_names: NotRequired[pulumi.Input[_builtins.str]]
    ignore_client_certificate_expiry: NotRequired[pulumi.Input[_builtins.bool]]
    trust_store_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerMutualAuthenticationArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str], advertise_trust_store_ca_names: Optional[pulumi.Input[_builtins.str]] = ..., ignore_client_certificate_expiry: Optional[pulumi.Input[_builtins.bool]] = ..., trust_store_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertiseTrustStoreCaNames")
    def advertise_trust_store_ca_names(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @advertise_trust_store_ca_names.setter
    def advertise_trust_store_ca_names(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreClientCertificateExpiry")
    def ignore_client_certificate_expiry(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_client_certificate_expiry.setter
    def ignore_client_certificate_expiry(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_store_arn.setter
    def trust_store_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerRuleActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    authenticate_cognito: NotRequired[pulumi.Input[ListenerRuleActionAuthenticateCognitoArgsDict]]
    authenticate_oidc: NotRequired[pulumi.Input[ListenerRuleActionAuthenticateOidcArgsDict]]
    fixed_response: NotRequired[pulumi.Input[ListenerRuleActionFixedResponseArgsDict]]
    forward: NotRequired[pulumi.Input[ListenerRuleActionForwardArgsDict]]
    jwt_validation: NotRequired[pulumi.Input[ListenerRuleActionJwtValidationArgsDict]]
    order: NotRequired[pulumi.Input[_builtins.int]]
    redirect: NotRequired[pulumi.Input[ListenerRuleActionRedirectArgsDict]]
    target_group_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerRuleActionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], authenticate_cognito: Optional[pulumi.Input[ListenerRuleActionAuthenticateCognitoArgs]] = ..., authenticate_oidc: Optional[pulumi.Input[ListenerRuleActionAuthenticateOidcArgs]] = ..., fixed_response: Optional[pulumi.Input[ListenerRuleActionFixedResponseArgs]] = ..., forward: Optional[pulumi.Input[ListenerRuleActionForwardArgs]] = ..., jwt_validation: Optional[pulumi.Input[ListenerRuleActionJwtValidationArgs]] = ..., order: Optional[pulumi.Input[_builtins.int]] = ..., redirect: Optional[pulumi.Input[ListenerRuleActionRedirectArgs]] = ..., target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticateCognito")
    def authenticate_cognito(self) -> Optional[pulumi.Input[ListenerRuleActionAuthenticateCognitoArgs]]:
        
        ...
    
    @authenticate_cognito.setter
    def authenticate_cognito(self, value: Optional[pulumi.Input[ListenerRuleActionAuthenticateCognitoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticateOidc")
    def authenticate_oidc(self) -> Optional[pulumi.Input[ListenerRuleActionAuthenticateOidcArgs]]:
        
        ...
    
    @authenticate_oidc.setter
    def authenticate_oidc(self, value: Optional[pulumi.Input[ListenerRuleActionAuthenticateOidcArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional[pulumi.Input[ListenerRuleActionFixedResponseArgs]]:
        
        ...
    
    @fixed_response.setter
    def fixed_response(self, value: Optional[pulumi.Input[ListenerRuleActionFixedResponseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def forward(self) -> Optional[pulumi.Input[ListenerRuleActionForwardArgs]]:
        
        ...
    
    @forward.setter
    def forward(self, value: Optional[pulumi.Input[ListenerRuleActionForwardArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtValidation")
    def jwt_validation(self) -> Optional[pulumi.Input[ListenerRuleActionJwtValidationArgs]]:
        
        ...
    
    @jwt_validation.setter
    def jwt_validation(self, value: Optional[pulumi.Input[ListenerRuleActionJwtValidationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[pulumi.Input[ListenerRuleActionRedirectArgs]]:
        
        ...
    
    @redirect.setter
    def redirect(self, value: Optional[pulumi.Input[ListenerRuleActionRedirectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroupArn")
    def target_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_group_arn.setter
    def target_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerRuleActionAuthenticateCognitoArgsDict(TypedDict):
    user_pool_arn: pulumi.Input[_builtins.str]
    user_pool_client_id: pulumi.Input[_builtins.str]
    user_pool_domain: pulumi.Input[_builtins.str]
    authentication_request_extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    on_unauthenticated_request: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    session_cookie_name: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerRuleActionAuthenticateCognitoArgs:
    def __init__(__self__, *, user_pool_arn: pulumi.Input[_builtins.str], user_pool_client_id: pulumi.Input[_builtins.str], user_pool_domain: pulumi.Input[_builtins.str], authentication_request_extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., on_unauthenticated_request: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., session_cookie_name: Optional[pulumi.Input[_builtins.str]] = ..., session_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_arn.setter
    def user_pool_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolClientId")
    def user_pool_client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_client_id.setter
    def user_pool_client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolDomain")
    def user_pool_domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_domain.setter
    def user_pool_domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authentication_request_extra_params.setter
    def authentication_request_extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_cookie_name.setter
    def session_cookie_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @session_timeout.setter
    def session_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerRuleActionAuthenticateOidcArgsDict(TypedDict):
    authorization_endpoint: pulumi.Input[_builtins.str]
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    user_info_endpoint: pulumi.Input[_builtins.str]
    authentication_request_extra_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    on_unauthenticated_request: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    session_cookie_name: NotRequired[pulumi.Input[_builtins.str]]
    session_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerRuleActionAuthenticateOidcArgs:
    def __init__(__self__, *, authorization_endpoint: pulumi.Input[_builtins.str], client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], issuer: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], user_info_endpoint: pulumi.Input[_builtins.str], authentication_request_extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., on_unauthenticated_request: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., session_cookie_name: Optional[pulumi.Input[_builtins.str]] = ..., session_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_info_endpoint.setter
    def user_info_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authentication_request_extra_params.setter
    def authentication_request_extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_cookie_name.setter
    def session_cookie_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @session_timeout.setter
    def session_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerRuleActionFixedResponseArgsDict(TypedDict):
    content_type: pulumi.Input[_builtins.str]
    message_body: NotRequired[pulumi.Input[_builtins.str]]
    status_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerRuleActionFixedResponseArgs:
    def __init__(__self__, *, content_type: pulumi.Input[_builtins.str], message_body: Optional[pulumi.Input[_builtins.str]] = ..., status_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageBody")
    def message_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_body.setter
    def message_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerRuleActionForwardArgsDict(TypedDict):
    target_groups: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgsDict]]]
    stickiness: NotRequired[pulumi.Input[ListenerRuleActionForwardStickinessArgsDict]]


@pulumi.input_type
class ListenerRuleActionForwardArgs:
    def __init__(__self__, *, target_groups: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgs]]], stickiness: Optional[pulumi.Input[ListenerRuleActionForwardStickinessArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgs]]]:
        
        ...
    
    @target_groups.setter
    def target_groups(self, value: pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionForwardTargetGroupArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stickiness(self) -> Optional[pulumi.Input[ListenerRuleActionForwardStickinessArgs]]:
        
        ...
    
    @stickiness.setter
    def stickiness(self, value: Optional[pulumi.Input[ListenerRuleActionForwardStickinessArgs]]): # -> None:
        ...
    


class ListenerRuleActionForwardStickinessArgsDict(TypedDict):
    duration: pulumi.Input[_builtins.int]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ListenerRuleActionForwardStickinessArgs:
    def __init__(__self__, *, duration: pulumi.Input[_builtins.int], enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @duration.setter
    def duration(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ListenerRuleActionForwardTargetGroupArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ListenerRuleActionForwardTargetGroupArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ListenerRuleActionJwtValidationArgsDict(TypedDict):
    issuer: pulumi.Input[_builtins.str]
    jwks_endpoint: pulumi.Input[_builtins.str]
    additional_claims: NotRequired[pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionJwtValidationAdditionalClaimArgsDict]]]]


@pulumi.input_type
class ListenerRuleActionJwtValidationArgs:
    def __init__(__self__, *, issuer: pulumi.Input[_builtins.str], jwks_endpoint: pulumi.Input[_builtins.str], additional_claims: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionJwtValidationAdditionalClaimArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksEndpoint")
    def jwks_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @jwks_endpoint.setter
    def jwks_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalClaims")
    def additional_claims(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionJwtValidationAdditionalClaimArgs]]]]:
        
        ...
    
    @additional_claims.setter
    def additional_claims(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleActionJwtValidationAdditionalClaimArgs]]]]): # -> None:
        ...
    


class ListenerRuleActionJwtValidationAdditionalClaimArgsDict(TypedDict):
    format: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ListenerRuleActionJwtValidationAdditionalClaimArgs:
    def __init__(__self__, *, format: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ListenerRuleActionRedirectArgsDict(TypedDict):
    status_code: pulumi.Input[_builtins.str]
    host: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    query: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerRuleActionRedirectArgs:
    def __init__(__self__, *, status_code: pulumi.Input[_builtins.str], host: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., query: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerRuleConditionArgsDict(TypedDict):
    host_header: NotRequired[pulumi.Input[ListenerRuleConditionHostHeaderArgsDict]]
    http_header: NotRequired[pulumi.Input[ListenerRuleConditionHttpHeaderArgsDict]]
    http_request_method: NotRequired[pulumi.Input[ListenerRuleConditionHttpRequestMethodArgsDict]]
    path_pattern: NotRequired[pulumi.Input[ListenerRuleConditionPathPatternArgsDict]]
    query_strings: NotRequired[pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionQueryStringArgsDict]]]]
    source_ip: NotRequired[pulumi.Input[ListenerRuleConditionSourceIpArgsDict]]


@pulumi.input_type
class ListenerRuleConditionArgs:
    def __init__(__self__, *, host_header: Optional[pulumi.Input[ListenerRuleConditionHostHeaderArgs]] = ..., http_header: Optional[pulumi.Input[ListenerRuleConditionHttpHeaderArgs]] = ..., http_request_method: Optional[pulumi.Input[ListenerRuleConditionHttpRequestMethodArgs]] = ..., path_pattern: Optional[pulumi.Input[ListenerRuleConditionPathPatternArgs]] = ..., query_strings: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionQueryStringArgs]]]] = ..., source_ip: Optional[pulumi.Input[ListenerRuleConditionSourceIpArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostHeader")
    def host_header(self) -> Optional[pulumi.Input[ListenerRuleConditionHostHeaderArgs]]:
        
        ...
    
    @host_header.setter
    def host_header(self, value: Optional[pulumi.Input[ListenerRuleConditionHostHeaderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeader")
    def http_header(self) -> Optional[pulumi.Input[ListenerRuleConditionHttpHeaderArgs]]:
        
        ...
    
    @http_header.setter
    def http_header(self, value: Optional[pulumi.Input[ListenerRuleConditionHttpHeaderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpRequestMethod")
    def http_request_method(self) -> Optional[pulumi.Input[ListenerRuleConditionHttpRequestMethodArgs]]:
        
        ...
    
    @http_request_method.setter
    def http_request_method(self, value: Optional[pulumi.Input[ListenerRuleConditionHttpRequestMethodArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> Optional[pulumi.Input[ListenerRuleConditionPathPatternArgs]]:
        
        ...
    
    @path_pattern.setter
    def path_pattern(self, value: Optional[pulumi.Input[ListenerRuleConditionPathPatternArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionQueryStringArgs]]]]:
        
        ...
    
    @query_strings.setter
    def query_strings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListenerRuleConditionQueryStringArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[ListenerRuleConditionSourceIpArgs]]:
        
        ...
    
    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[ListenerRuleConditionSourceIpArgs]]): # -> None:
        ...
    


class ListenerRuleConditionHostHeaderArgsDict(TypedDict):
    regex_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ListenerRuleConditionHostHeaderArgs:
    def __init__(__self__, *, regex_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regex_values.setter
    def regex_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ListenerRuleConditionHttpHeaderArgsDict(TypedDict):
    http_header_name: pulumi.Input[_builtins.str]
    regex_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ListenerRuleConditionHttpHeaderArgs:
    def __init__(__self__, *, http_header_name: pulumi.Input[_builtins.str], regex_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaderName")
    def http_header_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @http_header_name.setter
    def http_header_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regex_values.setter
    def regex_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ListenerRuleConditionHttpRequestMethodArgsDict(TypedDict):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ListenerRuleConditionHttpRequestMethodArgs:
    def __init__(__self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        ...
    
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ListenerRuleConditionPathPatternArgsDict(TypedDict):
    regex_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ListenerRuleConditionPathPatternArgs:
    def __init__(__self__, *, regex_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regex_values.setter
    def regex_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ListenerRuleConditionQueryStringArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ListenerRuleConditionQueryStringArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str], key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ListenerRuleConditionSourceIpArgsDict(TypedDict):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ListenerRuleConditionSourceIpArgs:
    def __init__(__self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        ...
    
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ListenerRuleTransformArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    host_header_rewrite_config: NotRequired[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigArgsDict]]
    url_rewrite_config: NotRequired[pulumi.Input[ListenerRuleTransformUrlRewriteConfigArgsDict]]


@pulumi.input_type
class ListenerRuleTransformArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], host_header_rewrite_config: Optional[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigArgs]] = ..., url_rewrite_config: Optional[pulumi.Input[ListenerRuleTransformUrlRewriteConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostHeaderRewriteConfig")
    def host_header_rewrite_config(self) -> Optional[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigArgs]]:
        
        ...
    
    @host_header_rewrite_config.setter
    def host_header_rewrite_config(self, value: Optional[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlRewriteConfig")
    def url_rewrite_config(self) -> Optional[pulumi.Input[ListenerRuleTransformUrlRewriteConfigArgs]]:
        
        ...
    
    @url_rewrite_config.setter
    def url_rewrite_config(self, value: Optional[pulumi.Input[ListenerRuleTransformUrlRewriteConfigArgs]]): # -> None:
        ...
    


class ListenerRuleTransformHostHeaderRewriteConfigArgsDict(TypedDict):
    rewrite: NotRequired[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigRewriteArgsDict]]


@pulumi.input_type
class ListenerRuleTransformHostHeaderRewriteConfigArgs:
    def __init__(__self__, *, rewrite: Optional[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigRewriteArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rewrite(self) -> Optional[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigRewriteArgs]]:
        
        ...
    
    @rewrite.setter
    def rewrite(self, value: Optional[pulumi.Input[ListenerRuleTransformHostHeaderRewriteConfigRewriteArgs]]): # -> None:
        ...
    


class ListenerRuleTransformHostHeaderRewriteConfigRewriteArgsDict(TypedDict):
    regex: pulumi.Input[_builtins.str]
    replace: pulumi.Input[_builtins.str]


@pulumi.input_type
class ListenerRuleTransformHostHeaderRewriteConfigRewriteArgs:
    def __init__(__self__, *, regex: pulumi.Input[_builtins.str], replace: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @regex.setter
    def regex(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replace.setter
    def replace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ListenerRuleTransformUrlRewriteConfigArgsDict(TypedDict):
    rewrite: NotRequired[pulumi.Input[ListenerRuleTransformUrlRewriteConfigRewriteArgsDict]]


@pulumi.input_type
class ListenerRuleTransformUrlRewriteConfigArgs:
    def __init__(__self__, *, rewrite: Optional[pulumi.Input[ListenerRuleTransformUrlRewriteConfigRewriteArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rewrite(self) -> Optional[pulumi.Input[ListenerRuleTransformUrlRewriteConfigRewriteArgs]]:
        
        ...
    
    @rewrite.setter
    def rewrite(self, value: Optional[pulumi.Input[ListenerRuleTransformUrlRewriteConfigRewriteArgs]]): # -> None:
        ...
    


class ListenerRuleTransformUrlRewriteConfigRewriteArgsDict(TypedDict):
    regex: pulumi.Input[_builtins.str]
    replace: pulumi.Input[_builtins.str]


@pulumi.input_type
class ListenerRuleTransformUrlRewriteConfigRewriteArgs:
    def __init__(__self__, *, regex: pulumi.Input[_builtins.str], replace: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @regex.setter
    def regex(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replace.setter
    def replace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LoadBalancerAccessLogsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoadBalancerAccessLogsArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoadBalancerConnectionLogsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoadBalancerConnectionLogsArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoadBalancerHealthCheckLogsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoadBalancerHealthCheckLogsArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoadBalancerIpamPoolsArgsDict(TypedDict):
    ipv4_ipam_pool_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class LoadBalancerIpamPoolsArgs:
    def __init__(__self__, *, ipv4_ipam_pool_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LoadBalancerMinimumLoadBalancerCapacityArgsDict(TypedDict):
    capacity_units: pulumi.Input[_builtins.int]


@pulumi.input_type
class LoadBalancerMinimumLoadBalancerCapacityArgs:
    def __init__(__self__, *, capacity_units: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityUnits")
    def capacity_units(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @capacity_units.setter
    def capacity_units(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class LoadBalancerSubnetMappingArgsDict(TypedDict):
    subnet_id: pulumi.Input[_builtins.str]
    allocation_id: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_address: NotRequired[pulumi.Input[_builtins.str]]
    outpost_id: NotRequired[pulumi.Input[_builtins.str]]
    private_ipv4_address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoadBalancerSubnetMappingArgs:
    def __init__(__self__, *, subnet_id: pulumi.Input[_builtins.str], allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., outpost_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ipv4_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostId")
    def outpost_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @outpost_id.setter
    def outpost_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpv4Address")
    def private_ipv4_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ipv4_address.setter
    def private_ipv4_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TargetGroupHealthCheckArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    healthy_threshold: NotRequired[pulumi.Input[_builtins.int]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    matcher: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.int]]
    unhealthy_threshold: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TargetGroupHealthCheckArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ..., interval: Optional[pulumi.Input[_builtins.int]] = ..., matcher: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ..., unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def matcher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @matcher.setter
    def matcher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TargetGroupStickinessArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    cookie_duration: NotRequired[pulumi.Input[_builtins.int]]
    cookie_name: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class TargetGroupStickinessArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], cookie_duration: Optional[pulumi.Input[_builtins.int]] = ..., cookie_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieDuration")
    def cookie_duration(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cookie_duration.setter
    def cookie_duration(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieName")
    def cookie_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cookie_name.setter
    def cookie_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class TargetGroupTargetFailoverArgsDict(TypedDict):
    on_deregistration: pulumi.Input[_builtins.str]
    on_unhealthy: pulumi.Input[_builtins.str]


@pulumi.input_type
class TargetGroupTargetFailoverArgs:
    def __init__(__self__, *, on_deregistration: pulumi.Input[_builtins.str], on_unhealthy: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDeregistration")
    def on_deregistration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @on_deregistration.setter
    def on_deregistration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUnhealthy")
    def on_unhealthy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @on_unhealthy.setter
    def on_unhealthy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TargetGroupTargetGroupHealthArgsDict(TypedDict):
    dns_failover: NotRequired[pulumi.Input[TargetGroupTargetGroupHealthDnsFailoverArgsDict]]
    unhealthy_state_routing: NotRequired[pulumi.Input[TargetGroupTargetGroupHealthUnhealthyStateRoutingArgsDict]]


@pulumi.input_type
class TargetGroupTargetGroupHealthArgs:
    def __init__(__self__, *, dns_failover: Optional[pulumi.Input[TargetGroupTargetGroupHealthDnsFailoverArgs]] = ..., unhealthy_state_routing: Optional[pulumi.Input[TargetGroupTargetGroupHealthUnhealthyStateRoutingArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsFailover")
    def dns_failover(self) -> Optional[pulumi.Input[TargetGroupTargetGroupHealthDnsFailoverArgs]]:
        
        ...
    
    @dns_failover.setter
    def dns_failover(self, value: Optional[pulumi.Input[TargetGroupTargetGroupHealthDnsFailoverArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyStateRouting")
    def unhealthy_state_routing(self) -> Optional[pulumi.Input[TargetGroupTargetGroupHealthUnhealthyStateRoutingArgs]]:
        
        ...
    
    @unhealthy_state_routing.setter
    def unhealthy_state_routing(self, value: Optional[pulumi.Input[TargetGroupTargetGroupHealthUnhealthyStateRoutingArgs]]): # -> None:
        ...
    


class TargetGroupTargetGroupHealthDnsFailoverArgsDict(TypedDict):
    minimum_healthy_targets_count: NotRequired[pulumi.Input[_builtins.str]]
    minimum_healthy_targets_percentage: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TargetGroupTargetGroupHealthDnsFailoverArgs:
    def __init__(__self__, *, minimum_healthy_targets_count: Optional[pulumi.Input[_builtins.str]] = ..., minimum_healthy_targets_percentage: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsCount")
    def minimum_healthy_targets_count(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimum_healthy_targets_count.setter
    def minimum_healthy_targets_count(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsPercentage")
    def minimum_healthy_targets_percentage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimum_healthy_targets_percentage.setter
    def minimum_healthy_targets_percentage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TargetGroupTargetGroupHealthUnhealthyStateRoutingArgsDict(TypedDict):
    minimum_healthy_targets_count: NotRequired[pulumi.Input[_builtins.int]]
    minimum_healthy_targets_percentage: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TargetGroupTargetGroupHealthUnhealthyStateRoutingArgs:
    def __init__(__self__, *, minimum_healthy_targets_count: Optional[pulumi.Input[_builtins.int]] = ..., minimum_healthy_targets_percentage: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsCount")
    def minimum_healthy_targets_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minimum_healthy_targets_count.setter
    def minimum_healthy_targets_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumHealthyTargetsPercentage")
    def minimum_healthy_targets_percentage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimum_healthy_targets_percentage.setter
    def minimum_healthy_targets_percentage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TargetGroupTargetHealthStateArgsDict(TypedDict):
    enable_unhealthy_connection_termination: pulumi.Input[_builtins.bool]
    unhealthy_draining_interval: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TargetGroupTargetHealthStateArgs:
    def __init__(__self__, *, enable_unhealthy_connection_termination: pulumi.Input[_builtins.bool], unhealthy_draining_interval: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableUnhealthyConnectionTermination")
    def enable_unhealthy_connection_termination(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_unhealthy_connection_termination.setter
    def enable_unhealthy_connection_termination(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyDrainingInterval")
    def unhealthy_draining_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @unhealthy_draining_interval.setter
    def unhealthy_draining_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class GetListenerRuleActionArgsDict(TypedDict):
    order: _builtins.int
    type: _builtins.str
    authenticate_cognitos: NotRequired[Sequence[GetListenerRuleActionAuthenticateCognitoArgsDict]]
    authenticate_oidcs: NotRequired[Sequence[GetListenerRuleActionAuthenticateOidcArgsDict]]
    fixed_responses: NotRequired[Sequence[GetListenerRuleActionFixedResponseArgsDict]]
    forwards: NotRequired[Sequence[GetListenerRuleActionForwardArgsDict]]
    jwt_validations: NotRequired[Sequence[GetListenerRuleActionJwtValidationArgsDict]]
    redirects: NotRequired[Sequence[GetListenerRuleActionRedirectArgsDict]]


@pulumi.input_type
class GetListenerRuleActionArgs:
    def __init__(__self__, *, order: _builtins.int, type: _builtins.str, authenticate_cognitos: Optional[Sequence[GetListenerRuleActionAuthenticateCognitoArgs]] = ..., authenticate_oidcs: Optional[Sequence[GetListenerRuleActionAuthenticateOidcArgs]] = ..., fixed_responses: Optional[Sequence[GetListenerRuleActionFixedResponseArgs]] = ..., forwards: Optional[Sequence[GetListenerRuleActionForwardArgs]] = ..., jwt_validations: Optional[Sequence[GetListenerRuleActionJwtValidationArgs]] = ..., redirects: Optional[Sequence[GetListenerRuleActionRedirectArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int:
        
        ...
    
    @order.setter
    def order(self, value: _builtins.int): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @type.setter
    def type(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticateCognitos")
    def authenticate_cognitos(self) -> Optional[Sequence[GetListenerRuleActionAuthenticateCognitoArgs]]:
        
        ...
    
    @authenticate_cognitos.setter
    def authenticate_cognitos(self, value: Optional[Sequence[GetListenerRuleActionAuthenticateCognitoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticateOidcs")
    def authenticate_oidcs(self) -> Optional[Sequence[GetListenerRuleActionAuthenticateOidcArgs]]:
        
        ...
    
    @authenticate_oidcs.setter
    def authenticate_oidcs(self, value: Optional[Sequence[GetListenerRuleActionAuthenticateOidcArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedResponses")
    def fixed_responses(self) -> Optional[Sequence[GetListenerRuleActionFixedResponseArgs]]:
        
        ...
    
    @fixed_responses.setter
    def fixed_responses(self, value: Optional[Sequence[GetListenerRuleActionFixedResponseArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def forwards(self) -> Optional[Sequence[GetListenerRuleActionForwardArgs]]:
        
        ...
    
    @forwards.setter
    def forwards(self, value: Optional[Sequence[GetListenerRuleActionForwardArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtValidations")
    def jwt_validations(self) -> Optional[Sequence[GetListenerRuleActionJwtValidationArgs]]:
        
        ...
    
    @jwt_validations.setter
    def jwt_validations(self, value: Optional[Sequence[GetListenerRuleActionJwtValidationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redirects(self) -> Optional[Sequence[GetListenerRuleActionRedirectArgs]]:
        
        ...
    
    @redirects.setter
    def redirects(self, value: Optional[Sequence[GetListenerRuleActionRedirectArgs]]): # -> None:
        ...
    


class GetListenerRuleActionAuthenticateCognitoArgsDict(TypedDict):
    authentication_request_extra_params: Mapping[str, _builtins.str]
    on_unauthenticated_request: _builtins.str
    scope: _builtins.str
    session_cookie_name: _builtins.str
    session_timeout: _builtins.int
    user_pool_arn: _builtins.str
    user_pool_client_id: _builtins.str
    user_pool_domain: _builtins.str


@pulumi.input_type
class GetListenerRuleActionAuthenticateCognitoArgs:
    def __init__(__self__, *, authentication_request_extra_params: Mapping[str, _builtins.str], on_unauthenticated_request: _builtins.str, scope: _builtins.str, session_cookie_name: _builtins.str, session_timeout: _builtins.int, user_pool_arn: _builtins.str, user_pool_client_id: _builtins.str, user_pool_domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @authentication_request_extra_params.setter
    def authentication_request_extra_params(self, value: Mapping[str, _builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> _builtins.str:
        
        ...
    
    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    
    @scope.setter
    def scope(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> _builtins.str:
        
        ...
    
    @session_cookie_name.setter
    def session_cookie_name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> _builtins.int:
        
        ...
    
    @session_timeout.setter
    def session_timeout(self, value: _builtins.int): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolArn")
    def user_pool_arn(self) -> _builtins.str:
        
        ...
    
    @user_pool_arn.setter
    def user_pool_arn(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolClientId")
    def user_pool_client_id(self) -> _builtins.str:
        
        ...
    
    @user_pool_client_id.setter
    def user_pool_client_id(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolDomain")
    def user_pool_domain(self) -> _builtins.str:
        
        ...
    
    @user_pool_domain.setter
    def user_pool_domain(self, value: _builtins.str): # -> None:
        ...
    


class GetListenerRuleActionAuthenticateOidcArgsDict(TypedDict):
    authentication_request_extra_params: Mapping[str, _builtins.str]
    authorization_endpoint: _builtins.str
    client_id: _builtins.str
    issuer: _builtins.str
    on_unauthenticated_request: _builtins.str
    scope: _builtins.str
    session_cookie_name: _builtins.str
    session_timeout: _builtins.int
    token_endpoint: _builtins.str
    user_info_endpoint: _builtins.str


@pulumi.input_type
class GetListenerRuleActionAuthenticateOidcArgs:
    def __init__(__self__, *, authentication_request_extra_params: Mapping[str, _builtins.str], authorization_endpoint: _builtins.str, client_id: _builtins.str, issuer: _builtins.str, on_unauthenticated_request: _builtins.str, scope: _builtins.str, session_cookie_name: _builtins.str, session_timeout: _builtins.int, token_endpoint: _builtins.str, user_info_endpoint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationRequestExtraParams")
    def authentication_request_extra_params(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @authentication_request_extra_params.setter
    def authentication_request_extra_params(self, value: Mapping[str, _builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str:
        
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @client_id.setter
    def client_id(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @issuer.setter
    def issuer(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> _builtins.str:
        
        ...
    
    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    
    @scope.setter
    def scope(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionCookieName")
    def session_cookie_name(self) -> _builtins.str:
        
        ...
    
    @session_cookie_name.setter
    def session_cookie_name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTimeout")
    def session_timeout(self) -> _builtins.int:
        
        ...
    
    @session_timeout.setter
    def session_timeout(self, value: _builtins.int): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfoEndpoint")
    def user_info_endpoint(self) -> _builtins.str:
        
        ...
    
    @user_info_endpoint.setter
    def user_info_endpoint(self, value: _builtins.str): # -> None:
        ...
    


class GetListenerRuleActionFixedResponseArgsDict(TypedDict):
    content_type: _builtins.str
    message_body: _builtins.str
    status_code: _builtins.str


@pulumi.input_type
class GetListenerRuleActionFixedResponseArgs:
    def __init__(__self__, *, content_type: _builtins.str, message_body: _builtins.str, status_code: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @content_type.setter
    def content_type(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageBody")
    def message_body(self) -> _builtins.str:
        
        ...
    
    @message_body.setter
    def message_body(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str:
        
        ...
    
    @status_code.setter
    def status_code(self, value: _builtins.str): # -> None:
        ...
    


class GetListenerRuleActionForwardArgsDict(TypedDict):
    stickinesses: NotRequired[Sequence[GetListenerRuleActionForwardStickinessArgsDict]]
    target_groups: NotRequired[Sequence[GetListenerRuleActionForwardTargetGroupArgsDict]]


@pulumi.input_type
class GetListenerRuleActionForwardArgs:
    def __init__(__self__, *, stickinesses: Optional[Sequence[GetListenerRuleActionForwardStickinessArgs]] = ..., target_groups: Optional[Sequence[GetListenerRuleActionForwardTargetGroupArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stickinesses(self) -> Optional[Sequence[GetListenerRuleActionForwardStickinessArgs]]:
        
        ...
    
    @stickinesses.setter
    def stickinesses(self, value: Optional[Sequence[GetListenerRuleActionForwardStickinessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> Optional[Sequence[GetListenerRuleActionForwardTargetGroupArgs]]:
        
        ...
    
    @target_groups.setter
    def target_groups(self, value: Optional[Sequence[GetListenerRuleActionForwardTargetGroupArgs]]): # -> None:
        ...
    


class GetListenerRuleActionForwardStickinessArgsDict(TypedDict):
    duration: _builtins.int
    enabled: _builtins.bool


@pulumi.input_type
class GetListenerRuleActionForwardStickinessArgs:
    def __init__(__self__, *, duration: _builtins.int, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.int:
        
        ...
    
    @duration.setter
    def duration(self, value: _builtins.int): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @enabled.setter
    def enabled(self, value: _builtins.bool): # -> None:
        ...
    


class GetListenerRuleActionForwardTargetGroupArgsDict(TypedDict):
    arn: _builtins.str
    weight: _builtins.int


@pulumi.input_type
class GetListenerRuleActionForwardTargetGroupArgs:
    def __init__(__self__, *, arn: _builtins.str, weight: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @arn.setter
    def arn(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int:
        
        ...
    
    @weight.setter
    def weight(self, value: _builtins.int): # -> None:
        ...
    


class GetListenerRuleActionJwtValidationArgsDict(TypedDict):
    issuer: _builtins.str
    jwks_endpoint: _builtins.str
    additional_claims: NotRequired[Sequence[GetListenerRuleActionJwtValidationAdditionalClaimArgsDict]]


@pulumi.input_type
class GetListenerRuleActionJwtValidationArgs:
    def __init__(__self__, *, issuer: _builtins.str, jwks_endpoint: _builtins.str, additional_claims: Optional[Sequence[GetListenerRuleActionJwtValidationAdditionalClaimArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @issuer.setter
    def issuer(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwksEndpoint")
    def jwks_endpoint(self) -> _builtins.str:
        
        ...
    
    @jwks_endpoint.setter
    def jwks_endpoint(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalClaims")
    def additional_claims(self) -> Optional[Sequence[GetListenerRuleActionJwtValidationAdditionalClaimArgs]]:
        
        ...
    
    @additional_claims.setter
    def additional_claims(self, value: Optional[Sequence[GetListenerRuleActionJwtValidationAdditionalClaimArgs]]): # -> None:
        ...
    


class GetListenerRuleActionJwtValidationAdditionalClaimArgsDict(TypedDict):
    format: _builtins.str
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetListenerRuleActionJwtValidationAdditionalClaimArgs:
    def __init__(__self__, *, format: _builtins.str, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str:
        
        ...
    
    @format.setter
    def format(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetListenerRuleActionRedirectArgsDict(TypedDict):
    host: _builtins.str
    path: _builtins.str
    port: _builtins.str
    protocol: _builtins.str
    query: _builtins.str
    status_code: _builtins.str


@pulumi.input_type
class GetListenerRuleActionRedirectArgs:
    def __init__(__self__, *, host: _builtins.str, path: _builtins.str, port: _builtins.str, protocol: _builtins.str, query: _builtins.str, status_code: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str:
        
        ...
    
    @host.setter
    def host(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @path.setter
    def path(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str:
        
        ...
    
    @port.setter
    def port(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @protocol.setter
    def protocol(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    
    @query.setter
    def query(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str:
        
        ...
    
    @status_code.setter
    def status_code(self, value: _builtins.str): # -> None:
        ...
    


class GetListenerRuleConditionArgsDict(TypedDict):
    host_headers: NotRequired[Sequence[GetListenerRuleConditionHostHeaderArgsDict]]
    http_headers: NotRequired[Sequence[GetListenerRuleConditionHttpHeaderArgsDict]]
    http_request_methods: NotRequired[Sequence[GetListenerRuleConditionHttpRequestMethodArgsDict]]
    path_patterns: NotRequired[Sequence[GetListenerRuleConditionPathPatternArgsDict]]
    query_strings: NotRequired[Sequence[GetListenerRuleConditionQueryStringArgsDict]]
    source_ips: NotRequired[Sequence[GetListenerRuleConditionSourceIpArgsDict]]


@pulumi.input_type
class GetListenerRuleConditionArgs:
    def __init__(__self__, *, host_headers: Optional[Sequence[GetListenerRuleConditionHostHeaderArgs]] = ..., http_headers: Optional[Sequence[GetListenerRuleConditionHttpHeaderArgs]] = ..., http_request_methods: Optional[Sequence[GetListenerRuleConditionHttpRequestMethodArgs]] = ..., path_patterns: Optional[Sequence[GetListenerRuleConditionPathPatternArgs]] = ..., query_strings: Optional[Sequence[GetListenerRuleConditionQueryStringArgs]] = ..., source_ips: Optional[Sequence[GetListenerRuleConditionSourceIpArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostHeaders")
    def host_headers(self) -> Optional[Sequence[GetListenerRuleConditionHostHeaderArgs]]:
        
        ...
    
    @host_headers.setter
    def host_headers(self, value: Optional[Sequence[GetListenerRuleConditionHostHeaderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[GetListenerRuleConditionHttpHeaderArgs]]:
        
        ...
    
    @http_headers.setter
    def http_headers(self, value: Optional[Sequence[GetListenerRuleConditionHttpHeaderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpRequestMethods")
    def http_request_methods(self) -> Optional[Sequence[GetListenerRuleConditionHttpRequestMethodArgs]]:
        
        ...
    
    @http_request_methods.setter
    def http_request_methods(self, value: Optional[Sequence[GetListenerRuleConditionHttpRequestMethodArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathPatterns")
    def path_patterns(self) -> Optional[Sequence[GetListenerRuleConditionPathPatternArgs]]:
        
        ...
    
    @path_patterns.setter
    def path_patterns(self, value: Optional[Sequence[GetListenerRuleConditionPathPatternArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(self) -> Optional[Sequence[GetListenerRuleConditionQueryStringArgs]]:
        
        ...
    
    @query_strings.setter
    def query_strings(self, value: Optional[Sequence[GetListenerRuleConditionQueryStringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIps")
    def source_ips(self) -> Optional[Sequence[GetListenerRuleConditionSourceIpArgs]]:
        
        ...
    
    @source_ips.setter
    def source_ips(self, value: Optional[Sequence[GetListenerRuleConditionSourceIpArgs]]): # -> None:
        ...
    


class GetListenerRuleConditionHostHeaderArgsDict(TypedDict):
    regex_values: Sequence[_builtins.str]
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetListenerRuleConditionHostHeaderArgs:
    def __init__(__self__, *, regex_values: Sequence[_builtins.str], values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @regex_values.setter
    def regex_values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetListenerRuleConditionHttpHeaderArgsDict(TypedDict):
    http_header_name: _builtins.str
    regex_values: Sequence[_builtins.str]
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetListenerRuleConditionHttpHeaderArgs:
    def __init__(__self__, *, http_header_name: _builtins.str, regex_values: Sequence[_builtins.str], values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaderName")
    def http_header_name(self) -> _builtins.str:
        
        ...
    
    @http_header_name.setter
    def http_header_name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @regex_values.setter
    def regex_values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetListenerRuleConditionHttpRequestMethodArgsDict(TypedDict):
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetListenerRuleConditionHttpRequestMethodArgs:
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetListenerRuleConditionPathPatternArgsDict(TypedDict):
    regex_values: Sequence[_builtins.str]
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetListenerRuleConditionPathPatternArgs:
    def __init__(__self__, *, regex_values: Sequence[_builtins.str], values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexValues")
    def regex_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @regex_values.setter
    def regex_values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetListenerRuleConditionQueryStringArgsDict(TypedDict):
    values: NotRequired[Sequence[GetListenerRuleConditionQueryStringValueArgsDict]]


@pulumi.input_type
class GetListenerRuleConditionQueryStringArgs:
    def __init__(__self__, *, values: Optional[Sequence[GetListenerRuleConditionQueryStringValueArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[GetListenerRuleConditionQueryStringValueArgs]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[Sequence[GetListenerRuleConditionQueryStringValueArgs]]): # -> None:
        ...
    


class GetListenerRuleConditionQueryStringValueArgsDict(TypedDict):
    key: _builtins.str
    value: _builtins.str


@pulumi.input_type
class GetListenerRuleConditionQueryStringValueArgs:
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @key.setter
    def key(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @value.setter
    def value(self, value: _builtins.str): # -> None:
        ...
    


class GetListenerRuleConditionSourceIpArgsDict(TypedDict):
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetListenerRuleConditionSourceIpArgs:
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetListenerRuleTransformArgsDict(TypedDict):
    type: _builtins.str
    host_header_rewrite_configs: NotRequired[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigArgsDict]]
    url_rewrite_configs: NotRequired[Sequence[GetListenerRuleTransformUrlRewriteConfigArgsDict]]


@pulumi.input_type
class GetListenerRuleTransformArgs:
    def __init__(__self__, *, type: _builtins.str, host_header_rewrite_configs: Optional[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigArgs]] = ..., url_rewrite_configs: Optional[Sequence[GetListenerRuleTransformUrlRewriteConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @type.setter
    def type(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostHeaderRewriteConfigs")
    def host_header_rewrite_configs(self) -> Optional[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigArgs]]:
        
        ...
    
    @host_header_rewrite_configs.setter
    def host_header_rewrite_configs(self, value: Optional[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlRewriteConfigs")
    def url_rewrite_configs(self) -> Optional[Sequence[GetListenerRuleTransformUrlRewriteConfigArgs]]:
        
        ...
    
    @url_rewrite_configs.setter
    def url_rewrite_configs(self, value: Optional[Sequence[GetListenerRuleTransformUrlRewriteConfigArgs]]): # -> None:
        ...
    


class GetListenerRuleTransformHostHeaderRewriteConfigArgsDict(TypedDict):
    rewrites: NotRequired[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigRewriteArgsDict]]


@pulumi.input_type
class GetListenerRuleTransformHostHeaderRewriteConfigArgs:
    def __init__(__self__, *, rewrites: Optional[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigRewriteArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rewrites(self) -> Optional[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigRewriteArgs]]:
        
        ...
    
    @rewrites.setter
    def rewrites(self, value: Optional[Sequence[GetListenerRuleTransformHostHeaderRewriteConfigRewriteArgs]]): # -> None:
        ...
    


class GetListenerRuleTransformHostHeaderRewriteConfigRewriteArgsDict(TypedDict):
    regex: _builtins.str
    replace: _builtins.str


@pulumi.input_type
class GetListenerRuleTransformHostHeaderRewriteConfigRewriteArgs:
    def __init__(__self__, *, regex: _builtins.str, replace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str:
        
        ...
    
    @regex.setter
    def regex(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replace(self) -> _builtins.str:
        
        ...
    
    @replace.setter
    def replace(self, value: _builtins.str): # -> None:
        ...
    


class GetListenerRuleTransformUrlRewriteConfigArgsDict(TypedDict):
    rewrites: NotRequired[Sequence[GetListenerRuleTransformUrlRewriteConfigRewriteArgsDict]]


@pulumi.input_type
class GetListenerRuleTransformUrlRewriteConfigArgs:
    def __init__(__self__, *, rewrites: Optional[Sequence[GetListenerRuleTransformUrlRewriteConfigRewriteArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rewrites(self) -> Optional[Sequence[GetListenerRuleTransformUrlRewriteConfigRewriteArgs]]:
        
        ...
    
    @rewrites.setter
    def rewrites(self, value: Optional[Sequence[GetListenerRuleTransformUrlRewriteConfigRewriteArgs]]): # -> None:
        ...
    


class GetListenerRuleTransformUrlRewriteConfigRewriteArgsDict(TypedDict):
    regex: _builtins.str
    replace: _builtins.str


@pulumi.input_type
class GetListenerRuleTransformUrlRewriteConfigRewriteArgs:
    def __init__(__self__, *, regex: _builtins.str, replace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str:
        
        ...
    
    @regex.setter
    def regex(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replace(self) -> _builtins.str:
        
        ...
    
    @replace.setter
    def replace(self, value: _builtins.str): # -> None:
        ...
    


