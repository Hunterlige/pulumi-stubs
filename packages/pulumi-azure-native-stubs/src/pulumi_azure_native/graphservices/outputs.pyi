import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountResourceResponseProperties", "AccountResourceResponseSystemData"]

@pulumi.output_type
class AccountResourceResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_id: _builtins.str,
        billing_plan_id: _builtins.str,
        provisioning_state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingPlanId")
    def billing_plan_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...

@pulumi.output_type
class AccountResourceResponseSystemData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...
