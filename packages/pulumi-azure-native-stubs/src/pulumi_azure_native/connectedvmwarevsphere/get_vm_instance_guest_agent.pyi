

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVMInstanceGuestAgentResult', 'AwaitableGetVMInstanceGuestAgentResult', 'get_vm_instance_guest_agent', 'get_vm_instance_guest_agent_output']
@pulumi.output_type
class GetVMInstanceGuestAgentResult:
    
    def __init__(__self__, azure_api_version=..., credentials=..., custom_resource_name=..., http_proxy_config=..., id=..., name=..., private_link_scope_resource_id=..., provisioning_action=..., provisioning_state=..., status=..., statuses=..., system_data=..., type=..., uuid=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.GuestCredentialResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> Optional[outputs.HttpProxyConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningAction")
    def provisioning_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Sequence[outputs.ResourceStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVMInstanceGuestAgentResult(GetVMInstanceGuestAgentResult):
    def __await__(self): # -> Generator[Never, Any, GetVMInstanceGuestAgentResult]:
        ...
    


def get_vm_instance_guest_agent(resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVMInstanceGuestAgentResult:
    
    ...

def get_vm_instance_guest_agent_output(resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVMInstanceGuestAgentResult]:
    
    ...

