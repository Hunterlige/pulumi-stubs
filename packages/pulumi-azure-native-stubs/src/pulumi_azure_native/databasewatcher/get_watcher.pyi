

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWatcherResult', 'AwaitableGetWatcherResult', 'get_watcher', 'get_watcher_output']
@pulumi.output_type
class GetWatcherResult:
    
    def __init__(__self__, azure_api_version=..., datastore=..., default_alert_rule_identity_resource_id=..., id=..., identity=..., location=..., name=..., provisioning_state=..., status=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datastore(self) -> Optional[outputs.DatastoreResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAlertRuleIdentityResourceId")
    def default_alert_rule_identity_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
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
    


class AwaitableGetWatcherResult(GetWatcherResult):
    def __await__(self): # -> Generator[Never, Any, GetWatcherResult]:
        ...
    


def get_watcher(resource_group_name: Optional[_builtins.str] = ..., watcher_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWatcherResult:
    
    ...

def get_watcher_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., watcher_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWatcherResult]:
    
    ...

