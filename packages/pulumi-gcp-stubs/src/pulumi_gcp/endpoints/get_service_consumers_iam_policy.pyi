import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceConsumersIamPolicyResult",
    "AwaitableGetServiceConsumersIamPolicyResult",
    "get_service_consumers_iam_policy",
    "get_service_consumers_iam_policy_output",
]

@pulumi.output_type
class GetServiceConsumersIamPolicyResult:
    def __init__(
        __self__,
        consumer_project=...,
        etag=...,
        id=...,
        policy_data=...,
        service_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

class AwaitableGetServiceConsumersIamPolicyResult(GetServiceConsumersIamPolicyResult):
    def __await__(self): ...

def get_service_consumers_iam_policy(
    consumer_project: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceConsumersIamPolicyResult: ...
def get_service_consumers_iam_policy_output(
    consumer_project: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceConsumersIamPolicyResult]: ...
