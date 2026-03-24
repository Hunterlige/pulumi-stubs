import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "OrganizationAccount",
    "OrganizationNonMasterAccount",
    "OrganizationRoot",
    "OrganizationRootPolicyType",
    "OrganizationalUnitAccount",
    ...,
    "GetDelegatedServicesDelegatedServiceResult",
    "GetOrganizationAccountResult",
    "GetOrganizationNonMasterAccountResult",
    "GetOrganizationRootResult",
    "GetOrganizationRootPolicyTypeResult",
    "GetOrganizationalUnitChildAccountsAccountResult",
    ...,
    ...,
    "GetOrganizationalUnitsChildResult",
]

@pulumi.output_type
class OrganizationAccount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        joined_method: Optional[_builtins.str] = ...,
        joined_timestamp: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationNonMasterAccount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        joined_method: Optional[_builtins.str] = ...,
        joined_timestamp: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationRoot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        policy_types: Optional[Sequence[outputs.OrganizationRootPolicyType]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyTypes")
    def policy_types(
        self,
    ) -> Optional[Sequence[outputs.OrganizationRootPolicyType]]: ...

@pulumi.output_type
class OrganizationRootPolicyType(dict):
    def __init__(
        __self__,
        *,
        status: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OrganizationalUnitAccount(dict):
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetDelegatedAdministratorsDelegatedAdministratorResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        delegation_enabled_date: _builtins.str,
        email: _builtins.str,
        id: _builtins.str,
        joined_method: _builtins.str,
        joined_timestamp: _builtins.str,
        name: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="delegationEnabledDate")
    def delegation_enabled_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetDelegatedServicesDelegatedServiceResult(dict):
    def __init__(
        __self__,
        *,
        delegation_enabled_date: _builtins.str,
        service_principal: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="delegationEnabledDate")
    def delegation_enabled_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationAccountResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        email: _builtins.str,
        id: _builtins.str,
        joined_method: _builtins.str,
        joined_timestamp: _builtins.str,
        name: _builtins.str,
        state: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationNonMasterAccountResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        email: _builtins.str,
        id: _builtins.str,
        joined_method: _builtins.str,
        joined_timestamp: _builtins.str,
        name: _builtins.str,
        state: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationRootResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        policy_types: Sequence[outputs.GetOrganizationRootPolicyTypeResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Sequence[outputs.GetOrganizationRootPolicyTypeResult]: ...

@pulumi.output_type
class GetOrganizationRootPolicyTypeResult(dict):
    def __init__(__self__, *, status: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationalUnitChildAccountsAccountResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        email: _builtins.str,
        id: _builtins.str,
        joined_method: _builtins.str,
        joined_timestamp: _builtins.str,
        name: _builtins.str,
        state: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationalUnitDescendantAccountsAccountResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        email: _builtins.str,
        id: _builtins.str,
        joined_method: _builtins.str,
        joined_timestamp: _builtins.str,
        name: _builtins.str,
        state: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationalUnitDescendantOrganizationalUnitsChildrenResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetOrganizationalUnitsChildResult(dict):
    def __init__(
        __self__, *, arn: _builtins.str, id: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
