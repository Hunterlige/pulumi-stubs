

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFileServicePropertiesResult', 'AwaitableGetFileServicePropertiesResult', 'get_file_service_properties', 'get_file_service_properties_output']
@pulumi.output_type
class GetFileServicePropertiesResult:
    
    def __init__(__self__, azure_api_version=..., cors=..., id=..., name=..., protocol_settings=..., share_delete_retention_policy=..., sku=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[outputs.CorsRulesResponse]:
        
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
    @pulumi.getter(name="protocolSettings")
    def protocol_settings(self) -> Optional[outputs.ProtocolSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareDeleteRetentionPolicy")
    def share_delete_retention_policy(self) -> Optional[outputs.DeleteRetentionPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFileServicePropertiesResult(GetFileServicePropertiesResult):
    def __await__(self): # -> Generator[Never, Any, GetFileServicePropertiesResult]:
        ...
    


def get_file_service_properties(account_name: Optional[_builtins.str] = ..., file_services_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFileServicePropertiesResult:
    
    ...

def get_file_service_properties_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., file_services_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFileServicePropertiesResult]:
    
    ...

