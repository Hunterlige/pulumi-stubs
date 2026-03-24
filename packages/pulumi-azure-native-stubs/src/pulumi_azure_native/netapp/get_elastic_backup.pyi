

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetElasticBackupResult', 'AwaitableGetElasticBackupResult', 'get_elastic_backup', 'get_elastic_backup_output']
@pulumi.output_type
class GetElasticBackupResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter
    def properties(self) -> outputs.ElasticBackupPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetElasticBackupResult(GetElasticBackupResult):
    def __await__(self): # -> Generator[Never, Any, GetElasticBackupResult]:
        ...
    


def get_elastic_backup(account_name: Optional[_builtins.str] = ..., backup_name: Optional[_builtins.str] = ..., backup_vault_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetElasticBackupResult:
    
    ...

def get_elastic_backup_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., backup_name: Optional[pulumi.Input[_builtins.str]] = ..., backup_vault_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetElasticBackupResult]:
    
    ...

