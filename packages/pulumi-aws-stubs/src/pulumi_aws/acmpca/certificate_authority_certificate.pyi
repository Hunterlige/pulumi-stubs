

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificateAuthorityCertificateArgs', 'CertificateAuthorityCertificate']
@pulumi.input_type
class CertificateAuthorityCertificateArgs:
    def __init__(__self__, *, certificate: pulumi.Input[_builtins.str], certificate_authority_arn: pulumi.Input[_builtins.str], certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CertificateAuthorityCertificateState:
    def __init__(__self__, *, certificate: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CertificateAuthorityCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CertificateAuthorityCertificateArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., certificate: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_chain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> CertificateAuthorityCertificate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


