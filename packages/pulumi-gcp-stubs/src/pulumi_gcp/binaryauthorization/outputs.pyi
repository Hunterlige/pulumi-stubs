

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AttestorAttestationAuthorityNote', 'AttestorAttestationAuthorityNotePublicKey', ..., 'AttestorIamBindingCondition', 'AttestorIamMemberCondition', 'PolicyAdmissionWhitelistPattern', 'PolicyClusterAdmissionRule', 'PolicyDefaultAdmissionRule']
@pulumi.output_type
class AttestorAttestationAuthorityNote(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, note_reference: _builtins.str, delegation_service_account_email: Optional[_builtins.str] = ..., public_keys: Optional[Sequence[outputs.AttestorAttestationAuthorityNotePublicKey]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noteReference")
    def note_reference(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegationServiceAccountEmail")
    def delegation_service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Optional[Sequence[outputs.AttestorAttestationAuthorityNotePublicKey]]:
        
        ...
    


@pulumi.output_type
class AttestorAttestationAuthorityNotePublicKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ascii_armored_pgp_public_key: Optional[_builtins.str] = ..., comment: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., pkix_public_key: Optional[outputs.AttestorAttestationAuthorityNotePublicKeyPkixPublicKey] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asciiArmoredPgpPublicKey")
    def ascii_armored_pgp_public_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pkixPublicKey")
    def pkix_public_key(self) -> Optional[outputs.AttestorAttestationAuthorityNotePublicKeyPkixPublicKey]:
        
        ...
    


@pulumi.output_type
class AttestorAttestationAuthorityNotePublicKeyPkixPublicKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, public_key_pem: Optional[_builtins.str] = ..., signature_algorithm: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeyPem")
    def public_key_pem(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AttestorIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class AttestorIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class PolicyAdmissionWhitelistPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name_pattern: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePattern")
    def name_pattern(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyClusterAdmissionRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster: _builtins.str, enforcement_mode: _builtins.str, evaluation_mode: _builtins.str, require_attestations_bies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireAttestationsBies")
    def require_attestations_bies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicyDefaultAdmissionRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enforcement_mode: _builtins.str, evaluation_mode: _builtins.str, require_attestations_bies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMode")
    def evaluation_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireAttestationsBies")
    def require_attestations_bies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


