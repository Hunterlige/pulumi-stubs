

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
__all__ = ['GcpUserAccessBindingArgs', 'GcpUserAccessBinding']
@pulumi.input_type
class GcpUserAccessBindingArgs:
    def __init__(__self__, *, group_key: pulumi.Input[_builtins.str], organization_id: pulumi.Input[_builtins.str], access_levels: Optional[pulumi.Input[_builtins.str]] = ..., scoped_access_settings: Optional[pulumi.Input[Sequence[pulumi.Input[GcpUserAccessBindingScopedAccessSettingArgs]]]] = ..., session_settings: Optional[pulumi.Input[GcpUserAccessBindingSessionSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_key.setter
    def group_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @organization_id.setter
    def organization_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_levels.setter
    def access_levels(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopedAccessSettings")
    def scoped_access_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GcpUserAccessBindingScopedAccessSettingArgs]]]]:
        
        ...
    
    @scoped_access_settings.setter
    def scoped_access_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GcpUserAccessBindingScopedAccessSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionSettings")
    def session_settings(self) -> Optional[pulumi.Input[GcpUserAccessBindingSessionSettingsArgs]]:
        
        ...
    
    @session_settings.setter
    def session_settings(self, value: Optional[pulumi.Input[GcpUserAccessBindingSessionSettingsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _GcpUserAccessBindingState:
    def __init__(__self__, *, access_levels: Optional[pulumi.Input[_builtins.str]] = ..., group_key: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization_id: Optional[pulumi.Input[_builtins.str]] = ..., scoped_access_settings: Optional[pulumi.Input[Sequence[pulumi.Input[GcpUserAccessBindingScopedAccessSettingArgs]]]] = ..., session_settings: Optional[pulumi.Input[GcpUserAccessBindingSessionSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_levels.setter
    def access_levels(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_key.setter
    def group_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopedAccessSettings")
    def scoped_access_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GcpUserAccessBindingScopedAccessSettingArgs]]]]:
        
        ...
    
    @scoped_access_settings.setter
    def scoped_access_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GcpUserAccessBindingScopedAccessSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionSettings")
    def session_settings(self) -> Optional[pulumi.Input[GcpUserAccessBindingSessionSettingsArgs]]:
        
        ...
    
    @session_settings.setter
    def session_settings(self, value: Optional[pulumi.Input[GcpUserAccessBindingSessionSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class GcpUserAccessBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_levels: Optional[pulumi.Input[_builtins.str]] = ..., group_key: Optional[pulumi.Input[_builtins.str]] = ..., organization_id: Optional[pulumi.Input[_builtins.str]] = ..., scoped_access_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GcpUserAccessBindingScopedAccessSettingArgs, GcpUserAccessBindingScopedAccessSettingArgsDict]]]]] = ..., session_settings: Optional[pulumi.Input[Union[GcpUserAccessBindingSessionSettingsArgs, GcpUserAccessBindingSessionSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GcpUserAccessBindingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_levels: Optional[pulumi.Input[_builtins.str]] = ..., group_key: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., organization_id: Optional[pulumi.Input[_builtins.str]] = ..., scoped_access_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GcpUserAccessBindingScopedAccessSettingArgs, GcpUserAccessBindingScopedAccessSettingArgsDict]]]]] = ..., session_settings: Optional[pulumi.Input[Union[GcpUserAccessBindingSessionSettingsArgs, GcpUserAccessBindingSessionSettingsArgsDict]]] = ...) -> GcpUserAccessBinding:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopedAccessSettings")
    def scoped_access_settings(self) -> pulumi.Output[Optional[Sequence[outputs.GcpUserAccessBindingScopedAccessSetting]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionSettings")
    def session_settings(self) -> pulumi.Output[Optional[outputs.GcpUserAccessBindingSessionSettings]]:
        
        ...
    


