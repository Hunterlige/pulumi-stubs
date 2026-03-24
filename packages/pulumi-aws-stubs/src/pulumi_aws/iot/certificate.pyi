import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CertificateArgs", "Certificate"]

@pulumi.input_type
class CertificateArgs:
    def __init__(
        __self__,
        *,
        active: pulumi.Input[_builtins.bool],
        ca_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        csr: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> pulumi.Input[_builtins.bool]: ...
    @active.setter
    def active(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="caPem")
    def ca_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_pem.setter
    def ca_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificatePem")
    def certificate_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_pem.setter
    def certificate_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def csr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csr.setter
    def csr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CertificateState:
    def __init__(
        __self__,
        *,
        active: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        csr: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @active.setter
    def active(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificateId")
    def ca_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate_id.setter
    def ca_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caPem")
    def ca_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_pem.setter
    def ca_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificatePem")
    def certificate_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_pem.setter
    def certificate_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def csr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @csr.setter
    def csr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:iot/certificate:Certificate")
class Certificate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        active: Optional[pulumi.Input[_builtins.bool]] = ...,
        ca_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        csr: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
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
        active: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        csr: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Certificate: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateId")
    def ca_certificate_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caPem")
    def ca_pem(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificatePem")
    def certificate_pem(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def csr(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
