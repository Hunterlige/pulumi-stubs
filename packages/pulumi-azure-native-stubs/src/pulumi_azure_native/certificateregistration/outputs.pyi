

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppServiceCertificateResponse', 'CertificateDetailsResponse', 'CertificateOrderContactResponse']
@pulumi.output_type
class AppServiceCertificateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, key_vault_id: Optional[_builtins.str] = ..., key_vault_secret_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issuer: _builtins.str, not_after: _builtins.str, not_before: _builtins.str, raw_data: _builtins.str, serial_number: _builtins.str, signature_algorithm: _builtins.str, subject: _builtins.str, thumbprint: _builtins.str, version: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawData")
    def raw_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class CertificateOrderContactResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email: Optional[_builtins.str] = ..., name_first: Optional[_builtins.str] = ..., name_last: Optional[_builtins.str] = ..., phone: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameFirst")
    def name_first(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameLast")
    def name_last(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[_builtins.str]:
        ...
    


