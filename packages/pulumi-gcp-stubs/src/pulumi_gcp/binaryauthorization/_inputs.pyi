import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AttestorAttestationAuthorityNoteArgs",
    "AttestorAttestationAuthorityNoteArgsDict",
    "AttestorAttestationAuthorityNotePublicKeyArgs",
    "AttestorAttestationAuthorityNotePublicKeyArgsDict",
    ...,
    ...,
    "AttestorIamBindingConditionArgs",
    "AttestorIamBindingConditionArgsDict",
    "AttestorIamMemberConditionArgs",
    "AttestorIamMemberConditionArgsDict",
    "PolicyAdmissionWhitelistPatternArgs",
    "PolicyAdmissionWhitelistPatternArgsDict",
    "PolicyClusterAdmissionRuleArgs",
    "PolicyClusterAdmissionRuleArgsDict",
    "PolicyDefaultAdmissionRuleArgs",
    "PolicyDefaultAdmissionRuleArgsDict",
]

class AttestorAttestationAuthorityNoteArgsDict(TypedDict):
    note_reference: pulumi.Input[_builtins.str]
    delegation_service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    public_keys: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AttestorAttestationAuthorityNotePublicKeyArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class AttestorAttestationAuthorityNoteArgs:
    def __init__(
        __self__,
        *,
        note_reference: pulumi.Input[_builtins.str],
        delegation_service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        public_keys: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AttestorAttestationAuthorityNotePublicKeyArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noteReference")
    def note_reference(self) -> pulumi.Input[_builtins.str]: ...
    @note_reference.setter
    def note_reference(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="delegationServiceAccountEmail")
    def delegation_service_account_email(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delegation_service_account_email.setter
    def delegation_service_account_email(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AttestorAttestationAuthorityNotePublicKeyArgs]]
        ]
    ]: ...
    @public_keys.setter
    def public_keys(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AttestorAttestationAuthorityNotePublicKeyArgs]]
            ]
        ],
    ): ...

class AttestorAttestationAuthorityNotePublicKeyArgsDict(TypedDict):
    ascii_armored_pgp_public_key: NotRequired[pulumi.Input[_builtins.str]]
    comment: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    pkix_public_key: NotRequired[
        pulumi.Input[AttestorAttestationAuthorityNotePublicKeyPkixPublicKeyArgsDict]
    ]
    ...

@pulumi.input_type
class AttestorAttestationAuthorityNotePublicKeyArgs:
    def __init__(
        __self__,
        *,
        ascii_armored_pgp_public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        comment: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        pkix_public_key: Optional[
            pulumi.Input[AttestorAttestationAuthorityNotePublicKeyPkixPublicKeyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asciiArmoredPgpPublicKey")
    def ascii_armored_pgp_public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ascii_armored_pgp_public_key.setter
    def ascii_armored_pgp_public_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pkixPublicKey")
    def pkix_public_key(
        self,
    ) -> Optional[
        pulumi.Input[AttestorAttestationAuthorityNotePublicKeyPkixPublicKeyArgs]
    ]: ...
    @pkix_public_key.setter
    def pkix_public_key(
        self,
        value: Optional[
            pulumi.Input[AttestorAttestationAuthorityNotePublicKeyPkixPublicKeyArgs]
        ],
    ): ...

class AttestorAttestationAuthorityNotePublicKeyPkixPublicKeyArgsDict(TypedDict):
    public_key_pem: NotRequired[pulumi.Input[_builtins.str]]
    signature_algorithm: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AttestorAttestationAuthorityNotePublicKeyPkixPublicKeyArgs:
    def __init__(
        __self__,
        *,
        public_key_pem: Optional[pulumi.Input[_builtins.str]] = ...,
        signature_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicKeyPem")
    def public_key_pem(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @public_key_pem.setter
    def public_key_pem(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signature_algorithm.setter
    def signature_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AttestorIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AttestorIamBindingConditionArgs:
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

class AttestorIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AttestorIamMemberConditionArgs:
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

class PolicyAdmissionWhitelistPatternArgsDict(TypedDict):
    name_pattern: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PolicyAdmissionWhitelistPatternArgs:
    def __init__(__self__, *, name_pattern: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namePattern")
    def name_pattern(self) -> pulumi.Input[_builtins.str]: ...
    @name_pattern.setter
    def name_pattern(self, value: pulumi.Input[_builtins.str]): ...

class PolicyClusterAdmissionRuleArgsDict(TypedDict):
    cluster: pulumi.Input[_builtins.str]
    enforcement_mode: pulumi.Input[_builtins.str]
    evaluation_mode: pulumi.Input[_builtins.str]
    require_attestations_bies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class PolicyClusterAdmissionRuleArgs:
    def __init__(
        __self__,
        *,
        cluster: pulumi.Input[_builtins.str],
        enforcement_mode: pulumi.Input[_builtins.str],
        evaluation_mode: pulumi.Input[_builtins.str],
        require_attestations_bies: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> pulumi.Input[_builtins.str]: ...
    @enforcement_mode.setter
    def enforcement_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> pulumi.Input[_builtins.str]: ...
    @evaluation_mode.setter
    def evaluation_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="requireAttestationsBies")
    def require_attestations_bies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @require_attestations_bies.setter
    def require_attestations_bies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PolicyDefaultAdmissionRuleArgsDict(TypedDict):
    enforcement_mode: pulumi.Input[_builtins.str]
    evaluation_mode: pulumi.Input[_builtins.str]
    require_attestations_bies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class PolicyDefaultAdmissionRuleArgs:
    def __init__(
        __self__,
        *,
        enforcement_mode: pulumi.Input[_builtins.str],
        evaluation_mode: pulumi.Input[_builtins.str],
        require_attestations_bies: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> pulumi.Input[_builtins.str]: ...
    @enforcement_mode.setter
    def enforcement_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> pulumi.Input[_builtins.str]: ...
    @evaluation_mode.setter
    def evaluation_mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="requireAttestationsBies")
    def require_attestations_bies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @require_attestations_bies.setter
    def require_attestations_bies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
