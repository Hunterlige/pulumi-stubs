

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
__all__ = ['EnterpriseKeyArgs', 'EnterpriseKey']
@pulumi.input_type
class EnterpriseKeyArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], android_settings: Optional[pulumi.Input[EnterpriseKeyAndroidSettingsArgs]] = ..., ios_settings: Optional[pulumi.Input[EnterpriseKeyIosSettingsArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., testing_options: Optional[pulumi.Input[EnterpriseKeyTestingOptionsArgs]] = ..., waf_settings: Optional[pulumi.Input[EnterpriseKeyWafSettingsArgs]] = ..., web_settings: Optional[pulumi.Input[EnterpriseKeyWebSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="androidSettings")
    def android_settings(self) -> Optional[pulumi.Input[EnterpriseKeyAndroidSettingsArgs]]:
        
        ...
    
    @android_settings.setter
    def android_settings(self, value: Optional[pulumi.Input[EnterpriseKeyAndroidSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iosSettings")
    def ios_settings(self) -> Optional[pulumi.Input[EnterpriseKeyIosSettingsArgs]]:
        
        ...
    
    @ios_settings.setter
    def ios_settings(self, value: Optional[pulumi.Input[EnterpriseKeyIosSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testingOptions")
    def testing_options(self) -> Optional[pulumi.Input[EnterpriseKeyTestingOptionsArgs]]:
        
        ...
    
    @testing_options.setter
    def testing_options(self, value: Optional[pulumi.Input[EnterpriseKeyTestingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wafSettings")
    def waf_settings(self) -> Optional[pulumi.Input[EnterpriseKeyWafSettingsArgs]]:
        
        ...
    
    @waf_settings.setter
    def waf_settings(self, value: Optional[pulumi.Input[EnterpriseKeyWafSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webSettings")
    def web_settings(self) -> Optional[pulumi.Input[EnterpriseKeyWebSettingsArgs]]:
        
        ...
    
    @web_settings.setter
    def web_settings(self, value: Optional[pulumi.Input[EnterpriseKeyWebSettingsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _EnterpriseKeyState:
    def __init__(__self__, *, android_settings: Optional[pulumi.Input[EnterpriseKeyAndroidSettingsArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ios_settings: Optional[pulumi.Input[EnterpriseKeyIosSettingsArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., testing_options: Optional[pulumi.Input[EnterpriseKeyTestingOptionsArgs]] = ..., waf_settings: Optional[pulumi.Input[EnterpriseKeyWafSettingsArgs]] = ..., web_settings: Optional[pulumi.Input[EnterpriseKeyWebSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="androidSettings")
    def android_settings(self) -> Optional[pulumi.Input[EnterpriseKeyAndroidSettingsArgs]]:
        
        ...
    
    @android_settings.setter
    def android_settings(self, value: Optional[pulumi.Input[EnterpriseKeyAndroidSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iosSettings")
    def ios_settings(self) -> Optional[pulumi.Input[EnterpriseKeyIosSettingsArgs]]:
        
        ...
    
    @ios_settings.setter
    def ios_settings(self, value: Optional[pulumi.Input[EnterpriseKeyIosSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testingOptions")
    def testing_options(self) -> Optional[pulumi.Input[EnterpriseKeyTestingOptionsArgs]]:
        
        ...
    
    @testing_options.setter
    def testing_options(self, value: Optional[pulumi.Input[EnterpriseKeyTestingOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wafSettings")
    def waf_settings(self) -> Optional[pulumi.Input[EnterpriseKeyWafSettingsArgs]]:
        
        ...
    
    @waf_settings.setter
    def waf_settings(self, value: Optional[pulumi.Input[EnterpriseKeyWafSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webSettings")
    def web_settings(self) -> Optional[pulumi.Input[EnterpriseKeyWebSettingsArgs]]:
        
        ...
    
    @web_settings.setter
    def web_settings(self, value: Optional[pulumi.Input[EnterpriseKeyWebSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:recaptcha/enterpriseKey:EnterpriseKey")
class EnterpriseKey(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., android_settings: Optional[pulumi.Input[Union[EnterpriseKeyAndroidSettingsArgs, EnterpriseKeyAndroidSettingsArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., ios_settings: Optional[pulumi.Input[Union[EnterpriseKeyIosSettingsArgs, EnterpriseKeyIosSettingsArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., testing_options: Optional[pulumi.Input[Union[EnterpriseKeyTestingOptionsArgs, EnterpriseKeyTestingOptionsArgsDict]]] = ..., waf_settings: Optional[pulumi.Input[Union[EnterpriseKeyWafSettingsArgs, EnterpriseKeyWafSettingsArgsDict]]] = ..., web_settings: Optional[pulumi.Input[Union[EnterpriseKeyWebSettingsArgs, EnterpriseKeyWebSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EnterpriseKeyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., android_settings: Optional[pulumi.Input[Union[EnterpriseKeyAndroidSettingsArgs, EnterpriseKeyAndroidSettingsArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ios_settings: Optional[pulumi.Input[Union[EnterpriseKeyIosSettingsArgs, EnterpriseKeyIosSettingsArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., testing_options: Optional[pulumi.Input[Union[EnterpriseKeyTestingOptionsArgs, EnterpriseKeyTestingOptionsArgsDict]]] = ..., waf_settings: Optional[pulumi.Input[Union[EnterpriseKeyWafSettingsArgs, EnterpriseKeyWafSettingsArgsDict]]] = ..., web_settings: Optional[pulumi.Input[Union[EnterpriseKeyWebSettingsArgs, EnterpriseKeyWebSettingsArgsDict]]] = ...) -> EnterpriseKey:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="androidSettings")
    def android_settings(self) -> pulumi.Output[Optional[outputs.EnterpriseKeyAndroidSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iosSettings")
    def ios_settings(self) -> pulumi.Output[Optional[outputs.EnterpriseKeyIosSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testingOptions")
    def testing_options(self) -> pulumi.Output[Optional[outputs.EnterpriseKeyTestingOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wafSettings")
    def waf_settings(self) -> pulumi.Output[Optional[outputs.EnterpriseKeyWafSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webSettings")
    def web_settings(self) -> pulumi.Output[Optional[outputs.EnterpriseKeyWebSettings]]:
        
        ...
    


