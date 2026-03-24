

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCodeSigningConfigResult', 'AwaitableGetCodeSigningConfigResult', 'get_code_signing_config', 'get_code_signing_config_output']
@pulumi.output_type
class GetCodeSigningConfigResult:
    
    def __init__(__self__, allowed_publishers=..., arn=..., config_id=..., description=..., id=..., last_modified=..., policies=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPublishers")
    def allowed_publishers(self) -> Sequence[outputs.GetCodeSigningConfigAllowedPublisherResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Sequence[outputs.GetCodeSigningConfigPolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetCodeSigningConfigResult(GetCodeSigningConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetCodeSigningConfigResult]:
        ...
    


def get_code_signing_config(arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCodeSigningConfigResult:
    
    ...

def get_code_signing_config_output(arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCodeSigningConfigResult]:
    
    ...

