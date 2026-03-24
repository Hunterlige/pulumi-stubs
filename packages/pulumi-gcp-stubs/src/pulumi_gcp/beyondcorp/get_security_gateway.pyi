import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityGatewayResult",
    "AwaitableGetSecurityGatewayResult",
    "get_security_gateway",
    "get_security_gateway_output",
]

@pulumi.output_type
class GetSecurityGatewayResult:
    def __init__(
        __self__,
        create_time=...,
        delegating_service_account=...,
        display_name=...,
        external_ips=...,
        hubs=...,
        id=...,
        location=...,
        loggings=...,
        name=...,
        project=...,
        proxy_protocol_configs=...,
        security_gateway_id=...,
        service_discoveries=...,
        state=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="delegatingServiceAccount")
    def delegating_service_account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalIps")
    def external_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hubs(self) -> Sequence[outputs.GetSecurityGatewayHubResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def loggings(self) -> Sequence[outputs.GetSecurityGatewayLoggingResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proxyProtocolConfigs")
    def proxy_protocol_configs(
        self,
    ) -> Sequence[outputs.GetSecurityGatewayProxyProtocolConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceDiscoveries")
    def service_discoveries(
        self,
    ) -> Sequence[outputs.GetSecurityGatewayServiceDiscoveryResult]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetSecurityGatewayResult(GetSecurityGatewayResult):
    def __await__(self): ...

def get_security_gateway(
    project: Optional[_builtins.str] = ...,
    security_gateway_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityGatewayResult: ...
def get_security_gateway_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityGatewayResult]: ...
