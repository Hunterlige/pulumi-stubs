

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebAppSitePushSettingsArgs', 'WebAppSitePushSettings']
@pulumi.input_type
class WebAppSitePushSettingsArgs:
    def __init__(__self__, *, is_push_enabled: pulumi.Input[_builtins.bool], name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], dynamic_tags_json: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., tag_whitelist_json: Optional[pulumi.Input[_builtins.str]] = ..., tags_requiring_auth: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPushEnabled")
    def is_push_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @is_push_enabled.setter
    def is_push_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicTagsJson")
    def dynamic_tags_json(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dynamic_tags_json.setter
    def dynamic_tags_json(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagWhitelistJson")
    def tag_whitelist_json(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag_whitelist_json.setter
    def tag_whitelist_json(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsRequiringAuth")
    def tags_requiring_auth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tags_requiring_auth.setter
    def tags_requiring_auth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:web:WebAppSitePushSettings")
class WebAppSitePushSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., dynamic_tags_json: Optional[pulumi.Input[_builtins.str]] = ..., is_push_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tag_whitelist_json: Optional[pulumi.Input[_builtins.str]] = ..., tags_requiring_auth: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAppSitePushSettingsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WebAppSitePushSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicTagsJson")
    def dynamic_tags_json(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPushEnabled")
    def is_push_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagWhitelistJson")
    def tag_whitelist_json(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsRequiringAuth")
    def tags_requiring_auth(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


