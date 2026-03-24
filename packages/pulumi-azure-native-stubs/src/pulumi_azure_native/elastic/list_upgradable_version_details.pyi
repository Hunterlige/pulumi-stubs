

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListUpgradableVersionDetailsResult', 'AwaitableListUpgradableVersionDetailsResult', 'list_upgradable_version_details', 'list_upgradable_version_details_output']
@pulumi.output_type
class ListUpgradableVersionDetailsResult:
    
    def __init__(__self__, current_version=..., upgradable_versions=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradableVersions")
    def upgradable_versions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableListUpgradableVersionDetailsResult(ListUpgradableVersionDetailsResult):
    def __await__(self): # -> Generator[Never, Any, ListUpgradableVersionDetailsResult]:
        ...
    


def list_upgradable_version_details(monitor_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListUpgradableVersionDetailsResult:
    
    ...

def list_upgradable_version_details_output(monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListUpgradableVersionDetailsResult]:
    
    ...

