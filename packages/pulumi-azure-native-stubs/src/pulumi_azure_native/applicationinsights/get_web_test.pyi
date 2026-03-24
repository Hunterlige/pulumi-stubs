

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebTestResult', 'AwaitableGetWebTestResult', 'get_web_test', 'get_web_test_output']
@pulumi.output_type
class GetWebTestResult:
    
    def __init__(__self__, azure_api_version=..., configuration=..., description=..., enabled=..., frequency=..., id=..., kind=..., location=..., locations=..., name=..., provisioning_state=..., request=..., retry_enabled=..., synthetic_monitor_id=..., tags=..., timeout=..., type=..., validation_rules=..., web_test_kind=..., web_test_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[outputs.WebTestPropertiesResponseConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.WebTestGeolocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[outputs.WebTestPropertiesResponseRequest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryEnabled")
    def retry_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syntheticMonitorId")
    def synthetic_monitor_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationRules")
    def validation_rules(self) -> Optional[outputs.WebTestPropertiesResponseValidationRules]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webTestKind")
    def web_test_kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webTestName")
    def web_test_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebTestResult(GetWebTestResult):
    def __await__(self): # -> Generator[Never, Any, GetWebTestResult]:
        ...
    


def get_web_test(resource_group_name: Optional[_builtins.str] = ..., web_test_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebTestResult:
    
    ...

def get_web_test_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., web_test_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebTestResult]:
    
    ...

