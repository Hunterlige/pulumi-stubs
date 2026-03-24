

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEmailTemplateResult', 'AwaitableGetEmailTemplateResult', 'get_email_template', 'get_email_template_output']
@pulumi.output_type
class GetEmailTemplateResult:
    
    def __init__(__self__, azure_api_version=..., body=..., description=..., id=..., is_default=..., name=..., parameters=..., subject=..., title=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.EmailTemplateParametersContractPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEmailTemplateResult(GetEmailTemplateResult):
    def __await__(self): # -> Generator[Never, Any, GetEmailTemplateResult]:
        ...
    


def get_email_template(resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., template_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEmailTemplateResult:
    
    ...

def get_email_template_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., template_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEmailTemplateResult]:
    
    ...

