

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ContactArgs', 'Contact']
@pulumi.input_type
class ContactArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], language_tag: pulumi.Input[_builtins.str], notification_category_subscriptions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], parent: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageTag")
    def language_tag(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @language_tag.setter
    def language_tag(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationCategorySubscriptions")
    def notification_category_subscriptions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @notification_category_subscriptions.setter
    def notification_category_subscriptions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _ContactState:
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., language_tag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_category_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageTag")
    def language_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_tag.setter
    def language_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationCategorySubscriptions")
    def notification_category_subscriptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @notification_category_subscriptions.setter
    def notification_category_subscriptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:essentialcontacts/contact:Contact")
class Contact(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., language_tag: Optional[pulumi.Input[_builtins.str]] = ..., notification_category_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContactArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., language_tag: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., notification_category_subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ...) -> Contact:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageTag")
    def language_tag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationCategorySubscriptions")
    def notification_category_subscriptions(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


