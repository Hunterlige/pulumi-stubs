import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["KeystoresAliasesSelfSignedCertArgs", "KeystoresAliasesSelfSignedCert"]

@pulumi.input_type
class KeystoresAliasesSelfSignedCertArgs:
    def __init__(
        __self__,
        *,
        alias: pulumi.Input[_builtins.str],
        environment: pulumi.Input[_builtins.str],
        keystore: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        sig_alg: pulumi.Input[_builtins.str],
        subject: pulumi.Input[KeystoresAliasesSelfSignedCertSubjectArgs],
        cert_validity_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        key_size: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_alternative_dns_names: Optional[
            pulumi.Input[KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Input[_builtins.str]: ...
    @alias.setter
    def alias(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Input[_builtins.str]: ...
    @environment.setter
    def environment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> pulumi.Input[_builtins.str]: ...
    @keystore.setter
    def keystore(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sigAlg")
    def sig_alg(self) -> pulumi.Input[_builtins.str]: ...
    @sig_alg.setter
    def sig_alg(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[KeystoresAliasesSelfSignedCertSubjectArgs]: ...
    @subject.setter
    def subject(
        self, value: pulumi.Input[KeystoresAliasesSelfSignedCertSubjectArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="certValidityInDays")
    def cert_validity_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cert_validity_in_days.setter
    def cert_validity_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="keySize")
    def key_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_size.setter
    def key_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeDnsNames")
    def subject_alternative_dns_names(
        self,
    ) -> Optional[
        pulumi.Input[KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs]
    ]: ...
    @subject_alternative_dns_names.setter
    def subject_alternative_dns_names(
        self,
        value: Optional[
            pulumi.Input[KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs]
        ],
    ): ...

@pulumi.input_type
class _KeystoresAliasesSelfSignedCertState:
    def __init__(
        __self__,
        *,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        cert_validity_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        certs_infos: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KeystoresAliasesSelfSignedCertCertsInfoArgs]]
            ]
        ] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        key_size: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sig_alg: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[
            pulumi.Input[KeystoresAliasesSelfSignedCertSubjectArgs]
        ] = ...,
        subject_alternative_dns_names: Optional[
            pulumi.Input[KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certValidityInDays")
    def cert_validity_in_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cert_validity_in_days.setter
    def cert_validity_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="certsInfos")
    def certs_infos(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[KeystoresAliasesSelfSignedCertCertsInfoArgs]]
        ]
    ]: ...
    @certs_infos.setter
    def certs_infos(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[KeystoresAliasesSelfSignedCertCertsInfoArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keySize")
    def key_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_size.setter
    def key_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keystore.setter
    def keystore(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sigAlg")
    def sig_alg(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sig_alg.setter
    def sig_alg(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subject(
        self,
    ) -> Optional[pulumi.Input[KeystoresAliasesSelfSignedCertSubjectArgs]]: ...
    @subject.setter
    def subject(
        self, value: Optional[pulumi.Input[KeystoresAliasesSelfSignedCertSubjectArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeDnsNames")
    def subject_alternative_dns_names(
        self,
    ) -> Optional[
        pulumi.Input[KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs]
    ]: ...
    @subject_alternative_dns_names.setter
    def subject_alternative_dns_names(
        self,
        value: Optional[
            pulumi.Input[KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class KeystoresAliasesSelfSignedCert(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        cert_validity_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        key_size: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sig_alg: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[
            pulumi.Input[
                Union[
                    KeystoresAliasesSelfSignedCertSubjectArgs,
                    KeystoresAliasesSelfSignedCertSubjectArgsDict,
                ]
            ]
        ] = ...,
        subject_alternative_dns_names: Optional[
            pulumi.Input[
                Union[
                    KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs,
                    KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: KeystoresAliasesSelfSignedCertArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        cert_validity_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        certs_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            KeystoresAliasesSelfSignedCertCertsInfoArgs,
                            KeystoresAliasesSelfSignedCertCertsInfoArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        key_size: Optional[pulumi.Input[_builtins.str]] = ...,
        keystore: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sig_alg: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[
            pulumi.Input[
                Union[
                    KeystoresAliasesSelfSignedCertSubjectArgs,
                    KeystoresAliasesSelfSignedCertSubjectArgsDict,
                ]
            ]
        ] = ...,
        subject_alternative_dns_names: Optional[
            pulumi.Input[
                Union[
                    KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgs,
                    KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNamesArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> KeystoresAliasesSelfSignedCert: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certValidityInDays")
    def cert_validity_in_days(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="certsInfos")
    def certs_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.KeystoresAliasesSelfSignedCertCertsInfo]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keySize")
    def key_size(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def keystore(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sigAlg")
    def sig_alg(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subject(
        self,
    ) -> pulumi.Output[outputs.KeystoresAliasesSelfSignedCertSubject]: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeDnsNames")
    def subject_alternative_dns_names(
        self,
    ) -> pulumi.Output[
        Optional[outputs.KeystoresAliasesSelfSignedCertSubjectAlternativeDnsNames]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
