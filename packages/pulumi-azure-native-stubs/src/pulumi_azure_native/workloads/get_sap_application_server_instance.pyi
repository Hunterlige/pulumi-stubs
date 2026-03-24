

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSapApplicationServerInstanceResult', 'AwaitableGetSapApplicationServerInstanceResult', 'get_sap_application_server_instance', 'get_sap_application_server_instance_output']
@pulumi.output_type
class GetSapApplicationServerInstanceResult:
    
    def __init__(__self__, azure_api_version=..., dispatcher_status=..., errors=..., gateway_port=..., health=..., hostname=..., icm_http_port=..., icm_https_port=..., id=..., instance_no=..., ip_address=..., kernel_patch=..., kernel_version=..., load_balancer_details=..., location=..., name=..., provisioning_state=..., status=..., subnet=..., system_data=..., tags=..., type=..., vm_details=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dispatcherStatus")
    def dispatcher_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.SAPVirtualInstanceErrorResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayPort")
    def gateway_port(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmHttpPort")
    def icm_http_port(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icmHttpsPort")
    def icm_https_port(self) -> _builtins.float:
        
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
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
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
    def vm_details(self) -> Sequence[outputs.ApplicationServerVmDetailsResponse]:
        
        ...
    


class AwaitableGetSapApplicationServerInstanceResult(GetSapApplicationServerInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetSapApplicationServerInstanceResult]:
        ...
    


def get_sap_application_server_instance(application_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sap_virtual_instance_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSapApplicationServerInstanceResult:
    
    ...

def get_sap_application_server_instance_output(application_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sap_virtual_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSapApplicationServerInstanceResult]:
    
    ...

