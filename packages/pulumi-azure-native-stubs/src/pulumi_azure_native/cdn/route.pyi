

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RouteArgs', 'Route']
@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *, endpoint_name: pulumi.Input[_builtins.str], profile_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], cache_configuration: Optional[pulumi.Input[AfdRouteCacheConfigurationArgs]] = ..., custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[ActivatedResourceReferenceArgs]]]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, EnabledState]]] = ..., forwarding_protocol: Optional[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]] = ..., https_redirect: Optional[pulumi.Input[Union[_builtins.str, HttpsRedirect]]] = ..., link_to_default_domain: Optional[pulumi.Input[Union[_builtins.str, LinkToDefaultDomain]]] = ..., origin_group: Optional[pulumi.Input[ResourceReferenceArgs]] = ..., origin_path: Optional[pulumi.Input[_builtins.str]] = ..., patterns_to_match: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., route_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]] = ..., supported_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AFDEndpointProtocols]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> Optional[pulumi.Input[AfdRouteCacheConfigurationArgs]]:
        
        ...
    
    @cache_configuration.setter
    def cache_configuration(self, value: Optional[pulumi.Input[AfdRouteCacheConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ActivatedResourceReferenceArgs]]]]:
        
        ...
    
    @custom_domains.setter
    def custom_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ActivatedResourceReferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[_builtins.str, EnabledState]]]:
        
        ...
    
    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[_builtins.str, EnabledState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]]:
        
        ...
    
    @forwarding_protocol.setter
    def forwarding_protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> Optional[pulumi.Input[Union[_builtins.str, HttpsRedirect]]]:
        
        ...
    
    @https_redirect.setter
    def https_redirect(self, value: Optional[pulumi.Input[Union[_builtins.str, HttpsRedirect]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkToDefaultDomain")
    def link_to_default_domain(self) -> Optional[pulumi.Input[Union[_builtins.str, LinkToDefaultDomain]]]:
        
        ...
    
    @link_to_default_domain.setter
    def link_to_default_domain(self, value: Optional[pulumi.Input[Union[_builtins.str, LinkToDefaultDomain]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @origin_group.setter
    def origin_group(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_path.setter
    def origin_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @patterns_to_match.setter
    def patterns_to_match(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeName")
    def route_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @route_name.setter
    def route_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]]:
        
        ...
    
    @rule_sets.setter
    def rule_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedProtocols")
    def supported_protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AFDEndpointProtocols]]]]]:
        
        ...
    
    @supported_protocols.setter
    def supported_protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AFDEndpointProtocols]]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cdn:Route")
class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cache_configuration: Optional[pulumi.Input[Union[AfdRouteCacheConfigurationArgs, AfdRouteCacheConfigurationArgsDict]]] = ..., custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ActivatedResourceReferenceArgs, ActivatedResourceReferenceArgsDict]]]]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, EnabledState]]] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., forwarding_protocol: Optional[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]] = ..., https_redirect: Optional[pulumi.Input[Union[_builtins.str, HttpsRedirect]]] = ..., link_to_default_domain: Optional[pulumi.Input[Union[_builtins.str, LinkToDefaultDomain]]] = ..., origin_group: Optional[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]] = ..., origin_path: Optional[pulumi.Input[_builtins.str]] = ..., patterns_to_match: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]]]] = ..., supported_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AFDEndpointProtocols]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RouteArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Route:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> pulumi.Output[Optional[outputs.AfdRouteCacheConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> pulumi.Output[Optional[Sequence[outputs.ActivatedResourceReferenceResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkToDefaultDomain")
    def link_to_default_domain(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> pulumi.Output[Optional[Sequence[outputs.ResourceReferenceResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedProtocols")
    def supported_protocols(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


