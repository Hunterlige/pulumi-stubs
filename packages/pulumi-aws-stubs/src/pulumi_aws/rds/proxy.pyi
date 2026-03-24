import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProxyArgs", "Proxy"]

@pulumi.input_type
class ProxyArgs:
    def __init__(
        __self__,
        *,
        engine_family: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        vpc_subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        auths: Optional[pulumi.Input[Sequence[pulumi.Input[ProxyAuthArgs]]]] = ...,
        debug_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        default_auth_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_client_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_connection_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="engineFamily")
    def engine_family(self) -> pulumi.Input[_builtins.str]: ...
    @engine_family.setter
    def engine_family(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @vpc_subnet_ids.setter
    def vpc_subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def auths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProxyAuthArgs]]]]: ...
    @auths.setter
    def auths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProxyAuthArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="debugLogging")
    def debug_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @debug_logging.setter
    def debug_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultAuthScheme")
    def default_auth_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_auth_scheme.setter
    def default_auth_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointNetworkType")
    def endpoint_network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_network_type.setter
    def endpoint_network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleClientTimeout")
    def idle_client_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_client_timeout.setter
    def idle_client_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_tls.setter
    def require_tls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetConnectionNetworkType")
    def target_connection_network_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_connection_network_type.setter
    def target_connection_network_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ProxyState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auths: Optional[pulumi.Input[Sequence[pulumi.Input[ProxyAuthArgs]]]] = ...,
        debug_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        default_auth_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_family: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_client_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_connection_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def auths(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProxyAuthArgs]]]]: ...
    @auths.setter
    def auths(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProxyAuthArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="debugLogging")
    def debug_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @debug_logging.setter
    def debug_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultAuthScheme")
    def default_auth_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_auth_scheme.setter
    def default_auth_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointNetworkType")
    def endpoint_network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_network_type.setter
    def endpoint_network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineFamily")
    def engine_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_family.setter
    def engine_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleClientTimeout")
    def idle_client_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_client_timeout.setter
    def idle_client_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_tls.setter
    def require_tls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetConnectionNetworkType")
    def target_connection_network_type(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_connection_network_type.setter
    def target_connection_network_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_subnet_ids.setter
    def vpc_subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:rds/proxy:Proxy")
class Proxy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auths: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ProxyAuthArgs, ProxyAuthArgsDict]]]
            ]
        ] = ...,
        debug_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        default_auth_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_family: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_client_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_connection_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProxyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auths: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ProxyAuthArgs, ProxyAuthArgsDict]]]
            ]
        ] = ...,
        debug_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
        default_auth_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_family: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_client_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target_connection_network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Proxy: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def auths(self) -> pulumi.Output[Optional[Sequence[outputs.ProxyAuth]]]: ...
    @_builtins.property
    @pulumi.getter(name="debugLogging")
    def debug_logging(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultAuthScheme")
    def default_auth_scheme(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointNetworkType")
    def endpoint_network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineFamily")
    def engine_family(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="idleClientTimeout")
    def idle_client_timeout(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetConnectionNetworkType")
    def target_connection_network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSubnetIds")
    def vpc_subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
