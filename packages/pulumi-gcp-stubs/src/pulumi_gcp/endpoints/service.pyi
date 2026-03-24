

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
__all__ = ['ServiceArgs', 'Service']
@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *, service_name: pulumi.Input[_builtins.str], grpc_config: Optional[pulumi.Input[_builtins.str]] = ..., openapi_config: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protoc_output_base64: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcConfig")
    def grpc_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grpc_config.setter
    def grpc_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openapiConfig")
    def openapi_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @openapi_config.setter
    def openapi_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocOutputBase64")
    def protoc_output_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protoc_output_base64.setter
    def protoc_output_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ServiceState:
    def __init__(__self__, *, apis: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceApiArgs]]]] = ..., config_id: Optional[pulumi.Input[_builtins.str]] = ..., dns_address: Optional[pulumi.Input[_builtins.str]] = ..., endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointArgs]]]] = ..., grpc_config: Optional[pulumi.Input[_builtins.str]] = ..., openapi_config: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protoc_output_base64: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def apis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceApiArgs]]]]:
        
        ...
    
    @apis.setter
    def apis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceApiArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config_id.setter
    def config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsAddress")
    def dns_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_address.setter
    def dns_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointArgs]]]]:
        
        ...
    
    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcConfig")
    def grpc_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @grpc_config.setter
    def grpc_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openapiConfig")
    def openapi_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @openapi_config.setter
    def openapi_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocOutputBase64")
    def protoc_output_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protoc_output_base64.setter
    def protoc_output_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:endpoints/service:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., grpc_config: Optional[pulumi.Input[_builtins.str]] = ..., openapi_config: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protoc_output_base64: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., apis: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceApiArgs, ServiceApiArgsDict]]]]] = ..., config_id: Optional[pulumi.Input[_builtins.str]] = ..., dns_address: Optional[pulumi.Input[_builtins.str]] = ..., endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ServiceEndpointArgs, ServiceEndpointArgsDict]]]]] = ..., grpc_config: Optional[pulumi.Input[_builtins.str]] = ..., openapi_config: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., protoc_output_base64: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> Service:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def apis(self) -> pulumi.Output[Sequence[outputs.ServiceApi]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsAddress")
    def dns_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence[outputs.ServiceEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcConfig")
    def grpc_config(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openapiConfig")
    def openapi_config(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocOutputBase64")
    def protoc_output_base64(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


