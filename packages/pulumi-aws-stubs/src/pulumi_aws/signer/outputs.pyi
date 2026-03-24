import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "SigningJobDestination",
    "SigningJobDestinationS3",
    "SigningJobRevocationRecord",
    "SigningJobSignedObject",
    "SigningJobSignedObjectS3",
    "SigningJobSource",
    "SigningJobSourceS3",
    "SigningProfileRevocationRecord",
    "SigningProfileSignatureValidityPeriod",
    "SigningProfileSigningMaterial",
    "GetSigningJobRevocationRecordResult",
    "GetSigningJobSignedObjectResult",
    "GetSigningJobSignedObjectS3Result",
    "GetSigningJobSourceResult",
    "GetSigningJobSourceS3Result",
    "GetSigningProfileRevocationRecordResult",
    "GetSigningProfileSignatureValidityPeriodResult",
    "GetSigningProfileSigningMaterialResult",
]

@pulumi.output_type
class SigningJobDestination(dict):
    def __init__(__self__, *, s3: outputs.SigningJobDestinationS3) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> outputs.SigningJobDestinationS3: ...

@pulumi.output_type
class SigningJobDestinationS3(dict):
    def __init__(
        __self__, *, bucket: _builtins.str, prefix: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SigningJobRevocationRecord(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        reason: Optional[_builtins.str] = ...,
        revoked_at: Optional[_builtins.str] = ...,
        revoked_by: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revokedAt")
    def revoked_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revokedBy")
    def revoked_by(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SigningJobSignedObject(dict):
    def __init__(
        __self__, *, s3s: Optional[Sequence[outputs.SigningJobSignedObjectS3]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3s(self) -> Optional[Sequence[outputs.SigningJobSignedObjectS3]]: ...

@pulumi.output_type
class SigningJobSignedObjectS3(dict):
    def __init__(
        __self__,
        *,
        bucket: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SigningJobSource(dict):
    def __init__(__self__, *, s3: outputs.SigningJobSourceS3) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> outputs.SigningJobSourceS3: ...

@pulumi.output_type
class SigningJobSourceS3(dict):
    def __init__(
        __self__, *, bucket: _builtins.str, key: _builtins.str, version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class SigningProfileRevocationRecord(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        revocation_effective_from: Optional[_builtins.str] = ...,
        revoked_at: Optional[_builtins.str] = ...,
        revoked_by: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revocationEffectiveFrom")
    def revocation_effective_from(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revokedAt")
    def revoked_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revokedBy")
    def revoked_by(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SigningProfileSignatureValidityPeriod(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class SigningProfileSigningMaterial(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetSigningJobRevocationRecordResult(dict):
    def __init__(
        __self__,
        *,
        reason: _builtins.str,
        revoked_at: _builtins.str,
        revoked_by: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="revokedAt")
    def revoked_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="revokedBy")
    def revoked_by(self) -> _builtins.str: ...

@pulumi.output_type
class GetSigningJobSignedObjectResult(dict):
    def __init__(
        __self__, *, s3s: Sequence[outputs.GetSigningJobSignedObjectS3Result]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3s(self) -> Sequence[outputs.GetSigningJobSignedObjectS3Result]: ...

@pulumi.output_type
class GetSigningJobSignedObjectS3Result(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class GetSigningJobSourceResult(dict):
    def __init__(
        __self__, *, s3s: Sequence[outputs.GetSigningJobSourceS3Result]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3s(self) -> Sequence[outputs.GetSigningJobSourceS3Result]: ...

@pulumi.output_type
class GetSigningJobSourceS3Result(dict):
    def __init__(
        __self__, *, bucket: _builtins.str, key: _builtins.str, version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetSigningProfileRevocationRecordResult(dict):
    def __init__(
        __self__,
        *,
        revocation_effective_from: _builtins.str,
        revoked_at: _builtins.str,
        revoked_by: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revocationEffectiveFrom")
    def revocation_effective_from(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="revokedAt")
    def revoked_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="revokedBy")
    def revoked_by(self) -> _builtins.str: ...

@pulumi.output_type
class GetSigningProfileSignatureValidityPeriodResult(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetSigningProfileSigningMaterialResult(dict):
    def __init__(__self__, *, certificate_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...
