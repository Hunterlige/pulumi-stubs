

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetControlOrganizationIntelligenceConfigResult', ..., 'get_control_organization_intelligence_config', ...]
@pulumi.output_type
class GetControlOrganizationIntelligenceConfigResult:
    
    def __init__(__self__, edition_config=..., effective_intelligence_configs=..., filters=..., id=..., name=..., trial_configs=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="editionConfig")
    def edition_config(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveIntelligenceConfigs")
    def effective_intelligence_configs(self) -> Sequence[outputs.GetControlOrganizationIntelligenceConfigEffectiveIntelligenceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trialConfigs")
    def trial_configs(self) -> Sequence[outputs.GetControlOrganizationIntelligenceConfigTrialConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetControlOrganizationIntelligenceConfigResult(GetControlOrganizationIntelligenceConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetControlOrganizationIntelligenceConfigResult]:
        ...
    


def get_control_organization_intelligence_config(name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetControlOrganizationIntelligenceConfigResult:
    
    ...

def get_control_organization_intelligence_config_output(name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetControlOrganizationIntelligenceConfigResult]:
    
    ...

