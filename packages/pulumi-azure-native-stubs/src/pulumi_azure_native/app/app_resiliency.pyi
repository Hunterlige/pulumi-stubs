import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppResiliencyArgs", "AppResiliency"]

@pulumi.input_type
class AppResiliencyArgs:
    def __init__(
        __self__,
        *,
        app_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        circuit_breaker_policy: Optional[pulumi.Input[CircuitBreakerPolicyArgs]] = ...,
        http_connection_pool: Optional[pulumi.Input[HttpConnectionPoolArgs]] = ...,
        http_retry_policy: Optional[pulumi.Input[HttpRetryPolicyArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        tcp_connection_pool: Optional[pulumi.Input[TcpConnectionPoolArgs]] = ...,
        tcp_retry_policy: Optional[pulumi.Input[TcpRetryPolicyArgs]] = ...,
        timeout_policy: Optional[pulumi.Input[TimeoutPolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Input[_builtins.str]: ...
    @app_name.setter
    def app_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakerPolicy")
    def circuit_breaker_policy(
        self,
    ) -> Optional[pulumi.Input[CircuitBreakerPolicyArgs]]: ...
    @circuit_breaker_policy.setter
    def circuit_breaker_policy(
        self, value: Optional[pulumi.Input[CircuitBreakerPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpConnectionPool")
    def http_connection_pool(
        self,
    ) -> Optional[pulumi.Input[HttpConnectionPoolArgs]]: ...
    @http_connection_pool.setter
    def http_connection_pool(
        self, value: Optional[pulumi.Input[HttpConnectionPoolArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpRetryPolicy")
    def http_retry_policy(self) -> Optional[pulumi.Input[HttpRetryPolicyArgs]]: ...
    @http_retry_policy.setter
    def http_retry_policy(self, value: Optional[pulumi.Input[HttpRetryPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpConnectionPool")
    def tcp_connection_pool(self) -> Optional[pulumi.Input[TcpConnectionPoolArgs]]: ...
    @tcp_connection_pool.setter
    def tcp_connection_pool(
        self, value: Optional[pulumi.Input[TcpConnectionPoolArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryPolicy")
    def tcp_retry_policy(self) -> Optional[pulumi.Input[TcpRetryPolicyArgs]]: ...
    @tcp_retry_policy.setter
    def tcp_retry_policy(self, value: Optional[pulumi.Input[TcpRetryPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutPolicy")
    def timeout_policy(self) -> Optional[pulumi.Input[TimeoutPolicyArgs]]: ...
    @timeout_policy.setter
    def timeout_policy(self, value: Optional[pulumi.Input[TimeoutPolicyArgs]]): ...

@pulumi.type_token("azure-native:app:AppResiliency")
class AppResiliency(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_name: Optional[pulumi.Input[_builtins.str]] = ...,
        circuit_breaker_policy: Optional[
            pulumi.Input[Union[CircuitBreakerPolicyArgs, CircuitBreakerPolicyArgsDict]]
        ] = ...,
        http_connection_pool: Optional[
            pulumi.Input[Union[HttpConnectionPoolArgs, HttpConnectionPoolArgsDict]]
        ] = ...,
        http_retry_policy: Optional[
            pulumi.Input[Union[HttpRetryPolicyArgs, HttpRetryPolicyArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tcp_connection_pool: Optional[
            pulumi.Input[Union[TcpConnectionPoolArgs, TcpConnectionPoolArgsDict]]
        ] = ...,
        tcp_retry_policy: Optional[
            pulumi.Input[Union[TcpRetryPolicyArgs, TcpRetryPolicyArgsDict]]
        ] = ...,
        timeout_policy: Optional[
            pulumi.Input[Union[TimeoutPolicyArgs, TimeoutPolicyArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppResiliencyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AppResiliency: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakerPolicy")
    def circuit_breaker_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.CircuitBreakerPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="httpConnectionPool")
    def http_connection_pool(
        self,
    ) -> pulumi.Output[Optional[outputs.HttpConnectionPoolResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="httpRetryPolicy")
    def http_retry_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.HttpRetryPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="tcpConnectionPool")
    def tcp_connection_pool(
        self,
    ) -> pulumi.Output[Optional[outputs.TcpConnectionPoolResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryPolicy")
    def tcp_retry_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.TcpRetryPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutPolicy")
    def timeout_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.TimeoutPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
