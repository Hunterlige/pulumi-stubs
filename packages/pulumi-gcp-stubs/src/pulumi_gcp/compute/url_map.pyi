

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
__all__ = ['URLMapArgs', 'URLMap']
@pulumi.input_type
class URLMapArgs:
    def __init__(__self__, *, default_custom_error_response_policy: Optional[pulumi.Input[URLMapDefaultCustomErrorResponsePolicyArgs]] = ..., default_route_action: Optional[pulumi.Input[URLMapDefaultRouteActionArgs]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[URLMapDefaultUrlRedirectArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[URLMapHeaderActionArgs]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapHostRuleArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapPathMatcherArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapTestArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCustomErrorResponsePolicy")
    def default_custom_error_response_policy(self) -> Optional[pulumi.Input[URLMapDefaultCustomErrorResponsePolicyArgs]]:
        
        ...
    
    @default_custom_error_response_policy.setter
    def default_custom_error_response_policy(self, value: Optional[pulumi.Input[URLMapDefaultCustomErrorResponsePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> Optional[pulumi.Input[URLMapDefaultRouteActionArgs]]:
        
        ...
    
    @default_route_action.setter
    def default_route_action(self, value: Optional[pulumi.Input[URLMapDefaultRouteActionArgs]]): # -> None:
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
    def default_url_redirect(self) -> Optional[pulumi.Input[URLMapDefaultUrlRedirectArgs]]:
        
        ...
    
    @default_url_redirect.setter
    def default_url_redirect(self, value: Optional[pulumi.Input[URLMapDefaultUrlRedirectArgs]]): # -> None:
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
    def header_action(self) -> Optional[pulumi.Input[URLMapHeaderActionArgs]]:
        
        ...
    
    @header_action.setter
    def header_action(self, value: Optional[pulumi.Input[URLMapHeaderActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[URLMapHostRuleArgs]]]]:
        
        ...
    
    @host_rules.setter
    def host_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapHostRuleArgs]]]]): # -> None:
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
    def path_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[URLMapPathMatcherArgs]]]]:
        
        ...
    
    @path_matchers.setter
    def path_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapPathMatcherArgs]]]]): # -> None:
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
    def tests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[URLMapTestArgs]]]]:
        
        ...
    
    @tests.setter
    def tests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapTestArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _URLMapState:
    def __init__(__self__, *, creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., default_custom_error_response_policy: Optional[pulumi.Input[URLMapDefaultCustomErrorResponsePolicyArgs]] = ..., default_route_action: Optional[pulumi.Input[URLMapDefaultRouteActionArgs]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[URLMapDefaultUrlRedirectArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[URLMapHeaderActionArgs]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapHostRuleArgs]]]] = ..., map_id: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapPathMatcherArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapTestArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCustomErrorResponsePolicy")
    def default_custom_error_response_policy(self) -> Optional[pulumi.Input[URLMapDefaultCustomErrorResponsePolicyArgs]]:
        
        ...
    
    @default_custom_error_response_policy.setter
    def default_custom_error_response_policy(self, value: Optional[pulumi.Input[URLMapDefaultCustomErrorResponsePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> Optional[pulumi.Input[URLMapDefaultRouteActionArgs]]:
        
        ...
    
    @default_route_action.setter
    def default_route_action(self, value: Optional[pulumi.Input[URLMapDefaultRouteActionArgs]]): # -> None:
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
    def default_url_redirect(self) -> Optional[pulumi.Input[URLMapDefaultUrlRedirectArgs]]:
        
        ...
    
    @default_url_redirect.setter
    def default_url_redirect(self, value: Optional[pulumi.Input[URLMapDefaultUrlRedirectArgs]]): # -> None:
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
    def header_action(self) -> Optional[pulumi.Input[URLMapHeaderActionArgs]]:
        
        ...
    
    @header_action.setter
    def header_action(self, value: Optional[pulumi.Input[URLMapHeaderActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[URLMapHostRuleArgs]]]]:
        
        ...
    
    @host_rules.setter
    def host_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapHostRuleArgs]]]]): # -> None:
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
    def path_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[URLMapPathMatcherArgs]]]]:
        
        ...
    
    @path_matchers.setter
    def path_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapPathMatcherArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[URLMapTestArgs]]]]:
        
        ...
    
    @tests.setter
    def tests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[URLMapTestArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/uRLMap:URLMap")
class URLMap(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., default_custom_error_response_policy: Optional[pulumi.Input[Union[URLMapDefaultCustomErrorResponsePolicyArgs, URLMapDefaultCustomErrorResponsePolicyArgsDict]]] = ..., default_route_action: Optional[pulumi.Input[Union[URLMapDefaultRouteActionArgs, URLMapDefaultRouteActionArgsDict]]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[Union[URLMapDefaultUrlRedirectArgs, URLMapDefaultUrlRedirectArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[Union[URLMapHeaderActionArgs, URLMapHeaderActionArgsDict]]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[URLMapHostRuleArgs, URLMapHostRuleArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[URLMapPathMatcherArgs, URLMapPathMatcherArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[Union[URLMapTestArgs, URLMapTestArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[URLMapArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., default_custom_error_response_policy: Optional[pulumi.Input[Union[URLMapDefaultCustomErrorResponsePolicyArgs, URLMapDefaultCustomErrorResponsePolicyArgsDict]]] = ..., default_route_action: Optional[pulumi.Input[Union[URLMapDefaultRouteActionArgs, URLMapDefaultRouteActionArgsDict]]] = ..., default_service: Optional[pulumi.Input[_builtins.str]] = ..., default_url_redirect: Optional[pulumi.Input[Union[URLMapDefaultUrlRedirectArgs, URLMapDefaultUrlRedirectArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., header_action: Optional[pulumi.Input[Union[URLMapHeaderActionArgs, URLMapHeaderActionArgsDict]]] = ..., host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[URLMapHostRuleArgs, URLMapHostRuleArgsDict]]]]] = ..., map_id: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[URLMapPathMatcherArgs, URLMapPathMatcherArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., tests: Optional[pulumi.Input[Sequence[pulumi.Input[Union[URLMapTestArgs, URLMapTestArgsDict]]]]] = ...) -> URLMap:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCustomErrorResponsePolicy")
    def default_custom_error_response_policy(self) -> pulumi.Output[Optional[outputs.URLMapDefaultCustomErrorResponsePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> pulumi.Output[Optional[outputs.URLMapDefaultRouteAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultService")
    def default_service(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultUrlRedirect")
    def default_url_redirect(self) -> pulumi.Output[Optional[outputs.URLMapDefaultUrlRedirect]]:
        
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
    def header_action(self) -> pulumi.Output[Optional[outputs.URLMapHeaderAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> pulumi.Output[Optional[Sequence[outputs.URLMapHostRule]]]:
        
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
    def path_matchers(self) -> pulumi.Output[Optional[Sequence[outputs.URLMapPathMatcher]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tests(self) -> pulumi.Output[Optional[Sequence[outputs.URLMapTest]]]:
        
        ...
    


