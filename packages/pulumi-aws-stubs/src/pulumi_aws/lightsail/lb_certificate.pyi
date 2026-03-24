import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LbCertificateArgs", "LbCertificate"]

@pulumi.input_type
class LbCertificateArgs:
    def __init__(
        __self__,
        *,
        lb_name: pulumi.Input[_builtins.str],
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_alternative_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lbName")
    def lb_name(self) -> pulumi.Input[_builtins.str]: ...
    @lb_name.setter
    def lb_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subject_alternative_names.setter
    def subject_alternative_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _LbCertificateState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_validation_records: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LbCertificateDomainValidationRecordArgs]]
            ]
        ] = ...,
        lb_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_alternative_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        support_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainValidationRecords")
    def domain_validation_records(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LbCertificateDomainValidationRecordArgs]]]
    ]: ...
    @domain_validation_records.setter
    def domain_validation_records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LbCertificateDomainValidationRecordArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lbName")
    def lb_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lb_name.setter
    def lb_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subject_alternative_names.setter
    def subject_alternative_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @support_code.setter
    def support_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:lightsail/lbCertificate:LbCertificate")
class LbCertificate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_alternative_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LbCertificateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_validation_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            LbCertificateDomainValidationRecordArgs,
                            LbCertificateDomainValidationRecordArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        lb_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        subject_alternative_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        support_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LbCertificate: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainValidationRecords")
    def domain_validation_records(
        self,
    ) -> pulumi.Output[Sequence[outputs.LbCertificateDomainValidationRecord]]: ...
    @_builtins.property
    @pulumi.getter(name="lbName")
    def lb_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> pulumi.Output[_builtins.str]: ...
