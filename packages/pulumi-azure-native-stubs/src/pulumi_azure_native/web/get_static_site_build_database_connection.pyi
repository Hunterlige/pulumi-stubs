

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStaticSiteBuildDatabaseConnectionResult', ..., 'get_static_site_build_database_connection', 'get_static_site_build_database_connection_output']
@pulumi.output_type
class GetStaticSiteBuildDatabaseConnectionResult:
    
    def __init__(__self__, azure_api_version=..., configuration_files=..., connection_identity=..., connection_string=..., id=..., kind=..., name=..., region=..., resource_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationFiles")
    def configuration_files(self) -> Sequence[outputs.StaticSiteDatabaseConnectionConfigurationFileOverviewResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionIdentity")
    def connection_identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetStaticSiteBuildDatabaseConnectionResult(GetStaticSiteBuildDatabaseConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetStaticSiteBuildDatabaseConnectionResult]:
        ...
    


def get_static_site_build_database_connection(database_connection_name: Optional[_builtins.str] = ..., environment_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStaticSiteBuildDatabaseConnectionResult:
    
    ...

def get_static_site_build_database_connection_output(database_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStaticSiteBuildDatabaseConnectionResult]:
    
    ...

