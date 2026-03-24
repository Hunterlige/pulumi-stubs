

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AttestationServiceCreationSpecificParamsArgs', 'AttestationServiceCreationSpecificParamsArgsDict', 'JsonWebKeySetArgs', 'JsonWebKeySetArgsDict', 'JsonWebKeyArgs', 'JsonWebKeyArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict']
class AttestationServiceCreationSpecificParamsArgsDict(TypedDict):
    
    policy_signing_certificates: NotRequired[pulumi.Input[JsonWebKeySetArgsDict]]
    public_network_access: NotRequired[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]]
    tpm_attestation_authentication: NotRequired[pulumi.Input[Union[_builtins.str, TpmAttestationAuthenticationType]]]


@pulumi.input_type
class AttestationServiceCreationSpecificParamsArgs:
    def __init__(__self__, *, policy_signing_certificates: Optional[pulumi.Input[JsonWebKeySetArgs]] = ..., public_network_access: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]] = ..., tpm_attestation_authentication: Optional[pulumi.Input[Union[_builtins.str, TpmAttestationAuthenticationType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policySigningCertificates")
    def policy_signing_certificates(self) -> Optional[pulumi.Input[JsonWebKeySetArgs]]:
        
        ...
    
    @policy_signing_certificates.setter
    def policy_signing_certificates(self, value: Optional[pulumi.Input[JsonWebKeySetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccessType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpmAttestationAuthentication")
    def tpm_attestation_authentication(self) -> Optional[pulumi.Input[Union[_builtins.str, TpmAttestationAuthenticationType]]]:
        
        ...
    
    @tpm_attestation_authentication.setter
    def tpm_attestation_authentication(self, value: Optional[pulumi.Input[Union[_builtins.str, TpmAttestationAuthenticationType]]]): # -> None:
        ...
    


class JsonWebKeySetArgsDict(TypedDict):
    keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[JsonWebKeyArgsDict]]]]


@pulumi.input_type
class JsonWebKeySetArgs:
    def __init__(__self__, *, keys: Optional[pulumi.Input[Sequence[pulumi.Input[JsonWebKeyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JsonWebKeyArgs]]]]:
        
        ...
    
    @keys.setter
    def keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JsonWebKeyArgs]]]]): # -> None:
        ...
    


class JsonWebKeyArgsDict(TypedDict):
    kty: pulumi.Input[_builtins.str]
    alg: NotRequired[pulumi.Input[_builtins.str]]
    crv: NotRequired[pulumi.Input[_builtins.str]]
    d: NotRequired[pulumi.Input[_builtins.str]]
    dp: NotRequired[pulumi.Input[_builtins.str]]
    dq: NotRequired[pulumi.Input[_builtins.str]]
    e: NotRequired[pulumi.Input[_builtins.str]]
    k: NotRequired[pulumi.Input[_builtins.str]]
    kid: NotRequired[pulumi.Input[_builtins.str]]
    n: NotRequired[pulumi.Input[_builtins.str]]
    p: NotRequired[pulumi.Input[_builtins.str]]
    q: NotRequired[pulumi.Input[_builtins.str]]
    qi: NotRequired[pulumi.Input[_builtins.str]]
    use: NotRequired[pulumi.Input[_builtins.str]]
    x: NotRequired[pulumi.Input[_builtins.str]]
    x5_c: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    y: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JsonWebKeyArgs:
    def __init__(__self__, *, kty: pulumi.Input[_builtins.str], alg: Optional[pulumi.Input[_builtins.str]] = ..., crv: Optional[pulumi.Input[_builtins.str]] = ..., d: Optional[pulumi.Input[_builtins.str]] = ..., dp: Optional[pulumi.Input[_builtins.str]] = ..., dq: Optional[pulumi.Input[_builtins.str]] = ..., e: Optional[pulumi.Input[_builtins.str]] = ..., k: Optional[pulumi.Input[_builtins.str]] = ..., kid: Optional[pulumi.Input[_builtins.str]] = ..., n: Optional[pulumi.Input[_builtins.str]] = ..., p: Optional[pulumi.Input[_builtins.str]] = ..., q: Optional[pulumi.Input[_builtins.str]] = ..., qi: Optional[pulumi.Input[_builtins.str]] = ..., use: Optional[pulumi.Input[_builtins.str]] = ..., x: Optional[pulumi.Input[_builtins.str]] = ..., x5_c: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., y: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kty(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kty.setter
    def kty(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def alg(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alg.setter
    def alg(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def crv(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crv.setter
    def crv(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def d(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @d.setter
    def d(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dp.setter
    def dp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dq(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dq.setter
    def dq(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def e(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @e.setter
    def e(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def k(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @k.setter
    def k(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kid.setter
    def kid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def n(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @n.setter
    def n(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def p(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @p.setter
    def p(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def q(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @q.setter
    def q(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def qi(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qi.setter
    def qi(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def use(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @use.setter
    def use(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def x(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @x.setter
    def x(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="x5C")
    def x5_c(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @x5_c.setter
    def x5_c(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def y(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @y.setter
    def y(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


