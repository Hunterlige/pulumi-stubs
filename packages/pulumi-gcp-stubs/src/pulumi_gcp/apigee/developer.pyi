

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
__all__ = ['DeveloperArgs', 'Developer']
@pulumi.input_type
class DeveloperArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], first_name: pulumi.Input[_builtins.str], last_name: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], user_name: pulumi.Input[_builtins.str], attributes: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAttributeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAttributeArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _DeveloperState:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAttributeArgs]]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_at: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., organizatio_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DeveloperAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizatioName")
    def organizatio_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizatio_name.setter
    def organizatio_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/developer:Developer")
class Developer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeveloperAttributeArgs, DeveloperAttributeArgsDict]]]]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DeveloperArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeveloperAttributeArgs, DeveloperAttributeArgsDict]]]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_at: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., organizatio_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> Developer:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Sequence[outputs.DeveloperAttribute]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizatioName")
    def organizatio_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


