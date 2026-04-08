import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GroupAdditionalGroupKeyArgs",
    "GroupAdditionalGroupKeyArgsDict",
    "GroupGroupKeyArgs",
    "GroupGroupKeyArgsDict",
    "GroupMembershipMemberKeyArgs",
    "GroupMembershipMemberKeyArgsDict",
    "GroupMembershipPreferredMemberKeyArgs",
    "GroupMembershipPreferredMemberKeyArgsDict",
    "GroupMembershipRoleArgs",
    "GroupMembershipRoleArgsDict",
    "GroupMembershipRoleExpiryDetailArgs",
    "GroupMembershipRoleExpiryDetailArgsDict",
    "PolicyPolicyQueryArgs",
    "PolicyPolicyQueryArgsDict",
    "PolicySettingArgs",
    "PolicySettingArgsDict",
    "GetGroupLookupGroupKeyArgs",
    "GetGroupLookupGroupKeyArgsDict",
]

class GroupAdditionalGroupKeyArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupAdditionalGroupKeyArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupGroupKeyArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupGroupKeyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupMembershipMemberKeyArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupMembershipMemberKeyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupMembershipPreferredMemberKeyArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    namespace: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GroupMembershipPreferredMemberKeyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GroupMembershipRoleArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    expiry_detail: NotRequired[pulumi.Input[GroupMembershipRoleExpiryDetailArgsDict]]

@pulumi.input_type
class GroupMembershipRoleArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        expiry_detail: Optional[
            pulumi.Input[GroupMembershipRoleExpiryDetailArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expiryDetail")
    def expiry_detail(
        self,
    ) -> Optional[pulumi.Input[GroupMembershipRoleExpiryDetailArgs]]: ...
    @expiry_detail.setter
    def expiry_detail(
        self, value: Optional[pulumi.Input[GroupMembershipRoleExpiryDetailArgs]]
    ): ...

class GroupMembershipRoleExpiryDetailArgsDict(TypedDict):
    expire_time: pulumi.Input[_builtins.str]

@pulumi.input_type
class GroupMembershipRoleExpiryDetailArgs:
    def __init__(__self__, *, expire_time: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Input[_builtins.str]: ...
    @expire_time.setter
    def expire_time(self, value: pulumi.Input[_builtins.str]): ...

class PolicyPolicyQueryArgsDict(TypedDict):
    org_unit: pulumi.Input[_builtins.str]
    group: NotRequired[pulumi.Input[_builtins.str]]
    query: NotRequired[pulumi.Input[_builtins.str]]
    sort_order: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PolicyPolicyQueryArgs:
    def __init__(
        __self__,
        *,
        org_unit: pulumi.Input[_builtins.str],
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        query: Optional[pulumi.Input[_builtins.str]] = ...,
        sort_order: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="orgUnit")
    def org_unit(self) -> pulumi.Input[_builtins.str]: ...
    @org_unit.setter
    def org_unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sort_order.setter
    def sort_order(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PolicySettingArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value_json: pulumi.Input[_builtins.str]

@pulumi.input_type
class PolicySettingArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        value_json: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueJson")
    def value_json(self) -> pulumi.Input[_builtins.str]: ...
    @value_json.setter
    def value_json(self, value: pulumi.Input[_builtins.str]): ...

class GetGroupLookupGroupKeyArgsDict(TypedDict):
    id: _builtins.str
    namespace: NotRequired[_builtins.str]

@pulumi.input_type
class GetGroupLookupGroupKeyArgs:
    def __init__(
        __self__, *, id: _builtins.str, namespace: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @id.setter
    def id(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: Optional[_builtins.str]): ...
