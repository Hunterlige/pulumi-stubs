import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetControlFolderIntelligenceConfigResult",
    "AwaitableGetControlFolderIntelligenceConfigResult",
    "get_control_folder_intelligence_config",
    "get_control_folder_intelligence_config_output",
]

@pulumi.output_type
class GetControlFolderIntelligenceConfigResult:
    def __init__(
        __self__,
        edition_config=...,
        effective_intelligence_configs=...,
        filters=...,
        id=...,
        name=...,
        trial_configs=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="editionConfig")
    def edition_config(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveIntelligenceConfigs")
    def effective_intelligence_configs(
        self,
    ) -> Sequence[
        outputs.GetControlFolderIntelligenceConfigEffectiveIntelligenceConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Sequence[outputs.GetControlFolderIntelligenceConfigFilterResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="trialConfigs")
    def trial_configs(
        self,
    ) -> Sequence[outputs.GetControlFolderIntelligenceConfigTrialConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetControlFolderIntelligenceConfigResult(
    GetControlFolderIntelligenceConfigResult
):
    def __await__(self): ...

def get_control_folder_intelligence_config(
    name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetControlFolderIntelligenceConfigResult: ...
def get_control_folder_intelligence_config_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetControlFolderIntelligenceConfigResult]: ...
