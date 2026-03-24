

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AFDCustomDomainArgs', 'AFDCustomDomain']
@pulumi.input_type
class AFDCustomDomainArgs:
    def __init__(__self__, *, host_name: pulumi.Input[_builtins.str], profile_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], azure_dns_zone: Optional[pulumi.Input[ResourceReferenceArgs]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., pre_validated_custom_domain_resource_id: Optional[pulumi.Input[ResourceReferenceArgs]] = ..., tls_settings: Optional[pulumi.Input[AFDDomainHttpsParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="azureDnsZone")
    def azure_dns_zone(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @azure_dns_zone.setter
    def azure_dns_zone(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extended_properties.setter
    def extended_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preValidatedCustomDomainResourceId")
    def pre_validated_custom_domain_resource_id(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @pre_validated_custom_domain_resource_id.setter
    def pre_validated_custom_domain_resource_id(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> Optional[pulumi.Input[AFDDomainHttpsParametersArgs]]:
        
        ...
    
    @tls_settings.setter
    def tls_settings(self, value: Optional[pulumi.Input[AFDDomainHttpsParametersArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cdn:AFDCustomDomain")
class AFDCustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_dns_zone: Optional[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]] = ..., custom_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., extended_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., host_name: Optional[pulumi.Input[_builtins.str]] = ..., pre_validated_custom_domain_resource_id: Optional[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tls_settings: Optional[pulumi.Input[Union[AFDDomainHttpsParametersArgs, AFDDomainHttpsParametersArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AFDCustomDomainArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AFDCustomDomain:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDnsZone")
    def azure_dns_zone(self) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainValidationState")
    def domain_validation_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preValidatedCustomDomainResourceId")
    def pre_validated_custom_domain_resource_id(self) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> pulumi.Output[Optional[outputs.AFDDomainHttpsParametersResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationProperties")
    def validation_properties(self) -> pulumi.Output[outputs.DomainValidationPropertiesResponse]:
        
        ...
    


