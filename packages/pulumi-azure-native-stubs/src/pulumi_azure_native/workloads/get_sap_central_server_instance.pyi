

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSapCentralServerInstanceResult', 'AwaitableGetSapCentralServerInstanceResult', 'get_sap_central_server_instance', 'get_sap_central_server_instance_output']
@pulumi.output_type
class GetSapCentralServerInstanceResult:
    
    def __init__(__self__, azure_api_version=..., enqueue_replication_server_properties=..., enqueue_server_properties=..., errors=..., gateway_server_properties=..., health=..., id=..., instance_no=..., kernel_patch=..., kernel_version=..., load_balancer_details=..., location=..., message_server_properties=..., name=..., provisioning_state=..., status=..., subnet=..., system_data=..., tags=..., type=..., vm_details=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enqueueReplicationServerProperties")
    def enqueue_replication_server_properties(self) -> Optional[outputs.EnqueueReplicationServerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enqueueServerProperties")
    def enqueue_server_properties(self) -> Optional[outputs.EnqueueServerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.SAPVirtualInstanceErrorResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayServerProperties")
    def gateway_server_properties(self) -> Optional[outputs.GatewayServerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceNo")
    def instance_no(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelPatch")
    def kernel_patch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kernelVersion")
    def kernel_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerDetails")
    def load_balancer_details(self) -> outputs.LoadBalancerDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageServerProperties")
    def message_server_properties(self) -> Optional[outputs.MessageServerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
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
    def subnet(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmDetails")
    def vm_details(self) -> Sequence[outputs.CentralServerVmDetailsResponse]:
        
        ...
    


class AwaitableGetSapCentralServerInstanceResult(GetSapCentralServerInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetSapCentralServerInstanceResult]:
        ...
    


def get_sap_central_server_instance(central_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sap_virtual_instance_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSapCentralServerInstanceResult:
    
    ...

def get_sap_central_server_instance_output(central_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sap_virtual_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSapCentralServerInstanceResult]:
    
    ...

