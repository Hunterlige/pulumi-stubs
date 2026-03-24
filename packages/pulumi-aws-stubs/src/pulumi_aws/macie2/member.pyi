

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MemberArgs', 'Member']
@pulumi.input_type
class MemberArgs:
    def __init__(__self__, *, account_id: pulumi.Input[_builtins.str], email: pulumi.Input[_builtins.str], invitation_disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ..., invitation_message: Optional[pulumi.Input[_builtins.str]] = ..., invite: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationDisableEmailNotification")
    def invitation_disable_email_notification(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @invitation_disable_email_notification.setter
    def invitation_disable_email_notification(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationMessage")
    def invitation_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invitation_message.setter
    def invitation_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def invite(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @invite.setter
    def invite(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _MemberState:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., administrator_account_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., invitation_disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ..., invitation_message: Optional[pulumi.Input[_builtins.str]] = ..., invite: Optional[pulumi.Input[_builtins.bool]] = ..., invited_at: Optional[pulumi.Input[_builtins.str]] = ..., master_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., relationship_status: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorAccountId")
    def administrator_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @administrator_account_id.setter
    def administrator_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationDisableEmailNotification")
    def invitation_disable_email_notification(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @invitation_disable_email_notification.setter
    def invitation_disable_email_notification(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationMessage")
    def invitation_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invitation_message.setter
    def invitation_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def invite(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @invite.setter
    def invite(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitedAt")
    def invited_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invited_at.setter
    def invited_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @master_account_id.setter
    def master_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipStatus")
    def relationship_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relationship_status.setter
    def relationship_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:macie2/member:Member")
class Member(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., invitation_disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ..., invitation_message: Optional[pulumi.Input[_builtins.str]] = ..., invite: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MemberArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., administrator_account_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., email: Optional[pulumi.Input[_builtins.str]] = ..., invitation_disable_email_notification: Optional[pulumi.Input[_builtins.bool]] = ..., invitation_message: Optional[pulumi.Input[_builtins.str]] = ..., invite: Optional[pulumi.Input[_builtins.bool]] = ..., invited_at: Optional[pulumi.Input[_builtins.str]] = ..., master_account_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., relationship_status: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., updated_at: Optional[pulumi.Input[_builtins.str]] = ...) -> Member:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorAccountId")
    def administrator_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationDisableEmailNotification")
    def invitation_disable_email_notification(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitationMessage")
    def invitation_message(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def invite(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invitedAt")
    def invited_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipStatus")
    def relationship_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


