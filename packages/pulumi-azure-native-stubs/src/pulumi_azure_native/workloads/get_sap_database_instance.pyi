

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSapDatabaseInstanceResult', 'AwaitableGetSapDatabaseInstanceResult', 'get_sap_database_instance', 'get_sap_database_instance_output']
@pulumi.output_type
class GetSapDatabaseInstanceResult:
    
    def __init__(__self__, azure_api_version=..., database_sid=..., database_type=..., errors=..., id=..., ip_address=..., load_balancer_details=..., location=..., name=..., provisioning_state=..., status=..., subnet=..., system_data=..., tags=..., type=..., vm_details=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseSid")
    def database_sid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> outputs.SAPVirtualInstanceErrorResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
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
    def vm_details(self) -> Sequence[outputs.DatabaseVmDetailsResponse]:
        
        ...
    


class AwaitableGetSapDatabaseInstanceResult(GetSapDatabaseInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetSapDatabaseInstanceResult]:
        ...
    


def get_sap_database_instance(database_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sap_virtual_instance_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSapDatabaseInstanceResult:
    
    ...

def get_sap_database_instance_output(database_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sap_virtual_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSapDatabaseInstanceResult]:
    
    ...

