

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointAuthenticationOption', 'EndpointClientConnectOptions', 'EndpointClientLoginBannerOptions', 'EndpointClientRouteEnforcementOptions', 'EndpointConnectionLogOptions', 'GetEndpointAuthenticationOptionResult', 'GetEndpointClientConnectOptionResult', 'GetEndpointClientLoginBannerOptionResult', 'GetEndpointClientRouteEnforcementOptionResult', 'GetEndpointConnectionLogOptionResult', 'GetEndpointFilterResult']
@pulumi.output_type
class EndpointAuthenticationOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, active_directory_id: Optional[_builtins.str] = ..., root_certificate_chain_arn: Optional[_builtins.str] = ..., saml_provider_arn: Optional[_builtins.str] = ..., self_service_saml_provider_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootCertificateChainArn")
    def root_certificate_chain_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="samlProviderArn")
    def saml_provider_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfServiceSamlProviderArn")
    def self_service_saml_provider_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointClientConnectOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., lambda_function_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EndpointClientLoginBannerOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, banner_text: Optional[_builtins.str] = ..., enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannerText")
    def banner_text(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class EndpointClientRouteEnforcementOptions(dict):
    def __init__(__self__, *, enforced: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class EndpointConnectionLogOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, cloudwatch_log_group: Optional[_builtins.str] = ..., cloudwatch_log_stream: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogStream")
    def cloudwatch_log_stream(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetEndpointAuthenticationOptionResult(dict):
    def __init__(__self__, *, active_directory_id: _builtins.str, root_certificate_chain_arn: _builtins.str, saml_provider_arn: _builtins.str, self_service_saml_provider_arn: _builtins.str, type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootCertificateChainArn")
    def root_certificate_chain_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="samlProviderArn")
    def saml_provider_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfServiceSamlProviderArn")
    def self_service_saml_provider_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointClientConnectOptionResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, lambda_function_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetEndpointClientLoginBannerOptionResult(dict):
    def __init__(__self__, *, banner_text: _builtins.str, enabled: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannerText")
    def banner_text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetEndpointClientRouteEnforcementOptionResult(dict):
    def __init__(__self__, *, enforced: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetEndpointConnectionLogOptionResult(dict):
    def __init__(__self__, *, cloudwatch_log_group: _builtins.str, cloudwatch_log_stream: _builtins.str, enabled: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogStream")
    def cloudwatch_log_stream(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class GetEndpointFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


