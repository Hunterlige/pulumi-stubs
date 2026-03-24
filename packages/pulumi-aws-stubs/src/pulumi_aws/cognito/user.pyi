

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserArgs', 'User']
@pulumi.input_type
class UserArgs:
    def __init__(__self__, *, user_pool_id: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str], attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., client_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., desired_delivery_mediums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., force_alias_creation: Optional[pulumi.Input[_builtins.bool]] = ..., message_action: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., temporary_password: Optional[pulumi.Input[_builtins.str]] = ..., validation_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientMetadata")
    def client_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_metadata.setter
    def client_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredDeliveryMediums")
    def desired_delivery_mediums(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @desired_delivery_mediums.setter
    def desired_delivery_mediums(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceAliasCreation")
    def force_alias_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_alias_creation.setter
    def force_alias_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageAction")
    def message_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_action.setter
    def message_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryPassword")
    def temporary_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @temporary_password.setter
    def temporary_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _UserState:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., client_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., desired_delivery_mediums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., force_alias_creation: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified_date: Optional[pulumi.Input[_builtins.str]] = ..., message_action: Optional[pulumi.Input[_builtins.str]] = ..., mfa_setting_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., preferred_mfa_setting: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., sub: Optional[pulumi.Input[_builtins.str]] = ..., temporary_password: Optional[pulumi.Input[_builtins.str]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ..., validation_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientMetadata")
    def client_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @client_metadata.setter
    def client_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredDeliveryMediums")
    def desired_delivery_mediums(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @desired_delivery_mediums.setter
    def desired_delivery_mediums(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceAliasCreation")
    def force_alias_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_alias_creation.setter
    def force_alias_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @last_modified_date.setter
    def last_modified_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageAction")
    def message_action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_action.setter
    def message_action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mfaSettingLists")
    def mfa_setting_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @mfa_setting_lists.setter
    def mfa_setting_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMfaSetting")
    def preferred_mfa_setting(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @preferred_mfa_setting.setter
    def preferred_mfa_setting(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def sub(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sub.setter
    def sub(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryPassword")
    def temporary_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @temporary_password.setter
    def temporary_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_pool_id.setter
    def user_pool_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @validation_data.setter
    def validation_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:cognito/user:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., client_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., desired_delivery_mediums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., force_alias_creation: Optional[pulumi.Input[_builtins.bool]] = ..., message_action: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., temporary_password: Optional[pulumi.Input[_builtins.str]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ..., validation_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., client_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., desired_delivery_mediums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., force_alias_creation: Optional[pulumi.Input[_builtins.bool]] = ..., last_modified_date: Optional[pulumi.Input[_builtins.str]] = ..., message_action: Optional[pulumi.Input[_builtins.str]] = ..., mfa_setting_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., preferred_mfa_setting: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., sub: Optional[pulumi.Input[_builtins.str]] = ..., temporary_password: Optional[pulumi.Input[_builtins.str]] = ..., user_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ..., validation_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> User:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientMetadata")
    def client_metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredDeliveryMediums")
    def desired_delivery_mediums(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceAliasCreation")
    def force_alias_creation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageAction")
    def message_action(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mfaSettingLists")
    def mfa_setting_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMfaSetting")
    def preferred_mfa_setting(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sub(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryPassword")
    def temporary_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    


