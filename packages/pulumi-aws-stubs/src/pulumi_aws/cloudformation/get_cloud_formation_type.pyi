

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudFormationTypeResult', 'AwaitableGetCloudFormationTypeResult', 'get_cloud_formation_type', 'get_cloud_formation_type_output']
@pulumi.output_type
class GetCloudFormationTypeResult:
    
    def __init__(__self__, arn=..., default_version_id=..., deprecated_status=..., description=..., documentation_url=..., execution_role_arn=..., id=..., is_default_version=..., logging_configs=..., provisioning_type=..., region=..., schema=..., source_url=..., type=..., type_arn=..., type_name=..., version_id=..., visibility=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultVersionId")
    def default_version_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deprecatedStatus")
    def deprecated_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfigs")
    def logging_configs(self) -> Sequence[outputs.GetCloudFormationTypeLoggingConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningType")
    def provisioning_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeArn")
    def type_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCloudFormationTypeResult(GetCloudFormationTypeResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudFormationTypeResult]:
        ...
    


def get_cloud_formation_type(arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., type_name: Optional[_builtins.str] = ..., version_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudFormationTypeResult:
    
    ...

def get_cloud_formation_type_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudFormationTypeResult]:
    
    ...

