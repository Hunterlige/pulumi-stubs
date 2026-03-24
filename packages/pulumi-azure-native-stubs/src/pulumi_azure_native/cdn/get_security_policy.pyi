

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecurityPolicyResult', 'AwaitableGetSecurityPolicyResult', 'get_security_policy', 'get_security_policy_output']
@pulumi.output_type
class GetSecurityPolicyResult:
    
    def __init__(__self__, azure_api_version=..., deployment_status=..., id=..., name=..., parameters=..., profile_name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> _builtins.str:
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
    @pulumi.getter
    def parameters(self) -> Optional[outputs.SecurityPolicyWebApplicationFirewallParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSecurityPolicyResult(GetSecurityPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetSecurityPolicyResult]:
        ...
    


def get_security_policy(profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., security_policy_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecurityPolicyResult:
    
    ...

def get_security_policy_output(profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., security_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecurityPolicyResult]:
    
    ...

