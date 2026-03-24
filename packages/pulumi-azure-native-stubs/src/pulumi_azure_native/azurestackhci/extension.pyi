

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ExtensionArgs', 'Extension']
@pulumi.input_type
class ExtensionArgs:
    def __init__(__self__, *, arc_setting_name: pulumi.Input[_builtins.str], cluster_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ..., enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., extension_name: Optional[pulumi.Input[_builtins.str]] = ..., force_update_tag: Optional[pulumi.Input[_builtins.str]] = ..., protected_settings: Optional[Any] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[Any] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., type_handler_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="arcSettingName")
    def arc_setting_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arc_setting_name.setter
    def arc_setting_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionName")
    def extension_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extension_name.setter
    def extension_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        
        ...
    
    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurestackhci:Extension")
class Extension(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arc_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., auto_upgrade_minor_version: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_automatic_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., extension_name: Optional[pulumi.Input[_builtins.str]] = ..., force_update_tag: Optional[pulumi.Input[_builtins.str]] = ..., protected_settings: Optional[Any] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[Any] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., type_handler_version: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExtensionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Extension:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregateState")
    def aggregate_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perNodeExtensionDetails")
    def per_node_extension_details(self) -> pulumi.Output[Sequence[outputs.PerNodeExtensionStateResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


