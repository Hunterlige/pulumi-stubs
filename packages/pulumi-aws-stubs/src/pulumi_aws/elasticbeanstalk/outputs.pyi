

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationAppversionLifecycle', 'ConfigurationTemplateSetting', 'EnvironmentAllSetting', 'EnvironmentSetting', 'GetApplicationAppversionLifecycleResult']
@pulumi.output_type
class ApplicationAppversionLifecycle(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_role: _builtins.str, delete_source_from_s3: Optional[_builtins.bool] = ..., max_age_in_days: Optional[_builtins.int] = ..., max_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteSourceFromS3")
    def delete_source_from_s3(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeInDays")
    def max_age_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ConfigurationTemplateSetting(dict):
    def __init__(__self__, *, name: _builtins.str, namespace: _builtins.str, value: _builtins.str, resource: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class EnvironmentAllSetting(dict):
    def __init__(__self__, *, name: _builtins.str, namespace: _builtins.str, value: _builtins.str, resource: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class EnvironmentSetting(dict):
    def __init__(__self__, *, name: _builtins.str, namespace: _builtins.str, value: _builtins.str, resource: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class GetApplicationAppversionLifecycleResult(dict):
    def __init__(__self__, *, delete_source_from_s3: _builtins.bool, max_age_in_days: _builtins.int, max_count: _builtins.int, service_role: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteSourceFromS3")
    def delete_source_from_s3(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeInDays")
    def max_age_in_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> _builtins.str:
        
        ...
    


