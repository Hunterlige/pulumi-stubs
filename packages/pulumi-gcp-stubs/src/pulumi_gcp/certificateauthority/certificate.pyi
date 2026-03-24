import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
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
        location: pulumi.Input[_builtins.str],
        pool: pulumi.Input[_builtins.str],
        certificate_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_template: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[pulumi.Input[CertificateConfigArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_csr: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Input[_builtins.str]: ...
    @pool.setter
    def pool(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_authority.setter
    def certificate_authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateTemplate")
    def certificate_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_template.setter
    def certificate_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[CertificateConfigArgs]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[CertificateConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifetime.setter
    def lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pemCsr")
    def pem_csr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_csr.setter
    def pem_csr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CertificateState:
    def __init__(
        __self__,
        *,
        certificate_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_descriptions: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateCertificateDescriptionArgs]]]
        ] = ...,
        certificate_template: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[pulumi.Input[CertificateConfigArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        issuer_certificate_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_certificate_chains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        pem_csr: Optional[pulumi.Input[_builtins.str]] = ...,
        pool: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        revocation_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateRevocationDetailArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_authority.setter
    def certificate_authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateDescriptions")
    def certificate_descriptions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CertificateCertificateDescriptionArgs]]]
    ]: ...
    @certificate_descriptions.setter
    def certificate_descriptions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateCertificateDescriptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateTemplate")
    def certificate_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_template.setter
    def certificate_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[CertificateConfigArgs]]: ...
    @config.setter
    def config(self, value: Optional[pulumi.Input[CertificateConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="issuerCertificateAuthority")
    def issuer_certificate_authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer_certificate_authority.setter
    def issuer_certificate_authority(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifetime.setter
    def lifetime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_certificate.setter
    def pem_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pemCertificateChains")
    def pem_certificate_chains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @pem_certificate_chains.setter
    def pem_certificate_chains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pemCsr")
    def pem_csr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pem_csr.setter
    def pem_csr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pool.setter
    def pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="revocationDetails")
    def revocation_details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CertificateRevocationDetailArgs]]]
    ]: ...
    @revocation_details.setter
    def revocation_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateRevocationDetailArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:certificateauthority/certificate:Certificate")
class Certificate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_template: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[
            pulumi.Input[Union[CertificateConfigArgs, CertificateConfigArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_csr: Optional[pulumi.Input[_builtins.str]] = ...,
        pool: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
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
        certificate_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_descriptions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CertificateCertificateDescriptionArgs,
                            CertificateCertificateDescriptionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        certificate_template: Optional[pulumi.Input[_builtins.str]] = ...,
        config: Optional[
            pulumi.Input[Union[CertificateConfigArgs, CertificateConfigArgsDict]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        issuer_certificate_authority: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        lifetime: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        pem_certificate_chains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        pem_csr: Optional[pulumi.Input[_builtins.str]] = ...,
        pool: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        revocation_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CertificateRevocationDetailArgs,
                            CertificateRevocationDetailArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Certificate: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateDescriptions")
    def certificate_descriptions(
        self,
    ) -> pulumi.Output[Sequence[outputs.CertificateCertificateDescription]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateTemplate")
    def certificate_template(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[outputs.CertificateConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="issuerCertificateAuthority")
    def issuer_certificate_authority(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def lifetime(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificate")
    def pem_certificate(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pemCertificateChains")
    def pem_certificate_chains(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pemCsr")
    def pem_csr(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="revocationDetails")
    def revocation_details(
        self,
    ) -> pulumi.Output[Sequence[outputs.CertificateRevocationDetail]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
