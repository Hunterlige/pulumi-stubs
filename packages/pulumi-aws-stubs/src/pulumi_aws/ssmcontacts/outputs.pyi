

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ContactChannelDeliveryAddress', 'PlanStage', 'PlanStageTarget', 'PlanStageTargetChannelTargetInfo', 'PlanStageTargetContactTargetInfo', 'GetContactChannelDeliveryAddressResult', 'GetPlanStageResult', 'GetPlanStageTargetResult', 'GetPlanStageTargetChannelTargetInfoResult', 'GetPlanStageTargetContactTargetInfoResult']
@pulumi.output_type
class ContactChannelDeliveryAddress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, simple_address: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="simpleAddress")
    def simple_address(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PlanStage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, duration_in_minutes: _builtins.int, targets: Optional[Sequence[outputs.PlanStageTarget]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInMinutes")
    def duration_in_minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[Sequence[outputs.PlanStageTarget]]:
        
        ...
    


@pulumi.output_type
class PlanStageTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_target_info: Optional[outputs.PlanStageTargetChannelTargetInfo] = ..., contact_target_info: Optional[outputs.PlanStageTargetContactTargetInfo] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelTargetInfo")
    def channel_target_info(self) -> Optional[outputs.PlanStageTargetChannelTargetInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactTargetInfo")
    def contact_target_info(self) -> Optional[outputs.PlanStageTargetContactTargetInfo]:
        
        ...
    


@pulumi.output_type
class PlanStageTargetChannelTargetInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contact_channel_id: _builtins.str, retry_interval_in_minutes: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactChannelId")
    def contact_channel_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryIntervalInMinutes")
    def retry_interval_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PlanStageTargetContactTargetInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_essential: _builtins.bool, contact_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEssential")
    def is_essential(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetContactChannelDeliveryAddressResult(dict):
    def __init__(__self__, *, simple_address: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="simpleAddress")
    def simple_address(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetPlanStageResult(dict):
    def __init__(__self__, *, duration_in_minutes: _builtins.int, targets: Sequence[outputs.GetPlanStageTargetResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationInMinutes")
    def duration_in_minutes(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Sequence[outputs.GetPlanStageTargetResult]:
        ...
    


@pulumi.output_type
class GetPlanStageTargetResult(dict):
    def __init__(__self__, *, channel_target_infos: Sequence[outputs.GetPlanStageTargetChannelTargetInfoResult], contact_target_infos: Sequence[outputs.GetPlanStageTargetContactTargetInfoResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelTargetInfos")
    def channel_target_infos(self) -> Sequence[outputs.GetPlanStageTargetChannelTargetInfoResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactTargetInfos")
    def contact_target_infos(self) -> Sequence[outputs.GetPlanStageTargetContactTargetInfoResult]:
        ...
    


@pulumi.output_type
class GetPlanStageTargetChannelTargetInfoResult(dict):
    def __init__(__self__, *, contact_channel_id: _builtins.str, retry_interval_in_minutes: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactChannelId")
    def contact_channel_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryIntervalInMinutes")
    def retry_interval_in_minutes(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class GetPlanStageTargetContactTargetInfoResult(dict):
    def __init__(__self__, *, contact_id: _builtins.str, is_essential: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEssential")
    def is_essential(self) -> _builtins.bool:
        ...
    


