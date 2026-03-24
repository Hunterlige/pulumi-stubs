

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
__all__ = ['PluginArgs', 'Plugin']
@pulumi.input_type
class PluginArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], plugin_id: pulumi.Input[_builtins.str], actions_configs: Optional[pulumi.Input[Sequence[pulumi.Input[PluginActionsConfigArgs]]]] = ..., config_template: Optional[pulumi.Input[PluginConfigTemplateArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[PluginDocumentationArgs]] = ..., hosting_service: Optional[pulumi.Input[PluginHostingServiceArgs]] = ..., plugin_category: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginId")
    def plugin_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @plugin_id.setter
    def plugin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsConfigs")
    def actions_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PluginActionsConfigArgs]]]]:
        
        ...
    
    @actions_configs.setter
    def actions_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PluginActionsConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configTemplate")
    def config_template(self) -> Optional[pulumi.Input[PluginConfigTemplateArgs]]:
        
        ...
    
    @config_template.setter
    def config_template(self, value: Optional[pulumi.Input[PluginConfigTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[PluginDocumentationArgs]]:
        
        ...
    
    @documentation.setter
    def documentation(self, value: Optional[pulumi.Input[PluginDocumentationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingService")
    def hosting_service(self) -> Optional[pulumi.Input[PluginHostingServiceArgs]]:
        
        ...
    
    @hosting_service.setter
    def hosting_service(self, value: Optional[pulumi.Input[PluginHostingServiceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginCategory")
    def plugin_category(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @plugin_category.setter
    def plugin_category(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PluginState:
    def __init__(__self__, *, actions_configs: Optional[pulumi.Input[Sequence[pulumi.Input[PluginActionsConfigArgs]]]] = ..., config_template: Optional[pulumi.Input[PluginConfigTemplateArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[PluginDocumentationArgs]] = ..., hosting_service: Optional[pulumi.Input[PluginHostingServiceArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ownership_type: Optional[pulumi.Input[_builtins.str]] = ..., plugin_category: Optional[pulumi.Input[_builtins.str]] = ..., plugin_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsConfigs")
    def actions_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PluginActionsConfigArgs]]]]:
        
        ...
    
    @actions_configs.setter
    def actions_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PluginActionsConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configTemplate")
    def config_template(self) -> Optional[pulumi.Input[PluginConfigTemplateArgs]]:
        
        ...
    
    @config_template.setter
    def config_template(self, value: Optional[pulumi.Input[PluginConfigTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[PluginDocumentationArgs]]:
        
        ...
    
    @documentation.setter
    def documentation(self, value: Optional[pulumi.Input[PluginDocumentationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingService")
    def hosting_service(self) -> Optional[pulumi.Input[PluginHostingServiceArgs]]:
        
        ...
    
    @hosting_service.setter
    def hosting_service(self, value: Optional[pulumi.Input[PluginHostingServiceArgs]]): # -> None:
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
    @pulumi.getter(name="ownershipType")
    def ownership_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ownership_type.setter
    def ownership_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginCategory")
    def plugin_category(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @plugin_category.setter
    def plugin_category(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginId")
    def plugin_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @plugin_id.setter
    def plugin_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apihub/plugin:Plugin")
class Plugin(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., actions_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PluginActionsConfigArgs, PluginActionsConfigArgsDict]]]]] = ..., config_template: Optional[pulumi.Input[Union[PluginConfigTemplateArgs, PluginConfigTemplateArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[Union[PluginDocumentationArgs, PluginDocumentationArgsDict]]] = ..., hosting_service: Optional[pulumi.Input[Union[PluginHostingServiceArgs, PluginHostingServiceArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., plugin_category: Optional[pulumi.Input[_builtins.str]] = ..., plugin_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PluginArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., actions_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PluginActionsConfigArgs, PluginActionsConfigArgsDict]]]]] = ..., config_template: Optional[pulumi.Input[Union[PluginConfigTemplateArgs, PluginConfigTemplateArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[Union[PluginDocumentationArgs, PluginDocumentationArgsDict]]] = ..., hosting_service: Optional[pulumi.Input[Union[PluginHostingServiceArgs, PluginHostingServiceArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ownership_type: Optional[pulumi.Input[_builtins.str]] = ..., plugin_category: Optional[pulumi.Input[_builtins.str]] = ..., plugin_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Plugin:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsConfigs")
    def actions_configs(self) -> pulumi.Output[Optional[Sequence[outputs.PluginActionsConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configTemplate")
    def config_template(self) -> pulumi.Output[outputs.PluginConfigTemplate]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> pulumi.Output[Optional[outputs.PluginDocumentation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingService")
    def hosting_service(self) -> pulumi.Output[Optional[outputs.PluginHostingService]]:
        
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
    @pulumi.getter(name="ownershipType")
    def ownership_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginCategory")
    def plugin_category(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginId")
    def plugin_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


