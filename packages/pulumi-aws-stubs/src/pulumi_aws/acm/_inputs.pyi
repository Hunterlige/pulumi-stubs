

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificateDomainValidationOptionArgs', 'CertificateDomainValidationOptionArgsDict', 'CertificateOptionsArgs', 'CertificateOptionsArgsDict', 'CertificateRenewalSummaryArgs', 'CertificateRenewalSummaryArgsDict', 'CertificateValidationOptionArgs', 'CertificateValidationOptionArgsDict']
class CertificateDomainValidationOptionArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_type: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateDomainValidationOptionArgs:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_record_name.setter
    def resource_record_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_record_type.setter
    def resource_record_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_record_value.setter
    def resource_record_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertificateOptionsArgsDict(TypedDict):
    certificate_transparency_logging_preference: NotRequired[pulumi.Input[_builtins.str]]
    export: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateOptionsArgs:
    def __init__(__self__, *, certificate_transparency_logging_preference: Optional[pulumi.Input[_builtins.str]] = ..., export: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_transparency_logging_preference.setter
    def certificate_transparency_logging_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @export.setter
    def export(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertificateRenewalSummaryArgsDict(TypedDict):
    renewal_status: NotRequired[pulumi.Input[_builtins.str]]
    renewal_status_reason: NotRequired[pulumi.Input[_builtins.str]]
    updated_at: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateRenewalSummaryArgs:
    def __init__(__self__, *, renewal_status: Optional[pulumi.Input[_builtins.str]] = ..., renewal_status_reason: Optional[pulumi.Input[_builtins.str]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalStatus")
    def renewal_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @renewal_status.setter
    def renewal_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalStatusReason")
    def renewal_status_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @renewal_status_reason.setter
    def renewal_status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertificateValidationOptionArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    validation_domain: pulumi.Input[_builtins.str]


@pulumi.input_type
class CertificateValidationOptionArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], validation_domain: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationDomain")
    def validation_domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @validation_domain.setter
    def validation_domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


