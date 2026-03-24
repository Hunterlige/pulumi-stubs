

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
__all__ = ['DomainArgs', 'Domain']
@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *, endpoint_options: Optional[pulumi.Input[DomainEndpointOptionsArgs]] = ..., index_fields: Optional[pulumi.Input[Sequence[pulumi.Input[DomainIndexFieldArgs]]]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_parameters: Optional[pulumi.Input[DomainScalingParametersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointOptions")
    def endpoint_options(self) -> Optional[pulumi.Input[DomainEndpointOptionsArgs]]:
        
        ...
    
    @endpoint_options.setter
    def endpoint_options(self, value: Optional[pulumi.Input[DomainEndpointOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexFields")
    def index_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainIndexFieldArgs]]]]:
        
        ...
    
    @index_fields.setter
    def index_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainIndexFieldArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingParameters")
    def scaling_parameters(self) -> Optional[pulumi.Input[DomainScalingParametersArgs]]:
        
        ...
    
    @scaling_parameters.setter
    def scaling_parameters(self, value: Optional[pulumi.Input[DomainScalingParametersArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., document_service_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., domain_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_options: Optional[pulumi.Input[DomainEndpointOptionsArgs]] = ..., index_fields: Optional[pulumi.Input[Sequence[pulumi.Input[DomainIndexFieldArgs]]]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_parameters: Optional[pulumi.Input[DomainScalingParametersArgs]] = ..., search_service_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentServiceEndpoint")
    def document_service_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_service_endpoint.setter
    def document_service_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointOptions")
    def endpoint_options(self) -> Optional[pulumi.Input[DomainEndpointOptionsArgs]]:
        
        ...
    
    @endpoint_options.setter
    def endpoint_options(self, value: Optional[pulumi.Input[DomainEndpointOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexFields")
    def index_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DomainIndexFieldArgs]]]]:
        
        ...
    
    @index_fields.setter
    def index_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DomainIndexFieldArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingParameters")
    def scaling_parameters(self) -> Optional[pulumi.Input[DomainScalingParametersArgs]]:
        
        ...
    
    @scaling_parameters.setter
    def scaling_parameters(self, value: Optional[pulumi.Input[DomainScalingParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchServiceEndpoint")
    def search_service_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @search_service_endpoint.setter
    def search_service_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:cloudsearch/domain:Domain")
class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., endpoint_options: Optional[pulumi.Input[Union[DomainEndpointOptionsArgs, DomainEndpointOptionsArgsDict]]] = ..., index_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainIndexFieldArgs, DomainIndexFieldArgsDict]]]]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_parameters: Optional[pulumi.Input[Union[DomainScalingParametersArgs, DomainScalingParametersArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[DomainArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., document_service_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., domain_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_options: Optional[pulumi.Input[Union[DomainEndpointOptionsArgs, DomainEndpointOptionsArgsDict]]] = ..., index_fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DomainIndexFieldArgs, DomainIndexFieldArgsDict]]]]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_parameters: Optional[pulumi.Input[Union[DomainScalingParametersArgs, DomainScalingParametersArgsDict]]] = ..., search_service_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> Domain:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentServiceEndpoint")
    def document_service_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointOptions")
    def endpoint_options(self) -> pulumi.Output[outputs.DomainEndpointOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexFields")
    def index_fields(self) -> pulumi.Output[Optional[Sequence[outputs.DomainIndexField]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingParameters")
    def scaling_parameters(self) -> pulumi.Output[outputs.DomainScalingParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchServiceEndpoint")
    def search_service_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


