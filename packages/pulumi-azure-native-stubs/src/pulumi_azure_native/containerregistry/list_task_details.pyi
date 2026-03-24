

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListTaskDetailsResult', 'AwaitableListTaskDetailsResult', 'list_task_details', 'list_task_details_output']
@pulumi.output_type
class ListTaskDetailsResult:
    
    def __init__(__self__, agent_configuration=..., agent_pool_name=..., creation_date=..., credentials=..., id=..., identity=..., is_system_task=..., location=..., log_template=..., name=..., platform=..., provisioning_state=..., status=..., step=..., system_data=..., tags=..., timeout=..., trigger=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(self) -> Optional[outputs.AgentPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentPoolName")
    def agent_pool_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.CredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSystemTask")
    def is_system_task(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logTemplate")
    def log_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[outputs.PlatformPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def step(self) -> Optional[Any]:
        
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
    def timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[outputs.TriggerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableListTaskDetailsResult(ListTaskDetailsResult):
    def __await__(self): # -> Generator[Never, Any, ListTaskDetailsResult]:
        ...
    


def list_task_details(registry_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., task_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListTaskDetailsResult:
    
    ...

def list_task_details_output(registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., task_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListTaskDetailsResult]:
    
    ...

