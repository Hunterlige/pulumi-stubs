import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CertificateArgs", "Certificate"]

@pulumi.input_type
class CertificateArgs:
    def __init__(
        __self__,
        *,
        certificate_authority_arn: pulumi.Input[_builtins.str],
        certificate_signing_request: pulumi.Input[_builtins.str],
        signing_algorithm: pulumi.Input[_builtins.str],
        validity: pulumi.Input[CertificateValidityArgs],
        api_passthrough: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        template_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateSigningRequest")
    def certificate_signing_request(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_signing_request.setter
    def certificate_signing_request(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> pulumi.Input[_builtins.str]: ...
    @signing_algorithm.setter
    def signing_algorithm(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def validity(self) -> pulumi.Input[CertificateValidityArgs]: ...
    @validity.setter
    def validity(self, value: pulumi.Input[CertificateValidityArgs]): ...
    @_builtins.property
    @pulumi.getter(name="apiPassthrough")
    def api_passthrough(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_passthrough.setter
    def api_passthrough(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateArn")
    def template_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_arn.setter
    def template_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CertificateState:
    def __init__(
        __self__,
        *,
        api_passthrough: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_chain: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_signing_request: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        template_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        validity: Optional[pulumi.Input[CertificateValidityArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiPassthrough")
    def api_passthrough(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_passthrough.setter
    def api_passthrough(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_authority_arn.setter
    def certificate_authority_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateSigningRequest")
    def certificate_signing_request(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_signing_request.setter
    def certificate_signing_request(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signing_algorithm.setter
    def signing_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="templateArn")
    def template_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @template_arn.setter
    def template_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def validity(self) -> Optional[pulumi.Input[CertificateValidityArgs]]: ...
    @validity.setter
    def validity(self, value: Optional[pulumi.Input[CertificateValidityArgs]]): ...

@pulumi.type_token("aws:acmpca/certificate:Certificate")
class Certificate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_passthrough: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_signing_request: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        template_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        validity: Optional[
            pulumi.Input[Union[CertificateValidityArgs, CertificateValidityArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CertificateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_passthrough: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_chain: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_signing_request: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        template_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        validity: Optional[
            pulumi.Input[Union[CertificateValidityArgs, CertificateValidityArgsDict]]
        ] = ...,
    ) -> Certificate: ...
    @_builtins.property
    @pulumi.getter(name="apiPassthrough")
    def api_passthrough(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateSigningRequest")
    def certificate_signing_request(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="templateArn")
    def template_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def validity(self) -> pulumi.Output[outputs.CertificateValidity]: ...
