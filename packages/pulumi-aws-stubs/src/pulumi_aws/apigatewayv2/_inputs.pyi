

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiCorsConfigurationArgs', 'ApiCorsConfigurationArgsDict', 'AuthorizerJwtConfigurationArgs', 'AuthorizerJwtConfigurationArgsDict', 'DomainNameDomainNameConfigurationArgs', 'DomainNameDomainNameConfigurationArgsDict', 'DomainNameMutualTlsAuthenticationArgs', 'DomainNameMutualTlsAuthenticationArgsDict', 'IntegrationResponseParameterArgs', 'IntegrationResponseParameterArgsDict', 'IntegrationTlsConfigArgs', 'IntegrationTlsConfigArgsDict', 'RouteRequestParameterArgs', 'RouteRequestParameterArgsDict', 'RoutingRuleActionArgs', 'RoutingRuleActionArgsDict', 'RoutingRuleActionInvokeApiArgs', 'RoutingRuleActionInvokeApiArgsDict', 'RoutingRuleConditionArgs', 'RoutingRuleConditionArgsDict', 'RoutingRuleConditionMatchBasePathsArgs', 'RoutingRuleConditionMatchBasePathsArgsDict', 'RoutingRuleConditionMatchHeadersArgs', 'RoutingRuleConditionMatchHeadersArgsDict', 'RoutingRuleConditionMatchHeadersAnyOfArgs', 'RoutingRuleConditionMatchHeadersAnyOfArgsDict', 'StageAccessLogSettingsArgs', 'StageAccessLogSettingsArgsDict', 'StageDefaultRouteSettingsArgs', 'StageDefaultRouteSettingsArgsDict', 'StageRouteSettingArgs', 'StageRouteSettingArgsDict']
class ApiCorsConfigurationArgsDict(TypedDict):
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    allow_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ApiCorsConfigurationArgs:
    def __init__(__self__, *, allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ..., allow_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allow_methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allow_origins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_age: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allow_headers.setter
    def allow_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allow_methods.setter
    def allow_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allow_origins.setter
    def allow_origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class AuthorizerJwtConfigurationArgsDict(TypedDict):
    audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthorizerJwtConfigurationArgs:
    def __init__(__self__, *, audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., issuer: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainNameDomainNameConfigurationArgsDict(TypedDict):
    certificate_arn: pulumi.Input[_builtins.str]
    endpoint_type: pulumi.Input[_builtins.str]
    security_policy: pulumi.Input[_builtins.str]
    hosted_zone_id: NotRequired[pulumi.Input[_builtins.str]]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    ownership_verification_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    target_domain_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainNameDomainNameConfigurationArgs:
    def __init__(__self__, *, certificate_arn: pulumi.Input[_builtins.str], endpoint_type: pulumi.Input[_builtins.str], security_policy: pulumi.Input[_builtins.str], hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., ownership_verification_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., target_domain_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @certificate_arn.setter
    def certificate_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_policy.setter
    def security_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDomainName")
    def target_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_domain_name.setter
    def target_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DomainNameMutualTlsAuthenticationArgsDict(TypedDict):
    truststore_uri: pulumi.Input[_builtins.str]
    truststore_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DomainNameMutualTlsAuthenticationArgs:
    def __init__(__self__, *, truststore_uri: pulumi.Input[_builtins.str], truststore_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="truststoreUri")
    def truststore_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @truststore_uri.setter
    def truststore_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="truststoreVersion")
    def truststore_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @truststore_version.setter
    def truststore_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IntegrationResponseParameterArgsDict(TypedDict):
    mappings: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    status_code: pulumi.Input[_builtins.str]


@pulumi.input_type
class IntegrationResponseParameterArgs:
    def __init__(__self__, *, mappings: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], status_code: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @mappings.setter
    def mappings(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IntegrationTlsConfigArgsDict(TypedDict):
    server_name_to_verify: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IntegrationTlsConfigArgs:
    def __init__(__self__, *, server_name_to_verify: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverNameToVerify")
    def server_name_to_verify(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_name_to_verify.setter
    def server_name_to_verify(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RouteRequestParameterArgsDict(TypedDict):
    request_parameter_key: pulumi.Input[_builtins.str]
    required: pulumi.Input[_builtins.bool]


@pulumi.input_type
class RouteRequestParameterArgs:
    def __init__(__self__, *, request_parameter_key: pulumi.Input[_builtins.str], required: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameterKey")
    def request_parameter_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @request_parameter_key.setter
    def request_parameter_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @required.setter
    def required(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class RoutingRuleActionArgsDict(TypedDict):
    invoke_api: pulumi.Input[RoutingRuleActionInvokeApiArgsDict]


@pulumi.input_type
class RoutingRuleActionArgs:
    def __init__(__self__, *, invoke_api: pulumi.Input[RoutingRuleActionInvokeApiArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeApi")
    def invoke_api(self) -> pulumi.Input[RoutingRuleActionInvokeApiArgs]:
        
        ...
    
    @invoke_api.setter
    def invoke_api(self, value: pulumi.Input[RoutingRuleActionInvokeApiArgs]): # -> None:
        ...
    


class RoutingRuleActionInvokeApiArgsDict(TypedDict):
    api_id: pulumi.Input[_builtins.str]
    stage: pulumi.Input[_builtins.str]
    strip_base_path: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class RoutingRuleActionInvokeApiArgs:
    def __init__(__self__, *, api_id: pulumi.Input[_builtins.str], stage: pulumi.Input[_builtins.str], strip_base_path: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stage.setter
    def stage(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stripBasePath")
    def strip_base_path(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @strip_base_path.setter
    def strip_base_path(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RoutingRuleConditionArgsDict(TypedDict):
    match_base_paths: NotRequired[pulumi.Input[RoutingRuleConditionMatchBasePathsArgsDict]]
    match_headers: NotRequired[pulumi.Input[RoutingRuleConditionMatchHeadersArgsDict]]


@pulumi.input_type
class RoutingRuleConditionArgs:
    def __init__(__self__, *, match_base_paths: Optional[pulumi.Input[RoutingRuleConditionMatchBasePathsArgs]] = ..., match_headers: Optional[pulumi.Input[RoutingRuleConditionMatchHeadersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchBasePaths")
    def match_base_paths(self) -> Optional[pulumi.Input[RoutingRuleConditionMatchBasePathsArgs]]:
        
        ...
    
    @match_base_paths.setter
    def match_base_paths(self, value: Optional[pulumi.Input[RoutingRuleConditionMatchBasePathsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchHeaders")
    def match_headers(self) -> Optional[pulumi.Input[RoutingRuleConditionMatchHeadersArgs]]:
        
        ...
    
    @match_headers.setter
    def match_headers(self, value: Optional[pulumi.Input[RoutingRuleConditionMatchHeadersArgs]]): # -> None:
        ...
    


class RoutingRuleConditionMatchBasePathsArgsDict(TypedDict):
    any_ofs: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class RoutingRuleConditionMatchBasePathsArgs:
    def __init__(__self__, *, any_ofs: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOfs")
    def any_ofs(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @any_ofs.setter
    def any_ofs(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class RoutingRuleConditionMatchHeadersArgsDict(TypedDict):
    any_of: pulumi.Input[RoutingRuleConditionMatchHeadersAnyOfArgsDict]


@pulumi.input_type
class RoutingRuleConditionMatchHeadersArgs:
    def __init__(__self__, *, any_of: pulumi.Input[RoutingRuleConditionMatchHeadersAnyOfArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> pulumi.Input[RoutingRuleConditionMatchHeadersAnyOfArgs]:
        
        ...
    
    @any_of.setter
    def any_of(self, value: pulumi.Input[RoutingRuleConditionMatchHeadersAnyOfArgs]): # -> None:
        ...
    


class RoutingRuleConditionMatchHeadersAnyOfArgsDict(TypedDict):
    header: pulumi.Input[_builtins.str]
    value_glob: pulumi.Input[_builtins.str]


@pulumi.input_type
class RoutingRuleConditionMatchHeadersAnyOfArgs:
    def __init__(__self__, *, header: pulumi.Input[_builtins.str], value_glob: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @header.setter
    def header(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueGlob")
    def value_glob(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value_glob.setter
    def value_glob(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class StageAccessLogSettingsArgsDict(TypedDict):
    destination_arn: pulumi.Input[_builtins.str]
    format: pulumi.Input[_builtins.str]


@pulumi.input_type
class StageAccessLogSettingsArgs:
    def __init__(__self__, *, destination_arn: pulumi.Input[_builtins.str], format: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class StageDefaultRouteSettingsArgsDict(TypedDict):
    data_trace_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    detailed_metrics_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    logging_level: NotRequired[pulumi.Input[_builtins.str]]
    throttling_burst_limit: NotRequired[pulumi.Input[_builtins.int]]
    throttling_rate_limit: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StageDefaultRouteSettingsArgs:
    def __init__(__self__, *, data_trace_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., detailed_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., logging_level: Optional[pulumi.Input[_builtins.str]] = ..., throttling_burst_limit: Optional[pulumi.Input[_builtins.int]] = ..., throttling_rate_limit: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @data_trace_enabled.setter
    def data_trace_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @detailed_metrics_enabled.setter
    def detailed_metrics_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throttling_burst_limit.setter
    def throttling_burst_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @throttling_rate_limit.setter
    def throttling_rate_limit(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class StageRouteSettingArgsDict(TypedDict):
    route_key: pulumi.Input[_builtins.str]
    data_trace_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    detailed_metrics_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    logging_level: NotRequired[pulumi.Input[_builtins.str]]
    throttling_burst_limit: NotRequired[pulumi.Input[_builtins.int]]
    throttling_rate_limit: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StageRouteSettingArgs:
    def __init__(__self__, *, route_key: pulumi.Input[_builtins.str], data_trace_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., detailed_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., logging_level: Optional[pulumi.Input[_builtins.str]] = ..., throttling_burst_limit: Optional[pulumi.Input[_builtins.int]] = ..., throttling_rate_limit: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @route_key.setter
    def route_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @data_trace_enabled.setter
    def data_trace_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @detailed_metrics_enabled.setter
    def detailed_metrics_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @throttling_burst_limit.setter
    def throttling_burst_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @throttling_rate_limit.setter
    def throttling_rate_limit(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


