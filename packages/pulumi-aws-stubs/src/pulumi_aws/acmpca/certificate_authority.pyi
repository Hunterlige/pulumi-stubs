

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificateAuthorityArgs', 'CertificateAuthority']
@pulumi.input_type
class CertificateAuthorityArgs:
    def __init__(__self__, *, certificate_authority_configuration: pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationArgs], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_storage_security_standard: Optional[pulumi.Input[_builtins.str]] = ..., permanent_deletion_time_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revocation_configuration: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., usage_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityConfiguration")
    def certificate_authority_configuration(self) -> pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationArgs]:
        
        ...
    
    @certificate_authority_configuration.setter
    def certificate_authority_configuration(self, value: pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStorageSecurityStandard")
    def key_storage_security_standard(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_storage_security_standard.setter
    def key_storage_security_standard(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permanentDeletionTimeInDays")
    def permanent_deletion_time_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @permanent_deletion_time_in_days.setter
    def permanent_deletion_time_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revocationConfiguration")
    def revocation_configuration(self) -> Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationArgs]]:
        
        ...
    
    @revocation_configuration.setter
    def revocation_configuration(self, value: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageMode")
    def usage_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @usage_mode.setter
    def usage_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CertificateAuthorityState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authority_configuration: Optional[pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationArgs]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., certificate_signing_request: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_storage_security_standard: Optional[pulumi.Input[_builtins.str]] = ..., not_after: Optional[pulumi.Input[_builtins.str]] = ..., not_before: Optional[pulumi.Input[_builtins.str]] = ..., permanent_deletion_time_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revocation_configuration: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationArgs]] = ..., serial: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., usage_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityConfiguration")
    def certificate_authority_configuration(self) -> Optional[pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationArgs]]:
        
        ...
    
    @certificate_authority_configuration.setter
    def certificate_authority_configuration(self, value: Optional[pulumi.Input[CertificateAuthorityCertificateAuthorityConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSigningRequest")
    def certificate_signing_request(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_signing_request.setter
    def certificate_signing_request(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStorageSecurityStandard")
    def key_storage_security_standard(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_storage_security_standard.setter
    def key_storage_security_standard(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @not_after.setter
    def not_after(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @not_before.setter
    def not_before(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permanentDeletionTimeInDays")
    def permanent_deletion_time_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @permanent_deletion_time_in_days.setter
    def permanent_deletion_time_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revocationConfiguration")
    def revocation_configuration(self) -> Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationArgs]]:
        
        ...
    
    @revocation_configuration.setter
    def revocation_configuration(self, value: Optional[pulumi.Input[CertificateAuthorityRevocationConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serial.setter
    def serial(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageMode")
    def usage_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @usage_mode.setter
    def usage_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CertificateAuthority(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., certificate_authority_configuration: Optional[pulumi.Input[Union[CertificateAuthorityCertificateAuthorityConfigurationArgs, CertificateAuthorityCertificateAuthorityConfigurationArgsDict]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_storage_security_standard: Optional[pulumi.Input[_builtins.str]] = ..., permanent_deletion_time_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revocation_configuration: Optional[pulumi.Input[Union[CertificateAuthorityRevocationConfigurationArgs, CertificateAuthorityRevocationConfigurationArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., usage_mode: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CertificateAuthorityArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authority_configuration: Optional[pulumi.Input[Union[CertificateAuthorityCertificateAuthorityConfigurationArgs, CertificateAuthorityCertificateAuthorityConfigurationArgsDict]]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., certificate_signing_request: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., key_storage_security_standard: Optional[pulumi.Input[_builtins.str]] = ..., not_after: Optional[pulumi.Input[_builtins.str]] = ..., not_before: Optional[pulumi.Input[_builtins.str]] = ..., permanent_deletion_time_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., revocation_configuration: Optional[pulumi.Input[Union[CertificateAuthorityRevocationConfigurationArgs, CertificateAuthorityRevocationConfigurationArgsDict]]] = ..., serial: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., usage_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> CertificateAuthority:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityConfiguration")
    def certificate_authority_configuration(self) -> pulumi.Output[outputs.CertificateAuthorityCertificateAuthorityConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateSigningRequest")
    def certificate_signing_request(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStorageSecurityStandard")
    def key_storage_security_standard(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permanentDeletionTimeInDays")
    def permanent_deletion_time_in_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revocationConfiguration")
    def revocation_configuration(self) -> pulumi.Output[Optional[outputs.CertificateAuthorityRevocationConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def serial(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageMode")
    def usage_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


