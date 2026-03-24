

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AADBasedSecurityPrincipalArgs', 'AADBasedSecurityPrincipalArgsDict', 'CertBasedSecurityPrincipalArgs', 'CertBasedSecurityPrincipalArgsDict', 'CertificateTagsArgs', 'CertificateTagsArgsDict', 'DeploymentTypeArgs', 'DeploymentTypeArgsDict', 'LedgerPropertiesArgs', 'LedgerPropertiesArgsDict', 'ManagedCCFPropertiesArgs', 'ManagedCCFPropertiesArgsDict', 'MemberIdentityCertificateArgs', 'MemberIdentityCertificateArgsDict']
class AADBasedSecurityPrincipalArgsDict(TypedDict):
    
    ledger_role_name: NotRequired[pulumi.Input[Union[_builtins.str, LedgerRoleName]]]
    principal_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AADBasedSecurityPrincipalArgs:
    def __init__(__self__, *, ledger_role_name: Optional[pulumi.Input[Union[_builtins.str, LedgerRoleName]]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> Optional[pulumi.Input[Union[_builtins.str, LedgerRoleName]]]:
        
        ...
    
    @ledger_role_name.setter
    def ledger_role_name(self, value: Optional[pulumi.Input[Union[_builtins.str, LedgerRoleName]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertBasedSecurityPrincipalArgsDict(TypedDict):
    
    cert: NotRequired[pulumi.Input[_builtins.str]]
    ledger_role_name: NotRequired[pulumi.Input[Union[_builtins.str, LedgerRoleName]]]


@pulumi.input_type
class CertBasedSecurityPrincipalArgs:
    def __init__(__self__, *, cert: Optional[pulumi.Input[_builtins.str]] = ..., ledger_role_name: Optional[pulumi.Input[Union[_builtins.str, LedgerRoleName]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> Optional[pulumi.Input[Union[_builtins.str, LedgerRoleName]]]:
        
        ...
    
    @ledger_role_name.setter
    def ledger_role_name(self, value: Optional[pulumi.Input[Union[_builtins.str, LedgerRoleName]]]): # -> None:
        ...
    


class CertificateTagsArgsDict(TypedDict):
    
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CertificateTagsArgs:
    def __init__(__self__, *, tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DeploymentTypeArgsDict(TypedDict):
    
    app_source_uri: NotRequired[pulumi.Input[_builtins.str]]
    language_runtime: NotRequired[pulumi.Input[Union[_builtins.str, LanguageRuntime]]]


@pulumi.input_type
class DeploymentTypeArgs:
    def __init__(__self__, *, app_source_uri: Optional[pulumi.Input[_builtins.str]] = ..., language_runtime: Optional[pulumi.Input[Union[_builtins.str, LanguageRuntime]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSourceUri")
    def app_source_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_source_uri.setter
    def app_source_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageRuntime")
    def language_runtime(self) -> Optional[pulumi.Input[Union[_builtins.str, LanguageRuntime]]]:
        
        ...
    
    @language_runtime.setter
    def language_runtime(self, value: Optional[pulumi.Input[Union[_builtins.str, LanguageRuntime]]]): # -> None:
        ...
    


class LedgerPropertiesArgsDict(TypedDict):
    
    aad_based_security_principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[AADBasedSecurityPrincipalArgsDict]]]]
    cert_based_security_principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[CertBasedSecurityPrincipalArgsDict]]]]
    ledger_sku: NotRequired[pulumi.Input[Union[_builtins.str, LedgerSku]]]
    ledger_type: NotRequired[pulumi.Input[Union[_builtins.str, LedgerType]]]
    running_state: NotRequired[pulumi.Input[Union[_builtins.str, RunningState]]]


@pulumi.input_type
class LedgerPropertiesArgs:
    def __init__(__self__, *, aad_based_security_principals: Optional[pulumi.Input[Sequence[pulumi.Input[AADBasedSecurityPrincipalArgs]]]] = ..., cert_based_security_principals: Optional[pulumi.Input[Sequence[pulumi.Input[CertBasedSecurityPrincipalArgs]]]] = ..., ledger_sku: Optional[pulumi.Input[Union[_builtins.str, LedgerSku]]] = ..., ledger_type: Optional[pulumi.Input[Union[_builtins.str, LedgerType]]] = ..., running_state: Optional[pulumi.Input[Union[_builtins.str, RunningState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadBasedSecurityPrincipals")
    def aad_based_security_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AADBasedSecurityPrincipalArgs]]]]:
        
        ...
    
    @aad_based_security_principals.setter
    def aad_based_security_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AADBasedSecurityPrincipalArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certBasedSecurityPrincipals")
    def cert_based_security_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertBasedSecurityPrincipalArgs]]]]:
        
        ...
    
    @cert_based_security_principals.setter
    def cert_based_security_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertBasedSecurityPrincipalArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ledgerSku")
    def ledger_sku(self) -> Optional[pulumi.Input[Union[_builtins.str, LedgerSku]]]:
        
        ...
    
    @ledger_sku.setter
    def ledger_sku(self, value: Optional[pulumi.Input[Union[_builtins.str, LedgerSku]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ledgerType")
    def ledger_type(self) -> Optional[pulumi.Input[Union[_builtins.str, LedgerType]]]:
        
        ...
    
    @ledger_type.setter
    def ledger_type(self, value: Optional[pulumi.Input[Union[_builtins.str, LedgerType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runningState")
    def running_state(self) -> Optional[pulumi.Input[Union[_builtins.str, RunningState]]]:
        
        ...
    
    @running_state.setter
    def running_state(self, value: Optional[pulumi.Input[Union[_builtins.str, RunningState]]]): # -> None:
        ...
    


class ManagedCCFPropertiesArgsDict(TypedDict):
    
    deployment_type: NotRequired[pulumi.Input[DeploymentTypeArgsDict]]
    member_identity_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[MemberIdentityCertificateArgsDict]]]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    running_state: NotRequired[pulumi.Input[Union[_builtins.str, RunningState]]]


@pulumi.input_type
class ManagedCCFPropertiesArgs:
    def __init__(__self__, *, deployment_type: Optional[pulumi.Input[DeploymentTypeArgs]] = ..., member_identity_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[MemberIdentityCertificateArgs]]]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., running_state: Optional[pulumi.Input[Union[_builtins.str, RunningState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[DeploymentTypeArgs]]:
        
        ...
    
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[DeploymentTypeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberIdentityCertificates")
    def member_identity_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MemberIdentityCertificateArgs]]]]:
        
        ...
    
    @member_identity_certificates.setter
    def member_identity_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MemberIdentityCertificateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runningState")
    def running_state(self) -> Optional[pulumi.Input[Union[_builtins.str, RunningState]]]:
        
        ...
    
    @running_state.setter
    def running_state(self, value: Optional[pulumi.Input[Union[_builtins.str, RunningState]]]): # -> None:
        ...
    


class MemberIdentityCertificateArgsDict(TypedDict):
    
    certificate: NotRequired[pulumi.Input[_builtins.str]]
    encryptionkey: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[CertificateTagsArgsDict]]]]


@pulumi.input_type
class MemberIdentityCertificateArgs:
    def __init__(__self__, *, certificate: Optional[pulumi.Input[_builtins.str]] = ..., encryptionkey: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateTagsArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryptionkey(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryptionkey.setter
    def encryptionkey(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateTagsArgs]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateTagsArgs]]]]): # -> None:
        ...
    


