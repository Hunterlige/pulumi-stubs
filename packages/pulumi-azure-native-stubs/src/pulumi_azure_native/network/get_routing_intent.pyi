

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRoutingIntentResult', 'AwaitableGetRoutingIntentResult', 'get_routing_intent', 'get_routing_intent_output']
@pulumi.output_type
class GetRoutingIntentResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., provisioning_state=..., routing_policies=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingPolicies")
    def routing_policies(self) -> Optional[Sequence[outputs.RoutingPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRoutingIntentResult(GetRoutingIntentResult):
    def __await__(self): # -> Generator[Never, Any, GetRoutingIntentResult]:
        ...
    


def get_routing_intent(resource_group_name: Optional[_builtins.str] = ..., routing_intent_name: Optional[_builtins.str] = ..., virtual_hub_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRoutingIntentResult:
    
    ...

def get_routing_intent_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., routing_intent_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRoutingIntentResult]:
    
    ...

