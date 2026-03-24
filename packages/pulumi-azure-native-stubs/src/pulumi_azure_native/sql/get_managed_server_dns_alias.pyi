

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedServerDnsAliasResult', 'AwaitableGetManagedServerDnsAliasResult', 'get_managed_server_dns_alias', 'get_managed_server_dns_alias_output']
@pulumi.output_type
class GetManagedServerDnsAliasResult:
    
    def __init__(__self__, azure_api_version=..., azure_dns_record=..., id=..., name=..., public_azure_dns_record=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureDnsRecord")
    def azure_dns_record(self) -> _builtins.str:
        
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
    @pulumi.getter(name="publicAzureDnsRecord")
    def public_azure_dns_record(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagedServerDnsAliasResult(GetManagedServerDnsAliasResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedServerDnsAliasResult]:
        ...
    


def get_managed_server_dns_alias(dns_alias_name: Optional[_builtins.str] = ..., managed_instance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedServerDnsAliasResult:
    
    ...

def get_managed_server_dns_alias_output(dns_alias_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedServerDnsAliasResult]:
    
    ...

