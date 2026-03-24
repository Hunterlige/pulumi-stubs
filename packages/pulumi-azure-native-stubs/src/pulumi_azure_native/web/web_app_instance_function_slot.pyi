

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebAppInstanceFunctionSlotArgs', 'WebAppInstanceFunctionSlot']
@pulumi.input_type
class WebAppInstanceFunctionSlotArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], slot: pulumi.Input[_builtins.str], config: Optional[Any] = ..., config_href: Optional[pulumi.Input[_builtins.str]] = ..., files: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., function_app_id: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., href: Optional[pulumi.Input[_builtins.str]] = ..., invoke_url_template: Optional[pulumi.Input[_builtins.str]] = ..., is_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., language: Optional[pulumi.Input[_builtins.str]] = ..., script_href: Optional[pulumi.Input[_builtins.str]] = ..., script_root_path_href: Optional[pulumi.Input[_builtins.str]] = ..., secrets_file_href: Optional[pulumi.Input[_builtins.str]] = ..., test_data: Optional[pulumi.Input[_builtins.str]] = ..., test_data_href: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter
    def slot(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @slot.setter
    def slot(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[Any]:
        
        ...
    
    @config.setter
    def config(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configHref")
    def config_href(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config_href.setter
    def config_href(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def files(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @files.setter
    def files(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_app_id.setter
    def function_app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def href(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @href.setter
    def href(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeUrlTemplate")
    def invoke_url_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @invoke_url_template.setter
    def invoke_url_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_disabled.setter
    def is_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptHref")
    def script_href(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @script_href.setter
    def script_href(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptRootPathHref")
    def script_root_path_href(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @script_root_path_href.setter
    def script_root_path_href(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsFileHref")
    def secrets_file_href(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secrets_file_href.setter
    def secrets_file_href(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testData")
    def test_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @test_data.setter
    def test_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testDataHref")
    def test_data_href(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @test_data_href.setter
    def test_data_href(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:web:WebAppInstanceFunctionSlot")
class WebAppInstanceFunctionSlot(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., config: Optional[Any] = ..., config_href: Optional[pulumi.Input[_builtins.str]] = ..., files: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., function_app_id: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., href: Optional[pulumi.Input[_builtins.str]] = ..., invoke_url_template: Optional[pulumi.Input[_builtins.str]] = ..., is_disabled: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., language: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., script_href: Optional[pulumi.Input[_builtins.str]] = ..., script_root_path_href: Optional[pulumi.Input[_builtins.str]] = ..., secrets_file_href: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., test_data: Optional[pulumi.Input[_builtins.str]] = ..., test_data_href: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAppInstanceFunctionSlotArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WebAppInstanceFunctionSlot:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configHref")
    def config_href(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def files(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppId")
    def function_app_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def href(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invokeUrlTemplate")
    def invoke_url_template(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptHref")
    def script_href(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptRootPathHref")
    def script_root_path_href(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsFileHref")
    def secrets_file_href(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testData")
    def test_data(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testDataHref")
    def test_data_href(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


