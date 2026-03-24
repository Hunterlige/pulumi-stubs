

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
__all__ = ['ScraperArgs', 'Scraper']
@pulumi.input_type
class ScraperArgs:
    def __init__(__self__, *, destination: pulumi.Input[ScraperDestinationArgs], scrape_configuration: pulumi.Input[_builtins.str], alias: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_configuration: Optional[pulumi.Input[ScraperRoleConfigurationArgs]] = ..., source: Optional[pulumi.Input[ScraperSourceArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[ScraperTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[ScraperDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[ScraperDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scrapeConfiguration")
    def scrape_configuration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @scrape_configuration.setter
    def scrape_configuration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleConfiguration")
    def role_configuration(self) -> Optional[pulumi.Input[ScraperRoleConfigurationArgs]]:
        
        ...
    
    @role_configuration.setter
    def role_configuration(self, value: Optional[pulumi.Input[ScraperRoleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[ScraperSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[ScraperSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ScraperTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ScraperTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ScraperState:
    def __init__(__self__, *, alias: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[ScraperDestinationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., role_configuration: Optional[pulumi.Input[ScraperRoleConfigurationArgs]] = ..., scrape_configuration: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[ScraperSourceArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[ScraperTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def destination(self) -> Optional[pulumi.Input[ScraperDestinationArgs]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[ScraperDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleConfiguration")
    def role_configuration(self) -> Optional[pulumi.Input[ScraperRoleConfigurationArgs]]:
        
        ...
    
    @role_configuration.setter
    def role_configuration(self, value: Optional[pulumi.Input[ScraperRoleConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scrapeConfiguration")
    def scrape_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scrape_configuration.setter
    def scrape_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[ScraperSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[ScraperSourceArgs]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ScraperTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ScraperTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:amp/scraper:Scraper")
class Scraper(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alias: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[Union[ScraperDestinationArgs, ScraperDestinationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_configuration: Optional[pulumi.Input[Union[ScraperRoleConfigurationArgs, ScraperRoleConfigurationArgsDict]]] = ..., scrape_configuration: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[ScraperSourceArgs, ScraperSourceArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[ScraperTimeoutsArgs, ScraperTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ScraperArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., alias: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[Union[ScraperDestinationArgs, ScraperDestinationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ..., role_configuration: Optional[pulumi.Input[Union[ScraperRoleConfigurationArgs, ScraperRoleConfigurationArgsDict]]] = ..., scrape_configuration: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[ScraperSourceArgs, ScraperSourceArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[ScraperTimeoutsArgs, ScraperTimeoutsArgsDict]]] = ...) -> Scraper:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[outputs.ScraperDestination]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleConfiguration")
    def role_configuration(self) -> pulumi.Output[Optional[outputs.ScraperRoleConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scrapeConfiguration")
    def scrape_configuration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[outputs.ScraperSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ScraperTimeouts]]:
        ...
    


