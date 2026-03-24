

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetKustoPoolPrincipalAssignmentResult', 'AwaitableGetKustoPoolPrincipalAssignmentResult', 'get_kusto_pool_principal_assignment', 'get_kusto_pool_principal_assignment_output']
@pulumi.output_type
class GetKustoPoolPrincipalAssignmentResult:
    
    def __init__(__self__, aad_object_id=..., azure_api_version=..., id=..., name=..., principal_id=..., principal_name=..., principal_type=..., provisioning_state=..., role=..., system_data=..., tenant_id=..., tenant_name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadObjectId")
    def aad_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetKustoPoolPrincipalAssignmentResult(GetKustoPoolPrincipalAssignmentResult):
    def __await__(self): # -> Generator[Never, Any, GetKustoPoolPrincipalAssignmentResult]:
        ...
    


def get_kusto_pool_principal_assignment(kusto_pool_name: Optional[_builtins.str] = ..., principal_assignment_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetKustoPoolPrincipalAssignmentResult:
    
    ...

def get_kusto_pool_principal_assignment_output(kusto_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., principal_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetKustoPoolPrincipalAssignmentResult]:
    
    ...

