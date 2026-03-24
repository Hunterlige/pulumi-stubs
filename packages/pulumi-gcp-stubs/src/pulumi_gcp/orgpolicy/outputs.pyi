

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyDryRunSpec', 'PolicyDryRunSpecRule', 'PolicyDryRunSpecRuleCondition', 'PolicyDryRunSpecRuleValues', 'PolicySpec', 'PolicySpecRule', 'PolicySpecRuleCondition', 'PolicySpecRuleValues']
@pulumi.output_type
class PolicyDryRunSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: Optional[_builtins.str] = ..., inherit_from_parent: Optional[_builtins.bool] = ..., reset: Optional[_builtins.bool] = ..., rules: Optional[Sequence[outputs.PolicyDryRunSpecRule]] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reset(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.PolicyDryRunSpecRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDryRunSpecRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_all: Optional[_builtins.str] = ..., condition: Optional[outputs.PolicyDryRunSpecRuleCondition] = ..., deny_all: Optional[_builtins.str] = ..., enforce: Optional[_builtins.str] = ..., parameters: Optional[_builtins.str] = ..., values: Optional[outputs.PolicyDryRunSpecRuleValues] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.PolicyDryRunSpecRuleCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[outputs.PolicyDryRunSpecRuleValues]:
        
        ...
    


@pulumi.output_type
class PolicyDryRunSpecRuleCondition(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., expression: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDryRunSpecRuleValues(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_values: Optional[Sequence[_builtins.str]] = ..., denied_values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedValues")
    def denied_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicySpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: Optional[_builtins.str] = ..., inherit_from_parent: Optional[_builtins.bool] = ..., reset: Optional[_builtins.bool] = ..., rules: Optional[Sequence[outputs.PolicySpecRule]] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reset(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.PolicySpecRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicySpecRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_all: Optional[_builtins.str] = ..., condition: Optional[outputs.PolicySpecRuleCondition] = ..., deny_all: Optional[_builtins.str] = ..., enforce: Optional[_builtins.str] = ..., parameters: Optional[_builtins.str] = ..., values: Optional[outputs.PolicySpecRuleValues] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.PolicySpecRuleCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[outputs.PolicySpecRuleValues]:
        
        ...
    


@pulumi.output_type
class PolicySpecRuleCondition(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., expression: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicySpecRuleValues(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_values: Optional[Sequence[_builtins.str]] = ..., denied_values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedValues")
    def denied_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


