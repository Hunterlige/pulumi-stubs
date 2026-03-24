import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainTrustArgs", "DomainTrust"]

@pulumi.input_type
class DomainTrustArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        target_dns_ip_addresses: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        target_domain_name: pulumi.Input[_builtins.str],
        trust_direction: pulumi.Input[_builtins.str],
        trust_handshake_secret: pulumi.Input[_builtins.str],
        trust_type: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        selective_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetDnsIpAddresses")
    def target_dns_ip_addresses(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @target_dns_ip_addresses.setter
    def target_dns_ip_addresses(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDomainName")
    def target_domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_domain_name.setter
    def target_domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> pulumi.Input[_builtins.str]: ...
    @trust_direction.setter
    def trust_direction(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trustHandshakeSecret")
    def trust_handshake_secret(self) -> pulumi.Input[_builtins.str]: ...
    @trust_handshake_secret.setter
    def trust_handshake_secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trustType")
    def trust_type(self) -> pulumi.Input[_builtins.str]: ...
    @trust_type.setter
    def trust_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selectiveAuthentication")
    def selective_authentication(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @selective_authentication.setter
    def selective_authentication(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _DomainTrustState:
    def __init__(
        __self__,
        *,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        selective_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        target_dns_ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_direction: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_handshake_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selectiveAuthentication")
    def selective_authentication(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @selective_authentication.setter
    def selective_authentication(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDnsIpAddresses")
    def target_dns_ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_dns_ip_addresses.setter
    def target_dns_ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDomainName")
    def target_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_domain_name.setter
    def target_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trust_direction.setter
    def trust_direction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustHandshakeSecret")
    def trust_handshake_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trust_handshake_secret.setter
    def trust_handshake_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustType")
    def trust_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trust_type.setter
    def trust_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:activedirectory/domainTrust:DomainTrust")
class DomainTrust(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        selective_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        target_dns_ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_direction: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_handshake_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainTrustArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        selective_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        target_dns_ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_direction: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_handshake_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DomainTrust: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selectiveAuthentication")
    def selective_authentication(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="targetDnsIpAddresses")
    def target_dns_ip_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetDomainName")
    def target_domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustDirection")
    def trust_direction(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustHandshakeSecret")
    def trust_handshake_secret(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustType")
    def trust_type(self) -> pulumi.Output[_builtins.str]: ...
