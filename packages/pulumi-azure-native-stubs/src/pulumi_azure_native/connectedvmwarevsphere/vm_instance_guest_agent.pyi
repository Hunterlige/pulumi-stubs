

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
__all__ = ['VMInstanceGuestAgentArgs', 'VMInstanceGuestAgent']
@pulumi.input_type
class VMInstanceGuestAgentArgs:
    def __init__(__self__, *, resource_uri: pulumi.Input[_builtins.str], credentials: Optional[pulumi.Input[GuestCredentialArgs]] = ..., http_proxy_config: Optional[pulumi.Input[HttpProxyConfigurationArgs]] = ..., private_link_scope_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_action: Optional[pulumi.Input[Union[_builtins.str, ProvisioningAction]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[GuestCredentialArgs]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[GuestCredentialArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> Optional[pulumi.Input[HttpProxyConfigurationArgs]]:
        
        ...
    
    @http_proxy_config.setter
    def http_proxy_config(self, value: Optional[pulumi.Input[HttpProxyConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_scope_resource_id.setter
    def private_link_scope_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningAction")
    def provisioning_action(self) -> Optional[pulumi.Input[Union[_builtins.str, ProvisioningAction]]]:
        
        ...
    
    @provisioning_action.setter
    def provisioning_action(self, value: Optional[pulumi.Input[Union[_builtins.str, ProvisioningAction]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VMInstanceGuestAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., credentials: Optional[pulumi.Input[Union[GuestCredentialArgs, GuestCredentialArgsDict]]] = ..., http_proxy_config: Optional[pulumi.Input[Union[HttpProxyConfigurationArgs, HttpProxyConfigurationArgsDict]]] = ..., private_link_scope_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_action: Optional[pulumi.Input[Union[_builtins.str, ProvisioningAction]]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VMInstanceGuestAgentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VMInstanceGuestAgent:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[outputs.GuestCredentialResponseV1]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> pulumi.Output[Optional[outputs.HttpProxyConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningAction")
    def provisioning_action(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.ResourceStatusResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


