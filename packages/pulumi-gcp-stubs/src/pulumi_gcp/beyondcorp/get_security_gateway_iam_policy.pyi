import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityGatewayIamPolicyResult",
    "AwaitableGetSecurityGatewayIamPolicyResult",
    "get_security_gateway_iam_policy",
    "get_security_gateway_iam_policy_output",
]

@pulumi.output_type
class GetSecurityGatewayIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        id=...,
        location=...,
        policy_data=...,
        project=...,
        security_gateway_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGatewayId")
    def security_gateway_id(self) -> _builtins.str: ...

class AwaitableGetSecurityGatewayIamPolicyResult(GetSecurityGatewayIamPolicyResult):
    def __await__(self): ...

def get_security_gateway_iam_policy(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    security_gateway_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityGatewayIamPolicyResult: ...
def get_security_gateway_iam_policy_output(
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    security_gateway_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityGatewayIamPolicyResult]: ...
