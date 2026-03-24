

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomDomainAssociationArgs', 'CustomDomainAssociation']
@pulumi.input_type
class CustomDomainAssociationArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], service_arn: pulumi.Input[_builtins.str], enable_www_subdomain: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_arn.setter
    def service_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableWwwSubdomain")
    def enable_www_subdomain(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_www_subdomain.setter
    def enable_www_subdomain(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CustomDomainAssociationState:
    def __init__(__self__, *, certificate_validation_records: Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainAssociationCertificateValidationRecordArgs]]]] = ..., dns_target: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_www_subdomain: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateValidationRecords")
    def certificate_validation_records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainAssociationCertificateValidationRecordArgs]]]]:
        
        ...
    
    @certificate_validation_records.setter
    def certificate_validation_records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainAssociationCertificateValidationRecordArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsTarget")
    def dns_target(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_target.setter
    def dns_target(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableWwwSubdomain")
    def enable_www_subdomain(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_www_subdomain.setter
    def enable_www_subdomain(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_arn.setter
    def service_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CustomDomainAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_www_subdomain: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomDomainAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., certificate_validation_records: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CustomDomainAssociationCertificateValidationRecordArgs, CustomDomainAssociationCertificateValidationRecordArgsDict]]]]] = ..., dns_target: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_www_subdomain: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> CustomDomainAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateValidationRecords")
    def certificate_validation_records(self) -> pulumi.Output[Sequence[outputs.CustomDomainAssociationCertificateValidationRecord]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsTarget")
    def dns_target(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableWwwSubdomain")
    def enable_www_subdomain(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceArn")
    def service_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


