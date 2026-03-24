

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
__all__ = ['EmailIdentityArgs', 'EmailIdentity']
@pulumi.input_type
class EmailIdentityArgs:
    def __init__(__self__, *, email_identity: pulumi.Input[_builtins.str], configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., dkim_signing_attributes: Optional[pulumi.Input[EmailIdentityDkimSigningAttributesArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email_identity.setter
    def email_identity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_set_name.setter
    def configuration_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dkimSigningAttributes")
    def dkim_signing_attributes(self) -> Optional[pulumi.Input[EmailIdentityDkimSigningAttributesArgs]]:
        
        ...
    
    @dkim_signing_attributes.setter
    def dkim_signing_attributes(self, value: Optional[pulumi.Input[EmailIdentityDkimSigningAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _EmailIdentityState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., dkim_signing_attributes: Optional[pulumi.Input[EmailIdentityDkimSigningAttributesArgs]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., identity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., verification_status: Optional[pulumi.Input[_builtins.str]] = ..., verified_for_sending_status: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_set_name.setter
    def configuration_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dkimSigningAttributes")
    def dkim_signing_attributes(self) -> Optional[pulumi.Input[EmailIdentityDkimSigningAttributesArgs]]:
        
        ...
    
    @dkim_signing_attributes.setter
    def dkim_signing_attributes(self, value: Optional[pulumi.Input[EmailIdentityDkimSigningAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_identity.setter
    def email_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="verificationStatus")
    def verification_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verification_status.setter
    def verification_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedForSendingStatus")
    def verified_for_sending_status(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @verified_for_sending_status.setter
    def verified_for_sending_status(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:sesv2/emailIdentity:EmailIdentity")
class EmailIdentity(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., dkim_signing_attributes: Optional[pulumi.Input[Union[EmailIdentityDkimSigningAttributesArgs, EmailIdentityDkimSigningAttributesArgsDict]]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EmailIdentityArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration_set_name: Optional[pulumi.Input[_builtins.str]] = ..., dkim_signing_attributes: Optional[pulumi.Input[Union[EmailIdentityDkimSigningAttributesArgs, EmailIdentityDkimSigningAttributesArgsDict]]] = ..., email_identity: Optional[pulumi.Input[_builtins.str]] = ..., identity_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., verification_status: Optional[pulumi.Input[_builtins.str]] = ..., verified_for_sending_status: Optional[pulumi.Input[_builtins.bool]] = ...) -> EmailIdentity:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationSetName")
    def configuration_set_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dkimSigningAttributes")
    def dkim_signing_attributes(self) -> pulumi.Output[outputs.EmailIdentityDkimSigningAttributes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailIdentity")
    def email_identity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="verificationStatus")
    def verification_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedForSendingStatus")
    def verified_for_sending_status(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    


