

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDbServersResult', 'AwaitableGetDbServersResult', 'get_db_servers', 'get_db_servers_output']
@pulumi.output_type
class GetDbServersResult:
    
    def __init__(__self__, cloud_exadata_infrastructure=..., db_servers=..., id=..., location=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructure")
    def cloud_exadata_infrastructure(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> Sequence[outputs.GetDbServersDbServerResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetDbServersResult(GetDbServersResult):
    def __await__(self): # -> Generator[Never, Any, GetDbServersResult]:
        ...
    


def get_db_servers(cloud_exadata_infrastructure: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDbServersResult:
    
    ...

def get_db_servers_output(cloud_exadata_infrastructure: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDbServersResult]:
    
    ...

