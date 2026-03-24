

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDirectoryResult', 'AwaitableGetDirectoryResult', 'get_directory', 'get_directory_output']
@pulumi.output_type
class GetDirectoryResult:
    
    def __init__(__self__, access_url=..., alias=..., connect_settings=..., description=..., directory_id=..., dns_ip_addresses=..., edition=..., enable_sso=..., id=..., name=..., radius_settings=..., region=..., security_group_id=..., short_name=..., size=..., tags=..., type=..., vpc_settings=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessUrl")
    def access_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectSettings")
    def connect_settings(self) -> Sequence[outputs.GetDirectoryConnectSettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSso")
    def enable_sso(self) -> _builtins.bool:
        
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
    @pulumi.getter(name="radiusSettings")
    def radius_settings(self) -> Sequence[outputs.GetDirectoryRadiusSettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSettings")
    def vpc_settings(self) -> Sequence[outputs.GetDirectoryVpcSettingResult]:
        ...
    


class AwaitableGetDirectoryResult(GetDirectoryResult):
    def __await__(self): # -> Generator[Never, Any, GetDirectoryResult]:
        ...
    


def get_directory(directory_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDirectoryResult:
    
    ...

def get_directory_output(directory_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDirectoryResult]:
    
    ...

