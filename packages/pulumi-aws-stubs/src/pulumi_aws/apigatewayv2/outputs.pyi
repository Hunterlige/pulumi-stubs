

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiCorsConfiguration', 'AuthorizerJwtConfiguration', 'DomainNameDomainNameConfiguration', 'DomainNameMutualTlsAuthentication', 'IntegrationResponseParameter', 'IntegrationTlsConfig', 'RouteRequestParameter', 'RoutingRuleAction', 'RoutingRuleActionInvokeApi', 'RoutingRuleCondition', 'RoutingRuleConditionMatchBasePaths', 'RoutingRuleConditionMatchHeaders', 'RoutingRuleConditionMatchHeadersAnyOf', 'StageAccessLogSettings', 'StageDefaultRouteSettings', 'StageRouteSetting', 'GetApiCorsConfigurationResult']
@pulumi.output_type
class ApiCorsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_credentials: Optional[_builtins.bool] = ..., allow_headers: Optional[Sequence[_builtins.str]] = ..., allow_methods: Optional[Sequence[_builtins.str]] = ..., allow_origins: Optional[Sequence[_builtins.str]] = ..., expose_headers: Optional[Sequence[_builtins.str]] = ..., max_age: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AuthorizerJwtConfiguration(dict):
    def __init__(__self__, *, audiences: Optional[Sequence[_builtins.str]] = ..., issuer: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audiences(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainNameDomainNameConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_arn: _builtins.str, endpoint_type: _builtins.str, security_policy: _builtins.str, hosted_zone_id: Optional[_builtins.str] = ..., ip_address_type: Optional[_builtins.str] = ..., ownership_verification_certificate_arn: Optional[_builtins.str] = ..., target_domain_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDomainName")
    def target_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainNameMutualTlsAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, truststore_uri: _builtins.str, truststore_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="truststoreUri")
    def truststore_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="truststoreVersion")
    def truststore_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IntegrationResponseParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mappings: Mapping[str, _builtins.str], status_code: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IntegrationTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server_name_to_verify: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverNameToVerify")
    def server_name_to_verify(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RouteRequestParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, request_parameter_key: _builtins.str, required: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestParameterKey")
    def request_parameter_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class RoutingRuleAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, invoke_api: outputs.RoutingRuleActionInvokeApi) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeApi")
    def invoke_api(self) -> outputs.RoutingRuleActionInvokeApi:
        
        ...
    


@pulumi.output_type
class RoutingRuleActionInvokeApi(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_id: _builtins.str, stage: _builtins.str, strip_base_path: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stripBasePath")
    def strip_base_path(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RoutingRuleCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_base_paths: Optional[outputs.RoutingRuleConditionMatchBasePaths] = ..., match_headers: Optional[outputs.RoutingRuleConditionMatchHeaders] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchBasePaths")
    def match_base_paths(self) -> Optional[outputs.RoutingRuleConditionMatchBasePaths]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchHeaders")
    def match_headers(self) -> Optional[outputs.RoutingRuleConditionMatchHeaders]:
        
        ...
    


@pulumi.output_type
class RoutingRuleConditionMatchBasePaths(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, any_ofs: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOfs")
    def any_ofs(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RoutingRuleConditionMatchHeaders(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, any_of: outputs.RoutingRuleConditionMatchHeadersAnyOf) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> outputs.RoutingRuleConditionMatchHeadersAnyOf:
        
        ...
    


@pulumi.output_type
class RoutingRuleConditionMatchHeadersAnyOf(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header: _builtins.str, value_glob: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueGlob")
    def value_glob(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class StageAccessLogSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_arn: _builtins.str, format: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class StageDefaultRouteSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_trace_enabled: Optional[_builtins.bool] = ..., detailed_metrics_enabled: Optional[_builtins.bool] = ..., logging_level: Optional[_builtins.str] = ..., throttling_burst_limit: Optional[_builtins.int] = ..., throttling_rate_limit: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class StageRouteSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, route_key: _builtins.str, data_trace_enabled: Optional[_builtins.bool] = ..., detailed_metrics_enabled: Optional[_builtins.bool] = ..., logging_level: Optional[_builtins.str] = ..., throttling_burst_limit: Optional[_builtins.int] = ..., throttling_rate_limit: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class GetApiCorsConfigurationResult(dict):
    def __init__(__self__, *, allow_credentials: _builtins.bool, allow_headers: Sequence[_builtins.str], allow_methods: Sequence[_builtins.str], allow_origins: Sequence[_builtins.str], expose_headers: Sequence[_builtins.str], max_age: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> _builtins.int:
        
        ...
    


