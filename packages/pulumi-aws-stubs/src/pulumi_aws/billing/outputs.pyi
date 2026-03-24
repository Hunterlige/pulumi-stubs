

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ViewDataFilterExpression', 'ViewDataFilterExpressionDimensions', 'ViewDataFilterExpressionTag', 'ViewDataFilterExpressionTimeRange', 'ViewTimeouts', 'GetViewsBillingViewResult']
@pulumi.output_type
class ViewDataFilterExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dimensions: Optional[outputs.ViewDataFilterExpressionDimensions] = ..., tags: Optional[Sequence[outputs.ViewDataFilterExpressionTag]] = ..., time_range: Optional[outputs.ViewDataFilterExpressionTimeRange] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.ViewDataFilterExpressionDimensions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[outputs.ViewDataFilterExpressionTag]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[outputs.ViewDataFilterExpressionTimeRange]:
        
        ...
    


@pulumi.output_type
class ViewDataFilterExpressionDimensions(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ViewDataFilterExpressionTag(dict):
    def __init__(__self__, *, key: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ViewDataFilterExpressionTimeRange(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, begin_date_inclusive: _builtins.str, end_date_inclusive: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beginDateInclusive")
    def begin_date_inclusive(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDateInclusive")
    def end_date_inclusive(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ViewTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetViewsBillingViewResult(dict):
    def __init__(__self__, *, arn: _builtins.str, billing_view_type: _builtins.str, description: _builtins.str, name: _builtins.str, owner_account_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingViewType")
    def billing_view_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> _builtins.str:
        
        ...
    


