

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebAppSiteBackupsResult', 'AwaitableListWebAppSiteBackupsResult', 'list_web_app_site_backups', 'list_web_app_site_backups_output']
@pulumi.output_type
class ListWebAppSiteBackupsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.BackupItemResponse]:
        
        ...
    


class AwaitableListWebAppSiteBackupsResult(ListWebAppSiteBackupsResult):
    def __await__(self): # -> Generator[Never, Any, ListWebAppSiteBackupsResult]:
        ...
    


def list_web_app_site_backups(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebAppSiteBackupsResult:
    
    ...

def list_web_app_site_backups_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebAppSiteBackupsResult]:
    
    ...

