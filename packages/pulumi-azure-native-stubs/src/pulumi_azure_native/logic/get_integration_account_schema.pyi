

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIntegrationAccountSchemaResult', 'AwaitableGetIntegrationAccountSchemaResult', 'get_integration_account_schema', 'get_integration_account_schema_output']
@pulumi.output_type
class GetIntegrationAccountSchemaResult:
    
    def __init__(__self__, azure_api_version=..., changed_time=..., content=..., content_link=..., content_type=..., created_time=..., document_name=..., file_name=..., id=..., location=..., metadata=..., name=..., schema_type=..., tags=..., target_namespace=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> outputs.ContentLinkResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentName")
    def document_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIntegrationAccountSchemaResult(GetIntegrationAccountSchemaResult):
    def __await__(self): # -> Generator[Never, Any, GetIntegrationAccountSchemaResult]:
        ...
    


def get_integration_account_schema(integration_account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., schema_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIntegrationAccountSchemaResult:
    
    ...

def get_integration_account_schema_output(integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIntegrationAccountSchemaResult]:
    
    ...

