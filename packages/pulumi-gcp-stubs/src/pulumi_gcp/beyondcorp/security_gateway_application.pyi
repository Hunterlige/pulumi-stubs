

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
__all__ = ['SecurityGatewayApplicationArgs', 'SecurityGatewayApplication']
@pulumi.input_type
class SecurityGatewayApplicationArgs:
    def __init__(__self__, *, application_id: pulumi.Input[_builtins.str], security_gateway_id: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationEndpointMatcherArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., upstreams: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationUpstreamArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_gateway_id.setter
    def security_gateway_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointMatchers")
    def endpoint_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationEndpointMatcherArgs]]]]:
        
        ...
    
    @endpoint_matchers.setter
    def endpoint_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationEndpointMatcherArgs]]]]): # -> None:
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
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def upstreams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationUpstreamArgs]]]]:
        
        ...
    
    @upstreams.setter
    def upstreams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationUpstreamArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _SecurityGatewayApplicationState:
    def __init__(__self__, *, application_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationEndpointMatcherArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., upstreams: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationUpstreamArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="endpointMatchers")
    def endpoint_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationEndpointMatcherArgs]]]]:
        
        ...
    
    @endpoint_matchers.setter
    def endpoint_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationEndpointMatcherArgs]]]]): # -> None:
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
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_gateway_id.setter
    def security_gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def upstreams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationUpstreamArgs]]]]:
        
        ...
    
    @upstreams.setter
    def upstreams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityGatewayApplicationUpstreamArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SecurityGatewayApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityGatewayApplicationEndpointMatcherArgs, SecurityGatewayApplicationEndpointMatcherArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., upstreams: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityGatewayApplicationUpstreamArgs, SecurityGatewayApplicationUpstreamArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityGatewayApplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityGatewayApplicationEndpointMatcherArgs, SecurityGatewayApplicationEndpointMatcherArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., upstreams: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SecurityGatewayApplicationUpstreamArgs, SecurityGatewayApplicationUpstreamArgsDict]]]]] = ...) -> SecurityGatewayApplication:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointMatchers")
    def endpoint_matchers(self) -> pulumi.Output[Optional[Sequence[outputs.SecurityGatewayApplicationEndpointMatcher]]]:
        
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
    @pulumi.getter
    def schema(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def upstreams(self) -> pulumi.Output[Optional[Sequence[outputs.SecurityGatewayApplicationUpstream]]]:
        
        ...
    


