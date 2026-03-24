

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiOperationArgs', 'ApiOperation']
@pulumi.input_type
class ApiOperationArgs:
    def __init__(__self__, *, api_id: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], method: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], url_template: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., operation_id: Optional[pulumi.Input[_builtins.str]] = ..., policies: Optional[pulumi.Input[_builtins.str]] = ..., request: Optional[pulumi.Input[RequestContractArgs]] = ..., responses: Optional[pulumi.Input[Sequence[pulumi.Input[ResponseContractArgs]]]] = ..., template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @method.setter
    def method(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @url_template.setter
    def url_template(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @operation_id.setter
    def operation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policies.setter
    def policies(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input[RequestContractArgs]]:
        
        ...
    
    @request.setter
    def request(self, value: Optional[pulumi.Input[RequestContractArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResponseContractArgs]]]]:
        
        ...
    
    @responses.setter
    def responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResponseContractArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]]:
        
        ...
    
    @template_parameters.setter
    def template_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ParameterContractArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:apimanagement:ApiOperation")
class ApiOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., method: Optional[pulumi.Input[_builtins.str]] = ..., operation_id: Optional[pulumi.Input[_builtins.str]] = ..., policies: Optional[pulumi.Input[_builtins.str]] = ..., request: Optional[pulumi.Input[Union[RequestContractArgs, RequestContractArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., responses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResponseContractArgs, ResponseContractArgsDict]]]]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., template_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ParameterContractArgs, ParameterContractArgsDict]]]]] = ..., url_template: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApiOperationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ApiOperation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> pulumi.Output[Optional[outputs.RequestContractResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def responses(self) -> pulumi.Output[Optional[Sequence[outputs.ResponseContractResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateParameters")
    def template_parameters(self) -> pulumi.Output[Optional[Sequence[outputs.ParameterContractResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


