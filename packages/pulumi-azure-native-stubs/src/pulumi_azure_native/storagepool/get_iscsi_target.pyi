

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIscsiTargetResult', 'AwaitableGetIscsiTargetResult', 'get_iscsi_target', 'get_iscsi_target_output']
@pulumi.output_type
class GetIscsiTargetResult:
    
    def __init__(__self__, acl_mode=..., azure_api_version=..., endpoints=..., id=..., luns=..., managed_by=..., managed_by_extended=..., name=..., port=..., provisioning_state=..., sessions=..., static_acls=..., status=..., system_data=..., target_iqn=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aclMode")
    def acl_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def luns(self) -> Optional[Sequence[outputs.IscsiLunResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sessions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticAcls")
    def static_acls(self) -> Optional[Sequence[outputs.AclResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemMetadataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIscsiTargetResult(GetIscsiTargetResult):
    def __await__(self): # -> Generator[Never, Any, GetIscsiTargetResult]:
        ...
    


def get_iscsi_target(disk_pool_name: Optional[_builtins.str] = ..., iscsi_target_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIscsiTargetResult:
    
    ...

def get_iscsi_target_output(disk_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., iscsi_target_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIscsiTargetResult]:
    
    ...

