

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LoadTestMappingArgs', 'LoadTestMapping']
@pulumi.input_type
class LoadTestMappingArgs:
    def __init__(__self__, *, resource_uri: pulumi.Input[_builtins.str], azure_load_testing_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., load_test_mapping_name: Optional[pulumi.Input[_builtins.str]] = ..., source_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., test_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLoadTestingResourceId")
    def azure_load_testing_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @azure_load_testing_resource_id.setter
    def azure_load_testing_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadTestMappingName")
    def load_test_mapping_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_test_mapping_name.setter
    def load_test_mapping_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testId")
    def test_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @test_id.setter
    def test_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:loadtestservice:LoadTestMapping")
class LoadTestMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_load_testing_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., load_test_mapping_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., source_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., test_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LoadTestMappingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> LoadTestMapping:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureLoadTestingResourceId")
    def azure_load_testing_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testId")
    def test_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


