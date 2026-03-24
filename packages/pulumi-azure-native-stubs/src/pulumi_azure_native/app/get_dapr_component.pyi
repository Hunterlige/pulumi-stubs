

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDaprComponentResult', 'AwaitableGetDaprComponentResult', 'get_dapr_component', 'get_dapr_component_output']
@pulumi.output_type
class GetDaprComponentResult:
    
    def __init__(__self__, azure_api_version=..., component_type=..., id=..., ignore_errors=..., init_timeout=..., metadata=..., name=..., scopes=..., secret_store_component=..., secrets=..., service_component_bind=..., system_data=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Sequence[outputs.DaprMetadataResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretStoreComponent")
    def secret_store_component(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.SecretResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceComponentBind")
    def service_component_bind(self) -> Optional[Sequence[outputs.DaprComponentServiceBindingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetDaprComponentResult(GetDaprComponentResult):
    def __await__(self): # -> Generator[Never, Any, GetDaprComponentResult]:
        ...
    


def get_dapr_component(component_name: Optional[_builtins.str] = ..., environment_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDaprComponentResult:
    
    ...

def get_dapr_component_output(component_name: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDaprComponentResult]:
    
    ...

