

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiConfigArgs', 'ApiConfig']
@pulumi.input_type
class ApiConfigArgs:
    def __init__(__self__, *, api: pulumi.Input[_builtins.str], api_config_id: Optional[pulumi.Input[_builtins.str]] = ..., api_config_id_prefix: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., gateway_config: Optional[pulumi.Input[ApiConfigGatewayConfigArgs]] = ..., grpc_services: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., managed_service_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigManagedServiceConfigArgs]]]] = ..., openapi_documents: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigOpenapiDocumentArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def api(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api.setter
    def api(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfigId")
    def api_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_config_id.setter
    def api_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfigIdPrefix")
    def api_config_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_config_id_prefix.setter
    def api_config_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayConfig")
    def gateway_config(self) -> Optional[pulumi.Input[ApiConfigGatewayConfigArgs]]:
        
        ...
    
    @gateway_config.setter
    def gateway_config(self, value: Optional[pulumi.Input[ApiConfigGatewayConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcServices")
    def grpc_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceArgs]]]]:
        
        ...
    
    @grpc_services.setter
    def grpc_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServiceConfigs")
    def managed_service_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigManagedServiceConfigArgs]]]]:
        
        ...
    
    @managed_service_configs.setter
    def managed_service_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigManagedServiceConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openapiDocuments")
    def openapi_documents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigOpenapiDocumentArgs]]]]:
        
        ...
    
    @openapi_documents.setter
    def openapi_documents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigOpenapiDocumentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ApiConfigState:
    def __init__(__self__, *, api: Optional[pulumi.Input[_builtins.str]] = ..., api_config_id: Optional[pulumi.Input[_builtins.str]] = ..., api_config_id_prefix: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gateway_config: Optional[pulumi.Input[ApiConfigGatewayConfigArgs]] = ..., grpc_services: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., managed_service_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigManagedServiceConfigArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., openapi_documents: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigOpenapiDocumentArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., service_config_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api.setter
    def api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfigId")
    def api_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_config_id.setter
    def api_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfigIdPrefix")
    def api_config_id_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_config_id_prefix.setter
    def api_config_id_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayConfig")
    def gateway_config(self) -> Optional[pulumi.Input[ApiConfigGatewayConfigArgs]]:
        
        ...
    
    @gateway_config.setter
    def gateway_config(self, value: Optional[pulumi.Input[ApiConfigGatewayConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcServices")
    def grpc_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceArgs]]]]:
        
        ...
    
    @grpc_services.setter
    def grpc_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigGrpcServiceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServiceConfigs")
    def managed_service_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigManagedServiceConfigArgs]]]]:
        
        ...
    
    @managed_service_configs.setter
    def managed_service_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigManagedServiceConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openapiDocuments")
    def openapi_documents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigOpenapiDocumentArgs]]]]:
        
        ...
    
    @openapi_documents.setter
    def openapi_documents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiConfigOpenapiDocumentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConfigId")
    def service_config_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_config_id.setter
    def service_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigateway/apiConfig:ApiConfig")
class ApiConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., api: Optional[pulumi.Input[_builtins.str]] = ..., api_config_id: Optional[pulumi.Input[_builtins.str]] = ..., api_config_id_prefix: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., gateway_config: Optional[pulumi.Input[Union[ApiConfigGatewayConfigArgs, ApiConfigGatewayConfigArgsDict]]] = ..., grpc_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApiConfigGrpcServiceArgs, ApiConfigGrpcServiceArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., managed_service_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApiConfigManagedServiceConfigArgs, ApiConfigManagedServiceConfigArgsDict]]]]] = ..., openapi_documents: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApiConfigOpenapiDocumentArgs, ApiConfigOpenapiDocumentArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApiConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., api: Optional[pulumi.Input[_builtins.str]] = ..., api_config_id: Optional[pulumi.Input[_builtins.str]] = ..., api_config_id_prefix: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gateway_config: Optional[pulumi.Input[Union[ApiConfigGatewayConfigArgs, ApiConfigGatewayConfigArgsDict]]] = ..., grpc_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApiConfigGrpcServiceArgs, ApiConfigGrpcServiceArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., managed_service_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApiConfigManagedServiceConfigArgs, ApiConfigManagedServiceConfigArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., openapi_documents: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ApiConfigOpenapiDocumentArgs, ApiConfigOpenapiDocumentArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., service_config_id: Optional[pulumi.Input[_builtins.str]] = ...) -> ApiConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def api(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfigId")
    def api_config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfigIdPrefix")
    def api_config_id_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayConfig")
    def gateway_config(self) -> pulumi.Output[Optional[outputs.ApiConfigGatewayConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcServices")
    def grpc_services(self) -> pulumi.Output[Optional[Sequence[outputs.ApiConfigGrpcService]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServiceConfigs")
    def managed_service_configs(self) -> pulumi.Output[Optional[Sequence[outputs.ApiConfigManagedServiceConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openapiDocuments")
    def openapi_documents(self) -> pulumi.Output[Optional[Sequence[outputs.ApiConfigOpenapiDocument]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceConfigId")
    def service_config_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


