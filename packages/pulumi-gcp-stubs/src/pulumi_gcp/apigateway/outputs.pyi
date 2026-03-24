

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApiConfigGatewayConfig', 'ApiConfigGatewayConfigBackendConfig', 'ApiConfigGrpcService', 'ApiConfigGrpcServiceFileDescriptorSet', 'ApiConfigGrpcServiceSource', 'ApiConfigIamBindingCondition', 'ApiConfigIamMemberCondition', 'ApiConfigManagedServiceConfig', 'ApiConfigOpenapiDocument', 'ApiConfigOpenapiDocumentDocument', 'ApiIamBindingCondition', 'ApiIamMemberCondition', 'GatewayIamBindingCondition', 'GatewayIamMemberCondition']
@pulumi.output_type
class ApiConfigGatewayConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backend_config: outputs.ApiConfigGatewayConfigBackendConfig) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendConfig")
    def backend_config(self) -> outputs.ApiConfigGatewayConfigBackendConfig:
        
        ...
    


@pulumi.output_type
class ApiConfigGatewayConfigBackendConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, google_service_account: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleServiceAccount")
    def google_service_account(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiConfigGrpcService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_descriptor_set: outputs.ApiConfigGrpcServiceFileDescriptorSet, sources: Optional[Sequence[outputs.ApiConfigGrpcServiceSource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileDescriptorSet")
    def file_descriptor_set(self) -> outputs.ApiConfigGrpcServiceFileDescriptorSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.ApiConfigGrpcServiceSource]]:
        
        ...
    


@pulumi.output_type
class ApiConfigGrpcServiceFileDescriptorSet(dict):
    def __init__(__self__, *, contents: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contents(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiConfigGrpcServiceSource(dict):
    def __init__(__self__, *, contents: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contents(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiConfigIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ApiConfigIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ApiConfigManagedServiceConfig(dict):
    def __init__(__self__, *, contents: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contents(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiConfigOpenapiDocument(dict):
    def __init__(__self__, *, document: outputs.ApiConfigOpenapiDocumentDocument) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def document(self) -> outputs.ApiConfigOpenapiDocumentDocument:
        
        ...
    


@pulumi.output_type
class ApiConfigOpenapiDocumentDocument(dict):
    def __init__(__self__, *, contents: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def contents(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ApiIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ApiIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class GatewayIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class GatewayIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


