

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAndroidAppConfigResult', 'AwaitableGetAndroidAppConfigResult', 'get_android_app_config', 'get_android_app_config_output']
@pulumi.output_type
class GetAndroidAppConfigResult:
    
    def __init__(__self__, app_id=..., config_file_contents=..., config_filename=..., id=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configFileContents")
    def config_file_contents(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configFilename")
    def config_filename(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetAndroidAppConfigResult(GetAndroidAppConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetAndroidAppConfigResult]:
        ...
    


def get_android_app_config(app_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAndroidAppConfigResult:
    
    ...

def get_android_app_config_output(app_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAndroidAppConfigResult]:
    
    ...

