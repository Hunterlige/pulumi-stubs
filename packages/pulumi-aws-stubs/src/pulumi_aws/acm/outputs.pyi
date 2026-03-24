

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificateDomainValidationOption', 'CertificateOptions', 'CertificateRenewalSummary', 'CertificateValidationOption']
@pulumi.output_type
class CertificateDomainValidationOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., resource_record_name: Optional[_builtins.str] = ..., resource_record_type: Optional[_builtins.str] = ..., resource_record_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_transparency_logging_preference: Optional[_builtins.str] = ..., export: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateRenewalSummary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, renewal_status: Optional[_builtins.str] = ..., renewal_status_reason: Optional[_builtins.str] = ..., updated_at: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalStatus")
    def renewal_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalStatusReason")
    def renewal_status_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class CertificateValidationOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: _builtins.str, validation_domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationDomain")
    def validation_domain(self) -> _builtins.str:
        
        ...
    


