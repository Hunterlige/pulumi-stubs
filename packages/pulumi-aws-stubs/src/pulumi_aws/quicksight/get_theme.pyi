

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetThemeResult', 'AwaitableGetThemeResult', 'get_theme', 'get_theme_output']
@pulumi.output_type
class GetThemeResult:
    
    def __init__(__self__, arn=..., aws_account_id=..., base_theme_id=..., configurations=..., created_time=..., id=..., last_updated_time=..., name=..., permissions=..., region=..., status=..., tags=..., theme_id=..., version_description=..., version_number=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseThemeId")
    def base_theme_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Sequence[outputs.GetThemeConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[outputs.GetThemePermissionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="themeId")
    def theme_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> _builtins.int:
        
        ...
    


class AwaitableGetThemeResult(GetThemeResult):
    def __await__(self): # -> Generator[Never, Any, GetThemeResult]:
        ...
    


def get_theme(aws_account_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., theme_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetThemeResult:
    
    ...

def get_theme_output(aws_account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., theme_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetThemeResult]:
    
    ...

