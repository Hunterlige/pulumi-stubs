

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BrandArgs', 'Brand']
@pulumi.input_type
class BrandArgs:
    def __init__(__self__, *, application_title: pulumi.Input[_builtins.str], support_email: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationTitle")
    def application_title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_title.setter
    def application_title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @support_email.setter
    def support_email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BrandState:
    def __init__(__self__, *, application_title: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_internal_only: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., support_email: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationTitle")
    def application_title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_title.setter
    def application_title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgInternalOnly")
    def org_internal_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @org_internal_only.setter
    def org_internal_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @support_email.setter
    def support_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:iap/brand:Brand")
class Brand(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_title: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., support_email: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BrandArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_title: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_internal_only: Optional[pulumi.Input[_builtins.bool]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., support_email: Optional[pulumi.Input[_builtins.str]] = ...) -> Brand:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationTitle")
    def application_title(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgInternalOnly")
    def org_internal_only(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


