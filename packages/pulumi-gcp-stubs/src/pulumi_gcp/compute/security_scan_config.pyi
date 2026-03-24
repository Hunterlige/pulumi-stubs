import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityScanConfigArgs", "SecurityScanConfig"]

@pulumi.input_type
class SecurityScanConfigArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        starting_urls: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        authentication: Optional[
            pulumi.Input[SecurityScanConfigAuthenticationArgs]
        ] = ...,
        blacklist_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        export_to_security_command_center: Optional[pulumi.Input[_builtins.str]] = ...,
        max_qps: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[SecurityScanConfigScheduleArgs]] = ...,
        target_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        user_agent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startingUrls")
    def starting_urls(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @starting_urls.setter
    def starting_urls(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> Optional[pulumi.Input[SecurityScanConfigAuthenticationArgs]]: ...
    @authentication.setter
    def authentication(
        self, value: Optional[pulumi.Input[SecurityScanConfigAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="blacklistPatterns")
    def blacklist_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @blacklist_patterns.setter
    def blacklist_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportToSecurityCommandCenter")
    def export_to_security_command_center(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_security_command_center.setter
    def export_to_security_command_center(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxQps")
    def max_qps(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_qps.setter
    def max_qps(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[SecurityScanConfigScheduleArgs]]: ...
    @schedule.setter
    def schedule(
        self, value: Optional[pulumi.Input[SecurityScanConfigScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPlatforms")
    def target_platforms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_platforms.setter
    def target_platforms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_agent.setter
    def user_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SecurityScanConfigState:
    def __init__(
        __self__,
        *,
        authentication: Optional[
            pulumi.Input[SecurityScanConfigAuthenticationArgs]
        ] = ...,
        blacklist_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_security_command_center: Optional[pulumi.Input[_builtins.str]] = ...,
        max_qps: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[SecurityScanConfigScheduleArgs]] = ...,
        starting_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        user_agent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> Optional[pulumi.Input[SecurityScanConfigAuthenticationArgs]]: ...
    @authentication.setter
    def authentication(
        self, value: Optional[pulumi.Input[SecurityScanConfigAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="blacklistPatterns")
    def blacklist_patterns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @blacklist_patterns.setter
    def blacklist_patterns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exportToSecurityCommandCenter")
    def export_to_security_command_center(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_security_command_center.setter
    def export_to_security_command_center(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxQps")
    def max_qps(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_qps.setter
    def max_qps(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[SecurityScanConfigScheduleArgs]]: ...
    @schedule.setter
    def schedule(
        self, value: Optional[pulumi.Input[SecurityScanConfigScheduleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startingUrls")
    def starting_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @starting_urls.setter
    def starting_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPlatforms")
    def target_platforms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_platforms.setter
    def target_platforms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_agent.setter
    def user_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/securityScanConfig:SecurityScanConfig")
class SecurityScanConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authentication: Optional[
            pulumi.Input[
                Union[
                    SecurityScanConfigAuthenticationArgs,
                    SecurityScanConfigAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        blacklist_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_security_command_center: Optional[pulumi.Input[_builtins.str]] = ...,
        max_qps: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[
            pulumi.Input[
                Union[
                    SecurityScanConfigScheduleArgs, SecurityScanConfigScheduleArgsDict
                ]
            ]
        ] = ...,
        starting_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        user_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityScanConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        authentication: Optional[
            pulumi.Input[
                Union[
                    SecurityScanConfigAuthenticationArgs,
                    SecurityScanConfigAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        blacklist_patterns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_security_command_center: Optional[pulumi.Input[_builtins.str]] = ...,
        max_qps: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[
            pulumi.Input[
                Union[
                    SecurityScanConfigScheduleArgs, SecurityScanConfigScheduleArgsDict
                ]
            ]
        ] = ...,
        starting_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        user_agent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecurityScanConfig: ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityScanConfigAuthentication]]: ...
    @_builtins.property
    @pulumi.getter(name="blacklistPatterns")
    def blacklist_patterns(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToSecurityCommandCenter")
    def export_to_security_command_center(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxQps")
    def max_qps(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityScanConfigSchedule]]: ...
    @_builtins.property
    @pulumi.getter(name="startingUrls")
    def starting_urls(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetPlatforms")
    def target_platforms(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
