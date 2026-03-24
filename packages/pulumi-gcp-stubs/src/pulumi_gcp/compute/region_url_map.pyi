

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
__all__ = ['RegionUrlMapArgs', 'RegionUrlMap']
@pulumi.input_type
class RegionUrlMapArgs:
    def __init__(__self__, *, default_route_action: Optional[pulumi.Input[RegionUrlMapDefaultRouteActionArgs]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[RegionUrlMapDefaultUrlRedirectArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[RegionUrlMapHeaderActionArgs]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapHostRuleArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapPathMatcherArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapTestArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> Optional[pulumi.Input[RegionUrlMapDefaultRouteActionArgs]]:
        
        ...
    
    @default_route_action.setter
    def default_route_action(self, value: Optional[pulumi.Input[RegionUrlMapDefaultRouteActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultService")
    def default_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_service.setter
    def default_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUrlRedirect")
    def default_url_redirect(self) -> Optional[pulumi.Input[RegionUrlMapDefaultUrlRedirectArgs]]:
        
        ...
    
    @default_url_redirect.setter
    def default_url_redirect(self, value: Optional[pulumi.Input[RegionUrlMapDefaultUrlRedirectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(self) -> Optional[pulumi.Input[RegionUrlMapHeaderActionArgs]]:
        
        ...
    
    @header_action.setter
    def header_action(self, value: Optional[pulumi.Input[RegionUrlMapHeaderActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapHostRuleArgs]]]]:
        
        ...
    
    @host_rules.setter
    def host_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapHostRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathMatchers")
    def path_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapPathMatcherArgs]]]]:
        
        ...
    
    @path_matchers.setter
    def path_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapPathMatcherArgs]]]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapTestArgs]]]]:
        
        ...
    
    @tests.setter
    def tests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapTestArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionUrlMapState:
    def __init__(__self__, *, creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., default_route_action: Optional[pulumi.Input[RegionUrlMapDefaultRouteActionArgs]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[RegionUrlMapDefaultUrlRedirectArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[RegionUrlMapHeaderActionArgs]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapHostRuleArgs]]]] = ..., map_id: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapPathMatcherArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapTestArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> Optional[pulumi.Input[RegionUrlMapDefaultRouteActionArgs]]:
        
        ...
    
    @default_route_action.setter
    def default_route_action(self, value: Optional[pulumi.Input[RegionUrlMapDefaultRouteActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultService")
    def default_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_service.setter
    def default_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUrlRedirect")
    def default_url_redirect(self) -> Optional[pulumi.Input[RegionUrlMapDefaultUrlRedirectArgs]]:
        
        ...
    
    @default_url_redirect.setter
    def default_url_redirect(self, value: Optional[pulumi.Input[RegionUrlMapDefaultUrlRedirectArgs]]): # -> None:
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
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(self) -> Optional[pulumi.Input[RegionUrlMapHeaderActionArgs]]:
        
        ...
    
    @header_action.setter
    def header_action(self, value: Optional[pulumi.Input[RegionUrlMapHeaderActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapHostRuleArgs]]]]:
        
        ...
    
    @host_rules.setter
    def host_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapHostRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapId")
    def map_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @map_id.setter
    def map_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathMatchers")
    def path_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapPathMatcherArgs]]]]:
        
        ...
    
    @path_matchers.setter
    def path_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapPathMatcherArgs]]]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapTestArgs]]]]:
        
        ...
    
    @tests.setter
    def tests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionUrlMapTestArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/regionUrlMap:RegionUrlMap")
class RegionUrlMap(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_route_action: Optional[pulumi.Input[Union[RegionUrlMapDefaultRouteActionArgs, RegionUrlMapDefaultRouteActionArgsDict]]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[Union[RegionUrlMapDefaultUrlRedirectArgs, RegionUrlMapDefaultUrlRedirectArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[Union[RegionUrlMapHeaderActionArgs, RegionUrlMapHeaderActionArgsDict]]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionUrlMapHostRuleArgs, RegionUrlMapHostRuleArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionUrlMapPathMatcherArgs, RegionUrlMapPathMatcherArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionUrlMapTestArgs, RegionUrlMapTestArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[RegionUrlMapArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., default_route_action: Optional[pulumi.Input[Union[RegionUrlMapDefaultRouteActionArgs, RegionUrlMapDefaultRouteActionArgsDict]]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[Union[RegionUrlMapDefaultUrlRedirectArgs, RegionUrlMapDefaultUrlRedirectArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[Union[RegionUrlMapHeaderActionArgs, RegionUrlMapHeaderActionArgsDict]]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionUrlMapHostRuleArgs, RegionUrlMapHostRuleArgsDict]]]]] = ..., map_id: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionUrlMapPathMatcherArgs, RegionUrlMapPathMatcherArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionUrlMapTestArgs, RegionUrlMapTestArgsDict]]]]] = ...) -> RegionUrlMap:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> pulumi.Output[Optional[outputs.RegionUrlMapDefaultRouteAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultService")
    def default_service(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUrlRedirect")
    def default_url_redirect(self) -> pulumi.Output[Optional[outputs.RegionUrlMapDefaultUrlRedirect]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(self) -> pulumi.Output[Optional[outputs.RegionUrlMapHeaderAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> pulumi.Output[Optional[Sequence[outputs.RegionUrlMapHostRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapId")
    def map_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathMatchers")
    def path_matchers(self) -> pulumi.Output[Optional[Sequence[outputs.RegionUrlMapPathMatcher]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tests(self) -> pulumi.Output[Optional[Sequence[outputs.RegionUrlMapTest]]]:
        
        ...
    


