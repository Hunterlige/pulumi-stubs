

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecurityGatewayApplicationIamPolicyResult', ..., 'get_security_gateway_application_iam_policy', 'get_security_gateway_application_iam_policy_output']
@pulumi.output_type
class GetSecurityGatewayApplicationIamPolicyResult:
    
    def __init__(__self__, application_id=..., etag=..., id=..., policy_data=..., project=..., security_gateway_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> _builtins.str:
        ...
    


class AwaitableGetSecurityGatewayApplicationIamPolicyResult(GetSecurityGatewayApplicationIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetSecurityGatewayApplicationIamPolicyResult]:
        ...
    


def get_security_gateway_application_iam_policy(application_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., security_gateway_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecurityGatewayApplicationIamPolicyResult:
    
    ...

def get_security_gateway_application_iam_policy_output(application_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecurityGatewayApplicationIamPolicyResult]:
    
    ...

