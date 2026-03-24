

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GatewayApiEntityTagArgs', 'GatewayApiEntityTag']
@pulumi.input_type
class GatewayApiEntityTagArgs:
    def __init__(__self__, *, gateway_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], api_id: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[ProvisioningState]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[ProvisioningState]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[ProvisioningState]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:apimanagement:GatewayApiEntityTag")
class GatewayApiEntityTag(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_state: Optional[pulumi.Input[ProvisioningState]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GatewayApiEntityTagArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> GatewayApiEntityTag:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiRevision")
    def api_revision(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiRevisionDescription")
    def api_revision_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiType")
    def api_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersionDescription")
    def api_version_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersionSet")
    def api_version_set(self) -> pulumi.Output[Optional[outputs.ApiVersionSetContractDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersionSetId")
    def api_version_set_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationSettings")
    def authentication_settings(self) -> pulumi.Output[Optional[outputs.AuthenticationSettingsContractResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contact(self) -> pulumi.Output[Optional[outputs.ApiContactInformationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCurrent")
    def is_current(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOnline")
    def is_online(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def license(self) -> pulumi.Output[Optional[outputs.ApiLicenseInformationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApiId")
    def source_api_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionKeyParameterNames")
    def subscription_key_parameter_names(self) -> pulumi.Output[Optional[outputs.SubscriptionKeyParameterNamesContractResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="termsOfServiceUrl")
    def terms_of_service_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


