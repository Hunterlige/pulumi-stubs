import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "SigningJobDestinationArgs",
    "SigningJobDestinationArgsDict",
    "SigningJobDestinationS3Args",
    "SigningJobDestinationS3ArgsDict",
    "SigningJobRevocationRecordArgs",
    "SigningJobRevocationRecordArgsDict",
    "SigningJobSignedObjectArgs",
    "SigningJobSignedObjectArgsDict",
    "SigningJobSignedObjectS3Args",
    "SigningJobSignedObjectS3ArgsDict",
    "SigningJobSourceArgs",
    "SigningJobSourceArgsDict",
    "SigningJobSourceS3Args",
    "SigningJobSourceS3ArgsDict",
    "SigningProfileRevocationRecordArgs",
    "SigningProfileRevocationRecordArgsDict",
    "SigningProfileSignatureValidityPeriodArgs",
    "SigningProfileSignatureValidityPeriodArgsDict",
    "SigningProfileSigningMaterialArgs",
    "SigningProfileSigningMaterialArgsDict",
]

class SigningJobDestinationArgsDict(TypedDict):
    s3: pulumi.Input[SigningJobDestinationS3ArgsDict]

@pulumi.input_type
class SigningJobDestinationArgs:
    def __init__(
        __self__, *, s3: pulumi.Input[SigningJobDestinationS3Args]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> pulumi.Input[SigningJobDestinationS3Args]: ...
    @s3.setter
    def s3(self, value: pulumi.Input[SigningJobDestinationS3Args]): ...

class SigningJobDestinationS3ArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SigningJobDestinationS3Args:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SigningJobRevocationRecordArgsDict(TypedDict):
    reason: NotRequired[pulumi.Input[_builtins.str]]
    revoked_at: NotRequired[pulumi.Input[_builtins.str]]
    revoked_by: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SigningJobRevocationRecordArgs:
    def __init__(
        __self__,
        *,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        revoked_at: Optional[pulumi.Input[_builtins.str]] = ...,
        revoked_by: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revokedAt")
    def revoked_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revoked_at.setter
    def revoked_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revokedBy")
    def revoked_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revoked_by.setter
    def revoked_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SigningJobSignedObjectArgsDict(TypedDict):
    s3s: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SigningJobSignedObjectS3ArgsDict]]]
    ]

@pulumi.input_type
class SigningJobSignedObjectArgs:
    def __init__(
        __self__,
        *,
        s3s: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningJobSignedObjectS3Args]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3s(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SigningJobSignedObjectS3Args]]]
    ]: ...
    @s3s.setter
    def s3s(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningJobSignedObjectS3Args]]]
        ],
    ): ...

class SigningJobSignedObjectS3ArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SigningJobSignedObjectS3Args:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SigningJobSourceArgsDict(TypedDict):
    s3: pulumi.Input[SigningJobSourceS3ArgsDict]

@pulumi.input_type
class SigningJobSourceArgs:
    def __init__(__self__, *, s3: pulumi.Input[SigningJobSourceS3Args]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> pulumi.Input[SigningJobSourceS3Args]: ...
    @s3.setter
    def s3(self, value: pulumi.Input[SigningJobSourceS3Args]): ...

class SigningJobSourceS3ArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]

@pulumi.input_type
class SigningJobSourceS3Args:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...

class SigningProfileRevocationRecordArgsDict(TypedDict):
    revocation_effective_from: NotRequired[pulumi.Input[_builtins.str]]
    revoked_at: NotRequired[pulumi.Input[_builtins.str]]
    revoked_by: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SigningProfileRevocationRecordArgs:
    def __init__(
        __self__,
        *,
        revocation_effective_from: Optional[pulumi.Input[_builtins.str]] = ...,
        revoked_at: Optional[pulumi.Input[_builtins.str]] = ...,
        revoked_by: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revocationEffectiveFrom")
    def revocation_effective_from(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revocation_effective_from.setter
    def revocation_effective_from(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="revokedAt")
    def revoked_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revoked_at.setter
    def revoked_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revokedBy")
    def revoked_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revoked_by.setter
    def revoked_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SigningProfileSignatureValidityPeriodArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class SigningProfileSignatureValidityPeriodArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class SigningProfileSigningMaterialArgsDict(TypedDict):
    certificate_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class SigningProfileSigningMaterialArgs:
    def __init__(__self__, *, certificate_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: pulumi.Input[_builtins.str]): ...
