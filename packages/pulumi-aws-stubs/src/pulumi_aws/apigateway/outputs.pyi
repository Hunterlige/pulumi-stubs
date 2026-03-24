

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountThrottleSetting', 'DocumentationPartLocation', 'DomainNameEndpointConfiguration', 'DomainNameMutualTlsAuthentication', 'IntegrationTlsConfig', 'MethodSettingsSettings', 'RestApiEndpointConfiguration', 'RestApiPutTimeouts', 'StageAccessLogSettings', 'StageCanarySettings', 'UsagePlanApiStage', 'UsagePlanApiStageThrottle', 'UsagePlanQuotaSettings', 'UsagePlanThrottleSettings', 'GetApiKeysItemResult', 'GetDomainNameEndpointConfigurationResult', 'GetRestApiEndpointConfigurationResult']
@pulumi.output_type
class AccountThrottleSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, burst_limit: _builtins.int, rate_limit: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class DocumentationPartLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, method: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., status_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DomainNameEndpointConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, types: _builtins.str, ip_address_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]:
        
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
class IntegrationTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insecure_skip_verification: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insecureSkipVerification")
    def insecure_skip_verification(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MethodSettingsSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_data_encrypted: Optional[_builtins.bool] = ..., cache_ttl_in_seconds: Optional[_builtins.int] = ..., caching_enabled: Optional[_builtins.bool] = ..., data_trace_enabled: Optional[_builtins.bool] = ..., logging_level: Optional[_builtins.str] = ..., metrics_enabled: Optional[_builtins.bool] = ..., require_authorization_for_cache_control: Optional[_builtins.bool] = ..., throttling_burst_limit: Optional[_builtins.int] = ..., throttling_rate_limit: Optional[_builtins.float] = ..., unauthorized_cache_control_header_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheDataEncrypted")
    def cache_data_encrypted(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheTtlInSeconds")
    def cache_ttl_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachingEnabled")
    def caching_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsEnabled")
    def metrics_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireAuthorizationForCacheControl")
    def require_authorization_for_cache_control(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unauthorizedCacheControlHeaderStrategy")
    def unauthorized_cache_control_header_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RestApiEndpointConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, types: _builtins.str, ip_address_type: Optional[_builtins.str] = ..., vpc_endpoint_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointIds")
    def vpc_endpoint_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RestApiPutTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
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
class StageCanarySettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_id: _builtins.str, percent_traffic: Optional[_builtins.float] = ..., stage_variable_overrides: Optional[Mapping[str, _builtins.str]] = ..., use_stage_cache: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentTraffic")
    def percent_traffic(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageVariableOverrides")
    def stage_variable_overrides(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useStageCache")
    def use_stage_cache(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UsagePlanApiStage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_id: _builtins.str, stage: _builtins.str, throttles: Optional[Sequence[outputs.UsagePlanApiStageThrottle]] = ...) -> None:
        
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
    @pulumi.getter
    def throttles(self) -> Optional[Sequence[outputs.UsagePlanApiStageThrottle]]:
        
        ...
    


@pulumi.output_type
class UsagePlanApiStageThrottle(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: _builtins.str, burst_limit: Optional[_builtins.int] = ..., rate_limit: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class UsagePlanQuotaSettings(dict):
    def __init__(__self__, *, limit: _builtins.int, period: _builtins.str, offset: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offset(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class UsagePlanThrottleSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, burst_limit: Optional[_builtins.int] = ..., rate_limit: Optional[_builtins.float] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[_builtins.float]:
        ...
    


@pulumi.output_type
class GetApiKeysItemResult(dict):
    def __init__(__self__, *, created_date: _builtins.str, customer_id: _builtins.str, description: _builtins.str, enabled: _builtins.bool, id: _builtins.str, last_updated_date: _builtins.str, name: _builtins.str, stage_keys: Sequence[_builtins.str], tags: Mapping[str, _builtins.str], value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stageKeys")
    def stage_keys(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDomainNameEndpointConfigurationResult(dict):
    def __init__(__self__, *, ip_address_type: _builtins.str, types: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetRestApiEndpointConfigurationResult(dict):
    def __init__(__self__, *, ip_address_type: _builtins.str, types: Sequence[_builtins.str], vpc_endpoint_ids: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointIds")
    def vpc_endpoint_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


