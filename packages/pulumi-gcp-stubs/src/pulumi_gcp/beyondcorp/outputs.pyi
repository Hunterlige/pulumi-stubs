

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppConnectionApplicationEndpoint', 'AppConnectionGateway', 'AppConnectorPrincipalInfo', 'AppConnectorPrincipalInfoServiceAccount', 'AppGatewayAllocatedConnection', 'SecurityGatewayApplicationEndpointMatcher', 'SecurityGatewayApplicationIamBindingCondition', 'SecurityGatewayApplicationIamMemberCondition', 'SecurityGatewayApplicationUpstream', 'SecurityGatewayApplicationUpstreamEgressPolicy', 'SecurityGatewayApplicationUpstreamExternal', 'SecurityGatewayApplicationUpstreamExternalEndpoint', 'SecurityGatewayApplicationUpstreamNetwork', 'SecurityGatewayApplicationUpstreamProxyProtocol', ..., ..., ..., ..., 'SecurityGatewayHub', 'SecurityGatewayHubInternetGateway', 'SecurityGatewayIamBindingCondition', 'SecurityGatewayIamMemberCondition', 'SecurityGatewayLogging', 'SecurityGatewayProxyProtocolConfig', ..., ..., ..., ..., 'SecurityGatewayServiceDiscovery', 'SecurityGatewayServiceDiscoveryApiGateway', ..., 'GetAppConnectionApplicationEndpointResult', 'GetAppConnectionGatewayResult', 'GetAppConnectorPrincipalInfoResult', 'GetAppConnectorPrincipalInfoServiceAccountResult', 'GetAppGatewayAllocatedConnectionResult', 'GetSecurityGatewayHubResult', 'GetSecurityGatewayHubInternetGatewayResult', 'GetSecurityGatewayLoggingResult', 'GetSecurityGatewayProxyProtocolConfigResult', ..., ..., ..., ..., 'GetSecurityGatewayServiceDiscoveryResult', 'GetSecurityGatewayServiceDiscoveryApiGatewayResult', ...]
@pulumi.output_type
class AppConnectionApplicationEndpoint(dict):
    def __init__(__self__, *, host: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AppConnectionGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_gateway: _builtins.str, ingress_port: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appGateway")
    def app_gateway(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppConnectorPrincipalInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: outputs.AppConnectorPrincipalInfoServiceAccount) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> outputs.AppConnectorPrincipalInfoServiceAccount:
        
        ...
    


@pulumi.output_type
class AppConnectorPrincipalInfoServiceAccount(dict):
    def __init__(__self__, *, email: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AppGatewayAllocatedConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ingress_port: Optional[_builtins.int] = ..., psc_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscUri")
    def psc_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationEndpointMatcher(dict):
    def __init__(__self__, *, hostname: _builtins.str, ports: Sequence[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationIamBindingCondition(dict):
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
class SecurityGatewayApplicationIamMemberCondition(dict):
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
class SecurityGatewayApplicationUpstream(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, egress_policy: Optional[outputs.SecurityGatewayApplicationUpstreamEgressPolicy] = ..., external: Optional[outputs.SecurityGatewayApplicationUpstreamExternal] = ..., network: Optional[outputs.SecurityGatewayApplicationUpstreamNetwork] = ..., proxy_protocol: Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocol] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="egressPolicy")
    def egress_policy(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamEgressPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def external(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamExternal]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamNetwork]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyProtocol")
    def proxy_protocol(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocol]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamEgressPolicy(dict):
    def __init__(__self__, *, regions: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamExternal(dict):
    def __init__(__self__, *, endpoints: Sequence[outputs.SecurityGatewayApplicationUpstreamExternalEndpoint]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.SecurityGatewayApplicationUpstreamExternalEndpoint]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamExternalEndpoint(dict):
    def __init__(__self__, *, hostname: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamNetwork(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamProxyProtocol(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_client_headers: Optional[Sequence[_builtins.str]] = ..., client_ip: Optional[_builtins.bool] = ..., contextual_headers: Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeaders] = ..., gateway_identity: Optional[_builtins.str] = ..., metadata_headers: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClientHeaders")
    def allowed_client_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIp")
    def client_ip(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextualHeaders")
    def contextual_headers(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeaders]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIdentity")
    def gateway_identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataHeaders")
    def metadata_headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeaders(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_info: Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfo] = ..., group_info: Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfo] = ..., output_type: Optional[_builtins.str] = ..., user_info: Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfo] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceInfo")
    def device_info(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupInfo")
    def group_info(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfo")
    def user_info(self) -> Optional[outputs.SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfo]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersDeviceInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersGroupInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayApplicationUpstreamProxyProtocolContextualHeadersUserInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayHub(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, region: _builtins.str, internet_gateway: Optional[outputs.SecurityGatewayHubInternetGateway] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateway")
    def internet_gateway(self) -> Optional[outputs.SecurityGatewayHubInternetGateway]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayHubInternetGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assigned_ips: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedIps")
    def assigned_ips(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayIamBindingCondition(dict):
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
class SecurityGatewayIamMemberCondition(dict):
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
class SecurityGatewayLogging(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class SecurityGatewayProxyProtocolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_client_headers: Optional[Sequence[_builtins.str]] = ..., client_ip: Optional[_builtins.bool] = ..., contextual_headers: Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeaders] = ..., gateway_identity: Optional[_builtins.str] = ..., metadata_headers: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClientHeaders")
    def allowed_client_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIp")
    def client_ip(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextualHeaders")
    def contextual_headers(self) -> Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeaders]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIdentity")
    def gateway_identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataHeaders")
    def metadata_headers(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayProxyProtocolConfigContextualHeaders(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, device_info: Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfo] = ..., group_info: Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfo] = ..., output_type: Optional[_builtins.str] = ..., user_info: Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeadersUserInfo] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceInfo")
    def device_info(self) -> Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupInfo")
    def group_info(self) -> Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfo")
    def user_info(self) -> Optional[outputs.SecurityGatewayProxyProtocolConfigContextualHeadersUserInfo]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayProxyProtocolConfigContextualHeadersDeviceInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayProxyProtocolConfigContextualHeadersGroupInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayProxyProtocolConfigContextualHeadersUserInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayServiceDiscovery(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_gateway: Optional[outputs.SecurityGatewayServiceDiscoveryApiGateway] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiGateway")
    def api_gateway(self) -> Optional[outputs.SecurityGatewayServiceDiscoveryApiGateway]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayServiceDiscoveryApiGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_override: Optional[outputs.SecurityGatewayServiceDiscoveryApiGatewayResourceOverride] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOverride")
    def resource_override(self) -> Optional[outputs.SecurityGatewayServiceDiscoveryApiGatewayResourceOverride]:
        
        ...
    


@pulumi.output_type
class SecurityGatewayServiceDiscoveryApiGatewayResourceOverride(dict):
    def __init__(__self__, *, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetAppConnectionApplicationEndpointResult(dict):
    def __init__(__self__, *, host: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetAppConnectionGatewayResult(dict):
    def __init__(__self__, *, app_gateway: _builtins.str, ingress_port: _builtins.int, type: _builtins.str, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appGateway")
    def app_gateway(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetAppConnectorPrincipalInfoResult(dict):
    def __init__(__self__, *, service_accounts: Sequence[outputs.GetAppConnectorPrincipalInfoServiceAccountResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(self) -> Sequence[outputs.GetAppConnectorPrincipalInfoServiceAccountResult]:
        
        ...
    


@pulumi.output_type
class GetAppConnectorPrincipalInfoServiceAccountResult(dict):
    def __init__(__self__, *, email: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetAppGatewayAllocatedConnectionResult(dict):
    def __init__(__self__, *, ingress_port: _builtins.int, psc_uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingressPort")
    def ingress_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscUri")
    def psc_uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayHubResult(dict):
    def __init__(__self__, *, internet_gateways: Sequence[outputs.GetSecurityGatewayHubInternetGatewayResult], region: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internetGateways")
    def internet_gateways(self) -> Sequence[outputs.GetSecurityGatewayHubInternetGatewayResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetSecurityGatewayHubInternetGatewayResult(dict):
    def __init__(__self__, *, assigned_ips: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedIps")
    def assigned_ips(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayLoggingResult(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class GetSecurityGatewayProxyProtocolConfigResult(dict):
    def __init__(__self__, *, allowed_client_headers: Sequence[_builtins.str], client_ip: _builtins.bool, contextual_headers: Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderResult], gateway_identity: _builtins.str, metadata_headers: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClientHeaders")
    def allowed_client_headers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientIp")
    def client_ip(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextualHeaders")
    def contextual_headers(self) -> Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIdentity")
    def gateway_identity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataHeaders")
    def metadata_headers(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayProxyProtocolConfigContextualHeaderResult(dict):
    def __init__(__self__, *, device_infos: Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderDeviceInfoResult], group_infos: Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderGroupInfoResult], output_type: _builtins.str, user_infos: Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderUserInfoResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceInfos")
    def device_infos(self) -> Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderDeviceInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupInfos")
    def group_infos(self) -> Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderGroupInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInfos")
    def user_infos(self) -> Sequence[outputs.GetSecurityGatewayProxyProtocolConfigContextualHeaderUserInfoResult]:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayProxyProtocolConfigContextualHeaderDeviceInfoResult(dict):
    def __init__(__self__, *, output_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayProxyProtocolConfigContextualHeaderGroupInfoResult(dict):
    def __init__(__self__, *, output_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayProxyProtocolConfigContextualHeaderUserInfoResult(dict):
    def __init__(__self__, *, output_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayServiceDiscoveryResult(dict):
    def __init__(__self__, *, api_gateways: Sequence[outputs.GetSecurityGatewayServiceDiscoveryApiGatewayResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiGateways")
    def api_gateways(self) -> Sequence[outputs.GetSecurityGatewayServiceDiscoveryApiGatewayResult]:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayServiceDiscoveryApiGatewayResult(dict):
    def __init__(__self__, *, resource_overrides: Sequence[outputs.GetSecurityGatewayServiceDiscoveryApiGatewayResourceOverrideResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceOverrides")
    def resource_overrides(self) -> Sequence[outputs.GetSecurityGatewayServiceDiscoveryApiGatewayResourceOverrideResult]:
        
        ...
    


@pulumi.output_type
class GetSecurityGatewayServiceDiscoveryApiGatewayResourceOverrideResult(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


