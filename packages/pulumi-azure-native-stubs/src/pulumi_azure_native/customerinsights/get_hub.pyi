

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHubResult', 'AwaitableGetHubResult', 'get_hub', 'get_hub_output']
@pulumi.output_type
class GetHubResult:
    
    def __init__(__self__, api_endpoint=..., azure_api_version=..., hub_billing_info=..., id=..., location=..., name=..., provisioning_state=..., tags=..., tenant_features=..., type=..., web_endpoint=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubBillingInfo")
    def hub_billing_info(self) -> Optional[outputs.HubBillingInfoFormatResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
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
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantFeatures")
    def tenant_features(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webEndpoint")
    def web_endpoint(self) -> _builtins.str:
        
        ...
    


class AwaitableGetHubResult(GetHubResult):
    def __await__(self): # -> Generator[Never, Any, GetHubResult]:
        ...
    


def get_hub(hub_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHubResult:
    
    ...

def get_hub_output(hub_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHubResult]:
    
    ...

