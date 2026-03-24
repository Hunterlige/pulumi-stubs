

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomDomainAssociationArgs', 'CustomDomainAssociation']
@pulumi.input_type
class CustomDomainAssociationArgs:
    def __init__(__self__, *, custom_domain_certificate_arn: pulumi.Input[_builtins.str], custom_domain_name: pulumi.Input[_builtins.str], workgroup_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainCertificateArn")
    def custom_domain_certificate_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @custom_domain_certificate_arn.setter
    def custom_domain_certificate_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @custom_domain_name.setter
    def custom_domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def __init__(__self__, *, custom_domain_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_certificate_expiry_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainCertificateArn")
    def custom_domain_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_domain_certificate_arn.setter
    def custom_domain_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainCertificateExpiryTime")
    def custom_domain_certificate_expiry_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_domain_certificate_expiry_time.setter
    def custom_domain_certificate_expiry_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CustomDomainAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_domain_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomDomainAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., custom_domain_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_certificate_expiry_time: Optional[pulumi.Input[_builtins.str]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> CustomDomainAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainCertificateArn")
    def custom_domain_certificate_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainCertificateExpiryTime")
    def custom_domain_certificate_expiry_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


