

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WidgetConfigArgs', 'WidgetConfig']
@pulumi.input_type
class WidgetConfigArgs:
    def __init__(__self__, *, engine_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], access_settings: Optional[pulumi.Input[WidgetConfigAccessSettingsArgs]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., homepage_setting: Optional[pulumi.Input[WidgetConfigHomepageSettingArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ui_branding: Optional[pulumi.Input[WidgetConfigUiBrandingArgs]] = ..., ui_settings: Optional[pulumi.Input[WidgetConfigUiSettingsArgs]] = ..., widget_config_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @engine_id.setter
    def engine_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessSettings")
    def access_settings(self) -> Optional[pulumi.Input[WidgetConfigAccessSettingsArgs]]:
        
        ...
    
    @access_settings.setter
    def access_settings(self, value: Optional[pulumi.Input[WidgetConfigAccessSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homepageSetting")
    def homepage_setting(self) -> Optional[pulumi.Input[WidgetConfigHomepageSettingArgs]]:
        
        ...
    
    @homepage_setting.setter
    def homepage_setting(self, value: Optional[pulumi.Input[WidgetConfigHomepageSettingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiBranding")
    def ui_branding(self) -> Optional[pulumi.Input[WidgetConfigUiBrandingArgs]]:
        
        ...
    
    @ui_branding.setter
    def ui_branding(self, value: Optional[pulumi.Input[WidgetConfigUiBrandingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiSettings")
    def ui_settings(self) -> Optional[pulumi.Input[WidgetConfigUiSettingsArgs]]:
        
        ...
    
    @ui_settings.setter
    def ui_settings(self, value: Optional[pulumi.Input[WidgetConfigUiSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="widgetConfigId")
    def widget_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @widget_config_id.setter
    def widget_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WidgetConfigState:
    def __init__(__self__, *, access_settings: Optional[pulumi.Input[WidgetConfigAccessSettingsArgs]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., homepage_setting: Optional[pulumi.Input[WidgetConfigHomepageSettingArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ui_branding: Optional[pulumi.Input[WidgetConfigUiBrandingArgs]] = ..., ui_settings: Optional[pulumi.Input[WidgetConfigUiSettingsArgs]] = ..., widget_config_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessSettings")
    def access_settings(self) -> Optional[pulumi.Input[WidgetConfigAccessSettingsArgs]]:
        
        ...
    
    @access_settings.setter
    def access_settings(self, value: Optional[pulumi.Input[WidgetConfigAccessSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_id.setter
    def engine_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homepageSetting")
    def homepage_setting(self) -> Optional[pulumi.Input[WidgetConfigHomepageSettingArgs]]:
        
        ...
    
    @homepage_setting.setter
    def homepage_setting(self, value: Optional[pulumi.Input[WidgetConfigHomepageSettingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiBranding")
    def ui_branding(self) -> Optional[pulumi.Input[WidgetConfigUiBrandingArgs]]:
        
        ...
    
    @ui_branding.setter
    def ui_branding(self, value: Optional[pulumi.Input[WidgetConfigUiBrandingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiSettings")
    def ui_settings(self) -> Optional[pulumi.Input[WidgetConfigUiSettingsArgs]]:
        
        ...
    
    @ui_settings.setter
    def ui_settings(self, value: Optional[pulumi.Input[WidgetConfigUiSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="widgetConfigId")
    def widget_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @widget_config_id.setter
    def widget_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:discoveryengine/widgetConfig:WidgetConfig")
class WidgetConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_settings: Optional[pulumi.Input[Union[WidgetConfigAccessSettingsArgs, WidgetConfigAccessSettingsArgsDict]]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., homepage_setting: Optional[pulumi.Input[Union[WidgetConfigHomepageSettingArgs, WidgetConfigHomepageSettingArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ui_branding: Optional[pulumi.Input[Union[WidgetConfigUiBrandingArgs, WidgetConfigUiBrandingArgsDict]]] = ..., ui_settings: Optional[pulumi.Input[Union[WidgetConfigUiSettingsArgs, WidgetConfigUiSettingsArgsDict]]] = ..., widget_config_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WidgetConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_settings: Optional[pulumi.Input[Union[WidgetConfigAccessSettingsArgs, WidgetConfigAccessSettingsArgsDict]]] = ..., collection_id: Optional[pulumi.Input[_builtins.str]] = ..., engine_id: Optional[pulumi.Input[_builtins.str]] = ..., homepage_setting: Optional[pulumi.Input[Union[WidgetConfigHomepageSettingArgs, WidgetConfigHomepageSettingArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ui_branding: Optional[pulumi.Input[Union[WidgetConfigUiBrandingArgs, WidgetConfigUiBrandingArgsDict]]] = ..., ui_settings: Optional[pulumi.Input[Union[WidgetConfigUiSettingsArgs, WidgetConfigUiSettingsArgsDict]]] = ..., widget_config_id: Optional[pulumi.Input[_builtins.str]] = ...) -> WidgetConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessSettings")
    def access_settings(self) -> pulumi.Output[outputs.WidgetConfigAccessSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homepageSetting")
    def homepage_setting(self) -> pulumi.Output[Optional[outputs.WidgetConfigHomepageSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiBranding")
    def ui_branding(self) -> pulumi.Output[Optional[outputs.WidgetConfigUiBranding]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uiSettings")
    def ui_settings(self) -> pulumi.Output[outputs.WidgetConfigUiSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="widgetConfigId")
    def widget_config_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


