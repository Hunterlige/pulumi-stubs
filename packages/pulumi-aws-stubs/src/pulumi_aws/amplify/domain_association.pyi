import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainAssociationArgs", "DomainAssociation"]

@pulumi.input_type
class DomainAssociationArgs:
    def __init__(
        __self__,
        *,
        app_id: pulumi.Input[_builtins.str],
        domain_name: pulumi.Input[_builtins.str],
        sub_domains: pulumi.Input[
            Sequence[pulumi.Input[DomainAssociationSubDomainArgs]]
        ],
        certificate_settings: Optional[
            pulumi.Input[DomainAssociationCertificateSettingsArgs]
        ] = ...,
        enable_auto_sub_domain: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]: ...
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subDomains")
    def sub_domains(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[DomainAssociationSubDomainArgs]]]: ...
    @sub_domains.setter
    def sub_domains(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[DomainAssociationSubDomainArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateSettings")
    def certificate_settings(
        self,
    ) -> Optional[pulumi.Input[DomainAssociationCertificateSettingsArgs]]: ...
    @certificate_settings.setter
    def certificate_settings(
        self, value: Optional[pulumi.Input[DomainAssociationCertificateSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAutoSubDomain")
    def enable_auto_sub_domain(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_auto_sub_domain.setter
    def enable_auto_sub_domain(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="waitForVerification")
    def wait_for_verification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_verification.setter
    def wait_for_verification(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _DomainAssociationState:
    def __init__(
        __self__,
        *,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_settings: Optional[
            pulumi.Input[DomainAssociationCertificateSettingsArgs]
        ] = ...,
        certificate_verification_dns_record: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_auto_sub_domain: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainAssociationSubDomainArgs]]]
        ] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateSettings")
    def certificate_settings(
        self,
    ) -> Optional[pulumi.Input[DomainAssociationCertificateSettingsArgs]]: ...
    @certificate_settings.setter
    def certificate_settings(
        self, value: Optional[pulumi.Input[DomainAssociationCertificateSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certificateVerificationDnsRecord")
    def certificate_verification_dns_record(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_verification_dns_record.setter
    def certificate_verification_dns_record(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAutoSubDomain")
    def enable_auto_sub_domain(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_auto_sub_domain.setter
    def enable_auto_sub_domain(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subDomains")
    def sub_domains(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DomainAssociationSubDomainArgs]]]
    ]: ...
    @sub_domains.setter
    def sub_domains(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainAssociationSubDomainArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForVerification")
    def wait_for_verification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_verification.setter
    def wait_for_verification(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("aws:amplify/domainAssociation:DomainAssociation")
class DomainAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_settings: Optional[
            pulumi.Input[
                Union[
                    DomainAssociationCertificateSettingsArgs,
                    DomainAssociationCertificateSettingsArgsDict,
                ]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_auto_sub_domain: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_domains: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DomainAssociationSubDomainArgs,
                            DomainAssociationSubDomainArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_settings: Optional[
            pulumi.Input[
                Union[
                    DomainAssociationCertificateSettingsArgs,
                    DomainAssociationCertificateSettingsArgsDict,
                ]
            ]
        ] = ...,
        certificate_verification_dns_record: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_auto_sub_domain: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_domains: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            DomainAssociationSubDomainArgs,
                            DomainAssociationSubDomainArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        wait_for_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> DomainAssociation: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateSettings")
    def certificate_settings(
        self,
    ) -> pulumi.Output[outputs.DomainAssociationCertificateSettings]: ...
    @_builtins.property
    @pulumi.getter(name="certificateVerificationDnsRecord")
    def certificate_verification_dns_record(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutoSubDomain")
    def enable_auto_sub_domain(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subDomains")
    def sub_domains(
        self,
    ) -> pulumi.Output[Sequence[outputs.DomainAssociationSubDomain]]: ...
    @_builtins.property
    @pulumi.getter(name="waitForVerification")
    def wait_for_verification(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
