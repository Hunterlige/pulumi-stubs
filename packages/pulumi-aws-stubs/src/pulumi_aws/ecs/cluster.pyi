

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, configuration: Optional[pulumi.Input[ClusterConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_defaults: Optional[pulumi.Input[ClusterServiceConnectDefaultsArgs]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterSettingArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[ClusterConfigurationArgs]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[ClusterConfigurationArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectDefaults")
    def service_connect_defaults(self) -> Optional[pulumi.Input[ClusterServiceConnectDefaultsArgs]]:
        
        ...
    
    @service_connect_defaults.setter
    def service_connect_defaults(self, value: Optional[pulumi.Input[ClusterServiceConnectDefaultsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterSettingArgs]]]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterSettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration: Optional[pulumi.Input[ClusterConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_defaults: Optional[pulumi.Input[ClusterServiceConnectDefaultsArgs]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterSettingArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
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
    def configuration(self) -> Optional[pulumi.Input[ClusterConfigurationArgs]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[ClusterConfigurationArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectDefaults")
    def service_connect_defaults(self) -> Optional[pulumi.Input[ClusterServiceConnectDefaultsArgs]]:
        
        ...
    
    @service_connect_defaults.setter
    def service_connect_defaults(self, value: Optional[pulumi.Input[ClusterServiceConnectDefaultsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterSettingArgs]]]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterSettingArgs]]]]): # -> None:
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
    


@pulumi.type_token("aws:ecs/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configuration: Optional[pulumi.Input[Union[ClusterConfigurationArgs, ClusterConfigurationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_defaults: Optional[pulumi.Input[Union[ClusterServiceConnectDefaultsArgs, ClusterServiceConnectDefaultsArgsDict]]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterSettingArgs, ClusterSettingArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ClusterArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., configuration: Optional[pulumi.Input[Union[ClusterConfigurationArgs, ClusterConfigurationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_connect_defaults: Optional[pulumi.Input[Union[ClusterServiceConnectDefaultsArgs, ClusterServiceConnectDefaultsArgsDict]]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterSettingArgs, ClusterSettingArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[outputs.ClusterConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConnectDefaults")
    def service_connect_defaults(self) -> pulumi.Output[Optional[outputs.ClusterServiceConnectDefaults]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Sequence[outputs.ClusterSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


