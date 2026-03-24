import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "NoteAttestationAuthority",
    "NoteAttestationAuthorityHint",
    "NoteIamBindingCondition",
    "NoteIamMemberCondition",
    "NoteRelatedUrl",
    "OccurenceAttestation",
    "OccurenceAttestationSignature",
]

@pulumi.output_type
class NoteAttestationAuthority(dict):
    def __init__(__self__, *, hint: outputs.NoteAttestationAuthorityHint) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hint(self) -> outputs.NoteAttestationAuthorityHint: ...

@pulumi.output_type
class NoteAttestationAuthorityHint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, human_readable_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="humanReadableName")
    def human_readable_name(self) -> _builtins.str: ...

@pulumi.output_type
class NoteIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NoteIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NoteRelatedUrl(dict):
    def __init__(
        __self__, *, url: _builtins.str, label: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OccurenceAttestation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        serialized_payload: _builtins.str,
        signatures: Sequence[outputs.OccurenceAttestationSignature],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serializedPayload")
    def serialized_payload(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def signatures(self) -> Sequence[outputs.OccurenceAttestationSignature]: ...

@pulumi.output_type
class OccurenceAttestationSignature(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        public_key_id: _builtins.str,
        signature: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeyId")
    def public_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def signature(self) -> Optional[_builtins.str]: ...
