

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ReleaseBlueprintArgs', 'ReleaseBlueprintArgsDict', 'ReleaseInputVariableArgs', 'ReleaseInputVariableArgsDict', 'ReleaseInputVariableDefaultArgs', 'ReleaseInputVariableDefaultArgsDict', 'ReleaseOutputVariableArgs', 'ReleaseOutputVariableArgsDict', 'ReleaseReleaseRequirementsArgs', 'ReleaseReleaseRequirementsArgsDict', 'RolloutKindErrorBudgetArgs', 'RolloutKindErrorBudgetArgsDict', 'SaaSLocationArgs', 'SaaSLocationArgsDict', 'UnitConditionArgs', 'UnitConditionArgsDict', 'UnitDependencyArgs', 'UnitDependencyArgsDict', 'UnitDependentArgs', 'UnitDependentArgsDict', 'UnitInputVariableArgs', 'UnitInputVariableArgsDict', 'UnitKindDependencyArgs', 'UnitKindDependencyArgsDict', 'UnitKindInputVariableMappingArgs', 'UnitKindInputVariableMappingArgsDict', 'UnitKindInputVariableMappingFromArgs', 'UnitKindInputVariableMappingFromArgsDict', 'UnitKindInputVariableMappingToArgs', 'UnitKindInputVariableMappingToArgsDict', 'UnitKindOutputVariableMappingArgs', 'UnitKindOutputVariableMappingArgsDict', 'UnitKindOutputVariableMappingFromArgs', 'UnitKindOutputVariableMappingFromArgsDict', 'UnitKindOutputVariableMappingToArgs', 'UnitKindOutputVariableMappingToArgsDict', 'UnitMaintenanceArgs', 'UnitMaintenanceArgsDict', 'UnitOperationConditionArgs', 'UnitOperationConditionArgsDict', 'UnitOperationDeprovisionArgs', 'UnitOperationDeprovisionArgsDict', 'UnitOperationProvisionArgs', 'UnitOperationProvisionArgsDict', 'UnitOperationProvisionInputVariableArgs', 'UnitOperationProvisionInputVariableArgsDict', 'UnitOperationUpgradeArgs', 'UnitOperationUpgradeArgsDict', 'UnitOperationUpgradeInputVariableArgs', 'UnitOperationUpgradeInputVariableArgsDict', 'UnitOutputVariableArgs', 'UnitOutputVariableArgsDict']
class ReleaseBlueprintArgsDict(TypedDict):
    engine: NotRequired[pulumi.Input[_builtins.str]]
    package: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReleaseBlueprintArgs:
    def __init__(__self__, *, engine: Optional[pulumi.Input[_builtins.str]] = ..., package: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def package(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package.setter
    def package(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReleaseInputVariableArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReleaseInputVariableArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReleaseInputVariableDefaultArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReleaseInputVariableDefaultArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReleaseOutputVariableArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ReleaseOutputVariableArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReleaseReleaseRequirementsArgsDict(TypedDict):
    upgradeable_from_releases: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ReleaseReleaseRequirementsArgs:
    def __init__(__self__, *, upgradeable_from_releases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeableFromReleases")
    def upgradeable_from_releases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @upgradeable_from_releases.setter
    def upgradeable_from_releases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RolloutKindErrorBudgetArgsDict(TypedDict):
    allowed_count: NotRequired[pulumi.Input[_builtins.int]]
    allowed_percentage: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class RolloutKindErrorBudgetArgs:
    def __init__(__self__, *, allowed_count: Optional[pulumi.Input[_builtins.int]] = ..., allowed_percentage: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedCount")
    def allowed_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allowed_count.setter
    def allowed_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPercentage")
    def allowed_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allowed_percentage.setter
    def allowed_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SaaSLocationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SaaSLocationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitConditionArgsDict(TypedDict):
    last_transition_time: pulumi.Input[_builtins.str]
    message: pulumi.Input[_builtins.str]
    reason: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class UnitConditionArgs:
    def __init__(__self__, *, last_transition_time: pulumi.Input[_builtins.str], message: pulumi.Input[_builtins.str], reason: pulumi.Input[_builtins.str], status: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @last_transition_time.setter
    def last_transition_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message.setter
    def message(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @reason.setter
    def reason(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UnitDependencyArgsDict(TypedDict):
    alias: NotRequired[pulumi.Input[_builtins.str]]
    unit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitDependencyArgs:
    def __init__(__self__, *, alias: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitDependentArgsDict(TypedDict):
    alias: NotRequired[pulumi.Input[_builtins.str]]
    unit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitDependentArgs:
    def __init__(__self__, *, alias: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitInputVariableArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitInputVariableArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitKindDependencyArgsDict(TypedDict):
    alias: pulumi.Input[_builtins.str]
    unit_kind: pulumi.Input[_builtins.str]


@pulumi.input_type
class UnitKindDependencyArgs:
    def __init__(__self__, *, alias: pulumi.Input[_builtins.str], unit_kind: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @alias.setter
    def alias(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @unit_kind.setter
    def unit_kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UnitKindInputVariableMappingArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    from_: NotRequired[pulumi.Input[UnitKindInputVariableMappingFromArgsDict]]
    to: NotRequired[pulumi.Input[UnitKindInputVariableMappingToArgsDict]]


@pulumi.input_type
class UnitKindInputVariableMappingArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], from_: Optional[pulumi.Input[UnitKindInputVariableMappingFromArgs]] = ..., to: Optional[pulumi.Input[UnitKindInputVariableMappingToArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[UnitKindInputVariableMappingFromArgs]]:
        
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[UnitKindInputVariableMappingFromArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[UnitKindInputVariableMappingToArgs]]:
        
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[UnitKindInputVariableMappingToArgs]]): # -> None:
        ...
    


class UnitKindInputVariableMappingFromArgsDict(TypedDict):
    dependency: pulumi.Input[_builtins.str]
    output_variable: pulumi.Input[_builtins.str]


@pulumi.input_type
class UnitKindInputVariableMappingFromArgs:
    def __init__(__self__, *, dependency: pulumi.Input[_builtins.str], output_variable: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dependency.setter
    def dependency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariable")
    def output_variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @output_variable.setter
    def output_variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UnitKindInputVariableMappingToArgsDict(TypedDict):
    dependency: pulumi.Input[_builtins.str]
    input_variable: pulumi.Input[_builtins.str]
    ignore_for_lookup: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class UnitKindInputVariableMappingToArgs:
    def __init__(__self__, *, dependency: pulumi.Input[_builtins.str], input_variable: pulumi.Input[_builtins.str], ignore_for_lookup: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dependency.setter
    def dependency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariable")
    def input_variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @input_variable.setter
    def input_variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreForLookup")
    def ignore_for_lookup(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_for_lookup.setter
    def ignore_for_lookup(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class UnitKindOutputVariableMappingArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    from_: NotRequired[pulumi.Input[UnitKindOutputVariableMappingFromArgsDict]]
    to: NotRequired[pulumi.Input[UnitKindOutputVariableMappingToArgsDict]]


@pulumi.input_type
class UnitKindOutputVariableMappingArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], from_: Optional[pulumi.Input[UnitKindOutputVariableMappingFromArgs]] = ..., to: Optional[pulumi.Input[UnitKindOutputVariableMappingToArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> Optional[pulumi.Input[UnitKindOutputVariableMappingFromArgs]]:
        
        ...
    
    @from_.setter
    def from_(self, value: Optional[pulumi.Input[UnitKindOutputVariableMappingFromArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[UnitKindOutputVariableMappingToArgs]]:
        
        ...
    
    @to.setter
    def to(self, value: Optional[pulumi.Input[UnitKindOutputVariableMappingToArgs]]): # -> None:
        ...
    


class UnitKindOutputVariableMappingFromArgsDict(TypedDict):
    dependency: pulumi.Input[_builtins.str]
    output_variable: pulumi.Input[_builtins.str]


@pulumi.input_type
class UnitKindOutputVariableMappingFromArgs:
    def __init__(__self__, *, dependency: pulumi.Input[_builtins.str], output_variable: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dependency.setter
    def dependency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariable")
    def output_variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @output_variable.setter
    def output_variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UnitKindOutputVariableMappingToArgsDict(TypedDict):
    dependency: pulumi.Input[_builtins.str]
    input_variable: pulumi.Input[_builtins.str]
    ignore_for_lookup: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class UnitKindOutputVariableMappingToArgs:
    def __init__(__self__, *, dependency: pulumi.Input[_builtins.str], input_variable: pulumi.Input[_builtins.str], ignore_for_lookup: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dependency.setter
    def dependency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariable")
    def input_variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @input_variable.setter
    def input_variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreForLookup")
    def ignore_for_lookup(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_for_lookup.setter
    def ignore_for_lookup(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class UnitMaintenanceArgsDict(TypedDict):
    pinned_until_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitMaintenanceArgs:
    def __init__(__self__, *, pinned_until_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pinnedUntilTime")
    def pinned_until_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pinned_until_time.setter
    def pinned_until_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitOperationConditionArgsDict(TypedDict):
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitOperationConditionArgs:
    def __init__(__self__, *, last_transition_time: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ..., reason: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitOperationDeprovisionArgsDict(TypedDict):
    ...


@pulumi.input_type
class UnitOperationDeprovisionArgs:
    def __init__(__self__) -> None:
        ...
    


class UnitOperationProvisionArgsDict(TypedDict):
    input_variables: NotRequired[pulumi.Input[Sequence[pulumi.Input[UnitOperationProvisionInputVariableArgsDict]]]]
    release: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitOperationProvisionArgs:
    def __init__(__self__, *, input_variables: Optional[pulumi.Input[Sequence[pulumi.Input[UnitOperationProvisionInputVariableArgs]]]] = ..., release: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitOperationProvisionInputVariableArgs]]]]:
        
        ...
    
    @input_variables.setter
    def input_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitOperationProvisionInputVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release.setter
    def release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitOperationProvisionInputVariableArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitOperationProvisionInputVariableArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitOperationUpgradeArgsDict(TypedDict):
    input_variables: NotRequired[pulumi.Input[Sequence[pulumi.Input[UnitOperationUpgradeInputVariableArgsDict]]]]
    release: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitOperationUpgradeArgs:
    def __init__(__self__, *, input_variables: Optional[pulumi.Input[Sequence[pulumi.Input[UnitOperationUpgradeInputVariableArgs]]]] = ..., release: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitOperationUpgradeInputVariableArgs]]]]:
        
        ...
    
    @input_variables.setter
    def input_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitOperationUpgradeInputVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release.setter
    def release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitOperationUpgradeInputVariableArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitOperationUpgradeInputVariableArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UnitOutputVariableArgsDict(TypedDict):
    variable: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UnitOutputVariableArgs:
    def __init__(__self__, *, variable: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variable(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable.setter
    def variable(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


