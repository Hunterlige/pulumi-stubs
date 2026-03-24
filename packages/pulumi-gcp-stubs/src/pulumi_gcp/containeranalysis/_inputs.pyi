import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "NoteAttestationAuthorityArgs",
    "NoteAttestationAuthorityArgsDict",
    "NoteAttestationAuthorityHintArgs",
    "NoteAttestationAuthorityHintArgsDict",
    "NoteIamBindingConditionArgs",
    "NoteIamBindingConditionArgsDict",
    "NoteIamMemberConditionArgs",
    "NoteIamMemberConditionArgsDict",
    "NoteRelatedUrlArgs",
    "NoteRelatedUrlArgsDict",
    "OccurenceAttestationArgs",
    "OccurenceAttestationArgsDict",
    "OccurenceAttestationSignatureArgs",
    "OccurenceAttestationSignatureArgsDict",
]

class NoteAttestationAuthorityArgsDict(TypedDict):
    hint: pulumi.Input[NoteAttestationAuthorityHintArgsDict]
    ...

@pulumi.input_type
class NoteAttestationAuthorityArgs:
    def __init__(
        __self__, *, hint: pulumi.Input[NoteAttestationAuthorityHintArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hint(self) -> pulumi.Input[NoteAttestationAuthorityHintArgs]: ...
    @hint.setter
    def hint(self, value: pulumi.Input[NoteAttestationAuthorityHintArgs]): ...

class NoteAttestationAuthorityHintArgsDict(TypedDict):
    human_readable_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class NoteAttestationAuthorityHintArgs:
    def __init__(
        __self__, *, human_readable_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="humanReadableName")
    def human_readable_name(self) -> pulumi.Input[_builtins.str]: ...
    @human_readable_name.setter
    def human_readable_name(self, value: pulumi.Input[_builtins.str]): ...

class NoteIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class NoteIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NoteIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class NoteIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NoteRelatedUrlArgsDict(TypedDict):
    url: pulumi.Input[_builtins.str]
    label: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class NoteRelatedUrlArgs:
    def __init__(
        __self__,
        *,
        url: pulumi.Input[_builtins.str],
        label: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OccurenceAttestationArgsDict(TypedDict):
    serialized_payload: pulumi.Input[_builtins.str]
    signatures: pulumi.Input[
        Sequence[pulumi.Input[OccurenceAttestationSignatureArgsDict]]
    ]
    ...

@pulumi.input_type
class OccurenceAttestationArgs:
    def __init__(
        __self__,
        *,
        serialized_payload: pulumi.Input[_builtins.str],
        signatures: pulumi.Input[
            Sequence[pulumi.Input[OccurenceAttestationSignatureArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serializedPayload")
    def serialized_payload(self) -> pulumi.Input[_builtins.str]: ...
    @serialized_payload.setter
    def serialized_payload(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def signatures(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[OccurenceAttestationSignatureArgs]]]: ...
    @signatures.setter
    def signatures(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[OccurenceAttestationSignatureArgs]]],
    ): ...

class OccurenceAttestationSignatureArgsDict(TypedDict):
    public_key_id: pulumi.Input[_builtins.str]
    signature: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class OccurenceAttestationSignatureArgs:
    def __init__(
        __self__,
        *,
        public_key_id: pulumi.Input[_builtins.str],
        signature: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeyId")
    def public_key_id(self) -> pulumi.Input[_builtins.str]: ...
    @public_key_id.setter
    def public_key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def signature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signature.setter
    def signature(self, value: Optional[pulumi.Input[_builtins.str]]): ...
