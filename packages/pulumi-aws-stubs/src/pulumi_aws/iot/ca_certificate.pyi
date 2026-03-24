import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CaCertificateArgs", "CaCertificate"]

@pulumi.input_type
class CaCertificateArgs:
    def __init__(
        __self__,
        *,
        active: pulumi.Input[_builtins.bool],
        allow_auto_registration: pulumi.Input[_builtins.bool],
        ca_certificate_pem: pulumi.Input[_builtins.str],
        certificate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_config: Optional[
            pulumi.Input[CaCertificateRegistrationConfigArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        verification_certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> pulumi.Input[_builtins.bool]: ...
    @active.setter
    def active(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="allowAutoRegistration")
    def allow_auto_registration(self) -> pulumi.Input[_builtins.bool]: ...
    @allow_auto_registration.setter
    def allow_auto_registration(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> pulumi.Input[_builtins.str]: ...
    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationConfig")
    def registration_config(
        self,
    ) -> Optional[pulumi.Input[CaCertificateRegistrationConfigArgs]]: ...
    @registration_config.setter
    def registration_config(
        self, value: Optional[pulumi.Input[CaCertificateRegistrationConfigArgs]]
    ): ...
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
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verification_certificate_pem.setter
    def verification_certificate_pem(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _CaCertificateState:
    def __init__(
        __self__,
        *,
        active: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_auto_registration: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_version: Optional[pulumi.Input[_builtins.int]] = ...,
        generation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_config: Optional[
            pulumi.Input[CaCertificateRegistrationConfigArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        validities: Optional[
            pulumi.Input[Sequence[pulumi.Input[CaCertificateValidityArgs]]]
        ] = ...,
        verification_certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @active.setter
    def active(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowAutoRegistration")
    def allow_auto_registration(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_auto_registration.setter
    def allow_auto_registration(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerVersion")
    def customer_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @customer_version.setter
    def customer_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="generationId")
    def generation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation_id.setter
    def generation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registrationConfig")
    def registration_config(
        self,
    ) -> Optional[pulumi.Input[CaCertificateRegistrationConfigArgs]]: ...
    @registration_config.setter
    def registration_config(
        self, value: Optional[pulumi.Input[CaCertificateRegistrationConfigArgs]]
    ): ...
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
    @pulumi.getter
    def validities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CaCertificateValidityArgs]]]]: ...
    @validities.setter
    def validities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CaCertificateValidityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verification_certificate_pem.setter
    def verification_certificate_pem(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("aws:iot/caCertificate:CaCertificate")
class CaCertificate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        active: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_auto_registration: Optional[pulumi.Input[_builtins.bool]] = ...,
        ca_certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_config: Optional[
            pulumi.Input[
                Union[
                    CaCertificateRegistrationConfigArgs,
                    CaCertificateRegistrationConfigArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        verification_certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CaCertificateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        active: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_auto_registration: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_version: Optional[pulumi.Input[_builtins.int]] = ...,
        generation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registration_config: Optional[
            pulumi.Input[
                Union[
                    CaCertificateRegistrationConfigArgs,
                    CaCertificateRegistrationConfigArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        validities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CaCertificateValidityArgs, CaCertificateValidityArgsDict]
                    ]
                ]
            ]
        ] = ...,
        verification_certificate_pem: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CaCertificate: ...
    @_builtins.property
    @pulumi.getter
    def active(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowAutoRegistration")
    def allow_auto_registration(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatePem")
    def ca_certificate_pem(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customerVersion")
    def customer_version(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="generationId")
    def generation_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationConfig")
    def registration_config(
        self,
    ) -> pulumi.Output[Optional[outputs.CaCertificateRegistrationConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def validities(self) -> pulumi.Output[Sequence[outputs.CaCertificateValidity]]: ...
    @_builtins.property
    @pulumi.getter(name="verificationCertificatePem")
    def verification_certificate_pem(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
