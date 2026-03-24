

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ReleaseBlueprint', 'ReleaseInputVariable', 'ReleaseInputVariableDefault', 'ReleaseOutputVariable', 'ReleaseReleaseRequirements', 'RolloutKindErrorBudget', 'SaaSLocation', 'UnitCondition', 'UnitDependency', 'UnitDependent', 'UnitInputVariable', 'UnitKindDependency', 'UnitKindInputVariableMapping', 'UnitKindInputVariableMappingFrom', 'UnitKindInputVariableMappingTo', 'UnitKindOutputVariableMapping', 'UnitKindOutputVariableMappingFrom', 'UnitKindOutputVariableMappingTo', 'UnitMaintenance', 'UnitOperationCondition', 'UnitOperationDeprovision', 'UnitOperationProvision', 'UnitOperationProvisionInputVariable', 'UnitOperationUpgrade', 'UnitOperationUpgradeInputVariable', 'UnitOutputVariable']
@pulumi.output_type
class ReleaseBlueprint(dict):
    def __init__(__self__, *, engine: Optional[_builtins.str] = ..., package: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def package(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReleaseInputVariable(dict):
    def __init__(__self__, *, variable: _builtins.str, type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReleaseInputVariableDefault(dict):
    def __init__(__self__, *, variable: _builtins.str, type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReleaseOutputVariable(dict):
    def __init__(__self__, *, variable: _builtins.str, type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReleaseReleaseRequirements(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, upgradeable_from_releases: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeableFromReleases")
    def upgradeable_from_releases(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RolloutKindErrorBudget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_count: Optional[_builtins.int] = ..., allowed_percentage: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedCount")
    def allowed_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPercentage")
    def allowed_percentage(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SaaSLocation(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: _builtins.str, message: _builtins.str, reason: _builtins.str, status: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UnitDependency(dict):
    def __init__(__self__, *, alias: Optional[_builtins.str] = ..., unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitDependent(dict):
    def __init__(__self__, *, alias: Optional[_builtins.str] = ..., unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitInputVariable(dict):
    def __init__(__self__, *, variable: _builtins.str, type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitKindDependency(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alias: _builtins.str, unit_kind: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UnitKindInputVariableMapping(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, variable: _builtins.str, from_: Optional[outputs.UnitKindInputVariableMappingFrom] = ..., to: Optional[outputs.UnitKindInputVariableMappingTo] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[outputs.UnitKindInputVariableMappingFrom]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[outputs.UnitKindInputVariableMappingTo]:
        
        ...
    


@pulumi.output_type
class UnitKindInputVariableMappingFrom(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dependency: _builtins.str, output_variable: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariable")
    def output_variable(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UnitKindInputVariableMappingTo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dependency: _builtins.str, input_variable: _builtins.str, ignore_for_lookup: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariable")
    def input_variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreForLookup")
    def ignore_for_lookup(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UnitKindOutputVariableMapping(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, variable: _builtins.str, from_: Optional[outputs.UnitKindOutputVariableMappingFrom] = ..., to: Optional[outputs.UnitKindOutputVariableMappingTo] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[outputs.UnitKindOutputVariableMappingFrom]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[outputs.UnitKindOutputVariableMappingTo]:
        
        ...
    


@pulumi.output_type
class UnitKindOutputVariableMappingFrom(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dependency: _builtins.str, output_variable: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariable")
    def output_variable(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UnitKindOutputVariableMappingTo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dependency: _builtins.str, input_variable: _builtins.str, ignore_for_lookup: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariable")
    def input_variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreForLookup")
    def ignore_for_lookup(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class UnitMaintenance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pinned_until_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pinnedUntilTime")
    def pinned_until_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitOperationCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_transition_time: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., reason: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitOperationDeprovision(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class UnitOperationProvision(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_variables: Optional[Sequence[outputs.UnitOperationProvisionInputVariable]] = ..., release: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(self) -> Optional[Sequence[outputs.UnitOperationProvisionInputVariable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def release(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitOperationProvisionInputVariable(dict):
    def __init__(__self__, *, variable: _builtins.str, type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitOperationUpgrade(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, input_variables: Optional[Sequence[outputs.UnitOperationUpgradeInputVariable]] = ..., release: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(self) -> Optional[Sequence[outputs.UnitOperationUpgradeInputVariable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def release(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitOperationUpgradeInputVariable(dict):
    def __init__(__self__, *, variable: _builtins.str, type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UnitOutputVariable(dict):
    def __init__(__self__, *, variable: _builtins.str, type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


