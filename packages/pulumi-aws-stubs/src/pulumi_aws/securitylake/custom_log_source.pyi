

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
__all__ = ['CustomLogSourceArgs', 'CustomLogSource']
@pulumi.input_type
class CustomLogSourceArgs:
    def __init__(__self__, *, configuration: pulumi.Input[CustomLogSourceConfigurationArgs], source_name: pulumi.Input[_builtins.str], event_classes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Input[CustomLogSourceConfigurationArgs]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: pulumi.Input[CustomLogSourceConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_name.setter
    def source_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventClasses")
    def event_classes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @event_classes.setter
    def event_classes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_version.setter
    def source_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CustomLogSourceState:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[Sequence[pulumi.Input[CustomLogSourceAttributeArgs]]]] = ..., configuration: Optional[pulumi.Input[CustomLogSourceConfigurationArgs]] = ..., event_classes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., provider_details: Optional[pulumi.Input[Sequence[pulumi.Input[CustomLogSourceProviderDetailArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_name: Optional[pulumi.Input[_builtins.str]] = ..., source_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomLogSourceAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomLogSourceAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[CustomLogSourceConfigurationArgs]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[CustomLogSourceConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventClasses")
    def event_classes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @event_classes.setter
    def event_classes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerDetails")
    def provider_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomLogSourceProviderDetailArgs]]]]:
        
        ...
    
    @provider_details.setter
    def provider_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomLogSourceProviderDetailArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_name.setter
    def source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_version.setter
    def source_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:securitylake/customLogSource:CustomLogSource")
class CustomLogSource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configuration: Optional[pulumi.Input[Union[CustomLogSourceConfigurationArgs, CustomLogSourceConfigurationArgsDict]]] = ..., event_classes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_name: Optional[pulumi.Input[_builtins.str]] = ..., source_version: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomLogSourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CustomLogSourceAttributeArgs, CustomLogSourceAttributeArgsDict]]]]] = ..., configuration: Optional[pulumi.Input[Union[CustomLogSourceConfigurationArgs, CustomLogSourceConfigurationArgsDict]]] = ..., event_classes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., provider_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CustomLogSourceProviderDetailArgs, CustomLogSourceProviderDetailArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_name: Optional[pulumi.Input[_builtins.str]] = ..., source_version: Optional[pulumi.Input[_builtins.str]] = ...) -> CustomLogSource:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Sequence[outputs.CustomLogSourceAttribute]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[outputs.CustomLogSourceConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventClasses")
    def event_classes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerDetails")
    def provider_details(self) -> pulumi.Output[Sequence[outputs.CustomLogSourceProviderDetail]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


