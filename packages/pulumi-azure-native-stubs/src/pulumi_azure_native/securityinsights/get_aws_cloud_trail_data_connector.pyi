

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAwsCloudTrailDataConnectorResult', 'AwaitableGetAwsCloudTrailDataConnectorResult', 'get_aws_cloud_trail_data_connector', 'get_aws_cloud_trail_data_connector_output']
@pulumi.output_type
class GetAwsCloudTrailDataConnectorResult:
    
    def __init__(__self__, aws_role_arn=..., azure_api_version=..., data_types=..., etag=..., id=..., kind=..., name=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRoleArn")
    def aws_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> outputs.AwsCloudTrailDataConnectorDataTypesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAwsCloudTrailDataConnectorResult(GetAwsCloudTrailDataConnectorResult):
    def __await__(self): # -> Generator[Never, Any, GetAwsCloudTrailDataConnectorResult]:
        ...
    


def get_aws_cloud_trail_data_connector(data_connector_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAwsCloudTrailDataConnectorResult:
    
    ...

def get_aws_cloud_trail_data_connector_output(data_connector_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAwsCloudTrailDataConnectorResult]:
    
    ...

