import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SigningProfileArgs", "SigningProfile"]

@pulumi.input_type
class SigningProfileArgs:
    def __init__(
        __self__,
        *,
        platform_id: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        signature_validity_period: Optional[
            pulumi.Input[SigningProfileSignatureValidityPeriodArgs]
        ] = ...,
        signing_material: Optional[
            pulumi.Input[SigningProfileSigningMaterialArgs]
        ] = ...,
        signing_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> pulumi.Input[_builtins.str]: ...
    @platform_id.setter
    def platform_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signatureValidityPeriod")
    def signature_validity_period(
        self,
    ) -> Optional[pulumi.Input[SigningProfileSignatureValidityPeriodArgs]]: ...
    @signature_validity_period.setter
    def signature_validity_period(
        self, value: Optional[pulumi.Input[SigningProfileSignatureValidityPeriodArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signingMaterial")
    def signing_material(
        self,
    ) -> Optional[pulumi.Input[SigningProfileSigningMaterialArgs]]: ...
    @signing_material.setter
    def signing_material(
        self, value: Optional[pulumi.Input[SigningProfileSigningMaterialArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signingParameters")
    def signing_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @signing_parameters.setter
    def signing_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
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

@pulumi.input_type
class _SigningProfileState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revocation_records: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningProfileRevocationRecordArgs]]]
        ] = ...,
        signature_validity_period: Optional[
            pulumi.Input[SigningProfileSignatureValidityPeriodArgs]
        ] = ...,
        signing_material: Optional[
            pulumi.Input[SigningProfileSigningMaterialArgs]
        ] = ...,
        signing_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        version_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformDisplayName")
    def platform_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_display_name.setter
    def platform_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_id.setter
    def platform_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationRecords")
    def revocation_records(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SigningProfileRevocationRecordArgs]]]
    ]: ...
    @revocation_records.setter
    def revocation_records(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningProfileRevocationRecordArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="signatureValidityPeriod")
    def signature_validity_period(
        self,
    ) -> Optional[pulumi.Input[SigningProfileSignatureValidityPeriodArgs]]: ...
    @signature_validity_period.setter
    def signature_validity_period(
        self, value: Optional[pulumi.Input[SigningProfileSignatureValidityPeriodArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signingMaterial")
    def signing_material(
        self,
    ) -> Optional[pulumi.Input[SigningProfileSigningMaterialArgs]]: ...
    @signing_material.setter
    def signing_material(
        self, value: Optional[pulumi.Input[SigningProfileSigningMaterialArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signingParameters")
    def signing_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @signing_parameters.setter
    def signing_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionArn")
    def version_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_arn.setter
    def version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:signer/signingProfile:SigningProfile")
class SigningProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        signature_validity_period: Optional[
            pulumi.Input[
                Union[
                    SigningProfileSignatureValidityPeriodArgs,
                    SigningProfileSignatureValidityPeriodArgsDict,
                ]
            ]
        ] = ...,
        signing_material: Optional[
            pulumi.Input[
                Union[
                    SigningProfileSigningMaterialArgs,
                    SigningProfileSigningMaterialArgsDict,
                ]
            ]
        ] = ...,
        signing_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SigningProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revocation_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SigningProfileRevocationRecordArgs,
                            SigningProfileRevocationRecordArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        signature_validity_period: Optional[
            pulumi.Input[
                Union[
                    SigningProfileSignatureValidityPeriodArgs,
                    SigningProfileSignatureValidityPeriodArgsDict,
                ]
            ]
        ] = ...,
        signing_material: Optional[
            pulumi.Input[
                Union[
                    SigningProfileSigningMaterialArgs,
                    SigningProfileSigningMaterialArgsDict,
                ]
            ]
        ] = ...,
        signing_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        version_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SigningProfile: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformDisplayName")
    def platform_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revocationRecords")
    def revocation_records(
        self,
    ) -> pulumi.Output[Sequence[outputs.SigningProfileRevocationRecord]]: ...
    @_builtins.property
    @pulumi.getter(name="signatureValidityPeriod")
    def signature_validity_period(
        self,
    ) -> pulumi.Output[outputs.SigningProfileSignatureValidityPeriod]: ...
    @_builtins.property
    @pulumi.getter(name="signingMaterial")
    def signing_material(
        self,
    ) -> pulumi.Output[outputs.SigningProfileSigningMaterial]: ...
    @_builtins.property
    @pulumi.getter(name="signingParameters")
    def signing_parameters(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionArn")
    def version_arn(self) -> pulumi.Output[_builtins.str]: ...
