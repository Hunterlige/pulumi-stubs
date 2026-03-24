

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BudgetComparisonExpressionResponse', 'BudgetFilterPropertiesResponse', 'BudgetFilterResponse', 'BudgetTimePeriodResponse', 'CurrentSpendResponse', 'ForecastSpendResponse', 'NotificationResponse', 'SystemDataResponse']
@pulumi.output_type
class BudgetComparisonExpressionResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, operator: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BudgetFilterPropertiesResponse(dict):
    
    def __init__(__self__, *, dimensions: Optional[outputs.BudgetComparisonExpressionResponse] = ..., tags: Optional[outputs.BudgetComparisonExpressionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetComparisonExpressionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetComparisonExpressionResponse]:
        
        ...
    


@pulumi.output_type
class BudgetFilterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, and_: Optional[Sequence[outputs.BudgetFilterPropertiesResponse]] = ..., dimensions: Optional[outputs.BudgetComparisonExpressionResponse] = ..., tags: Optional[outputs.BudgetComparisonExpressionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[Sequence[outputs.BudgetFilterPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[outputs.BudgetComparisonExpressionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[outputs.BudgetComparisonExpressionResponse]:
        
        ...
    


@pulumi.output_type
class BudgetTimePeriodResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_date: _builtins.str, end_date: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CurrentSpendResponse(dict):
    
    def __init__(__self__, *, amount: _builtins.float, unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ForecastSpendResponse(dict):
    
    def __init__(__self__, *, amount: _builtins.float, unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amount(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class NotificationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, contact_emails: Sequence[_builtins.str], enabled: _builtins.bool, operator: _builtins.str, threshold: _builtins.float, contact_groups: Optional[Sequence[_builtins.str]] = ..., contact_roles: Optional[Sequence[_builtins.str]] = ..., locale: Optional[_builtins.str] = ..., threshold_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactEmails")
    def contact_emails(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactGroups")
    def contact_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactRoles")
    def contact_roles(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="thresholdType")
    def threshold_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


